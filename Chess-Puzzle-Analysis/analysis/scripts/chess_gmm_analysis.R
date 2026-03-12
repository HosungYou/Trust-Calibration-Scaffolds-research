#!/usr/bin/env Rscript
# =============================================================================
# Chess Puzzle GMM Analysis
# =============================================================================
# Applies Gaussian Mixture Model (mclust) to Chess Puzzle trajectory data
# Bondi et al. (2023) — Independent analysis
#
# Three strategies:
#   S1: Wide-format R_b + AI_accuracy per window (12 features)
#   S2: Trajectory features (slope, SD, reversals, etc.) (scaled)
#   S3: Wide-format R_b + cal_gap + appropriate_reliance (18 features)
# =============================================================================

library(mclust)
library(readr)

cat("================================================================\n")
cat("CHESS PUZZLE GMM ANALYSIS\n")
cat("Bondi et al. (2023)\n")
cat("================================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis"
output_dir <- file.path(base_dir, "analysis", "outputs")

# --- Load data ---
features_df <- read_csv(file.path(output_dir, "chess_participant_features.csv"),
                        show_col_types = FALSE)
window_df <- read_csv(file.path(output_dir, "chess_window_level.csv"),
                      show_col_types = FALSE)

cat("Loaded:", nrow(features_df), "sessions\n")
cat("  C1 (High→Low):", sum(features_df$condition == 1), "\n")
cat("  C2 (Low→High):", sum(features_df$condition == 2), "\n\n")

# =============================================================================
# Strategy 1: Wide-format R_b + AI_accuracy per window
# =============================================================================
cat("--- Strategy 1: Wide R_b + AI_accuracy (12 features) ---\n")

s1_cols <- c(paste0("R_b_w", 1:6), paste0("AI_acc_w", 1:6))
s1_data <- as.data.frame(features_df[, s1_cols])
rownames(s1_data) <- features_df$session_id

# Remove constant columns (AI_accuracy is deterministic per window in this design)
s1_var <- sapply(s1_data, var, na.rm = TRUE)
s1_cols_use <- names(s1_var[s1_var > 0.001])
cat("  Non-constant features:", length(s1_cols_use), "of", length(s1_cols), "\n")

if (length(s1_cols_use) >= 3) {
  s1_fit <- Mclust(s1_data[, s1_cols_use], G = 2:8, verbose = FALSE)
  cat("  Best model:", s1_fit$modelName, "with G =", s1_fit$G, "\n")
  cat("  BIC:", round(max(s1_fit$BIC, na.rm = TRUE), 1), "\n")
  cat("  Avg posterior:", round(mean(apply(s1_fit$z, 1, max)), 3), "\n")

  s1_assign <- data.frame(
    session_id = features_df$session_id,
    participant_id = features_df$participant_id,
    condition = features_df$condition,
    s1_class = s1_fit$classification,
    s1_posterior = round(apply(s1_fit$z, 1, max), 4)
  )
  write_csv(s1_assign, file.path(output_dir, "chess_gmm_s1_assignments.csv"))

  # Class summaries
  cat("\n  Class summaries:\n")
  for (g in sort(unique(s1_fit$classification))) {
    idx <- s1_fit$classification == g
    n <- sum(idx)
    n_c1 <- sum(features_df$condition[idx] == 1)
    n_c2 <- sum(features_df$condition[idx] == 2)
    cat(sprintf("    Class %d: N=%d (C1=%d, C2=%d)\n", g, n, n_c1, n_c2))
  }
} else {
  cat("  SKIPPED: insufficient non-constant features\n")
  s1_fit <- NULL
}

# =============================================================================
# Strategy 2: Trajectory features (scaled)
# =============================================================================
cat("\n--- Strategy 2: Trajectory features (scaled) ---\n")

s2_cols <- c(
  "R_b_slope", "R_b_sd", "R_b_mean", "R_b_range", "R_b_reversals",
  "R_b_max_drop", "R_b_switch_effect", "R_b_switch_jump",
  "cal_gap_slope", "cal_gap_sd", "cal_gap_mean", "cal_gap_range",
  "cal_gap_reversals", "cal_gap_max_drop", "cal_gap_switch_effect", "cal_gap_switch_jump",
  "appropriate_reliance_slope", "appropriate_reliance_sd",
  "appropriate_reliance_mean", "appropriate_reliance_switch_effect"
)
s2_cols_exist <- s2_cols[s2_cols %in% names(features_df)]
s2_data <- scale(as.data.frame(features_df[, s2_cols_exist]))
rownames(s2_data) <- features_df$session_id

cat("  Features:", ncol(s2_data), "\n")

s2_fit <- Mclust(s2_data, G = 2:8, verbose = FALSE)
cat("  Best model:", s2_fit$modelName, "with G =", s2_fit$G, "\n")
cat("  BIC:", round(max(s2_fit$BIC, na.rm = TRUE), 1), "\n")
cat("  Avg posterior:", round(mean(apply(s2_fit$z, 1, max)), 3), "\n")

s2_assign <- data.frame(
  session_id = features_df$session_id,
  participant_id = features_df$participant_id,
  condition = features_df$condition,
  s2_class = s2_fit$classification,
  s2_posterior = round(apply(s2_fit$z, 1, max), 4)
)
write_csv(s2_assign, file.path(output_dir, "chess_gmm_s2_assignments.csv"))

# Class summaries with trajectory info
cat("\n  Class summaries (with trajectories):\n")
for (g in sort(unique(s2_fit$classification))) {
  idx <- s2_fit$classification == g
  n <- sum(idx)
  n_c1 <- sum(features_df$condition[idx] == 1)
  n_c2 <- sum(features_df$condition[idx] == 2)

  sub_w <- window_df[window_df$session_id %in% features_df$session_id[idx], ]
  cat(sprintf("\n    Class %d: N=%d (C1=%d, C2=%d)\n", g, n, n_c1, n_c2))

  for (w in 1:6) {
    ww <- sub_w[sub_w$window == w, ]
    if (nrow(ww) > 0) {
      cat(sprintf("      W%d: R_b=%.3f  AI_acc=%.3f  Gap=%+.3f  Approp=%.3f\n",
                  w, mean(ww$R_b), mean(ww$AI_accuracy),
                  mean(ww$cal_gap), mean(ww$appropriate_reliance)))
    }
  }

  # Trajectory features
  sub_f <- features_df[idx, ]
  cat(sprintf("      Features: gap_slope=%+.4f  gap_sd=%.4f  gap_reversals=%.1f  switch_jump=%+.3f\n",
              mean(sub_f$cal_gap_slope), mean(sub_f$cal_gap_sd),
              mean(sub_f$cal_gap_reversals), mean(sub_f$cal_gap_switch_jump)))
}

# =============================================================================
# Strategy 3: Wide R_b + cal_gap + appropriate_reliance
# =============================================================================
cat("\n--- Strategy 3: Wide R_b + Gap + Appropriate (18 features) ---\n")

s3_cols <- c(paste0("R_b_w", 1:6), paste0("cal_gap_w", 1:6), paste0("approp_w", 1:6))
s3_cols_exist <- s3_cols[s3_cols %in% names(features_df)]
s3_data <- as.data.frame(features_df[, s3_cols_exist])
rownames(s3_data) <- features_df$session_id

# Remove constant columns
s3_var <- sapply(s3_data, var, na.rm = TRUE)
s3_cols_use <- names(s3_var[s3_var > 0.001])
cat("  Non-constant features:", length(s3_cols_use), "of", length(s3_cols_exist), "\n")

if (length(s3_cols_use) >= 3) {
  s3_fit <- Mclust(s3_data[, s3_cols_use], G = 2:8, verbose = FALSE)
  cat("  Best model:", s3_fit$modelName, "with G =", s3_fit$G, "\n")
  cat("  BIC:", round(max(s3_fit$BIC, na.rm = TRUE), 1), "\n")
  cat("  Avg posterior:", round(mean(apply(s3_fit$z, 1, max)), 3), "\n")

  s3_assign <- data.frame(
    session_id = features_df$session_id,
    participant_id = features_df$participant_id,
    condition = features_df$condition,
    s3_class = s3_fit$classification,
    s3_posterior = round(apply(s3_fit$z, 1, max), 4)
  )
  write_csv(s3_assign, file.path(output_dir, "chess_gmm_s3_assignments.csv"))

  cat("\n  Class summaries:\n")
  for (g in sort(unique(s3_fit$classification))) {
    idx <- s3_fit$classification == g
    n <- sum(idx)
    n_c1 <- sum(features_df$condition[idx] == 1)
    n_c2 <- sum(features_df$condition[idx] == 2)

    sub_w <- window_df[window_df$session_id %in% features_df$session_id[idx], ]
    cat(sprintf("\n    Class %d: N=%d (C1=%d, C2=%d)\n", g, n, n_c1, n_c2))
    for (w in 1:6) {
      ww <- sub_w[sub_w$window == w, ]
      if (nrow(ww) > 0) {
        cat(sprintf("      W%d: R_b=%.3f  Gap=%+.3f  Approp=%.3f\n",
                    w, mean(ww$R_b), mean(ww$cal_gap), mean(ww$appropriate_reliance)))
      }
    }
  }
} else {
  cat("  SKIPPED: insufficient non-constant features\n")
  s3_fit <- NULL
}

# =============================================================================
# Cross-strategy comparison
# =============================================================================
if (!is.null(s1_fit)) {
  cat("\n\n--- Cross-Strategy Comparison ---\n")
  if (exists("s2_fit") && !is.null(s2_fit)) {
    ari_12 <- adjustedRandIndex(s1_fit$classification, s2_fit$classification)
    cat(sprintf("  ARI (S1 vs S2): %.3f\n", ari_12))
  }
  if (!is.null(s3_fit)) {
    ari_13 <- adjustedRandIndex(s1_fit$classification, s3_fit$classification)
    ari_23 <- adjustedRandIndex(s2_fit$classification, s3_fit$classification)
    cat(sprintf("  ARI (S1 vs S3): %.3f\n", ari_13))
    cat(sprintf("  ARI (S2 vs S3): %.3f\n", ari_23))
  }
}

# =============================================================================
# Save workspace
# =============================================================================
save.image(file.path(output_dir, "chess_gmm_workspace.RData"))
cat("\n\nSaved workspace to chess_gmm_workspace.RData\n")
cat("Done!\n")
