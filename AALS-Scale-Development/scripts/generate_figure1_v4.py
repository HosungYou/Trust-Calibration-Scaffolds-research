#!/usr/bin/env python3
"""
Generate Figure 1 v4: Trust Calibration Process Model
Visually improved version of v3 with same correct framing:
- Functional labels as primary (Monitoring/Evaluative/Regulatory Capacity)
- Source theories as "[informed by: ...]"
- Professional publication-ready design
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ─── Global style ───
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica Neue', 'Helvetica', 'Arial', 'DejaVu Sans']

# Color palette — sophisticated, harmonized
C = {
    'monitor':     '#FF9800',  # warm orange
    'monitor_bg':  '#FFF3E0',
    'monitor_bdr': '#E65100',
    'eval':        '#1976D2',  # deep blue
    'eval_bg':     '#E3F2FD',
    'eval_bdr':    '#0D47A1',
    'regulate':    '#7B1FA2',  # deep purple
    'regulate_bg': '#F3E5F5',
    'regulate_bdr':'#4A148C',
    'calibrate':   '#2E7D32',  # deep green
    'calib_bg':    '#E8F5E9',
    'calib_bdr':   '#1B5E20',
    'overtrust':   '#FFCDD2',
    'distrust':    '#BBDEFB',
    'text_dark':   '#212121',
    'text_mid':    '#616161',
    'text_light':  '#9E9E9E',
    'arrow_main':  '#424242',
    'arrow_feed':  '#9E9E9E',
    'bg':          '#FAFAFA',
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 9.5),
                                gridspec_kw={'width_ratios': [1, 1.15]})
fig.patch.set_facecolor('white')
fig.subplots_adjust(wspace=0.06, left=0.04, right=0.97, top=0.92, bottom=0.06)

# ════════════════════════════════════════════════════════════
# Panel (a): Trust Calibration Space
# ════════════════════════════════════════════════════════════
ax1.set_xlim(-0.08, 1.08)
ax1.set_ylim(-0.08, 1.08)
ax1.set_facecolor('#FAFAFA')

# Background zones with smooth gradients
from matplotlib.colors import LinearSegmentedColormap

# Overtrust zone (above diagonal)
for i in range(50):
    alpha = 0.012 * (50 - i) / 50
    y_offset = i * 0.02
    ax1.fill_between([0, 1], [0 + y_offset, 1 + y_offset],
                     [1.1, 1.1], color='#E53935', alpha=alpha, zorder=0)

# Distrust zone (below diagonal)
for i in range(50):
    alpha = 0.012 * (50 - i) / 50
    y_offset = -i * 0.02
    ax1.fill_between([0, 1], [-0.1, -0.1],
                     [0 + y_offset, 1 + y_offset], color='#1565C0', alpha=alpha, zorder=0)

# Zone labels
ax1.text(0.12, 0.94, 'OVER-TRUST ZONE', fontsize=8.5, color='#C62828',
         fontweight='bold', alpha=0.6, fontstyle='italic')
ax1.text(0.12, 0.90, '(Misuse / Complacency)', fontsize=7, color='#C62828',
         alpha=0.45, fontstyle='italic')
ax1.text(0.62, 0.06, 'DISTRUST ZONE', fontsize=8.5, color='#1565C0',
         fontweight='bold', alpha=0.6, fontstyle='italic')
ax1.text(0.62, 0.02, '(Disuse / Rejection)', fontsize=7, color='#1565C0',
         alpha=0.45, fontstyle='italic')

# Calibration line
ax1.plot([0, 1], [0, 1], color='#2E7D32', linewidth=2.5, zorder=2, alpha=0.8)
ax1.text(0.72, 0.80, 'Perfect\nCalibration', fontsize=7.5, color='#2E7D32',
         fontweight='bold', alpha=0.7, rotation=40, ha='center', va='center')

# Calibration point (main)
ax1.plot(0.5, 0.5, 'o', color='#2E7D32', markersize=16, zorder=5,
         markeredgecolor='white', markeredgewidth=2)
ax1.annotate('Calibrated\n(Trust = Reliability)', xy=(0.5, 0.5),
             xytext=(0.15, 0.60), fontsize=7.5, color='#2E7D32',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.5,
                           connectionstyle='arc3,rad=0.2'),
             zorder=5,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9',
                      edgecolor='#2E7D32', alpha=0.9, linewidth=1))

# Over-trust point
ax1.plot(0.30, 0.78, 'o', color='#C62828', markersize=11, zorder=5,
         markeredgecolor='white', markeredgewidth=1.5)
ax1.annotate('Over-trust', xy=(0.30, 0.78),
             xytext=(0.52, 0.92), fontsize=7.5, color='#C62828',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.2,
                           connectionstyle='arc3,rad=-0.2'),
             zorder=5)

# Distrust point
ax1.plot(0.70, 0.25, 'o', color='#1565C0', markersize=11, zorder=5,
         markeredgecolor='white', markeredgewidth=1.5)
ax1.annotate('Distrust', xy=(0.70, 0.25),
             xytext=(0.82, 0.15), fontsize=7.5, color='#1565C0',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.2,
                           connectionstyle='arc3,rad=0.2'),
             zorder=5)

# Regulation arrows (from miscalibrated → calibration line)
ax1.annotate('', xy=(0.42, 0.58), xytext=(0.30, 0.74),
             arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=2.2,
                           connectionstyle='arc3,rad=0.15'), zorder=4)
ax1.text(0.19, 0.70, 'Regulate\n(reduce trust)', fontsize=6.5, color='#2E7D32',
         fontstyle='italic', alpha=0.8)

ax1.annotate('', xy=(0.58, 0.42), xytext=(0.70, 0.29),
             arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=2.2,
                           connectionstyle='arc3,rad=0.15'), zorder=4)
ax1.text(0.72, 0.37, 'Regulate\n(increase trust)', fontsize=6.5, color='#2E7D32',
         fontstyle='italic', alpha=0.8)

# Monitoring label box
monitor_box = FancyBboxPatch((0.01, 0.80), 0.28, 0.12,
                              boxstyle="round,pad=0.02",
                              facecolor=C['monitor_bg'], edgecolor=C['monitor'],
                              linewidth=1.8, zorder=6, alpha=0.95)
ax1.add_patch(monitor_box)
ax1.text(0.15, 0.88, 'Monitoring:', fontsize=7, ha='center', va='center',
         color=C['monitor_bdr'], fontweight='bold', zorder=7)
ax1.text(0.15, 0.84, '"Where am I\nin this space?"', fontsize=6, ha='center',
         va='center', color=C['monitor_bdr'], fontstyle='italic', zorder=7)

# Axes styling
ax1.set_xlabel('AI Reliability (Actual Performance)', fontsize=10.5,
               fontweight='bold', color=C['text_dark'], labelpad=8)
ax1.set_ylabel("Trust Level (Learner's Subjective Trust)", fontsize=10.5,
               fontweight='bold', color=C['text_dark'], labelpad=8)
ax1.set_xticks([0, 0.5, 1])
ax1.set_xticklabels(['Low', 'Medium', 'High'], fontsize=9, color=C['text_mid'])
ax1.set_yticks([0, 0.5, 1])
ax1.set_yticklabels(['Low', 'Medium', 'High'], fontsize=9, color=C['text_mid'])

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_color(C['text_light'])
ax1.spines['left'].set_color(C['text_light'])
ax1.tick_params(colors=C['text_light'])

ax1.set_title('(a) Trust Calibration Space', fontsize=13, fontweight='bold',
              color=C['text_dark'], pad=12)

# Readiness note
note_text = ("Note: The TCRS measures readiness to engage\n"
             "in this calibration process, not the learner's\n"
             "position in this space.")
props = dict(boxstyle='round,pad=0.4', facecolor='#FFFDE7',
             edgecolor='#F9A825', linewidth=1.2, alpha=0.95)
ax1.text(0.50, 0.01, note_text, transform=ax1.transAxes,
         fontsize=6.5, verticalalignment='bottom', horizontalalignment='center',
         bbox=props, fontstyle='italic', color='#5D4037', zorder=10)

# ════════════════════════════════════════════════════════════
# Panel (b): Trust Calibration Process Model
# ════════════════════════════════════════════════════════════
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_facecolor('white')
ax2.set_title('(b) Trust Calibration Process Model', fontsize=13,
              fontweight='bold', color=C['text_dark'], pad=12)

# ─── Box definitions ───
box_data = [
    {
        'x': 3.8, 'y': 9.0, 'w': 5.2, 'h': 1.35,
        'bg': C['monitor_bg'], 'border': C['monitor'], 'accent': C['monitor_bdr'],
        'step': '1', 'title': 'MONITORING CAPACITY',
        'question': '"Where am I?"',
        'informed': 'informed by: self-monitoring in SRL\n(Winne & Hadwin, 1998)',
        'role': 'Foundation',
    },
    {
        'x': 3.8, 'y': 6.45, 'w': 5.2, 'h': 1.35,
        'bg': C['eval_bg'], 'border': C['eval'], 'accent': C['eval_bdr'],
        'step': '2', 'title': 'EVALUATIVE CAPACITY',
        'question': '"Is my trust appropriate?"',
        'informed': 'informed by: trust dynamics\n(Lee & See, 2004)',
        'role': 'Variable',
    },
    {
        'x': 3.8, 'y': 3.9, 'w': 5.2, 'h': 1.35,
        'bg': C['regulate_bg'], 'border': C['regulate'], 'accent': C['regulate_bdr'],
        'step': '3', 'title': 'REGULATORY CAPACITY',
        'question': '"Adjust toward appropriate"',
        'informed': 'informed by: self-regulation\n(Bandura, 2001)',
        'role': 'Mechanism',
    },
    {
        'x': 3.8, 'y': 1.5, 'w': 5.2, 'h': 1.05,
        'bg': C['calib_bg'], 'border': C['calibrate'], 'accent': C['calib_bdr'],
        'step': '', 'title': 'CALIBRATION',
        'question': '',
        'informed': '',
        'role': 'Outcome',
    },
]

# ─── Draw boxes ───
for b in box_data:
    x0 = b['x'] - b['w']/2
    y0 = b['y'] - b['h']/2

    # Main box
    rect = FancyBboxPatch((x0, y0), b['w'], b['h'],
                           boxstyle="round,pad=0.18",
                           facecolor=b['bg'], edgecolor=b['border'],
                           linewidth=2.2, zorder=3)
    ax2.add_patch(rect)

    # Step number circle
    if b['step']:
        circle = plt.Circle((x0 + 0.35, b['y'] + b['h']/2 - 0.32), 0.22,
                            facecolor=b['border'], edgecolor='white',
                            linewidth=1.5, zorder=6)
        ax2.add_patch(circle)
        ax2.text(x0 + 0.35, b['y'] + b['h']/2 - 0.32, b['step'],
                fontsize=9, fontweight='bold', color='white',
                ha='center', va='center', zorder=7)

    # Title
    title_y = b['y'] + 0.38 if b['step'] else b['y'] + 0.25
    ax2.text(b['x'], title_y, b['title'],
             fontsize=11, fontweight='bold', ha='center', va='center',
             color=b['accent'], zorder=5)

    # Question
    if b['question']:
        ax2.text(b['x'], b['y'] + 0.02, b['question'],
                 fontsize=9, ha='center', va='center',
                 fontstyle='italic', color=C['text_dark'], zorder=5)

    # Informed by
    if b['informed']:
        ax2.text(b['x'], b['y'] - 0.38, b['informed'],
                 fontsize=6.5, ha='center', va='center',
                 color=C['text_light'], fontstyle='italic', zorder=5)

    # Calibration outcome text
    if b['title'] == 'CALIBRATION':
        ax2.text(b['x'], b['y'] - 0.05,
                 'Trust matches reliability\nAppropriate trust achieved',
                 fontsize=7.5, ha='center', va='center',
                 color=C['text_mid'], zorder=5)

# ─── Sequential arrows (main flow) ───
arrow_kw = dict(arrowstyle='->', color=C['arrow_main'], lw=2.2,
                connectionstyle='arc3,rad=0')

# Step 1 → Step 2
ax2.annotate('', xy=(3.8, 7.13), xytext=(3.8, 8.32),
             arrowprops=arrow_kw, zorder=4)
# Step 2 → Step 3
ax2.annotate('', xy=(3.8, 4.58), xytext=(3.8, 5.77),
             arrowprops=arrow_kw, zorder=4)
# Step 3 → Outcome
ax2.annotate('', xy=(3.8, 2.03), xytext=(3.8, 3.22),
             arrowprops=arrow_kw, zorder=4)

# Role labels on arrows
role_style = dict(fontsize=7, color=C['text_light'], fontstyle='italic', ha='left')
ax2.text(4.15, 7.72, 'Foundation', **role_style)
ax2.text(4.15, 5.17, 'Variable', **role_style)
ax2.text(4.15, 2.62, 'Mechanism', **role_style)

# ─── Recursive feedback arrow (dashed, from Outcome back to Monitoring) ───
ax2.annotate('',
             xy=(1.15, 9.3),
             xytext=(1.15, 1.2),
             arrowprops=dict(arrowstyle='->', color=C['arrow_feed'], lw=1.8,
                            linestyle='dashed',
                            connectionstyle='arc3,rad=0.12'),
             zorder=4)

ax2.text(0.45, 5.2, 'recursive\nfeedback',
         fontsize=7, color=C['arrow_feed'], fontstyle='italic',
         ha='center', va='center', rotation=90, zorder=5)

# ─── TCRS Subscale boxes (right side) ───
subscales = [
    {'y': 9.0, 'label': 'Calibration\nAwareness\n(CA-Aw)', 'color': C['monitor']},
    {'y': 6.45, 'label': 'Calibration\nJudgment\n(CA-Jd)', 'color': C['eval']},
    {'y': 3.9, 'label': 'Calibration\nAction\n(CA-Ac)', 'color': C['regulate']},
    {'y': 1.5, 'label': '(Outcome\u2014not\ndirectly measured)', 'color': C['calibrate']},
]

# Column header
ax2.text(8.8, 9.85, 'TCRS Subscale', fontsize=9.5, fontweight='bold',
         ha='center', va='center', color=C['text_dark'])

for s in subscales:
    x0 = 7.6
    y0 = s['y'] - 0.42
    w = 2.2
    h = 0.84

    rect = FancyBboxPatch((x0, y0), w, h,
                           boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor=s['color'],
                           linewidth=1.5, linestyle='dashed', zorder=3,
                           alpha=0.9)
    ax2.add_patch(rect)
    ax2.text(x0 + w/2, s['y'], s['label'],
             fontsize=7.5, ha='center', va='center',
             color=s['color'], fontweight='bold', fontstyle='italic', zorder=5)

    # Connection arrow
    ax2.annotate('', xy=(7.6, s['y']), xytext=(6.4, s['y']),
                 arrowprops=dict(arrowstyle='->', color=s['color'],
                                lw=1.2, linestyle='dashed'),
                 zorder=2)

# ─── Save ───
output_path = ('/Volumes/External SSD/Projects/Research/'
               'Trust-Calibration-Scaffolds-research/AALS-Scale-Development/'
               'figures/Figure_1_Trust_Calibration_Process_Model_v4.png')

plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white',
            edgecolor='none')
plt.close()
print(f"Figure 1 v4 saved: {output_path}")
