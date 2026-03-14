#!/usr/bin/env Rscript
#
# Phase 4: Sensitivity Analysis for GMM Trajectory Clustering
#
# Validates the Phase 2 result (VEE, G=6, BIC=139,751.3) through:
#   1. Forced class comparison (G=4-7)
#   2. Bootstrap LRT (5v6, 6v7)
#   3. Split-half validation
#   4. Threshold sensitivity (adaptive_ratio 0.15, 0.20)
#   5. Entropy and classification quality metrics
#

library(mclust)

cat("============================================================\n")
cat("  Phase 4: Sensitivity Analysis\n")
cat("============================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
out_dir  <- file.path(base_dir, "analysis/outputs")

# ── Load Phase 2 workspace ──────────────────────────────────────
cat("Loading Phase 2 workspace...\n")
load(file.path(out_dir, "phase2_workspace.RData"))
# Available: final_mc, mc, traj_df, assignments, wide, df

X <- as.matrix(wide[, -1])           # feature matrix (drop user_id)
rownames(X) <- wide$user_id
N <- nrow(X)
cat(sprintf("  Loaded: %d students, %d features, Phase 2 best: %s G=%d BIC=%.1f\n\n",
            N, ncol(X), final_mc$modelName, final_mc$G, final_mc$bic))

# Collectors for output
comparison_rows <- list()
summary_lines   <- character()

add_summary <- function(...) {
  line <- sprintf(...)
  cat(line)
  summary_lines <<- c(summary_lines, line)
}

# ══════════════════════════════════════════════════════════════════
# 1. FORCED CLASS COMPARISON (G = 4-7)
# ══════════════════════════════════════════════════════════════════
add_summary("============================================================\n")
add_summary("  1. Forced Class Comparison (G = 4-7)\n")
add_summary("============================================================\n\n")

compute_entropy <- function(z) {
  # Normalized entropy: 1 = perfect classification, 0 = chance
  N  <- nrow(z)
  G  <- ncol(z)
  ent <- -sum(z * log(pmax(z, 1e-300))) / (N * log(G))
  1 - ent
}

compute_icl <- function(mc_obj) {
  # ICL = BIC - 2 * entropy penalty
  z   <- mc_obj$z
  ent <- -sum(z * log(pmax(z, 1e-300)))
  mc_obj$bic - 2 * ent
}

for (g in 4:7) {
  cat(sprintf("  Fitting G=%d ... ", g))
  t0 <- Sys.time()
  mg <- Mclust(X, G = g, verbose = FALSE)
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))

  if (is.null(mg)) {
    add_summary("  G=%d: model fitting failed\n", g)
    next
  }
  cat(sprintf("%.1fs\n", elapsed))

  cls_tab <- table(mg$classification)
  min_prop <- min(cls_tab) / N

  ent_val <- compute_entropy(mg$z)
  icl_val <- compute_icl(mg)

  # Average posterior probability per class
  avg_pp <- sapply(1:g, function(k) {
    idx <- mg$classification == k
    if (sum(idx) > 0) mean(mg$z[idx, k]) else NA
  })

  comparison_rows[[length(comparison_rows) + 1]] <- data.frame(
    G           = g,
    model       = mg$modelName,
    BIC         = mg$bic,
    loglik      = mg$loglik,
    ICL         = icl_val,
    entropy     = ent_val,
    min_class_n = min(cls_tab),
    min_class_pct = round(min_prop * 100, 2),
    avg_posterior = round(mean(sapply(1:g, function(k) {
      idx <- mg$classification == k
      if (sum(idx) > 0) mean(mg$z[idx, k]) else NA
    }), na.rm = TRUE), 4),
    class_sizes = paste(as.integer(cls_tab), collapse = "/")
  )

  add_summary("  G=%d (%s): BIC=%.1f, loglik=%.1f, ICL=%.1f, entropy=%.4f\n",
              g, mg$modelName, mg$bic, mg$loglik, icl_val, ent_val)
  add_summary("    Class sizes: %s  (min=%.1f%%)\n",
              paste(as.integer(cls_tab), collapse = "/"), min_prop * 100)
  add_summary("    Avg posterior per class: %s\n",
              paste(round(avg_pp, 3), collapse = ", "))
}

comparison_df <- do.call(rbind, comparison_rows)
add_summary("\n  Summary: Best BIC at G=%d (%.1f)\n\n",
            comparison_df$G[which.max(comparison_df$BIC)],
            max(comparison_df$BIC))


# ══════════════════════════════════════════════════════════════════
# 2. BOOTSTRAP LRT (5 vs 6, 6 vs 7)
# ══════════════════════════════════════════════════════════════════
add_summary("============================================================\n")
add_summary("  2. Bootstrap Likelihood Ratio Tests\n")
add_summary("============================================================\n\n")

run_bootstrap_lrt <- function(data, g_null, g_alt, nboot = 100) {
  cat(sprintf("  Bootstrap LRT: G=%d vs G=%d (nboot=%d) ...\n", g_null, g_alt, nboot))
  tryCatch({
    t0 <- Sys.time()
    blrt <- mclustBootstrapLRT(data, modelName = final_mc$modelName,
                                nboot = nboot, maxG = g_alt)
    elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
    cat(sprintf("    Done (%.1fs)\n", elapsed))
    return(blrt)
  }, error = function(e) {
    cat(sprintf("    ERROR: %s\n", e$message))
    return(NULL)
  })
}

blrt_5v6 <- run_bootstrap_lrt(X, 5, 6, nboot = 100)
if (!is.null(blrt_5v6)) {
  add_summary("  LRT results (up to G=%d):\n", 6)
  # Capture the print output
  blrt_output <- capture.output(print(blrt_5v6))
  for (line in blrt_output) {
    add_summary("    %s\n", line)
  }
  add_summary("\n")
}

blrt_6v7 <- run_bootstrap_lrt(X, 6, 7, nboot = 100)
if (!is.null(blrt_6v7)) {
  add_summary("  LRT results (up to G=%d):\n", 7)
  blrt_output <- capture.output(print(blrt_6v7))
  for (line in blrt_output) {
    add_summary("    %s\n", line)
  }
  add_summary("\n")
}

if (is.null(blrt_5v6) && is.null(blrt_6v7)) {
  add_summary("  Both bootstrap LRT tests failed. See console for errors.\n\n")
}


# ══════════════════════════════════════════════════════════════════
# 3. SPLIT-HALF VALIDATION
# ══════════════════════════════════════════════════════════════════
add_summary("============================================================\n")
add_summary("  3. Split-Half Validation\n")
add_summary("============================================================\n\n")

set.seed(42)
idx_all  <- 1:N
half1_idx <- sort(sample(idx_all, size = floor(N / 2)))
half2_idx <- setdiff(idx_all, half1_idx)

add_summary("  Half 1: N=%d, Half 2: N=%d\n", length(half1_idx), length(half2_idx))

X1 <- X[half1_idx, ]
X2 <- X[half2_idx, ]

cat("  Fitting Half 1 (G=6) ... ")
t0 <- Sys.time()
mc_h1 <- Mclust(X1, G = 6, verbose = FALSE)
cat(sprintf("%.1fs\n", as.numeric(difftime(Sys.time(), t0, units = "secs"))))

cat("  Fitting Half 2 (G=6) ... ")
t0 <- Sys.time()
mc_h2 <- Mclust(X2, G = 6, verbose = FALSE)
cat(sprintf("%.1fs\n", as.numeric(difftime(Sys.time(), t0, units = "secs"))))

if (!is.null(mc_h1) && !is.null(mc_h2)) {
  add_summary("  Half 1: %s G=%d BIC=%.1f\n", mc_h1$modelName, mc_h1$G, mc_h1$bic)
  add_summary("  Half 2: %s G=%d BIC=%.1f\n", mc_h2$modelName, mc_h2$G, mc_h2$bic)

  # Compute class centroids for each half
  # Centroids = mean of each feature per class
  centroids_h1 <- t(sapply(1:mc_h1$G, function(k) {
    colMeans(X1[mc_h1$classification == k, , drop = FALSE])
  }))  # G x 20

  centroids_h2 <- t(sapply(1:mc_h2$G, function(k) {
    colMeans(X2[mc_h2$classification == k, , drop = FALSE])
  }))  # G x 20

  # Match classes across halves using correlation
  # Compute correlation matrix between all pairs of centroids
  cor_mat <- cor(t(centroids_h1), t(centroids_h2))
  add_summary("\n  Centroid correlation matrix (Half1 rows x Half2 cols):\n")
  add_summary("         %s\n", paste(sprintf("H2_C%d  ", 1:ncol(cor_mat)), collapse = ""))
  for (i in 1:nrow(cor_mat)) {
    add_summary("  H1_C%d %s\n", i,
                paste(sprintf("%+.4f ", cor_mat[i, ]), collapse = ""))
  }

  # Greedy matching: for each Half1 class, find best Half2 match
  matched <- integer(nrow(cor_mat))
  used    <- logical(ncol(cor_mat))
  order_match <- order(apply(cor_mat, 1, max), decreasing = TRUE)

  for (i in order_match) {
    avail <- which(!used)
    best  <- avail[which.max(cor_mat[i, avail])]
    matched[i] <- best
    used[best] <- TRUE
  }

  matched_cors <- sapply(1:length(matched), function(i) cor_mat[i, matched[i]])
  add_summary("\n  Best match correlations: %s\n",
              paste(sprintf("H1_%d<->H2_%d: %.4f", 1:length(matched), matched, matched_cors),
                    collapse = ", "))
  add_summary("  Mean matched correlation: %.4f\n", mean(matched_cors))

  # Adjusted Rand Index using full-sample predictions
  # Predict each half's students in the other model is not straightforward,
  # so we compare classifications for the same students using predict
  pred_h1_in_h2 <- predict(mc_h2, X1)
  pred_h2_in_h1 <- predict(mc_h1, X2)

  # ARI between half1's own classification and half2-model's classification of half1
  ari_h1 <- adjustedRandIndex(mc_h1$classification, pred_h1_in_h2$classification)
  ari_h2 <- adjustedRandIndex(mc_h2$classification, pred_h2_in_h1$classification)

  add_summary("  ARI (Half1 own vs Half2-model prediction on Half1): %.4f\n", ari_h1)
  add_summary("  ARI (Half2 own vs Half1-model prediction on Half2): %.4f\n", ari_h2)
  add_summary("  Mean cross-ARI: %.4f\n\n", mean(c(ari_h1, ari_h2)))

  # Class size comparison
  add_summary("  Class size proportions:\n")
  tab_h1 <- table(mc_h1$classification)
  tab_h2 <- table(mc_h2$classification)
  add_summary("    Half 1: %s\n", paste(sprintf("%.1f%%", prop.table(tab_h1) * 100), collapse = " / "))
  add_summary("    Half 2: %s\n", paste(sprintf("%.1f%%", prop.table(tab_h2) * 100), collapse = " / "))
  add_summary("    Full:   %s\n\n",
              paste(sprintf("%.1f%%", prop.table(table(final_mc$classification)) * 100), collapse = " / "))
} else {
  add_summary("  Split-half fitting FAILED for one or both halves.\n\n")
}


# ══════════════════════════════════════════════════════════════════
# 4. THRESHOLD SENSITIVITY
# ══════════════════════════════════════════════════════════════════
add_summary("============================================================\n")
add_summary("  4. Threshold Sensitivity\n")
add_summary("============================================================\n\n")

# Read raw data for re-filtering
summary_df <- read.csv(file.path(out_dir, "phase1_student_summary.csv"),
                       stringsAsFactors = FALSE)
long_df    <- read.csv(file.path(out_dir, "phase1_timeseries_long.csv"),
                       stringsAsFactors = FALSE)

# Original thresholds: adaptive_ratio >= 0.10, n_episodes >= 60, n_adaptive >= 5, time_span_days >= 1
# We vary adaptive_ratio only

reshape_to_wide <- function(ldf) {
  # Replicate the Phase 2 reshape logic
  rb_w <- reshape(ldf[, c("user_id", "window", "R_b")],
                  idvar = "user_id", timevar = "window",
                  direction = "wide")
  names(rb_w) <- c("user_id", paste0("Rb_w", 1:10))

  p_w <- reshape(ldf[, c("user_id", "window", "P")],
                 idvar = "user_id", timevar = "window",
                 direction = "wide")
  names(p_w) <- c("user_id", paste0("P_w", 1:10))

  w <- merge(rb_w, p_w, by = "user_id")
  return(w)
}

for (thresh in c(0.15, 0.20)) {
  add_summary("  --- Threshold: adaptive_ratio >= %.2f ---\n", thresh)

  # Filter students
  keep <- summary_df$user_id[summary_df$adaptive_ratio >= thresh &
                              summary_df$n_episodes >= 60 &
                              summary_df$n_adaptive >= 5 &
                              summary_df$time_span_days >= 1]

  filt_long <- long_df[long_df$user_id %in% keep, ]
  add_summary("  Students passing filter: %d (original: %d)\n", length(keep), N)

  if (length(keep) < 50) {
    add_summary("  Too few students for GMM. Skipping.\n\n")
    next
  }

  # Reshape
  w_filt <- reshape_to_wide(filt_long)
  X_filt <- as.matrix(w_filt[, -1])
  rownames(X_filt) <- w_filt$user_id

  # Run mclust G=4:7
  cat(sprintf("  Fitting mclust (G=4:7) for threshold %.2f ... ", thresh))
  t0 <- Sys.time()
  mc_filt <- Mclust(X_filt, G = 4:7, verbose = FALSE)
  elapsed <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  cat(sprintf("%.1fs\n", elapsed))

  if (!is.null(mc_filt)) {
    add_summary("  Best model: %s, G=%d, BIC=%.1f\n",
                mc_filt$modelName, mc_filt$G, mc_filt$bic)

    # BIC for each G
    bic_vals <- mc_filt$BIC
    best_bic_per_g <- apply(bic_vals, 1, max, na.rm = TRUE)
    for (g in names(best_bic_per_g)) {
      if (is.finite(best_bic_per_g[g])) {
        add_summary("    G=%s: BIC=%.1f\n", g, best_bic_per_g[g])
      }
    }

    # Class proportions
    cls_tab_filt <- table(mc_filt$classification)
    add_summary("  Class proportions: %s\n",
                paste(sprintf("%.1f%%", prop.table(cls_tab_filt) * 100), collapse = " / "))

    # Compare trajectory shapes (centroids)
    centroids_filt <- t(sapply(1:mc_filt$G, function(k) {
      colMeans(X_filt[mc_filt$classification == k, , drop = FALSE])
    }))

    # Compare to original centroids
    centroids_orig <- t(sapply(1:final_mc$G, function(k) {
      colMeans(X[final_mc$classification == k, , drop = FALSE])
    }))

    # If same G, compute correlation
    if (mc_filt$G == final_mc$G) {
      cor_m <- cor(t(centroids_filt), t(centroids_orig))
      max_cors <- apply(cor_m, 1, max)
      add_summary("  Max centroid correlation with original (per class): %s\n",
                  paste(sprintf("%.3f", max_cors), collapse = ", "))
    } else {
      add_summary("  Different G selected (%d vs original %d) -- direct centroid comparison skipped\n",
                  mc_filt$G, final_mc$G)
    }

    # ARI with original (for overlapping students)
    overlap_ids <- intersect(w_filt$user_id, wide$user_id)
    if (length(overlap_ids) > 0) {
      cls_orig <- final_mc$classification[match(overlap_ids, wide$user_id)]
      cls_filt <- mc_filt$classification[match(overlap_ids, w_filt$user_id)]
      ari_val  <- adjustedRandIndex(cls_orig, cls_filt)
      add_summary("  ARI with original (N=%d overlap): %.4f\n", length(overlap_ids), ari_val)
    }
  } else {
    add_summary("  mclust FAILED for threshold %.2f\n", thresh)
  }
  add_summary("\n")
}


# ══════════════════════════════════════════════════════════════════
# 5. ENTROPY AND CLASSIFICATION QUALITY
# ══════════════════════════════════════════════════════════════════
add_summary("============================================================\n")
add_summary("  5. Entropy and Classification Quality\n")
add_summary("============================================================\n\n")

z <- final_mc$z  # N x G posterior probabilities

# Average posterior probability per class
add_summary("  Average posterior probability per class:\n")
for (k in 1:final_mc$G) {
  idx <- final_mc$classification == k
  avg_pp_k <- mean(z[idx, k])
  med_pp_k <- median(z[idx, k])
  add_summary("    Class %d (N=%d): mean=%.4f, median=%.4f\n",
              k, sum(idx), avg_pp_k, med_pp_k)
}

# Overall average posterior for assigned class
max_pp <- apply(z, 1, max)
add_summary("\n  Overall average posterior (assigned class): %.4f\n", mean(max_pp))

# Proportion above thresholds
for (thr in c(0.7, 0.8, 0.9)) {
  prop_above <- mean(max_pp > thr)
  n_above    <- sum(max_pp > thr)
  add_summary("  Students with max posterior > %.1f: %d (%.1f%%)\n",
              thr, n_above, prop_above * 100)
}

# Normalized entropy (Celka)
G <- final_mc$G
ent_raw <- -sum(z * log(pmax(z, 1e-300)))
ent_norm <- 1 - ent_raw / (N * log(G))
add_summary("\n  Normalized entropy (E_k): %.4f\n", ent_norm)
add_summary("  Interpretation: %.1f%% of classification certainty retained\n",
            ent_norm * 100)

# Classification table: rows = assigned class, columns = 2nd most likely class
add_summary("\n  Classification uncertainty table (assigned vs 2nd-most-likely class):\n")
second_class <- apply(z, 1, function(row) {
  ord <- order(row, decreasing = TRUE)
  ord[2]
})
cross_tab <- table(Assigned = final_mc$classification, Second = second_class)
cross_output <- capture.output(print(cross_tab))
for (line in cross_output) {
  add_summary("    %s\n", line)
}

# Per-class entropy
add_summary("\n  Per-class average entropy (lower = better separated):\n")
for (k in 1:final_mc$G) {
  idx <- final_mc$classification == k
  z_k <- z[idx, , drop = FALSE]
  ent_k <- -mean(rowSums(z_k * log(pmax(z_k, 1e-300))))
  add_summary("    Class %d: %.4f\n", k, ent_k)
}

add_summary("\n")


# ══════════════════════════════════════════════════════════════════
# 6. SAVE OUTPUTS
# ══════════════════════════════════════════════════════════════════
cat("============================================================\n")
cat("  Saving outputs\n")
cat("============================================================\n\n")

# Save comparison CSV
write.csv(comparison_df,
          file.path(out_dir, "phase4_sensitivity_comparison.csv"),
          row.names = FALSE)
cat("  Saved: phase4_sensitivity_comparison.csv\n")

# Save summary text
writeLines(summary_lines, file.path(out_dir, "phase4_sensitivity_summary.txt"))
cat("  Saved: phase4_sensitivity_summary.txt\n")

cat("\n============================================================\n")
cat("  Phase 4: Sensitivity Analysis Complete\n")
cat("============================================================\n")
