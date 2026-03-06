#!/usr/bin/env python3
"""
Generate Figure 1 v2: Trust Calibration Process Model
Changes from v1:
  - Panel (a): Added annotation box about TCRS measuring readiness
  - Panel (b): "TRUST" → "TRUST EVALUATION"
  - Panel (b): Dashed feedback arrow from Calibration back to Metacognition
  - Panel (b): "(with recursive feedback)" note
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9),
                                gridspec_kw={'width_ratios': [1, 1.1]})
fig.subplots_adjust(wspace=0.08, left=0.05, right=0.97, top=0.95, bottom=0.05)

# ============================================================
# Panel (a): Trust Calibration Space
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

# Over-trust point and arrow
ax1.plot(0.35, 0.78, 'o', color='#CC4444', markersize=10, zorder=5)
ax1.annotate('Over-trust\n(Misuse)', xy=(0.35, 0.78),
             xytext=(0.55, 0.88), fontsize=7.5, color='#CC4444',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#CC4444', lw=1.2),
             zorder=5)

# Distrust point and arrow
ax1.plot(0.65, 0.22, 'o', color='#4444CC', markersize=10, zorder=5)
ax1.annotate('Distrust\n(Disuse)', xy=(0.65, 0.22),
             xytext=(0.75, 0.12), fontsize=7.5, color='#4444CC',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#4444CC', lw=1.2),
             zorder=5)

# Agency arrows (green, showing adjustment toward calibration)
ax1.annotate('', xy=(0.43, 0.58), xytext=(0.35, 0.74),
             arrowprops=dict(arrowstyle='->', color='#2E8B57', lw=2),
             zorder=4)
ax1.text(0.25, 0.67, 'Agency\n(Adjust)', fontsize=7, color='#2E8B57',
         fontstyle='italic')

ax1.annotate('', xy=(0.57, 0.42), xytext=(0.65, 0.26),
             arrowprops=dict(arrowstyle='->', color='#2E8B57', lw=2),
             zorder=4)
ax1.text(0.67, 0.33, 'Agency\n(Adjust)', fontsize=7, color='#2E8B57',
         fontstyle='italic')

# Metacognition label (top-left)
metacog_box = FancyBboxPatch((0.02, 0.82), 0.22, 0.08,
                              boxstyle="round,pad=0.01",
                              facecolor='#FFF3E0', edgecolor='#FF9800',
                              linewidth=1.5, zorder=6)
ax1.add_patch(metacog_box)
ax1.text(0.13, 0.86, 'Metacognition:\n"Where am I in\nthis space?"',
         fontsize=6.5, ha='center', va='center', color='#E65100',
         fontweight='bold', zorder=7)

# Axes
ax1.set_xlabel('AI Reliability (Actual Performance)', fontsize=10, fontweight='bold')
ax1.set_ylabel("Trust Level (Learner's Subjective Trust)", fontsize=10, fontweight='bold')
ax1.set_xticks([0, 0.33, 0.66, 1])
ax1.set_xticklabels(['Low', '', '', 'High'], fontsize=9)
ax1.set_yticks([0, 0.33, 0.66, 1])
ax1.set_yticklabels(['Low', '', '', 'High'], fontsize=9)

ax1.set_title('(a) Trust Calibration Space', fontsize=12, fontweight='bold',
              pad=10)

# --- NEW: Readiness annotation box ---
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
# Panel (b): Trust Calibration Process Model
# ============================================================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('(b) Trust Calibration Process Model', fontsize=12,
              fontweight='bold', pad=10)

# Box definitions [x_center, y_center, width, height, color, border, label, theory, description]
boxes = [
    # Metacognition
    {'x': 3.5, 'y': 8.8, 'w': 4.5, 'h': 1.3,
     'fc': '#FFF3E0', 'ec': '#FF9800', 'lw': 2,
     'title': 'METACOGNITION', 'theory': 'Winne & Hadwin (1998)',
     'subtitle': 'Process Stage',
     'q': '"Where am I?"',
     'desc': 'Self-monitoring of trust state\n+ AI system & task context awareness',
     'role': 'Foundation'},
    # Trust Evaluation (changed from TRUST)
    {'x': 3.5, 'y': 6.2, 'w': 4.5, 'h': 1.3,
     'fc': '#E3F2FD', 'ec': '#2196F3', 'lw': 2,
     'title': 'TRUST EVALUATION', 'theory': 'Lee & See (2004)',
     'subtitle': '',
     'q': '"Am I over/under-trusting?"',
     'desc': 'Force displacing from optimal\n(variable being calibrated)',
     'role': 'Variable'},
    # Human Agency
    {'x': 3.5, 'y': 3.6, 'w': 4.5, 'h': 1.3,
     'fc': '#F3E5F5', 'ec': '#9C27B0', 'lw': 2,
     'title': 'HUMAN AGENCY', 'theory': 'Bandura (2001)',
     'subtitle': '',
     'q': '"Adjust toward optimal"',
     'desc': 'Intentional evaluation,\ncomparison, & regulation',
     'role': 'Mechanism'},
    # Calibration
    {'x': 3.5, 'y': 1.0, 'w': 4.5, 'h': 1.3,
     'fc': '#E8F5E9', 'ec': '#4CAF50', 'lw': 2,
     'title': 'CALIBRATION', 'theory': 'Stone (2000)',
     'subtitle': '',
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

    # Title
    ax2.text(b['x'] - 0.5, b['y'] + 0.45, b['title'],
             fontsize=10, fontweight='bold', ha='center', va='center', zorder=5)

    # Theory reference (top-right)
    ax2.text(b['x'] + b['w']/2 - 0.2, b['y'] + 0.5,
             b['theory'], fontsize=6.5, ha='right', va='center',
             color='#666666', fontstyle='italic', zorder=5)

    # Question
    if b['q']:
        ax2.text(b['x'], b['y'] + 0.05, b['q'],
                 fontsize=8, ha='center', va='center',
                 fontstyle='italic', color='#333333', zorder=5)

    # Description
    ax2.text(b['x'], b['y'] - 0.35, b['desc'],
             fontsize=7, ha='center', va='center',
             color='#555555', zorder=5)

# Arrows between boxes (solid, main flow)
arrow_style = dict(arrowstyle='->', color='#333333', lw=2)
ax2.annotate('', xy=(3.5, 6.85), xytext=(3.5, 8.15),
             arrowprops=arrow_style, zorder=4)
ax2.annotate('', xy=(3.5, 4.25), xytext=(3.5, 5.55),
             arrowprops=arrow_style, zorder=4)
ax2.annotate('', xy=(3.5, 1.65), xytext=(3.5, 2.95),
             arrowprops=arrow_style, zorder=4)

# Role labels on arrows
ax2.text(4.0, 7.5, 'Foundation', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')
ax2.text(4.0, 4.9, 'Variable', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')
ax2.text(4.0, 2.3, 'Mechanism', fontsize=7, color='#888888',
         fontstyle='italic', ha='left')

# --- NEW: Dashed feedback arrow from Calibration back to Metacognition ---
# Draw a curved dashed arrow on the left side
from matplotlib.patches import FancyArrowPatch
import matplotlib.path as mpath

# Left-side feedback path: from Calibration (left) up to Metacognition (left)
feedback_x = 0.7
ax2.annotate('',
             xy=(1.25, 9.1),  # top (near Metacognition)
             xytext=(1.25, 0.9),  # bottom (near Calibration)
             arrowprops=dict(arrowstyle='->', color='#888888', lw=1.8,
                            linestyle='dashed',
                            connectionstyle='arc3,rad=0.15'),
             zorder=4)

# Feedback label
ax2.text(0.55, 5.0, '(with recursive\n  feedback)',
         fontsize=7, color='#888888', fontstyle='italic',
         ha='center', va='center', rotation=90, zorder=5)

# Scale subscale labels (right side, with dashed boxes)
subscales = [
    {'y': 8.8, 'label': 'Calibration Awareness', 'color': '#FF9800'},
    {'y': 6.2, 'label': 'Calibration Judgment', 'color': '#2196F3'},
    {'y': 3.6, 'label': 'Calibration Action', 'color': '#9C27B0'},
    {'y': 1.0, 'label': '(Outcome — not\n directly measured)', 'color': '#4CAF50'},
]

for s in subscales:
    # Dashed box on right
    x0 = 7.8
    y0 = s['y'] - 0.4
    w = 2.0
    h = 0.8
    rect = FancyBboxPatch((x0, y0), w, h,
                           boxstyle="round,pad=0.1",
                           facecolor='white', edgecolor=s['color'],
                           linewidth=1.5, linestyle='dashed', zorder=3)
    ax2.add_patch(rect)
    ax2.text(x0 + w/2, s['y'], s['label'],
             fontsize=8, ha='center', va='center',
             color=s['color'], fontstyle='italic', fontweight='bold', zorder=5)

    # Connecting line from main box to subscale box
    ax2.annotate('', xy=(7.8, s['y']), xytext=(5.75, s['y']),
                 arrowprops=dict(arrowstyle='->', color=s['color'],
                                lw=1, linestyle='dashed'),
                 zorder=2)

# Right column header
ax2.text(8.8, 9.8, 'Scale Subscale', fontsize=9, fontweight='bold',
         ha='center', va='center', color='#333333')

plt.savefig('/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/'
            'AALS-Scale-Development/figures/Figure_1_Trust_Calibration_Process_Model_v2.png',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 1 v2 saved successfully.")
