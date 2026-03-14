#!/usr/bin/env python3
"""
Generate Figure 7: Outcome Comparison — Accuracy x Improvement Scatter.

Shows the inverse relationship between accuracy level and improvement
across the 6 trajectory classes, revealing the "Calibration-Outcome Paradox."

Target journal: Computers in Human Behavior (CHB)
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# ── Global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
})

BASE = "/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper"
DATA_PATH = os.path.join(BASE, "analysis", "outputs", "phase3_rq4_outcomes.csv")
OUT = Path(os.path.join(BASE, "figures", "Figure_7_Outcome_Scatter.png"))

# Colorblind-friendly palette matching existing figures
COLORS = {
    1: '#4477AA',  # blue
    2: '#228833',  # green
    3: '#EE6677',  # rose/red
    4: '#CCBB44',  # olive/yellow
    5: '#AA3377',  # purple
    6: '#66CCEE',  # cyan
}

MARKERS = {1: 'o', 2: 's', 3: '^', 4: 'D', 5: 'v', 6: 'P'}

CLASS_SHORT_LABELS = {
    1: 'C1: Gradual\nAdopters',
    2: 'C2: Steady\nCalibrators',
    3: 'C3: Strong\nCalibrators',
    4: 'C4: High\nPerformers',
    5: 'C5: Heavy\nAdopters',
    6: 'C6: Early\nHeavy Users',
}

# Annotation offset tuning to avoid overlap
# (x_offset, y_offset, ha, va)
LABEL_OFFSETS = {
    1: (0.012, -0.012, 'left', 'top'),
    2: (-0.012, 0.010, 'right', 'bottom'),
    3: (-0.012, 0.010, 'right', 'bottom'),
    4: (0.012, -0.010, 'left', 'top'),
    5: (0.012, 0.008, 'left', 'bottom'),
    6: (-0.012, -0.008, 'right', 'top'),
}


def main():
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} classes from {DATA_PATH}")
    print(df[['class', 'n', 'overall_acc_mean', 'acc_improve_mean']].to_string(index=False))

    fig, ax = plt.subplots(figsize=(9, 7))

    x = df['overall_acc_mean'].values
    y = df['acc_improve_mean'].values
    n_vals = df['n'].values
    classes = df['class'].values

    # ── Trend line ───────────────────────────────────────────────────────────
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_trend = np.linspace(min(x) - 0.01, max(x) + 0.01, 100)
    y_trend = slope * x_trend + intercept
    ax.plot(x_trend, y_trend, color='#78909C', linestyle='--', linewidth=1.5,
            alpha=0.6, zorder=1,
            label=f'Trend ($r$ = {r_value:.2f})')

    # ── Reference lines ──────────────────────────────────────────────────────
    # Horizontal: zero improvement
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.3,
               zorder=1)
    ax.text(max(x) + 0.008, 0.001, 'No improvement', fontsize=8,
            color='#9E9E9E', fontstyle='italic', va='bottom')

    # Vertical: grand mean accuracy
    grand_mean_acc = np.average(x, weights=n_vals)
    ax.axvline(x=grand_mean_acc, color='#BDBDBD', linestyle=':', linewidth=1.0,
               alpha=0.5, zorder=1)
    ax.text(grand_mean_acc, max(y) + 0.008, f'Grand mean\n({grand_mean_acc:.3f})',
            fontsize=8, color='#9E9E9E', ha='center', va='bottom',
            fontstyle='italic')

    # ── Scatter points (sized by N) ──────────────────────────────────────────
    # Scale sizes: min N=69 -> small, max N=1582 -> large
    size_min, size_max = 150, 800
    n_min, n_max = min(n_vals), max(n_vals)
    sizes = size_min + (n_vals - n_min) / (n_max - n_min) * (size_max - size_min)

    for i, cls in enumerate(classes):
        ax.scatter(x[i], y[i],
                   s=sizes[i], c=COLORS[int(cls)], marker=MARKERS[int(cls)],
                   edgecolors='white', linewidths=1.5, zorder=5,
                   label=f'C{int(cls)} (n={int(n_vals[i]):,})')

    # ── Class labels ─────────────────────────────────────────────────────────
    for i, cls in enumerate(classes):
        ox, oy, ha, va = LABEL_OFFSETS[int(cls)]
        ax.annotate(
            CLASS_SHORT_LABELS[int(cls)],
            xy=(x[i], y[i]),
            xytext=(x[i] + ox, y[i] + oy),
            fontsize=8.5, fontweight='bold', color=COLORS[int(cls)],
            ha=ha, va=va,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=COLORS[int(cls)], alpha=0.85, linewidth=0.7),
            arrowprops=dict(arrowstyle='-', color=COLORS[int(cls)],
                            alpha=0.4, linewidth=0.5),
            zorder=6,
        )

    # ── Quadrant annotations ────────────────────────────────────────────────
    # Upper-left quadrant: Low accuracy, high improvement
    ax.text(0.535, 0.052, 'Low accuracy,\nhigh growth',
            fontsize=9, color='#4CAF50', fontstyle='italic',
            ha='center', va='center', alpha=0.7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9',
                      edgecolor='#A5D6A7', alpha=0.5))

    # Lower-right quadrant: High accuracy, low improvement
    ax.text(0.645, -0.012, 'High accuracy,\nlow growth',
            fontsize=9, color='#F57C00', fontstyle='italic',
            ha='center', va='center', alpha=0.7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0',
                      edgecolor='#FFCC80', alpha=0.5))

    # ── Key insight annotation box ───────────────────────────────────────────
    insight_text = ('Key insight: Strongest calibrators (C3) improve\n'
                    'most but start at lowest accuracy. Highest\n'
                    'performers (C4) show minimal improvement.')
    ax.text(0.03, 0.03, insight_text,
            transform=ax.transAxes, fontsize=9.5,
            va='bottom', ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E1',
                      edgecolor='#FFD54F', alpha=0.95, linewidth=1))

    # ── Axis formatting ─────────────────────────────────────────────────────
    ax.set_xlabel('Overall Accuracy (mean per class)', fontsize=13)
    ax.set_ylabel('Accuracy Improvement ($\\Delta$ accuracy, W1 to W10)', fontsize=13)
    ax.yaxis.grid(True, color='gray', alpha=0.2, linewidth=0.5)
    ax.xaxis.grid(True, color='gray', alpha=0.2, linewidth=0.5)
    ax.set_axisbelow(True)

    # Extend limits slightly for annotations
    x_margin = (max(x) - min(x)) * 0.15
    y_margin = (max(y) - min(y)) * 0.2
    ax.set_xlim(min(x) - x_margin, max(x) + x_margin * 1.5)
    ax.set_ylim(min(y) - y_margin, max(y) + y_margin)

    # Legend — size guide
    # Create custom legend with point sizes
    legend = ax.legend(loc='upper right', frameon=True, edgecolor='lightgray',
                       fancybox=False, fontsize=9, ncol=2,
                       title='Class (point size $\\propto$ N)',
                       title_fontsize=9)

    # ── Titles ───────────────────────────────────────────────────────────────
    fig.suptitle(
        'The Calibration-Outcome Paradox',
        fontsize=15, fontweight='bold', y=0.98,
    )
    fig.text(0.5, 0.93,
             'Convergent calibrators grow most, but start lowest',
             fontsize=11.5, ha='center', color='#555555', fontstyle='italic')

    fig.tight_layout(rect=[0, 0, 1, 0.91])
    fig.savefig(OUT, facecolor='white')
    plt.close(fig)
    print(f"Saved: {OUT}")
    print(f"Size: {OUT.stat().st_size / 1024:.0f} KB")


if __name__ == '__main__':
    main()
