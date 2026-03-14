#!/usr/bin/env Rscript
#
# Phase 2 (Alternative): GMM via mclust on wide-format trajectories
#
# Approach: reshape to wide (each student = 1 row with 20 features:
#   R_b_w1..R_b_w10, P_w1..P_w10), then cluster with Gaussian mixture.
#
# This avoids lcmm convergence issues while still identifying trajectory types.

library(mclust)

cat("============ Phase 2: GMM (mclust) ============\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
data_path <- file.path(base_dir, "analysis/outputs/phase1_timeseries_long.csv")
out_dir <- file.path(base_dir, "analysis/outputs")

df <- read.csv(data_path, stringsAsFactors = FALSE)
cat("Long format:", nrow(df), "rows,", length(unique(df$user_id)), "students\n")

# ── Reshape to wide ──
# R_b columns
rb_wide <- reshape(df[, c("user_id", "window", "R_b")],
                   idvar = "user_id", timevar = "window",
                   direction = "wide")
names(rb_wide) <- c("user_id", paste0("Rb_w", 1:10))

# P columns
p_wide <- reshape(df[, c("user_id", "window", "P")],
                  idvar = "user_id", timevar = "window",
                  direction = "wide")
names(p_wide) <- c("user_id", paste0("P_w", 1:10))

# Merge
wide <- merge(rb_wide, p_wide, by = "user_id")
cat("Wide format:", nrow(wide), "students x", ncol(wide)-1, "features\n\n")

# Feature matrix (drop user_id)
X <- as.matrix(wide[, -1])
rownames(X) <- wide$user_id

# ── Run mclust (BIC-based model selection, 1-7 classes) ──
cat("--- Running mclust (1-7 classes, all model types) ---\n")
t0 <- Sys.time()

# mclust automatically selects best model type and number of classes via BIC
mc <- Mclust(X, G = 1:7, verbose = FALSE)

elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
cat(sprintf("  Done (%.1fs)\n", elapsed))
cat(sprintf("  Best model: %s with %d classes\n", mc$modelName, mc$G))
cat(sprintf("  BIC: %.1f\n", mc$bic))
cat(sprintf("  LogLik: %.1f\n", mc$loglik))

# Class sizes
cls_table <- table(mc$classification)
cat("\n  Class sizes:\n")
for (i in seq_along(cls_table)) {
  cat(sprintf("    Class %d: %d (%.1f%%)\n", i, cls_table[i],
              cls_table[i] / nrow(wide) * 100))
}

# ── BIC comparison across number of classes ──
cat("\n===== BIC COMPARISON =====\n")
bic_summary <- mc$BIC
# Get the best model type's BIC for each G
best_per_g <- apply(bic_summary, 1, max, na.rm = TRUE)
cat(sprintf("%-4s %-12s\n", "G", "Best BIC"))
for (g in 1:min(7, length(best_per_g))) {
  if (!is.na(best_per_g[g])) {
    cat(sprintf("%-4d %-12.1f\n", g, best_per_g[g]))
  }
}

# ── Also try a focused analysis with VEV and VVV models (flexible) ──
cat("\n--- Focused run (VEV, VVV, EEV models, 2-6 classes) ---\n")
t0 <- Sys.time()
mc2 <- Mclust(X, G = 2:6, modelNames = c("VEV", "VVV", "EEV"), verbose = FALSE)
elapsed2 <- as.numeric(difftime(Sys.time(), t0, units = "secs"))

if (!is.null(mc2)) {
  cat(sprintf("  Done (%.1fs): %s with %d classes, BIC=%.1f\n",
              elapsed2, mc2$modelName, mc2$G, mc2$bic))
} else {
  cat("  No model selected\n")
}

# Use the overall best
final_mc <- if (!is.null(mc2) && mc2$bic > mc$bic) mc2 else mc
cat(sprintf("\nFinal selection: %s, G=%d, BIC=%.1f\n",
            final_mc$modelName, final_mc$G, final_mc$bic))

# ── Save model fit comparison ──
fit_df <- data.frame(
  ng = 1:7,
  best_bic = best_per_g[1:7]
)
write.csv(fit_df, file.path(out_dir, "phase2_model_fit.csv"), row.names = FALSE)
cat("Saved: phase2_model_fit.csv\n")

# ── Save class assignments ──
assignments <- data.frame(
  user_id = wide$user_id,
  class = final_mc$classification,
  uncertainty = final_mc$uncertainty
)

# Add posterior probabilities
pp <- final_mc$z
colnames(pp) <- paste0("prob_class", 1:ncol(pp))
assignments <- cbind(assignments, pp)

write.csv(assignments, file.path(out_dir, "phase2_class_assignments.csv"), row.names = FALSE)
cat(sprintf("Saved: phase2_class_assignments.csv (%d students, %d classes)\n",
            nrow(assignments), final_mc$G))

# ── Compute class trajectories ──
traj_rows <- list()
for (cls in 1:final_mc$G) {
  members <- wide$user_id[final_mc$classification == cls]
  cls_long <- df[df$user_id %in% members, ]

  for (w in 1:10) {
    w_data <- cls_long[cls_long$window == w, ]
    traj_rows <- append(traj_rows, list(data.frame(
      class = cls,
      window = w,
      mean_R_b = mean(w_data$R_b, na.rm = TRUE),
      mean_P = mean(w_data$P, na.rm = TRUE),
      mean_gap = mean(w_data$R_b - w_data$P, na.rm = TRUE),
      sd_R_b = sd(w_data$R_b, na.rm = TRUE),
      sd_P = sd(w_data$P, na.rm = TRUE),
      mean_expl_rate = mean(w_data$expl_rate, na.rm = TRUE),
      n = length(unique(w_data$user_id))
    )))
  }
}

traj_df <- do.call(rbind, traj_rows)
write.csv(traj_df, file.path(out_dir, "phase2_class_trajectories.csv"), row.names = FALSE)
cat("Saved: phase2_class_trajectories.csv\n")

# ── Print trajectories ──
cat("\n===== CLASS TRAJECTORIES =====\n")
N_total <- nrow(wide)
for (cls in 1:final_mc$G) {
  ct <- traj_df[traj_df$class == cls, ]
  n_m <- ct$n[1]
  pct <- n_m / N_total * 100

  cat(sprintf("\nClass %d (N=%d, %.1f%%):\n", cls, n_m, pct))
  cat(sprintf("  %-4s %-8s %-8s %-9s %-8s\n", "Win", "R_b", "P", "Gap", "Expl"))
  for (i in 1:nrow(ct)) {
    cat(sprintf("  %-4d %-8.4f %-8.4f %+-9.4f %-8.4f\n",
                ct$window[i], ct$mean_R_b[i], ct$mean_P[i],
                ct$mean_gap[i], ct$mean_expl_rate[i]))
  }

  # Summary
  cat(sprintf("  Δ R_b: %+.4f | Δ P: %+.4f | Δ Gap: %+.4f\n",
              ct$mean_R_b[10] - ct$mean_R_b[1],
              ct$mean_P[10] - ct$mean_P[1],
              ct$mean_gap[10] - ct$mean_gap[1]))
}

# ── Classification quality ──
cat("\n===== CLASSIFICATION QUALITY =====\n")
cat(sprintf("  Average uncertainty: %.4f\n", mean(final_mc$uncertainty)))
cat(sprintf("  Entropy: %.4f (closer to 1 = better)\n",
            1 - mean(final_mc$uncertainty)))

# Per-class uncertainty
for (cls in 1:final_mc$G) {
  cls_unc <- final_mc$uncertainty[final_mc$classification == cls]
  cat(sprintf("  Class %d uncertainty: mean=%.4f, median=%.4f\n",
              cls, mean(cls_unc), median(cls_unc)))
}

# ── Save workspace ──
save(final_mc, mc, traj_df, assignments, wide, df,
     file = file.path(out_dir, "phase2_workspace.RData"))
cat("\nSaved: phase2_workspace.RData\n")

cat("\n============ Phase 2 Complete ============\n")
