"""
Paper 4: Trust Calibration Trajectories — Analysis Plan Visualizations
Generates 6 figures explaining the full analysis pipeline.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'figure.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.3,
})

COLORS = {
    'blue': '#2563EB',
    'green': '#059669',
    'orange': '#D97706',
    'red': '#DC2626',
    'purple': '#7C3AED',
    'gray': '#6B7280',
    'light_blue': '#DBEAFE',
    'light_green': '#D1FAE5',
    'light_orange': '#FEF3C7',
    'light_red': '#FEE2E2',
    'light_purple': '#EDE9FE',
    'light_gray': '#F3F4F6',
    'bg': '#FAFAFA',
}


# ============================================================
# Figure A: Overall Analysis Pipeline
# ============================================================
def fig_a_pipeline():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Title
    ax.text(8, 9.5, 'Analysis Pipeline Overview', fontsize=16, fontweight='bold',
            ha='center', va='center')
    ax.text(8, 9.1, 'Python (Data Wrangling + Visualization) → R (Growth Mixture Modeling) → Python (Interpretation)',
            fontsize=9, ha='center', va='center', color=COLORS['gray'])

    # Phase boxes
    phases = [
        {
            'x': 0.5, 'y': 6.5, 'w': 4.5, 'h': 2.2,
            'color': COLORS['light_blue'], 'border': COLORS['blue'],
            'title': 'Phase 1: Data Wrangling',
            'subtitle': 'Python (pandas)',
            'items': [
                '297,915 raw CSV files',
                '→ Filter: 100+ episodes (~68K students)',
                '→ Parse episodes from action logs',
                '→ Compute Trust Proxy variables',
                '→ Time-normalize to ventiles (20 bins)',
            ]
        },
        {
            'x': 5.8, 'y': 6.5, 'w': 4.5, 'h': 2.2,
            'color': COLORS['light_green'], 'border': COLORS['green'],
            'title': 'Phase 2: Trajectory Classification',
            'subtitle': 'R (mclust / tidyLPA / lcmm)',
            'items': [
                'Input: student × ventile matrix',
                '→ Fit GMM: 1-class to 6-class',
                '→ Compare: BIC, AIC, Entropy, BLRT',
                '→ Select optimal class number',
                '→ Assign students to trajectory types',
            ]
        },
        {
            'x': 11.2, 'y': 6.5, 'w': 4.3, 'h': 2.2,
            'color': COLORS['light_orange'], 'border': COLORS['orange'],
            'title': 'Phase 3: Validation & Outcomes',
            'subtitle': 'Python + R',
            'items': [
                'Multinomial logistic regression',
                '→ Predictors of trajectory type',
                'Learning outcome comparison',
                '→ Accuracy gain by trajectory type',
                'Cross-validation with Tier 1 data',
            ]
        },
    ]

    for p in phases:
        rect = FancyBboxPatch((p['x'], p['y']), p['w'], p['h'],
                               boxstyle="round,pad=0.1", facecolor=p['color'],
                               edgecolor=p['border'], linewidth=2)
        ax.add_patch(rect)
        ax.text(p['x'] + p['w']/2, p['y'] + p['h'] - 0.25, p['title'],
                fontsize=11, fontweight='bold', ha='center', va='center', color=p['border'])
        ax.text(p['x'] + p['w']/2, p['y'] + p['h'] - 0.55, p['subtitle'],
                fontsize=8, ha='center', va='center', color=COLORS['gray'], style='italic')
        for i, item in enumerate(p['items']):
            ax.text(p['x'] + 0.3, p['y'] + p['h'] - 0.9 - i * 0.28, item,
                    fontsize=8, ha='left', va='center',
                    color='#1F2937' if item.startswith('→') else '#374151',
                    fontweight='normal' if item.startswith('→') else 'bold')

    # Arrows between phases
    ax.annotate('', xy=(5.6, 7.6), xytext=(5.1, 7.6),
                arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))
    ax.annotate('', xy=(11.0, 7.6), xytext=(10.5, 7.6),
                arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))

    # Data flow boxes at bottom
    data_boxes = [
        {'x': 1.0, 'y': 4.0, 'label': 'EdNet KT3\n297,915 CSVs\n4.2 GB', 'color': COLORS['blue']},
        {'x': 3.5, 'y': 4.0, 'label': 'Filtered\n~68,000 students\n100+ episodes', 'color': COLORS['blue']},
        {'x': 6.5, 'y': 4.0, 'label': 'Trust Proxy\nMatrix\n68K × 20 ventiles', 'color': COLORS['blue']},
        {'x': 9.5, 'y': 4.0, 'label': 'GMM Results\nK classes\nBIC/Entropy', 'color': COLORS['green']},
        {'x': 12.5, 'y': 4.0, 'label': 'Trajectory\nAssignments\n+ Predictors', 'color': COLORS['orange']},
    ]

    for b in data_boxes:
        rect = FancyBboxPatch((b['x'] - 0.9, b['y'] - 0.5), 1.8, 1.0,
                               boxstyle="round,pad=0.08", facecolor='white',
                               edgecolor=b['color'], linewidth=1.5, linestyle='--')
        ax.add_patch(rect)
        ax.text(b['x'], b['y'], b['label'], fontsize=7.5, ha='center', va='center',
                color=b['color'])

    for i in range(len(data_boxes) - 1):
        ax.annotate('', xy=(data_boxes[i+1]['x'] - 1.0, data_boxes[i+1]['y']),
                    xytext=(data_boxes[i]['x'] + 1.0, data_boxes[i]['y']),
                    arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=1.5))

    # Bottom section: Expected outputs
    ax.text(8, 2.8, 'Expected Outputs for Computers & Education', fontsize=12, fontweight='bold',
            ha='center', va='center')

    outputs = [
        ('RQ1: Trajectory\nType Count', '3-5 distinct types\n(BIC-optimal)'),
        ('RQ2: Theory\nValidation', 'Convergent / Oscillating\n/ Stagnant confirmed?'),
        ('RQ3: Predictors', 'Early behavior →\ntrajectory type'),
        ('RQ4: Learning\nOutcomes', 'Convergent > Oscillating\n> Stagnant?'),
    ]

    for i, (title, desc) in enumerate(outputs):
        x = 2.0 + i * 3.5
        rect = FancyBboxPatch((x - 1.3, 1.2), 2.6, 1.3,
                               boxstyle="round,pad=0.08", facecolor=COLORS['light_purple'],
                               edgecolor=COLORS['purple'], linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 2.2, title, fontsize=8.5, fontweight='bold', ha='center', va='center',
                color=COLORS['purple'])
        ax.text(x, 1.6, desc, fontsize=7.5, ha='center', va='center', color='#4B5563')

    fig.savefig(OUT / 'Analysis_A_Pipeline_Overview.png')
    plt.close()
    print('✓ Figure A: Pipeline Overview')


# ============================================================
# Figure B: Trust Proxy Variable Construction
# ============================================================
def fig_b_trust_proxy():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('Trust Proxy Variable Construction from EdNet KT3 Raw Logs',
                 fontsize=14, fontweight='bold', y=1.02)

    # Panel 1: Raw action log → Episode parsing
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Step 1: Episode Parsing', fontsize=11, fontweight='bold', color=COLORS['blue'])

    # Raw log representation
    log_entries = [
        ('enter', 'b790', 'sprint', '', COLORS['light_blue']),
        ('respond', 'q790', 'sprint', 'b→d', COLORS['light_green']),
        ('submit', 'b790', 'sprint', '', COLORS['light_blue']),
        ('enter', 'e790', 'sprint', '', COLORS['light_orange']),
        ('quit', 'e790', 'sprint', '', COLORS['light_orange']),
        ('enter', 'l540', 'adaptive', '', COLORS['light_purple']),
        ('quit', 'l540', 'adaptive', '', COLORS['light_purple']),
        ('enter', 'b6191', 'adaptive', '', COLORS['light_red']),
        ('respond', 'q8840', 'adaptive', 'c', COLORS['light_red']),
        ('submit', 'b6191', 'adaptive', '', COLORS['light_red']),
    ]

    for i, (action, item, source, answer, color) in enumerate(log_entries):
        y = 9.0 - i * 0.75
        rect = FancyBboxPatch((0.3, y - 0.25), 9.2, 0.55,
                               boxstyle="round,pad=0.05", facecolor=color,
                               edgecolor='#D1D5DB', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(1.0, y, action, fontsize=7, fontweight='bold', ha='left', va='center')
        ax.text(3.2, y, item, fontsize=7, ha='left', va='center', family='monospace')
        ax.text(5.5, y, source, fontsize=7, ha='left', va='center', color=COLORS['gray'])
        if answer:
            ax.text(8.0, y, answer, fontsize=7, ha='left', va='center', color=COLORS['red'])

    # Brackets for episodes
    ax.annotate('', xy=(9.7, 8.75), xytext=(9.7, 6.50),
                arrowprops=dict(arrowstyle='-', color=COLORS['blue'], lw=2))
    ax.text(9.9, 7.6, 'Episode 1\n(sprint)', fontsize=7, fontweight='bold',
            color=COLORS['blue'], rotation=0, ha='left', va='center')

    ax.annotate('', xy=(9.7, 6.25), xytext=(9.7, 1.75),
                arrowprops=dict(arrowstyle='-', color=COLORS['red'], lw=2))
    ax.text(9.9, 4.0, 'Episode 2\n(adaptive\n_offer)', fontsize=7, fontweight='bold',
            color=COLORS['red'], rotation=0, ha='left', va='center')

    # Panel 2: Episode → Trust Proxy Variables
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Step 2: Variable Extraction', fontsize=11, fontweight='bold', color=COLORS['green'])

    variables = [
        {
            'name': 'AI Reliance (T)',
            'formula': 'adaptive_offer episodes\n÷ total episodes\n(rolling window = 20)',
            'color': COLORS['blue'],
            'y': 8.5,
            'mapping': 'Trust → T dimension'
        },
        {
            'name': 'Explanation Depth',
            'formula': 'explanation dwell time\n÷ problem solving time\n(normalized ratio)',
            'color': COLORS['green'],
            'y': 6.5,
            'mapping': 'Engagement depth'
        },
        {
            'name': 'System Accuracy (R)',
            'formula': 'correct responses\n÷ total responses\n(rolling window = 20)',
            'color': COLORS['orange'],
            'y': 4.5,
            'mapping': 'Reliability → R dimension'
        },
        {
            'name': 'Calibration Gap',
            'formula': '|AI_Reliance − Sys_Accuracy|\nSmall gap = well-calibrated\nLarge gap = miscalibrated',
            'color': COLORS['red'],
            'y': 2.5,
            'mapping': 'KEY OUTCOME VARIABLE'
        },
    ]

    for v in variables:
        rect = FancyBboxPatch((0.3, v['y'] - 0.7), 5.5, 1.4,
                               boxstyle="round,pad=0.08", facecolor='white',
                               edgecolor=v['color'], linewidth=2)
        ax.add_patch(rect)
        ax.text(0.6, v['y'] + 0.35, v['name'], fontsize=9, fontweight='bold',
                color=v['color'], ha='left', va='center')
        ax.text(0.6, v['y'] - 0.25, v['formula'], fontsize=7, ha='left', va='center',
                color='#4B5563', linespacing=1.3)

        # Mapping tag
        tag = FancyBboxPatch((6.2, v['y'] - 0.25), 3.3, 0.5,
                              boxstyle="round,pad=0.05", facecolor=v['color'],
                              edgecolor=v['color'], linewidth=1, alpha=0.15)
        ax.add_patch(tag)
        ax.text(7.85, v['y'], v['mapping'], fontsize=7.5, fontweight='bold',
                ha='center', va='center', color=v['color'])

    # Panel 3: Time normalization
    ax = axes[2]
    ax.set_title('Step 3: Time Normalization', fontsize=11, fontweight='bold', color=COLORS['orange'])

    # Show variable-length → fixed ventile
    np.random.seed(42)

    # Student A: 400 episodes
    x_a = np.linspace(0, 1, 20)
    y_a = 0.5 + 0.3 * np.exp(-3 * x_a) * np.sin(8 * x_a) + 0.02 * np.random.randn(20)

    # Student B: 100 episodes
    x_b = np.linspace(0, 1, 20)
    y_b = 0.7 - 0.25 * x_b + 0.02 * np.random.randn(20)

    # Student C: 200 episodes
    x_c = np.linspace(0, 1, 20)
    y_c = 0.4 + 0.1 * np.sin(4 * x_c) + 0.02 * np.random.randn(20)

    ax.plot(x_a, y_a, 'o-', color=COLORS['blue'], label='Student A (400 ep)', markersize=4, lw=1.5)
    ax.plot(x_b, y_b, 's-', color=COLORS['red'], label='Student B (100 ep)', markersize=4, lw=1.5)
    ax.plot(x_c, y_c, '^-', color=COLORS['green'], label='Student C (200 ep)', markersize=4, lw=1.5)

    ax.set_xlabel('Normalized Time (ventile: 0%–100%)', fontsize=9)
    ax.set_ylabel('Calibration Gap', fontsize=9)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
    ax.legend(fontsize=8, loc='upper right')
    ax.set_ylim(0, 1)
    ax.grid(alpha=0.3)

    # Annotation
    ax.text(0.5, -0.18, 'All students mapped to 20 ventiles\nregardless of actual episode count',
            fontsize=8, ha='center', va='center', transform=ax.transAxes,
            color=COLORS['gray'], style='italic')

    plt.tight_layout()
    fig.savefig(OUT / 'Analysis_B_Trust_Proxy_Construction.png')
    plt.close()
    print('✓ Figure B: Trust Proxy Construction')


# ============================================================
# Figure C: Expected Trajectory Patterns
# ============================================================
def fig_c_expected_trajectories():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))
    fig.suptitle('Theoretically Predicted Trajectory Types (T × R × τ Model)',
                 fontsize=13, fontweight='bold', y=1.05)

    np.random.seed(42)
    t = np.linspace(0, 1, 20)

    patterns = [
        {
            'title': 'Type 1: Convergent',
            'subtitle': '"Bayesian Decision Maker"\n(Guo & Yang, 2021)',
            'color': COLORS['green'],
            'gap': 0.6 * np.exp(-4 * t) + 0.05,
            'trust': 0.3 + 0.35 * (1 - np.exp(-3 * t)),
            'reliability': 0.65 * np.ones_like(t),
            'description': 'Gap shrinks monotonically\n→ Trust converges to reliability'
        },
        {
            'title': 'Type 2: Oscillating',
            'subtitle': '"Oscillator"\n(Guo & Yang, 2021)',
            'color': COLORS['orange'],
            'gap': 0.4 * np.exp(-2 * t) * np.abs(np.sin(6 * t)) + 0.08,
            'trust': 0.5 + 0.25 * np.exp(-2 * t) * np.sin(6 * t),
            'reliability': 0.5 * np.ones_like(t),
            'description': 'Damped oscillation\n→ Eventual convergence (slow)'
        },
        {
            'title': 'Type 3: Stagnant',
            'subtitle': '"Disbeliever"\n(Guo & Yang, 2021)',
            'color': COLORS['red'],
            'gap': 0.45 + 0.05 * np.sin(2 * t) + 0.02 * np.random.randn(20),
            'trust': 0.2 + 0.03 * np.random.randn(20),
            'reliability': 0.65 * np.ones_like(t),
            'description': 'Gap persists\n→ Trust never matches reliability'
        },
        {
            'title': 'Type 4: Catastrophic',
            'subtitle': '(Possible additional type)',
            'color': COLORS['purple'],
            'gap': np.concatenate([0.1 * np.ones(12), 0.1 + 0.5 * (t[12:] - t[12])/(t[-1] - t[12])]),
            'trust': np.concatenate([0.6 * np.ones(12), 0.6 - 0.45 * (t[12:] - t[12])/(t[-1] - t[12])]),
            'reliability': np.concatenate([0.6 * np.ones(12), 0.6 - 0.3 * (t[12:] - t[12])/(t[-1] - t[12])]),
            'description': 'Sudden trust collapse\n→ Triggered by negative event'
        },
    ]

    for ax, p in zip(axes, patterns):
        # Plot calibration gap
        ax.fill_between(t, 0, p['gap'], alpha=0.15, color=p['color'])
        ax.plot(t, p['gap'], '-', color=p['color'], lw=2.5, label='Calibration Gap')

        # Reference line
        ax.axhline(y=0.1, color=COLORS['gray'], ls='--', lw=0.8, alpha=0.5)

        ax.set_title(p['title'], fontsize=10, fontweight='bold', color=p['color'])
        ax.text(0.5, 1.08, p['subtitle'], fontsize=7.5, ha='center', va='center',
                transform=ax.transAxes, color=COLORS['gray'], style='italic')
        ax.text(0.5, -0.22, p['description'], fontsize=7.5, ha='center', va='center',
                transform=ax.transAxes, color='#4B5563')

        ax.set_xlabel('Time (ventile)', fontsize=8)
        if ax == axes[0]:
            ax.set_ylabel('|Trust − Reliability|', fontsize=8)
        ax.set_ylim(0, 0.8)
        ax.set_xticks([0, 0.5, 1.0])
        ax.set_xticklabels(['Early', 'Mid', 'Late'], fontsize=7)
        ax.grid(alpha=0.2)

    plt.tight_layout()
    fig.savefig(OUT / 'Analysis_C_Expected_Trajectory_Patterns.png')
    plt.close()
    print('✓ Figure C: Expected Trajectory Patterns')


# ============================================================
# Figure D: GMM Model Selection Process
# ============================================================
def fig_d_gmm_selection():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Growth Mixture Model Selection Strategy',
                 fontsize=13, fontweight='bold', y=1.02)

    # Panel 1: BIC comparison (simulated)
    ax = axes[0]
    k_values = [1, 2, 3, 4, 5, 6]
    bic_values = [125000, 98000, 87000, 86500, 87200, 88000]
    aic_values = [124000, 96000, 85000, 84000, 85500, 87000]

    ax.plot(k_values, bic_values, 'o-', color=COLORS['blue'], lw=2, markersize=8, label='BIC')
    ax.plot(k_values, aic_values, 's--', color=COLORS['orange'], lw=2, markersize=8, label='AIC')

    # Highlight optimal
    ax.axvline(x=3, color=COLORS['green'], ls=':', lw=2, alpha=0.5)
    ax.annotate('Optimal\n(K=3)', xy=(3, 87000), xytext=(4.2, 95000),
                fontsize=9, fontweight='bold', color=COLORS['green'],
                arrowprops=dict(arrowstyle='->', color=COLORS['green'], lw=1.5))

    ax.set_xlabel('Number of Classes (K)', fontsize=10)
    ax.set_ylabel('Information Criterion', fontsize=10)
    ax.set_title('Step 1: Information Criteria', fontsize=11, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: Entropy
    ax = axes[1]
    entropy = [1.0, 0.82, 0.88, 0.79, 0.72, 0.65]
    bars = ax.bar(k_values, entropy, color=[COLORS['gray']]*6, edgecolor='white', lw=1.5)
    bars[2].set_color(COLORS['green'])
    bars[2].set_alpha(1.0)
    for b in bars:
        if b != bars[2]:
            b.set_alpha(0.4)

    ax.axhline(y=0.8, color=COLORS['red'], ls='--', lw=1.5, alpha=0.7)
    ax.text(6.3, 0.81, 'Threshold\n(0.80)', fontsize=8, color=COLORS['red'], va='bottom')

    ax.annotate('K=3: 0.88\n(Good separation)', xy=(3, 0.88), xytext=(4.5, 0.93),
                fontsize=9, fontweight='bold', color=COLORS['green'],
                arrowprops=dict(arrowstyle='->', color=COLORS['green'], lw=1.5))

    ax.set_xlabel('Number of Classes (K)', fontsize=10)
    ax.set_ylabel('Entropy', fontsize=10)
    ax.set_title('Step 2: Classification Quality', fontsize=11, fontweight='bold')
    ax.set_ylim(0.5, 1.05)
    ax.grid(alpha=0.3)

    # Panel 3: BLRT + class proportions
    ax = axes[2]
    ax.axis('off')
    ax.set_title('Step 3: Final Model Validation', fontsize=11, fontweight='bold')

    # Decision tree
    criteria = [
        ('BIC', 'K=3 minimal', '✅', 0.9),
        ('AIC', 'K=3 or 4', '✅', 0.75),
        ('Entropy', '0.88 > 0.80', '✅', 0.6),
        ('BLRT', 'K=3 vs K=2 sig.', '✅', 0.45),
        ('Class size', 'All > 5% of N', '✅', 0.3),
        ('Interpretability', 'Matches theory', '✅', 0.15),
    ]

    for label, desc, check, y in criteria:
        rect = FancyBboxPatch((0.05, y - 0.04), 0.9, 0.11,
                               boxstyle="round,pad=0.02", facecolor=COLORS['light_green'],
                               edgecolor=COLORS['green'], linewidth=1, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(0.08, y + 0.015, f'{check} {label}:', fontsize=9, fontweight='bold',
                transform=ax.transAxes, va='center', color=COLORS['green'])
        ax.text(0.42, y + 0.015, desc, fontsize=9, transform=ax.transAxes,
                va='center', color='#374151')

    # Final verdict box
    verdict = FancyBboxPatch((0.1, -0.02), 0.8, 0.12,
                              boxstyle="round,pad=0.03", facecolor=COLORS['green'],
                              edgecolor=COLORS['green'], linewidth=2, transform=ax.transAxes,
                              alpha=0.15)
    ax.add_patch(verdict)
    ax.text(0.5, 0.04, '→ Accept K=3 model (or data-driven K)', fontsize=10,
            fontweight='bold', ha='center', va='center', transform=ax.transAxes,
            color=COLORS['green'])

    plt.tight_layout()
    fig.savefig(OUT / 'Analysis_D_GMM_Model_Selection.png')
    plt.close()
    print('✓ Figure D: GMM Model Selection')


# ============================================================
# Figure E: Cross-Validation Strategy
# ============================================================
def fig_e_cross_validation():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 6.6, 'Cross-Validation Strategy: EdNet → Tier 1 Experiments',
            fontsize=14, fontweight='bold', ha='center')

    # Main dataset (EdNet)
    rect = FancyBboxPatch((0.5, 3.8), 4.0, 2.2,
                           boxstyle="round,pad=0.1", facecolor=COLORS['light_blue'],
                           edgecolor=COLORS['blue'], linewidth=2.5)
    ax.add_patch(rect)
    ax.text(2.5, 5.6, 'PRIMARY', fontsize=9, fontweight='bold', ha='center', color=COLORS['blue'])
    ax.text(2.5, 5.2, 'EdNet KT3', fontsize=12, fontweight='bold', ha='center', color=COLORS['blue'])
    ax.text(2.5, 4.7, 'N = ~68,000 students', fontsize=9, ha='center', color='#374151')
    ax.text(2.5, 4.35, '100+ episodes each', fontsize=9, ha='center', color='#374151')
    ax.text(2.5, 4.0, 'Behavioral trust proxy', fontsize=9, ha='center', color='#6B7280')

    # Arrow to center
    ax.annotate('', xy=(5.5, 4.9), xytext=(4.7, 4.9),
                arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))

    # Center: Pattern matching
    rect = FancyBboxPatch((5.5, 3.5), 3.0, 2.8,
                           boxstyle="round,pad=0.1", facecolor=COLORS['light_purple'],
                           edgecolor=COLORS['purple'], linewidth=2.5)
    ax.add_patch(rect)
    ax.text(7.0, 5.9, 'Pattern Matching', fontsize=11, fontweight='bold',
            ha='center', color=COLORS['purple'])
    ax.text(7.0, 5.3, 'Do the same K\ntrajectory types\nemerge across\nall datasets?', fontsize=9,
            ha='center', color='#374151', linespacing=1.4)
    ax.text(7.0, 3.8, 'Convergent?\nOscillating?\nStagnant?', fontsize=9,
            ha='center', color=COLORS['purple'], fontweight='bold', linespacing=1.3)

    # Tier 1 datasets
    tier1 = [
        {'name': 'Rittenberg\n(2024)', 'n': 'N=147', 'detail': '30 trust pts\nVAS 0–100',
         'y': 5.3, 'color': COLORS['green']},
        {'name': 'Zouhar\n(2023)', 'n': 'N=332', 'detail': '56 trials\nBetting task',
         'y': 3.5, 'color': COLORS['orange']},
        {'name': 'Lu & Yin\n(2021)', 'n': 'N=~300', 'detail': 'Self-report\n+ behavioral',
         'y': 1.7, 'color': COLORS['red']},
    ]

    for t1 in tier1:
        rect = FancyBboxPatch((9.5, t1['y'] - 0.6), 4.0, 1.2,
                               boxstyle="round,pad=0.08", facecolor='white',
                               edgecolor=t1['color'], linewidth=1.5)
        ax.add_patch(rect)
        ax.text(10.0, t1['y'] + 0.2, t1['name'], fontsize=9, fontweight='bold',
                ha='left', color=t1['color'])
        ax.text(11.5, t1['y'] + 0.2, t1['n'], fontsize=9, ha='left', color='#374151')
        ax.text(12.3, t1['y'] + 0.2, t1['detail'], fontsize=7.5, ha='left',
                color='#6B7280')

        # Arrow from center to tier1
        ax.annotate('', xy=(9.3, t1['y']), xytext=(8.7, 4.9),
                    arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=1.5,
                                     connectionstyle='arc3,rad=0.1'))

    # Bottom: Validation logic
    ax.text(7, 0.8, 'Validation Logic', fontsize=11, fontweight='bold', ha='center',
            color='#1F2937')
    ax.text(7, 0.3, 'If K trajectory types found in EdNet (behavioral proxy) also appear in\n'
            'controlled experiments (self-report trust) → model generalizes across\n'
            'measurement methods, domains, and populations',
            fontsize=9, ha='center', color='#4B5563', linespacing=1.4)

    fig.savefig(OUT / 'Analysis_E_Cross_Validation_Strategy.png')
    plt.close()
    print('✓ Figure E: Cross-Validation Strategy')


# ============================================================
# Figure F: Technical Architecture (Python ↔ R)
# ============================================================
def fig_f_tech_architecture():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    ax.text(7, 7.5, 'Technical Architecture: Python ↔ R Subprocess Pipeline',
            fontsize=14, fontweight='bold', ha='center')

    # Python column
    python_box = FancyBboxPatch((0.5, 0.5), 5.0, 6.5,
                                 boxstyle="round,pad=0.15", facecolor='#FFF7ED',
                                 edgecolor='#F59E0B', linewidth=2)
    ax.add_patch(python_box)
    ax.text(3.0, 6.7, 'Python 3.12', fontsize=13, fontweight='bold', ha='center',
            color='#B45309')
    ax.text(3.0, 6.35, 'pandas / numpy / scikit-learn / matplotlib',
            fontsize=8, ha='center', color='#92400E', style='italic')

    py_steps = [
        ('1. Load & Filter', 'Read 297K CSVs\nFilter 100+ episode students\n→ ~68,000 students', 5.6),
        ('2. Parse Episodes', 'Action logs → episodes\nCompute: accuracy, time,\nsource, explanation', 4.4),
        ('3. Compute Proxies', 'Rolling window (20 ep):\nAI_reliance, sys_accuracy,\ncalibration_gap', 3.2),
        ('4. Time Normalize', 'Variable-length → 20 ventiles\nstudent × 20 matrix\n→ CSV export', 2.0),
        ('6. Visualize & Report', 'Trajectory plots, tables\nOutcome comparisons\n→ Publication figures', 0.8),
    ]

    for title, desc, y in py_steps:
        rect = FancyBboxPatch((0.8, y - 0.45), 4.4, 0.9,
                               boxstyle="round,pad=0.05", facecolor='white',
                               edgecolor='#F59E0B', linewidth=1)
        ax.add_patch(rect)
        ax.text(1.0, y + 0.2, title, fontsize=9, fontweight='bold', color='#B45309')
        ax.text(1.0, y - 0.15, desc, fontsize=7, color='#374151', linespacing=1.2)

    # R column
    r_box = FancyBboxPatch((8.5, 1.5), 5.0, 5.0,
                             boxstyle="round,pad=0.15", facecolor='#EFF6FF',
                             edgecolor='#2563EB', linewidth=2)
    ax.add_patch(r_box)
    ax.text(11.0, 6.2, 'R 4.5.2', fontsize=13, fontweight='bold', ha='center',
            color='#1E40AF')
    ax.text(11.0, 5.85, 'mclust / tidyLPA / lcmm / flexmix',
            fontsize=8, ha='center', color='#1E3A8A', style='italic')

    r_steps = [
        ('5a. Growth Mixture Model', 'Read ventile matrix CSV\nFit GMM: K=1 to K=6\nmclust::Mclust()', 5.0),
        ('5b. Model Comparison', 'BIC, AIC, Entropy, BLRT\ntidyLPA::compare_solutions()\n→ Optimal K', 3.8),
        ('5c. Class Assignment', 'Posterior probabilities\nMost-likely class per student\n→ CSV export', 2.6),
    ]

    for title, desc, y in r_steps:
        rect = FancyBboxPatch((8.8, y - 0.45), 4.4, 0.9,
                               boxstyle="round,pad=0.05", facecolor='white',
                               edgecolor='#2563EB', linewidth=1)
        ax.add_patch(rect)
        ax.text(9.0, y + 0.2, title, fontsize=9, fontweight='bold', color='#1E40AF')
        ax.text(9.0, y - 0.15, desc, fontsize=7, color='#374151', linespacing=1.2)

    # Arrows between Python and R
    # Python step 4 → R step 5a
    ax.annotate('', xy=(8.3, 4.5), xytext=(5.7, 2.0),
                arrowprops=dict(arrowstyle='->', color='#6B7280', lw=2.5,
                                 connectionstyle='arc3,rad=-0.3'))
    ax.text(6.5, 3.8, 'ventile_matrix.csv', fontsize=8, fontweight='bold',
            color='#6B7280', ha='center', rotation=-25,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#D1D5DB'))

    # R step 5c → Python step 6
    ax.annotate('', xy=(5.7, 0.8), xytext=(8.3, 2.1),
                arrowprops=dict(arrowstyle='->', color='#6B7280', lw=2.5,
                                 connectionstyle='arc3,rad=-0.3'))
    ax.text(7.5, 1.1, 'class_assignments.csv', fontsize=8, fontweight='bold',
            color='#6B7280', ha='center', rotation=25,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#D1D5DB'))

    # Subprocess call notation
    ax.text(7.0, 0.2, 'Interface: subprocess.run(["Rscript", "gmm_analysis.R"])',
            fontsize=9, ha='center', color='#6B7280', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3F4F6', edgecolor='#D1D5DB'))

    fig.savefig(OUT / 'Analysis_F_Technical_Architecture.png')
    plt.close()
    print('✓ Figure F: Technical Architecture')


if __name__ == '__main__':
    fig_a_pipeline()
    fig_b_trust_proxy()
    fig_c_expected_trajectories()
    fig_d_gmm_selection()
    fig_e_cross_validation()
    fig_f_tech_architecture()
    print('\nAll 6 analysis plan figures generated!')
