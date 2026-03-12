"""
Phase 4: 3D Visualization — Theoretical Figure 2 vs Empirical Figure 2'

Creates:
  1. Theoretical Figure 2: Predicted trajectory types in R_b × P × Time space
  2. Empirical Figure 2': Observed 6-class trajectories from mclust GMM
  3. Side-by-side comparison panel
  4. 2D projected views (R_b vs Time, P vs Time, R_b vs P)

Input:
  - phase2_class_trajectories.csv

Output:
  - fig2_theoretical_3d.png
  - fig2_empirical_3d.png
  - fig2_comparison.png
  - fig2_projections.png
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

OUT_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
               "TCR-Trajectory-Paper/analysis/outputs")
FIG_DIR = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/"
               "TCR-Trajectory-Paper/analysis/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Style
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ── Color scheme ──
CLASS_COLORS = {
    1: "#2196F3",  # Blue — Gradual Adopter
    2: "#4CAF50",  # Green — Steady Calibrator
    3: "#FF9800",  # Orange — Strong Calibrator
    4: "#9C27B0",  # Purple — High Performer Low Reliance
    5: "#F44336",  # Red — Heavy Adopter
    6: "#795548",  # Brown — Early Heavy User
}

CLASS_LABELS = {
    1: "C1: Gradual Adopter (29.9%)",
    2: "C2: Steady Calibrator (34.6%)",
    3: "C3: Strong Calibrator (18.8%)",
    4: "C4: High Performer (9.9%)",
    5: "C5: Heavy Adopter (5.3%)",
    6: "C6: Early Heavy User (1.5%)",
}

THEORY_COLORS = {
    "convergent": "#4CAF50",
    "oscillating": "#FF9800",
    "stagnant": "#9C27B0",
    "catastrophic": "#F44336",
}

THEORY_LABELS = {
    "convergent": "Convergent (Gap→0)",
    "oscillating": "Oscillating (damped)",
    "stagnant": "Stagnant (Gap persistent)",
    "catastrophic": "Catastrophic Drop",
}


# ══════════════════════════════════════════════════
# 1. Theoretical Figure 2: Predicted Trajectories
# ══════════════════════════════════════════════════

def generate_theoretical_trajectories():
    """Generate theoretical trajectory predictions from the T×R×τ model."""
    t = np.linspace(0, 1, 50)  # normalized time

    trajectories = {}

    # Convergent: R_b starts low, climbs; P starts mid, climbs; gap closes
    trajectories["convergent"] = {
        "R_b": 0.15 + 0.45 * (1 - np.exp(-3 * t)),
        "P":   0.40 + 0.25 * (1 - np.exp(-2 * t)),
    }

    # Oscillating: R_b oscillates with damping; P oscillates less
    trajectories["oscillating"] = {
        "R_b": 0.40 + 0.20 * np.sin(4 * np.pi * t) * np.exp(-2 * t) + 0.10 * t,
        "P":   0.45 + 0.10 * np.sin(4 * np.pi * t + 0.5) * np.exp(-2.5 * t) + 0.15 * t,
    }

    # Stagnant: both flat, gap persists
    trajectories["stagnant"] = {
        "R_b": 0.20 + 0.03 * t + 0.02 * np.sin(2 * np.pi * t),
        "P":   0.60 - 0.02 * t + 0.01 * np.sin(2 * np.pi * t),
    }

    # Catastrophic drop: R_b high then plummets; P drops then partial recovery
    trajectories["catastrophic"] = {
        "R_b": 0.70 - 0.50 * (1 / (1 + np.exp(-10 * (t - 0.4)))),
        "P":   0.55 - 0.20 * (1 / (1 + np.exp(-10 * (t - 0.4)))) + 0.10 * np.maximum(t - 0.5, 0),
    }

    return t, trajectories


def plot_theoretical_3d():
    """Plot theoretical 3D trajectories."""
    t, trajectories = generate_theoretical_trajectories()

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    for ttype, data in trajectories.items():
        ax.plot(data["R_b"], data["P"], t,
                color=THEORY_COLORS[ttype], linewidth=2.5,
                label=THEORY_LABELS[ttype])
        # Start marker
        ax.scatter(data["R_b"][0], data["P"][0], t[0],
                   color=THEORY_COLORS[ttype], s=60, marker="o", zorder=5)
        # End marker
        ax.scatter(data["R_b"][-1], data["P"][-1], t[-1],
                   color=THEORY_COLORS[ttype], s=60, marker="^", zorder=5)

    # Perfect calibration plane: R_b = P
    rb_grid = np.linspace(0, 0.8, 20)
    t_grid = np.linspace(0, 1, 20)
    RB, T = np.meshgrid(rb_grid, t_grid)
    P_cal = RB  # R_b = P line extended as a plane
    ax.plot_surface(RB, P_cal, T, alpha=0.08, color="gray")

    # y=x line on floor
    cal_line = np.linspace(0, 0.8, 50)
    ax.plot(cal_line, cal_line, np.zeros_like(cal_line),
            "k--", alpha=0.3, linewidth=1)

    ax.set_xlabel("Reliance  R_b(τ)", labelpad=10)
    ax.set_ylabel("Performance  P(τ)", labelpad=10)
    ax.set_zlabel("Time  τ  (normalized)", labelpad=10)
    ax.set_title("Figure 2: Theoretical Trajectory Predictions\nin R_b × P × τ Space", pad=15)
    ax.legend(loc="upper left", framealpha=0.9)

    ax.set_xlim(0, 0.8)
    ax.set_ylim(0.3, 0.75)
    ax.set_zlim(0, 1)
    ax.view_init(elev=20, azim=-60)

    fig.savefig(FIG_DIR / "fig2_theoretical_3d.png")
    plt.close(fig)
    print("Saved: fig2_theoretical_3d.png")


# ══════════════════════════════════════════════════
# 2. Empirical Figure 2': Observed Trajectories
# ══════════════════════════════════════════════════

def plot_empirical_3d(traj_df):
    """Plot empirical 3D trajectories from GMM results."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        rb = ct["mean_R_b"].values
        p = ct["mean_P"].values
        w = ct["window"].values

        ax.plot(rb, p, w,
                color=CLASS_COLORS[cls], linewidth=2.5,
                label=CLASS_LABELS[cls])
        # Start
        ax.scatter(rb[0], p[0], w[0],
                   color=CLASS_COLORS[cls], s=60, marker="o", zorder=5)
        # End
        ax.scatter(rb[-1], p[-1], w[-1],
                   color=CLASS_COLORS[cls], s=60, marker="^", zorder=5)

        # Confidence band (±1 SD) as thin lines
        sd_rb = ct["sd_R_b"].values
        sd_p = ct["sd_P"].values
        ax.plot(rb + sd_rb, p, w, color=CLASS_COLORS[cls], linewidth=0.5, alpha=0.3)
        ax.plot(rb - sd_rb, p, w, color=CLASS_COLORS[cls], linewidth=0.5, alpha=0.3)

    # Perfect calibration plane
    rb_grid = np.linspace(0, 0.4, 20)
    w_grid = np.linspace(1, 10, 20)
    RB, W = np.meshgrid(rb_grid, w_grid)
    P_cal = RB
    ax.plot_surface(RB, P_cal, W, alpha=0.06, color="gray")

    # y=x on floor
    cal_line = np.linspace(0, 0.4, 50)
    ax.plot(cal_line, cal_line, np.ones_like(cal_line),
            "k--", alpha=0.3, linewidth=1)

    ax.set_xlabel("Reliance  R_b(τ)", labelpad=10)
    ax.set_ylabel("Performance  P(τ)", labelpad=10)
    ax.set_zlabel("Window  τ", labelpad=10)
    ax.set_title("Figure 2': Empirical Trajectory Classes\nin R_b × P × τ Space  (N = 4,568)", pad=15)
    ax.legend(loc="upper left", framealpha=0.9, fontsize=8)

    ax.set_xlim(0, 0.40)
    ax.set_ylim(0.45, 0.70)
    ax.set_zlim(1, 10)
    ax.view_init(elev=20, azim=-60)

    fig.savefig(FIG_DIR / "fig2_empirical_3d.png")
    plt.close(fig)
    print("Saved: fig2_empirical_3d.png")


# ══════════════════════════════════════════════════
# 3. Side-by-Side Comparison
# ══════════════════════════════════════════════════

def plot_comparison(traj_df):
    """Side-by-side: theoretical vs empirical."""
    t_theory, trajectories = generate_theoretical_trajectories()

    fig = plt.figure(figsize=(18, 8))

    # ── Left: Theoretical ──
    ax1 = fig.add_subplot(121, projection="3d")
    for ttype, data in trajectories.items():
        ax1.plot(data["R_b"], data["P"], t_theory * 9 + 1,  # scale to 1-10
                 color=THEORY_COLORS[ttype], linewidth=2.5,
                 label=THEORY_LABELS[ttype])
        ax1.scatter(data["R_b"][0], data["P"][0], 1,
                    color=THEORY_COLORS[ttype], s=50, marker="o")
        ax1.scatter(data["R_b"][-1], data["P"][-1], 10,
                    color=THEORY_COLORS[ttype], s=50, marker="^")

    ax1.set_xlabel("R_b(τ)", labelpad=8)
    ax1.set_ylabel("P(τ)", labelpad=8)
    ax1.set_zlabel("Window τ", labelpad=8)
    ax1.set_title("(a) Theoretical Predictions", fontsize=14, pad=10)
    ax1.legend(loc="upper left", framealpha=0.9, fontsize=8)
    ax1.set_xlim(0, 0.8)
    ax1.set_ylim(0.3, 0.75)
    ax1.set_zlim(1, 10)
    ax1.view_init(elev=22, azim=-55)

    # ── Right: Empirical ──
    ax2 = fig.add_subplot(122, projection="3d")
    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        ax2.plot(ct["mean_R_b"].values, ct["mean_P"].values, ct["window"].values,
                 color=CLASS_COLORS[cls], linewidth=2.5,
                 label=CLASS_LABELS[cls])
        ax2.scatter(ct["mean_R_b"].values[0], ct["mean_P"].values[0], ct["window"].values[0],
                    color=CLASS_COLORS[cls], s=50, marker="o")
        ax2.scatter(ct["mean_R_b"].values[-1], ct["mean_P"].values[-1], ct["window"].values[-1],
                    color=CLASS_COLORS[cls], s=50, marker="^")

    ax2.set_xlabel("R_b(τ)", labelpad=8)
    ax2.set_ylabel("P(τ)", labelpad=8)
    ax2.set_zlabel("Window τ", labelpad=8)
    ax2.set_title("(b) Empirical Trajectories (N = 4,568)", fontsize=14, pad=10)
    ax2.legend(loc="upper left", framealpha=0.9, fontsize=7)
    ax2.set_xlim(0, 0.40)
    ax2.set_ylim(0.45, 0.70)
    ax2.set_zlim(1, 10)
    ax2.view_init(elev=22, azim=-55)

    fig.suptitle("Theoretical Predictions vs. Empirical Observations\n"
                 "in Reliance × Performance × Time Space",
                 fontsize=15, fontweight="bold", y=1.02)

    fig.savefig(FIG_DIR / "fig2_comparison.png")
    plt.close(fig)
    print("Saved: fig2_comparison.png")


# ══════════════════════════════════════════════════
# 4. 2D Projected Views (publication-quality panels)
# ══════════════════════════════════════════════════

def plot_projections(traj_df):
    """Four-panel 2D projections for detailed inspection."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # ── (a) R_b vs Time ──
    ax = axes[0, 0]
    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        ax.plot(ct["window"], ct["mean_R_b"],
                color=CLASS_COLORS[cls], linewidth=2, marker="o", markersize=4,
                label=CLASS_LABELS[cls])
        ax.fill_between(ct["window"],
                        ct["mean_R_b"] - ct["sd_R_b"],
                        ct["mean_R_b"] + ct["sd_R_b"],
                        color=CLASS_COLORS[cls], alpha=0.1)
    ax.set_xlabel("Window τ")
    ax.set_ylabel("Reliance  R_b(τ)")
    ax.set_title("(a) Reliance Trajectories")
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlim(1, 10)
    ax.set_ylim(0, 0.50)
    ax.grid(True, alpha=0.3)

    # ── (b) P vs Time ──
    ax = axes[0, 1]
    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        ax.plot(ct["window"], ct["mean_P"],
                color=CLASS_COLORS[cls], linewidth=2, marker="o", markersize=4,
                label=CLASS_LABELS[cls])
        ax.fill_between(ct["window"],
                        ct["mean_P"] - ct["sd_P"],
                        ct["mean_P"] + ct["sd_P"],
                        color=CLASS_COLORS[cls], alpha=0.1)
    ax.set_xlabel("Window τ")
    ax.set_ylabel("Performance  P(τ)")
    ax.set_title("(b) Performance Trajectories")
    ax.legend(fontsize=7, loc="lower left")
    ax.set_xlim(1, 10)
    ax.set_ylim(0.35, 0.75)
    ax.grid(True, alpha=0.3)

    # ── (c) Gap vs Time ──
    ax = axes[1, 0]
    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        ax.plot(ct["window"], ct["mean_gap"],
                color=CLASS_COLORS[cls], linewidth=2, marker="o", markersize=4,
                label=CLASS_LABELS[cls])
    ax.axhline(y=0, color="black", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.set_xlabel("Window τ")
    ax.set_ylabel("Calibration Gap  (R_b − P)")
    ax.set_title("(c) Calibration Gap Trajectories")
    ax.legend(fontsize=7, loc="lower right")
    ax.set_xlim(1, 10)
    ax.grid(True, alpha=0.3)

    # ── (d) R_b vs P (phase plot, time as arrow) ──
    ax = axes[1, 1]
    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        rb = ct["mean_R_b"].values
        p = ct["mean_P"].values

        ax.plot(rb, p,
                color=CLASS_COLORS[cls], linewidth=2,
                label=CLASS_LABELS[cls])
        # Start (circle) and end (triangle)
        ax.scatter(rb[0], p[0], color=CLASS_COLORS[cls], s=80, marker="o",
                   zorder=5, edgecolors="white", linewidths=0.5)
        ax.scatter(rb[-1], p[-1], color=CLASS_COLORS[cls], s=80, marker="^",
                   zorder=5, edgecolors="white", linewidths=0.5)
        # Direction arrows at midpoint
        mid = len(rb) // 2
        dx = rb[mid + 1] - rb[mid]
        dy = p[mid + 1] - p[mid]
        ax.annotate("", xy=(rb[mid + 1], p[mid + 1]),
                     xytext=(rb[mid], p[mid]),
                     arrowprops=dict(arrowstyle="->", color=CLASS_COLORS[cls], lw=1.5))

    # y=x line
    lim_line = np.linspace(0, 0.7, 100)
    ax.plot(lim_line, lim_line, "k--", alpha=0.3, linewidth=1, label="R_b = P (perfect calibration)")

    ax.set_xlabel("Reliance  R_b")
    ax.set_ylabel("Performance  P")
    ax.set_title("(d) Phase Plot: R_b vs P  (○=start, △=end)")
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlim(0, 0.40)
    ax.set_ylim(0.45, 0.70)
    ax.grid(True, alpha=0.3)

    fig.suptitle("Empirical Trajectory Projections by Class (N = 4,568)",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    fig.savefig(FIG_DIR / "fig2_projections.png")
    plt.close(fig)
    print("Saved: fig2_projections.png")


# ══════════════════════════════════════════════════
# 5. Theory-Empirical Mapping Annotation Figure
# ══════════════════════════════════════════════════

def plot_mapping(traj_df):
    """Annotated figure showing theory→empirical class mapping."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # ── Left: Theoretical Gap Trajectories ──
    ax = axes[0]
    t = np.linspace(1, 10, 50)
    t_norm = (t - 1) / 9

    # Convergent
    gap_conv = -0.50 * np.exp(-3 * t_norm) + 0.05
    ax.plot(t, gap_conv, color=THEORY_COLORS["convergent"], linewidth=2.5,
            label="Convergent (Gap→0)")

    # Oscillating
    gap_osc = -0.30 * np.cos(4 * np.pi * t_norm) * np.exp(-2 * t_norm) - 0.15
    ax.plot(t, gap_osc, color=THEORY_COLORS["oscillating"], linewidth=2.5,
            label="Oscillating (damped)")

    # Stagnant
    gap_stag = -0.40 + 0.02 * np.sin(np.pi * t_norm)
    ax.plot(t, gap_stag, color=THEORY_COLORS["stagnant"], linewidth=2.5,
            label="Stagnant (persistent)")

    # Catastrophic
    gap_cat = -0.15 - 0.40 * (1 / (1 + np.exp(-10 * (t_norm - 0.4))))
    ax.plot(t, gap_cat, color=THEORY_COLORS["catastrophic"], linewidth=2.5,
            label="Catastrophic Drop")

    ax.axhline(y=0, color="black", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.set_xlabel("Window τ")
    ax.set_ylabel("Calibration Gap  (R_b − P)")
    ax.set_title("(a) Theoretical: Predicted Gap Dynamics", fontsize=13)
    ax.legend(fontsize=9)
    ax.set_xlim(1, 10)
    ax.set_ylim(-0.65, 0.15)
    ax.grid(True, alpha=0.3)

    # ── Right: Empirical Gap Trajectories ──
    ax = axes[1]
    # Mapping annotations
    mapping_notes = {
        1: "~ Gradual convergence",
        2: "~ Steady convergence",
        3: "~ Strong convergence",
        4: "~ Stagnant (high P)",
        5: "~ High-reliance, slow convergence",
        6: "~ No clear theoretical match",
    }

    for cls in sorted(traj_df["class"].unique()):
        ct = traj_df[traj_df["class"] == cls].sort_values("window")
        ax.plot(ct["window"], ct["mean_gap"],
                color=CLASS_COLORS[cls], linewidth=2.5, marker="o", markersize=3,
                label=CLASS_LABELS[cls])

    ax.axhline(y=0, color="black", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.set_xlabel("Window τ")
    ax.set_ylabel("Calibration Gap  (R_b − P)")
    ax.set_title("(b) Empirical: Observed Gap Dynamics", fontsize=13)
    ax.legend(fontsize=7, loc="lower right")
    ax.set_xlim(1, 10)
    ax.set_ylim(-0.65, 0.15)
    ax.grid(True, alpha=0.3)

    # Add mapping arrows
    ax.annotate("All classes show\nnegative gaps\n(Under-reliance dominant)",
                xy=(5.5, -0.30), fontsize=9, fontstyle="italic",
                ha="center", color="#555555",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8))

    fig.suptitle("Theory vs. Empirical: Calibration Gap Dynamics (Figure 5 Comparison)",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    fig.savefig(FIG_DIR / "fig5_gap_comparison.png")
    plt.close(fig)
    print("Saved: fig5_gap_comparison.png")


# ══════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════

if __name__ == "__main__":
    print("Loading trajectory data...")
    traj = pd.read_csv(OUT_DIR / "phase2_class_trajectories.csv")
    print(f"  {len(traj)} rows, {traj['class'].nunique()} classes")

    print("\n--- Generating figures ---")
    plot_theoretical_3d()
    plot_empirical_3d(traj)
    plot_comparison(traj)
    plot_projections(traj)
    plot_mapping(traj)

    print("\n============ Phase 4 Visualization Complete ============")
    print(f"All figures saved to: {FIG_DIR}")
