#!/usr/bin/env Rscript
#
# Phase 2: Parallel Process Growth Mixture Model (PP-GMM)
#
# Simplified approach:
#   1. Fit 1-class on subsample (N=1000) to find starting values
#   2. Scale up to full data
#   3. Gridsearch for 2-5 classes

library(lcmm)

cat("============ Phase 2: PP-GMM ============\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
data_path <- file.path(base_dir, "analysis/outputs/phase1_timeseries_long.csv")
out_dir <- file.path(base_dir, "analysis/outputs")

df <- read.csv(data_path, stringsAsFactors = FALSE)

# Time: window 1-10 → 0-9
df$Time <- df$window - 1

# Numeric subject ID
uid_map <- data.frame(
  user_id = sort(unique(df$user_id)),
  sid = seq_along(unique(df$user_id))
)
df <- merge(df, uid_map, by = "user_id")
N <- length(unique(df$sid))
cat("Full data: N =", N, ", rows =", nrow(df), "\n\n")

# ── Subsample for fast model exploration ──
set.seed(42)
sub_sids <- sample(unique(df$sid), 1000)
df_sub <- df[df$sid %in% sub_sids, ]
N_sub <- length(unique(df_sub$sid))
cat("Subsample: N =", N_sub, "\n\n")

# ── Step 1: 1-class on subsample ──
cat("--- 1-class model (subsample N=1000) ---\n")
t0 <- Sys.time()

m1_sub <- multlcmm(
  R_b + P ~ Time,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  link = c("linear", "linear"),
  data = df_sub,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d, npm=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units="secs")),
            m1_sub$loglik, m1_sub$conv, m1_sub$npm))

# ── Step 2: Multi-class on subsample ──
sub_models <- list()
sub_models[["1"]] <- m1_sub

for (ng in 2:5) {
  cat(sprintf("--- %d-class model (subsample, gridsearch 20 reps) ---\n", ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 20,
      maxiter = 50,
      minit = m1_sub,
      multlcmm(
        R_b + P ~ Time,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time,
        ng = ng,
        link = c("linear", "linear"),
        data = df_sub,
        maxiter = 500,
        nwg = TRUE
      )
    )

    elapsed <- as.numeric(difftime(Sys.time(), t0, units="secs"))
    bic_val <- -2 * m$loglik + log(N_sub) * m$npm

    props <- table(m$pprob$class) / nrow(m$pprob)
    prop_str <- paste(sprintf("%.1f%%", props * 100), collapse=", ")

    sub_models[[as.character(ng)]] <- m
    cat(sprintf("  Done (%.1fs): loglik=%.1f, BIC=%.1f, conv=%d | %s\n\n",
                elapsed, m$loglik, bic_val, m$conv, prop_str))

  }, error = function(e) {
    cat(sprintf("  FAILED: %s\n\n", e$message))
  })
}

# ── Subsample model comparison ──
cat("\n===== SUBSAMPLE MODEL COMPARISON =====\n")
cat(sprintf("%-4s %-11s %-5s %-11s %-11s %-5s %-25s\n",
            "ng", "LogLik", "npar", "AIC", "BIC", "Conv", "Classes"))

for (ng_str in names(sub_models)) {
  m <- sub_models[[ng_str]]
  ng <- as.integer(ng_str)
  bic <- -2 * m$loglik + log(N_sub) * m$npm
  aic <- -2 * m$loglik + 2 * m$npm

  if (ng > 1 && m$conv == 1) {
    props <- table(m$pprob$class) / nrow(m$pprob)
    prop_str <- paste(sprintf("%.1f%%", props * 100), collapse=", ")
  } else {
    prop_str <- "100%"
  }

  cat(sprintf("%-4d %-11.1f %-5d %-11.1f %-11.1f %-5d %s\n",
              ng, m$loglik, m$npm, aic, bic, m$conv, prop_str))
}

# ── Step 3: Refit best candidates on FULL data ──
cat("\n===== REFITTING ON FULL DATA (N=4568) =====\n\n")

# Fit 1-class on full data
cat("--- 1-class model (full data) ---\n")
t0 <- Sys.time()

m1_full <- multlcmm(
  R_b + P ~ Time,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  link = c("linear", "linear"),
  data = df,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units="secs")),
            m1_full$loglik, m1_full$conv))

full_models <- list()
full_models[["1"]] <- m1_full

# Refit 2-5 class models using subsample results as initial values
for (ng in 2:5) {
  ng_str <- as.character(ng)
  if (is.null(sub_models[[ng_str]])) next

  cat(sprintf("--- %d-class model (full data, gridsearch 15 reps) ---\n", ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 15,
      maxiter = 50,
      minit = m1_full,
      multlcmm(
        R_b + P ~ Time,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time,
        ng = ng,
        link = c("linear", "linear"),
        data = df,
        maxiter = 1000,
        nwg = TRUE
      )
    )

    elapsed <- as.numeric(difftime(Sys.time(), t0, units="secs"))
    bic_val <- -2 * m$loglik + log(N) * m$npm

    props <- table(m$pprob$class) / nrow(m$pprob)
    prop_str <- paste(sprintf("%.1f%%", props * 100), collapse=", ")
    min_prop <- min(props)

    full_models[[ng_str]] <- m
    cat(sprintf("  Done (%.1fs): loglik=%.1f, BIC=%.1f, conv=%d | %s\n\n",
                elapsed, m$loglik, bic_val, m$conv, prop_str))

  }, error = function(e) {
    cat(sprintf("  FAILED: %s\n\n", e$message))
  })
}

# ── Full data model comparison ──
cat("\n===== FULL DATA MODEL COMPARISON =====\n")
cat(sprintf("%-4s %-12s %-5s %-12s %-12s %-5s %-6s %-25s\n",
            "ng", "LogLik", "npar", "AIC", "BIC", "Conv", "MinCl", "Classes"))

fit_rows <- list()
for (ng_str in names(full_models)) {
  m <- full_models[[ng_str]]
  ng <- as.integer(ng_str)
  bic <- -2 * m$loglik + log(N) * m$npm
  aic <- -2 * m$loglik + 2 * m$npm

  if (ng > 1 && m$conv == 1) {
    props <- table(m$pprob$class) / nrow(m$pprob)
    prop_str <- paste(sprintf("%.1f%%", props * 100), collapse=", ")
    min_prop <- min(props)
  } else {
    prop_str <- "100%"
    min_prop <- 1.0
  }

  cat(sprintf("%-4d %-12.1f %-5d %-12.1f %-12.1f %-5d %-6.1f %s\n",
              ng, m$loglik, m$npm, aic, bic, m$conv, min_prop*100, prop_str))

  fit_rows <- append(fit_rows, list(data.frame(
    ng=ng, loglik=m$loglik, npm=m$npm, aic=aic, bic=bic,
    conv=m$conv, min_class_prop=round(min_prop,4)
  )))
}

fit_df <- do.call(rbind, fit_rows)
write.csv(fit_df, file.path(out_dir, "phase2_model_fit.csv"), row.names = FALSE)
cat("\nSaved: phase2_model_fit.csv\n")

# ── Select best ──
fit_df$valid <- fit_df$conv == 1 & fit_df$min_class_prop >= 0.05
valid_fits <- fit_df[fit_df$valid, ]

if (nrow(valid_fits) > 0) {
  best_ng <- valid_fits$ng[which.min(valid_fits$bic)]
  cat(sprintf("\n>>> BEST MODEL: ng=%d (BIC=%.1f) <<<\n\n", best_ng,
              valid_fits$bic[valid_fits$ng == best_ng]))
  final_model <- full_models[[as.character(best_ng)]]
} else {
  cat("\nNo valid model found. Using ng=1.\n")
  final_model <- m1_full
  best_ng <- 1
}

# ── Save class assignments ──
pprob <- final_model$pprob
pprob_out <- merge(pprob, uid_map, by.x = "sid", by.y = "sid")
write.csv(pprob_out, file.path(out_dir, "phase2_class_assignments.csv"), row.names = FALSE)
cat(sprintf("Saved: phase2_class_assignments.csv (%d students, %d classes)\n",
            nrow(pprob_out), best_ng))

# ── Compute class trajectories ──
traj_rows <- list()
for (cls in 1:best_ng) {
  members <- pprob$sid[pprob$class == cls]
  cls_data <- df[df$sid %in% members, ]

  for (w in 0:9) {
    w_data <- cls_data[cls_data$Time == w, ]
    traj_rows <- append(traj_rows, list(data.frame(
      class = cls,
      window = w + 1,
      mean_R_b = mean(w_data$R_b, na.rm = TRUE),
      mean_P = mean(w_data$P, na.rm = TRUE),
      mean_gap = mean(w_data$R_b - w_data$P, na.rm = TRUE),
      sd_R_b = sd(w_data$R_b, na.rm = TRUE),
      sd_P = sd(w_data$P, na.rm = TRUE),
      n = length(unique(w_data$sid))
    )))
  }
}

traj_df <- do.call(rbind, traj_rows)
write.csv(traj_df, file.path(out_dir, "phase2_class_trajectories.csv"), row.names = FALSE)
cat("Saved: phase2_class_trajectories.csv\n")

# ── Print trajectories ──
cat("\n===== CLASS TRAJECTORIES =====\n")
for (cls in 1:best_ng) {
  ct <- traj_df[traj_df$class == cls, ]
  n_m <- ct$n[1]
  pct <- n_m / N * 100
  cat(sprintf("\nClass %d (N=%d, %.1f%%):\n", cls, n_m, pct))
  cat(sprintf("  %-4s %-7s %-7s %-7s\n", "Win", "R_b", "P", "Gap"))
  for (i in 1:nrow(ct)) {
    cat(sprintf("  %-4d %-7.4f %-7.4f %+.4f\n",
                ct$window[i], ct$mean_R_b[i], ct$mean_P[i], ct$mean_gap[i]))
  }
  cat(sprintf("  Δ R_b: %+.4f, Δ P: %+.4f, Δ Gap: %+.4f\n",
              ct$mean_R_b[10] - ct$mean_R_b[1],
              ct$mean_P[10] - ct$mean_P[1],
              ct$mean_gap[10] - ct$mean_gap[1]))
}

# ── Save workspace ──
save(final_model, full_models, sub_models, fit_df, traj_df, pprob, uid_map, df,
     file = file.path(out_dir, "phase2_workspace.RData"))
cat("\nSaved: phase2_workspace.RData\n")
cat("\n============ Phase 2 Complete ============\n")
