# Paper 4 Identity & Structure Decision Document

**Date:** 2026-03-12
**Decision Context:** Pre-manuscript finalization review
**Participants:** Hosung You (PI), Claude (Research AI)

---

## Decision Summary

### D1. Title & Method Label

**Decision:** Change "Growth Mixture Analysis" → "Model-Based Clustering"

**Rationale:**
- Actual analysis uses `mclust` (Scrucca et al., 2016) — wide-format multivariate Gaussian mixture model
- Traditional GMM (Muthén, 2004; Nagin, 2005) involves growth curves with latent classes (e.g., `lcmm`, `Mplus`)
- `lcmm` was attempted but failed due to zero-inflation in R_b (documented in Method 3.4.2)
- Using "Growth Mixture Analysis" in the title is methodologically inaccurate and invites reviewer criticism
- "Model-Based Clustering" accurately describes the `mclust` approach

**New Title (working):** "Patterns of AI Reliance Calibration Among Learners: A Model-Based Clustering Analysis of Behavioral Trajectories in an AI Tutoring System"

**Alternative:** May further refine to foreground the theoretical contribution:
"Behavioral Evidence for Trust Calibration Trajectory Theory: A Model-Based Clustering Analysis of AI Reliance Patterns in an Educational Platform"

---

### D2. Paper Identity / Framing

**Decision:** Option B — "Behavioral Evidence for Trust Calibration Theory"

**Framing:**
- The paper uses behavioral proxy (reliance) to test predictions derived from trust-in-automation theory
- Trust is the theoretical lens; reliance calibration is the empirical construct
- This positions the paper as a theory-testing contribution rather than a purely exploratory descriptive study
- Discussion explicitly bridges behavioral findings back to trust calibration implications

**Implementation:**
- Introduction: Frame as "testing whether theoretically predicted trust calibration dynamics are observable in behavioral reliance data"
- Method: Maintain "reliance calibration" as the measured construct
- Discussion: Bridge back to "trust calibration theory" — what behavioral patterns tell us about underlying trust processes
- Conclusion: "behavioral evidence consistent with / extending trust calibration theory"

---

### D3. LCGA — Promote to RQ

**Decision:** Consider promoting LCGA (Phase 2C) to a separate RQ

**Rationale:**
- Phase 2C LCGA provides direct trajectory modeling (gap over time), complementing the wide-format mclust approach
- LCGA maps more directly onto theoretical predictions (convergent, stagnant, divergent patterns)
- 4-class LCGA solution (83% Stagnant, 9% Convergent, 5.5% Divergent, 2.3% Oscillating) strengthens theory-empirical mapping
- Including both methods demonstrates robustness and triangulation
- Makes the paper methodologically stronger and addresses the "why not use actual growth modeling?" question proactively

**Proposed new RQ structure:**
- RQ1 (unchanged): How many distinct trajectory classes? → Model-based clustering (mclust 6-class)
- RQ2 (new): Does latent class growth analysis replicate the trajectory typology? → LCGA comparison
- RQ3 (was RQ2): Theory-empirical correspondence
- RQ4 (was RQ3): Early behavior prediction
- RQ5 (was RQ4): Outcome differences
- Plus: AI Benefit Emergence as a key finding (see D4)

**Note:** Exact RQ wording TBD pending PI confirmation.

---

### D4. AI Benefit Emergence (ABE) — Include as Discovery

**Decision:** Include ABE as a finding in Paper 4

**Rationale:**
- ABE was inductively discovered in Phase 2B (split performance operationalization)
- EdNet evidence: S2 Class 4 (n=256, 5.7%), P_adaptive 0.275→0.852, R_b 0.020→0.171, Gap −0.039→−0.601
- Represents a theoretically novel pattern: AI effectiveness increases but learner reliance lags behind
- Mirror opposite of Catastrophic pattern (same |α| asymmetry, opposite direction)
- Paper 4 has the larger sample (n=256 vs. Chess n=9), making it the more credible evidence base

**Implementation considerations:**
- Requires describing the alternative operationalization (P_adaptive vs P_non_adaptive) in Method
- Could be positioned as: (a) additional RQ, (b) within RQ3 (theory-empirical comparison), or (c) as a "supplementary finding"
- Need to balance additional complexity against manuscript length

**Trade-off with Paper 5:**
- Paper 5 also reports ABE (Chess n=9, gap=-0.600)
- Including ABE in Paper 4 establishes it as a Paper 4 discovery; Paper 5 then "confirms" it experimentally
- This is strategically advantageous: discovery (Paper 4) → experimental confirmation (Paper 5)

---

### D5. Hypothesis Restructuring

**Decision:** Remove H2b (oscillation), retain 3 hypotheses

**Rationale:**
- H2b (oscillating pattern) was "Not Supported" — no clear oscillation in any of the 6 classes
- 10-window temporal resolution is too coarse to detect oscillation
- Presenting a hypothesis only to reject it wastes space without adding value
- LCGA Class 2 (2.3%) shows weak oscillatory signal, but this is too marginal to support a hypothesis

**New hypothesis structure:**
- **H1:** ≥3 distinct trajectory classes will emerge (heterogeneity)
- **H2a:** At least one class will show convergent calibration (gap narrowing)
- **H2b:** At least one class will show stagnant calibration (gap constant)
- **H3 (was H3):** Early explanation-seeking predicts trajectory membership
- **H4 (was H4):** Convergent calibration associated with best learning outcomes

**Note on "+α":** The AI Benefit Emergence pattern constitutes the inductive "+α" — a pattern not predicted a priori but discovered empirically. This is reported as a finding, not as a hypothesis.

---

### D6. Target Journal

**Decision:** Choose among Human Factors, IJHCS, or Computers in Human Behavior

**Evaluation:**

| Criterion | Human Factors | IJHCS | CHB |
|-----------|:---:|:---:|:---:|
| Impact Factor | ~3.3 | ~5.4 | ~9.9 |
| Theory fit | Excellent | Good | Good |
| Method fit | Good (but prefers experimental) | Excellent | Excellent |
| Audience overlap with Paper 5 | HIGH (Paper 5 → HF) | Low | Low |
| Accepts observational/secondary data | Sometimes | Yes | Yes |
| Education angle | Weak | Moderate | Strong |
| Large-N behavioral analysis | Less common | Common | Common |

**Recommendation:** Computers in Human Behavior (CHB) or IJHCS — final decision pending PI input

**Reasoning against Human Factors:**
1. Paper 5 already targets Human Factors → publishing both there creates audience saturation
2. HF prefers experimental/controlled designs; observational secondary analysis of educational data is a weaker fit
3. Lower IF

**Reasoning for CHB:**
- Highest IF (~9.9), broader readership
- Regularly publishes trust-in-AI, behavioral pattern, and educational technology papers
- Accepts large-N observational studies
- Strong match for "behavioral evidence for theory" framing

**Reasoning for IJHCS:**
- More technical, HCI-focused readership
- Strong match for model-based clustering methodology
- Moderate IF but high prestige in HCI

---

### D7. Tables & Figures Plan

**Decision:** Follow proposed structure (5 Tables + 3-4 Figures)

| Location | Element | Content |
|----------|---------|---------|
| After Method | **Table 1** | Descriptive stats (10 windows × R_b, P, Gap) |
| RQ1 Results | **Table 2** | GMM model comparison (BIC, entropy, class sizes) |
| RQ1 Results | **Figure 1** | 6-class mean trajectories (R_b + P, 2-panel or 6-panel) |
| RQ1 Results | **Figure 2** | Gap trajectories by class |
| RQ3 (Theory-Empirical) | **Figure 3** | Theory vs Empirical overlay |
| RQ4 (Prediction) | **Table 3** | Multinomial logistic regression coefficients |
| RQ5 (Outcomes) | **Table 4** | Class outcome differences (accuracy, improvement, post-hoc) |
| Sensitivity | **Table 5** | Sensitivity analysis summary |

**Notes:**
- If LCGA is promoted to RQ, add Figure/Table for LCGA results
- Trust-Reliability Matrix (current Figure 1) moved to supplementary or removed (already in Paper 3)
- Theoretical 3D trajectory figure: evaluate whether needed or redundant

---

### D8. Paper 5 Reference

**Decision:** Do not reference Paper 5 in Paper 4

**Rationale:**
- Paper 4 publishes first and must stand alone
- No "(Authors, in preparation)" references — reviewers may view this skeptically
- Paper 5 will reference Paper 4; not the reverse
- Future research section can mention "experimental validation" generically without citing Paper 5

---

## Outstanding Questions for PI

1. **Journal final choice:** CHB vs IJHCS? (Recommendation: CHB for higher impact and broader reach)
2. **LCGA RQ structure:** New RQ2 ("Does LCGA replicate the typology?") or integrated into existing RQ2 (theory-empirical comparison)?
3. **ABE positioning:** Separate finding section, within theory-empirical comparison, or new RQ?
4. **Author information:** Solo author or co-authors? Affiliations?
5. **IRB determination:** Is there a formal exempt determination from Penn State IRB, or is a general statement sufficient?
6. **"+α" hypothesis clarification:** Should ABE be elevated to a formal hypothesis (H2c: "A novel pattern of under-reliance despite improving AI performance will emerge"), or kept as an inductive discovery?

---

## Implementation Plan

Once questions are resolved:
1. Restructure manuscript with new RQ/hypothesis framework
2. Add LCGA results section
3. Add ABE finding with Phase 2B operationalization description
4. Reframe Discussion for "behavioral evidence for theory" identity
5. Format as APA 7th Word document with in-text tables and figures
6. Complete missing elements (author, IRB, data availability, etc.)

---

*Document created: 2026-03-12*
