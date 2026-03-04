"""
Figure 2: Research Orientation Typology Distribution
Horizontal bar chart — trust in educational AI research domains.
10 x 6 in, 300 DPI. Academic publication quality.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Palette ───────────────────────────────────────────────────────────────────
C = {
    'D1': '#d9d9d9',
    'D2': '#969696',
    'D3': '#525252',
    'D4': '#3182bd',
    'D5': '#006d2c',
    'D4a': '#9ecae1',
    'D4b': '#6baed6',
    'D4c': '#2171b5',
    'D5_db':  '#74c476',
    'D5_sup': '#238b45',
    'thr': '#d62728',
}

# ── Geometry ──────────────────────────────────────────────────────────────────
BAR_H   = 0.46     # main bar height
SUB_H   = 0.13     # subcategory indicator height
YSTEP   = 1.0      # vertical spacing

Y = {d: i * YSTEP for i, d in enumerate(['D1','D2','D3','D4','D5'])}
XLIM = 60

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
fig.subplots_adjust(left=0.22, right=0.97, top=0.88, bottom=0.10)

# ── Main bars ─────────────────────────────────────────────────────────────────
main = [
    ('D1',  5,  5.2),
    ('D2', 11, 11.3),
    ('D3', 24, 24.7),
    ('D4', 41, 42.3),
    ('D5', 16, 16.5),
]
for key, n, pct in main:
    ax.barh(Y[key], n, height=BAR_H, color=C[key],
            edgecolor='white', linewidth=1.2, zorder=3)

# ── D4 subcategory hatched stripes (inside the D4 bar) ───────────────────────
d4_subs = [
    # (y_offset_from_D4, n, hatch, color)
    (-SUB_H,     16, '//',   C['D4a']),
    (0,          18, '\\\\', C['D4b']),
    (+SUB_H,      7, 'xx',   C['D4c']),
]
for dy, n, hatch, color in d4_subs:
    ax.barh(Y['D4'] + dy, n, height=SUB_H * 0.85,
            color=color, hatch=hatch,
            edgecolor='white', linewidth=0.5,
            alpha=0.90, zorder=4)

# ── D5 subcategory hatched stripes ────────────────────────────────────────────
d5_subs = [
    (-SUB_H * 0.5,  3,  '//',   C['D5_db']),
    (+SUB_H * 0.5, 13,  '\\\\', C['D5_sup']),
]
for dy, n, hatch, color in d5_subs:
    ax.barh(Y['D5'] + dy, n, height=SUB_H * 0.85,
            color=color, hatch=hatch,
            edgecolor='white', linewidth=0.5,
            alpha=0.90, zorder=4)

# ── n / % labels on main bars ─────────────────────────────────────────────────
for key, n, pct in main:
    lbl = f'n={n}  ({pct}%)'
    if n >= 10:
        ax.text(n / 2, Y[key], lbl,
                va='center', ha='center',
                fontsize=9, fontweight='bold',
                color='white', zorder=5)
    else:
        ax.text(n + 0.6, Y[key], lbl,
                va='center', ha='left',
                fontsize=9, fontweight='bold',
                color='#333333', zorder=5)

# ── D4 sub labels (right of D4 bar, stacked vertically) ──────────────────────
d4_lbl_x = 42.0
d4_lbls = [
    (16, 'D4a: Overtrust (n=16)',       C['D4a'], '//'),
    (18, 'D4b: Undertrust (n=18)',      C['D4b'], '\\\\'),
    ( 7, 'D4c: Bidirectional (n=7)',    C['D4c'], 'xx'),
]
for i, (n, lbl, color, hatch) in enumerate(d4_lbls):
    ry = Y['D4'] + (i - 1) * 0.20
    # small swatch
    ax.barh(ry, 0.9, height=0.14, left=d4_lbl_x,
            color=color, hatch=hatch,
            edgecolor='#555', linewidth=0.5,
            alpha=0.92, zorder=5)
    ax.text(d4_lbl_x + 1.1, ry,
            lbl,
            va='center', ha='left',
            fontsize=7.0, color='#222',
            fontstyle='italic', zorder=6)

# ── D5 sub labels ─────────────────────────────────────────────────────────────
d5_lbl_x = 17.0
d5_lbls = [
    ( 3, 'DB Sourced',     C['D5_db'],  '//'),
    (13, 'Supplementary',  C['D5_sup'], '\\\\'),
]
for i, (n, lbl, color, hatch) in enumerate(d5_lbls):
    ry = Y['D5'] + (i - 0.5) * 0.20
    ax.barh(ry, 1.0, height=0.14, left=d5_lbl_x,
            color=color, hatch=hatch,
            edgecolor='#555', linewidth=0.5,
            alpha=0.92, zorder=5)
    ax.text(d5_lbl_x + 1.3, ry,
            f'{lbl}  (n={n})',
            va='center', ha='left',
            fontsize=7.0, color='#222',
            fontstyle='italic', zorder=6)

# ── Calibration Threshold line ────────────────────────────────────────────────
thresh_x = 41.8
ax.axvline(thresh_x, color=C['thr'], linewidth=1.8,
           linestyle='--', zorder=6)

# Label above bars
ax.text(thresh_x + 0.5, Y['D5'] + BAR_H / 2 + 0.22,
        'Calibration\nThreshold',
        va='bottom', ha='left',
        fontsize=7.8, color=C['thr'], fontweight='bold')

# ── "83.5% below" annotation ─────────────────────────────────────────────────
# Placed between D1 and D2 on the right (above the legend zone)
below_y = (Y['D1'] + Y['D2']) / 2
ax.annotate(
    '83.5% below\ncalibration threshold\n(D1–D4)',
    xy=(thresh_x - 0.5, (Y['D1'] + Y['D4']) / 2),
    xytext=(thresh_x - 16, below_y + 0.1),
    va='center', ha='center',
    fontsize=8.0, color='#444', fontweight='semibold',
    arrowprops=dict(
        arrowstyle='->', color='#888',
        lw=1.2, connectionstyle='arc3,rad=0.15'),
    bbox=dict(boxstyle='round,pad=0.4', fc='#f7f7f7',
              ec='#cccccc', lw=0.8, alpha=0.92),
    zorder=7,
)

# ── "16.5% at calibration level" annotation ──────────────────────────────────
ax.annotate(
    '16.5% at\ncalibration level\n(D5)',
    xy=(thresh_x + 0.5, Y['D5']),
    xytext=(thresh_x + 9, Y['D5'] - 0.6),
    va='center', ha='center',
    fontsize=8.0, color='#005824', fontweight='semibold',
    arrowprops=dict(
        arrowstyle='->', color='#238b45',
        lw=1.2),
    bbox=dict(boxstyle='round,pad=0.4', fc='#e5f5e0',
              ec='#74c476', lw=0.8, alpha=0.92),
    zorder=7,
)

# ── Axes ──────────────────────────────────────────────────────────────────────
y_labels = {
    'D1': 'D1: Trust\nAdoption',
    'D2': 'D2: Trust\nConceptualization',
    'D3': 'D3: Trust\nDesign',
    'D4': 'D4: Trust\nAwareness',
    'D5': 'D5: Trust\nCalibration',
}
ax.set_yticks([Y[k] for k in ['D1','D2','D3','D4','D5']])
ax.set_yticklabels([y_labels[k] for k in ['D1','D2','D3','D4','D5']],
                   fontsize=9.5)
ax.set_xlabel('Number of Studies (n)', fontsize=10, labelpad=8)
ax.set_xlim(0, XLIM)
ax.set_ylim(Y['D1'] - 0.55, Y['D5'] + 0.80)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#c0c0c0')
ax.spines['bottom'].set_color('#c0c0c0')
ax.tick_params(axis='both', color='#c0c0c0', length=3)
ax.tick_params(axis='y', pad=6)
ax.set_axisbelow(True)
ax.xaxis.grid(True, color='#ebebeb', linewidth=0.7)

# ── Legend ────────────────────────────────────────────────────────────────────
leg = [
    mpatches.Patch(fc=C['D1'], ec='#888', label='D1: Trust Adoption'),
    mpatches.Patch(fc=C['D2'], ec='#888', label='D2: Trust Conceptualization'),
    mpatches.Patch(fc=C['D3'], ec='#888', label='D3: Trust Design'),
    mpatches.Patch(fc=C['D4'], ec='#888', label='D4: Trust Awareness'),
    mpatches.Patch(fc=C['D5'], ec='#888', label='D5: Trust Calibration'),
    mpatches.Patch(fc='white', ec='#555', hatch='//',   label='D4 subcategory (hatched)'),
    mpatches.Patch(fc='white', ec='#555', hatch='\\\\', label='D5: DB vs. Supplementary'),
    plt.Line2D([0],[0], color=C['thr'], lw=1.6,
               linestyle='--', label='Calibration Threshold'),
]
ax.legend(handles=leg,
          loc='lower right',
          fontsize=7.0,
          framealpha=0.93,
          edgecolor='#cccccc',
          ncol=2,
          handlelength=1.3,
          handletextpad=0.5,
          columnspacing=0.8,
          borderpad=0.7)

# ── Title ─────────────────────────────────────────────────────────────────────
fig.text(0.595, 0.97,
         'Figure 2. Research Orientation Typology Distribution\n'
         'in Trust and Educational AI Literature (N = 97)',
         ha='center', va='top',
         fontsize=11, fontweight='bold', color='#111',
         multialignment='center')

# ── Save ──────────────────────────────────────────────────────────────────────
out = ('/Volumes/External SSD/Projects/Trust-Calibration-Scaffolds-research/'
       'manuscript/figures/figure2_domain_typology.png')
plt.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
print(f'Saved: {out}')
plt.close()
