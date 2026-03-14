# Figure 4 Redesign: 3D Plot to 2D Phase Portrait

**Date:** 2026-03-13
**Decision Context:** Figure clarity and communication effectiveness for CHB submission
**Participants:** Hosung You (PI), Claude (Research AI)

---

## Context

- Paper 4 targets Computers in Human Behavior (CHB) journal
- Figure 4 was originally a 3D plot in R_b x P x tau space showing 6 empirical trajectory classes
- The 3D version had annotations and velocity vectors but was problematic

---

## Problem with Original 3D Figure

1. **Annotation overlap**: C1, C2, C3 theory labels completely overlapped at the top endpoint cluster where trajectories converge
2. **3D perspective reduced readability**: Trajectories crossed and overlapped, making individual class identification difficult
3. **Velocity arrows added visual noise**: Arrows merged with other trajectories, making direction interpretation impossible
4. **tau axis information was limited**: Z-axis in 3D is inherently less readable than either x or y in 2D
5. **The 3D added complexity without proportional information gain**: Time (tau) as z-axis did not add information that could not be encoded differently

---

## Decision: 2D R_b x P Phase Portrait

Replaced the 3D plot with a 2D phase portrait that:

- **X-axis:** Behavioral Reliance R_b(tau)
- **Y-axis:** Performance P(tau)
- **Time (tau)** encoded as **color gradient** (light=early to dark=late) and **directional arrows** at tau=3, 6, 9
- **R_b = P diagonal** as "perfect calibration" reference line
- **Under-reliance zone** (R_b < P) shaded in light blue
- **Theory-empirical mapping annotations** at each class endpoint
- **Start markers** (open circle) and **end markers** (filled circle)

---

## Rationale

1. **Directly communicates the core theoretical claim**: Convergence toward vs. divergence from calibration is visible as distance from the R_b = P diagonal
2. **No annotation overlap**: 2D allows precise positioning of labels with leader lines
3. **Time encoding via color gradient is intuitive**: Readers naturally associate lighter=earlier, darker=later
4. **Phase portraits are established in dynamics literature**: Natural representation for trajectory analysis
5. **All 6 class patterns clearly distinguishable**:
   - C4 (Stagnant): Barely moves from upper-left -- true stagnation
   - C6 (Self-Correcting): Dramatic rightward movement then reversal -- clearly self-correcting
   - C5 (Escalating): Rapid rightward expansion -- escalating reliance
   - C1-C3 (Convergent): Progressive diagonal movement with different speeds

---

## What Was Lost

- Explicit tau axis visualization (mitigated by color gradient + arrows)
- 3D visual novelty (but novelty does not equal clarity)

---

## Files

- **Generator script:** `figures/generate_figure4_phase_portrait.py`
- **Output:** `figures/Figure_4_3D_Theory_vs_Empirical.png` (filename kept for compatibility with Word generator)
- **Previous 3D generator:** `figures/generate_figure4_3d.py` (preserved for reference)

---

## Impact on Manuscript

- Figure 4 caption in `generate_final_word.py` FIGURE_CAPTIONS should be reviewed
- The manuscript text in `draft_v2.md` referencing "3D" should be updated to "phase portrait"
- Word document regenerated: `Paper4_APA7th_FINAL.docx` (1,218 KB)
