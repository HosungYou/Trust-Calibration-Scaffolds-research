#!/usr/bin/env Rscript
# Figure 5 — AI Benefit Emergence (ABE): The Fifth Trajectory Pattern
#
# Two-panel layout: LCGA Class 4 (main) + MBC Phase 2B Class 4 (confirmation)
# P_adaptive (rising blue) vs R_b (flat/declining red), widening gap shaded
# Legend placed outside plot area to avoid occlusion

library(ggplot2)
library(patchwork)
library(scales)

# ── Paths ──────────────────────────────────────────────────────────────────────
base <- "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
out_dir <- file.path(base, "figures/ggplot2")

# ── LCGA Class 4 data (N=177, 5.5%) ───────────────────────────────────────────
lcga <- data.frame(
  window = 1:10,
  R_b = c(0.090, 0.151, 0.172, 0.188, 0.186, 0.194, 0.189, 0.164, 0.155, 0.147),
  P_adaptive = c(0.473, 0.511, 0.531, 0.551, 0.589, 0.642, 0.638, 0.678, 0.716, 0.722),
  Gap = c(-0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543)
)

# ── MBC Phase 2B Class 4 data (N=256, 5.7%) ───────────────────────────────────
mbc <- data.frame(
  window = 1:10,
  R_b = c(0.020, 0.053, 0.096, 0.125, 0.124, 0.154, 0.162, 0.174, 0.171, 0.171),
  P_adaptive = c(0.275, 0.341, 0.486, 0.562, 0.643, 0.676, 0.726, 0.789, 0.800, 0.852)
)

# ── Colors ─────────────────────────────────────────────────────────────────────
col_P  <- "#1565C0"   # deep blue for P_adaptive
col_Rb <- "#C62828"   # deep red for R_b
col_gap <- "#FFCDD2"  # light red for gap shading
col_gap_text <- "#B71C1C"

# ── Reshape for ggplot ─────────────────────────────────────────────────────────
lcga_long <- data.frame(
  window = rep(lcga$window, 2),
  value = c(lcga$P_adaptive, lcga$R_b),
  variable = rep(c("P_adaptive", "R_b"), each = 10)
)

mbc_long <- data.frame(
  window = rep(mbc$window, 2),
  value = c(mbc$P_adaptive, mbc$R_b),
  variable = rep(c("P_adaptive", "R_b"), each = 10)
)

# ══════════════════════════════════════════════════════════════════════════════
# Panel A: LCGA Class 4 (main figure)
# ══════════════════════════════════════════════════════════════════════════════

p_lcga <- ggplot() +
  # Shaded gap area
  geom_ribbon(data = lcga, aes(x = window, ymin = R_b, ymax = P_adaptive),
              fill = col_gap, alpha = 0.45) +
  # P_adaptive line (solid + circles)
  geom_line(data = lcga, aes(x = window, y = P_adaptive),
            color = col_P, linewidth = 1.2) +
  geom_point(data = lcga, aes(x = window, y = P_adaptive),
             color = col_P, size = 3, shape = 16) +
  # R_b line (dashed + squares)
  geom_line(data = lcga, aes(x = window, y = R_b),
            color = col_Rb, linewidth = 1.2, linetype = "dashed") +
  geom_point(data = lcga, aes(x = window, y = R_b),
             color = col_Rb, size = 3, shape = 15) +
  # Annotation: AI effectiveness rising
  annotate("text", x = 2.5, y = 0.68,
           label = "AI becomes more\neffective over time",
           color = col_P, size = 3.2, fontface = "bold", hjust = 0.5) +
  annotate("segment", x = 2.5, y = 0.64, xend = 3.0, yend = 0.545,
           color = col_P, linewidth = 0.6,
           arrow = arrow(length = unit(0.15, "cm"), type = "closed")) +
  # Annotation: Reliance stays flat
  annotate("text", x = 7.5, y = 0.06,
           label = "Learner reliance\nstays flat then declines",
           color = col_Rb, size = 3.2, fontface = "bold", hjust = 0.5) +
  annotate("segment", x = 7.0, y = 0.09, xend = 6.5, yend = 0.178,
           color = col_Rb, linewidth = 0.6,
           arrow = arrow(length = unit(0.15, "cm"), type = "closed")) +
  # Annotation: Growing missed opportunity
  annotate("label", x = 7.5, y = 0.42,
           label = "Growing\nmissed opportunity",
           color = col_gap_text, size = 3.0, fontface = "italic",
           fill = "white", label.padding = unit(0.3, "lines")) +
  # Gap arrows at W1 and W10
  annotate("segment", x = 0.6, y = lcga$P_adaptive[1], xend = 0.6, yend = lcga$R_b[1],
           color = col_gap_text, linewidth = 0.7,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "closed")) +
  annotate("text", x = 0.35, y = mean(c(lcga$P_adaptive[1], lcga$R_b[1])),
           label = paste0("Gap\n= ", sprintf("%.2f", abs(lcga$Gap[1]))),
           color = col_gap_text, size = 2.5, hjust = 1, fontface = "bold") +
  annotate("segment", x = 10.4, y = lcga$P_adaptive[10], xend = 10.4, yend = lcga$R_b[10],
           color = col_gap_text, linewidth = 0.7,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "closed")) +
  annotate("text", x = 10.65, y = mean(c(lcga$P_adaptive[10], lcga$R_b[10])),
           label = paste0("Gap\n= ", sprintf("%.2f", abs(lcga$Gap[10]))),
           color = col_gap_text, size = 2.5, hjust = 0, fontface = "bold") +
  scale_x_continuous(breaks = 1:10, expand = expansion(mult = c(0.08, 0.08))) +
  scale_y_continuous(limits = c(0, 0.82), labels = label_number(accuracy = 0.01)) +
  labs(x = expression(Temporal~Window~(tau)),
       y = "Proportion",
       subtitle = "LCGA Class 4 (N = 177, 5.5%)") +
  theme_minimal(base_size = 11, base_family = "serif") +
  theme(
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray92", linewidth = 0.3),
    axis.title = element_text(size = 12),
    plot.subtitle = element_text(size = 11, face = "bold", hjust = 0.5),
    plot.margin = margin(10, 15, 10, 10)
  )

# ══════════════════════════════════════════════════════════════════════════════
# Panel B: MBC Phase 2B Class 4 (cross-method confirmation)
# ══════════════════════════════════════════════════════════════════════════════

mbc_gap_w1 <- abs(mbc$P_adaptive[1] - mbc$R_b[1])
mbc_gap_w10 <- abs(mbc$P_adaptive[10] - mbc$R_b[10])

p_mbc <- ggplot() +
  # Shaded gap
  geom_ribbon(data = mbc, aes(x = window, ymin = R_b, ymax = P_adaptive),
              fill = col_gap, alpha = 0.45) +
  # P_adaptive
  geom_line(data = mbc, aes(x = window, y = P_adaptive),
            color = col_P, linewidth = 1.2) +
  geom_point(data = mbc, aes(x = window, y = P_adaptive),
             color = col_P, size = 3, shape = 16) +
  # R_b
  geom_line(data = mbc, aes(x = window, y = R_b),
            color = col_Rb, linewidth = 1.2, linetype = "dashed") +
  geom_point(data = mbc, aes(x = window, y = R_b),
             color = col_Rb, size = 3, shape = 15) +
  # Gap arrows
  annotate("segment", x = 0.6, y = mbc$P_adaptive[1], xend = 0.6, yend = mbc$R_b[1],
           color = col_gap_text, linewidth = 0.7,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "closed")) +
  annotate("text", x = 0.35, y = mean(c(mbc$P_adaptive[1], mbc$R_b[1])),
           label = paste0("Gap = ", sprintf("%.2f", mbc_gap_w1)),
           color = col_gap_text, size = 2.5, hjust = 1, fontface = "bold") +
  annotate("segment", x = 10.4, y = mbc$P_adaptive[10], xend = 10.4, yend = mbc$R_b[10],
           color = col_gap_text, linewidth = 0.7,
           arrow = arrow(length = unit(0.1, "cm"), ends = "both", type = "closed")) +
  annotate("text", x = 10.4, y = mean(c(mbc$P_adaptive[10], mbc$R_b[10])) + 0.04,
           label = paste0("Gap\n= ", sprintf("%.2f", mbc_gap_w10)),
           color = col_gap_text, size = 2.5, hjust = 0.5, fontface = "bold") +
  scale_x_continuous(breaks = 1:10, expand = expansion(mult = c(0.08, 0.12))) +
  scale_y_continuous(limits = c(0, 0.92), labels = label_number(accuracy = 0.01)) +
  labs(x = expression(Temporal~Window~(tau)),
       y = "Proportion",
       subtitle = "MBC Phase 2B Class 4 (N = 256, 5.7%)") +
  theme_minimal(base_size = 11, base_family = "serif") +
  theme(
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray92", linewidth = 0.3),
    axis.title = element_text(size = 12),
    plot.subtitle = element_text(size = 11, face = "bold", hjust = 0.5),
    plot.margin = margin(10, 20, 10, 10)
  )

# ══════════════════════════════════════════════════════════════════════════════
# Combined with shared legend at bottom
# ══════════════════════════════════════════════════════════════════════════════

# Create a dummy plot just for the legend
legend_data <- data.frame(
  x = c(1, 1),
  y = c(0.5, 0.2),
  variable = factor(c("P[adaptive]~(AI~effectiveness)", "R[b]~(learner~reliance)"),
                     levels = c("P[adaptive]~(AI~effectiveness)", "R[b]~(learner~reliance)"))
)

p_legend <- ggplot(legend_data, aes(x = x, y = y, color = variable, linetype = variable, shape = variable)) +
  geom_line(linewidth = 1.2) +
  geom_point(size = 3) +
  scale_color_manual(values = c(col_P, col_Rb),
                     labels = c(expression(italic(P)[adaptive]~"(AI effectiveness)"),
                                expression(italic(R)[b]~"(learner reliance)"))) +
  scale_linetype_manual(values = c("solid", "dashed"),
                        labels = c(expression(italic(P)[adaptive]~"(AI effectiveness)"),
                                   expression(italic(R)[b]~"(learner reliance)"))) +
  scale_shape_manual(values = c(16, 15),
                     labels = c(expression(italic(P)[adaptive]~"(AI effectiveness)"),
                                expression(italic(R)[b]~"(learner reliance)"))) +
  guides(color = guide_legend(title = NULL, nrow = 1),
         linetype = guide_legend(title = NULL, nrow = 1),
         shape = guide_legend(title = NULL, nrow = 1)) +
  theme_void(base_family = "serif") +
  theme(legend.position = "bottom",
        legend.text = element_text(size = 10),
        legend.key.width = unit(2.5, "cm"))

# Extract legend
library(grid)
library(gtable)
g <- ggplotGrob(p_legend)
legend_grob <- g$grobs[[which(sapply(g$grobs, function(x) x$name) == "guide-box")]]

# Combine panels
combined <- (p_lcga | p_mbc) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(size = 13, face = "bold", family = "serif"))

# Save with legend below
png(file.path(out_dir, "Figure_5_ABE_Discovery.png"),
    width = 10, height = 5.5, units = "in", res = 300, bg = "white")

# Layout: panels on top, legend at bottom
pushViewport(viewport(layout = grid.layout(2, 1, heights = unit(c(1, 0.08), c("null", "null")))))
pushViewport(viewport(layout.pos.row = 1))
print(combined, newpage = FALSE)
popViewport()
pushViewport(viewport(layout.pos.row = 2))
grid.draw(legend_grob)
popViewport()
popViewport()

dev.off()
cat("Saved: Figure_5_ABE_Discovery.png\n")

# Also save to main figures dir
file.copy(file.path(out_dir, "Figure_5_ABE_Discovery.png"),
          file.path(base, "figures/Figure_5_ABE_Discovery.png"),
          overwrite = TRUE)
cat("Copied to main figures directory\n")
