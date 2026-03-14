#!/usr/bin/env python3
"""
Generate Figure 6: Early Prediction Feature Importance.

Horizontal bar chart showing which early behavioral features best predict
trajectory class membership. Metacognitive features (explanation rate and
duration) are highlighted to support the theoretical narrative.

Target journal: Computers in Human Behavior (CHB)
"""

import os
import numpy as np
import pandas as pd
from pathlib import Path

# ── Shared style framework ────────────────────────────────────────────────────
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_style import *

apply_style()

# ── Paths ─────────────────────────────────────────────────────────────────────
DATA_PATH = DATA_DIR / "phase3_rq3_prediction.csv"
OUT_FILENAME = "Figure_6_Early_Prediction.png"

# ── Feature display names ────────────────────────────────────────────────────
FEATURE_NAMES = {
    'early_expl_rate': 'Explanation Request Rate',
    'early_avg_expl_dur_s': 'Avg. Explanation Duration (s)',
    'early_R_b': 'Initial Behavioral Reliance ($R_b$)',
    'early_gap': 'Initial Calibration Gap',
    'early_P': 'Initial Performance ($P$)',
    'early_answer_change_rate': 'Answer Change Rate',
    'early_lecture_rate': 'Lecture Viewing Rate',
}

# Features that are metacognitive
METACOG_FEATURES = {'early_expl_rate', 'early_avg_expl_dur_s'}


def main():
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} features from {DATA_PATH}")
    print(df.to_string(index=False))

    # Sort by importance (ascending for horizontal barh — top bar = highest)
    df = df.sort_values('mean_abs_coef', ascending=True).reset_index(drop=True)

    # Map feature names
    display_names = [FEATURE_NAMES.get(f, f) for f in df['feature']]

    # Color: metacognitive features highlighted, others gray
    colors = [
        PRED_COLOR_HIGHLIGHT if f in METACOG_FEATURES else PRED_COLOR_DEFAULT
        for f in df['feature']
    ]

    # Edge colors for emphasis
    edge_colors = [
        PRED_EDGE_HIGHLIGHT if f in METACOG_FEATURES else PRED_EDGE_DEFAULT
        for f in df['feature']
    ]

    fig, ax = plt.subplots(figsize=(7, 5))

    bars = ax.barh(range(len(df)), df['mean_abs_coef'], height=0.65,
                   color=colors, edgecolor=edge_colors, linewidth=0.8,
                   zorder=3)

    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(display_names, fontsize=TICK_LABEL_SIZE)
    ax.set_xlabel('Mean |Coefficient| (Multinomial Logistic Regression)',
                  fontsize=AXIS_LABEL_SIZE)
    ax.set_xlim(0, max(df['mean_abs_coef']) * 1.25)

    # Gridlines
    add_x_gridlines(ax)

    # Value labels on bars
    for i, (val, feat) in enumerate(zip(df['mean_abs_coef'], df['feature'])):
        ax.text(val + 0.015, i, f'{val:.3f}', va='center',
                fontsize=ANNOTATION_SIZE + 0.5,
                fontweight='bold' if feat in METACOG_FEATURES else 'normal',
                color=PRED_COLOR_HIGHLIGHT if feat in METACOG_FEATURES
                else '#546E7A')

    # ── Metacognitive bracket annotation ─────────────────────────────────────
    # The top two bars (highest importance) are metacognitive features
    # They are at positions len(df)-1 and len(df)-2 after sorting ascending
    top_idx = len(df) - 1
    second_idx = len(df) - 2

    # Draw bracket on the right side
    bracket_x = max(df['mean_abs_coef']) * 1.12
    bracket_y_top = top_idx + 0.3
    bracket_y_bot = second_idx - 0.3
    bracket_y_mid = (top_idx + second_idx) / 2

    # Vertical line of bracket
    ax.plot([bracket_x, bracket_x], [bracket_y_bot, bracket_y_top],
            color=PRED_COLOR_HIGHLIGHT, linewidth=1.5, clip_on=False)
    # Top cap
    ax.plot([bracket_x - 0.015, bracket_x], [bracket_y_top, bracket_y_top],
            color=PRED_COLOR_HIGHLIGHT, linewidth=1.5, clip_on=False)
    # Bottom cap
    ax.plot([bracket_x - 0.015, bracket_x], [bracket_y_bot, bracket_y_bot],
            color=PRED_COLOR_HIGHLIGHT, linewidth=1.5, clip_on=False)

    ax.text(bracket_x + 0.02, bracket_y_mid,
            'Metacognitive\nEngagement',
            fontsize=LEGEND_FONT_SIZE + 0.5, fontweight='bold',
            color=PRED_COLOR_HIGHLIGHT,
            ha='left', va='center', clip_on=False)

    # ── Model accuracy box ───────────────────────────────────────────────────
    acc_text = ('Model: Multinomial Logistic Regression\n'
                'Accuracy: 49.4% (chance = 16.7%)\n'
                'Performance: $3\\times$ chance level')
    ax.text(0.55, 0.15, acc_text,
            transform=ax.transAxes, fontsize=ANNOTATION_SIZE + 0.5,
            va='bottom', ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#E3F2FD',
                      edgecolor='#90CAF9', alpha=0.95, linewidth=1))

    # ── Vertical reference line at mean importance ───────────────────────────
    mean_imp = df['mean_abs_coef'].mean()
    ax.axvline(x=mean_imp, color=PRED_EDGE_DEFAULT, linestyle='--',
               linewidth=1.0, alpha=REFERENCE_LINE_ALPHA, zorder=2)
    ax.text(mean_imp, -0.7, f'Mean = {mean_imp:.3f}', fontsize=8,
            ha='center', color=PRED_EDGE_DEFAULT, fontstyle='italic')

    fig.tight_layout()
    save_figure(fig, OUT_FILENAME)


if __name__ == '__main__':
    main()
