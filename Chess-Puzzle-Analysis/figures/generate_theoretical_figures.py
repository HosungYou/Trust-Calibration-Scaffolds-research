#!/usr/bin/env python3
"""
Generate 3 publication-quality theoretical framework figures for Paper 5
(Chess Trust Calibration study).

Figure A: Trust-Reliability Matrix (2D T x R with trajectories)
Figure B: 3D Trust Trajectory (T x R x tau)
Figure C: Theoretical Predictions (5-pattern subplots)

Style: matplotlib, serif fonts, 300 DPI, minimal/clean, colorblind-friendly.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, Ellipse
from mpl_toolkits.mplot3d import proj3d

# ── Global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'DejaVu Serif', 'Times New Roman'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.5,
    'patch.linewidth': 0.5,
})

# ── Paths ────────────────────────────────────────────────────────────────────
DATA_DIR = '/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis/analysis/outputs'
FIG_DIR = '/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis/figures'

# ── GMM class mapping ────────────────────────────────────────────────────────
# Wong colorblind-friendly palette
CLASS_INFO = {
    5: {'label': 'Catastrophic',           'color': '#882255', 'marker': 'v', 'n': 30, 'cond': 'C1'},
    1: {'label': 'Convergent (Rapid)',     'color': '#117733', 'marker': 'o', 'n': 20, 'cond': 'C1'},
    3: {'label': 'Convergent (Gradual)',   'color': '#44AA99', 'marker': 's', 'n': 25, 'cond': 'C2'},
    2: {'label': 'Oscillating',            'color': '#EE7733', 'marker': 'D', 'n': 14, 'cond': 'C2'},
    4: {'label': 'ABE',                    'color': '#0077BB', 'marker': '^', 'n': 9,  'cond': 'C2'},
    6: {'label': 'Extreme Compliance',     'color': '#999999', 'marker': 'X', 'n': 2,  'cond': 'C2'},
}

PLOT_ORDER = [5, 1, 3, 2, 4, 6]

# ── Load data ────────────────────────────────────────────────────────────────
print("Loading data...")
wl = pd.read_csv(os.path.join(DATA_DIR, 'chess_window_level.csv'))
gmm = pd.read_csv(os.path.join(DATA_DIR, 'chess_gmm_s2_assignments.csv'))

merged = wl.merge(gmm[['session_id', 's2_class']], on='session_id', how='inner')

class_means = merged.groupby(['s2_class', 'window']).agg(
    mean_Rb=('R_b', 'mean'),
    mean_AI=('AI_accuracy', 'mean'),
    mean_gap=('cal_gap', 'mean'),
    se_Rb=('R_b', 'sem'),
    se_AI=('AI_accuracy', 'sem'),
    se_gap=('cal_gap', 'sem'),
).reset_index()

windows = np.arange(1, 7)

print(f"  Data loaded: {len(merged)} rows, {merged['session_id'].nunique()} sessions")
for cls in PLOT_ORDER:
    n = merged[merged['s2_class'] == cls]['session_id'].nunique()
    print(f"  Class {cls} ({CLASS_INFO[cls]['label']}): n={n}")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE A – Trust-Reliability Matrix (2D T x R)
# ═════════════════════════════════════════════════════════════════════════════
def figure_A():
    print("\nGenerating Figure A: Trust-Reliability Matrix...")

    fig, ax = plt.subplots(figsize=(7.5, 7.0))

    # --- Background layer: Theoretical framework ---
    x_diag = np.linspace(0, 1, 200)

    # Calibration zone (narrow green band along diagonal, +/- 0.1)
    ax.fill_between(x_diag, x_diag - 0.1, x_diag + 0.1,
                    color='#AADDAA', alpha=0.20, zorder=0)

    # Over-reliance region (above T=R+0.1)
    ax.fill_between(x_diag, np.clip(x_diag + 0.1, 0, 1), 1.0,
                    color='#FFCCCC', alpha=0.20, zorder=0)

    # Under-reliance region (below T=R-0.1)
    ax.fill_between(x_diag, 0.0, np.clip(x_diag - 0.1, 0, 1),
                    color='#CCE0FF', alpha=0.20, zorder=0)

    # Diagonal line T=R
    ax.plot([0, 1], [0, 1], '--', color='#555555', linewidth=1.2, zorder=2)
    ax.text(0.85, 0.91, '$T = R$', fontsize=10, color='#555555',
            rotation=42, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85))

    # Region labels
    ax.text(0.15, 0.85, 'Over-reliance\n($T > R$)', fontsize=9,
            ha='center', va='center', color='#CC4444', fontstyle='italic', alpha=0.65)
    ax.text(0.85, 0.15, 'Under-reliance\n($T < R$)', fontsize=9,
            ha='center', va='center', color='#4466AA', fontstyle='italic', alpha=0.65)
    ax.text(0.07, 0.02, 'Calibrated\nAvoidance', fontsize=7.5,
            ha='center', va='bottom', color='#448844', fontstyle='italic', alpha=0.55)
    ax.text(0.93, 0.98, 'Calibrated\nUse', fontsize=7.5,
            ha='center', va='top', color='#448844', fontstyle='italic', alpha=0.55)

    # --- Data layer: GMM class trajectories ---
    # Hand-tuned W1/W6 label offsets based on actual data positions:
    # Cls5 W1:(0.80,0.60) W6:(0.20,0.62)  -- C1 High->Low
    # Cls1 W1:(0.80,0.63) W6:(0.20,0.34)  -- C1 High->Low
    # Cls3 W1:(0.20,0.28) W6:(0.80,0.73)  -- C2 Low->High
    # Cls2 W1:(0.20,0.53) W6:(0.80,0.43)  -- C2 Low->High
    # Cls4 W1:(0.20,0.13) W6:(0.80,0.20)  -- C2 Low->High
    # Cls6 W1:(0.20,0.90) W6:(0.80,1.00)  -- C2 Low->High

    w1_offsets = {
        5: (-0.06, 0.015),    # Catastrophic: left of W1 at (0.80, 0.60)
        1: (0.025, 0.025),    # Conv Rapid: right-up of W1 at (0.80, 0.63)
        3: (-0.06, -0.015),   # Conv Gradual: left of W1 at (0.20, 0.28)
        2: (-0.06, 0.015),    # Oscillating: left of W1 at (0.20, 0.53)
        4: (-0.06, -0.015),   # ABE: left of W1 at (0.20, 0.13)
        6: (-0.06, 0.015),    # Extreme: left of W1 at (0.20, 0.90)
    }
    w6_offsets = {
        5: (0.025, 0.02),     # Catastrophic: right of W6 at (0.20, 0.62)
        1: (0.025, -0.025),   # Conv Rapid: right-down of W6 at (0.20, 0.34)
        3: (0.025, 0.02),     # Conv Gradual: right of W6 at (0.80, 0.73)
        2: (0.025, -0.025),   # Oscillating: right-down of W6 at (0.80, 0.43)
        4: (0.025, 0.02),     # ABE: right of W6 at (0.80, 0.20)
        6: (0.025, -0.025),   # Extreme: right-down of W6 at (0.80, 1.00)
    }

    for cls in PLOT_ORDER:
        info = CLASS_INFO[cls]
        cm = class_means[class_means['s2_class'] == cls].sort_values('window')

        r_vals = cm['mean_AI'].values
        t_vals = cm['mean_Rb'].values

        # Trajectory line
        ax.plot(r_vals, t_vals, '-', color=info['color'], linewidth=2.0, zorder=4)

        # Markers
        ax.plot(r_vals, t_vals, info['marker'], color=info['color'],
                markersize=7, markeredgecolor='white', markeredgewidth=0.6, zorder=5,
                label=f"{info['label']} ($n$={info['n']})")

        # Direction arrows (at midpoint of each segment)
        for i in range(len(r_vals) - 1):
            dx = r_vals[i+1] - r_vals[i]
            dy = t_vals[i+1] - t_vals[i]
            mx = (r_vals[i] + r_vals[i+1]) / 2
            my = (t_vals[i] + t_vals[i+1]) / 2
            length = np.sqrt(dx**2 + dy**2)
            if length > 0.01:
                ax.annotate('', xy=(mx + dx*0.015, my + dy*0.015),
                            xytext=(mx - dx*0.015, my - dy*0.015),
                            arrowprops=dict(arrowstyle='->', color=info['color'],
                                            lw=1.0, mutation_scale=9),
                            zorder=6)

        # W1 label
        ox, oy = w1_offsets[cls]
        ax.annotate('W1', xy=(r_vals[0], t_vals[0]),
                    xytext=(r_vals[0] + ox, t_vals[0] + oy),
                    fontsize=6.5, color=info['color'], fontweight='bold', zorder=7,
                    path_effects=[pe.withStroke(linewidth=2, foreground='white')])

        # W6 label
        ox6, oy6 = w6_offsets[cls]
        ax.annotate('W6', xy=(r_vals[-1], t_vals[-1]),
                    xytext=(r_vals[-1] + ox6, t_vals[-1] + oy6),
                    fontsize=6.5, color=info['color'], fontweight='bold', zorder=7,
                    path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    ax.set_xlabel('AI Reliability ($R$)', fontsize=11)
    ax.set_ylabel('Behavioral Reliance ($T = R_b$)', fontsize=11)
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.03)
    ax.set_xticks(np.arange(0, 1.1, 0.2))
    ax.set_yticks(np.arange(0, 1.1, 0.2))
    ax.set_aspect('equal')

    # Legend
    leg = ax.legend(loc='upper left', frameon=True, framealpha=0.95,
                    edgecolor='#cccccc', fontsize=8.5, handlelength=2.5,
                    borderpad=0.6, labelspacing=0.5)
    leg.set_zorder(10)

    fig.tight_layout()
    outpath = os.path.join(FIG_DIR, 'Figure_2_Trust_Reliability_Matrix.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE B – 3D Trust Trajectory (T x R x tau)
# ═════════════════════════════════════════════════════════════════════════════
class Arrow3D(FancyArrowPatch):
    """3D arrow for matplotlib 3D axes."""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return min(zs)


def figure_B():
    print("\nGenerating Figure B: 3D Trust Trajectory...")

    fig = plt.figure(figsize=(9.5, 7.5))
    ax = fig.add_subplot(111, projection='3d')

    # --- Calibration plane T = R (semi-transparent gray) ---
    r_plane = np.linspace(0, 1, 20)
    tau_plane = np.linspace(1, 6, 20)
    R_grid, Tau_grid = np.meshgrid(r_plane, tau_plane)
    T_grid = R_grid  # T = R surface

    ax.plot_surface(Tau_grid, R_grid, T_grid, alpha=0.10, color='#999999',
                    edgecolor='none', zorder=0)

    # Label the calibration plane
    ax.text(1.5, 0.80, 0.88, '$T = R$ Plane',
            fontsize=8.5, color='#777777', fontstyle='italic', ha='center')

    # --- Reliability switch plane at tau = 4.5 ---
    r_switch = np.linspace(0, 1, 10)
    t_switch = np.linspace(0, 1, 10)
    R_sw, T_sw = np.meshgrid(r_switch, t_switch)
    Tau_sw = np.full_like(R_sw, 4.5)
    ax.plot_surface(Tau_sw, R_sw, T_sw, alpha=0.05, color='#444444',
                    edgecolor='none', zorder=0)

    # Highlight edges of the switch plane
    ax.plot([4.5, 4.5], [0, 0], [0, 1], '--', color='#666666', linewidth=0.6, alpha=0.4)
    ax.plot([4.5, 4.5], [1, 1], [0, 1], '--', color='#666666', linewidth=0.6, alpha=0.4)
    ax.plot([4.5, 4.5], [0, 1], [0, 0], '--', color='#666666', linewidth=0.6, alpha=0.4)
    ax.plot([4.5, 4.5], [0, 1], [1, 1], '--', color='#666666', linewidth=0.6, alpha=0.4)

    # Switch label (positioned carefully to avoid axis overlap)
    ax.text(4.5, 1.08, 0.0, 'Reliability\nSwitch ($\\tau$=4.5)', fontsize=8,
            color='#555555', ha='center', va='bottom')

    # --- Plot GMM class trajectories ---
    for cls in PLOT_ORDER:
        info = CLASS_INFO[cls]
        cm = class_means[class_means['s2_class'] == cls].sort_values('window')

        tau_vals = cm['window'].values.astype(float)
        r_vals = cm['mean_AI'].values
        t_vals = cm['mean_Rb'].values

        # Trajectory line
        ax.plot(tau_vals, r_vals, t_vals, '-', color=info['color'],
                linewidth=2.5, zorder=5,
                label=f"{info['label']} ($n$={info['n']})")

        # Markers
        ax.scatter(tau_vals, r_vals, t_vals, color=info['color'],
                   marker=info['marker'], s=45, edgecolors='white',
                   linewidths=0.5, zorder=6, depthshade=False)

        # Arrow at end of trajectory
        if len(tau_vals) >= 2:
            arrow = Arrow3D(
                [tau_vals[-2], tau_vals[-1]],
                [r_vals[-2], r_vals[-1]],
                [t_vals[-2], t_vals[-1]],
                mutation_scale=12, lw=1.5, arrowstyle='->', color=info['color']
            )
            ax.add_artist(arrow)

    # --- Axes configuration ---
    ax.set_xlabel('Time ($\\tau$, Windows)', fontsize=10, labelpad=10)
    ax.set_ylabel('AI Reliability ($R$)', fontsize=10, labelpad=10)
    ax.set_zlabel('Behavioral Reliance ($T$)', fontsize=10, labelpad=10)

    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_zticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

    ax.view_init(elev=22, azim=-50)

    ax.tick_params(axis='both', which='major', labelsize=7.5, pad=2)

    # Legend
    leg = ax.legend(loc='upper left', bbox_to_anchor=(-0.05, 0.95),
                    frameon=True, framealpha=0.95, edgecolor='#cccccc',
                    fontsize=8, handlelength=2.5, ncol=1, borderpad=0.5)

    # Make panes lighter
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#dddddd')
    ax.yaxis.pane.set_edgecolor('#dddddd')
    ax.zaxis.pane.set_edgecolor('#dddddd')

    # Subtle grid
    ax.xaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)
    ax.yaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)
    ax.zaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)

    fig.tight_layout(pad=1.5)
    outpath = os.path.join(FIG_DIR, 'Figure_3_3D_Trust_Trajectory.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE C – Theoretical Predictions (5-pattern + summary)
# ═════════════════════════════════════════════════════════════════════════════
def figure_C():
    print("\nGenerating Figure C: Theoretical Predictions...")

    fig, axes = plt.subplots(2, 3, figsize=(10.5, 7.0))
    fig.subplots_adjust(hspace=0.55, wspace=0.38, top=0.93, bottom=0.08)

    windows_th = np.linspace(1, 6, 200)
    switch_idx = 4.5

    def get_phase(x):
        return x <= switch_idx, x > switch_idx

    def format_subplot(ax, title, subtitle, annotation, color):
        ax.axhline(y=0, color='#888888', linestyle='-', linewidth=0.6, zorder=1)
        ax.axvline(x=switch_idx, color='#444444', linestyle='--', linewidth=0.9, zorder=2)
        ax.set_xlim(0.5, 6.5)
        ax.set_ylim(-0.55, 0.55)
        ax.set_xticks([1, 2, 3, 4, 5, 6])
        ax.set_yticks([-0.4, -0.2, 0, 0.2, 0.4])
        ax.set_xlabel('Window', fontsize=8.5)
        ax.set_ylabel('Cal. Gap ($T - R$)', fontsize=8.5)
        ax.tick_params(labelsize=7.5)

        # Title and subtitle as a single two-line title
        ax.set_title(f'{title}\n', fontsize=10, fontweight='bold', color=color, pad=12)
        ax.text(0.5, 1.01, subtitle, transform=ax.transAxes,
                fontsize=7, ha='center', va='bottom', fontstyle='italic',
                color='#777777')

        # Annotation box (top-right inside plot)
        ax.text(0.97, 0.95, annotation, transform=ax.transAxes,
                fontsize=7, ha='right', va='top',
                bbox=dict(boxstyle='round,pad=0.25', fc='#f8f8f8',
                          ec='#cccccc', lw=0.5))

        # Phase labels at bottom
        ax.text(2.5, -0.52, 'Pre-switch', fontsize=6.5, ha='center',
                color='#aaaaaa', fontstyle='italic')
        ax.text(5.5, -0.52, 'Post', fontsize=6.5, ha='center',
                color='#aaaaaa', fontstyle='italic')

    # ── 1. Convergent ──
    ax1 = axes[0, 0]
    pre, post = get_phase(windows_th)
    gap_conv = np.zeros_like(windows_th)
    gap_conv[pre] = 0.25 * np.exp(-0.6 * (windows_th[pre] - 1))
    gap_conv[post] = -0.28 * np.exp(-1.8 * (windows_th[post] - switch_idx)) + 0.015
    ax1.fill_between(windows_th, 0, gap_conv, where=(gap_conv > 0),
                     color='#117733', alpha=0.15, zorder=1)
    ax1.fill_between(windows_th, 0, gap_conv, where=(gap_conv < 0),
                     color='#117733', alpha=0.15, zorder=1)
    ax1.plot(windows_th, gap_conv, '-', color='#117733', linewidth=2.2, zorder=3)
    format_subplot(ax1, 'Convergent', 'Both learning rates active',
                   '$\\alpha^+, \\alpha^- > \\alpha_{min}$', '#117733')

    # ── 2. Oscillating ──
    ax2 = axes[0, 1]
    gap_osc = np.zeros_like(windows_th)
    gap_osc[pre] = 0.18 * np.sin(2.5 * np.pi * (windows_th[pre] - 1) / 4) * \
                   np.exp(-0.2 * (windows_th[pre] - 1))
    gap_osc[post] = -0.25 * np.sin(2.0 * np.pi * (windows_th[post] - switch_idx) / 2.5) * \
                    np.exp(-0.5 * (windows_th[post] - switch_idx))
    ax2.fill_between(windows_th, 0, gap_osc, where=(gap_osc > 0),
                     color='#EE7733', alpha=0.12, zorder=1)
    ax2.fill_between(windows_th, 0, gap_osc, where=(gap_osc < 0),
                     color='#EE7733', alpha=0.12, zorder=1)
    ax2.plot(windows_th, gap_osc, '-', color='#EE7733', linewidth=2.2, zorder=3)
    format_subplot(ax2, 'Oscillating', 'Threshold-dependent updating',
                   'Nonlinear $\\alpha$', '#EE7733')

    # ── 3. Stagnant ──
    ax3 = axes[0, 2]
    gap_stag = 0.15 + 0.015 * np.sin(0.8 * np.pi * windows_th)
    bump = 0.025 * np.exp(-2.0 * (windows_th - switch_idx)**2)
    gap_stag = gap_stag + bump
    ax3.fill_between(windows_th, 0, gap_stag,
                     color='#CC3311', alpha=0.12, zorder=1)
    ax3.plot(windows_th, gap_stag, '-', color='#CC3311', linewidth=2.2, zorder=3)
    format_subplot(ax3, 'Stagnant', 'Learning rates near zero',
                   '$\\alpha^+ \\approx \\alpha^- \\approx 0$', '#CC3311')

    # ── 4. Catastrophic ──
    ax4 = axes[1, 0]
    gap_cat = np.zeros_like(windows_th)
    gap_cat[pre] = -0.04 + 0.015 * np.sin(0.5 * np.pi * windows_th[pre])
    transition = np.clip((windows_th[post] - switch_idx) / 0.25, 0, 1)
    gap_cat[post] = 0.35 * transition + 0.015 * np.sin(0.5 * np.pi * windows_th[post])
    ax4.fill_between(windows_th[post], 0, gap_cat[post],
                     color='#882255', alpha=0.18, zorder=1)
    ax4.plot(windows_th, gap_cat, '-', color='#882255', linewidth=2.2, zorder=3)
    ax4.annotate('Persistent\ngap', xy=(5.6, 0.28), xytext=(3.5, 0.42),
                 fontsize=6.5, ha='center', color='#882255',
                 arrowprops=dict(arrowstyle='->', color='#882255', lw=0.8))
    format_subplot(ax4, 'Catastrophic', 'Downward learning failure',
                   '$\\alpha^- \\approx 0 \\mid R\\!\\downarrow$', '#882255')

    # ── 5. ABE ──
    ax5 = axes[1, 1]
    gap_abe = np.zeros_like(windows_th)
    gap_abe[pre] = 0.04 - 0.015 * np.sin(0.5 * np.pi * windows_th[pre])
    transition_abe = np.clip((windows_th[post] - switch_idx) / 0.25, 0, 1)
    gap_abe[post] = -0.35 * transition_abe - 0.015 * (windows_th[post] - switch_idx) * 0.08
    ax5.fill_between(windows_th[post], 0, gap_abe[post],
                     color='#0077BB', alpha=0.18, zorder=1)
    ax5.plot(windows_th, gap_abe, '-', color='#0077BB', linewidth=2.2, zorder=3)
    ax5.annotate('Persistent\ngap', xy=(5.6, -0.30), xytext=(3.5, -0.45),
                 fontsize=6.5, ha='center', color='#0077BB',
                 arrowprops=dict(arrowstyle='->', color='#0077BB', lw=0.8))
    format_subplot(ax5, 'ABE', 'Upward learning failure',
                   '$\\alpha^+ \\approx 0 \\mid R\\!\\uparrow$', '#0077BB')

    # ── 6. Summary: Learning Rate Space ──
    ax6 = axes[1, 2]
    # Reset spines for this panel
    ax6.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)

    ax6.set_xlim(-0.05, 1.05)
    ax6.set_ylim(-0.05, 1.05)
    ax6.set_xlabel('$\\alpha^+$ (upward learning)', fontsize=8.5)
    ax6.set_ylabel('$\\alpha^-$ (downward learning)', fontsize=8.5)
    ax6.set_title('Learning Rate Space\n', fontsize=10, fontweight='bold',
                  color='#444444', pad=12)
    ax6.text(0.5, 1.01, 'Catastrophic-ABE mirror symmetry', transform=ax6.transAxes,
             fontsize=7, ha='center', va='bottom', fontstyle='italic',
             color='#777777')

    # Diagonal: balanced learning
    ax6.plot([0, 1], [0, 1], '--', color='#aaaaaa', linewidth=0.8)
    ax6.text(0.75, 0.82, '$\\alpha^+ = \\alpha^-$', fontsize=7,
             color='#999999', rotation=42, ha='center', va='center')

    # Convergent region
    ell_conv = Ellipse((0.55, 0.55), 0.35, 0.35, angle=45,
                       fc='#117733', alpha=0.12, ec='#117733', lw=0.8)
    ax6.add_patch(ell_conv)
    ax6.text(0.57, 0.57, 'Convergent', fontsize=7, ha='center', va='center',
             color='#117733', fontweight='bold')

    # Oscillating region
    ell_osc = Ellipse((0.35, 0.35), 0.18, 0.18, angle=45,
                      fc='#EE7733', alpha=0.12, ec='#EE7733', lw=0.8, ls='--')
    ax6.add_patch(ell_osc)
    ax6.text(0.28, 0.24, 'Osc.', fontsize=6.5, ha='center', va='center',
             color='#EE7733', fontweight='bold')

    # Stagnant region
    ell_stag = Ellipse((0.07, 0.07), 0.14, 0.14, angle=0,
                       fc='#CC3311', alpha=0.12, ec='#CC3311', lw=0.8)
    ax6.add_patch(ell_stag)
    ax6.text(0.07, 0.07, 'Stag.', fontsize=6.5, ha='center', va='center',
             color='#CC3311', fontweight='bold')

    # Catastrophic marker: high alpha+, low alpha-
    ax6.scatter([0.65], [0.04], marker='v', s=100, color='#882255',
                edgecolors='white', linewidths=0.5, zorder=5)
    ax6.text(0.67, 0.12, 'Catastrophic\n$\\alpha^- \\approx 0$', fontsize=7,
             ha='left', va='bottom', color='#882255', fontweight='bold')

    # ABE marker: low alpha+, high alpha-
    ax6.scatter([0.04], [0.65], marker='^', s=100, color='#0077BB',
                edgecolors='white', linewidths=0.5, zorder=5)
    ax6.text(0.12, 0.63, 'ABE\n$\\alpha^+ \\approx 0$', fontsize=7,
             ha='left', va='center', color='#0077BB', fontweight='bold')

    # Mirror symmetry arrow
    ax6.annotate('', xy=(0.07, 0.58), xytext=(0.58, 0.07),
                 arrowprops=dict(arrowstyle='<->', color='#888888',
                                 lw=0.9, ls='--', connectionstyle='arc3,rad=0.25'))
    ax6.text(0.40, 0.38, 'Mirror', fontsize=6.5, ha='center', va='center',
             color='#888888', rotation=-42,
             bbox=dict(boxstyle='round,pad=0.12', fc='white', ec='none', alpha=0.85))

    ax6.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax6.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax6.tick_params(labelsize=7.5)
    ax6.set_aspect('equal')

    outpath = os.path.join(FIG_DIR, 'Figure_4_Theoretical_Predictions.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    os.makedirs(FIG_DIR, exist_ok=True)
    figure_A()
    figure_B()
    figure_C()
    print("\nAll 3 theoretical framework figures generated successfully.")
