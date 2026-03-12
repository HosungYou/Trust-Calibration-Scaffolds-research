#!/usr/bin/env python3
"""
Generate the 5-pattern theoretical trajectory figure.
Adds "AI Benefit Emergence" (Type 5) to the original 4-pattern figure.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'figure.facecolor': 'white',
})

t = np.linspace(0, 1, 200)

# Trajectory data
patterns = [
    {
        'name': 'Type 1: Convergent',
        'subtitle': '"Bayesian Decision Maker"',
        'color': '#1a9e76',
        'fill_color': '#1a9e7630',
        'y': 0.7 * np.exp(-4 * t),
        'desc_top': 'Gap shrinks monotonically',
        'desc_bot': 'Trust converges to reliability (adaptive)',
    },
    {
        'name': 'Type 2: Oscillating',
        'subtitle': '"Cautious Adjuster"',
        'color': '#e6851e',
        'fill_color': '#e6851e30',
        'y': 0.15 + 0.35 * np.exp(-2.5 * t) * np.abs(np.sin(4 * np.pi * t)),
        'desc_top': 'Damped oscillation',
        'desc_bot': 'Eventual convergence (slow)',
    },
    {
        'name': 'Type 3: Stagnant',
        'subtitle': '"Stubborn User"',
        'color': '#d62728',
        'fill_color': '#d6272830',
        'y': 0.48 + 0.02 * np.sin(2 * np.pi * t),
        'desc_top': 'Gap persists',
        'desc_bot': 'Trust never matches reliability',
    },
    {
        'name': 'Type 4: Catastrophic',
        'subtitle': '"Betrayed Truster"',
        'color': '#9467bd',
        'fill_color': '#9467bd30',
        'y': np.where(t < 0.55, 0.12 - 0.04 * t, 0.12 - 0.04 * 0.55 + 0.55 * (1 - np.exp(-8 * (t - 0.55)))),
        'desc_top': 'Sudden trust collapse',
        'desc_bot': 'Triggered by negative event',
    },
    {
        'name': 'Type 5: Divergent\nUnder-Adaptation',
        'subtitle': '"AI Benefit Emergence"',
        'color': '#2176ae',
        'fill_color': '#2176ae30',
        'y': 0.05 + 0.55 * (1 - np.exp(-2.0 * t)) * t,
        'desc_top': 'Gap widens gradually',
        'desc_bot': 'AI improves, reliance lags behind',
    },
]

# Layout: 3 panels top row, 2 panels bottom row (centered)
fig = plt.figure(figsize=(16, 8.5))
fig.suptitle('Theoretically Predicted Trajectory Types (T × R × τ Model)',
             fontsize=15, fontweight='bold', y=0.97)

# Create gridspec for uneven layout
gs_top = fig.add_gridspec(2, 6, hspace=0.50, wspace=0.35,
                          top=0.88, bottom=0.08, left=0.04, right=0.96)

# Top row: 3 panels spanning 2 columns each
axes_top = [fig.add_subplot(gs_top[0, i*2:(i+1)*2]) for i in range(3)]
# Bottom row: 2 panels centered (spanning cols 1-3 and 3-5)
axes_bot = [fig.add_subplot(gs_top[1, 1:3]), fig.add_subplot(gs_top[1, 3:5])]

all_axes = axes_top + axes_bot

for ax, pat in zip(all_axes, patterns):
    y = pat['y']

    # Plot
    ax.plot(t, y, color=pat['color'], linewidth=2.5, zorder=3)
    ax.fill_between(t, 0, y, color=pat['fill_color'], alpha=0.4, zorder=2)

    # Event marker for catastrophic
    if 'Catastrophic' in pat['name']:
        event_x = 0.55
        event_y_val = np.interp(event_x, t, y)
        ax.axvline(x=event_x, color='gray', linestyle='--', alpha=0.5, linewidth=1)
        ax.annotate('Trust\nviolation', xy=(event_x, event_y_val),
                    xytext=(event_x + 0.12, event_y_val - 0.08),
                    fontsize=7, color='gray', ha='center',
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.8))

    # Annotations for divergent pattern
    if 'Divergent' in pat['name']:
        # Arrow showing widening gap
        ax.annotate('', xy=(0.85, 0.42), xytext=(0.85, 0.08),
                    arrowprops=dict(arrowstyle='<->', color=pat['color'],
                                    lw=1.5, linestyle='-'))
        ax.text(0.92, 0.25, 'Gap\nwidens', fontsize=7, color=pat['color'],
                ha='center', va='center')

    # Styling
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 0.82)
    ax.set_xticks([0, 0.5, 1.0])
    ax.set_xticklabels(['Early', 'Mid', 'Late'], fontsize=9)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8])
    ax.set_yticklabels(['0', '0.2', '0.4', '0.6', '0.8'], fontsize=8)
    ax.set_xlabel('Time (window)', fontsize=9)
    if ax in [axes_top[0], axes_bot[0]]:
        ax.set_ylabel('|Trust − Reliability| Gap', fontsize=9)

    # Title and subtitle
    title_color = pat['color']
    ax.set_title(pat['name'], color=title_color, fontsize=11, fontweight='bold', pad=12)
    ax.text(0.5, 1.02, pat['subtitle'], transform=ax.transAxes,
            fontsize=8, fontstyle='italic', color='#666666',
            ha='center', va='bottom')

    # Description below
    desc = f"- {pat['desc_top']}\n- {pat['desc_bot']}"
    ax.text(0.5, -0.22, desc, transform=ax.transAxes,
            fontsize=7.5, color='#555555', ha='center', va='top')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.2, linewidth=0.5)

# NEW badge on Type 5
ax5 = axes_bot[1]
ax5.text(0.98, 0.95, 'NEW', transform=ax5.transAxes,
         fontsize=9, fontweight='bold', color='white',
         ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#2176ae',
                   edgecolor='none', alpha=0.9))

# Save
out_2d = "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/figures/Figure_2D_5_Trajectory_Patterns.png"
fig.savefig(out_2d, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Saved: {out_2d}")
plt.close()


# =============================================================================
# 3D Figure: 5 trajectories in T × R × τ space
# =============================================================================
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

tau = np.linspace(0, 10, 200)

trajectories_3d = {
    'Convergent': {
        'T': 0.3 + 0.5 * (1 - np.exp(-0.4 * tau)),
        'R': np.full_like(tau, 0.8),
        'color': '#1a9e76', 'lw': 2.5,
    },
    'Oscillating': {
        'T': 0.5 + 0.3 * np.exp(-0.2 * tau) * np.sin(1.5 * tau),
        'R': np.full_like(tau, 0.5),
        'color': '#e6851e', 'lw': 2.5,
    },
    'Stagnant': {
        'T': np.full_like(tau, 0.3) + 0.02 * np.sin(0.5 * tau),
        'R': np.full_like(tau, 0.7),
        'color': '#d62728', 'lw': 2.5,
    },
    'Catastrophic': {
        'T': np.where(tau < 5, 0.7 + 0.05 * tau/5, 0.75 - 0.5 * (1 - np.exp(-1.5 * (tau - 5)))),
        'R': np.where(tau < 5, 0.8, 0.8 - 0.5 * (1 - np.exp(-2 * (tau - 5)))),
        'color': '#9467bd', 'lw': 2.5,
    },
    'AI Benefit\nEmergence (NEW)': {
        'T': 0.2 + 0.15 * (1 - np.exp(-0.15 * tau)),
        'R': 0.2 + 0.6 * (1 - np.exp(-0.35 * tau)),
        'color': '#2176ae', 'lw': 3.0,
    },
}

for name, traj in trajectories_3d.items():
    T = traj['T']
    R = traj['R']
    ax.plot(tau, T, R, color=traj['color'], linewidth=traj['lw'], label=name, alpha=0.9)
    # Start marker
    ax.scatter([tau[0]], [T[0]], [R[0]], color=traj['color'], s=40, zorder=5)
    # End marker (arrow-like)
    ax.scatter([tau[-1]], [T[-1]], [R[-1]], color=traj['color'], s=60,
               marker='>', zorder=5)

# T=R plane (diagonal)
t_plane = np.linspace(0, 1, 50)
tau_plane = np.linspace(0, 10, 50)
T_mesh, TAU_mesh = np.meshgrid(t_plane, tau_plane)
R_mesh = T_mesh  # T = R plane
ax.plot_surface(TAU_mesh, T_mesh, R_mesh, alpha=0.08, color='gray')
ax.text(8, 0.9, 0.9, 'T = R\n(Perfect\nCalibration)', fontsize=8,
        color='gray', alpha=0.6)

ax.set_xlabel('Time (τ)', fontsize=11, labelpad=10)
ax.set_ylabel('Trust / Reliance (T)', fontsize=11, labelpad=10)
ax.set_zlabel('AI Reliability (R)', fontsize=11, labelpad=10)
ax.set_title('T × R × τ 3D Trajectory Model\n(5 Theoretical Patterns)',
             fontsize=14, fontweight='bold', pad=20)

ax.view_init(elev=25, azim=-60)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

out_3d = "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper/figures/Figure_3D_5_Trajectory_Patterns.png"
fig.savefig(out_3d, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Saved: {out_3d}")
plt.close()

print("\nDone! Both figures generated with 5 trajectory patterns.")
