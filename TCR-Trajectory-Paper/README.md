# Trust Calibration Trajectories in AI-Assisted Learning

**Paper 4 of the Trust Calibration Research Program**

**Working Title:** How Learners Calibrate Trust in AI: Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System

**Type:** Empirical (Secondary Data Analysis)
**Author:** Hosung You
**Target Journal:** Computers & Education (IF ~12.0)

## Core Question

> Do learners follow qualitatively distinct Trust Calibration trajectories when interacting with an AI tutoring system — and if so, do these match the theoretically predicted patterns (convergent, oscillating, stagnant)?

## Research Questions

| RQ | Question | Method |
|----|----------|--------|
| RQ1 | How many trajectory types exist? | Growth Mixture Modeling |
| RQ2 | Do predicted patterns (convergent/oscillating/stagnant) emerge? | GMM vs theory |
| RQ3 | Can early behavior predict trajectory type? | Multinomial logistic regression |
| RQ4 | Do trajectory types differ in learning outcomes? | ANOVA / Kruskal-Wallis |

## Data

| Dataset | Role | N | Trust Measure |
|---------|------|---|---------------|
| **EdNet KT3** | Primary | ~68,000 students | Behavioral proxy (adaptive_offer compliance, explanation depth) |
| Rittenberg et al. (2024) | Cross-validation | 147 | VAS 0–100 (30 timepoints) |
| Zouhar et al. (2023) | Cross-validation | 332 | Betting behavior (56 trials) |
| Lu & Yin (2021) | Cross-validation | ~300 | 7-point self-report + behavioral |

## Technical Stack

- **Python 3.12:** Data wrangling (pandas), visualization (matplotlib), prediction (scikit-learn)
- **R 4.5.2:** Growth Mixture Modeling (mclust, tidyLPA, lcmm)
- **Interface:** Python → CSV → R (subprocess) → CSV → Python

## Research Program Context

```
Paper 1 (SLR): "What is the problem?"     → Calibration Gap
Paper 2 (Scale): "How to measure?"         → TCRS (Aw → Jd → Ac)
Paper 3 (Conceptual): "Why does it matter?" → TCR = Educational Competency
Paper 4 (THIS): "Does it actually happen?" → Trajectory Types (Empirical)
```

## Status

- [x] Dataset identification & verification
- [x] EdNet KT3 full download (297,915 students, 4.2GB)
- [x] Data profiling & sample analysis
- [x] Analysis plan with visual aids (Discussion 08)
- [ ] Phase 1: Data wrangling (Python)
- [ ] Phase 2: GMM/LCGA (R)
- [ ] Phase 3: Validation & outcomes
- [ ] Manuscript draft
- [ ] Submission to C&E
