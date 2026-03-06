# TCRS: Trust Calibration Readiness Scale Development

## Paper 2 of the Trust Calibration Research Program

**Title (working):** Trust Calibration in Educational AI: A Process Model and Scale Development

**Relationship to Paper 1 (SLR):**
Paper 1 ("The Calibration Gap") identified that 83.5% of 97 studies fall below the calibration threshold. Paper 2 develops a measurement instrument for learner-side trust calibration readiness.

## Process Model

Calibration is a process, not a trait:

```
Metacognition (Winne, 1998)     → "Where am I?" — awareness of own trust state
        ↓
Trust Evaluation (Lee & See, 2004) → "Am I over/under-trusting?" — evaluate trust appropriateness
        ↓
Human Agency (Bandura, 2001)    → "Adjust" — active regulation toward optimal
        ↓
Calibration (Outcome)           → Appropriate trust = optimal point
```

## Scale Structure (48 items → target 18-24 after EFA)

| Subscale | Process Stage | Items | Response Format |
|----------|--------------|-------|-----------------|
| Calibration Awareness (CA-Aw) | Recognition | 16 | 7-point Agree-Disagree |
| Calibration Judgment (CA-Jd) | Evaluation | 16 | 7-point Agree-Disagree |
| Calibration Action (CA-Ac) | Regulation | 16 | 7-point Never-Always |

## Current Status

- [x] Process model development
- [x] Literature review (16+ existing scales mapped)
- [x] Expert critique synthesis (A3, D4, C1)
- [x] Item pool development (48 items, 9 facets)
- [x] Figure 1: Trust Calibration Process Model
- [x] Manuscript draft v1 (pre-data collection)
- [x] Diverga multi-agent coherence assessment (A3, A2, A5, F1)
- [x] Manuscript draft v2 (13 revisions based on Diverga assessment)
- [x] Figure 1 v2 (feedback loop, Trust Evaluation relabel, readiness annotation)
- [ ] Expert panel (CVI) ← NEXT
- [ ] Cognitive interviews
- [ ] Pilot test
- [ ] OSF preregistration
- [ ] Study 1: EFA (N=300-350)
- [ ] Study 2: CFA + validity (N=300-350)

## Methodology

- Study 1: EFA (N=300-350, online survey)
- Study 2: CFA + convergent/discriminant validity (N=300-350, online survey)
- No experiment, no AI system construction required

## Directory Structure

```
AALS-Scale-Development/
├── README.md
├── discussion/
│   ├── 01_Conceptualization — 3D framework and initial scale design
│   ├── 02_Literature_Review — AI literacy scales landscape (16+ scales)
│   ├── 03_Expert_Critique — Feasibility critique (A3, D4, C1)
│   ├── 04_Process_Model — Process model and scale architecture
│   ├── 05_Item_Pool — Initial 42-item pool
│   ├── 06_Item_Revision — D4 review and revised 48-item pool
│   ├── 07_Roadmap — Next steps and timeline
│   ├── 08_Diverga_Review — Multi-agent coherence assessment
│   └── 09_Diverga_Revision — Manuscript revision based on assessment
├── manuscript/
│   ├── draft_v1_TCRS.md — Initial pre-data manuscript draft
│   ├── draft_v2_TCRS.md — Revised draft (13 changes from Diverga review)
│   └── TCRS_Theoretical_Background_APA7.docx — APA 7th Word document
├── scripts/
│   ├── generate_figure1_v2.py — Figure 1 generation (matplotlib)
│   └── generate_tcrs_word.py — DOCX generation (python-docx)
└── figures/
    ├── Figure_1_Trust_Calibration_Process_Model.png — v1
    ├── Figure_1_Trust_Calibration_Process_Model_v2.png — v2 (current)
    ├── AALS_Research_Design.png
    ├── Framework_Scale_Connection.png
    └── Process_Model_Comparison.png
```
