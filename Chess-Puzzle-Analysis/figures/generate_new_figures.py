#!/usr/bin/env python3
"""
Generate 3 new publication-quality figures for Paper 5:
  Figure 2: 3D Theoretical Trust Calibration Framework (T × R × τ)
  Figure 3: Theoretical Predictions vs Empirical Findings (composite)
  Figure 6: GMM Model Selection (BIC across G and parameterizations)

Style: Human Factors journal, APA-compatible, 300 DPI, serif fonts.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Ellipse
from mpl_toolkits.mplot3d import Axes3D, proj3d

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

FIG_DIR = '/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/Chess-Puzzle-Analysis/figures'

# ── Pattern colors (Tol/Wong palette) ────────────────────────────────────────
PAT_COLORS = {
    'Convergent':   '#117733',
    'Oscillating':  '#EE7733',
    'Stagnant':     '#CC3311',
    'Catastrophic': '#882255',
    'ABE':          '#0077BB',
}


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 – 3D Theoretical Trust Calibration Framework
# ═══════════════════════════════════════════════════════════════════════════════
class Arrow3D(FancyArrowPatch):
    """3D arrow helper."""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return min(zs)


def figure_2_3d_framework():
    """Theoretical 3D T×R×τ trajectories with idealized smooth curves."""
    print("Generating Figure 2: 3D Theoretical Framework...")

    fig = plt.figure(figsize=(9.0, 7.5))
    ax = fig.add_subplot(111, projection='3d')

    # --- Calibration plane T = R ---
    r_plane = np.linspace(0, 1, 25)
    tau_plane = np.linspace(0, 10, 25)
    R_grid, Tau_grid = np.meshgrid(r_plane, tau_plane)
    T_grid = R_grid

    ax.plot_surface(Tau_grid, R_grid, T_grid, alpha=0.08, color='#999999',
                    edgecolor='none', zorder=0)
    ax.text(1.0, 0.82, 0.90, '$T = R$\n(Perfect Calibration)',
            fontsize=8, color='#777777', fontstyle='italic', ha='center')

    # --- Reliability switch plane at τ = 5 ---
    r_sw = np.linspace(0, 1, 8)
    t_sw = np.linspace(0, 1, 8)
    R_sw, T_sw = np.meshgrid(r_sw, t_sw)
    Tau_sw = np.full_like(R_sw, 5.0)
    ax.plot_surface(Tau_sw, R_sw, T_sw, alpha=0.04, color='#444444',
                    edgecolor='none', zorder=0)
    ax.text(5.0, 1.08, 0.0, 'Reliability\nSwitch', fontsize=7.5,
            color='#555555', ha='center', va='bottom')

    # Time axis
    tau = np.linspace(0, 10, 300)
    switch = 5.0

    # --- 1. Convergent (Green) ---
    # High R → trust catches up; then R drops → trust adapts down
    R_conv = np.where(tau < switch, 0.80, 0.80 - 0.50 * (1 - np.exp(-0.8 * (tau - switch))))
    T_conv = np.where(tau < switch,
                      0.40 + 0.38 * (1 - np.exp(-0.6 * tau)),
                      0.78 - 0.45 * (1 - np.exp(-0.7 * (tau - switch))))
    ax.plot(tau, R_conv, T_conv, '-', color=PAT_COLORS['Convergent'],
            linewidth=2.8, zorder=5, label='Convergent')
    ax.scatter([tau[0]], [R_conv[0]], [T_conv[0]], color=PAT_COLORS['Convergent'],
               s=60, marker='o', edgecolors='white', linewidths=0.8, zorder=6)
    ax.scatter([tau[-1]], [R_conv[-1]], [T_conv[-1]], color=PAT_COLORS['Convergent'],
               s=80, marker='*', edgecolors='white', linewidths=0.5, zorder=6)

    # --- 2. Oscillating (Orange) ---
    R_osc = np.where(tau < switch, 0.50, 0.50 + 0.30 * (1 - np.exp(-0.5 * (tau - switch))))
    T_osc_base = np.where(tau < switch,
                          0.50 + 0.05 * tau,
                          0.75 - 0.20 * np.exp(-0.3 * (tau - switch)))
    T_osc = T_osc_base + 0.12 * np.sin(1.8 * np.pi * tau / 5) * np.exp(-0.08 * tau)
    ax.plot(tau, R_osc, T_osc, '-', color=PAT_COLORS['Oscillating'],
            linewidth=2.8, zorder=5, label='Oscillating')
    ax.scatter([tau[0]], [R_osc[0]], [T_osc[0]], color=PAT_COLORS['Oscillating'],
               s=60, marker='o', edgecolors='white', linewidths=0.8, zorder=6)
    ax.scatter([tau[-1]], [R_osc[-1]], [T_osc[-1]], color=PAT_COLORS['Oscillating'],
               s=80, marker='*', edgecolors='white', linewidths=0.5, zorder=6)

    # --- 3. Stagnant (Red) ---
    R_stag = np.where(tau < switch, 0.70, 0.70 - 0.35 * (1 - np.exp(-0.6 * (tau - switch))))
    T_stag = 0.30 + 0.015 * np.sin(0.4 * np.pi * tau)  # Nearly flat
    ax.plot(tau, R_stag, T_stag, '-', color=PAT_COLORS['Stagnant'],
            linewidth=2.8, zorder=5, label='Stagnant')
    ax.scatter([tau[0]], [R_stag[0]], [T_stag[0]], color=PAT_COLORS['Stagnant'],
               s=60, marker='o', edgecolors='white', linewidths=0.8, zorder=6)
    ax.scatter([tau[-1]], [R_stag[-1]], [T_stag[-1]], color=PAT_COLORS['Stagnant'],
               s=80, marker='*', edgecolors='white', linewidths=0.5, zorder=6)

    # --- 4. Catastrophic (Purple) ---
    R_cat = np.where(tau < switch, 0.80, 0.80 - 0.50 * (1 - np.exp(-0.8 * (tau - switch))))
    T_cat = np.where(tau < switch,
                     0.70 + 0.08 * (1 - np.exp(-0.3 * tau)),
                     0.78 - 0.05 * np.log1p(tau - switch))  # Barely moves down
    ax.plot(tau, R_cat, T_cat, '-', color=PAT_COLORS['Catastrophic'],
            linewidth=2.8, zorder=5, label='Catastrophic')
    ax.scatter([tau[0]], [R_cat[0]], [T_cat[0]], color=PAT_COLORS['Catastrophic'],
               s=60, marker='o', edgecolors='white', linewidths=0.8, zorder=6)
    ax.scatter([tau[-1]], [R_cat[-1]], [T_cat[-1]], color=PAT_COLORS['Catastrophic'],
               s=80, marker='*', edgecolors='white', linewidths=0.5, zorder=6)

    # --- 5. ABE (Blue) ---
    R_abe = np.where(tau < switch, 0.20, 0.20 + 0.55 * (1 - np.exp(-0.6 * (tau - switch))))
    T_abe = np.where(tau < switch,
                     0.15 + 0.03 * tau,
                     0.30 + 0.03 * np.log1p(tau - switch))  # Barely moves up
    ax.plot(tau, R_abe, T_abe, '-', color=PAT_COLORS['ABE'],
            linewidth=2.8, zorder=5, label='ABE')
    ax.scatter([tau[0]], [R_abe[0]], [T_abe[0]], color=PAT_COLORS['ABE'],
               s=60, marker='o', edgecolors='white', linewidths=0.8, zorder=6)
    ax.scatter([tau[-1]], [R_abe[-1]], [T_abe[-1]], color=PAT_COLORS['ABE'],
               s=80, marker='*', edgecolors='white', linewidths=0.5, zorder=6)

    # --- Axes ---
    ax.set_xlabel('Time ($\\tau$)', fontsize=10, labelpad=10)
    ax.set_ylabel('AI Reliability ($R$)', fontsize=10, labelpad=10)
    ax.set_zlabel('Trust ($T$)', fontsize=10, labelpad=10)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xticks([0, 2, 4, 5, 6, 8, 10])
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_zticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.view_init(elev=22, azim=-55)
    ax.tick_params(axis='both', which='major', labelsize=7.5, pad=2)

    # Legend
    legend_elements = [
        Line2D([0], [0], color=PAT_COLORS['Convergent'], lw=2.5, label='Convergent'),
        Line2D([0], [0], color=PAT_COLORS['Oscillating'], lw=2.5, label='Oscillating'),
        Line2D([0], [0], color=PAT_COLORS['Stagnant'], lw=2.5, label='Stagnant'),
        Line2D([0], [0], color=PAT_COLORS['Catastrophic'], lw=2.5, label='Catastrophic'),
        Line2D([0], [0], color=PAT_COLORS['ABE'], lw=2.5, label='ABE'),
        Line2D([0], [0], color='none', marker='o', markerfacecolor='gray',
               markersize=6, label='Start ($\\tau = 0$)'),
        Line2D([0], [0], color='none', marker='*', markerfacecolor='gray',
               markersize=8, label='End ($\\tau = 10$)'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(-0.08, 0.98),
              frameon=True, framealpha=0.95, edgecolor='#cccccc',
              fontsize=8, handlelength=2.5, ncol=1, borderpad=0.6)

    # Pane styling
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#dddddd')
    ax.yaxis.pane.set_edgecolor('#dddddd')
    ax.zaxis.pane.set_edgecolor('#dddddd')
    ax.xaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)
    ax.yaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)
    ax.zaxis._axinfo['grid']['color'] = (0.85, 0.85, 0.85, 0.4)

    fig.tight_layout(pad=1.5)
    outpath = os.path.join(FIG_DIR, 'Figure_2_3D_Theoretical_Framework.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 – Theoretical Predictions vs Empirical Findings (composite)
# ═══════════════════════════════════════════════════════════════════════════════
def figure_3_theory_vs_empirical():
    """Side-by-side: (a) Theoretical calibration gap predictions, (b) Empirical GMM."""
    print("Generating Figure 3: Theory vs Empirical Comparison...")

    fig = plt.figure(figsize=(12.0, 5.5))

    # ── Panel (a): Theoretical Predictions ──
    ax_theory = fig.add_subplot(121)

    tau_th = np.linspace(1, 6, 200)
    switch = 4.5

    # AI accuracy by condition
    ai_c1 = np.where(tau_th <= switch, 0.80, 0.80 - 0.50 * np.clip((tau_th - switch) / 0.5, 0, 1))
    ai_c2 = np.where(tau_th <= switch, 0.20, 0.20 + 0.55 * np.clip((tau_th - switch) / 0.5, 0, 1))

    # Theoretical calibration gap = R_b - AI_accuracy
    # Convergent (C1→C2 or vice versa): gap approaches 0
    gap_conv = np.where(tau_th <= switch,
                        0.02 + 0.005 * (tau_th - 1),
                        -0.20 * np.exp(-1.5 * (tau_th - switch)))

    # Catastrophic (C1, High→Low): gap jumps up (over-reliance persists)
    gap_cat = np.where(tau_th <= switch,
                       0.02 + 0.005 * (tau_th - 1),
                       0.30 * (1 - np.exp(-2.0 * (tau_th - switch))))

    # Oscillating (C2, Low→High): gap fluctuates
    gap_osc = np.where(tau_th <= switch,
                       -0.05 + 0.01 * (tau_th - 1),
                       -0.15 * np.sin(3.5 * (tau_th - switch)) * np.exp(-0.4 * (tau_th - switch)))

    # ABE (C2, Low→High): gap stays strongly negative
    gap_abe = np.where(tau_th <= switch,
                       -0.04 + 0.005 * (tau_th - 1),
                       -0.30 * (1 - np.exp(-1.5 * (tau_th - switch))))

    # Stagnant: gap stays roughly constant
    gap_stag = 0.15 + 0.01 * np.sin(0.8 * np.pi * tau_th)

    # Reliability switch line
    ax_theory.axvline(x=switch, color='#333333', linestyle='--', linewidth=0.9, zorder=2)
    ax_theory.axhline(y=0, color='#888888', linestyle='-', linewidth=0.6, zorder=1)

    ax_theory.plot(tau_th, gap_conv, '-', color=PAT_COLORS['Convergent'],
                   linewidth=2.2, label='Convergent')
    ax_theory.plot(tau_th, gap_cat, '-', color=PAT_COLORS['Catastrophic'],
                   linewidth=2.2, label='Catastrophic')
    ax_theory.plot(tau_th, gap_osc, '-', color=PAT_COLORS['Oscillating'],
                   linewidth=2.2, label='Oscillating')
    ax_theory.plot(tau_th, gap_abe, '-', color=PAT_COLORS['ABE'],
                   linewidth=2.2, label='ABE')
    ax_theory.plot(tau_th, gap_stag, '-', color=PAT_COLORS['Stagnant'],
                   linewidth=2.2, label='Stagnant')

    # Shading
    ax_theory.fill_between(tau_th, 0, gap_cat, where=(gap_cat > 0),
                           color=PAT_COLORS['Catastrophic'], alpha=0.08)
    ax_theory.fill_between(tau_th, 0, gap_abe, where=(gap_abe < 0),
                           color=PAT_COLORS['ABE'], alpha=0.08)

    ax_theory.text(switch + 0.05, 0.35, 'Switch', fontsize=7.5, color='#555555', va='bottom')
    ax_theory.text(3.5, 0.18, 'Over-reliance', fontsize=7, color='#aa5555', fontstyle='italic', ha='center')
    ax_theory.text(3.5, -0.32, 'Under-reliance', fontsize=7, color='#5577aa', fontstyle='italic', ha='center')

    ax_theory.set_xlabel('Window ($\\tau$)')
    ax_theory.set_ylabel('Calibration Gap ($R_b - P$)')
    ax_theory.set_xlim(0.5, 6.5)
    ax_theory.set_ylim(-0.45, 0.45)
    ax_theory.set_xticks([1, 2, 3, 4, 5, 6])
    ax_theory.legend(frameon=True, framealpha=0.95, edgecolor='#cccccc',
                     fontsize=7.5, loc='lower left')
    ax_theory.set_title('(a) Theoretical Predictions', fontweight='bold', fontsize=11)

    # ── Panel (b): Empirical GMM Findings ──
    ax_emp = fig.add_subplot(122)

    # Empirical mean calibration gaps by GMM class (R_b - AI_accuracy)
    # Class 5: Catastrophic (C1, n=30) — trust inertia, over-reliance post-switch
    emp_cls5 = {'windows': [1,2,3,4,5,6],
                'gap': [-0.200, 0.020, -0.167, -0.300, 0.420, 0.420]}
    # Class 1: Convergent Rapid (C1, n=20) — adapts reliance down
    emp_cls1 = {'windows': [1,2,3,4,5,6],
                'gap': [-0.170, -0.050, -0.220, -0.230, 0.110, 0.140]}
    # Class 3: Convergent Gradual (C2, n=25) — gradual trust building
    emp_cls3 = {'windows': [1,2,3,4,5,6],
                'gap': [0.080, 0.056, 0.272, 0.288, -0.208, -0.072]}
    # Class 2: Oscillating (C2, n=14) — non-monotonic adjustment
    emp_cls2 = {'windows': [1,2,3,4,5,6],
                'gap': [0.329, 0.171, 0.471, 0.357, -0.343, -0.371]}
    # Class 4: ABE (C2, n=9) — persistent under-reliance despite improvement
    emp_cls4 = {'windows': [1,2,3,4,5,6],
                'gap': [-0.067, -0.244, 0.089, 0.222, -0.533, -0.600]}

    ax_emp.axvline(x=4.5, color='#333333', linestyle='--', linewidth=0.9, zorder=2)
    ax_emp.axhline(y=0, color='#888888', linestyle='-', linewidth=0.6, zorder=1)

    for cls_data, name, color, marker, n in [
        (emp_cls5, 'Catastrophic', PAT_COLORS['Catastrophic'], 'v', 30),
        (emp_cls1, 'Convergent (R)', PAT_COLORS['Convergent'], 'o', 20),
        (emp_cls3, 'Convergent (G)', '#44AA99', 's', 25),
        (emp_cls2, 'Oscillating', PAT_COLORS['Oscillating'], 'D', 14),
        (emp_cls4, 'ABE', PAT_COLORS['ABE'], '^', 9),
    ]:
        ax_emp.plot(cls_data['windows'], cls_data['gap'], f'{marker}-',
                    color=color, linewidth=2.0, markersize=5, markeredgecolor='white',
                    markeredgewidth=0.5, label=f'{name} ($n$={n})', zorder=4)

    # Shading for catastrophic over-reliance
    ax_emp.fill_between(emp_cls5['windows'], 0, emp_cls5['gap'],
                        where=[g > 0 for g in emp_cls5['gap']],
                        color=PAT_COLORS['Catastrophic'], alpha=0.08, interpolate=True)
    ax_emp.fill_between(emp_cls4['windows'], 0, emp_cls4['gap'],
                        where=[g < 0 for g in emp_cls4['gap']],
                        color=PAT_COLORS['ABE'], alpha=0.08, interpolate=True)

    ax_emp.text(4.55, 0.35, 'Switch', fontsize=7.5, color='#555555', va='bottom')

    ax_emp.set_xlabel('Window ($\\tau$)')
    ax_emp.set_ylabel('Calibration Gap ($R_b - P$)')
    ax_emp.set_xlim(0.5, 6.5)
    ax_emp.set_ylim(-0.75, 0.45)
    ax_emp.set_xticks([1, 2, 3, 4, 5, 6])
    ax_emp.legend(frameon=True, framealpha=0.95, edgecolor='#cccccc',
                  fontsize=7.5, loc='lower left')
    ax_emp.set_title('(b) Empirical GMM Classes (Chess Data)', fontweight='bold', fontsize=11)

    fig.tight_layout(w_pad=3.0)
    outpath = os.path.join(FIG_DIR, 'Figure_3_Theory_vs_Empirical.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 6 – GMM Model Selection (BIC by G and Parameterization)
# ═══════════════════════════════════════════════════════════════════════════════
def figure_6_gmm_model_selection():
    """BIC comparison across G and covariance parameterizations for S2."""
    print("Generating Figure 6: GMM Model Selection...")

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.5))

    # ── S2 BIC data (from mclust output) ──
    G_vals = [2, 3, 4, 5, 6, 7, 8]

    bic_s2 = {
        'EII': [-5575.2, -5496.6, -5372.5, -5322.5, -5268.0, -5251.8, -5235.8],
        'VII': [-5569.1, -5423.3, -5335.7, -5267.6, -5218.3, -5167.5, -5152.8],
        'EEI': [-5430.2, -5312.5, -5079.4, -5030.4, -4996.4, -4997.7, -4992.6],
        'VEI': [-5425.0, -5236.9, -5065.4, -5026.4, -4966.3, -5050.1, -5042.8],
    }

    # Best BIC per G
    best_bic = []
    best_model = []
    for i, g in enumerate(G_vals):
        bics = [(bic_s2[m][i], m) for m in bic_s2]
        b, m = max(bics, key=lambda x: x[0])
        best_bic.append(b)
        best_model.append(m)

    # ── Panel (a): BIC by G across parameterizations ──
    ax1 = axes[0]
    param_styles = {
        'EII': {'color': '#999999', 'ls': ':', 'marker': 'o', 'ms': 4},
        'VII': {'color': '#666666', 'ls': '-.', 'marker': 's', 'ms': 4},
        'EEI': {'color': '#E69F00', 'ls': '--', 'marker': 'D', 'ms': 4},
        'VEI': {'color': '#D55E00', 'ls': '-', 'marker': '^', 'ms': 5},
    }

    for param, vals in bic_s2.items():
        st = param_styles[param]
        ax1.plot(G_vals, vals, f'{st["marker"]}{st["ls"]}', color=st['color'],
                 linewidth=1.8, markersize=st['ms'], markeredgecolor='white',
                 markeredgewidth=0.4, label=param, zorder=4)

    # Highlight optimal point
    opt_idx = best_bic.index(max(best_bic))
    ax1.scatter([G_vals[opt_idx]], [max(best_bic)], s=200, facecolors='none',
                edgecolors='#D55E00', linewidths=2.5, zorder=6)
    ax1.annotate(f'Optimal\n$G$={G_vals[opt_idx]}, VEI\nBIC={max(best_bic):.1f}',
                 xy=(G_vals[opt_idx], max(best_bic)),
                 xytext=(G_vals[opt_idx] + 1.0, max(best_bic) + 120),
                 fontsize=8, ha='center', color='#D55E00', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', fc='#fff5ee', ec='#D55E00', lw=0.8))

    ax1.set_xlabel('Number of Classes ($G$)')
    ax1.set_ylabel('BIC (higher is better)')
    ax1.set_xticks(G_vals)
    ax1.legend(frameon=True, framealpha=0.95, edgecolor='#cccccc',
               title='Parameterization', title_fontsize=8, fontsize=8)
    ax1.set_title('(a) BIC Across $G$ and Parameterizations', fontweight='bold')

    # ── Panel (b): Best BIC per G (elbow plot with delta-BIC) ──
    ax2 = axes[1]

    # Line plot (zoomed y-axis for clarity)
    ax2.plot(G_vals, best_bic, 'o-', color='#333333', linewidth=2.0,
             markersize=7, markeredgecolor='white', markeredgewidth=0.8, zorder=4)

    # Highlight optimal
    ax2.scatter([G_vals[opt_idx]], [best_bic[opt_idx]], s=180, facecolors='none',
                edgecolors='#D55E00', linewidths=2.5, zorder=6)

    # Model name annotations
    for i, (g, bic, model) in enumerate(zip(G_vals, best_bic, best_model)):
        offset_y = 18 if i != opt_idx else -35
        ax2.annotate(model, xy=(g, bic), xytext=(0, offset_y),
                     textcoords='offset points', ha='center', fontsize=7.5,
                     fontweight='bold' if i == opt_idx else 'normal',
                     color='#D55E00' if i == opt_idx else '#666666')

    # Delta-BIC arrows
    delta_bic_5_6 = best_bic[4] - best_bic[3]  # G6 - G5
    delta_bic_6_7 = best_bic[5] - best_bic[4]  # G7 - G6
    mid_y_56 = (best_bic[3] + best_bic[4]) / 2
    mid_y_67 = (best_bic[4] + best_bic[5]) / 2

    ax2.annotate('', xy=(6, best_bic[4]), xytext=(5, best_bic[3]),
                 arrowprops=dict(arrowstyle='->', color='#117733', lw=1.2))
    ax2.text(5.5, mid_y_56 + 10, f'$\\Delta$={delta_bic_5_6:.1f}',
             fontsize=7.5, ha='center', color='#117733', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#eef8ee', ec='#117733', lw=0.5))

    ax2.annotate('', xy=(7, best_bic[5]), xytext=(6, best_bic[4]),
                 arrowprops=dict(arrowstyle='->', color='#CC3311', lw=1.2))
    ax2.text(6.5, mid_y_67 - 10, f'$\\Delta$={delta_bic_6_7:.1f}',
             fontsize=7.5, ha='center', color='#CC3311', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#fee', ec='#CC3311', lw=0.5))

    # Zoom into the relevant BIC range
    y_min = min(best_bic) - 50
    y_max = max(best_bic) + 80
    ax2.set_ylim(y_min, y_max)
    ax2.set_xlabel('Number of Classes ($G$)')
    ax2.set_ylabel('Best BIC (higher is better)')
    ax2.set_xticks(G_vals)
    ax2.set_title('(b) Best BIC per $G$ (Elbow Plot)', fontweight='bold')

    fig.tight_layout(w_pad=3.0)
    outpath = os.path.join(FIG_DIR, 'Figure_6_GMM_Model_Selection.png')
    fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  -> Saved {os.path.basename(outpath)}")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    os.makedirs(FIG_DIR, exist_ok=True)
    figure_2_3d_framework()
    figure_3_theory_vs_empirical()
    figure_6_gmm_model_selection()
    print("\nAll 3 new figures generated successfully.")
