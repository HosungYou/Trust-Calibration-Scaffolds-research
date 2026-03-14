#!/usr/bin/env python3
"""
Generate Figure 4: Phase Portrait of Trajectory Classes in R_b × P Space.

Each class trajectory is plotted as R_b vs P, with temporal progression
shown via color gradient (light→dark) and directional arrows.
The R_b = P diagonal represents perfect calibration.

This 2D phase portrait communicates the core theoretical claim —
convergence toward vs divergence from calibration — far more clearly
than a 3D plot.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_style import *

apply_style()

DATA = DATA_DIR / "phase2_class_trajectories.csv"
OUT_FILENAME = "Figure_4_3D_Theory_vs_Empirical.png"

# Base colors per class (Tol bright palette via figure_style)
BASE_COLORS = MBC_COLORS

LABELS = {
    1: "C1: Gradual Adopter (29.9%)",
    2: "C2: Steady Calibrator (34.6%)",
    3: "C3: Strong Calibrator (18.8%)",
    4: "C4: High Performer (9.9%)",
    5: "C5: Heavy Adopter (5.3%)",
    6: "C6: Early Heavy User (1.5%)",
}

# Theory-empirical mapping labels (from RQ3)
THEORY_LABELS = {
    1: "Gradual Convergence",
    2: "Steady Convergence",
    3: "Strong Convergence",
    4: "Stagnant (High P)",
    5: "Escalating Reliance",
    6: "Self-Correcting\nOver-Reliance",
}

# Annotation positions: (x_offset, y_offset, ha, va)
# Tuned for 7×6 figure size
ANNOT_POS = {
    1: (0.015, 0.012, "left", "bottom"),
    2: (-0.015, -0.015, "right", "top"),
    3: (0.015, -0.015, "left", "top"),
    4: (-0.012, 0.012, "right", "bottom"),
    5: (0.012, -0.012, "left", "top"),
    6: (0.012, 0.012, "left", "bottom"),
}


def lighten_color(color, amount=0.5):
    """Lighten a color by mixing with white."""
    c = mcolors.to_rgb(color)
    return tuple(c_i + (1.0 - c_i) * amount for c_i in c)


def main():
    traj = pd.read_csv(DATA)
    print(f"Loaded {len(traj)} rows, {traj['class'].nunique()} classes")

    fig, ax = plt.subplots(figsize=(7, 6))

    # Perfect calibration line (R_b = P)
    cal_range = np.linspace(0, 0.50, 100)
    ax.plot(cal_range, cal_range, "k--", alpha=0.25, linewidth=1.0,
            label="$R_b = P$ (perfect calibration)", zorder=1)

    # Shade the under-reliance region (R_b < P, above the diagonal)
    ax.fill_between(cal_range, cal_range, 0.75,
                    color="#E3F2FD", alpha=0.3, zorder=0)
    ax.text(0.06, 0.68, "Under-reliance zone\n($R_b < P$)",
            fontsize=9, fontstyle="italic", color="#90A4AE",
            ha="center", va="center")

    for cls in sorted(traj["class"].unique()):
        ct = traj[traj["class"] == cls].sort_values("window")
        rb = ct["mean_R_b"].values
        p_val = ct["mean_P"].values
        windows = ct["window"].values
        n_pts = len(rb)

        base_color = BASE_COLORS[cls]
        light_color = lighten_color(base_color, 0.6)

        # Draw trajectory segments with color gradient (light → dark = early → late)
        for i in range(n_pts - 1):
            frac = i / max(n_pts - 2, 1)
            # Interpolate color: light (early) → base (late)
            seg_color = tuple(
                light_color[j] + (mcolors.to_rgb(base_color)[j] - light_color[j]) * frac
                for j in range(3)
            )
            lw = 1.5 + frac * 1.5  # thicker as time progresses

            ax.plot([rb[i], rb[i+1]], [p_val[i], p_val[i+1]],
                    color=seg_color, linewidth=lw, solid_capstyle="round",
                    zorder=3)

        # Directional arrows at windows 3, 6, 9 (indices 2, 5, 8)
        for ai in [2, 5, 8]:
            if ai < n_pts - 1:
                frac = ai / max(n_pts - 2, 1)
                arrow_color = tuple(
                    light_color[j] + (mcolors.to_rgb(base_color)[j] - light_color[j]) * frac
                    for j in range(3)
                )
                dx = rb[ai+1] - rb[ai]
                dy = p_val[ai+1] - p_val[ai]
                ax.annotate("",
                            xy=(rb[ai] + dx * 0.6, p_val[ai] + dy * 0.6),
                            xytext=(rb[ai], p_val[ai]),
                            arrowprops=dict(
                                arrowstyle="-|>",
                                color=arrow_color,
                                lw=1.8,
                                mutation_scale=12,
                            ),
                            zorder=4)

        # Start marker (window 1): open circle
        ax.scatter(rb[0], p_val[0], s=60, facecolors="white",
                   edgecolors=base_color, linewidths=1.5, zorder=6)

        # End marker (window 10): filled circle with label
        ax.scatter(rb[-1], p_val[-1], s=60, facecolors=base_color,
                   edgecolors="white", linewidths=0.8, zorder=6,
                   label=LABELS[cls])

        # Theory annotation at endpoint
        ox, oy, ha, va = ANNOT_POS[cls]
        ax.annotate(
            THEORY_LABELS[cls],
            xy=(rb[-1], p_val[-1]),
            xytext=(rb[-1] + ox, p_val[-1] + oy),
            fontsize=7.5, fontweight="bold", color=base_color,
            ha=ha, va=va,
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="white", edgecolor=base_color,
                      alpha=0.9, linewidth=0.8),
            arrowprops=dict(arrowstyle="-",
                            color=base_color, alpha=0.4,
                            linewidth=0.6),
            zorder=7,
        )

    # Axis labels and limits
    ax.set_xlabel("Behavioral Reliance  $R_b(\\tau)$")
    ax.set_ylabel("Performance  $P(\\tau)$")
    ax.set_xlim(-0.005, 0.42)
    ax.set_ylim(0.44, 0.72)

    # Grid
    ax.grid(True, alpha=0.15, linewidth=0.5)
    ax.set_axisbelow(True)

    # Legend
    handles, labels = ax.get_legend_handles_labels()
    # Reorder: calibration line first, then classes
    ax.legend(handles, labels,
              loc="lower right", framealpha=0.95, fontsize=8,
              edgecolor="#CCCCCC")

    save_figure(fig, OUT_FILENAME)


if __name__ == "__main__":
    main()
