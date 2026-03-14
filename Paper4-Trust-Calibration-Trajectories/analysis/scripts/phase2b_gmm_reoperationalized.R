#!/usr/bin/env Rscript
#
# Phase 2B: GMM on re-operationalized variables
#
# Two strategies:
#   Strategy 1: Wide-format R_b + P_adaptive (impute missing with student mean)
#   Strategy 2: Trajectory features (slope, SD, reversals for each variable)
#
# Compares with original Phase 2 (6-class VEE solution)

library(mclust)

cat("============================================================\n")
cat("  Phase 2B: GMM on Re-operationalized Variables\n")
cat("============================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
out_dir <- file.path(base_dir, "analysis/outputs")

# ── Load Phase 1B data ──
ts_path <- file.path(out_dir, "phase1b_timeseries_long.csv")
feat_path <- file.path(out_dir, "phase1b_student_features.csv")

df <- read.csv(ts_path, stringsAsFactors = FALSE)
features <- read.csv(feat_path, stringsAsFactors = FALSE)

cat("Time series:", nrow(df), "rows,", length(unique(df$user_id)), "students\n")
cat("Features:", nrow(features), "students\n\n")

# ── Load original class assignments for comparison ──
orig_assign_path <- file.path(out_dir, "phase2_class_assignments.csv")
orig_assign <- read.csv(orig_assign_path, stringsAsFactors = FALSE)
cat("Original assignments:", nrow(orig_assign), "students,",
    length(unique(orig_assign$class)), "classes\n\n")


# ============================================================
#  STRATEGY 1: Wide-format R_b + P_adaptive
# ============================================================

cat("============================================================\n")
cat("  STRATEGY 1: Wide R_b + P_adaptive (20 features)\n")
cat("============================================================\n\n")

# Convert empty strings to NA
df$P_adaptive[df$P_adaptive == ""] <- NA
df$P_non_adaptive[df$P_non_adaptive == ""] <- NA
df$AI_benefit[df$AI_benefit == ""] <- NA
df$calibration_gap_new[df$calibration_gap_new == ""] <- NA

df$P_adaptive <- as.numeric(df$P_adaptive)
df$P_non_adaptive <- as.numeric(df$P_non_adaptive)
df$AI_benefit <- as.numeric(df$AI_benefit)
df$calibration_gap_new <- as.numeric(df$calibration_gap_new)

# Compute per-student mean P_adaptive for imputation
student_means <- aggregate(P_adaptive ~ user_id, data = df, FUN = mean, na.rm = TRUE)
names(student_means)[2] <- "mean_P_adaptive"

# Count valid windows per student
valid_counts <- aggregate(!is.na(df$P_adaptive) ~ user_id, data = df, FUN = sum)
names(valid_counts) <- c("user_id", "n_valid_P_adaptive")
student_means <- merge(student_means, valid_counts, by = "user_id")

cat("Students with >=7 valid P_adaptive windows:",
    sum(student_means$n_valid_P_adaptive >= 7), "of", nrow(student_means), "\n")
cat("Students with >=5 valid P_adaptive windows:",
    sum(student_means$n_valid_P_adaptive >= 5), "of", nrow(student_means), "\n\n")

# Filter: require >=5 valid P_adaptive windows
valid_students <- student_means$user_id[student_means$n_valid_P_adaptive >= 5]
df_valid <- df[df$user_id %in% valid_students, ]
cat("Using students with >=5 valid windows: N =", length(valid_students), "\n")

# Impute missing P_adaptive with student mean
for (uid in unique(df_valid$user_id)) {
  idx <- which(df_valid$user_id == uid & is.na(df_valid$P_adaptive))
  if (length(idx) > 0) {
    sm <- student_means$mean_P_adaptive[student_means$user_id == uid]
    df_valid$P_adaptive[idx] <- sm
  }
}

# Reshape to wide: R_b + P_adaptive
rb_wide <- reshape(df_valid[, c("user_id", "window", "R_b")],
                   idvar = "user_id", timevar = "window", direction = "wide")
names(rb_wide) <- c("user_id", paste0("Rb_w", 1:10))

pa_wide <- reshape(df_valid[, c("user_id", "window", "P_adaptive")],
                   idvar = "user_id", timevar = "window", direction = "wide")
names(pa_wide) <- c("user_id", paste0("Pa_w", 1:10))

wide1 <- merge(rb_wide, pa_wide, by = "user_id")
cat("Strategy 1 matrix:", nrow(wide1), "x", ncol(wide1)-1, "\n")

# Check for remaining NAs
na_count <- sum(is.na(wide1[,-1]))
cat("Remaining NAs after imputation:", na_count, "\n")

# Remove any rows with remaining NAs
wide1_clean <- wide1[complete.cases(wide1[,-1]), ]
cat("After removing NA rows:", nrow(wide1_clean), "\n\n")

X1 <- as.matrix(wide1_clean[, -1])
rownames(X1) <- wide1_clean$user_id

# Run mclust
cat("--- Running mclust Strategy 1 (1-8 classes) ---\n")
t0 <- Sys.time()
mc1 <- Mclust(X1, G = 1:8, verbose = FALSE)
elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("  Done (%.1fs)\n", elapsed))
cat(sprintf("  Best model: %s with %d classes, BIC=%.1f\n",
            mc1$modelName, mc1$G, mc1$bic))

# BIC comparison
bic1 <- mc1$BIC
best_bic1 <- apply(bic1, 1, max, na.rm = TRUE)
cat("\n  BIC by G:\n")
for (g in 1:min(8, length(best_bic1))) {
  if (!is.finite(best_bic1[g])) next
  marker <- if (g == mc1$G) " <-- BEST" else ""
  cat(sprintf("    G=%d: %.1f%s\n", g, best_bic1[g], marker))
}

# Class sizes
cat("\n  Class sizes:\n")
cls_tab1 <- table(mc1$classification)
for (i in seq_along(cls_tab1)) {
  cat(sprintf("    Class %d: %d (%.1f%%)\n", i, cls_tab1[i],
              cls_tab1[i]/nrow(wide1_clean)*100))
}


# ============================================================
#  STRATEGY 2: Trajectory Features
# ============================================================

cat("\n\n============================================================\n")
cat("  STRATEGY 2: Trajectory Features (multi-dimensional)\n")
cat("============================================================\n\n")

# Select feature columns (numeric trajectory features only)
feat_cols <- c(
  "R_b_slope", "R_b_sd", "R_b_reversals", "R_b_max_drop", "R_b_mean",
  "P_adaptive_slope", "P_adaptive_sd", "P_adaptive_reversals", "P_adaptive_max_drop", "P_adaptive_mean",
  "AI_benefit_slope", "AI_benefit_sd", "AI_benefit_reversals", "AI_benefit_max_drop", "AI_benefit_mean",
  "cal_gap_slope", "cal_gap_sd", "cal_gap_reversals", "cal_gap_max_drop", "cal_gap_mean"
)

# Convert to numeric and filter complete cases
feat_mat <- features[, c("user_id", feat_cols)]
for (col in feat_cols) {
  feat_mat[[col]] <- as.numeric(feat_mat[[col]])
}

feat_complete <- feat_mat[complete.cases(feat_mat[, feat_cols]), ]
cat("Complete cases for trajectory features:", nrow(feat_complete), "\n")

X2 <- as.matrix(feat_complete[, feat_cols])
rownames(X2) <- feat_complete$user_id

# Scale features
X2_scaled <- scale(X2)

cat("--- Running mclust Strategy 2 (1-8 classes, scaled features) ---\n")
t0 <- Sys.time()
mc2 <- Mclust(X2_scaled, G = 1:8, verbose = FALSE)
elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("  Done (%.1fs)\n", elapsed))
cat(sprintf("  Best model: %s with %d classes, BIC=%.1f\n",
            mc2$modelName, mc2$G, mc2$bic))

bic2 <- mc2$BIC
best_bic2 <- apply(bic2, 1, max, na.rm = TRUE)
cat("\n  BIC by G:\n")
for (g in 1:min(8, length(best_bic2))) {
  if (!is.finite(best_bic2[g])) next
  marker <- if (g == mc2$G) " <-- BEST" else ""
  cat(sprintf("    G=%d: %.1f%s\n", g, best_bic2[g], marker))
}

cat("\n  Class sizes:\n")
cls_tab2 <- table(mc2$classification)
for (i in seq_along(cls_tab2)) {
  cat(sprintf("    Class %d: %d (%.1f%%)\n", i, cls_tab2[i],
              cls_tab2[i]/nrow(feat_complete)*100))
}


# ============================================================
#  STRATEGY 3: R_b + P_adaptive + AI_benefit wide (30 features)
# ============================================================

cat("\n\n============================================================\n")
cat("  STRATEGY 3: Wide R_b + P_adaptive + AI_benefit (30 features)\n")
cat("============================================================\n\n")

# Impute AI_benefit similarly
for (uid in unique(df_valid$user_id)) {
  idx <- which(df_valid$user_id == uid & is.na(df_valid$AI_benefit))
  if (length(idx) > 0) {
    vals <- df_valid$AI_benefit[df_valid$user_id == uid & !is.na(df_valid$AI_benefit)]
    if (length(vals) > 0) {
      df_valid$AI_benefit[idx] <- mean(vals)
    }
  }
}

ab_wide <- reshape(df_valid[, c("user_id", "window", "AI_benefit")],
                   idvar = "user_id", timevar = "window", direction = "wide")
names(ab_wide) <- c("user_id", paste0("Ab_w", 1:10))

wide3 <- merge(wide1, ab_wide, by = "user_id")
wide3_clean <- wide3[complete.cases(wide3[,-1]), ]
cat("Strategy 3 matrix:", nrow(wide3_clean), "x", ncol(wide3_clean)-1, "\n")

X3 <- as.matrix(wide3_clean[, -1])
rownames(X3) <- wide3_clean$user_id

cat("--- Running mclust Strategy 3 (1-8 classes) ---\n")
t0 <- Sys.time()
mc3 <- Mclust(X3, G = 1:8, verbose = FALSE)
elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("  Done (%.1fs)\n", elapsed))
cat(sprintf("  Best model: %s with %d classes, BIC=%.1f\n",
            mc3$modelName, mc3$G, mc3$bic))

bic3 <- mc3$BIC
best_bic3 <- apply(bic3, 1, max, na.rm = TRUE)
cat("\n  BIC by G:\n")
for (g in 1:min(8, length(best_bic3))) {
  if (!is.finite(best_bic3[g])) next
  marker <- if (g == mc3$G) " <-- BEST" else ""
  cat(sprintf("    G=%d: %.1f%s\n", g, best_bic3[g], marker))
}

cat("\n  Class sizes:\n")
cls_tab3 <- table(mc3$classification)
for (i in seq_along(cls_tab3)) {
  cat(sprintf("    Class %d: %d (%.1f%%)\n", i, cls_tab3[i],
              cls_tab3[i]/nrow(wide3_clean)*100))
}


# ============================================================
#  COMPARE ALL STRATEGIES: Compute trajectories for best model
# ============================================================

cat("\n\n============================================================\n")
cat("  COMPARISON: Selecting Best Strategy\n")
cat("============================================================\n\n")

# For each strategy, compute the class trajectories using the new variables
compute_trajectories <- function(mc_model, wide_data, ts_data, strategy_name) {
  cat(sprintf("\n--- %s: %s G=%d ---\n", strategy_name, mc_model$modelName, mc_model$G))

  # Map user_id to class
  class_map <- data.frame(
    user_id = rownames(mc_model$z),
    class = mc_model$classification,
    stringsAsFactors = FALSE
  )

  traj_rows <- list()
  for (cls in 1:mc_model$G) {
    members <- class_map$user_id[class_map$class == cls]
    cls_ts <- ts_data[ts_data$user_id %in% members, ]

    for (w in 1:10) {
      w_data <- cls_ts[cls_ts$window == w, ]

      # P_adaptive might have NAs
      pa_vals <- as.numeric(w_data$P_adaptive)
      pn_vals <- as.numeric(w_data$P_non_adaptive)
      ab_vals <- as.numeric(w_data$AI_benefit)
      cg_vals <- as.numeric(w_data$calibration_gap_new)

      traj_rows <- append(traj_rows, list(data.frame(
        class = cls,
        window = w,
        n = length(unique(w_data$user_id)),
        mean_R_b = mean(w_data$R_b, na.rm = TRUE),
        mean_P = mean(as.numeric(w_data$P), na.rm = TRUE),
        mean_P_adaptive = mean(pa_vals, na.rm = TRUE),
        mean_P_non_adaptive = mean(pn_vals, na.rm = TRUE),
        mean_AI_benefit = mean(ab_vals, na.rm = TRUE),
        mean_gap_old = mean(w_data$R_b - as.numeric(w_data$P), na.rm = TRUE),
        mean_gap_new = mean(cg_vals, na.rm = TRUE),
        sd_R_b = sd(w_data$R_b, na.rm = TRUE),
        sd_P_adaptive = sd(pa_vals, na.rm = TRUE)
      )))
    }
  }

  traj_df <- do.call(rbind, traj_rows)

  # Print summary
  N_total <- length(unique(class_map$user_id))
  for (cls in 1:mc_model$G) {
    ct <- traj_df[traj_df$class == cls, ]
    n_m <- ct$n[1]
    pct <- n_m / N_total * 100

    cat(sprintf("\n  Class %d (N=%d, %.1f%%):\n", cls, n_m, pct))
    cat(sprintf("    %-4s %-7s %-7s %-7s %-8s %-8s\n",
                "Win", "R_b", "P_adap", "P_non", "AI_ben", "Gap_new"))
    for (i in 1:nrow(ct)) {
      cat(sprintf("    %-4d %-7.3f %-7.3f %-7.3f %+-8.3f %+-8.3f\n",
                  ct$window[i], ct$mean_R_b[i], ct$mean_P_adaptive[i],
                  ct$mean_P_non_adaptive[i], ct$mean_AI_benefit[i],
                  ct$mean_gap_new[i]))
    }

    # Trajectory features
    rb_first <- ct$mean_R_b[1]
    rb_last <- ct$mean_R_b[10]
    pa_first <- ct$mean_P_adaptive[1]
    pa_last <- ct$mean_P_adaptive[10]
    gn_first <- ct$mean_gap_new[1]
    gn_last <- ct$mean_gap_new[10]
    ab_first <- ct$mean_AI_benefit[1]
    ab_last <- ct$mean_AI_benefit[10]

    cat(sprintf("    Delta: R_b=%+.3f, P_ad=%+.3f, AI_ben=%+.3f, Gap_new=%+.3f\n",
                rb_last - rb_first, pa_last - pa_first,
                ab_last - ab_first, gn_last - gn_first))

    # Non-monotonicity check on gap_new
    gap_series <- ct$mean_gap_new
    reversals <- 0
    for (i in 3:length(gap_series)) {
      d1 <- gap_series[i-1] - gap_series[i-2]
      d2 <- gap_series[i] - gap_series[i-1]
      if ((d1 > 0.001 && d2 < -0.001) || (d1 < -0.001 && d2 > 0.001)) {
        reversals <- reversals + 1
      }
    }
    cat(sprintf("    Gap_new reversals (class-level): %d\n", reversals))
  }

  return(traj_df)
}

# Compute trajectories for each strategy
traj1 <- compute_trajectories(mc1, wide1_clean, df_valid, "Strategy 1 (R_b+P_adaptive)")
traj2_data <- compute_trajectories(mc2, feat_complete, df, "Strategy 2 (Trajectory Features)")
traj3 <- compute_trajectories(mc3, wide3_clean, df_valid, "Strategy 3 (R_b+P_adaptive+AI_benefit)")


# ============================================================
#  ARI comparison with original
# ============================================================

cat("\n\n============================================================\n")
cat("  ARI Comparison with Original 6-class Solution\n")
cat("============================================================\n\n")

# Strategy 1 vs original
common1 <- intersect(wide1_clean$user_id, orig_assign$user_id)
if (length(common1) > 100) {
  orig_cls1 <- orig_assign$class[match(common1, orig_assign$user_id)]
  new_cls1 <- mc1$classification[match(common1, rownames(mc1$z))]
  ari1 <- adjustedRandIndex(orig_cls1, new_cls1)
  cat(sprintf("Strategy 1 vs Original: ARI = %.4f (N=%d overlap)\n", ari1, length(common1)))
}

# Strategy 2 vs original
common2 <- intersect(feat_complete$user_id, orig_assign$user_id)
if (length(common2) > 100) {
  orig_cls2 <- orig_assign$class[match(common2, orig_assign$user_id)]
  new_cls2 <- mc2$classification[match(common2, rownames(mc2$z))]
  ari2 <- adjustedRandIndex(orig_cls2, new_cls2)
  cat(sprintf("Strategy 2 vs Original: ARI = %.4f (N=%d overlap)\n", ari2, length(common2)))
}

# Strategy 3 vs original
common3 <- intersect(wide3_clean$user_id, orig_assign$user_id)
if (length(common3) > 100) {
  orig_cls3 <- orig_assign$class[match(common3, orig_assign$user_id)]
  new_cls3 <- mc3$classification[match(common3, rownames(mc3$z))]
  ari3 <- adjustedRandIndex(orig_cls3, new_cls3)
  cat(sprintf("Strategy 3 vs Original: ARI = %.4f (N=%d overlap)\n", ari3, length(common3)))
}

# Strategy 1 vs Strategy 2
common12 <- intersect(rownames(mc1$z), rownames(mc2$z))
if (length(common12) > 100) {
  cls1_12 <- mc1$classification[match(common12, rownames(mc1$z))]
  cls2_12 <- mc2$classification[match(common12, rownames(mc2$z))]
  ari12 <- adjustedRandIndex(cls1_12, cls2_12)
  cat(sprintf("Strategy 1 vs Strategy 2: ARI = %.4f (N=%d overlap)\n", ari12, length(common12)))
}


# ============================================================
#  CLASSIFICATION QUALITY per strategy
# ============================================================

cat("\n\n============================================================\n")
cat("  Classification Quality\n")
cat("============================================================\n\n")

for (strat_name in c("Strategy 1", "Strategy 2", "Strategy 3")) {
  mc_obj <- switch(strat_name,
    "Strategy 1" = mc1,
    "Strategy 2" = mc2,
    "Strategy 3" = mc3
  )

  avg_pp <- mean(apply(mc_obj$z, 1, max))
  n_gt7 <- sum(apply(mc_obj$z, 1, max) > 0.7)
  n_gt8 <- sum(apply(mc_obj$z, 1, max) > 0.8)

  cat(sprintf("%s (%s, G=%d):\n", strat_name, mc_obj$modelName, mc_obj$G))
  cat(sprintf("  Avg max posterior: %.4f\n", avg_pp))
  cat(sprintf("  > 0.7: %d (%.1f%%)\n", n_gt7, n_gt7/nrow(mc_obj$z)*100))
  cat(sprintf("  > 0.8: %d (%.1f%%)\n", n_gt8, n_gt8/nrow(mc_obj$z)*100))
  cat(sprintf("  Avg uncertainty: %.4f\n\n", mean(mc_obj$uncertainty)))
}


# ============================================================
#  SAVE BEST STRATEGY OUTPUTS
# ============================================================

cat("\n============================================================\n")
cat("  Saving Outputs\n")
cat("============================================================\n\n")

# Save Strategy 1 outputs (R_b + P_adaptive — most directly comparable to original)
assign1 <- data.frame(
  user_id = wide1_clean$user_id,
  class = mc1$classification,
  uncertainty = mc1$uncertainty,
  stringsAsFactors = FALSE
)
pp1 <- mc1$z
colnames(pp1) <- paste0("prob_class", 1:ncol(pp1))
assign1 <- cbind(assign1, pp1)
write.csv(assign1, file.path(out_dir, "phase2b_s1_class_assignments.csv"), row.names = FALSE)
write.csv(traj1, file.path(out_dir, "phase2b_s1_class_trajectories.csv"), row.names = FALSE)
cat("Saved: phase2b_s1_class_assignments.csv\n")
cat("Saved: phase2b_s1_class_trajectories.csv\n")

# Save Strategy 2 outputs (trajectory features)
assign2 <- data.frame(
  user_id = feat_complete$user_id,
  class = mc2$classification,
  uncertainty = mc2$uncertainty,
  stringsAsFactors = FALSE
)
pp2 <- mc2$z
colnames(pp2) <- paste0("prob_class", 1:ncol(pp2))
assign2 <- cbind(assign2, pp2)
write.csv(assign2, file.path(out_dir, "phase2b_s2_class_assignments.csv"), row.names = FALSE)
write.csv(traj2_data, file.path(out_dir, "phase2b_s2_class_trajectories.csv"), row.names = FALSE)
cat("Saved: phase2b_s2_class_assignments.csv\n")
cat("Saved: phase2b_s2_class_trajectories.csv\n")

# Save Strategy 3 outputs (R_b + P_adaptive + AI_benefit)
assign3 <- data.frame(
  user_id = wide3_clean$user_id,
  class = mc3$classification,
  uncertainty = mc3$uncertainty,
  stringsAsFactors = FALSE
)
pp3 <- mc3$z
colnames(pp3) <- paste0("prob_class", 1:ncol(pp3))
assign3 <- cbind(assign3, pp3)
write.csv(assign3, file.path(out_dir, "phase2b_s3_class_assignments.csv"), row.names = FALSE)
write.csv(traj3, file.path(out_dir, "phase2b_s3_class_trajectories.csv"), row.names = FALSE)
cat("Saved: phase2b_s3_class_assignments.csv\n")
cat("Saved: phase2b_s3_class_trajectories.csv\n")

# Save workspace
save(mc1, mc2, mc3, traj1, traj2_data, traj3,
     assign1, assign2, assign3,
     wide1_clean, wide3_clean, feat_complete, df_valid,
     file = file.path(out_dir, "phase2b_workspace.RData"))
cat("Saved: phase2b_workspace.RData\n")

cat("\n============ Phase 2B Complete ============\n")
