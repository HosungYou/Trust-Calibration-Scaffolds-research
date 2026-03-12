#!/usr/bin/env Rscript
# =============================================================================
# Chess Puzzle GMM — Condition-Specific Analysis
# =============================================================================
# Runs separate GMM within each condition to identify individual differences
# AFTER removing the dominant condition effect.
#
# Critical for reviewer defense: "Even within the same experimental condition,
# participants diverge into distinct trajectory types."
# =============================================================================

library(mclust)
library(readr)

cat("================================================================\n")
cat("CHESS PUZZLE — CONDITION-SPECIFIC GMM\n")
cat("================================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis"
output_dir <- file.path(base_dir, "analysis", "outputs")

features_df <- read_csv(file.path(output_dir, "chess_participant_features.csv"),
                        show_col_types = FALSE)
window_df <- read_csv(file.path(output_dir, "chess_window_level.csv"),
                      show_col_types = FALSE)

# =============================================================================
# Part 1: C1-Only GMM (High→Low, Trust Violation)
# =============================================================================
cat("\n========================================\n")
cat("CONDITION 1 (High→Low): N=50\n")
cat("========================================\n")

c1_feat <- features_df[features_df$condition == 1, ]
c1_wind <- window_df[window_df$condition == 1, ]

# Strategy A: Trajectory features
c1_cols <- c(
  "R_b_slope", "R_b_sd", "R_b_mean", "R_b_range", "R_b_reversals",
  "R_b_max_drop", "R_b_switch_effect", "R_b_switch_jump",
  "cal_gap_slope", "cal_gap_sd", "cal_gap_mean", "cal_gap_range",
  "cal_gap_reversals", "cal_gap_max_drop", "cal_gap_switch_effect", "cal_gap_switch_jump",
  "appropriate_reliance_slope", "appropriate_reliance_sd",
  "appropriate_reliance_mean", "appropriate_reliance_switch_effect"
)
c1_cols_use <- c1_cols[c1_cols %in% names(c1_feat)]
c1_data <- scale(as.data.frame(c1_feat[, c1_cols_use]))
rownames(c1_data) <- c1_feat$session_id

cat("\n--- C1 Strategy A: Trajectory Features ---\n")
c1_fit_a <- Mclust(c1_data, G = 2:6, verbose = FALSE)
cat("  Model:", c1_fit_a$modelName, "G =", c1_fit_a$G, "\n")
cat("  BIC:", round(max(c1_fit_a$BIC, na.rm = TRUE), 1), "\n")
cat("  Avg posterior:", round(mean(apply(c1_fit_a$z, 1, max)), 3), "\n")

# Class summaries
cat("\n  C1 Class Details:\n")
for (g in sort(unique(c1_fit_a$classification))) {
  idx <- c1_fit_a$classification == g
  n <- sum(idx)
  sub_w <- c1_wind[c1_wind$session_id %in% c1_feat$session_id[idx], ]
  sub_f <- c1_feat[idx, ]

  cat(sprintf("\n  === C1-Class %d (N=%d, %.0f%%) ===\n", g, n, n/nrow(c1_feat)*100))

  for (w in 1:6) {
    ww <- sub_w[sub_w$window == w, ]
    if (nrow(ww) > 0) {
      switch_mark <- ifelse(w == 5, " ◄", "")
      cat(sprintf("    W%d: R_b=%.3f  AI_acc=%.3f  Gap=%+.3f  Approp=%.3f%s\n",
                  w, mean(ww$R_b), mean(ww$AI_accuracy),
                  mean(ww$cal_gap), mean(ww$appropriate_reliance), switch_mark))
    }
  }

  cat(sprintf("    Features: gap_slope=%+.4f  gap_sd=%.4f  gap_rev=%.1f  R_b_switch=%+.3f  gap_jump=%+.3f\n",
              mean(sub_f$cal_gap_slope), mean(sub_f$cal_gap_sd),
              mean(sub_f$cal_gap_reversals),
              mean(sub_f$R_b_switch_effect), mean(sub_f$cal_gap_switch_jump)))

  # Pattern label
  mean_rb_switch <- mean(sub_f$R_b_switch_effect)
  mean_gap_post <- mean(sub_f$cal_gap_post_mean)
  mean_gap_sd <- mean(sub_f$cal_gap_sd)

  if (mean_rb_switch < -0.20 && mean_gap_post < 0.20) {
    cat("    → Pattern: ADAPTIVE REDUCER (Rapid Convergent)\n")
  } else if (mean_rb_switch > -0.10 && mean_gap_post > 0.30) {
    cat("    → Pattern: PERSISTENT OVER-RELIANCE (Catastrophic)\n")
  } else if (mean_gap_sd > 0.30) {
    cat("    → Pattern: OSCILLATING\n")
  } else {
    cat("    → Pattern: INTERMEDIATE\n")
  }
}

# Save C1 assignments
c1_assign <- data.frame(
  session_id = c1_feat$session_id,
  participant_id = c1_feat$participant_id,
  c1_class = c1_fit_a$classification,
  c1_posterior = round(apply(c1_fit_a$z, 1, max), 4)
)
write_csv(c1_assign, file.path(output_dir, "chess_gmm_c1_only_assignments.csv"))

# Strategy B: Wide-format window values
cat("\n--- C1 Strategy B: Wide R_b + Gap per window ---\n")
c1_wide_cols <- c(paste0("R_b_w", 1:6), paste0("cal_gap_w", 1:6))
c1_wide_cols_use <- c1_wide_cols[c1_wide_cols %in% names(c1_feat)]
c1_wide_data <- as.data.frame(c1_feat[, c1_wide_cols_use])

c1_wide_var <- sapply(c1_wide_data, var, na.rm = TRUE)
c1_wide_cols_nonconst <- names(c1_wide_var[c1_wide_var > 0.001])

if (length(c1_wide_cols_nonconst) >= 3) {
  c1_fit_b <- Mclust(c1_wide_data[, c1_wide_cols_nonconst], G = 2:6, verbose = FALSE)
  cat("  Model:", c1_fit_b$modelName, "G =", c1_fit_b$G, "\n")
  cat("  Avg posterior:", round(mean(apply(c1_fit_b$z, 1, max)), 3), "\n")

  # ARI between strategies
  ari_c1 <- adjustedRandIndex(c1_fit_a$classification, c1_fit_b$classification)
  cat("  ARI (A vs B):", round(ari_c1, 3), "\n")
}


# =============================================================================
# Part 2: C2-Only GMM (Low→High, Trust Repair)
# =============================================================================
cat("\n\n========================================\n")
cat("CONDITION 2 (Low→High): N=50\n")
cat("========================================\n")

c2_feat <- features_df[features_df$condition == 2, ]
c2_wind <- window_df[window_df$condition == 2, ]

c2_data <- scale(as.data.frame(c2_feat[, c1_cols_use]))
rownames(c2_data) <- c2_feat$session_id

cat("\n--- C2 Strategy A: Trajectory Features ---\n")
c2_fit_a <- Mclust(c2_data, G = 2:6, verbose = FALSE)
cat("  Model:", c2_fit_a$modelName, "G =", c2_fit_a$G, "\n")
cat("  BIC:", round(max(c2_fit_a$BIC, na.rm = TRUE), 1), "\n")
cat("  Avg posterior:", round(mean(apply(c2_fit_a$z, 1, max)), 3), "\n")

cat("\n  C2 Class Details:\n")
for (g in sort(unique(c2_fit_a$classification))) {
  idx <- c2_fit_a$classification == g
  n <- sum(idx)
  sub_w <- c2_wind[c2_wind$session_id %in% c2_feat$session_id[idx], ]
  sub_f <- c2_feat[idx, ]

  cat(sprintf("\n  === C2-Class %d (N=%d, %.0f%%) ===\n", g, n, n/nrow(c2_feat)*100))

  for (w in 1:6) {
    ww <- sub_w[sub_w$window == w, ]
    if (nrow(ww) > 0) {
      switch_mark <- ifelse(w == 5, " ◄", "")
      cat(sprintf("    W%d: R_b=%.3f  AI_acc=%.3f  Gap=%+.3f  Approp=%.3f%s\n",
                  w, mean(ww$R_b), mean(ww$AI_accuracy),
                  mean(ww$cal_gap), mean(ww$appropriate_reliance), switch_mark))
    }
  }

  cat(sprintf("    Features: gap_slope=%+.4f  gap_sd=%.4f  gap_rev=%.1f  R_b_switch=%+.3f  gap_jump=%+.3f\n",
              mean(sub_f$cal_gap_slope), mean(sub_f$cal_gap_sd),
              mean(sub_f$cal_gap_reversals),
              mean(sub_f$R_b_switch_effect), mean(sub_f$cal_gap_switch_jump)))

  # Pattern label for C2
  mean_rb_post <- mean(sub_f$R_b_post_mean)
  mean_gap_post <- mean(sub_f$cal_gap_post_mean)
  mean_rb_switch <- mean(sub_f$R_b_switch_effect)
  mean_gap_sd <- mean(sub_f$cal_gap_sd)

  if (mean_rb_post > 0.60 && abs(mean_gap_post) < 0.15) {
    cat("    → Pattern: GRADUAL ADAPTOR (Convergent)\n")
  } else if (mean_rb_post < 0.30 && mean_gap_post < -0.40) {
    cat("    → Pattern: PERSISTENT DISTRUST (AI Benefit Emergence)\n")
  } else if (mean_gap_sd > 0.35) {
    cat("    → Pattern: OSCILLATING\n")
  } else if (mean_rb_post > 0.85) {
    cat("    → Pattern: ALWAYS FOLLOW (Extreme Compliance)\n")
  } else {
    cat("    → Pattern: MODERATE ADAPTOR\n")
  }
}

# Save C2 assignments
c2_assign <- data.frame(
  session_id = c2_feat$session_id,
  participant_id = c2_feat$participant_id,
  c2_class = c2_fit_a$classification,
  c2_posterior = round(apply(c2_fit_a$z, 1, max), 4)
)
write_csv(c2_assign, file.path(output_dir, "chess_gmm_c2_only_assignments.csv"))

# C2 Wide format
cat("\n--- C2 Strategy B: Wide R_b + Gap per window ---\n")
c2_wide_data <- as.data.frame(c2_feat[, c1_wide_cols_use])
c2_wide_var <- sapply(c2_wide_data, var, na.rm = TRUE)
c2_wide_cols_nonconst <- names(c2_wide_var[c2_wide_var > 0.001])

if (length(c2_wide_cols_nonconst) >= 3) {
  c2_fit_b <- Mclust(c2_wide_data[, c2_wide_cols_nonconst], G = 2:6, verbose = FALSE)
  cat("  Model:", c2_fit_b$modelName, "G =", c2_fit_b$G, "\n")
  cat("  Avg posterior:", round(mean(apply(c2_fit_b$z, 1, max)), 3), "\n")
  ari_c2 <- adjustedRandIndex(c2_fit_a$classification, c2_fit_b$classification)
  cat("  ARI (A vs B):", round(ari_c2, 3), "\n")
}


# =============================================================================
# Part 3: Cross-Condition Comparison
# =============================================================================
cat("\n\n========================================\n")
cat("CROSS-CONDITION COMPARISON\n")
cat("========================================\n")

cat("\nC1 class distribution:\n")
print(table(c1_fit_a$classification))

cat("\nC2 class distribution:\n")
print(table(c2_fit_a$classification))

# Within-participant consistency
# Same participant did both conditions. Do they show consistent patterns?
cat("\n--- Within-Participant Consistency ---\n")
cat("(Same person in C1 and C2: do they show similar individual traits?)\n\n")

merged <- merge(c1_assign, c2_assign, by = "participant_id")
cat("Participants with both conditions:", nrow(merged), "\n")
cat("\nC1 class × C2 class crosstab:\n")
print(table(C1 = merged$c1_class, C2 = merged$c2_class))


# =============================================================================
# Part 4: Bootstrap Stability (simplified)
# =============================================================================
cat("\n\n========================================\n")
cat("BOOTSTRAP STABILITY CHECK (200 iterations)\n")
cat("========================================\n")

set.seed(42)
n_boot <- 200

# C1 Bootstrap
cat("\n--- C1 Bootstrap ---\n")
c1_boot_G <- numeric(n_boot)
for (b in 1:n_boot) {
  idx <- sample(nrow(c1_data), replace = TRUE)
  tryCatch({
    fit <- Mclust(c1_data[idx, ], G = 2:6, verbose = FALSE)
    c1_boot_G[b] <- fit$G
  }, error = function(e) { c1_boot_G[b] <<- NA })
}
c1_boot_G <- c1_boot_G[!is.na(c1_boot_G)]
cat("  G distribution:", paste(names(table(c1_boot_G)), ":", table(c1_boot_G), collapse = ", "), "\n")
cat("  Modal G:", as.numeric(names(which.max(table(c1_boot_G)))), "\n")
cat("  G = original (", c1_fit_a$G, ") in",
    round(sum(c1_boot_G == c1_fit_a$G) / length(c1_boot_G) * 100, 1), "% of bootstraps\n")

# C2 Bootstrap
cat("\n--- C2 Bootstrap ---\n")
c2_boot_G <- numeric(n_boot)
for (b in 1:n_boot) {
  idx <- sample(nrow(c2_data), replace = TRUE)
  tryCatch({
    fit <- Mclust(c2_data[idx, ], G = 2:6, verbose = FALSE)
    c2_boot_G[b] <- fit$G
  }, error = function(e) { c2_boot_G[b] <<- NA })
}
c2_boot_G <- c2_boot_G[!is.na(c2_boot_G)]
cat("  G distribution:", paste(names(table(c2_boot_G)), ":", table(c2_boot_G), collapse = ", "), "\n")
cat("  Modal G:", as.numeric(names(which.max(table(c2_boot_G)))), "\n")
cat("  G = original (", c2_fit_a$G, ") in",
    round(sum(c2_boot_G == c2_fit_a$G) / length(c2_boot_G) * 100, 1), "% of bootstraps\n")

# =============================================================================
# Part 5: Reproduce Key Bondi 2023 Statistics
# =============================================================================
cat("\n\n========================================\n")
cat("BONDI 2023 REPRODUCTION CHECK\n")
cat("========================================\n")

trial_df <- read_csv(file.path(output_dir, "chess_trial_level.csv"), show_col_types = FALSE)

cat("\n--- Overall Statistics ---\n")
cat("  Total trials:", nrow(trial_df), "\n")
cat("  Participants:", length(unique(trial_df$participant_id)), "\n")
cat("  Sessions:", length(unique(trial_df$session_id)), "\n")

cat("\n--- AI Follow Rate by Condition ---\n")
for (c in 1:2) {
  ct <- trial_df[trial_df$condition == c, ]
  cl <- ifelse(c == 1, "High→Low", "Low→High")
  cat(sprintf("  C%d (%s): overall=%.3f, pre=%.3f, post=%.3f\n",
              c, cl,
              mean(ct$followed_ai),
              mean(ct$followed_ai[ct$phase == "pre_switch"]),
              mean(ct$followed_ai[ct$phase == "post_switch"])))
}

cat("\n--- Performance by Condition ---\n")
for (c in 1:2) {
  ct <- trial_df[trial_df$condition == c, ]
  cl <- ifelse(c == 1, "High→Low", "Low→High")
  cat(sprintf("  C%d (%s): overall=%.3f, pre=%.3f, post=%.3f\n",
              c, cl,
              mean(ct$trial_correct),
              mean(ct$trial_correct[ct$phase == "pre_switch"]),
              mean(ct$trial_correct[ct$phase == "post_switch"])))
}

cat("\n--- Confidence Ratings (mean per condition × phase) ---\n")
for (c in 1:2) {
  cl <- ifelse(c == 1, "High→Low", "Low→High")
  for (ph in c("pre_switch", "post_switch")) {
    ct <- trial_df[trial_df$condition == c & trial_df$phase == ph, ]
    sc <- ct$selfconf[!is.na(ct$selfconf)]
    ac <- ct$aiconf[!is.na(ct$aiconf)]
    cat(sprintf("  C%d %s: selfconf=%.3f, aiconf=%.3f\n",
                c, ph,
                ifelse(length(sc) > 0, mean(sc), NA),
                ifelse(length(ac) > 0, mean(ac), NA)))
  }
}

# Save
save.image(file.path(output_dir, "chess_gmm_by_condition_workspace.RData"))
cat("\n\nDone! All condition-specific analyses complete.\n")
