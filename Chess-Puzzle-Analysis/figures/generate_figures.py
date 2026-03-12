#!/usr/bin/env python3
"""
Generate 5 publication-quality figures for:
Trust Calibration Trajectories in Human-AI Interaction (Chess Puzzle Experiment)

Targets: Human Factors journal, APA-compatible style, 300 DPI, serif fonts.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

# ── Global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'DejaVu Serif', 'Times New Roman'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
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

# ── Colorblind-friendly palette ──────────────────────────────────────────────
C1_COLOR = '#D55E00'   # vermillion (High-to-Low)
C2_COLOR = '#0072B2'   # blue (Low-to-High)
OVER_COLOR = '#D55E00'  # over-reliance shading (warm)
UNDER_COLOR = '#0072B2' # under-reliance shading (cool)

# GMM class colors (Wong palette extended)
GMM_COLORS = {
    5: '#D55E00',  # Catastrophic – vermillion
    1: '#E69F00',  # Convergent (Rapid) – amber
    6: '#CC79A7',  # Extreme Compliance – reddish purple
    3: '#0072B2',  # Convergent (Gradual) – blue
    2: '#009E73',  # Oscillating – bluish green
    4: '#56B4E9',  # ABE – sky blue
}

# ── Load data ────────────────────────────────────────────────────────────────
wl = pd.read_csv(os.path.join(DATA_DIR, 'chess_window_level.csv'))
gmm = pd.read_csv(os.path.join(DATA_DIR, 'chess_gmm_s2_assignments.csv'))
lcga = pd.read_csv(os.path.join(DATA_DIR, 'chess_lcga_gap_assignments.csv'))


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 1 – Experimental Design (AI Accuracy by Condition)
# ═════════════════════════════════════════════════════════════════════════════
def figure_1():
    print("Generating Figure 1: Experimental Design...")
    means = wl.groupby(['condition', 'window'])['AI_accuracy'].mean().unstack(level=0)
    windows = np.arange(1, 7)

    fig, ax = plt.subplots(figsize=(5.5, 3.5))

    # Shaded phases
    ax.axvspan(0.5, 4.5, color='#f0f0f0', zorder=0, label='_nolegend_')
    ax.axvspan(4.5, 6.5, color='#e0e0e0', zorder=0, label='_nolegend_')

    # Phase labels
    ax.text(2.5, 0.03, 'Pre-Switch Phase', ha='center', va='bottom',
            fontsize=8, fontstyle='italic', color='#555555')
    ax.text(5.5, 0.03, 'Post-Switch\nPhase', ha='center', va='bottom',
            fontsize=8, fontstyle='italic', color='#555555')

    # Reliability switch line
    ax.axvline(x=4.5, color='#333333', linestyle='--', linewidth=1.0, zorder=3)
    ax.annotate('Reliability\nSwitch', xy=(4.5, 0.95), fontsize=8,
                ha='center', va='top', color='#333333',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#999999', lw=0.5))

    # Plot lines
    ax.plot(windows, means[1].values, 'o-', color=C1_COLOR, markersize=6,
            label='C1: High $\\rightarrow$ Low', zorder=5)
    ax.plot(windows, means[2].values, 's-', color=C2_COLOR, markersize=6,
            label='C2: Low $\\rightarrow$ High', zorder=5)

    ax.set_xlabel('Window')
    ax.set_ylabel('AI Accuracy')
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks(windows)
    ax.legend(frameon=True, framealpha=0.9, edgecolor='#cccccc', loc='center right')

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'Figure_1_Experimental_Design.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> Saved Figure_1_Experimental_Design.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 2 – LCGA Calibration Gap Trajectories (G=2)
# ═════════════════════════════════════════════════════════════════════════════
def figure_2():
    print("Generating Figure 2: LCGA Trajectories...")
    lcga_merged = wl.merge(lcga[['session_id', 'class']], on='session_id', how='inner')
    lcga_merged['cal_gap_rb_p'] = lcga_merged['R_b'] - lcga_merged['P']

    windows = np.arange(1, 7)
    class_info = {
        1: {'color': C1_COLOR, 'label': 'Class 1: High$\\rightarrow$Low Dominant'},
        2: {'color': C2_COLOR, 'label': 'Class 2: Low$\\rightarrow$High Dominant'},
    }

    # Compute n per class
    n_per_class = lcga_merged.groupby('class')['session_id'].nunique()

    fig, ax = plt.subplots(figsize=(5.5, 4.0))

    # Reference lines
    ax.axhline(y=0, color='#888888', linestyle='--', linewidth=0.8, zorder=2)
    ax.axvline(x=4.5, color='#333333', linestyle='--', linewidth=1.0, zorder=2)

    for cls in [1, 2]:
        subset = lcga_merged[lcga_merged['class'] == cls]
        n = n_per_class[cls]
        info = class_info[cls]

        # Individual trajectories
        for sid, grp in subset.groupby('session_id'):
            ax.plot(grp['window'].values, grp['cal_gap_rb_p'].values,
                    color=info['color'], alpha=0.12, linewidth=0.6, zorder=1)

        # Mean trajectory
        means = subset.groupby('window')['cal_gap_rb_p'].mean()
        se = subset.groupby('window')['cal_gap_rb_p'].sem()
        ax.plot(windows, means.values, 'o-', color=info['color'],
                linewidth=2.5, markersize=5, zorder=4,
                label=f"{info['label']} ($n$ = {n})")
        ax.fill_between(windows, (means - 1.96 * se).values, (means + 1.96 * se).values,
                         color=info['color'], alpha=0.15, zorder=3)

    ax.text(4.55, ax.get_ylim()[1] * 0.9, 'Reliability\nSwitch', fontsize=8,
            ha='left', va='top', color='#333333')

    ax.set_xlabel('Window')
    ax.set_ylabel('Calibration Gap ($R_b - P$)')
    ax.set_xlim(0.5, 6.5)
    ax.set_xticks(windows)
    ax.legend(frameon=True, framealpha=0.9, edgecolor='#cccccc', loc='best')

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'Figure_2_LCGA_Trajectories.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> Saved Figure_2_LCGA_Trajectories.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 3 – GMM 6-Class Trajectory Profiles (2x3 subplots)
# ═════════════════════════════════════════════════════════════════════════════
def figure_3():
    print("Generating Figure 3: GMM Six-Class Profiles...")
    gmm_merged = wl.merge(gmm[['session_id', 's2_class']], on='session_id', how='inner')

    n_per_class = gmm_merged.groupby('s2_class')['session_id'].nunique()
    windows = np.arange(1, 7)

    # Layout: 2 rows x 3 cols
    # Row 1: Class 5 (Catastrophic), Class 1 (Convergent-Rapid), Class 6 (Extreme Compliance)
    # Row 2: Class 3 (Convergent-Gradual), Class 2 (Oscillating), Class 4 (ABE)
    subplot_order = [5, 1, 6, 3, 2, 4]
    class_labels = {
        5: 'Catastrophic',
        1: 'Convergent (Rapid)',
        6: 'Extreme Compliance',
        3: 'Convergent (Gradual)',
        2: 'Oscillating',
        4: 'ABE',
    }
    class_conditions = {5: 'C1', 1: 'C1', 6: 'C2', 3: 'C2', 2: 'C2', 4: 'C2'}

    fig, axes = plt.subplots(2, 3, figsize=(8.5, 5.0), sharex=True, sharey=True)

    for idx, cls in enumerate(subplot_order):
        row, col = divmod(idx, 3)
        ax = axes[row, col]

        subset = gmm_merged[gmm_merged['s2_class'] == cls]
        n = n_per_class.get(cls, 0)
        means = subset.groupby('window')[['R_b', 'AI_accuracy']].mean()

        rb_vals = means['R_b'].values
        ai_vals = means['AI_accuracy'].values

        # Shaded calibration gap (red = over-reliance R_b > AI, blue = under-reliance)
        for w in range(len(windows) - 1):
            x_seg = [windows[w], windows[w + 1]]
            rb_seg = [rb_vals[w], rb_vals[w + 1]]
            ai_seg = [ai_vals[w], ai_vals[w + 1]]
            # Determine dominant direction in this segment
            avg_diff = ((rb_vals[w] - ai_vals[w]) + (rb_vals[w + 1] - ai_vals[w + 1])) / 2
            color = OVER_COLOR if avg_diff > 0 else UNDER_COLOR
            ax.fill_between(x_seg, rb_seg, ai_seg, color=color, alpha=0.15, zorder=1)

        # Lines
        ax.plot(windows, rb_vals, 'o-', color='#333333', linewidth=2.0,
                markersize=4, zorder=5, label='$R_b$ (Reliance)')
        ax.plot(windows, ai_vals, 's--', color='#888888', linewidth=1.5,
                markersize=4, zorder=5, label='AI Accuracy')

        # Switch line
        ax.axvline(x=4.5, color='#aaaaaa', linestyle=':', linewidth=0.8, zorder=2)

        # Subplot title
        cond_tag = class_conditions[cls]
        ax.set_title(f"Class {cls}: {class_labels[cls]} ({cond_tag}, $n$={n})",
                      fontsize=9, fontweight='bold')

        ax.set_ylim(-0.05, 1.1)
        ax.set_xlim(0.5, 6.5)
        ax.set_xticks(windows)

        if row == 1:
            ax.set_xlabel('Window')
        if col == 0:
            ax.set_ylabel('Proportion')

    # Shared legend at bottom
    handles = [
        Line2D([0], [0], color='#333333', linewidth=2.0, marker='o', markersize=4,
               label='$R_b$ (Behavioral Reliance)'),
        Line2D([0], [0], color='#888888', linewidth=1.5, linestyle='--', marker='s',
               markersize=4, label='AI Accuracy'),
        mpatches.Patch(color=OVER_COLOR, alpha=0.25, label='Over-reliance ($R_b > P$)'),
        mpatches.Patch(color=UNDER_COLOR, alpha=0.25, label='Under-reliance ($R_b < P$)'),
    ]
    fig.legend(handles=handles, loc='lower center', ncol=4, frameon=True,
               framealpha=0.9, edgecolor='#cccccc', fontsize=8,
               bbox_to_anchor=(0.5, -0.02))

    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig(os.path.join(FIG_DIR, 'Figure_3_GMM_Six_Class_Profiles.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> Saved Figure_3_GMM_Six_Class_Profiles.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 4 – Theoretical Pattern Map (Bayesian Update Parameter Space)
# ═════════════════════════════════════════════════════════════════════════════
def figure_4():
    print("Generating Figure 4: Theoretical Pattern Map...")

    fig, ax = plt.subplots(figsize=(5.5, 5.0))

    # Regions (ellipses / patches)
    from matplotlib.patches import Ellipse

    # Convergent: upper-right
    ell_conv = Ellipse((0.70, 0.70), 0.40, 0.40, angle=0,
                        facecolor='#009E73', alpha=0.18, edgecolor='#009E73',
                        linewidth=1.2, linestyle='-', zorder=2)
    ax.add_patch(ell_conv)
    ax.annotate('Convergent\n($n$ = 45)', xy=(0.70, 0.70), fontsize=9,
                ha='center', va='center', fontweight='bold', color='#006B52',
                zorder=5)

    # Stagnant: lower-left
    ell_stag = Ellipse((0.15, 0.15), 0.25, 0.25, angle=0,
                        facecolor='#999999', alpha=0.20, edgecolor='#777777',
                        linewidth=1.2, zorder=2)
    ax.add_patch(ell_stag)
    ax.annotate('Stagnant\n($n$ = 0)', xy=(0.15, 0.15), fontsize=9,
                ha='center', va='center', fontweight='bold', color='#555555',
                zorder=5)

    # Catastrophic: bottom-right (high alpha+, low alpha-)
    ell_cat = Ellipse((0.72, 0.12), 0.45, 0.20, angle=0,
                       facecolor='#D55E00', alpha=0.18, edgecolor='#D55E00',
                       linewidth=1.2, zorder=2)
    ax.add_patch(ell_cat)
    ax.annotate('Catastrophic\n($n$ = 30)', xy=(0.72, 0.12), fontsize=9,
                ha='center', va='center', fontweight='bold', color='#A04800',
                zorder=5)

    # ABE (Automation Bias Entrenchment): left edge, upper
    ell_abe = Ellipse((0.12, 0.72), 0.20, 0.45, angle=0,
                       facecolor='#56B4E9', alpha=0.18, edgecolor='#56B4E9',
                       linewidth=1.2, zorder=2)
    ax.add_patch(ell_abe)
    ax.annotate('ABE\n($n$ = 9)', xy=(0.12, 0.72), fontsize=9,
                ha='center', va='center', fontweight='bold', color='#2E7CA8',
                zorder=5)

    # Oscillating: center (nonlinear/threshold)
    ell_osc = Ellipse((0.45, 0.45), 0.28, 0.22, angle=30,
                       facecolor='#E69F00', alpha=0.18, edgecolor='#E69F00',
                       linewidth=1.2, linestyle='--', zorder=2)
    ax.add_patch(ell_osc)
    ax.annotate('Oscillating\n($n$ = 14)', xy=(0.45, 0.45), fontsize=9,
                ha='center', va='center', fontweight='bold', color='#B37C00',
                zorder=5)

    # Diagonal: symmetric updating
    ax.plot([0, 1], [0, 1], color='#aaaaaa', linestyle='-.', linewidth=1.0, zorder=1)
    ax.text(0.82, 0.90, r'$\alpha^{+} = \alpha^{-}$', fontsize=8,
            rotation=40, color='#888888', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))

    # Descriptive annotations for axes regions
    ax.annotate('', xy=(0.98, 0.02), xytext=(0.55, 0.02),
                arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.0))
    ax.text(0.77, 0.035, 'High positive\nlearning', fontsize=7, color='#D55E00',
            ha='center', va='bottom', fontstyle='italic')

    ax.annotate('', xy=(0.02, 0.98), xytext=(0.02, 0.55),
                arrowprops=dict(arrowstyle='->', color='#56B4E9', lw=1.0))
    ax.text(0.045, 0.77, 'High negative\nlearning', fontsize=7, color='#56B4E9',
            ha='left', va='center', fontstyle='italic', rotation=90)

    ax.set_xlabel(r'$\alpha^{+}$ (Positive Learning Rate)')
    ax.set_ylabel(r'$\alpha^{-}$ (Negative Learning Rate)')
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_aspect('equal')

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'Figure_4_Theoretical_Pattern_Map.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> Saved Figure_4_Theoretical_Pattern_Map.png")


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE 5 – Cross-Method Comparison Heatmap (LCGA x GMM)
# ═════════════════════════════════════════════════════════════════════════════
def figure_5():
    print("Generating Figure 5: Cross-Method Comparison Heatmap...")

    # Cross-tabulation
    ct_data = np.array([
        [19,  0,  3,  0, 30,  0],
        [ 1, 14, 22,  9,  0,  2],
    ])

    gmm_labels = [
        'Class 1\nConvergent\n(Rapid)',
        'Class 2\nOscillating',
        'Class 3\nConvergent\n(Gradual)',
        'Class 4\nABE',
        'Class 5\nCatastrophic',
        'Class 6\nExtreme\nCompliance',
    ]
    lcga_labels = [
        'LCGA Class 1\n($n$ = 52)',
        'LCGA Class 2\n($n$ = 48)',
    ]

    fig, ax = plt.subplots(figsize=(7.0, 3.0))

    # Normalize for color mapping (per row or absolute)
    im = ax.imshow(ct_data, cmap='YlOrRd', aspect='auto', vmin=0, vmax=30)

    # Annotate cells
    for i in range(2):
        for j in range(6):
            val = ct_data[i, j]
            text_color = 'white' if val > 18 else '#333333'
            ax.text(j, i, str(val), ha='center', va='center',
                    fontsize=11, fontweight='bold', color=text_color)

    ax.set_xticks(range(6))
    ax.set_xticklabels(gmm_labels, fontsize=8)
    ax.set_yticks(range(2))
    ax.set_yticklabels(lcga_labels, fontsize=9)

    ax.set_xlabel('GMM Class (Micro-level Patterns)', labelpad=8)
    ax.set_ylabel('LCGA Class\n(Macro-level Trajectories)', labelpad=8)

    # Move x-axis labels to top for clarity (optional, but keep at bottom for APA)
    ax.tick_params(axis='x', bottom=True, top=False, labelbottom=True, labeltop=False)

    # ARI annotation
    ax.text(5.4, -0.7, 'ARI = 0.362', fontsize=9, fontstyle='italic',
            ha='right', va='top', color='#333333',
            bbox=dict(boxstyle='round,pad=0.3', fc='#f5f5f5', ec='#cccccc', lw=0.5))

    # Colorbar
    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label('Count', fontsize=9)
    cbar.ax.tick_params(labelsize=8)

    # Restore all spines for heatmap
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.5)
        spine.set_color('#cccccc')

    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'Figure_5_Cross_Method_Comparison.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print("  -> Saved Figure_5_Cross_Method_Comparison.png")


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print(f"Output directory: {FIG_DIR}\n")
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    figure_5()
    print("\nAll 5 figures generated successfully.")
