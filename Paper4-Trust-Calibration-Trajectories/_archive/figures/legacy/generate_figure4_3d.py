#!/usr/bin/env python3
"""
Generate Figure 4: Empirical 3D Trajectory Classes with Theory Annotations
and Velocity Vectors in R_b × P × τ Space.

Improvements over raw fig2_empirical_3d.png:
  1. Theory pattern labels annotated on each class
  2. Velocity vectors (arrows) showing direction & speed of change
  3. Publication-quality title and formatting
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

DATA = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
            "TCR-Trajectory-Paper/analysis/outputs/phase2_class_trajectories.csv")
OUT = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
           "TCR-Trajectory-Paper/figures/Figure_4_3D_Theory_vs_Empirical.png")

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

COLORS = {
    1: "#2196F3", 2: "#4CAF50", 3: "#FF9800",
    4: "#9C27B0", 5: "#F44336", 6: "#795548",
}

LABELS = {
    1: "C1: Gradual Adopter (29.9%)",
    2: "C2: Steady Calibrator (34.6%)",
    3: "C3: Strong Calibrator (18.8%)",
    4: "C4: High Performer (9.9%)",
    5: "C5: Heavy Adopter (5.3%)",
    6: "C6: Early Heavy User (1.5%)",
}

# Theory-empirical mapping (from RQ3 analysis)
THEORY_ANNOTATIONS = {
    1: "Gradual\nConvergence",
    2: "Steady\nConvergence",
    3: "Strong\nConvergence",
    4: "Stagnant\n(High P)",
    5: "Escalating\nReliance",
    6: "Self-Correcting\nOver-Reliance",
}

# Annotation positions (offset from endpoint for readability)
ANNOT_OFFSETS = {
    1: (0.02, 0.01, 0.3),
    2: (0.02, 0.01, 0.3),
    3: (-0.03, 0.02, 0.3),
    4: (0.02, 0.01, 0.3),
    5: (0.03, -0.02, 0.3),
    6: (0.03, -0.02, -1.5),
}


def compute_velocity(rb, p, w):
    """Compute velocity magnitude at each point (finite differences)."""
    drb = np.gradient(rb)
    dp = np.gradient(p)
    dw = np.gradient(w.astype(float))
    # Normalize time step to 1 (windows are evenly spaced)
    speed = np.sqrt(drb**2 + dp**2)
    return speed, drb, dp


def main():
    traj = pd.read_csv(DATA)
    print(f"Loaded {len(traj)} rows, {traj['class'].nunique()} classes")

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection="3d")

    for cls in sorted(traj["class"].unique()):
        ct = traj[traj["class"] == cls].sort_values("window")
        rb = ct["mean_R_b"].values
        p = ct["mean_P"].values
        w = ct["window"].values

        # Main trajectory line
        ax.plot(rb, p, w,
                color=COLORS[cls], linewidth=2.5, zorder=5,
                label=LABELS[cls])

        # Start marker (circle)
        ax.scatter(rb[0], p[0], w[0],
                   color=COLORS[cls], s=70, marker="o",
                   edgecolors="white", linewidths=0.5, zorder=6)

        # End marker (triangle)
        ax.scatter(rb[-1], p[-1], w[-1],
                   color=COLORS[cls], s=70, marker="^",
                   edgecolors="white", linewidths=0.5, zorder=6)

        # Velocity vectors at windows 3, 5, 7
        speed, drb, dp = compute_velocity(rb, p, w)
        for vi in [2, 4, 6]:  # indices for windows 3, 5, 7
            if vi < len(rb) - 1:
                scale = 3.0  # arrow scale factor
                ax.quiver(rb[vi], p[vi], w[vi],
                          drb[vi] * scale, dp[vi] * scale, 0.8,
                          color=COLORS[cls], alpha=0.6,
                          arrow_length_ratio=0.3, linewidth=1.2)

        # Theory pattern annotation at endpoint
        ox, oy, oz = ANNOT_OFFSETS[cls]
        ax.text(rb[-1] + ox, p[-1] + oy, w[-1] + oz,
                THEORY_ANNOTATIONS[cls],
                color=COLORS[cls], fontsize=7.5, fontweight="bold",
                ha="left", va="center",
                bbox=dict(boxstyle="round,pad=0.2",
                          facecolor="white", edgecolor=COLORS[cls],
                          alpha=0.85, linewidth=0.8))

    # Perfect calibration reference line on the floor
    cal_line = np.linspace(0, 0.40, 50)
    ax.plot(cal_line, cal_line, np.ones_like(cal_line),
            "k--", alpha=0.2, linewidth=1,
            label="$R_b = P$ (perfect calibration)")

    # Under-reliance zone annotation
    ax.text(0.08, 0.62, 1.0, "Under-reliance zone\n($R_b < P$ for all classes)",
            fontsize=8, fontstyle="italic", color="#666666", alpha=0.8,
            ha="center")

    ax.set_xlabel("Behavioral Reliance  $R_b(\\tau)$", labelpad=10)
    ax.set_ylabel("Performance  $P(\\tau)$", labelpad=10)
    ax.set_zlabel("Temporal Window  $\\tau$", labelpad=10)

    ax.set_xlim(0, 0.40)
    ax.set_ylim(0.44, 0.70)
    ax.set_zlim(1, 10)
    ax.view_init(elev=22, azim=-58)

    ax.legend(loc="upper left", framealpha=0.9, fontsize=7.5,
              bbox_to_anchor=(0.0, 0.95))

    fig.suptitle(
        "Empirical Trajectory Classes With Theoretical Pattern Annotations\n"
        "in $R_b \\times P \\times \\tau$ Space  (N = 4,568)",
        fontsize=13, fontweight="bold", y=0.98,
    )

    # Subtitle: velocity arrows explanation
    ax.text2D(0.5, -0.02,
              "Arrows indicate velocity (direction and speed of change) at windows 3, 5, and 7.\n"
              "○ = start (window 1),  △ = end (window 10).  "
              "Annotations show theory–empirical mapping from RQ3.",
              transform=ax.transAxes, fontsize=8, ha="center",
              color="#555555", fontstyle="italic")

    fig.savefig(OUT)
    plt.close(fig)
    print(f"Saved: {OUT}")
    print(f"Size: {OUT.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
