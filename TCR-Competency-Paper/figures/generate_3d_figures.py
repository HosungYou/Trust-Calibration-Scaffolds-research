"""
Generate 3D Trust-Reliability-Time figures for TCR-Competency Paper
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

# Output directory
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica Neue', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Colors
COLORS = {
    'calibrated': '#2ecc71',
    'overtrust': '#e74c3c',
    'undertrust': '#3498db',
    'avoidance': '#95a5a6',
    'trajectory_good': '#27ae60',
    'trajectory_bad': '#c0392b',
    'trajectory_osc': '#f39c12',
    'trajectory_stag': '#7f8c8d',
    'grid': '#ecf0f1',
    'diagonal': '#34495e',
}

# ─────────────────────────────────────────────
# Figure 1: 2D Trust-Reliability Matrix (baseline)
# ─────────────────────────────────────────────
def fig1_2d_matrix():
    fig, ax = plt.subplots(figsize=(7, 6))

    # Quadrant fills
    ax.fill_between([0.5, 1], 0.5, 1, color=COLORS['calibrated'], alpha=0.12)
    ax.fill_between([0, 0.5], 0.5, 1, color=COLORS['undertrust'], alpha=0.12)
    ax.fill_between([0.5, 1], 0, 0.5, color=COLORS['overtrust'], alpha=0.12)
    ax.fill_between([0, 0.5], 0, 0.5, color=COLORS['avoidance'], alpha=0.12)

    # Diagonal y=x
    ax.plot([0, 1], [0, 1], '--', color=COLORS['diagonal'], linewidth=1.5, alpha=0.7, label='T = R (Perfect Calibration)')

    # Labels
    ax.text(0.75, 0.75, 'Q1: Calibrated\n(Appropriate Use)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#1a7a3c')
    ax.text(0.25, 0.75, 'Q3: Undertrust\n(Missed Benefit)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#1f6aa5')
    ax.text(0.75, 0.25, 'Q2: Overtrust\n("Bastani Trap")', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#b52a1c')
    ax.text(0.25, 0.25, 'Q4: Calibrated\nAvoidance', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#6b7b86')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('AI Reliability (R)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Trust (T)', fontsize=12, fontweight='bold')
    ax.set_title('2D Trust-Reliability Matrix', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(['Low', '', 'Medium', '', 'High'])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticklabels(['Low', '', 'Medium', '', 'High'])
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    fig.savefig(os.path.join(OUT_DIR, 'Figure_1_2D_Trust_Reliability_Matrix.png'))
    plt.close()
    print("Figure 1 saved.")


# ─────────────────────────────────────────────
# Figure 2: 3D Trust × Reliability × Time with trajectories
# ─────────────────────────────────────────────
def fig2_3d_trajectories():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Diagonal plane T=R across time
    R_plane = np.linspace(0, 1, 20)
    T_plane = np.linspace(0, 1, 20)
    R_mesh, T_mesh = np.meshgrid(R_plane, T_plane)
    tau_plane = np.zeros_like(R_mesh)
    # Only draw where T≈R
    mask = np.abs(R_mesh - T_mesh) < 0.05

    # Draw y=x line at several time slices
    for t_val in [0, 0.33, 0.66, 1.0]:
        r_line = np.linspace(0, 1, 50)
        ax.plot(r_line, r_line, t_val, '--', color=COLORS['diagonal'], alpha=0.3, linewidth=0.8)

    # Trajectory A: Convergent (good calibrator)
    tau_a = np.linspace(0, 1, 100)
    r_a = 0.7 * np.ones_like(tau_a)
    t_a = 0.9 - 0.25 * (1 - np.exp(-3 * tau_a))  # starts overtrusting, converges to R
    ax.plot(r_a, t_a, tau_a, color=COLORS['trajectory_good'], linewidth=2.5, label='Convergent (High Readiness)')
    ax.scatter([r_a[0]], [t_a[0]], [tau_a[0]], color=COLORS['trajectory_good'], s=60, marker='o', zorder=5)
    ax.scatter([r_a[-1]], [t_a[-1]], [tau_a[-1]], color=COLORS['trajectory_good'], s=100, marker='*', zorder=5)

    # Trajectory B: Oscillating (developing calibrator)
    tau_b = np.linspace(0, 1, 100)
    r_b = 0.6 * np.ones_like(tau_b)
    t_b = 0.6 + 0.25 * np.sin(6 * np.pi * tau_b) * np.exp(-2 * tau_b)
    ax.plot(r_b, t_b, tau_b, color=COLORS['trajectory_osc'], linewidth=2.5, label='Oscillating (Developing)')
    ax.scatter([r_b[0]], [t_b[0]], [tau_b[0]], color=COLORS['trajectory_osc'], s=60, marker='o', zorder=5)
    ax.scatter([r_b[-1]], [t_b[-1]], [tau_b[-1]], color=COLORS['trajectory_osc'], s=100, marker='*', zorder=5)

    # Trajectory C: Stagnant (low readiness — stays overtrusting)
    tau_c = np.linspace(0, 1, 100)
    r_c = 0.4 * np.ones_like(tau_c)
    t_c = 0.85 + 0.02 * np.sin(2 * np.pi * tau_c)  # barely moves
    ax.plot(r_c, t_c, tau_c, color=COLORS['trajectory_bad'], linewidth=2.5, label='Stagnant (Low Readiness)')
    ax.scatter([r_c[0]], [t_c[0]], [tau_c[0]], color=COLORS['trajectory_bad'], s=60, marker='o', zorder=5)
    ax.scatter([r_c[-1]], [t_c[-1]], [tau_c[-1]], color=COLORS['trajectory_bad'], s=100, marker='*', zorder=5)

    # Trajectory D: Catastrophic drop (trust collapse)
    tau_d = np.linspace(0, 1, 100)
    r_d = np.where(tau_d < 0.5, 0.8, 0.8 - 0.4 * (tau_d - 0.5) / 0.5)  # R gradually drops
    t_d_pre = 0.8 * np.ones(50)
    # Catastrophe at tau=0.7
    t_d_post_1 = 0.8 * np.ones(20)
    t_d_collapse = 0.8 - 0.6 * np.exp(3 * (np.linspace(0, 1, 10) - 0.3))
    t_d_collapse = np.clip(t_d_collapse, 0.15, 0.8)
    t_d_after = 0.15 * np.ones(20)
    t_d = np.concatenate([t_d_pre, t_d_post_1, t_d_collapse, t_d_after])
    ax.plot(r_d, t_d, tau_d, color='#8e44ad', linewidth=2.5, label='Catastrophic Drop', linestyle='-.')
    ax.scatter([r_d[0]], [t_d[0]], [tau_d[0]], color='#8e44ad', s=60, marker='o', zorder=5)
    ax.scatter([r_d[-1]], [t_d[-1]], [tau_d[-1]], color='#8e44ad', s=100, marker='*', zorder=5)

    ax.set_xlabel('\nAI Reliability (R)', fontsize=11, fontweight='bold')
    ax.set_ylabel('\nTrust (T)', fontsize=11, fontweight='bold')
    ax.set_zlabel('\nTime (τ)', fontsize=11, fontweight='bold')
    ax.set_title('3D Trust × Reliability × Time: Calibration Trajectories', fontsize=13, fontweight='bold', pad=20)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)

    ax.view_init(elev=25, azim=135)
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

    fig.savefig(os.path.join(OUT_DIR, 'Figure_2_3D_Trust_Reliability_Time_Trajectories.png'))
    plt.close()
    print("Figure 2 saved.")


# ─────────────────────────────────────────────
# Figure 3: Hysteresis curve
# ─────────────────────────────────────────────
def fig3_hysteresis():
    fig, ax = plt.subplots(figsize=(7, 5))

    # Building path (slow increase)
    r_build = np.linspace(0, 1, 200)
    t_build = 1 / (1 + np.exp(-8 * (r_build - 0.6)))

    # Erosion path (fast decrease)
    r_erode = np.linspace(1, 0, 200)
    t_erode = 1 / (1 + np.exp(-8 * (r_erode - 0.35)))

    ax.plot(r_build, t_build, color=COLORS['trajectory_good'], linewidth=2.5, label='Trust Building (slow)')
    ax.plot(r_erode, t_erode, color=COLORS['trajectory_bad'], linewidth=2.5, label='Trust Erosion (fast)')

    # Arrows
    ax.annotate('', xy=(0.7, 0.73), xytext=(0.5, 0.27),
                arrowprops=dict(arrowstyle='->', color=COLORS['trajectory_good'], lw=2))
    ax.annotate('', xy=(0.3, 0.27), xytext=(0.5, 0.73),
                arrowprops=dict(arrowstyle='->', color=COLORS['trajectory_bad'], lw=2))

    # y=x diagonal
    ax.plot([0, 1], [0, 1], '--', color=COLORS['diagonal'], alpha=0.5, linewidth=1, label='T = R')

    # Hysteresis region
    ax.fill_between(r_build, t_build, np.interp(r_build, r_erode[::-1], t_erode[::-1]),
                     alpha=0.08, color='#8e44ad')
    ax.text(0.5, 0.5, 'Hysteresis\nRegion', ha='center', va='center',
            fontsize=11, fontstyle='italic', color='#6c3483', alpha=0.8)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('AI Reliability (R)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Trust (T)', fontsize=12, fontweight='bold')
    ax.set_title('Trust Hysteresis: Building vs. Erosion Paths', fontsize=13, fontweight='bold', pad=10)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    fig.savefig(os.path.join(OUT_DIR, 'Figure_3_Trust_Hysteresis.png'))
    plt.close()
    print("Figure 3 saved.")


# ─────────────────────────────────────────────
# Figure 4: Division of labor — Matrix vs TCRS
# ─────────────────────────────────────────────
def fig4_division_of_labor():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')

    # Left box: Matrix (T × R × τ)
    left_box = mpatches.FancyBboxPatch((0.02, 0.15), 0.4, 0.7,
                                         boxstyle="round,pad=0.02",
                                         facecolor='#eaf2f8', edgecolor='#2980b9', linewidth=2)
    ax.add_patch(left_box)
    ax.text(0.22, 0.8, 'Trust-Reliability Matrix + Time', ha='center', va='center',
            fontsize=12, fontweight='bold', color='#2c3e50')
    ax.text(0.22, 0.72, '(3D Diagnostic Space)', ha='center', va='center',
            fontsize=10, fontstyle='italic', color='#5d6d7e')
    ax.text(0.22, 0.60, 'T × R × τ', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#2980b9', family='monospace')
    ax.text(0.22, 0.48, 'WHERE is the learner?\nHOW is the learner moving?',
            ha='center', va='center', fontsize=10, color='#2c3e50')
    ax.text(0.22, 0.32, 'Output: Trajectory patterns\n(convergent, oscillating,\nstagnant, catastrophic)',
            ha='center', va='center', fontsize=9, color='#5d6d7e')

    # Right box: TCRS Readiness
    right_box = mpatches.FancyBboxPatch((0.58, 0.15), 0.4, 0.7,
                                          boxstyle="round,pad=0.02",
                                          facecolor='#eafaf1', edgecolor='#27ae60', linewidth=2)
    ax.add_patch(right_box)
    ax.text(0.78, 0.8, 'TCRS Process Model', ha='center', va='center',
            fontsize=12, fontweight='bold', color='#2c3e50')
    ax.text(0.78, 0.72, '(Readiness Mechanism)', ha='center', va='center',
            fontsize=10, fontstyle='italic', color='#5d6d7e')
    ax.text(0.78, 0.60, 'Aw → Jd → Ac', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#27ae60', family='monospace')
    ax.text(0.78, 0.48, 'WHY does the learner\nmove that way?',
            ha='center', va='center', fontsize=10, color='#2c3e50')
    ax.text(0.78, 0.32, 'Output: Readiness scores\n(CA-Aw, CA-Jd, CA-Ac)\nPredicts trajectory type',
            ha='center', va='center', fontsize=9, color='#5d6d7e')

    # Connection arrow
    ax.annotate('', xy=(0.57, 0.5), xytext=(0.43, 0.5),
                arrowprops=dict(arrowstyle='<->', color='#8e44ad', lw=2.5,
                                connectionstyle='arc3,rad=0'))
    ax.text(0.50, 0.55, 'Readiness\nexplains\ntrajectory', ha='center', va='bottom',
            fontsize=9, fontweight='bold', color='#8e44ad')

    # Bottom text
    ax.text(0.50, 0.05,
            'Matrix diagnoses the state and dynamics; TCRS explains the mechanism.\n'
            'Neither duplicates the other — they form a complementary ecosystem.',
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#2c3e50')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.95)
    ax.set_title('Division of Labor: Diagnostic Space vs. Readiness Mechanism',
                 fontsize=14, fontweight='bold', pad=15)

    fig.savefig(os.path.join(OUT_DIR, 'Figure_4_Division_of_Labor.png'))
    plt.close()
    print("Figure 4 saved.")


# ─────────────────────────────────────────────
# Figure 5: Convergence patterns linked to Readiness
# ─────────────────────────────────────────────
def fig5_patterns_readiness():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    time = np.linspace(0, 10, 200)

    # Pattern A: Convergent
    ax = axes[0]
    gap_a = 0.4 * np.exp(-0.5 * time)
    ax.plot(time, gap_a, color=COLORS['trajectory_good'], linewidth=2.5)
    ax.axhline(y=0, color=COLORS['diagonal'], linestyle='--', alpha=0.5)
    ax.fill_between(time, 0, gap_a, alpha=0.1, color=COLORS['trajectory_good'])
    ax.set_title('Pattern A: Convergent\n(High Readiness)', fontsize=11, fontweight='bold',
                 color=COLORS['trajectory_good'])
    ax.set_xlabel('Time (τ)')
    ax.set_ylabel('Trust-Reliability Gap\n|T - R|')
    ax.set_ylim(-0.1, 0.5)
    ax.grid(True, alpha=0.3)

    # Pattern B: Oscillating
    ax = axes[1]
    gap_b = 0.3 * np.sin(1.5 * time) * np.exp(-0.15 * time)
    ax.plot(time, gap_b, color=COLORS['trajectory_osc'], linewidth=2.5)
    ax.axhline(y=0, color=COLORS['diagonal'], linestyle='--', alpha=0.5)
    ax.fill_between(time, 0, gap_b, where=(gap_b > 0), alpha=0.1, color=COLORS['overtrust'])
    ax.fill_between(time, 0, gap_b, where=(gap_b < 0), alpha=0.1, color=COLORS['undertrust'])
    ax.set_title('Pattern B: Oscillating\n(Developing Readiness)', fontsize=11, fontweight='bold',
                 color=COLORS['trajectory_osc'])
    ax.set_xlabel('Time (τ)')
    ax.set_ylim(-0.4, 0.4)
    ax.text(8, 0.25, 'Overtrust', fontsize=8, color=COLORS['overtrust'], alpha=0.7)
    ax.text(8, -0.25, 'Undertrust', fontsize=8, color=COLORS['undertrust'], alpha=0.7)
    ax.grid(True, alpha=0.3)

    # Pattern C: Stagnant
    ax = axes[2]
    gap_c = 0.35 + 0.02 * np.sin(0.5 * time)
    ax.plot(time, gap_c, color=COLORS['trajectory_bad'], linewidth=2.5)
    ax.axhline(y=0, color=COLORS['diagonal'], linestyle='--', alpha=0.5)
    ax.fill_between(time, 0, gap_c, alpha=0.1, color=COLORS['trajectory_bad'])
    ax.set_title('Pattern C: Stagnant\n(Low Readiness)', fontsize=11, fontweight='bold',
                 color=COLORS['trajectory_bad'])
    ax.set_xlabel('Time (τ)')
    ax.set_ylim(-0.1, 0.5)
    ax.grid(True, alpha=0.3)

    plt.suptitle('Calibration Gap Dynamics: Trajectory Patterns Predicted by TCRS Readiness',
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, 'Figure_5_Patterns_Readiness_Link.png'))
    plt.close()
    print("Figure 5 saved.")


if __name__ == '__main__':
    fig1_2d_matrix()
    fig2_3d_trajectories()
    fig3_hysteresis()
    fig4_division_of_labor()
    fig5_patterns_readiness()
    print("\nAll figures generated successfully.")
