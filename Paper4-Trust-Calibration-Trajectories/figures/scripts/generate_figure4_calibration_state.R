#!/usr/bin/env Rscript
# ==============================================================================
# Figure 4: Calibration State Space (Reconceptualized Phase Portrait)
# Trust Calibration Scaffolds — Trajectory Paper
#
# X-axis: Behavioral Reliance (R_b)
# Y-axis: Calibration Gap (R_b - P)  — 0 = perfect calibration
#         Gap < 0: under-reliance | Gap > 0: over-reliance
#
# Generates:
#   Figure_4A_Calibration_StateSpace.png       (single panel, all 6 classes)
#   Figure_4B_Calibration_StateSpace_Faceted.png (2x3 faceted, ghost traces)
#
# APA 7th style: No embedded title, serif font, 300 DPI
# ==============================================================================

library(ggplot2)
library(dplyr)
library(ggrepel)
library(scales)

# --- Global settings ----------------------------------------------------------

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

DPI         <- 300
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
      legend.position  = "right",
      plot.margin      = margin(8, 12, 8, 8)
    )
}

# --- Color palette (Tol bright) ----------------------------------------------

class_colors <- c(
  "1" = "#4477AA", "2" = "#228833", "3" = "#EE6677",
  "4" = "#CCBB44", "5" = "#AA3377", "6" = "#66CCEE"
)

class_labels <- c(
  "1" = "C1: Gradual Adopters (n=1,367)",
  "2" = "C2: Steady Calibrators (n=1,582)",
  "3" = "C3: Strong Calibrators (n=859)",
  "4" = "C4: High Performers, Low Reliance (n=451)",
  "5" = "C5: Heavy Adopters (n=240)",
  "6" = "C6: Early Heavy Users (n=69)"
)

# Short labels for the legend (Figure A)
class_labels_short <- c(
  "1" = "C1: Gradual Adopters",
  "2" = "C2: Steady Calibrators",
  "3" = "C3: Strong Calibrators",
  "4" = "C4: High Perf., Low Reliance",
  "5" = "C5: Heavy Adopters",
  "6" = "C6: Early Heavy Users"
)

# --- Load data ----------------------------------------------------------------

data_dir <- file.path(dirname(output_dir), "..", "analysis", "outputs")
df <- read.csv(file.path(data_dir, "phase2_class_trajectories.csv"))
cat("Data loaded:", nrow(df), "rows\n")

# --- Prepare data -------------------------------------------------------------

df$class_f <- as.character(df$class)
df$class_label <- factor(class_labels[df$class_f], levels = class_labels)

df <- df %>% arrange(class, window)

# Start and end points
starts <- df %>% filter(window == 1)
ends   <- df %>% filter(window == 10)

# Shared axis limits
x_lim <- c(0, 0.40)
y_lim <- c(-0.65, 0.10)

# ==============================================================================
# Figure A: Single-panel (all 6 classes overlaid)
# ==============================================================================
cat("Generating Figure 4A: Calibration State Space (single panel)...\n")

fig4a <- ggplot() +
  # 1. Zone shading — Over-reliance (above 0): light red
  annotate("rect",
           xmin = x_lim[1], xmax = x_lim[2],
           ymin = 0, ymax = y_lim[2],
           fill = "#FFCCCC", alpha = 0.06) +
  # 2. Zone shading — Under-reliance (below 0): light blue
  annotate("rect",
           xmin = x_lim[1], xmax = x_lim[2],
           ymin = y_lim[1], ymax = 0,
           fill = "#CCE0FF", alpha = 0.06) +
  # 3. Perfect Calibration reference line (Gap = 0)
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey40",
             linewidth = 0.5) +
  # 4. Zone labels
  annotate("text", x = x_lim[2] - 0.005, y = 0.06,
           label = "Over-reliance", color = "#CC4444",
           size = 3.2, family = FONT_FAMILY, fontface = "italic",
           hjust = 1, alpha = 0.7) +
  annotate("text", x = x_lim[2] - 0.005, y = -0.06,
           label = "Under-reliance", color = "#4466AA",
           size = 3.2, family = FONT_FAMILY, fontface = "italic",
           hjust = 1, alpha = 0.7) +
  # 5. "Perfect Calibration" label on the reference line
  annotate("text", x = 0.005, y = 0.018,
           label = "Perfect Calibration", color = "grey40",
           size = 2.8, family = FONT_FAMILY, fontface = "italic",
           hjust = 0, alpha = 0.8) +
  # 6. Trajectory paths with terminal arrow
  geom_path(data = df,
            aes(x = mean_R_b, y = mean_gap, color = class_f, group = class_f),
            linewidth = 0.8,
            arrow = arrow(length = unit(0.12, "cm"), type = "closed"),
            lineend = "round") +
  # 7. All 10 time-point dots (small)
  geom_point(data = df,
             aes(x = mean_R_b, y = mean_gap, color = class_f),
             size = 1.5) +
  # 8. Start point: open circle (window 1)
  geom_point(data = starts,
             aes(x = mean_R_b, y = mean_gap, color = class_f),
             shape = 21, fill = "white", size = 3, stroke = 1.0) +
  # 9. End point: filled circle (window 10)
  geom_point(data = ends,
             aes(x = mean_R_b, y = mean_gap, fill = class_f),
             shape = 21, size = 3, stroke = 0.5, color = "grey30") +
  # 10. Class labels at endpoints via ggrepel
  geom_label_repel(data = ends,
                   aes(x = mean_R_b, y = mean_gap,
                       label = class_labels_short[class_f],
                       color = class_f),
                   size = 2.6, family = FONT_FAMILY,
                   fill = alpha("white", 0.85),
                   label.size = 0.2,
                   box.padding = 0.5,
                   point.padding = 0.3,
                   segment.size = 0.3,
                   segment.color = "grey60",
                   max.overlaps = 20,
                   seed = 42,
                   show.legend = FALSE) +
  # Color and fill scales
  scale_color_manual(values = class_colors,
                     labels = class_labels_short,
                     name = "Trajectory Class") +
  scale_fill_manual(values = class_colors,
                    labels = class_labels_short,
                    name = "Trajectory Class") +
  # Axes
  scale_x_continuous(limits = x_lim, expand = c(0.02, 0),
                     breaks = seq(0, 0.40, by = 0.05),
                     labels = label_number(accuracy = 0.01)) +
  scale_y_continuous(limits = y_lim, expand = c(0.02, 0),
                     breaks = seq(-0.60, 0.10, by = 0.10),
                     labels = label_number(accuracy = 0.01)) +
  labs(x = expression("Behavioral Reliance (" * italic(R)[italic(b)] * ")"),
       y = expression("Calibration Gap (" * italic(R)[italic(b)] ~ "\u2212" ~ italic(P) * ")")) +
  # Theme
  theme_apa() +
  theme(
    legend.position  = "right",
    legend.title     = element_text(size = 9, face = "bold", family = FONT_FAMILY),
    legend.text      = element_text(size = 8, family = FONT_FAMILY),
    legend.key.size  = unit(0.8, "lines")
  ) +
  guides(color = guide_legend(override.aes = list(size = 2, linewidth = 0.8)),
         fill  = "none")

# Save Figure A
out_a <- file.path(output_dir, "Figure_4A_Calibration_StateSpace.png")
ggsave(out_a, fig4a, width = 7, height = 5.5, dpi = DPI, bg = "white")
cat("  -> Saved", out_a, "\n")


# ==============================================================================
# Figure B: Faceted 2x3 (one panel per class, ghost traces)
# ==============================================================================
cat("Generating Figure 4B: Calibration State Space (faceted)...\n")

# Build a "ghost" data frame: for each focal class panel, include all OTHER classes
ghost_list <- lapply(unique(df$class_f), function(focal) {
  other <- df %>% filter(class_f != focal)
  other$focal_class <- focal
  other
})
ghost_df <- bind_rows(ghost_list)
ghost_df$focal_label <- factor(class_labels[ghost_df$focal_class],
                               levels = class_labels)

# Focal data: each class in its own facet
df_focal <- df
df_focal$focal_label <- df_focal$class_label

starts_focal <- starts
starts_focal$focal_label <- factor(class_labels[starts_focal$class_f],
                                   levels = class_labels)

ends_focal <- ends
ends_focal$focal_label <- factor(class_labels[ends_focal$class_f],
                                 levels = class_labels)

# Ghost start/end points
ghost_starts <- ghost_df %>% filter(window == 1)
ghost_ends   <- ghost_df %>% filter(window == 10)

fig4b <- ggplot() +
  # 1. Zone shading — Over-reliance (above 0)
  annotate("rect",
           xmin = x_lim[1], xmax = x_lim[2],
           ymin = 0, ymax = y_lim[2],
           fill = "#FFCCCC", alpha = 0.06) +
  # 2. Zone shading — Under-reliance (below 0)
  annotate("rect",
           xmin = x_lim[1], xmax = x_lim[2],
           ymin = y_lim[1], ymax = 0,
           fill = "#CCE0FF", alpha = 0.06) +
  # 3. Perfect Calibration reference line
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey40",
             linewidth = 0.5) +
  # 4. Ghost traces (all other classes, thin grey)
  geom_path(data = ghost_df,
            aes(x = mean_R_b, y = mean_gap, group = class_f),
            color = "grey70", linewidth = 0.4, alpha = 0.15) +
  geom_point(data = ghost_df,
             aes(x = mean_R_b, y = mean_gap, group = class_f),
             color = "grey70", size = 0.5, alpha = 0.15) +
  # 5. Focal trajectory path with arrow
  geom_path(data = df_focal,
            aes(x = mean_R_b, y = mean_gap, color = class_f, group = class_f),
            linewidth = 0.9,
            arrow = arrow(length = unit(0.12, "cm"), type = "closed"),
            lineend = "round") +
  # 6. Focal time-point dots
  geom_point(data = df_focal,
             aes(x = mean_R_b, y = mean_gap, color = class_f),
             size = 1.5) +
  # 7. Start point: open circle
  geom_point(data = starts_focal,
             aes(x = mean_R_b, y = mean_gap, color = class_f),
             shape = 21, fill = "white", size = 3, stroke = 1.0) +
  # 8. End point: filled circle
  geom_point(data = ends_focal,
             aes(x = mean_R_b, y = mean_gap, fill = class_f),
             shape = 21, size = 3, stroke = 0.5, color = "grey30") +
  # 9. Window labels at start and end
  geom_text(data = starts_focal,
            aes(x = mean_R_b, y = mean_gap, label = "1"),
            size = 2.5, family = FONT_FAMILY, color = "grey20",
            nudge_x = -0.012, nudge_y = 0.018) +
  geom_text(data = ends_focal,
            aes(x = mean_R_b, y = mean_gap, label = "10"),
            size = 2.5, family = FONT_FAMILY, color = "grey20",
            nudge_x = 0.012, nudge_y = 0.018) +
  # Color and fill scales
  scale_color_manual(values = class_colors) +
  scale_fill_manual(values = class_colors) +
  # Axes
  scale_x_continuous(limits = x_lim, expand = c(0.02, 0),
                     breaks = seq(0, 0.40, by = 0.10),
                     labels = label_number(accuracy = 0.01)) +
  scale_y_continuous(limits = y_lim, expand = c(0.02, 0),
                     breaks = seq(-0.60, 0.10, by = 0.10),
                     labels = label_number(accuracy = 0.01)) +
  labs(x = expression("Behavioral Reliance (" * italic(R)[italic(b)] * ")"),
       y = expression("Calibration Gap (" * italic(R)[italic(b)] ~ "\u2212" ~ italic(P) * ")")) +
  # Facet: 2 rows x 3 columns
  facet_wrap(~ focal_label, ncol = 3) +
  # Theme
  theme_apa() +
  theme(
    legend.position  = "none",
    strip.text       = element_text(size = 9, face = "bold", family = FONT_FAMILY),
    panel.spacing    = unit(0.8, "lines")
  )

# Save Figure B
out_b <- file.path(output_dir, "Figure_4B_Calibration_StateSpace_Faceted.png")
ggsave(out_b, fig4b, width = 10, height = 7, dpi = DPI, bg = "white")
cat("  -> Saved", out_b, "\n")

cat("Done. Both figures generated.\n")
