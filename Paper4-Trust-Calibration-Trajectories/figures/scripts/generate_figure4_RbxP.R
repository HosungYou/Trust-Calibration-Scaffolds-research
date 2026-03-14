#!/usr/bin/env Rscript
# Figure 4 — Phase Portrait in R_b × P Space
# Faceted 2×3 with grey ghost traces
# No R_b=P diagonal (scales are incommensurable)

library(ggplot2)
library(ggrepel)
library(scales)

# ── Paths ──────────────────────────────────────────────────────────────────────
base <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
data_path <- file.path(base, "analysis/outputs/phase2_class_trajectories.csv")
out_dir <- file.path(base, "figures/ggplot2")

# ── Data ───────────────────────────────────────────────────────────────────────
df <- read.csv(data_path)

# ── Tol bright palette ─────────────────────────────────────────────────────────
tol_colors <- c(
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

df$class_f <- factor(df$class, levels = 1:6, labels = class_labels)

# Ghost traces: all classes for background
ghost <- df[, c("class", "window", "mean_R_b", "mean_P")]

# ── Start/end points ──────────────────────────────────────────────────────────
starts <- df[df$window == 1, ]
ends   <- df[df$window == 10, ]

# Arrow segments (window 9 → 10)
arrows_df <- merge(
  df[df$window == 9, c("class", "class_f", "mean_R_b", "mean_P")],
  df[df$window == 10, c("class", "class_f", "mean_R_b", "mean_P")],
  by = c("class", "class_f"), suffixes = c("_from", "_to")
)

# ══════════════════════════════════════════════════════════════════════════════
# Figure 4A: Single panel
# ══════════════════════════════════════════════════════════════════════════════

p4a <- ggplot(df, aes(x = mean_R_b, y = mean_P, color = factor(class))) +
  # Trajectories
  geom_path(aes(group = class), linewidth = 0.9) +
  geom_point(aes(group = class), size = 2) +
  # Start markers (open)
  geom_point(data = starts, shape = 21, size = 4, stroke = 1.2,
             aes(fill = factor(class)), color = "white") +
  geom_point(data = starts, shape = 21, size = 4, stroke = 1.2, fill = NA) +
  # End markers (filled large)
  geom_point(data = ends, size = 5) +
  # Terminal arrows
  geom_segment(data = arrows_df,
               aes(x = mean_R_b_from, y = mean_P_from,
                   xend = mean_R_b_to, yend = mean_P_to,
                   color = factor(class)),
               arrow = arrow(length = unit(0.15, "cm"), type = "closed"),
               linewidth = 1.0, show.legend = FALSE) +
  # End labels
  geom_text_repel(data = ends,
                  aes(label = paste0("C", class)),
                  size = 3.2, fontface = "bold",
                  box.padding = 0.4, point.padding = 0.3,
                  min.segment.length = 0.2, seed = 42,
                  show.legend = FALSE) +
  scale_color_manual(values = tol_colors, labels = class_labels, name = "Trajectory Class") +
  scale_fill_manual(values = tol_colors, guide = "none") +
  scale_x_continuous(labels = label_number(accuracy = 0.01)) +
  scale_y_continuous(labels = label_number(accuracy = 0.01)) +
  labs(x = expression(Behavioral~Reliance~(italic(R)[b])),
       y = expression(Performance~(italic(P)))) +
  theme_minimal(base_size = 11, base_family = "serif") +
  theme(
    legend.position = "right",
    legend.text = element_text(size = 8),
    legend.title = element_text(size = 9, face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray90", linewidth = 0.3),
    axis.title = element_text(size = 12),
    plot.margin = margin(10, 10, 10, 10)
  )

ggsave(file.path(out_dir, "Figure_4A_RbxP_SinglePanel.png"),
       p4a, width = 7, height = 5.5, dpi = 300, bg = "white")
cat("Saved: Figure_4A_RbxP_SinglePanel.png\n")

# ══════════════════════════════════════════════════════════════════════════════
# Figure 4B: Faceted 2×3 with ghost traces
# ══════════════════════════════════════════════════════════════════════════════

# Build ghost data for each facet
ghost_list <- list()
for (cls in 1:6) {
  g <- ghost
  g$focal_class <- cls
  g$class_f <- factor(cls, levels = 1:6, labels = class_labels)
  ghost_list[[cls]] <- g
}
ghost_all <- do.call(rbind, ghost_list)

# Focal data
focal <- df
focal$focal_class <- focal$class

# Focal starts/ends
focal_starts <- starts
focal_starts$focal_class <- focal_starts$class
focal_ends <- ends
focal_ends$focal_class <- focal_ends$class
focal_arrows <- arrows_df
focal_arrows$focal_class <- focal_arrows$class

p4b <- ggplot() +
  # Ghost traces (all classes in grey)
  geom_path(data = ghost_all,
            aes(x = mean_R_b, y = mean_P, group = class),
            color = "gray75", linewidth = 0.4, alpha = 0.5) +
  geom_point(data = ghost_all,
             aes(x = mean_R_b, y = mean_P, group = class),
             color = "gray80", size = 0.5, alpha = 0.4) +
  # Focal trajectory
  geom_path(data = focal,
            aes(x = mean_R_b, y = mean_P, color = factor(class)),
            linewidth = 1.0) +
  geom_point(data = focal,
             aes(x = mean_R_b, y = mean_P, color = factor(class)),
             size = 2.2) +
  # Start markers (open)
  geom_point(data = focal_starts,
             aes(x = mean_R_b, y = mean_P),
             shape = 21, size = 4.5, stroke = 1.3, fill = "white",
             color = "gray30") +
  # End markers (filled)
  geom_point(data = focal_ends,
             aes(x = mean_R_b, y = mean_P, color = factor(class)),
             size = 5) +
  # Terminal arrows
  geom_segment(data = focal_arrows,
               aes(x = mean_R_b_from, y = mean_P_from,
                   xend = mean_R_b_to, yend = mean_P_to,
                   color = factor(class)),
               arrow = arrow(length = unit(0.15, "cm"), type = "closed"),
               linewidth = 1.0, show.legend = FALSE) +
  # Window labels at start and end
  geom_text(data = focal_starts,
            aes(x = mean_R_b, y = mean_P, label = "1"),
            size = 2.5, vjust = 2.5, color = "gray40") +
  geom_text(data = focal_ends,
            aes(x = mean_R_b, y = mean_P, label = "10"),
            size = 2.5, vjust = -1.5, color = "gray40") +
  facet_wrap(~ class_f, ncol = 3) +
  scale_color_manual(values = tol_colors, guide = "none") +
  scale_x_continuous(labels = label_number(accuracy = 0.01)) +
  scale_y_continuous(labels = label_number(accuracy = 0.01)) +
  labs(x = expression(Behavioral~Reliance~(italic(R)[b])),
       y = expression(Performance~(italic(P)))) +
  theme_minimal(base_size = 11, base_family = "serif") +
  theme(
    strip.text = element_text(size = 10, face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray90", linewidth = 0.3),
    axis.title = element_text(size = 12),
    plot.margin = margin(10, 10, 10, 10)
  )

ggsave(file.path(out_dir, "Figure_4B_RbxP_Faceted.png"),
       p4b, width = 10, height = 7, dpi = 300, bg = "white")
cat("Saved: Figure_4B_RbxP_Faceted.png\n")

# ══════════════════════════════════════════════════════════════════════════════
# Figure 4C: Faceted with INDEPENDENT y-axis scales per class
# This zooms into each class's actual movement range
# ══════════════════════════════════════════════════════════════════════════════

p4c <- ggplot() +
  # Ghost traces
  geom_path(data = ghost_all,
            aes(x = mean_R_b, y = mean_P, group = class),
            color = "gray80", linewidth = 0.3, alpha = 0.3) +
  # Focal trajectory
  geom_path(data = focal,
            aes(x = mean_R_b, y = mean_P, color = factor(class)),
            linewidth = 1.0) +
  geom_point(data = focal,
             aes(x = mean_R_b, y = mean_P, color = factor(class)),
             size = 2.2) +
  # Start markers
  geom_point(data = focal_starts,
             aes(x = mean_R_b, y = mean_P),
             shape = 21, size = 4.5, stroke = 1.3, fill = "white",
             color = "gray30") +
  # End markers
  geom_point(data = focal_ends,
             aes(x = mean_R_b, y = mean_P, color = factor(class)),
             size = 5) +
  # Arrows
  geom_segment(data = focal_arrows,
               aes(x = mean_R_b_from, y = mean_P_from,
                   xend = mean_R_b_to, yend = mean_P_to,
                   color = factor(class)),
               arrow = arrow(length = unit(0.15, "cm"), type = "closed"),
               linewidth = 1.0, show.legend = FALSE) +
  # Window labels
  geom_text(data = focal_starts,
            aes(x = mean_R_b, y = mean_P, label = "1"),
            size = 2.5, vjust = 2.5, color = "gray40") +
  geom_text(data = focal_ends,
            aes(x = mean_R_b, y = mean_P, label = "10"),
            size = 2.5, vjust = -1.5, color = "gray40") +
  facet_wrap(~ class_f, ncol = 3, scales = "free") +
  scale_color_manual(values = tol_colors, guide = "none") +
  scale_x_continuous(labels = label_number(accuracy = 0.01)) +
  scale_y_continuous(labels = label_number(accuracy = 0.01)) +
  labs(x = expression(Behavioral~Reliance~(italic(R)[b])),
       y = expression(Performance~(italic(P)))) +
  theme_minimal(base_size = 11, base_family = "serif") +
  theme(
    strip.text = element_text(size = 10, face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray90", linewidth = 0.3),
    axis.title = element_text(size = 12),
    plot.margin = margin(10, 10, 10, 10)
  )

ggsave(file.path(out_dir, "Figure_4C_RbxP_Faceted_FreeScales.png"),
       p4c, width = 10, height = 7, dpi = 300, bg = "white")
cat("Saved: Figure_4C_RbxP_Faceted_FreeScales.png\n")

cat("\nDone. 3 versions generated.\n")
