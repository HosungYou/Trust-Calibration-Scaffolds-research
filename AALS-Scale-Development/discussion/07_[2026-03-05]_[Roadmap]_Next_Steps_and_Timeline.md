# Roadmap: Next Steps and Timeline

**Date:** 2026-03-05
**Status:** Planning — pre-data collection
**Current Progress:** Process model confirmed, item pool developed (48 items), manuscript draft v1 complete

---

## 1. Completed Phases

| Phase | Task | Status | Output |
|-------|------|--------|--------|
| Phase 1 | Conceptualization & 3D Framework | Done | Discussion 01 |
| Phase 1 | Literature Review (16+ scales) | Done | Discussion 02 |
| Phase 1 | Expert Critique (A3, D4, C1) | Done | Discussion 03 |
| Phase 1 | Process Model & Scale Architecture | Done | Discussion 04 |
| Phase 0 | Initial Item Pool (42 items) | Done | Discussion 05 |
| Phase 0 | D4 Review & Revision (48 items) | Done | Discussion 06 |
| — | Figure 1: Trust Calibration Process Model | Done | figures/ |
| — | Manuscript Draft v1 (pre-data) | Done | manuscript/ |

---

## 2. Upcoming Phases

### Phase 2: Expert Panel (CVI) ← NEXT

**Goal:** Content validity assessment of 48 items by domain experts

**Tasks:**
1. Recruit 5-7 experts across five domains:
   - AI in education / Educational technology (1-2)
   - Trust in automation / Human-AI interaction (1)
   - Psychometrics / Scale development (1)
   - Metacognition / Self-regulated learning (1)
   - AI literacy (1)
2. Prepare CVI rating materials:
   - Construct definitions for each subscale
   - Process model explanation (Figure 1)
   - Item pool with subscale assignment
   - Rating form: relevance (1-4) + open comments + cross-classification task
3. Conduct review (2-3 weeks for experts to respond)
4. Calculate I-CVI (item-level, threshold ≥ .78) and S-CVI/Ave (scale-level, threshold ≥ .90)
5. Revise or remove items with I-CVI < .78
6. Target output: 30-36 items retained

**Decision Points:**
- Items with I-CVI .60-.77: discuss with panel, revise or drop?
- Cross-classification disagreements: reassign or revise?

**Deliverable:** Discussion 08 — Expert Panel CVI Results

---

### Phase 3: Cognitive Interviews

**Goal:** Response process validity — do learners understand items as intended?

**Tasks:**
1. Recruit 8-10 undergraduate/graduate students
   - Diverse: STEM + humanities, high/low AI experience
2. Think-aloud protocol (30-45 min per participant):
   - "What does this question mean to you?"
   - "Can you think of a recent example?"
   - "Was anything confusing?"
   - "How did you decide on your answer?"
3. Focus on:
   - Items flagged as complex: Aw08, Jd07, Jd15, Ac09
   - New items without precedent: Aw06 (affective), Aw16 (social), Jd15 (proportional trust)
   - Reverse-coded items: comprehension check
4. Revise items based on patterns in interview data
5. Target output: 30-36 items finalized for pilot

**Deliverable:** Discussion 09 — Cognitive Interview Results

---

### Phase 4: Pilot Test

**Goal:** Initial reliability and item performance check

**Tasks:**
1. Small sample: N = 50-80 (convenience sample, online)
2. Administer finalized item pool
3. Assess:
   - Item descriptive statistics (mean, SD, skewness, kurtosis)
   - Item-total correlations (threshold ≥ .30)
   - Internal consistency (Cronbach's alpha, target ≥ .70 per subscale)
   - Floor/ceiling effects (threshold < 15%)
4. Identify and flag problematic items
5. Final item revisions if needed

**Deliverable:** Discussion 10 — Pilot Test Results

---

### Phase 5: OSF Preregistration

**Goal:** Transparent, pre-committed analysis plan before data collection

**Tasks:**
1. Register on Open Science Framework (OSF):
   - Hypothesized factor structure (2 or 3 factors)
   - Nomological network with predicted correlation ranges
   - Sample size justification
   - Detailed analysis plan (EFA criteria, CFA model comparison, validity tests)
   - Falsification criteria for Judgment subscale (CT correlation threshold)
2. Create preregistration document using AsPredicted or OSF standard template

**Key Pre-committed Decisions:**

| Decision | Pre-committed Choice |
|----------|---------------------|
| EFA extraction method | Principal axis factoring |
| Rotation | Oblique (Promax, kappa = 4) |
| Factor number determination | Parallel analysis + scree + theory |
| Item retention | Loading ≥ .40 primary, < .30 cross, communality ≥ .30 |
| CFA estimation | MLR |
| Model fit criteria | CFI/TLI > .95, RMSEA < .06, SRMR < .08 |
| Falsification threshold | CA-Jd ↔ CT r ≥ .60 → fold Judgment into Awareness |
| Convergent validity range | r = .40-.60 with MAILS, CT |
| Discriminant validity range | r < .30 with S-TIAS, GSE |

**Deliverable:** OSF preregistration URL (to be cited in manuscript)

---

### Phase 6: Study 1 — Exploratory Factor Analysis

**Goal:** Determine the TCRS factor structure empirically

**Tasks:**
1. **Sample recruitment:** N = 300-350
   - Higher education students
   - AI tool experience required
   - Online survey (Qualtrics or similar)
   - Compensation: [TBD]
2. **Survey contents:**
   - Demographics (age, gender, field, year)
   - AI use profile (tools, frequency, duration)
   - TCRS item pool (30-36 items)
   - 1-2 attention check items
3. **Analysis:**
   - Data screening (normality, outliers, missing data)
   - Factorability (KMO > .80, Bartlett's p < .001)
   - EFA: Principal axis factoring, Promax rotation
   - Factor number: Parallel analysis + scree + eigenvalue > 1 + theory
   - Item retention: loading ≥ .40, cross-loading < .30, communality ≥ .30
   - Internal consistency: alpha and omega per subscale
4. **Expected outcomes:**
   - 3-factor solution (55-60% probability)
   - 2-factor solution (30-35%): Cognition + Action
   - Final scale: 18-24 items (6-8 per subscale)

**Deliverable:** Manuscript Study 1 Results section

---

### Phase 7: Study 2 — CFA + Validity Evidence

**Goal:** Confirm factor structure and establish validity

**Tasks:**
1. **Sample recruitment:** N = 300-350 (independent of Study 1)
   - Same inclusion criteria
   - Online survey
2. **Survey contents:**
   - Demographics + AI use profile
   - TCRS (retained items from Study 1)
   - Convergent validity: MAILS Short (10 items) + CT Disposition (~11 items)
   - Discriminant validity: S-TIAS (3 items) + General Self-Efficacy (10 items)
   - Attention checks
   - Total survey: ~60-70 items + demographics
3. **Analysis:**
   - CFA: 4 competing models (1-factor, 2-factor, 3-factor, bifactor)
   - Model fit: CFI, TLI, RMSEA, SRMR
   - Method factor for response format
   - Bifactor analysis: omega-h, omega-s (Rodriguez et al., 2016)
   - Convergent/discriminant validity: correlation matrix
   - Known-groups: AI experience × field of study comparisons
   - Falsification test: CA-Jd ↔ CT correlation
   - Measurement invariance: gender, field of study (configural → metric → scalar)

**Deliverable:** Manuscript Study 2 Results section

---

### Phase 8: Manuscript Completion

**Tasks:**
1. Complete Results sections (Studies 1 and 2)
2. Write General Discussion
3. Finalize tables and figures
4. Prepare supplementary materials
5. Internal review
6. Target journal selection and submission

---

## 3. Timeline Estimate

| Phase | Task | Duration | Cumulative |
|-------|------|----------|------------|
| Phase 2 | Expert Panel (CVI) | 3-4 weeks | Month 1 |
| Phase 3 | Cognitive Interviews | 2-3 weeks | Month 2 |
| Phase 4 | Pilot Test | 2 weeks | Month 2-3 |
| Phase 5 | OSF Preregistration | 1 week | Month 3 |
| Phase 6 | Study 1 (EFA): recruitment + data collection | 4-6 weeks | Month 4-5 |
| Phase 6 | Study 1: analysis + write-up | 2-3 weeks | Month 5-6 |
| Phase 7 | Study 2 (CFA): recruitment + data collection | 4-6 weeks | Month 6-8 |
| Phase 7 | Study 2: analysis + write-up | 3-4 weeks | Month 8-9 |
| Phase 8 | Manuscript completion + revision | 4-6 weeks | Month 9-11 |
| — | **Total estimated** | **9-11 months** | — |

---

## 4. Budget Considerations

| Item | Estimate | Notes |
|------|----------|-------|
| Survey platform (Qualtrics/Prolific) | Varies | May have institutional access |
| Participant compensation — Study 1 | N × rate | Online survey, ~15 min |
| Participant compensation — Study 2 | N × rate | Online survey, ~20-25 min |
| Expert panel honorarium | Optional | Some experts may volunteer |
| Cognitive interview compensation | 8-10 × rate | 30-45 min interviews |
| Total participants | ~700-750 | Studies 1+2 + pilot + cognitive interviews |

---

## 5. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Aw-Jd factor collapse in EFA | 30-35% | Medium | Report 2-factor model honestly; discuss theoretical vs. empirical distinction |
| CA-Jd ↔ CT r ≥ .60 (falsification) | 15-20% | High | Pre-committed fallback: 2-subscale model (Awareness + Action) |
| Low reliability (alpha < .70) | 10-15% | High | Pilot test catches this early; revise items |
| Insufficient sample size | 10% | High | Plan for online recruitment (Prolific) as backup |
| AI landscape shifts during study | Low | Low | Scale at construct level, not technology level |
| Expert panel recruitment difficulty | 15% | Medium | Start recruitment early; expand search globally |

---

## 6. Key Decisions Still Pending

| # | Decision | When to Decide | Options |
|---|----------|---------------|---------|
| 1 | Scale name | Before expert panel | TCRS vs. Trust Calibration Readiness Scale vs. other |
| 2 | Development language | Before expert panel | Korean-first → English translation, or English-first → Korean |
| 3 | Survey platform | Before pilot | Qualtrics, Google Forms, Prolific |
| 4 | Recruitment strategy | Before Study 1 | University sample, Prolific, mixed |
| 5 | Compensation rate | Before pilot | Depends on funding |
| 6 | Target journal | Before manuscript completion | Computers & Education, BJET, CHB, ETR&D |
