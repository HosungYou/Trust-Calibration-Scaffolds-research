"""
Generate publication-quality figures for the Trust Calibration Trajectory paper.
Target journal: Computers in Human Behavior
APA style: no figure titles (titles go in captions below figures)
"""

import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path

# Import shared figure style module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_style import *

# ── Apply unified style ──────────────────────────────────────────────────────
apply_style()

# ── Load data ─────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_DIR / "phase2_class_trajectories.csv")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 1 – Mean Behavioral Reliance and Performance Trajectories by Class
# ══════════════════════════════════════════════════════════════════════════════
fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(12, 5))

for cls in sorted(df['class'].unique()):
    sub = df[df['class'] == cls].sort_values('window')
    ax1a.plot(sub['window'], sub['mean_R_b'],
              color=MBC_COLORS[cls], marker=MBC_MARKERS[cls],
              linestyle=MBC_LINESTYLES[cls],
              markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
              label=MBC_LABELS[cls])
    ax1b.plot(sub['window'], sub['mean_P'],
              color=MBC_COLORS[cls], marker=MBC_MARKERS[cls],
              linestyle=MBC_LINESTYLES[cls],
              markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
              label=MBC_LABELS[cls])

# Left panel – R_b
ax1a.set_xlabel("Temporal Window")
ax1a.set_ylabel("Behavioral Reliance ($R_b$)")
ax1a.set_xlim(0.5, 10.5)
ax1a.set_ylim(0, 0.40)
ax1a.set_xticks(WINDOWS)
ax1a.text(-0.12, 1.06, '(a)', transform=ax1a.transAxes,
           fontsize=PANEL_LABEL_SIZE, fontweight='bold', va='top')
add_y_gridlines(ax1a)

# Right panel – P
ax1b.set_xlabel("Temporal Window")
ax1b.set_ylabel("Performance ($P$)")
ax1b.set_xlim(0.5, 10.5)
ax1b.set_ylim(0.45, 0.70)
ax1b.set_xticks(WINDOWS)
ax1b.text(-0.12, 1.06, '(b)', transform=ax1b.transAxes,
           fontsize=PANEL_LABEL_SIZE, fontweight='bold', va='top')
add_y_gridlines(ax1b)

# Shared legend below both panels
handles, labels = ax1a.get_legend_handles_labels()
fig1.legend(handles, labels, loc='lower center', ncol=3,
            frameon=True, edgecolor='lightgray', fancybox=False,
            bbox_to_anchor=(0.5, -0.12))

fig1.tight_layout(rect=[0, 0.08, 1, 1])
save_figure(fig1, "Figure_1_MBC_Trajectories.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 – Calibration Gap Trajectories by Class (Model-Based Clustering)
# ══════════════════════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(8, 5))

for cls in sorted(df['class'].unique()):
    sub = df[df['class'] == cls].sort_values('window')
    ax2.plot(sub['window'], sub['mean_gap'],
             color=MBC_COLORS[cls], marker=MBC_MARKERS[cls],
             linestyle=MBC_LINESTYLES[cls],
             markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label=MBC_LABELS[cls])
    # Light shaded band: mean_gap +/- approximate SD
    # gap = R_b - P, so sd_gap ~ sqrt(sd_R_b^2 + sd_P^2)  (independence approx)
    sd_gap = np.sqrt(sub['sd_R_b'].values**2 + sub['sd_P'].values**2)
    upper = sub['mean_gap'].values + sd_gap
    lower = sub['mean_gap'].values - sd_gap
    ax2.fill_between(sub['window'].values, lower, upper,
                     color=MBC_COLORS[cls], alpha=0.15)

# Calibration reference line
ax2.axhline(y=0, color='black', linestyle='--', linewidth=1.0,
            alpha=REFERENCE_LINE_ALPHA)
ax2.text(10.3, 0.012, "Perfect Calibration", fontsize=ANNOTATION_SIZE,
         va='bottom', ha='right', style='italic', color='black', alpha=0.7)

ax2.set_xlabel("Temporal Window")
ax2.set_ylabel("Calibration Gap ($R_b - P$)")
ax2.set_xlim(0.5, 10.5)
ax2.set_ylim(-0.65, 0.05)
ax2.set_xticks(WINDOWS)
add_y_gridlines(ax2)

ax2.legend(loc='lower right', frameon=True, edgecolor='lightgray',
           fancybox=False, fontsize=LEGEND_FONT_SIZE)

fig2.tight_layout()
save_figure(fig2, "Figure_2_MBC_Gap_Trajectories.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 – Calibration Gap Trajectories by Class (LCGA)
# ══════════════════════════════════════════════════════════════════════════════

# Hardcoded LCGA 4-class gap trajectories
lcga_data = {
    1: [-0.698, -0.676, -0.653, -0.630, -0.615, -0.609, -0.585, -0.585, -0.569, -0.562],
    2: [-0.214, -0.266, -0.252, -0.197, -0.144, -0.188, -0.193, -0.085, -0.127, -0.196],
    3: [-0.573, -0.569, -0.495, -0.474, -0.417, -0.362, -0.334, -0.283, -0.277, -0.280],
    4: [-0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543],
}

fig3, ax3 = plt.subplots(figsize=(8, 5))

for cls in [1, 2, 3, 4]:
    vals = lcga_data[cls]
    # Class 4 (ABE) gets special emphasis
    if cls == 4:
        ax3.plot(WINDOWS, vals,
                 color=LCGA_COLORS[cls], marker=LCGA_MARKERS[cls],
                 linestyle=LCGA_LINESTYLES[cls],
                 markersize=EMPHASIS_MARKER_SIZE,
                 linewidth=EMPHASIS_LINE_WIDTH,
                 label=LCGA_LABELS[cls], zorder=5)
    else:
        ax3.plot(WINDOWS, vals,
                 color=LCGA_COLORS[cls], marker=LCGA_MARKERS[cls],
                 linestyle=LCGA_LINESTYLES[cls],
                 markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
                 label=LCGA_LABELS[cls])

# Calibration reference line
ax3.axhline(y=0, color='black', linestyle='--', linewidth=1.0,
            alpha=REFERENCE_LINE_ALPHA)
ax3.text(10.3, 0.012, "Perfect Calibration", fontsize=ANNOTATION_SIZE,
         va='bottom', ha='right', style='italic', color='black', alpha=0.7)

ax3.set_xlabel("Temporal Window")
ax3.set_ylabel("Calibration Gap ($R_b - P_{adaptive}$)")
ax3.set_xlim(0.5, 10.5)
ax3.set_ylim(-0.80, 0.05)
ax3.set_xticks(WINDOWS)
add_y_gridlines(ax3)

ax3.legend(loc='upper right', frameon=True, edgecolor='lightgray',
           fancybox=False, fontsize=LEGEND_FONT_SIZE)

fig3.tight_layout()
save_figure(fig3, "Figure_3_LCGA_Gap_Trajectories.png")

print("\nAll 3 figures generated successfully.")
