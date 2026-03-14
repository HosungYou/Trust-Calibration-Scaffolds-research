"""
Unified Figure Style Framework for Trust Calibration Trajectory Paper.

All figure generation scripts import from this module to ensure
consistent typography, colors, markers, line styles, and save settings
across all publication figures.

Design system based on:
- APA 7th Edition figure guidelines (no embedded titles)
- Tol (2021) colorblind-safe palette for MBC (6 classes)
- Wong (2011) colorblind-safe palette for LCGA (4 classes)
- CHB single-column width: ≤7 inches

References:
  Tol, P. (2021). Colour Schemes. SRON Technical Note, SRON/EPS/TN/09-002.
  Wong, B. (2011). Color blindness. Nature Methods, 8(6), 441.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path("/Volumes/External SSD/Projects/Research/Trust-Calibration-Scaffolds-research/TCR-Trajectory-Paper")
DATA_DIR = BASE / "analysis" / "outputs"
FIG_DIR = BASE / "figures"

# ── Typography ───────────────────────────────────────────────────────────────
FONT_FAMILY = 'serif'
FONT_SERIF = ['Times New Roman', 'Times', 'DejaVu Serif']
BASE_FONT_SIZE = 11
AXIS_LABEL_SIZE = 12
TICK_LABEL_SIZE = 11
LEGEND_FONT_SIZE = 9.5
PANEL_LABEL_SIZE = 13
ANNOTATION_SIZE = 9

# ── Layout ───────────────────────────────────────────────────────────────────
SINGLE_COL_WIDTH = 7.0    # inches (CHB single-column max)
DOUBLE_COL_WIDTH = 12.0   # inches (CHB two-panel max)
DPI = 300
SAVE_PAD = 0.15

# ── MBC Class Colors (Tol bright palette, colorblind-safe) ───────────────────
MBC_COLORS = {
    1: '#4477AA',  # blue
    2: '#228833',  # green
    3: '#EE6677',  # rose/red
    4: '#CCBB44',  # olive/yellow
    5: '#AA3377',  # purple
    6: '#66CCEE',  # cyan
}

# ── MBC Class Markers ───────────────────────────────────────────────────────
MBC_MARKERS = {
    1: 'o',  # circle
    2: 's',  # square
    3: '^',  # triangle up
    4: 'D',  # diamond
    5: 'v',  # triangle down
    6: 'P',  # plus (filled)
}

# ── MBC Class Line Styles ───────────────────────────────────────────────────
MBC_LINESTYLES = {
    1: '-',
    2: '-',
    3: '-',
    4: '-',
    5: '-',
    6: '-',
}

# ── MBC Class Labels ────────────────────────────────────────────────────────
MBC_LABELS = {
    1: "C1: Gradual Adopters (n=1,367)",
    2: "C2: Steady Calibrators (n=1,582)",
    3: "C3: Strong Calibrators (n=859)",
    4: "C4: High Performers, Low Reliance (n=451)",
    5: "C5: Heavy Adopters (n=240)",
    6: "C6: Early Heavy Users (n=69)",
}

# ── LCGA Class Colors (Wong palette, visually distinct from Tol) ────────────
LCGA_COLORS = {
    1: '#E69F00',  # amber/orange
    2: '#56B4E9',  # sky blue
    3: '#009E73',  # teal/green
    4: '#CC79A7',  # pink/mauve
}

# ── LCGA Class Markers ──────────────────────────────────────────────────────
LCGA_MARKERS = {
    1: 'o',  # circle
    2: 's',  # square
    3: '^',  # triangle up
    4: 'D',  # diamond
}

# ── LCGA Class Line Styles (redundant encoding) ─────────────────────────────
LCGA_LINESTYLES = {
    1: '-',     # solid
    2: '--',    # dashed
    3: '-.',    # dash-dot
    4: ':',     # dotted
}

# ── LCGA Class Labels ───────────────────────────────────────────────────────
LCGA_LABELS = {
    1: "LCGA-1: Stagnant Under-Reliance (n=2,662; 83.1%)",
    2: "LCGA-2: Near-Calibrated Fluctuators (n=75; 2.3%)",
    3: "LCGA-3: Convergent Learners (n=290; 9.1%)",
    4: "LCGA-4: AI Benefit Emergence (n=177; 5.5%)",
}

# ── ABE Figure Colors ───────────────────────────────────────────────────────
ABE_COLOR_P = '#1565C0'   # deep blue for P_adaptive
ABE_COLOR_R = '#C62828'   # deep red for R_b
ABE_COLOR_GAP = '#FFCDD2' # light red for shaded gap area
ABE_COLOR_TEXT = '#B71C1C' # dark red for gap annotations

# ── Prediction Figure Colors ─────────────────────────────────────────────────
PRED_COLOR_HIGHLIGHT = '#1565C0'  # deep blue for metacognitive features
PRED_COLOR_DEFAULT = '#B0BEC5'    # gray for other features
PRED_EDGE_HIGHLIGHT = '#0D47A1'
PRED_EDGE_DEFAULT = '#78909C'

# ── Shared Constants ─────────────────────────────────────────────────────────
WINDOWS = np.arange(1, 11)
LINE_WIDTH = 2.0
MARKER_SIZE = 7
EMPHASIS_LINE_WIDTH = 2.8
EMPHASIS_MARKER_SIZE = 8
GRID_ALPHA = 0.3
GRID_COLOR = 'gray'
GRID_LW = 0.5
REFERENCE_LINE_ALPHA = 0.6


def apply_style():
    """Apply the unified matplotlib rcParams for all figures."""
    plt.rcParams.update({
        'font.family': FONT_FAMILY,
        'font.serif': FONT_SERIF,
        'font.size': BASE_FONT_SIZE,
        'axes.labelsize': AXIS_LABEL_SIZE,
        'axes.titlesize': AXIS_LABEL_SIZE + 1,
        'xtick.labelsize': TICK_LABEL_SIZE,
        'ytick.labelsize': TICK_LABEL_SIZE,
        'legend.fontsize': LEGEND_FONT_SIZE,
        'figure.dpi': DPI,
        'savefig.dpi': DPI,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': SAVE_PAD,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.facecolor': 'white',
        'figure.facecolor': 'white',
        'axes.grid': False,
    })


def add_y_gridlines(ax):
    """Add light gray horizontal gridlines."""
    ax.yaxis.grid(True, color=GRID_COLOR, alpha=GRID_ALPHA, linewidth=GRID_LW)
    ax.set_axisbelow(True)


def add_x_gridlines(ax):
    """Add light gray vertical gridlines."""
    ax.xaxis.grid(True, color=GRID_COLOR, alpha=0.2, linewidth=GRID_LW)
    ax.set_axisbelow(True)


def save_figure(fig, filename, fig_dir=None):
    """Save figure as RGB PNG at publication DPI."""
    out_dir = fig_dir or FIG_DIR
    out_path = out_dir / filename
    fig.savefig(out_path, dpi=DPI, format='png',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    size_kb = out_path.stat().st_size / 1024
    print(f"Saved: {out_path}  ({size_kb:.0f} KB)")
    return out_path
