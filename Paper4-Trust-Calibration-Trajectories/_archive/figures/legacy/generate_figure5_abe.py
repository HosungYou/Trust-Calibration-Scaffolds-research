#!/usr/bin/env python3
"""
Generate Figure 5: AI Benefit Emergence (ABE) — The "Scissors" Graph.

Shows the diverging trajectories of P_adaptive (rising) and R_b (flat)
for LCGA Class 4, with the widening gap shaded. Inset shows the
MBC Phase 2B ABE class for cross-method comparison.

Target journal: Computers in Human Behavior (CHB)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.interpolate import make_interp_spline
from pathlib import Path
import sys

# ── Shared figure style ──────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_style import *

apply_style()

OUT = FIG_DIR / "Figure_5_ABE_Discovery.png"

# ── LCGA Class 4 data (N=177, 5.5%) ─────────────────────────────────────────
# Known data points at W01, W05, W10
lcga_windows_known = np.array([1, 5, 10])
lcga_Rb_known = np.array([0.090, 0.186, 0.147])
lcga_Pa_known = np.array([0.473, 0.589, 0.722])

# Interpolate to get smooth curves for all 10 windows
# Use LCGA gap trajectory for intermediate points as guide
# From discussion file: gap = [-0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543]
lcga_gap_all = np.array([-0.301, -0.320, -0.332, -0.336, -0.374, -0.429, -0.427, -0.493, -0.535, -0.543])
windows_all = np.arange(1, 11)

# We know R_b at W1, W5, W10. Interpolate R_b smoothly.
# R_b rises then slightly falls: use cubic spline
spl_rb = make_interp_spline(lcga_windows_known, lcga_Rb_known, k=2)
lcga_Rb_all = spl_rb(windows_all)
# Derive P_adaptive from gap: gap = R_b - P_adaptive => P_adaptive = R_b - gap
lcga_Pa_all = lcga_Rb_all - lcga_gap_all

# For smooth plotting: fine-grained x
x_fine = np.linspace(1, 10, 200)
spl_rb_fine = make_interp_spline(windows_all, lcga_Rb_all, k=3)
spl_pa_fine = make_interp_spline(windows_all, lcga_Pa_all, k=3)
rb_fine = spl_rb_fine(x_fine)
pa_fine = spl_pa_fine(x_fine)

# ── MBC Phase 2B Class 4 data (N=256, 5.7%) ─────────────────────────────────
mbc_windows_known = np.array([1, 5, 10])
mbc_Rb_known = np.array([0.020, 0.108, 0.171])
mbc_Pa_known = np.array([0.275, 0.643, 0.852])
mbc_gap_known = np.array([-0.039, -0.378, -0.601])

# Interpolate MBC data
# Smooth R_b
mbc_Rb_interp = np.interp(windows_all, mbc_windows_known, mbc_Rb_known)
mbc_Pa_interp = np.interp(windows_all, mbc_windows_known, mbc_Pa_known)


def main():
    fig = plt.figure(figsize=(7, 5.5))

    # Main axes — no embedded titles, so give full vertical space
    ax = fig.add_axes([0.12, 0.10, 0.80, 0.85])

    # ── Shaded gap area ──────────────────────────────────────────────────────
    ax.fill_between(x_fine, rb_fine, pa_fine,
                    color=ABE_COLOR_GAP, alpha=0.35, zorder=1,
                    label='_nolegend_')

    # ── P_adaptive line (blue, rising) — solid + circle markers ──────────────
    ax.plot(x_fine, pa_fine, color=ABE_COLOR_P, linewidth=2.8,
            linestyle='-', zorder=3,
            label='$P_{adaptive}$ (AI effectiveness)')
    ax.scatter(windows_all, lcga_Pa_all, color=ABE_COLOR_P, s=45,
               marker='o', edgecolors='white', linewidths=0.8, zorder=4)

    # ── R_b line (red, flat) — dashed + square markers ───────────────────────
    ax.plot(x_fine, rb_fine, color=ABE_COLOR_R, linewidth=2.8,
            linestyle='--', zorder=3,
            label='$R_b$ (learner reliance)')
    ax.scatter(windows_all, lcga_Rb_all, color=ABE_COLOR_R, s=45,
               marker='s', edgecolors='white', linewidths=0.8, zorder=4)

    # ── Annotations ──────────────────────────────────────────────────────────
    # "AI becomes more effective" near P_adaptive — positioned left to avoid inset
    ax.annotate(
        'AI becomes more\neffective over time',
        xy=(3.5, spl_pa_fine(3.5)),
        xytext=(1.5, 0.62),
        fontsize=ANNOTATION_SIZE, fontweight='bold', color=ABE_COLOR_P,
        ha='center',
        arrowprops=dict(arrowstyle='->', color=ABE_COLOR_P, lw=1.5,
                        connectionstyle='arc3,rad=-0.2'),
        zorder=5,
    )

    # "Learner reliance stays flat" near R_b
    ax.annotate(
        'Learner reliance\nstays flat',
        xy=(5, spl_rb_fine(5)),
        xytext=(3.0, 0.03),
        fontsize=ANNOTATION_SIZE, fontweight='bold', color=ABE_COLOR_R,
        ha='center',
        arrowprops=dict(arrowstyle='->', color=ABE_COLOR_R, lw=1.5,
                        connectionstyle='arc3,rad=0.2'),
        zorder=5,
    )

    # "Growing missed opportunity" in the gap — moved left to avoid inset
    mid_y = (spl_pa_fine(5) + spl_rb_fine(5)) / 2
    ax.text(5.0, mid_y, 'Growing\nmissed\nopportunity',
            fontsize=ANNOTATION_SIZE, fontstyle='italic', color=ABE_COLOR_TEXT,
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#EF9A9A', alpha=0.9, linewidth=1),
            zorder=5)

    # Draw double-headed arrow showing gap width at W10
    y_top_w10 = spl_pa_fine(10)
    y_bot_w10 = spl_rb_fine(10)
    ax.annotate('', xy=(10.3, y_top_w10), xytext=(10.3, y_bot_w10),
                arrowprops=dict(arrowstyle='<->', color=ABE_COLOR_TEXT, lw=1.5))
    ax.text(10.55, (y_top_w10 + y_bot_w10) / 2, f'Gap\n= {abs(lcga_gap_all[-1]):.2f}',
            fontsize=8.5, color=ABE_COLOR_TEXT, ha='left', va='center',
            fontweight='bold')

    # Draw smaller gap arrow at W1 for comparison
    y_top_w1 = spl_pa_fine(1)
    y_bot_w1 = spl_rb_fine(1)
    ax.annotate('', xy=(0.7, y_top_w1), xytext=(0.7, y_bot_w1),
                arrowprops=dict(arrowstyle='<->', color=ABE_COLOR_TEXT, lw=1.2, alpha=0.6))
    ax.text(0.45, (y_top_w1 + y_bot_w1) / 2, f'Gap\n= {abs(lcga_gap_all[0]):.2f}',
            fontsize=7.5, color=ABE_COLOR_TEXT, ha='right', va='center', alpha=0.7)

    # ── Axis formatting ─────────────────────────────────────────────────────
    ax.set_xlabel('Temporal Window ($\\tau$)')
    ax.set_ylabel('Proportion')
    ax.set_xlim(0.3, 11.2)
    ax.set_ylim(-0.02, 0.88)
    ax.set_xticks(windows_all)
    ax.set_xticklabels([f'{w}' for w in windows_all])
    add_y_gridlines(ax)

    # Legend
    ax.legend(loc='upper left', frameon=True, edgecolor='lightgray',
              fancybox=False)

    # ── Inset: MBC Phase 2B comparison ───────────────────────────────────────
    ax_inset = fig.add_axes([0.58, 0.58, 0.28, 0.28])

    # Smooth MBC data
    x_mbc_fine = np.linspace(1, 10, 100)
    spl_mbc_pa = make_interp_spline(windows_all, mbc_Pa_interp, k=3)
    spl_mbc_rb = make_interp_spline(windows_all, mbc_Rb_interp, k=3)

    ax_inset.fill_between(x_mbc_fine, spl_mbc_rb(x_mbc_fine),
                          spl_mbc_pa(x_mbc_fine),
                          color=ABE_COLOR_GAP, alpha=0.3)
    ax_inset.plot(x_mbc_fine, spl_mbc_pa(x_mbc_fine),
                  color=ABE_COLOR_P, linewidth=2.0,
                  linestyle='-', label='$P_{adaptive}$')
    ax_inset.plot(x_mbc_fine, spl_mbc_rb(x_mbc_fine),
                  color=ABE_COLOR_R, linewidth=2.0,
                  linestyle='--', label='$R_b$')
    ax_inset.scatter(mbc_windows_known, mbc_Pa_known, color=ABE_COLOR_P,
                     s=30, marker='o', edgecolors='white', linewidths=0.5, zorder=4)
    ax_inset.scatter(mbc_windows_known, mbc_Rb_known, color=ABE_COLOR_R,
                     s=30, marker='s', edgecolors='white', linewidths=0.5, zorder=4)

    ax_inset.set_title('MBC Phase 2B (N=256)', fontsize=9, fontweight='bold',
                        pad=4)
    ax_inset.set_xlabel('Window', fontsize=8)
    ax_inset.set_ylabel('Proportion', fontsize=8)
    ax_inset.set_xlim(0.5, 10.5)
    ax_inset.set_ylim(-0.02, 0.92)
    ax_inset.set_xticks([1, 5, 10])
    ax_inset.tick_params(labelsize=8)
    add_y_gridlines(ax_inset)
    ax_inset.legend(fontsize=7, loc='center left', frameon=True,
                    edgecolor='lightgray')

    # Inset border
    for spine in ax_inset.spines.values():
        spine.set_edgecolor('#999999')
        spine.set_linewidth(0.8)

    # ── Save ──────────────────────────────────────────────────────────────────
    save_figure(fig, "Figure_5_ABE_Discovery.png")


if __name__ == '__main__':
    main()
