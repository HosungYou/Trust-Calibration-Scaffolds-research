#!/usr/bin/env Rscript
# =============================================================================
# Chess Puzzle LCGA Analysis
# =============================================================================
# Latent Class Growth Analysis using lcmm package
# Piecewise linear model with switch point at Window 4.5
# Bondi et al. (2023) — Independent analysis
#
# This script complements the mclust GMM analysis by explicitly
# modeling temporal structure via growth curves.
# =============================================================================

library(lcmm)
library(readr)

cat("================================================================\n")
cat("CHESS PUZZLE LCGA ANALYSIS (lcmm)\n")
cat("Piecewise Linear Growth Model\n")
cat("================================================================\n\n")

base_dir <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis"
output_dir <- file.path(base_dir, "analysis", "outputs")

# --- Load data ---
df <- read_csv(file.path(output_dir, "chess_window_level.csv"),
               show_col_types = FALSE)

cat("Loaded:", nrow(df), "rows,", length(unique(df$session_id)), "sessions\n")
cat("  C1 (High->Low):", sum(df$condition == 1) / 6, "\n")
cat("  C2 (Low->High):", sum(df$condition == 2) / 6, "\n\n")

# --- Prepare variables ---
# Time: window 1-6 -> 0-5
df$Time <- df$window - 1

# Piecewise: switch between W4 and W5 (Time 3 and 4)
# post_switch = max(0, Time - 3.5) for piecewise slope
df$post_switch <- pmax(0, df$Time - 3.5)

# Numeric subject ID for lcmm
uid_map <- data.frame(
  session_id = sort(unique(df$session_id)),
  sid = seq_along(unique(df$session_id))
)
df <- merge(df, uid_map, by = "session_id")
N <- length(unique(df$sid))
cat("Subjects (sessions):", N, "\n\n")

# =============================================================================
# Analysis A: cal_gap trajectory (primary outcome)
# =============================================================================
cat("=== Analysis A: cal_gap trajectory ===\n\n")

# --- A1: 1-class baseline ---
cat("--- A1: 1-class model ---\n")
t0 <- Sys.time()

m1_gap <- hlme(
  cal_gap ~ Time + post_switch,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  data = df,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            m1_gap$loglik, m1_gap$conv))

# --- A2-A6: Multi-class models ---
gap_models <- list()
gap_models[["1"]] <- m1_gap

for (ng in 2:6) {
  cat(sprintf("--- A%d: %d-class model (gridsearch 30 reps) ---\n", ng, ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 30,
      maxiter = 100,
      minit = m1_gap,
      hlme(
        cal_gap ~ Time + post_switch,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time + post_switch,
        ng = ng,
        data = df,
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
cat("\n=== cal_gap Model Selection ===\n")
cat(sprintf("%-5s %10s %10s %10s %10s %10s %10s\n",
            "G", "loglik", "npm", "BIC", "SABIC", "Entropy", "Conv"))

gap_fit <- data.frame()

for (k in names(gap_models)) {
  m <- gap_models[[k]]
  n_obs <- nrow(df)
  n_subj <- N
  loglik <- m$loglik
  npm <- ifelse(is.null(m$npm), length(m$best), m$npm)
  bic_val <- m$BIC
  # SABIC: -2*loglik + npm * ln((N+2)/24)
  sabic <- -2 * loglik + npm * log((n_subj + 2) / 24)
  # Entropy (for multi-class)
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

write_csv(gap_fit, file.path(output_dir, "chess_lcga_gap_model_fit.csv"))

# Select best by BIC
best_g_gap <- gap_fit$G[which.min(gap_fit$BIC)]
cat(sprintf("\nBest model (BIC): G=%d\n", best_g_gap))

# Best model details
best_gap <- gap_models[[as.character(best_g_gap)]]

# Class assignments
if (best_g_gap > 1 && !is.null(best_gap$pprob)) {
  gap_assign <- best_gap$pprob
  gap_assign <- merge(gap_assign, uid_map, by = "sid")
  gap_assign <- merge(gap_assign,
                      unique(df[, c("session_id", "condition")]),
                      by = "session_id")
  write_csv(gap_assign, file.path(output_dir, "chess_lcga_gap_assignments.csv"))

  cat("\nClass distribution:\n")
  for (g in 1:best_g_gap) {
    idx <- gap_assign$class == g
    n <- sum(idx)
    n_c1 <- sum(gap_assign$condition[idx] == 1)
    n_c2 <- sum(gap_assign$condition[idx] == 2)
    cat(sprintf("  Class %d: N=%d (C1=%d, C2=%d)\n", g, n, n_c1, n_c2))
  }
}

# =============================================================================
# Analysis B: R_b trajectory (behavioral outcome)
# =============================================================================
cat("\n\n=== Analysis B: R_b trajectory ===\n\n")

cat("--- B1: 1-class model ---\n")
t0 <- Sys.time()

m1_rb <- hlme(
  R_b ~ Time + post_switch,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  data = df,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            m1_rb$loglik, m1_rb$conv))

rb_models <- list()
rb_models[["1"]] <- m1_rb

for (ng in 2:6) {
  cat(sprintf("--- B%d: %d-class model (gridsearch 30 reps) ---\n", ng, ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 30,
      maxiter = 100,
      minit = m1_rb,
      hlme(
        R_b ~ Time + post_switch,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time + post_switch,
        ng = ng,
        data = df,
        maxiter = 1000
      )
    )

    rb_models[[as.character(ng)]] <- m
    cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d, BIC=%.1f\n\n",
                as.numeric(difftime(Sys.time(), t0, units = "secs")),
                m$loglik, m$conv, m$BIC))
  }, error = function(e) {
    cat("  ERROR:", e$message, "\n\n")
  })
}

# Model selection for R_b
cat("\n=== R_b Model Selection ===\n")
cat(sprintf("%-5s %10s %10s %10s %10s %10s %10s\n",
            "G", "loglik", "npm", "BIC", "SABIC", "Entropy", "Conv"))

rb_fit <- data.frame()

for (k in names(rb_models)) {
  m <- rb_models[[k]]
  loglik <- m$loglik
  npm <- ifelse(is.null(m$npm), length(m$best), m$npm)
  bic_val <- m$BIC
  sabic <- -2 * loglik + npm * log((N + 2) / 24)
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

  rb_fit <- rbind(rb_fit, data.frame(
    G = as.integer(k), loglik = loglik, npm = npm,
    BIC = bic_val, SABIC = sabic, Entropy = entropy,
    Conv = m$conv
  ))
}

write_csv(rb_fit, file.path(output_dir, "chess_lcga_rb_model_fit.csv"))

best_g_rb <- rb_fit$G[which.min(rb_fit$BIC)]
cat(sprintf("\nBest model (BIC): G=%d\n", best_g_rb))

best_rb <- rb_models[[as.character(best_g_rb)]]

if (best_g_rb > 1 && !is.null(best_rb$pprob)) {
  rb_assign <- best_rb$pprob
  rb_assign <- merge(rb_assign, uid_map, by = "sid")
  rb_assign <- merge(rb_assign,
                     unique(df[, c("session_id", "condition")]),
                     by = "session_id")
  write_csv(rb_assign, file.path(output_dir, "chess_lcga_rb_assignments.csv"))

  cat("\nClass distribution:\n")
  for (g in 1:best_g_rb) {
    idx <- rb_assign$class == g
    n <- sum(idx)
    n_c1 <- sum(rb_assign$condition[idx] == 1)
    n_c2 <- sum(rb_assign$condition[idx] == 2)
    cat(sprintf("  Class %d: N=%d (C1=%d, C2=%d)\n", g, n, n_c1, n_c2))
  }
}

# =============================================================================
# Analysis C: Multivariate LCGA (R_b + cal_gap jointly)
# =============================================================================
cat("\n\n=== Analysis C: Multivariate LCGA (R_b + cal_gap) ===\n\n")

cat("--- C1: 1-class bivariate model ---\n")
t0 <- Sys.time()

m1_biv <- multlcmm(
  R_b + cal_gap ~ Time + post_switch,
  random = ~ 1,
  subject = "sid",
  ng = 1,
  link = c("linear", "linear"),
  data = df,
  maxiter = 2000
)

cat(sprintf("  Done (%.1fs): loglik=%.1f, conv=%d\n\n",
            as.numeric(difftime(Sys.time(), t0, units = "secs")),
            m1_biv$loglik, m1_biv$conv))

biv_models <- list()
biv_models[["1"]] <- m1_biv

for (ng in 2:5) {
  cat(sprintf("--- C%d: %d-class bivariate model (gridsearch 20 reps) ---\n", ng, ng))
  t0 <- Sys.time()

  tryCatch({
    m <- gridsearch(
      rep = 20,
      maxiter = 50,
      minit = m1_biv,
      multlcmm(
        R_b + cal_gap ~ Time + post_switch,
        random = ~ 1,
        subject = "sid",
        mixture = ~ Time + post_switch,
        ng = ng,
        link = c("linear", "linear"),
        data = df,
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

# Model selection for bivariate
cat("\n=== Bivariate Model Selection ===\n")
cat(sprintf("%-5s %10s %10s %10s %10s %10s\n",
            "G", "loglik", "npm", "BIC", "SABIC", "Conv"))

biv_fit <- data.frame()

for (k in names(biv_models)) {
  m <- biv_models[[k]]
  loglik <- m$loglik
  npm <- ifelse(is.null(m$npm), length(m$best), m$npm)
  bic_val <- m$BIC
  sabic <- -2 * loglik + npm * log((N + 2) / 24)

  cat(sprintf("%-5s %10.1f %10d %10.1f %10.1f %10d\n",
              k, loglik, npm, bic_val, sabic, m$conv))

  biv_fit <- rbind(biv_fit, data.frame(
    G = as.integer(k), loglik = loglik, npm = npm,
    BIC = bic_val, SABIC = sabic, Conv = m$conv
  ))
}

write_csv(biv_fit, file.path(output_dir, "chess_lcga_bivariate_model_fit.csv"))

# =============================================================================
# Cross-method comparison: LCGA vs mclust GMM
# =============================================================================
cat("\n\n=== Cross-Method Comparison ===\n")

# Load mclust assignments if available
gmm_s2_path <- file.path(output_dir, "chess_gmm_s2_assignments.csv")
if (file.exists(gmm_s2_path) && best_g_gap > 1) {
  gmm_s2 <- read_csv(gmm_s2_path, show_col_types = FALSE)
  lcga_cls <- gap_assign[, c("session_id", "class")]
  names(lcga_cls)[2] <- "lcga_class"
  gmm_cls <- gmm_s2[, c("session_id", "s2_class")]
  names(gmm_cls)[2] <- "gmm_class"

  comp <- merge(lcga_cls, gmm_cls, by = "session_id")

  # ARI
  ari <- mclust::adjustedRandIndex(comp$lcga_class, comp$gmm_class)
  cat(sprintf("  ARI (LCGA gap G=%d vs mclust GMM S2): %.3f\n", best_g_gap, ari))

  # Cross-tabulation
  cat("\n  Cross-tabulation:\n")
  ct <- table(LCGA = comp$lcga_class, GMM = comp$gmm_class)
  print(ct)
}

# =============================================================================
# Save workspace
# =============================================================================
save.image(file.path(output_dir, "chess_lcga_workspace.RData"))
cat("\n\nSaved workspace to chess_lcga_workspace.RData\n")
cat("Done!\n")
