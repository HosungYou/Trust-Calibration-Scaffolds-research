#!/usr/bin/env Rscript
# ==============================================================================
# Generate All 6 Publication Figures (ggplot2)
# Trust Calibration Scaffolds — Trajectory Paper
# APA 7th style: No embedded titles, serif font, 300 DPI
# ==============================================================================

library(ggplot2)
library(patchwork)
library(ggrepel)
library(scales)
library(grid)
library(dplyr)

# --- Global settings ----------------------------------------------------------

# Determine script directory: try commandArgs, fall back to getwd()
.get_script_dir <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) {
    return(dirname(normalizePath(sub("^--file=", "", file_arg[1]))))
  }
  return(getwd())
}
output_dir <- .get_script_dir()
cat("Output directory:", output_dir, "\n")

DPI        <- 300
FONT_FAMILY <- "serif"
BASE_SIZE   <- 11

# APA theme: minimal base, customized for publication
theme_apa <- function(base_size = BASE_SIZE) {
  theme_minimal(base_size = base_size) %+replace%
    theme(
      text             = element_text(family = FONT_FAMILY),
      plot.title       = element_blank(),
      plot.subtitle    = element_blank(),
      axis.title       = element_text(size = base_size, face = "plain"),
      axis.text        = element_text(size = base_size - 1, color = "grey30"),
      axis.line        = element_line(color = "grey40", linewidth = 0.4),
      axis.ticks       = element_line(color = "grey40", linewidth = 0.3),
      panel.grid.major = element_line(color = "grey90", linewidth = 0.25),
      panel.grid.minor = element_blank(),
      legend.text      = element_text(size = base_size - 1),
      legend.title     = element_blank(),
      legend.key.width = unit(1.5, "cm"),
      legend.position  = "bottom",
      plot.margin      = margin(8, 12, 8, 8)
    )
}

# --- Color palettes -----------------------------------------------------------

# MBC: Tol bright (6 classes)
mbc_colors <- c(
  "C1" = "#4477AA", "C2" = "#228833", "C3" = "#EE6677",
  "C4" = "#CCBB44", "C5" = "#AA3377", "C6" = "#66CCEE"
)
mbc_labels <- c(
  "C1" = "C1: Gradual Adopters (n = 1,367)",
  "C2" = "C2: Steady Calibrators (n = 1,582)",
  "C3" = "C3: Strong Calibrators (n = 859)",
  "C4" = "C4: High Performers, Low Reliance (n = 451)",
  "C5" = "C5: Heavy Adopters (n = 240)",
  "C6" = "C6: Early Heavy Users (n = 69)"
)

# LCGA: Wong palette (4 classes)
lcga_colors <- c(
  "LCGA-1" = "#E69F00", "LCGA-2" = "#56B4E9",
  "LCGA-3" = "#009E73", "LCGA-4" = "#CC79A7"
)
lcga_labels <- c(
  "LCGA-1" = "LCGA-1: Stagnant Under-Reliance (n = 2,662; 83.1%)",
  "LCGA-2" = "LCGA-2: Near-Calibrated Fluctuators (n = 75; 2.3%)",
  "LCGA-3" = "LCGA-3: Convergent Learners (n = 290; 9.1%)",
  "LCGA-4" = "LCGA-4: AI Benefit Emergence (n = 177; 5.5%)"
)

# MBC marker shapes (6 classes)
mbc_shapes <- c("C1" = 16, "C2" = 17, "C3" = 15, "C4" = 18, "C5" = 8, "C6" = 4)

# LCGA linetypes
lcga_linetypes <- c("LCGA-1" = "solid", "LCGA-2" = "dashed",
                    "LCGA-3" = "dotdash", "LCGA-4" = "dotted")

# --- Load data ----------------------------------------------------------------

data_dir <- file.path(dirname(output_dir), "..", "analysis", "outputs")
mbc_df <- read.csv(file.path(data_dir, "phase2_class_trajectories.csv"))
pred_df <- read.csv(file.path(data_dir, "phase3_rq3_prediction.csv"))

# Create class factor for MBC
mbc_df$class_id <- paste0("C", mbc_df$class)
mbc_df$class_id <- factor(mbc_df$class_id, levels = paste0("C", 1:6))

# LCGA data (hardcoded)
lcga_df <- data.frame(
  class = rep(1:4, each = 10),
  window = rep(1:10, 4),
  mean_gap = c(
    -0.698, -0.676, -0.653, -0.630, -0.615, -0.609, -0.585, -0.585, -0.569, -0.562,
    -0.214, -0.266, -0.252, -0.197, -0.144, -0.188, -0.193, -0.085, -0.127, -0.196,
    -0.573, -0.569, -0.495, -0.474, -0.417, -0.362, -0.334, -0.283, -0.277, -0.280,
    -0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543
  )
)
lcga_df$class_id <- paste0("LCGA-", lcga_df$class)
lcga_df$class_id <- factor(lcga_df$class_id, levels = paste0("LCGA-", 1:4))

# ABE data for Figure 5 (LCGA Class 4)
abe_df <- data.frame(
  window = 1:10,
  R_b  = c(0.090, 0.122, 0.148, 0.168, 0.186, 0.182, 0.177, 0.171, 0.161, 0.147),
  P_a  = c(0.391, 0.442, 0.480, 0.504, 0.560, 0.611, 0.604, 0.664, 0.696, 0.690),
  gap  = c(-0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543)
)

# ==============================================================================
# FIGURE 1: MBC Trajectories (2-panel: R_b left, P right)
# ==============================================================================
cat("Generating Figure 1: MBC Trajectories...\n")

panel_a <- ggplot(mbc_df, aes(x = window, y = mean_R_b,
                               color = class_id, shape = class_id)) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 2.2) +
  scale_color_manual(values = mbc_colors, labels = mbc_labels) +
  scale_shape_manual(values = mbc_shapes, labels = mbc_labels) +
  scale_x_continuous(breaks = 1:10) +
  labs(x = "Temporal Window", y = expression(italic(R[b]))) +
  annotate("text", x = 0.8, y = Inf, label = "(a)", vjust = 1.5, hjust = 0,
           size = 4.5, fontface = "bold", family = FONT_FAMILY) +
  theme_apa() +
  theme(legend.position = "none")

panel_b <- ggplot(mbc_df, aes(x = window, y = mean_P,
                               color = class_id, shape = class_id)) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 2.2) +
  scale_color_manual(values = mbc_colors, labels = mbc_labels) +
  scale_shape_manual(values = mbc_shapes, labels = mbc_labels) +
  scale_x_continuous(breaks = 1:10) +
  labs(x = "Temporal Window", y = expression(italic(P))) +
  annotate("text", x = 0.8, y = Inf, label = "(b)", vjust = 1.5, hjust = 0,
           size = 4.5, fontface = "bold", family = FONT_FAMILY) +
  theme_apa() +
  theme(legend.position = "none")

# Combine with patchwork and collect shared legend at bottom
fig1 <- (panel_a | panel_b) +
  plot_layout(guides = "collect") &
  theme(legend.position = "bottom",
        legend.key.height = unit(0.4, "cm"),
        legend.key.width  = unit(1.2, "cm")) &
  guides(color = guide_legend(nrow = 3, byrow = TRUE),
         shape = guide_legend(nrow = 3, byrow = TRUE))

ggsave(file.path(output_dir, "Figure_1_MBC_Trajectories.png"),
       fig1, width = 12, height = 5.5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_1_MBC_Trajectories.png\n")

# ==============================================================================
# FIGURE 2: MBC Calibration Gap
# ==============================================================================
cat("Generating Figure 2: MBC Calibration Gap...\n")

fig2 <- ggplot(mbc_df, aes(x = window, y = mean_gap,
                            color = class_id, shape = class_id)) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey50", linewidth = 0.5) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 2.2) +
  scale_color_manual(values = mbc_colors, labels = mbc_labels) +
  scale_shape_manual(values = mbc_shapes, labels = mbc_labels) +
  scale_x_continuous(breaks = 1:10) +
  annotate("text", x = 10.3, y = 0.015, label = "Perfect\nCalibration",
           hjust = 0, size = 2.8, color = "grey40", family = FONT_FAMILY,
           lineheight = 0.9) +
  coord_cartesian(clip = "off") +
  labs(x = "Temporal Window",
       y = expression("Calibration Gap (" * italic(R[b]) - italic(P) * ")")) +
  theme_apa() +
  theme(legend.position = "bottom",
        plot.margin = margin(8, 45, 8, 8),
        legend.key.height = unit(0.4, "cm"),
        legend.key.width  = unit(1.2, "cm")) +
  guides(color = guide_legend(nrow = 3, byrow = TRUE),
         shape = guide_legend(nrow = 3, byrow = TRUE))

ggsave(file.path(output_dir, "Figure_2_MBC_Gap_Trajectories.png"),
       fig2, width = 7, height = 5.5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_2_MBC_Gap_Trajectories.png\n")

# ==============================================================================
# FIGURE 3: LCGA Calibration Gap
# ==============================================================================
cat("Generating Figure 3: LCGA Calibration Gap...\n")

lcga_shapes <- c("LCGA-1" = 16, "LCGA-2" = 17, "LCGA-3" = 15, "LCGA-4" = 18)

fig3 <- ggplot(lcga_df, aes(x = window, y = mean_gap,
                             color = class_id, linetype = class_id,
                             shape = class_id)) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey50", linewidth = 0.5) +
  geom_line(aes(linewidth = class_id)) +
  geom_point(size = 2.2) +
  scale_color_manual(values = lcga_colors, labels = lcga_labels) +
  scale_linetype_manual(values = lcga_linetypes, labels = lcga_labels) +
  scale_shape_manual(values = lcga_shapes, labels = lcga_labels) +
  scale_linewidth_manual(values = c("LCGA-1" = 0.7, "LCGA-2" = 0.7,
                                     "LCGA-3" = 0.7, "LCGA-4" = 1.3),
                          labels = lcga_labels) +
  scale_x_continuous(breaks = 1:10) +
  annotate("text", x = 10.3, y = 0.015, label = "Perfect\nCalibration",
           hjust = 0, size = 2.8, color = "grey40", family = FONT_FAMILY,
           lineheight = 0.9) +
  coord_cartesian(clip = "off") +
  labs(x = "Temporal Window",
       y = expression("Calibration Gap (" * italic(R[b]) - italic(P) * ")")) +
  theme_apa() +
  theme(legend.position = "bottom",
        plot.margin = margin(8, 45, 8, 8),
        legend.key.height = unit(0.4, "cm"),
        legend.key.width  = unit(1.5, "cm")) +
  guides(color     = guide_legend(nrow = 2, byrow = TRUE),
         linetype  = guide_legend(nrow = 2, byrow = TRUE),
         shape     = guide_legend(nrow = 2, byrow = TRUE),
         linewidth = guide_legend(nrow = 2, byrow = TRUE))

ggsave(file.path(output_dir, "Figure_3_LCGA_Gap_Trajectories.png"),
       fig3, width = 8, height = 5.5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_3_LCGA_Gap_Trajectories.png\n")

# ==============================================================================
# FIGURE 4: Phase Portrait (R_b x P space)
# ==============================================================================
cat("Generating Figure 4: Phase Portrait...\n")

# Prepare trajectory data: start and end points
phase_df <- mbc_df %>%
  group_by(class_id) %>%
  arrange(window) %>%
  mutate(is_start = window == min(window),
         is_end   = window == max(window))

# Start / end points
starts <- phase_df %>% filter(is_start)
ends   <- phase_df %>% filter(is_end)

# Diagonal reference line limits
diag_range <- c(0, max(c(mbc_df$mean_R_b, mbc_df$mean_P), na.rm = TRUE) + 0.05)

# Axis limits for the phase portrait
x_lim <- c(0, 0.42)
y_lim <- c(0.42, 0.70)

fig4 <- ggplot() +
  # Under-reliance shading (above diagonal: P > R_b)
  # Polygon: top-left of the diagonal within the visible axes
  # Diagonal intersects right edge (x=0.42) at y=0.42 and bottom edge (y=0.42) at x=0.42
  # So the polygon is: (0, 0.42) -> (0, 0.70) -> (0.42, 0.70) -> (0.42, 0.42) minus the
  # tiny triangle at bottom-right where P < R_b. Since the diagonal just clips the corner,
  # the under-reliance zone polygon is everything above the diagonal:
  annotate("polygon",
           x = c(x_lim[1], x_lim[1], x_lim[2], x_lim[2]),
           y = c(x_lim[1], y_lim[2], y_lim[2], x_lim[2]),
           fill = "#DCEEF8", alpha = 0.3) +
  # Diagonal line: R_b = P
  geom_abline(intercept = 0, slope = 1, linetype = "dashed",
              color = "grey50", linewidth = 0.5) +
  # Trajectories with arrow at end
  geom_path(data = phase_df, aes(x = mean_R_b, y = mean_P, color = class_id,
                                  group = class_id),
            linewidth = 0.8,
            arrow = arrow(length = unit(0.15, "cm"), type = "closed"),
            lineend = "round") +
  # Start points (open circles)
  geom_point(data = starts, aes(x = mean_R_b, y = mean_P, color = class_id),
             shape = 21, size = 3, fill = "white", stroke = 1.2) +
  # End points (filled circles)
  geom_point(data = ends, aes(x = mean_R_b, y = mean_P, color = class_id),
             shape = 16, size = 3) +
  # Labels at endpoints using ggrepel
  geom_label_repel(data = ends,
                   aes(x = mean_R_b, y = mean_P, label = class_id, color = class_id),
                   size = 3, family = FONT_FAMILY,
                   fontface = "bold",
                   fill = "white", alpha = 0.85,
                   label.padding = unit(0.15, "lines"),
                   label.size = 0.3,
                   box.padding = unit(0.5, "lines"),
                   point.padding = unit(0.3, "lines"),
                   segment.color = "grey60",
                   segment.size = 0.3,
                   max.overlaps = 20,
                   seed = 42,
                   show.legend = FALSE) +
  # Zone label in the upper-left (safely within the shaded region)
  annotate("text", x = 0.02, y = 0.68, label = "Under-reliance zone",
           size = 3, color = "steelblue4", fontface = "italic",
           family = FONT_FAMILY, hjust = 0) +
  # Diagonal label near where it intersects visible area
  annotate("text", x = 0.38, y = 0.44, label = "italic(R[b]) == italic(P)",
           parse = TRUE, size = 3, color = "grey45", angle = 40,
           family = FONT_FAMILY) +
  scale_color_manual(values = mbc_colors, labels = mbc_labels) +
  scale_x_continuous(limits = x_lim, expand = c(0, 0.01)) +
  scale_y_continuous(limits = y_lim, expand = c(0, 0.01)) +
  labs(x = expression(italic(R[b]) ~ "(AI Reliance Behavior)"),
       y = expression(italic(P) ~ "(Adaptive Performance)")) +
  theme_apa() +
  theme(legend.position = "none",
        aspect.ratio = 0.8)

ggsave(file.path(output_dir, "Figure_4_Phase_Portrait.png"),
       fig4, width = 7, height = 6.5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_4_Phase_Portrait.png\n")

# ==============================================================================
# FIGURE 5: ABE Discovery (Scissors graph)
# ==============================================================================
cat("Generating Figure 5: ABE Discovery...\n")

abe_long <- data.frame(
  window = rep(1:10, 2),
  value  = c(abe_df$P_a, abe_df$R_b),
  metric = rep(c("P_adaptive", "R_b"), each = 10)
)

# Gap width data for ribbon
ribbon_df <- data.frame(
  window = 1:10,
  ymin = abe_df$R_b,
  ymax = abe_df$P_a
)

fig5 <- ggplot() +
  # Shaded area between curves
  geom_ribbon(data = ribbon_df, aes(x = window, ymin = ymin, ymax = ymax),
              fill = "#FFCCCC", alpha = 0.4) +
  # P_adaptive line (blue, solid, circles)
  geom_line(data = filter(abe_long, metric == "P_adaptive"),
            aes(x = window, y = value),
            color = "#2166AC", linewidth = 1, linetype = "solid") +
  geom_point(data = filter(abe_long, metric == "P_adaptive"),
             aes(x = window, y = value),
             color = "#2166AC", shape = 16, size = 3) +
  # R_b line (red, dashed, squares)
  geom_line(data = filter(abe_long, metric == "R_b"),
            aes(x = window, y = value),
            color = "#B2182B", linewidth = 1, linetype = "dashed") +
  geom_point(data = filter(abe_long, metric == "R_b"),
             aes(x = window, y = value),
             color = "#B2182B", shape = 15, size = 3) +
  # Gap arrows at W1 and W10
  annotate("segment", x = 1, xend = 1,
           y = abe_df$R_b[1] + 0.01, yend = abe_df$P_a[1] - 0.01,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "open"),
           color = "grey40", linewidth = 0.5) +
  annotate("text", x = 0.7, y = mean(c(abe_df$R_b[1], abe_df$P_a[1])),
           label = paste0("Gap = ", sprintf("%.2f", abs(abe_df$gap[1]))),
           size = 2.8, hjust = 1, family = FONT_FAMILY, color = "grey30") +
  annotate("segment", x = 10, xend = 10,
           y = abe_df$R_b[10] + 0.01, yend = abe_df$P_a[10] - 0.01,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "open"),
           color = "grey40", linewidth = 0.5) +
  annotate("text", x = 10.3, y = mean(c(abe_df$R_b[10], abe_df$P_a[10])),
           label = paste0("Gap = ", sprintf("%.2f", abs(abe_df$gap[10]))),
           size = 2.8, hjust = 0, family = FONT_FAMILY, color = "grey30") +
  # Metric labels (at right end)
  annotate("text", x = 10.4, y = abe_df$P_a[10] + 0.015,
           label = expression(italic(P)[adaptive]),
           size = 3.2, hjust = 0, color = "#2166AC", family = FONT_FAMILY) +
  annotate("text", x = 10.4, y = abe_df$R_b[10] - 0.015,
           label = expression(italic(R[b])),
           size = 3.2, hjust = 0, color = "#B2182B", family = FONT_FAMILY) +
  scale_x_continuous(breaks = 1:10) +
  scale_y_continuous(limits = c(0, 0.8), breaks = seq(0, 0.8, 0.1)) +
  coord_cartesian(clip = "off") +
  labs(x = "Temporal Window",
       y = "Score") +
  theme_apa() +
  theme(legend.position = "none",
        plot.margin = margin(8, 55, 8, 8))

ggsave(file.path(output_dir, "Figure_5_ABE_Discovery.png"),
       fig5, width = 7, height = 5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_5_ABE_Discovery.png\n")

# ==============================================================================
# FIGURE 6: Early Prediction Feature Importance
# ==============================================================================
cat("Generating Figure 6: Early Prediction Feature Importance...\n")

# Feature display names
feat_names <- c(
  "early_expl_rate"        = "Explanation Rate",
  "early_avg_expl_dur_s"   = "Avg. Explanation Duration",
  "early_R_b"              = "Early R_b",
  "early_gap"              = "Early Gap",
  "early_P"                = "Early P",
  "early_answer_change_rate" = "Answer Change Rate",
  "early_lecture_rate"     = "Lecture Rate"
)

pred_df$display_name <- feat_names[pred_df$feature]
pred_df$is_metacog <- pred_df$feature %in% c("early_expl_rate", "early_avg_expl_dur_s")
pred_df$bar_color <- ifelse(pred_df$is_metacog, "#4477AA", "#AAAAAA")

# Sort by importance
pred_df <- pred_df %>% arrange(mean_abs_coef)
pred_df$display_name <- factor(pred_df$display_name, levels = pred_df$display_name)

fig6 <- ggplot(pred_df, aes(x = mean_abs_coef, y = display_name, fill = is_metacog)) +
  geom_col(width = 0.65) +
  geom_text(aes(label = sprintf("%.3f", mean_abs_coef)),
            hjust = -0.15, size = 3, family = FONT_FAMILY, color = "grey30") +
  scale_fill_manual(values = c("TRUE" = "#4477AA", "FALSE" = "#BBBBBB"),
                    labels = c("TRUE" = "Metacognitive", "FALSE" = "Other"),
                    guide = "none") +
  scale_x_continuous(expand = expansion(mult = c(0, 0.2))) +
  labs(x = "Mean |Coefficient|", y = NULL) +
  # Bracket annotation for metacognitive features
  annotate("segment", x = max(pred_df$mean_abs_coef) * 1.12,
           xend = max(pred_df$mean_abs_coef) * 1.12,
           y = which(levels(pred_df$display_name) == "Avg. Explanation Duration"),
           yend = which(levels(pred_df$display_name) == "Explanation Rate"),
           color = "#4477AA", linewidth = 0.8) +
  annotate("text", x = max(pred_df$mean_abs_coef) * 1.15,
           y = mean(c(which(levels(pred_df$display_name) == "Avg. Explanation Duration"),
                      which(levels(pred_df$display_name) == "Explanation Rate"))),
           label = "Metacognitive\nEngagement",
           hjust = 0, size = 3, color = "#4477AA", family = FONT_FAMILY,
           fontface = "bold", lineheight = 0.9) +
  # Model info box
  annotate("label", x = max(pred_df$mean_abs_coef) * 0.55, y = 1.8,
           label = "Logistic Regression (L1)\nAccuracy: 0.78 | AUC: 0.84",
           size = 2.8, family = FONT_FAMILY, fill = "grey95",
           label.padding = unit(0.4, "lines"),
           color = "grey30") +
  coord_cartesian(clip = "off") +
  theme_apa() +
  theme(legend.position = "none",
        panel.grid.major.y = element_blank(),
        plot.margin = margin(8, 70, 8, 8))

ggsave(file.path(output_dir, "Figure_6_Early_Prediction.png"),
       fig6, width = 7, height = 4.5, dpi = DPI, bg = "white")
cat("  -> Saved Figure_6_Early_Prediction.png\n")

# ==============================================================================
cat("\nAll 6 figures generated successfully.\n")
cat("Output directory:", output_dir, "\n")
