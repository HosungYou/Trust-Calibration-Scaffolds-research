"""
Generate Figure 2: Research Design Flowchart
for the TCRS Scale Development Paper.

Shows the 5-phase scale development process as a vertical flowchart
with color-coded phases and key outputs.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "figures",
)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Figure_2_Research_Design_Flowchart.png")

# Phase definitions: (phase_num, title, output_text, color)
COLOR_THEORETICAL = "#FFF9DB"       # light yellow
COLOR_THEORETICAL_EDGE = "#D4A843"
COLOR_QUALITATIVE = "#FFE8CC"       # light orange
COLOR_QUALITATIVE_EDGE = "#D48A3C"
COLOR_QUANTITATIVE = "#D6EAF8"      # light blue
COLOR_QUANTITATIVE_EDGE = "#5B9BD5"

PHASES = [
    {
        "num": 1,
        "title": "Construct Definition\n& Item Generation",
        "output": "48 initial items\n(16 per subscale)",
        "fill": COLOR_THEORETICAL,
        "edge": COLOR_THEORETICAL_EDGE,
        "sample": None,
    },
    {
        "num": 2,
        "title": "Expert Panel Review",
        "output": "I-CVI \u2265 .78\nS-CVI/Ave \u2265 .90",
        "fill": COLOR_QUALITATIVE,
        "edge": COLOR_QUALITATIVE_EDGE,
        "sample": None,
    },
    {
        "num": 3,
        "title": "Cognitive Interviews",
        "output": "Item refinement",
        "fill": COLOR_QUALITATIVE,
        "edge": COLOR_QUALITATIVE_EDGE,
        "sample": None,
    },
    {
        "num": 4,
        "title": "Study 1: EFA",
        "output": "Factor structure\nN = 300\u2013350",
        "fill": COLOR_QUANTITATIVE,
        "edge": COLOR_QUANTITATIVE_EDGE,
        "sample": "Independent Sample 1",
    },
    {
        "num": 5,
        "title": "Study 2: CFA + Validity",
        "output": "Confirmation\nN = 400\nTest\u2013retest n = 80\u2013100",
        "fill": COLOR_QUANTITATIVE,
        "edge": COLOR_QUANTITATIVE_EDGE,
        "sample": "Independent Sample 2",
    },
]

# Layout constants
FIG_W, FIG_H = 8, 10
BOX_W = 3.2          # phase box width (data coords)
BOX_H = 0.95         # phase box height
OUTPUT_W = 2.6       # output box width
OUTPUT_H_BASE = 0.85 # output box base height (grows with text lines)
Y_TOP = 8.8          # top of first box
Y_SPACING = 1.65     # vertical distance between box centres
ARROW_GAP = 0.08     # gap between box edge and arrow tip
X_CENTER = 3.2       # centre x of phase boxes
X_OUTPUT = 6.6       # centre x of output boxes

# Font sizes
FONT_PHASE_NUM = 10
FONT_PHASE_TITLE = 10.5
FONT_OUTPUT = 9.5
FONT_SAMPLE = 8.5
FONT_LEGEND = 9

# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------

def draw_rounded_box(ax, x_center, y_center, w, h, facecolor, edgecolor,
                     linewidth=1.3, zorder=2):
    """Draw a rounded rectangle centred at (x_center, y_center)."""
    box = FancyBboxPatch(
        (x_center - w / 2, y_center - h / 2), w, h,
        boxstyle="round,pad=0.12",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.add_patch(box)
    return box


def draw_arrow(ax, x0, y0, x1, y1, color="#555555", lw=1.5):
    """Draw a straight arrow between two points."""
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            shrinkA=0,
            shrinkB=0,
        ),
        zorder=1,
    )


# ---------------------------------------------------------------------------
# Build figure
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W + 1.5)
ax.set_ylim(0, FIG_H + 1.6)
ax.set_aspect("equal")
ax.axis("off")

# Title
ax.text(
    (FIG_W + 1.5) / 2, FIG_H + 1.25,
    "Figure 2. Research Design Flowchart: TCRS Scale Development",
    ha="center", va="center",
    fontsize=12.5, fontweight="bold",
    family="serif",
)

# Draw phases
y_positions = []
for i, phase in enumerate(PHASES):
    y = Y_TOP - i * Y_SPACING
    y_positions.append(y)

    # --- Phase box ---
    draw_rounded_box(ax, X_CENTER, y, BOX_W, BOX_H,
                     phase["fill"], phase["edge"], linewidth=1.6)

    # Phase number label
    ax.text(
        X_CENTER, y + 0.22,
        f"Phase {phase['num']}",
        ha="center", va="center",
        fontsize=FONT_PHASE_NUM, fontweight="bold",
        color="#333333", family="serif",
    )
    # Phase title
    ax.text(
        X_CENTER, y - 0.15,
        phase["title"],
        ha="center", va="center",
        fontsize=FONT_PHASE_TITLE,
        color="#222222", family="serif",
        linespacing=1.15,
    )

    # --- Output box ---
    n_lines = phase["output"].count("\n") + 1
    out_h = OUTPUT_H_BASE + max(0, (n_lines - 2)) * 0.22
    draw_rounded_box(ax, X_OUTPUT, y, OUTPUT_W, out_h,
                     "#F8F8F8", "#AAAAAA", linewidth=1.0)
    ax.text(
        X_OUTPUT, y,
        phase["output"],
        ha="center", va="center",
        fontsize=FONT_OUTPUT,
        color="#333333", family="serif",
        linespacing=1.25,
    )

    # --- Horizontal connector: phase box -> output box ---
    x_start = X_CENTER + BOX_W / 2 + 0.05
    x_end = X_OUTPUT - OUTPUT_W / 2 - 0.05
    draw_arrow(ax, x_start, y, x_end, y, color="#999999", lw=1.2)

    # --- Sample annotation (Studies 1 & 2) ---
    if phase["sample"]:
        ax.text(
            X_CENTER, y - BOX_H / 2 - 0.18,
            phase["sample"],
            ha="center", va="top",
            fontsize=FONT_SAMPLE,
            fontstyle="italic",
            color="#555555", family="serif",
        )

# Vertical arrows between phase boxes
for i in range(len(PHASES) - 1):
    y_from = y_positions[i] - BOX_H / 2 - ARROW_GAP
    y_to = y_positions[i + 1] + BOX_H / 2 + ARROW_GAP
    draw_arrow(ax, X_CENTER, y_from, X_CENTER, y_to, color="#555555", lw=1.8)

# --- Bracket / brace annotations for category labels ---
# We place small labels on the left side to group phases by category.

def draw_bracket_label(ax, y_top, y_bot, label, x=1.05):
    """Draw a vertical bracket with a label on the left."""
    bracket_x = x
    text_x = x - 0.35
    mid_y = (y_top + y_bot) / 2

    # Vertical line
    ax.plot(
        [bracket_x, bracket_x], [y_bot, y_top],
        color="#888888", lw=1.2, solid_capstyle="round", zorder=1,
    )
    # Top tick
    ax.plot(
        [bracket_x, bracket_x + 0.15], [y_top, y_top],
        color="#888888", lw=1.2, solid_capstyle="round", zorder=1,
    )
    # Bottom tick
    ax.plot(
        [bracket_x, bracket_x + 0.15], [y_bot, y_bot],
        color="#888888", lw=1.2, solid_capstyle="round", zorder=1,
    )
    # Label
    ax.text(
        text_x, mid_y, label,
        ha="center", va="center",
        fontsize=8.5, color="#666666",
        family="serif", rotation=90,
        fontstyle="italic",
    )


# Phase 1: Theoretical
draw_bracket_label(
    ax,
    y_positions[0] + BOX_H / 2,
    y_positions[0] - BOX_H / 2,
    "Theoretical",
)

# Phases 2-3: Qualitative Validation
draw_bracket_label(
    ax,
    y_positions[1] + BOX_H / 2,
    y_positions[2] - BOX_H / 2,
    "Qualitative\nValidation",
)

# Phases 4-5: Quantitative Validation
draw_bracket_label(
    ax,
    y_positions[3] + BOX_H / 2,
    y_positions[4] - BOX_H / 2,
    "Quantitative\nValidation",
)

# --- Legend ---
legend_y = 0.55
legend_x_start = 1.8
legend_spacing = 2.8
legend_items = [
    ("Theoretical", COLOR_THEORETICAL, COLOR_THEORETICAL_EDGE),
    ("Qualitative Validation", COLOR_QUALITATIVE, COLOR_QUALITATIVE_EDGE),
    ("Quantitative Validation", COLOR_QUANTITATIVE, COLOR_QUANTITATIVE_EDGE),
]

for idx, (label, fc, ec) in enumerate(legend_items):
    lx = legend_x_start + idx * legend_spacing
    rect = FancyBboxPatch(
        (lx - 0.25, legend_y - 0.15), 0.5, 0.3,
        boxstyle="round,pad=0.05",
        facecolor=fc, edgecolor=ec, linewidth=1.2,
    )
    ax.add_patch(rect)
    ax.text(
        lx + 0.45, legend_y,
        label,
        ha="left", va="center",
        fontsize=FONT_LEGEND, color="#444444",
        family="serif",
    )

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
fig.tight_layout(pad=0.5)
fig.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Figure saved to: {OUTPUT_FILE}")
