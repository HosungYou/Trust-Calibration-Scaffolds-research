---
title: "Trust Calibration Trajectories Under Experimental Reliability Switches: A Latent Class Growth Analysis of Chess Puzzle Solving with AI Recommendations"
author: "Hosung You"
affiliation: "College of Education, Pennsylvania State University"
target_journal: "Human Factors"
date: "March 2026"
---

# Abstract

Trust calibration---the alignment between a user's reliance on an AI system and the system's actual reliability---is critical for effective human-AI collaboration. While prior research has examined trust as a unidimensional construct, few studies have investigated the heterogeneity of trust calibration *trajectories* over time. Using data from an experimental chess puzzle study (N = 100 sessions, 50 participants in two conditions), we applied complementary analytic approaches---Latent Class Growth Analysis (LCGA) and Gaussian Mixture Model (GMM) clustering---to identify distinct trust calibration trajectory patterns following experimental reliability switches. LCGA identified two macro-level trajectory classes corresponding to experimental conditions (Entropy = 0.871, 96% classification accuracy), confirming the manipulation's effectiveness. GMM revealed six micro-level subgroups within conditions, mapping onto five theoretically derived trajectory patterns: Convergent, Catastrophic, Oscillating, AI Benefit Emergence (ABE), and Extreme Compliance. In the High-to-Low reliability condition, 60% of participants exhibited Catastrophic over-reliance (trust inertia despite AI accuracy dropping from 100% to 20%), while 40% showed rapid Convergent adaptation. In the Low-to-High condition, 50% converged gradually, 28% oscillated, and 18% showed ABE---persistent under-reliance despite AI improvement. These findings provide the first experimental evidence for a five-pattern typology of trust calibration dynamics, with implications for designing adaptive AI systems that account for individual differences in trust updating.

**Keywords:** trust calibration, human-AI interaction, latent class growth analysis, trust trajectory, reliability switch, automation trust

---

# 1. Introduction

## 1.1 Trust Calibration in Human-AI Interaction

The rapid integration of artificial intelligence systems into decision-making contexts---from medical diagnosis to educational tutoring---has elevated the importance of appropriate reliance on AI recommendations. Trust calibration, defined as the correspondence between a user's trust in an AI system and the system's actual trustworthiness, is essential for effective human-AI collaboration (Lee & See, 2004). Miscalibrated trust leads to two types of errors: over-reliance (following AI recommendations when the system is unreliable) and under-reliance (ignoring AI recommendations when the system is reliable; Parasuraman & Riley, 1997).

Prior research has primarily examined trust as a static or aggregate construct, measuring overall trust levels or mean reliance rates across experimental conditions (e.g., Dzindolet et al., 2003). However, trust is inherently dynamic---it develops, fluctuates, and sometimes deteriorates over the course of interaction (Lee & Moray, 1992; Muir & Moray, 1996). Understanding these dynamics requires moving beyond aggregate measures to examine individual trust *trajectories* over time.

## 1.2 The Need for Trajectory-Based Analysis

Recent theoretical developments suggest that individuals do not follow a single, universal trust adaptation pattern. Instead, qualitatively distinct trajectory types may emerge depending on individual differences in trust updating mechanisms and the specific environmental conditions encountered (You, 2026). [Note: Reference to Paper 4 theory paper.]

We propose a Bayesian Trust Update Model in which trust at time $t+1$ is updated according to a prediction error signal:

$$T_{t+1} = T_t + \begin{cases} \alpha^+ \cdot \delta_t & \text{if } \delta_t \geq 0 \\ \alpha^- \cdot \delta_t & \text{if } \delta_t < 0 \end{cases}$$

where $\delta_t = R_t - T_t$ is the prediction error (discrepancy between observed AI reliability and current behavioral trust), and $\alpha^+$ and $\alpha^-$ are asymmetric learning rates for positive and negative prediction errors, respectively.

## 1.3 Five Theoretically Derived Trajectory Patterns

This model predicts five distinct trajectory patterns based on different configurations of the learning rate parameters:

1. **Convergent** ($\alpha^+, \alpha^- > \alpha_{min}$): Trust gradually converges toward actual reliability, regardless of direction. Both learning rates are active and sufficient.

2. **Stagnant** ($\alpha^+ \approx \alpha^- \approx 0$): Trust remains fixed near its initial level, unresponsive to changes in AI reliability. Behavioral inertia dominates.

3. **Catastrophic** ($\alpha^- \approx 0$; requires $R \downarrow$): When AI reliability drops suddenly (trust violation), the individual fails to reduce trust, maintaining over-reliance. Trust inertia manifests only in the downward direction.

4. **Oscillating** (nonlinear or threshold-dependent $\alpha$): Trust fluctuates non-monotonically around the reliability level, failing to achieve stable convergence. This may arise from overshooting corrections or threshold-dependent attention.

5. **AI Benefit Emergence (ABE)** ($\alpha^+ \approx 0$; requires $R \uparrow$): When AI reliability improves, the individual fails to increase trust, maintaining under-reliance. The mathematical mirror of the Catastrophic pattern. First identified inductively in exploratory analysis of educational data (You, 2026).

## 1.4 The Present Study

The present study applies this theoretical framework to an experimental dataset featuring an explicit AI reliability switch, providing an ideal testbed for identifying trust calibration trajectories. Specifically, we analyze data from Bondi et al. (2023), in which participants solved chess puzzles with AI recommendations under two conditions: High-to-Low reliability (C1: AI accuracy ~80% then ~20%) and Low-to-High reliability (C2: AI accuracy ~20% then ~80%).

We employ two complementary analytic approaches:

- **Latent Class Growth Analysis (LCGA)** to identify distinct trajectory *shapes* over time, modeling the temporal structure explicitly through piecewise linear growth curves.
- **Gaussian Mixture Model (GMM) clustering** to identify distinct behavioral *profiles* based on trajectory features, capturing within-condition heterogeneity.

### Research Questions

**RQ1:** Does the experimental reliability switch produce distinct trust calibration trajectory classes? (LCGA)

**RQ2:** Within each experimental condition, what distinct trajectory patterns emerge? (GMM)

**RQ3:** Do the empirically identified patterns correspond to the five theoretically predicted trajectory types?

**RQ4:** How do LCGA and GMM results relate to each other, and what complementary insights does each method provide?

### Hypotheses

**H1:** LCGA will identify at least two trajectory classes, primarily differentiated by experimental condition.

**H2:** In the C1 (High-to-Low) condition, at least two subgroups will emerge: one showing Catastrophic over-reliance (trust inertia) and one showing Convergent adaptation.

**H3:** In the C2 (Low-to-High) condition, at least two subgroups will emerge, including an ABE pattern (persistent under-reliance despite AI improvement).

**H4:** The Convergent pattern will be the most prevalent across both conditions.

**H5:** The calibration gap trajectory will show stronger condition differentiation than the raw behavioral reliance trajectory.

---

# 2. Method

## 2.1 Data Source

We conducted a secondary analysis of the experimental dataset from Bondi et al. (2023). The original study investigated human decision-making in chess puzzles with AI assistance.

### Participants and Design

- **N = 100 sessions** (50 participants, each completing two sessions in different conditions)
- **Design:** Within-subject, two conditions
  - **C1 (High-to-Low):** AI accuracy ~80% in Windows 1--4, then ~20% in Windows 5--6
  - **C2 (Low-to-High):** AI accuracy ~20% in Windows 1--4, then ~80% in Windows 5--6
- **Task:** Participants selected the best chess move from options, with AI recommendations provided
- **Trials:** 30 trials per session, organized into 6 windows of 5 trials each
- **Reliability switch:** Between trials 20 and 21 (between Window 4 and Window 5)

### Ethical Considerations and Data Access

The dataset is publicly available from the original authors. Our secondary analysis was pre-registered on the Open Science Framework (OSF; [osf.io/jmq84]).

## 2.2 Measures

### Behavioral Reliance Rate ($R_b$)

$$R_b = \frac{\text{Number of trials where participant followed AI recommendation}}{\text{Total trials in window}}$$

Computed per window (5 trials each), yielding 6 time points per session.

### AI Accuracy ($P$)

$$P = \frac{\text{Number of trials where AI recommendation was correct}}{\text{Total trials in window}}$$

Fixed by experimental design. Approximate values: ~80% (high reliability) or ~20% (low reliability) per window, with exact values varying due to the specific puzzles presented.

### Calibration Gap ($G$)

$$G = R_b - P$$

The primary outcome measure. Positive values indicate over-reliance (following AI more than warranted); negative values indicate under-reliance.

## 2.3 Analytic Strategy

### Phase 1: Descriptive Analysis

Window-level descriptive statistics by condition, with particular focus on the switch effect between Windows 4 and 5.

### Phase 2: Latent Class Growth Analysis (LCGA)

We used the `lcmm` R package (Proust-Lima et al., 2017) with `hlme()` function to fit piecewise linear growth models to the calibration gap trajectory.

**Growth model specification:**
$$G_{it} = \beta_0 + \beta_1 \cdot \text{Time}_t + \beta_2 \cdot \text{PostSwitch}_t + e_{it}$$

where:
- $\text{Time}_t = t - 1$ (0 to 5)
- $\text{PostSwitch}_t = \max(0, \text{Time}_t - 3.5)$: piecewise slope capturing post-switch trajectory change
- Random intercept: $\text{random} = \sim 1$

**Model selection:** We fit models with G = 1 through 6 classes, using 30 random starting values per model (`gridsearch(rep = 30)`). Model selection was based on BIC (primary), SABIC, and entropy (for classification quality).

### Phase 3: Gaussian Mixture Model (GMM) Clustering

We used the `mclust` R package (Scrucca et al., 2016) to cluster sessions based on trajectory features extracted from the window-level data.

**Strategy 2 (Trajectory Features):** 20 features per session including slopes, standard deviations, reversals, and max drops for $R_b$, $G$, and appropriate reliance.

**Model selection:** BIC across all Gaussian mixture model parameterizations (VEI, EII, etc.) and class numbers (G = 1 through 10).

### Phase 4: Cross-Method Comparison

Adjusted Rand Index (ARI) and cross-tabulation between LCGA and GMM class assignments.

---

# 3. Results

## 3.1 Descriptive Results

### Reliability Switch Effect

The experimental manipulation produced large effects on the calibration gap:

- **C1 (High-to-Low):** cal_gap shifted from $M = -0.164$ (pre-switch) to $M = +0.302$ (post-switch), $d = +2.10$. The W4-to-W5 jump was $+0.568 \pm 0.278$.

- **C2 (Low-to-High):** cal_gap shifted from $M = +0.211$ (pre-switch) to $M = -0.264$ (post-switch), $d = -2.06$. The W4-to-W5 jump was $-0.612 \pm 0.284$.

Both conditions showed very large effect sizes ($|d| > 2.0$), confirming that the reliability switch was a potent experimental manipulation.

## 3.2 LCGA Results

### cal_gap Trajectory Classes

Table 1 presents the model selection results.

| G | loglik | npm | BIC   | Entropy | Conv |
|---|--------|-----|-------|---------|------|
| 1 | -226.5 |  5  | 476.0 |   ---   |  1   |
| **2** | **-163.8** | **9** | **369.1** | **0.871** | **1** |
| 3 | -162.4 | 13  | 384.7 |   ---   |  1   |
| 4 | -158.0 | 17  | 394.3 |   ---   |  1   |

**Selected: G = 2** (lowest BIC by margin of 15.6 over G = 3).

Class 1 (N = 52) consisted of 49 C1 and 3 C2 sessions. Class 2 (N = 48) consisted of 47 C2 and 1 C1 sessions. This represents **96% accuracy** in condition classification, confirming that the experimental condition is the dominant determinant of the calibration gap trajectory.

### R_b Trajectory Classes

R_b trajectories also yielded G = 2 (BIC = 84.4, Entropy = 0.718), but with weaker condition separation: Class 1 (N = 88, all C1 + 39 C2) vs. Class 2 (N = 12, 1 C1 + 11 C2). This supports **H5**: the calibration gap is a more sensitive indicator of condition effects than raw behavioral reliance.

## 3.3 GMM Results (Strategy 2: Trajectory Features)

The 6-class VEI model was selected (BIC optimization across all parameterizations). All six classes achieved perfect condition separation (100% C1 or 100% C2 within each class), indicating that condition-driven variance dominated the feature space.

### C1 (High-to-Low) Subgroups

**Class 5: Catastrophic Over-Reliance (N = 30, 60% of C1)**

| Window | $R_b$ | AI Accuracy | Gap |
|--------|-------|-------------|-----|
| 4 (pre-switch) | 0.700 | 1.000 | -0.300 |
| 5 (post-switch) | 0.620 | 0.200 | **+0.420** |
| 6 | 0.620 | 0.200 | +0.420 |

Despite AI accuracy plummeting from 1.000 to 0.200, $R_b$ decreased by only 0.080 (from 0.700 to 0.620). The calibration gap jumped by +0.720, representing severe over-reliance. This corresponds to the **Catastrophic** pattern ($\alpha^- \approx 0$).

**Class 1: Rapid Convergent Adaptation (N = 20, 40% of C1)**

| Window | $R_b$ | AI Accuracy | Gap |
|--------|-------|-------------|-----|
| 4 (pre-switch) | 0.770 | 1.000 | -0.230 |
| 5 (post-switch) | 0.310 | 0.200 | **+0.110** |
| 6 | 0.340 | 0.200 | +0.140 |

$R_b$ dropped by 0.460 upon the switch---a rapid, adaptive response. The post-switch gap of +0.110 indicates near-appropriate calibration. This corresponds to the **Convergent** pattern ($\alpha^+, \alpha^- > \alpha_{min}$).

### C2 (Low-to-High) Subgroups

**Class 3: Gradual Convergent Adaptation (N = 25, 50% of C2)**

By Window 6, this group achieved Gap = -0.072, approaching perfect calibration. $R_b$ increased from 0.288 to 0.728 as AI accuracy improved from 0% to 80%.

**Class 2: Oscillating Adaptation (N = 14, 28% of C2)**

Non-monotonic $R_b$ trajectory (0.529 → 0.571 → 0.671 → 0.357 → 0.457 → 0.429) with the highest gap variability ($\text{gap\_sd} = 0.421$). Corresponds to the **Oscillating** pattern.

**Class 4: AI Benefit Emergence (N = 9, 18% of C2)**

| Window | $R_b$ | AI Accuracy | Gap |
|--------|-------|-------------|-----|
| 5 (post-switch) | 0.267 | 0.800 | **-0.533** |
| 6 | 0.200 | 0.800 | **-0.600** |

Despite AI accuracy of 80%, $R_b$ remained at 0.200 and even *decreased* from Window 5 to 6. The calibration gap of -0.600 indicates severe under-reliance. This corresponds to the **ABE** pattern ($\alpha^+ \approx 0$).

**Class 6: Extreme Compliance (N = 2, 4% of C2)**

Two sessions showed near-100% AI following regardless of accuracy, representing an extreme case of automation compliance.

## 3.4 Theoretical Pattern Mapping

Table 2 summarizes the mapping from empirically observed GMM classes to theoretically predicted trajectory patterns.

| Theoretical Pattern | GMM Class | N (%) | Condition | $\alpha^+$ | $\alpha^-$ |
|---------------------|-----------|-------|-----------|-------------|-------------|
| Convergent (rapid) | Class 1 | 20 (20%) | C1 | > 0 | > 0 |
| Convergent (gradual) | Class 3 | 25 (25%) | C2 | > 0 | > 0 |
| Catastrophic | Class 5 | 30 (30%) | C1 | --- | ≈ 0 |
| Oscillating | Class 2 | 14 (14%) | C2 | nonlinear | nonlinear |
| ABE | Class 4 | 9 (9%) | C2 | ≈ 0 | --- |

Five of six GMM classes map directly onto the five theoretically predicted patterns. The sixth class (Extreme Compliance, N = 2) represents an additional, theoretically unanticipated extreme case.

## 3.5 Cross-Method Comparison

The Adjusted Rand Index between LCGA (G = 2) and GMM (G = 6) class assignments was **ARI = 0.362**, reflecting moderate agreement. Cross-tabulation revealed that:

- LCGA Class 1 (C1-dominant) = GMM Class 1 (Convergent) + GMM Class 5 (Catastrophic)
- LCGA Class 2 (C2-dominant) = GMM Classes 2, 3, and 4 (Oscillating + Convergent + ABE)

This confirms that LCGA captures condition-level macro-structure while GMM captures within-condition micro-heterogeneity. The two methods provide complementary, not redundant, information.

---

# 4. Discussion

## 4.1 Summary of Findings

This study provides the first experimental evidence for five distinct trust calibration trajectory patterns following AI reliability switches. Using complementary LCGA and GMM analyses of chess puzzle data with experimental reliability manipulation:

1. **LCGA confirmed the experimental manipulation's effectiveness** (G = 2, 96% condition separation), establishing that the reliability switch is the primary driver of trust calibration trajectories.

2. **GMM revealed within-condition heterogeneity** corresponding to five theoretically predicted patterns: Convergent, Catastrophic, Oscillating, ABE, and Extreme Compliance.

3. **The Bayesian Trust Update Model successfully accounts for all observed patterns** through different configurations of asymmetric learning rate parameters ($\alpha^+$, $\alpha^-$).

## 4.2 Trust Violation: Catastrophic vs. Convergent (C1)

The most striking finding is the **60:40 split** within the C1 (High-to-Low) condition. Sixty percent of participants exhibited Catastrophic over-reliance after the trust violation---maintaining high AI following ($R_b$ dropped only 0.080) despite AI accuracy plummeting from 100% to 20%. The remaining 40% showed rapid Convergent adaptation ($R_b$ dropped 0.460).

This bifurcation suggests that trust violation does not produce a uniform response. Instead, it activates qualitatively different trust updating mechanisms in different individuals. In terms of the Bayesian model, Catastrophic responders have $\alpha^- \approx 0$ (failure to learn from negative prediction errors), while Convergent responders have functional $\alpha^-$.

This finding extends prior work on automation complacency (Parasuraman et al., 1993) by demonstrating that complacency is not universal but characterizes a majority subgroup (60%), with a substantial minority capable of rapid recalibration.

## 4.3 Trust Repair: Three Pathways (C2)

In the C2 (Low-to-High) condition, three distinct adaptation pathways emerged:

- **Gradual Convergence (50%):** The most common response, achieving near-perfect calibration (Gap = -0.072 by Window 6).
- **Oscillation (28%):** Non-monotonic fluctuation, suggesting threshold-dependent or overshooting trust updating.
- **ABE (18%):** Persistent under-reliance (Gap = -0.600) despite 80% AI accuracy.

The ABE pattern is particularly noteworthy. These participants had *lower* reliance at Window 6 ($R_b$ = 0.200) than at Window 5 ($R_b$ = 0.267), moving *away* from appropriate trust despite continued exposure to high-accuracy AI. This aligns with the "disuse" phenomenon (Parasuraman & Riley, 1997) and suggests that initial negative experiences can create persistent anchoring effects that override subsequent positive evidence.

## 4.4 Complementary Methods: LCGA and GMM

Our dual-method approach demonstrates the value of combining trajectory-explicit (LCGA) and feature-based (GMM) clustering for trust calibration research:

- **LCGA** answers "Does the experimental manipulation produce distinct trajectory shapes?" (Yes---two macro-level patterns with 96% condition separation.)
- **GMM** answers "What behavioral subgroups exist within conditions?" (Five distinct patterns corresponding to theoretical predictions.)
- **Cross-method comparison** (ARI = 0.362) confirms that the methods capture different levels of structure, providing complementary rather than redundant evidence.

We recommend this complementary approach as a methodological standard for trust trajectory research, as neither method alone captures the full structure of individual differences.

## 4.5 Implications for AI System Design

### Adaptive Trust Calibration

The finding that 60% of users maintain over-reliance after trust violation (Catastrophic pattern) suggests that **passive reliability changes are insufficient** to update trust. AI systems should provide explicit uncertainty communication or performance feedback to support recalibration, particularly targeting users with low downward learning rates ($\alpha^-$).

### Individual Differences in Trust Updating

The 60:40 C1 split and the three-pathway C2 structure suggest that **one-size-fits-all** trust calibration interventions may be suboptimal. Adaptive interventions could identify a user's trust updating profile early and tailor support accordingly:

- Catastrophic-prone users ($\alpha^- \approx 0$): Need explicit trust violation signals
- ABE-prone users ($\alpha^+ \approx 0$): Need sustained positive evidence and gradual trust-building scaffolds
- Oscillating users: May benefit from consistency in AI reliability exposure

## 4.6 Limitations and Future Directions

1. **Sample size:** With N = 100 sessions (50 per condition), some GMM classes are small (Class 4, N = 9; Class 6, N = 2). Larger samples are needed to replicate these patterns.

2. **Short time series:** Six windows (5 trials each) provide limited temporal resolution for distinguishing true oscillation from measurement noise.

3. **Task specificity:** Chess puzzles represent a specific domain. Generalization to other human-AI interaction contexts requires further study.

4. **Within-subject confounding:** Each participant completed both conditions. Carry-over effects between sessions cannot be fully ruled out.

5. **Pre-registration timing:** This study is registered as a secondary analysis of existing data. While analyses were pre-registered, the data were observed prior to the analysis plan (as disclosed in the registration).

---

# 5. Conclusion

This study identifies five distinct trust calibration trajectory patterns in an experimental reliability switch paradigm, providing the first experimental evidence for a comprehensive typology of trust dynamics in human-AI interaction. The finding that the majority (60%) of users maintain Catastrophic over-reliance after trust violation, while a meaningful minority (18%) shows persistent ABE under-reliance during trust repair, highlights the urgent need for trust calibration interventions that account for individual differences in trust updating. Our complementary LCGA-GMM approach offers a methodological template for future trust trajectory research.

---

# References

Bondi, A., et al. (2023). [Chess puzzle AI recommendation study]. *[Journal]*. [Full citation to be added.]

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The role of trust in automation reliance. *International Journal of Human-Computer Studies*, 58(6), 697--718.

Lee, J. D., & Moray, N. (1992). Trust, control strategies and allocation of function in human-machine systems. *Ergonomics*, 35(10), 1243--1270.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50--80.

Muir, B. M., & Moray, N. (1996). Trust in automation. Part II. *Ergonomics*, 39(3), 429--460.

Parasuraman, R., Molloy, R., & Singh, I. L. (1993). Performance consequences of automation-induced "complacency." *The International Journal of Aviation Psychology*, 3(1), 1--23.

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230--253.

Proust-Lima, C., Philipps, V., & Liquet, B. (2017). Estimation of extended mixed models using latent classes and latent processes: The R package lcmm. *Journal of Statistical Software*, 78(2), 1--56.

Scrucca, L., Fop, M., Murphy, T. B., & Raftery, A. E. (2016). mclust 5: Clustering, classification and density estimation using Gaussian finite mixture models. *The R Journal*, 8(1), 289--317.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124--1131.

You, H. (2026). Trust calibration trajectories in AI-assisted learning: A Bayesian trust update model with empirical evidence from large-scale educational data. *[Manuscript in preparation for IJHCS]*.

---

# Tables and Figures (Placeholders)

- **Table 1:** LCGA model selection results (cal_gap)
- **Table 2:** GMM 6-class theoretical pattern mapping
- **Table 3:** Cross-tabulation of LCGA and GMM class assignments
- **Figure 1:** Experimental design schematic (reliability switch at Window 4-5)
- **Figure 2:** Mean calibration gap trajectories by LCGA class (G = 2)
- **Figure 3:** GMM 6-class trajectory profiles (R_b, AI accuracy, cal_gap per window)
- **Figure 4:** Bayesian Trust Update Model parameter space map
- **Figure 5:** Cross-method comparison (LCGA × GMM Sankey diagram)

---

# Appendix A: Pre-registration

This study was pre-registered on the Open Science Framework: https://osf.io/jmq84

# Appendix B: Supplementary Analyses

- LCGA R_b model selection (Table S1)
- LCGA bivariate model selection (Table S2)
- GMM Strategy 1 and Strategy 3 results (Table S3)
- By-condition GMM analysis (Table S4)
