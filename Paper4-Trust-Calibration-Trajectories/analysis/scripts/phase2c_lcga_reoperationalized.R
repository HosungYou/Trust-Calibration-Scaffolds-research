#!/usr/bin/env Rscript
# =============================================================================
# Phase 2C: LCGA with Re-operationalized Variables (P_adaptive)
# =============================================================================
# Updates Phase 2 PP-GMM to use Phase 1B re-operationalized data:
#   - R_b + P_adaptive (instead of R_b + P)
#   - calibration_gap_new = R_b - P_adaptive
#   - AI_benefit
#
# Uses lcmm::multlcmm() for bivariate trajectory modeling
# and lcmm::lcmm() for univariate cal_gap trajectory
# =============================================================================

library(lcmm)
library(readr)

cat("================================================================\n")
cat("Phase 2C: LCGA with Re-operationalized Variables\n")
cat("EdNet KT3 — R_b + P_adaptive\n")
cat("================================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
data_path <- file.path(base_dir, "analysis/outputs/phase1b_timeseries_long.csv")
out_dir <- file.path(base_dir, "analysis/outputs")

df <- read_csv(data_path, show_col_types = FALSE)

cat("Loaded:", nrow(df), "rows\n")
cat("Columns:", paste(names(df), collapse = ", "), "\n\n")

# --- Prepare variables ---
df$Time <- df$window - 1  # 0-9

# Handle missing P_adaptive (23.8% windows)
# Strategy: use only students with >= 7 valid P_adaptive windows
valid_counts <- aggregate(
  !is.na(df$P_adaptive),
  by = list(user_id = df$user_id),
  FUN = sum
)
names(valid_counts)[2] <- "n_valid"
valid_users <- valid_counts$user_id[valid_counts$n_valid >= 7]

df_complete <- df[df$user_id %in% valid_users, ]

# Impute remaining missing P_adaptive with student mean
df_complete <- do.call(rbind, lapply(split(df_complete, df_complete$user_id), function(x) {
  x$P_adaptive[is.na(x$P_adaptive)] <- mean(x$P_adaptive, na.rm = TRUE)
  x$calibration_gap_new[is.na(x$calibration_gap_new)] <- mean(x$calibration_gap_new, na.rm = TRUE)
  x
}))

# Numeric subject ID
uid_map <- data.frame(
  user_id = sort(unique(df_complete$user_id)),
  sid = seq_along(unique(df_complete$user_id))
)
df_complete <- merge(df_complete, uid_map, by = "user_id")
N <- length(unique(df_complete$sid))
cat("After filtering (>=7 valid windows): N =", N, ", rows =", nrow(df_complete), "\n\n")

# =============================================================================
# Analysis A: Univariate LCGA on calibration_gap_new (R_b - P_adaptive)
# =============================================================================
cat("=== Analysis A: calibration_gap_new LCGA ===\n\n")

# --- A1: 1-class baseline (subsample for speed) ---
set.seed(42)
sub_sids <- sample(unique(df_complete$sid), min(1500, N))
df_sub <- df_complete[df_complete$sid %in% sub_sids, ]
N_sub <- length(unique(df_sub$sid))
cat("Subsample for model exploration: N =", N_sub, "\n\n")

cat("--- A1: 1-class model (subsample) ---\n")
t0 <- Sys.time()

m1_gap <- hlme(
  calibration_gap_new ~ Time,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  data = df_sub,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            m1_gap$loglik, m1_gap$conv))

# --- Multi-class models ---
gap_models <- list()
gap_models[["1"]] <- m1_gap

for (ng in 2:7) {
  cat(sprintf("--- A%d: %d-class model (subsample, gridsearch 30 reps) ---\n", ng, ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 30,
      maxiter = 100,
      minit = m1_gap,
      hlme(
        calibration_gap_new ~ Time,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time,
        ng = ng,
        data = df_sub,
        maxiter = 1000
      )
    )

    gap_models[[as.character(ng)]] <- m
    cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d, BIC=%.1f\n\n",
                as.numeric(difftime(Sys.time(), t0, units = "secs")),
                m$loglik, m$conv, m$BIC))
  }, error = function(e) {
    cat("  ERROR:", e$message, "\n\n")
  })
}

# --- Model selection ---
cat("\n=== calibration_gap_new Model Selection ===\n")
cat(sprintf("%-5s %10s %10s %10s %10s %10s %10s\n",
            "G", "loglik", "npm", "BIC", "SABIC", "Entropy", "Conv"))

gap_fit <- data.frame()

for (k in names(gap_models)) {
  m <- gap_models[[k]]
  loglik <- m$loglik
  npm <- ifelse(is.null(m$npm), length(m$best), m$npm)
  bic_val <- m$BIC
  sabic <- -2 * loglik + npm * log((N_sub + 2) / 24)
  if (as.integer(k) > 1 && !is.null(m$pprob)) {
    probs <- m$pprob[, grep("^prob", names(m$pprob))]
    ent_i <- -rowSums(probs * log(pmax(probs, 1e-10)))
    max_ent <- log(as.integer(k))
    entropy <- 1 - mean(ent_i) / max_ent
  } else {
    entropy <- NA
  }

  cat(sprintf("%-5s %10.1f %10d %10.1f %10.1f %10.3f %10d\n",
              k, loglik, npm, bic_val, sabic,
              ifelse(is.na(entropy), 0, entropy), m$conv))

  gap_fit <- rbind(gap_fit, data.frame(
    G = as.integer(k), loglik = loglik, npm = npm,
    BIC = bic_val, SABIC = sabic, Entropy = entropy,
    Conv = m$conv
  ))
}

write_csv(gap_fit, file.path(out_dir, "phase2c_lcga_gap_model_fit.csv"))

best_g_gap <- gap_fit$G[which.min(gap_fit$BIC)]
cat(sprintf("\nBest model (BIC): G=%d\n", best_g_gap))

# --- Refit best model on full data ---
cat(sprintf("\n--- Refitting G=%d on full data (N=%d) ---\n", best_g_gap, N))
t0 <- Sys.time()

# 1-class on full data first
m1_full <- hlme(
  calibration_gap_new ~ Time,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  data = df_complete,
  maxiter = 2000
)

if (best_g_gap > 1) {
  best_gap_full <- gridsearch(
    rep = 30,
    maxiter = 100,
    minit = m1_full,
    hlme(
      calibration_gap_new ~ Time,
      random = ~ 1,
      subject = "sid",
      mixture = ~ Time,
      ng = best_g_gap,
      data = df_complete,
      maxiter = 2000
    )
  )
} else {
  best_gap_full <- m1_full
}

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d, BIC=%.1f\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            best_gap_full$loglik, best_gap_full$conv, best_gap_full$BIC))

# Save assignments
if (best_g_gap > 1 && !is.null(best_gap_full$pprob)) {
  gap_assign <- best_gap_full$pprob
  gap_assign <- merge(gap_assign, uid_map, by = "sid")
  write_csv(gap_assign, file.path(out_dir, "phase2c_lcga_gap_assignments.csv"))

  cat("Class distribution (full data):\n")
  for (g in 1:best_g_gap) {
    n <- sum(gap_assign$class == g)
    pct <- round(100 * n / N, 1)
    cat(sprintf("  Class %d: N=%d (%.1f%%)\n", g, n, pct))
  }

  # Class trajectories
  cat("\nClass mean trajectories:\n")
  for (g in 1:best_g_gap) {
    cls_users <- gap_assign$sid[gap_assign$class == g]
    cls_data <- df_complete[df_complete$sid %in% cls_users, ]
    cat(sprintf("\n  Class %d (N=%d):\n", g, length(cls_users)))
    for (w in 1:10) {
      ww <- cls_data[cls_data$window == w, ]
      if (nrow(ww) > 0) {
        cat(sprintf("    W%02d: R_b=%.3f  P_adap=%.3f  Gap=%+.3f\n",
                    w, mean(ww$R_b, na.rm = TRUE),
                    mean(ww$P_adaptive, na.rm = TRUE),
                    mean(ww$calibration_gap_new, na.rm = TRUE)))
      }
    }
  }
}

# =============================================================================
# Analysis B: Bivariate LCGA (R_b + P_adaptive)
# =============================================================================
cat("\n\n=== Analysis B: Bivariate LCGA (R_b + P_adaptive) ===\n\n")

cat("--- B1: 1-class bivariate model (subsample) ---\n")
t0 <- Sys.time()

m1_biv <- multlcmm(
  R_b + P_adaptive ~ Time,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  link = c("linear", "linear"),
  data = df_sub,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            m1_biv$loglik, m1_biv$conv))

biv_models <- list()
biv_models[["1"]] <- m1_biv

for (ng in 2:6) {
  cat(sprintf("--- B%d: %d-class bivariate model (gridsearch 20 reps) ---\n", ng, ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 20,
      maxiter = 50,
      minit = m1_biv,
      multlcmm(
        R_b + P_adaptive ~ Time,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time,
        ng = ng,
        link = c("linear", "linear"),
        data = df_sub,
        maxiter = 1000,
        nwg = TRUE
      )
    )

    biv_models[[as.character(ng)]] <- m
    cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d, BIC=%.1f\n\n",
                as.numeric(difftime(Sys.time(), t0, units = "secs")),
                m$loglik, m$conv, m$BIC))
  }, error = function(e) {
    cat("  ERROR:", e$message, "\n\n")
  })
}

# Model selection
cat("\n=== Bivariate Model Selection ===\n")
cat(sprintf("%-5s %10s %10s %10s %10s %10s\n",
            "G", "loglik", "npm", "BIC", "SABIC", "Conv"))

biv_fit <- data.frame()

for (k in names(biv_models)) {
  m <- biv_models[[k]]
  loglik <- m$loglik
  npm <- ifelse(is.null(m$npm), length(m$best), m$npm)
  bic_val <- m$BIC
  sabic <- -2 * loglik + npm * log((N_sub + 2) / 24)

  cat(sprintf("%-5s %10.1f %10d %10.1f %10.1f %10d\n",
              k, loglik, npm, bic_val, sabic, m$conv))

  biv_fit <- rbind(biv_fit, data.frame(
    G = as.integer(k), loglik = loglik, npm = npm,
    BIC = bic_val, SABIC = sabic, Conv = m$conv
  ))
}

write_csv(biv_fit, file.path(out_dir, "phase2c_lcga_bivariate_model_fit.csv"))

# =============================================================================
# Cross-method comparison: LCGA vs mclust GMM (Phase 2b)
# =============================================================================
cat("\n\n=== Cross-Method Comparison ===\n")

gmm_path <- file.path(out_dir, "phase2b_s2_class_assignments.csv")
if (file.exists(gmm_path) && best_g_gap > 1) {
  gmm_df <- read_csv(gmm_path, show_col_types = FALSE)

  # Match by user_id
  lcga_cls <- gap_assign[, c("user_id", "class")]
  names(lcga_cls)[2] <- "lcga_class"

  if ("s2_class" %in% names(gmm_df)) {
    gmm_cls <- gmm_df[, c("user_id", "s2_class")]
    names(gmm_cls)[2] <- "gmm_class"
  } else {
    # Try first class column
    cls_col <- grep("class", names(gmm_df), value = TRUE)[1]
    gmm_cls <- gmm_df[, c("user_id", cls_col)]
    names(gmm_cls)[2] <- "gmm_class"
  }

  comp <- merge(lcga_cls, gmm_cls, by = "user_id")

  if (nrow(comp) > 0) {
    ari <- mclust::adjustedRandIndex(comp$lcga_class, comp$gmm_class)
    cat(sprintf("  ARI (LCGA G=%d vs mclust GMM S2): %.3f\n", best_g_gap, ari))
    cat(sprintf("  N matched: %d\n", nrow(comp)))

    cat("\n  Cross-tabulation:\n")
    ct <- table(LCGA = comp$lcga_class, GMM = comp$gmm_class)
    print(ct)
  }
} else {
  cat("  GMM assignments not found or single-class LCGA. Skipping comparison.\n")
}

# =============================================================================
# Save workspace
# =============================================================================
save.image(file.path(out_dir, "phase2c_lcga_workspace.RData"))
cat("\n\nSaved workspace to phase2c_lcga_workspace.RData\n")
cat("Done!\n")
