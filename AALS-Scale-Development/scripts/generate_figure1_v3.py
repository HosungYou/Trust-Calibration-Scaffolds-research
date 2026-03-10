#!/usr/bin/env python3
"""
Generate Figure 1 v3: Trust Calibration Process Model
Key change from v2: Panel (b) uses FUNCTIONAL LABELS (Monitoring/Evaluative/Regulatory Capacity)
instead of source theory names as primary labels. Source theories demoted to "[informed by: ...]".
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9),
                                gridspec_kw={'width_ratios': [1, 1.1]})
fig.subplots_adjust(wspace=0.08, left=0.05, right=0.97, top=0.95, bottom=0.05)

# ============================================================
# Panel (a): Trust Calibration Space (unchanged from v2)
# ============================================================
ax1.set_xlim(-0.05, 1.05)
ax1.set_ylim(-0.05, 1.05)

# Background zones
ax1.fill_between([0, 1], [0, 1], [1, 1], color='#FFE0E0', alpha=0.5, zorder=0)
ax1.fill_between([0, 1], [0, 0], [0, 1], color='#E0E8FF', alpha=0.5, zorder=0)

# Zone labels
ax1.text(0.15, 0.92, 'OVER-TRUST ZONE', fontsize=8, color='#CC4444',
         fontstyle='italic', alpha=0.7)
ax1.text(0.65, 0.08, 'DISTRUST ZONE', fontsize=8, color='#4444CC',
         fontstyle='italic', alpha=0.7)

# Calibration line
ax1.plot([0, 1], [0, 1], 'k-', linewidth=2, zorder=2)

# Calibration point
ax1.plot(0.5, 0.5, 'o', color='#2E8B57', markersize=14, zorder=5)
ax1.annotate('Calibration\n(Trust = Reliability)', xy=(0.5, 0.5),
             xytext=(0.18, 0.58), fontsize=7.5, color='#2E8B57',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#2E8B57', lw=1.5),
             zorder=5)

# Over-trust point
ax1.plot(0.35, 0.78, 'o', color='#CC4444', markersize=10, zorder=5)
ax1.annotate('Over-trust\n(Misuse)', xy=(0.35, 0.78),
             xytext=(0.55, 0.88), fontsize=7.5, color='#CC4444',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#CC4444', lw=1.2),
             zorder=5)

# Distrust point
ax1.plot(0.65, 0.22, 'o', color='#4444CC', markersize=10, zorder=5)
ax1.annotate('Distrust\n(Disuse)', xy=(0.65, 0.22),
             xytext=(0.75, 0.12), fontsize=7.5, color='#4444CC',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#4444CC', lw=1.2),
             zorder=5)

# Agency arrows
ax1.annotate('', xy=(0.43, 0.58), xytext=(0.35, 0.74),
             arrowprops=dict(arrowstyle='->', color='#2E8B57', lw=2), zorder=4)
ax1.text(0.22, 0.67, 'Regulation\n(Adjust)', fontsize=7, color='#2E8B57',
         fontstyle='italic')

ax1.annotate('', xy=(0.57, 0.42), xytext=(0.65, 0.26),
             arrowprops=dict(arrowstyle='->', color='#2E8B57', lw=2), zorder=4)
ax1.text(0.67, 0.33, 'Regulation\n(Adjust)', fontsize=7, color='#2E8B57',
         fontstyle='italic')

# Monitoring label
metacog_box = FancyBboxPatch((0.02, 0.82), 0.22, 0.08,
                              boxstyle="round,pad=0.01",
                              facecolor='#FFF3E0', edgecolor='#FF9800',
                              linewidth=1.5, zorder=6)
ax1.add_patch(metacog_box)
ax1.text(0.13, 0.86, 'Monitoring:\n"Where am I in\nthis space?"',
         fontsize=6.5, ha='center', va='center', color='#E65100',
         fontweight='bold', zorder=7)

# Axes
ax1.set_xlabel('AI Reliability (Actual Performance)', fontsize=10, fontweight='bold')
ax1.set_ylabel("Trust Level (Learner's Subjective Trust)", fontsize=10, fontweight='bold')
ax1.set_xticks([0, 0.33, 0.66, 1])
ax1.set_xticklabels(['Low', '', '', 'High'], fontsize=9)
ax1.set_yticks([0, 0.33, 0.66, 1])
ax1.set_yticklabels(['Low', '', '', 'High'], fontsize=9)

ax1.set_title('(a) Trust Calibration Space', fontsize=12, fontweight='bold', pad=10)

# Readiness annotation box
annotation_text = ("Note: The TCRS measures readiness to\n"
                   "engage in this calibration process,\n"
                   "not the learner's position in this space.")
props = dict(boxstyle='round,pad=0.4', facecolor='#FFFDE7',
             edgecolor='#F9A825', linewidth=1.5, alpha=0.95)
ax1.text(0.50, 0.02, annotation_text, transform=ax1.transAxes,
         fontsize=7, verticalalignment='bottom', horizontalalignment='center',
         bbox=props, fontstyle='italic', color='#5D4037', zorder=10)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# ============================================================
# Panel (b): Trust Calibration Process Model — FUNCTIONAL LABELS
# ============================================================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('(b) Trust Calibration Process Model', fontsize=12,
              fontweight='bold', pad=10)

# Box definitions — FUNCTIONAL LABELS as primary, source theory as "[informed by: ...]"
boxes = [
    # Monitoring Capacity
    {'x': 3.5, 'y': 8.8, 'w': 4.8, 'h': 1.4,
     'fc': '#FFF3E0', 'ec': '#FF9800', 'lw': 2,
     'title': 'MONITORING CAPACITY',
     'informed_by': '[informed by: self-monitoring\nin SRL, Winne & Hadwin, 1998]',
     'q': '"Where am I?"',
     'desc': 'Self-monitoring of trust state\n+ AI system & task context awareness',
     'role': 'Foundation'},
    # Evaluative Capacity
    {'x': 3.5, 'y': 6.1, 'w': 4.8, 'h': 1.4,
     'fc': '#E3F2FD', 'ec': '#2196F3', 'lw': 2,
     'title': 'EVALUATIVE CAPACITY',
     'informed_by': '[informed by: trust dynamics,\nLee & See, 2004]',
     'q': '"Is my trust appropriate?"',
     'desc': 'Trust-reliability matching assessment\n(variable being calibrated)',
     'role': 'Variable'},
    # Regulatory Capacity
    {'x': 3.5, 'y': 3.4, 'w': 4.8, 'h': 1.4,
     'fc': '#F3E5F5', 'ec': '#9C27B0', 'lw': 2,
     'title': 'REGULATORY CAPACITY',
     'informed_by': '[informed by: self-regulation,\nBandura, 2001]',
     'q': '"Adjust toward appropriate"',
     'desc': 'Intentional verification,\ncomparison, & behavioral adjustment',
     'role': 'Mechanism'},
    # Calibration
    {'x': 3.5, 'y': 0.9, 'w': 4.8, 'h': 1.1,
     'fc': '#E8F5E9', 'ec': '#4CAF50', 'lw': 2,
     'title': 'CALIBRATION',
     'informed_by': '',
     'q': '',
     'desc': 'Trust matches reliability\nAppropriate trust achieved\n(Outcome)',
     'role': 'Outcome'},
]

# Draw boxes
for b in boxes:
    x0 = b['x'] - b['w']/2
    y0 = b['y'] - b['h']/2
    rect = FancyBboxPatch((x0, y0), b['w'], b['h'],
                           boxstyle="round,pad=0.15",
                           facecolor=b['fc'], edgecolor=b['ec'],
                           linewidth=b['lw'], zorder=3)
    ax2.add_patch(rect)

    # Title (functional label — primary, bold)
    ax2.text(b['x'], b['y'] + 0.48, b['title'],
             fontsize=10, fontweight='bold', ha='center', va='center', zorder=5)

    # Question
    if b['q']:
        ax2.text(b['x'], b['y'] + 0.1, b['q'],
                 fontsize=8.5, ha='center', va='center',
                 fontstyle='italic', color='#333333', zorder=5)

    # Informed by (smaller, gray — demoted)
    if b['informed_by']:
        ax2.text(b['x'], b['y'] - 0.28, b['informed_by'],
                 fontsize=6.5, ha='center', va='center',
                 color='#777777', fontstyle='italic', zorder=5)

    # Description (bottom)
    desc_y = b['y'] - 0.55 if b['informed_by'] else b['y'] - 0.2
    if b['desc'] and b['title'] != 'CALIBRATION':
        pass  # Description folded into informed_by line for cleaner look

    # For Calibration box, show desc
    if b['title'] == 'CALIBRATION':
        ax2.text(b['x'], b['y'] - 0.05, b['desc'],
                 fontsize=7, ha='center', va='center',
                 color='#555555', zorder=5)

# Arrows between boxes (solid, main flow)
arrow_style = dict(arrowstyle='->', color='#333333', lw=2)
ax2.annotate('', xy=(3.5, 6.80), xytext=(3.5, 8.08),
             arrowprops=arrow_style, zorder=4)
ax2.annotate('', xy=(3.5, 4.10), xytext=(3.5, 5.38),
             arrowprops=arrow_style, zorder=4)
ax2.annotate('', xy=(3.5, 1.45), xytext=(3.5, 2.68),
             arrowprops=arrow_style, zorder=4)

# Role labels on arrows
ax2.text(4.2, 7.45, 'Foundation', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')
ax2.text(4.2, 4.75, 'Variable', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')
ax2.text(4.2, 2.05, 'Mechanism', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')

# Dashed feedback arrow from Calibration back to Monitoring Capacity
ax2.annotate('',
             xy=(1.1, 9.2),
             xytext=(1.1, 0.7),
             arrowprops=dict(arrowstyle='->', color='#888888', lw=1.8,
                            linestyle='dashed',
                            connectionstyle='arc3,rad=0.15'),
             zorder=4)

ax2.text(0.45, 5.0, '(recursive\n feedback)',
         fontsize=7, color='#888888', fontstyle='italic',
         ha='center', va='center', rotation=90, zorder=5)

# Scale subscale labels (right side, dashed boxes)
subscales = [
    {'y': 8.8, 'label': 'Calibration\nAwareness\n(CA-Aw)', 'color': '#FF9800'},
    {'y': 6.1, 'label': 'Calibration\nJudgment\n(CA-Jd)', 'color': '#2196F3'},
    {'y': 3.4, 'label': 'Calibration\nAction\n(CA-Ac)', 'color': '#9C27B0'},
    {'y': 0.9, 'label': '(Outcome \u2014 not\n directly measured)', 'color': '#4CAF50'},
]

for s in subscales:
    x0 = 7.8
    y0 = s['y'] - 0.45
    w = 2.0
    h = 0.9
    rect = FancyBboxPatch((x0, y0), w, h,
                           boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor=s['color'],
                           linewidth=1.5, linestyle='dashed', zorder=3)
    ax2.add_patch(rect)
    ax2.text(x0 + w/2, s['y'], s['label'],
             fontsize=7.5, ha='center', va='center',
             color=s['color'], fontstyle='italic', fontweight='bold', zorder=5)

    ax2.annotate('', xy=(7.8, s['y']), xytext=(5.9, s['y']),
                 arrowprops=dict(arrowstyle='->', color=s['color'],
                                lw=1, linestyle='dashed'),
                 zorder=2)

# Right column header
ax2.text(8.8, 9.8, 'Scale Subscale', fontsize=9, fontweight='bold',
         ha='center', va='center', color='#333333')

plt.savefig('/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/'
            'AALS-Scale-Development/figures/Figure_1_Trust_Calibration_Process_Model_v3.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 1 v3 saved successfully.")
