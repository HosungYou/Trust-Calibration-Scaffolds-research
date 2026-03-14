# Over-Reliance Audit: Structural vs Empirical Under-Reliance Analysis

**Date:** 2026-03-13
**Context:** Reviewer defense preparation — verifying that the universal under-reliance finding is empirical, not a structural artifact
**Decision Status:** Analysis complete, manuscript correction required

---

## 1. Motivation

All 6 MBC classes and all 4 LCGA classes exhibit negative mean calibration gaps (R_b < P) across all 10 temporal windows. Previous discussion documents (D11, D12) stated "Over-reliance (R_b > P) cases: none." This audit investigates whether this claim is:

- (A) A **structural/mathematical constraint** of the operationalization (i.e., over-reliance is impossible by construction), or
- (B) A **genuine empirical finding** (i.e., over-reliance is possible but rare)

If (A), the finding is trivial and indefensible. If (B), it is a substantive contribution.

---

## 2. Operationalization Review

### 2.1 Variable Definitions (from `phase1_build_timeseries.py`)

```python
R_b(τ) = n_adaptive / n_episodes       # adaptive episodes / total episodes
P(τ)   = total_correct / total_questions  # correct answers / total questions
Gap(τ) = R_b(τ) - P(τ)
```

### 2.2 Denominator Analysis

| Variable | Numerator | Denominator |
|----------|-----------|-------------|
| R_b | adaptive_offer episodes | All episodes (diagnosis, sprint, adaptive, etc.) |
| P | Correct question responses | All question-answering episodes |

The denominators differ: R_b includes non-question episodes (e.g., lectures, reviews), while P counts only question episodes. However, the ratio of n_questions/n_episodes has:
- Mean: 1.05
- Median: 1.00

This near-unity ratio means the denominator mismatch creates **negligible structural bias**. Standardizing R_b's denominator to n_questions would increase over-reliance observations from 765 to ~850 — a marginal change.

### 2.3 Theoretical Constraint Check

For R_b > P, a student would need:

```
(adaptive episodes / total episodes) > (correct answers / total questions)
```

Example: A student with 100 total episodes, 40 adaptive, 45 correct out of 100 questions:
- R_b = 40/100 = 0.40
- P = 45/100 = 0.45
- Gap = -0.05 (under-reliance)

Example: A student with 100 total episodes, 50 adaptive, 30 correct out of 100 questions:
- R_b = 50/100 = 0.50
- P = 30/100 = 0.30
- Gap = +0.20 (**over-reliance**)

**Conclusion: Over-reliance is mathematically possible.** There is no structural ceiling preventing R_b > P.

---

## 3. Empirical Evidence: Over-Reliance EXISTS

### 3.1 Observation-Level Analysis (N = 45,680 student-windows)

| Metric | Value |
|--------|-------|
| Observations with R_b > P | **765 / 45,680 (1.67%)** |
| Students with ≥1 over-reliance window | **581 / 4,568 (12.7%)** |
| Maximum positive Gap | **+0.78** |
| Mean positive Gap (when R_b > P) | +0.12 |

### 3.2 Temporal Distribution

| Window | % observations with R_b > P |
|:------:|:---------------------------:|
| 1 | 0.4% |
| 2 | 1.0% |
| 3 | 1.4% |
| 4 | 1.6% |
| 5 | 1.7% |
| 6 | 1.7% |
| 7 | 1.9% |
| 8 | 2.0% |
| 9 | 2.2% |
| 10 | **2.4%** |

Over-reliance prevalence increases over time as R_b rises (mean R_b: 0.048 → 0.166 across windows).

### 3.3 Profile of Over-Reliance Students

| Metric | Over-reliance (≥1 window, N=581) | Others (N=3,987) |
|--------|:------:|:------:|
| Mean adaptive ratio | **0.172** | 0.133 |
| Mean overall accuracy | **0.512** | 0.590 |
| Mean R_b (all windows) | **0.189** | 0.119 |

Over-reliance students have:
- **Higher** adaptive engagement (more AI use)
- **Lower** overall accuracy (weaker performance)

This profile is **theoretically consistent**: over-reliance occurs when learners rely on AI more than their performance warrants (high R_b + low P).

---

## 4. Why Over-Reliance Doesn't Appear at the CLASS MEAN Level

Despite 1.67% of observations showing over-reliance, no class mean trajectory crosses R_b = P. This is because:

1. **Scale mismatch**: R_b median (0.126) is ~4.7x lower than P median (0.590). Even with the ≥0.10 adaptive ratio filter, most students use adaptive content for only ~13% of episodes, while achieving ~58% accuracy. The "baseline gap" is approximately -0.46.

2. **Averaging effect**: Individual over-reliance windows (1.67%) are distributed across all 6 classes rather than concentrated in one. When averaged within a class of hundreds or thousands of students, a few over-reliance observations are overwhelmed by the dominant under-reliance pattern.

3. **Platform design**: Santa's adaptive_offer system presents AI-recommended content as one option among many (diagnosis, sprint, review_quiz, etc.). The platform does not force or strongly promote adaptive content, structurally limiting the maximum achievable R_b for most students.

---

## 5. Corrections Required

### 5.1 Previous Inaccurate Statements

| Document | Statement | Correction |
|----------|-----------|------------|
| D11, Section 1.2 | "Over-reliance (R_b > P) cases: none" | Over-reliance exists in 1.67% of observations (765/45,680) |
| D10, Section 9.3 | Implied no over-reliance | Should note individual-level over-reliance |

### 5.2 Manuscript Correction (draft_v2.md)

**Current text (Section 5.4, "The Dominance of Under-Reliance"):**
> "Even Class 6, with the highest reliance levels, maintained a gap near zero rather than crossing into over-reliance territory."

**Revised text:**
> "At the individual observation level, over-reliance (R_b > P) was observed in 1.67% of student-window observations, spanning 12.7% of students. However, no class mean trajectory crossed into over-reliance territory. Students who exhibited over-reliance windows were characterized by higher adaptive engagement and lower accuracy — a profile consistent with theoretical predictions of over-reliance as high AI dependence paired with low personal competence. The rarity of over-reliance at the aggregate level, despite its structural possibility, strengthens the conclusion that under-reliance is the dominant behavioral pattern in educational AI contexts."

### 5.3 Figure 4 Phase Portrait Correction

**Current subtitle:**
> "All classes remain in under-reliance zone (R_b < P)."

**Revised subtitle:**
> "All class means remain in under-reliance zone (R_b < P). Individual-level over-reliance observed in 1.67% of observations."

---

## 6. Implications for the Paper

### 6.1 This Finding STRENGTHENS the Paper

| If over-reliance were... | Implication |
|--------------------------|-------------|
| **Structurally impossible** | "Under-reliance dominance" would be trivial — a measurement artifact |
| **Possible but rare (actual finding)** | "Under-reliance dominance" is a genuine empirical discovery |

The fact that over-reliance CAN occur but almost never does at the trajectory level is a **stronger claim** than if it simply couldn't occur.

### 6.2 Construct Validity Support

The profile of over-reliance students (high adaptive use, low accuracy) matches theoretical predictions perfectly. This means:
- R_b and P are measuring constructs that can produce both over- and under-reliance
- The gap between them captures meaningful behavioral variation
- The operationalization is not structurally biased toward one direction

### 6.3 Reviewer Defense

**Anticipated attack:** "Your measures make over-reliance impossible, so finding under-reliance is trivial."

**Defense:** "Over-reliance is both mathematically possible and empirically observed at the individual level (1.67% of observations, 12.7% of students). Students exhibiting over-reliance show the theoretically predicted profile of high AI engagement and low accuracy. The dominance of under-reliance at the trajectory class level is therefore an empirical finding, not a structural artifact."

---

## 7. Decision Record

| Date | Decision |
|------|----------|
| 2026-03-13 | Over-reliance audit initiated to verify structural vs. empirical basis |
| 2026-03-13 | **Finding: Over-reliance is structurally possible and empirically present (1.67%)** |
| 2026-03-13 | Previous "no over-reliance" statements identified as inaccurate — correction required |
| 2026-03-13 | Manuscript Section 5.4 and Figure 4 subtitle to be updated |
| 2026-03-13 | Finding strengthens construct validity and reviewer defense |
