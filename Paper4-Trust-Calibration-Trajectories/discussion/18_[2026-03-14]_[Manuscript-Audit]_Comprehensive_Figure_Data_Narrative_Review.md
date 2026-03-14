# Comprehensive Manuscript Audit: Figures, Data, Narrative, and Submission Readiness

**Date:** 2026-03-14
**Context:** Final review before CHB submission — figure redesign, data verification, narrative strengthening, humanizing
**Decision Status:** COMPLETED — all audit items resolved, Word document regenerated

---

## 1. Figure Redesign Decisions (2026-03-13 to 2026-03-14)

### 1.1 Unified Figure Style Framework
- Created `figures/figure_style.py` — shared style module for all figure scripts
- Tol (2021) colorblind-safe palette for MBC (6 classes)
- Wong (2011) colorblind-safe palette for LCGA (4 classes)
- APA 7th: no embedded titles, titles go in manuscript captions
- DPI = 300, single-column width = 7 inches

### 1.2 Figure 4: Phase Portrait Reconceptualization
**Problem:** Original 3D Theory vs Empirical figure was cluttered, filename mislabeled, and phase portrait concept didn't work because R_b (0.03-0.35) and P (0.49-0.65) are on incommensurable scales — the R_b=P diagonal was unreachable and meaningless.

**Process:**
1. First attempt: Calibration State Space (R_b × Gap) — Gap=0 as horizontal reference line
   - Result: C1, C2, C3, C5 all showed nearly identical upward-right trajectories
   - **Problem:** P information is hidden inside Gap (Gap = R_b - P), so classes that differ in P levels appear similar

2. Second attempt: R_b × P space with faceted 2×3 panels + ghost traces
   - **Result:** Classes occupy distinct regions, movement patterns are qualitatively different
   - C4's retreat pattern visible; C6's volatility visible; C3's large displacement visible
   - **Decision: ADOPTED** — `Figure_4_Phase_Portrait.png` (ggplot2, faceted with ghost traces)

3. 3D version (R_b × Gap × Time): Generated for comparison from 4 viewing angles
   - **Decision: REJECTED for publication** — occlusion, axis readability, depth perception issues on printed page
   - Could be used as supplementary material or interactive (plotly) for conference presentation

### 1.3 Figure 5: ABE Discovery
**Problem:** Legend in upper-left corner overlapped with P_adaptive trajectory.

**Solution:** Regenerated in ggplot2 as 2-panel layout (A: LCGA Class 4, B: MBC Phase 2B Class 4) with shared legend at bottom. No occlusion. Annotations repositioned.

### 1.4 Figure 7: Removed
- Outcome scatter figure removed from manuscript and Word generator (D16 follow-up)
- Final figure count: 6

### 1.5 Final FIGURE_MAP
| Figure | Content | Source |
|--------|---------|--------|
| 1 | MBC Trajectories (R_b + P, 2-panel) | matplotlib |
| 2 | MBC Gap Trajectories | matplotlib |
| 3 | LCGA Gap Trajectories | matplotlib |
| 4 | Phase Portrait (R_b × P, faceted 2×3 with ghost traces) | ggplot2 |
| 5 | ABE Discovery (2-panel: LCGA + MBC) | ggplot2 |
| 6 | Early Prediction Feature Importance | matplotlib |

---

## 2. Manuscript Narrative Revisions

### 2.1 Section 4.4 — Figure 4 Description Added
- Added paragraph after Figure 4 placeholder describing spatial separation of classes in R_b × P state space
- Describes convergent movement of C2/C3, retreat of C4, volatility of C6

### 2.2 Section 5.2 — Class Interpretations Rewritten
**Key change:** All psychological interpretations now use hedging language:
- "consistent with" replaced with varied alternatives ("compatible with", "points toward", direct behavioral assertions)
- Added explicit interpretive caveat paragraph at end of section
- Each class interpretation references Figure 4 panels

**Rationale:** Behavioral log data captures actions, not intentions or psychological states. R_b is a behavioral proxy for reliance, not a direct measure of trust. Performance changes may reflect independent learning, practice effects, or content difficulty — not necessarily AI-mediated benefit.

### 2.3 Section 4.4.5 — Figure 5 Narrative Added
- Added paragraph describing the "scissors" pattern visible in Figure 5
- Quantifies the widening gap: Panel A (0.30→0.54), Panel B (0.26→0.68)
- Notes cross-method convergence as evidence against artifact interpretation

### 2.4 Section 1.2 — Social Context Added (NEW)
- "AI in Education: Between Panic and Promise" — 2 paragraphs
- ChatGPT inflection point, UNESCO 2023, over-reliance assumption vs help-avoidance evidence
- Subsequent sections renumbered (1.2→1.3 through 1.6→1.7)

### 2.5 Discussion 5.4 — Policy Narrative Added (NEW)
- 2 paragraphs: under-reliance vs over-reliance policy tension
- Practical reframing: monitoring minority over-reliance while supporting majority under-utilizers

### 2.6 Discussion 5.8 — Calibration-Aware Design Added (NEW)
- Restructured from 6 parallel "For X..." blocks into 3 thematic groups
- Under-reliance majority (C1/C2/C3), stagnant non-engagers (C4), at-risk trajectories (C5/C6/ABE)
- Added calibration-aware instructional design framing

---

## 3. Data Inconsistency Audit — RESOLVED

### 3.1 Root Cause
Manuscript accuracy values were **manually typed from a preliminary/superseded analysis run** during initial drafting (draft_v1.md had identical errors). The correct source is `phase3_rq4_outcomes.csv`, independently verified by joining `phase1_student_summary.csv` with `phase2_class_assignments.csv`.

### 3.2 Corrections Applied

**Section 4.6.1 accuracy values:**

| Class | WRONG (old) | CORRECT (fixed) | SD (fixed) |
|:-----:|:-----------:|:---------------:|:----------:|
| C4 | .649 | .649 | .04 |
| C1 | .589 | **.598** | .05 |
| C6 | .591 | **.581** | .11 |
| C5 | .572 | .576 | .05 |
| C2 | .547 | **.570** | .07 |
| C3 | .518 | **.536** | .10 |

Note: Ranking also corrected — C1 (.598) > C6 (.581), not C6 > C1 as previously stated.

**Section 4.6.2 accuracy improvement — negative values now disclosed:**
- C1: ΔP = **-0.010** (was omitted)
- C5: ΔP = **-0.003** (was omitted)
- Added interpretive text: increasing R_b does not uniformly translate into performance gains

**Table 3 numbering conflict:**
- Line 307: Changed "Table 3 presents" → "The following table presents" (inline LCGA model fit table)
- Table 3 now exclusively refers to multinomial logistic regression (line 377)

### 3.3 Important Note
Table 4 in the Word document was ALREADY correct (reads from CSV). The inconsistency was between inline prose and the auto-generated table — now resolved.

---

## 4. Social Context Integration — COMPLETED

### 4.1 Rationale
The paper is technically strong but lacks connection to the current societal discourse on AI in education:
- Post-ChatGPT AI anxiety (2022-2026)
- University AI ban/allow policy oscillation
- Dominant narrative: over-reliance fear
- This paper's counter-narrative: under-reliance is the actual problem

### 4.2 Additions Made
- **Introduction Section 1.2** "AI in Education: Between Panic and Promise" — 2 paragraphs on ChatGPT moment, over-reliance assumption, help-avoidance literature
- **Discussion 5.4** — 2 paragraphs after Aleven/Baker paragraph: under-reliance vs policy narrative tension, practical reframing
- **Discussion 5.8** — 1 paragraph on calibration-aware instructional design with class-specific examples

### 4.3 New References Added (10 total)
- UNESCO (2023), Kasneci et al. (2023), Mollick & Mollick (2023)
- Baidoo-Anu & Ansah (2023), Crompton & Burke (2023)
- Aleven et al. (2016), Roll et al. (2011), Ryan & Deci (2000)
- Long & Magerko (2020), Loibl & Rummel (2014)

---

## 5. Reference Verification — COMPLETED

### 5.1 Results
- 43+ references checked by two independent verification agents
- 39 verified, 5 flagged and fixed

### 5.2 Fixes Applied
| Reference | Issue | Fix |
|-----------|-------|-----|
| Holmes et al. (2022) | Year wrong, no 2nd ed. exists | → (2019), removed "(2nd ed.)" |
| Kaur et al. (2022) | Published at CHI 2020, not 2022 | → (2020), DOI added |
| Schemmer et al. (2023) | "Dennerlein" not a real co-author | Removed from author list (5 authors, not 6) |
| Guo & Yang (2021) | Entirely fabricated — wrong authors, year, venue | Removed from manuscript and reference list |
| Choudhury et al. (2020) | Co-author "Stahelin" unverifiable; title/venue suspect | Corrected to verified JMIR paper (Choudhury, Asan, & Bayrak, 2020) |

---

## 6. CHB Submission Guidelines — COMPLETED

### 6.1 Key Requirements Applied
- **Abstract:** Shortened from 291 → 161 words (max 200-250 per CHB)
- **Highlights:** 5 bullet points added (all ≤85 characters)
- **CRediT Author Statement:** Added before Acknowledgments
- **Declaration of Competing Interest:** Added
- **Declaration of Generative AI:** Added (Claude, Anthropic — analysis scripting, figure generation, manuscript drafting)
- **Data Availability Statement:** Added as standalone section; removed redundant Appendix A.2
- **Acknowledgments:** Added (Riiid AI Research for EdNet dataset)
- **Reference style:** APA 7th (already compliant)

### 6.2 Submission Notes
- CHB uses Editorial Manager (`editorialmanager.com/CHB/`)
- Figures: TIFF preferred, 300+ DPI (current PNGs at 300 DPI acceptable for initial submission)
- No strict word limit posted, but ~8,000-12,000 typical
- Color online is free; "Your Paper Your Way" for initial submission
- Numbered sections required (already compliant)

---

## 7. Humanization Pass — COMPLETED

### 7.1 AI Pattern Audit Results (Diverga G5 Agent)
- Initial AI probability score: ~74% (10 active patterns)
- Primary risk zones: Section 5.2 ("consistent with" x6 in 13 lines), Section 5.6 ("may reflect" x5), Section 5.8 (parallel "For X..." x6)

### 7.2 Fixes Applied
| Pattern | Action |
|---------|--------|
| "Several X warrant Y" (x4) | Replaced with specific counts ("Three mechanisms", "Four ways", "Five limitations", "Four questions") |
| "Importantly/Notably" openers | Deleted or restructured |
| "Consistent with" chain (14→11) | Replaced 5 Discussion instances with varied verbs; kept Results uses |
| "May reflect" x5 chain (5.6) | Rewrote as varied prose ("look like trust building in action", "suggests settled indifference") |
| Section 1.2 tonal break | Dampened journalistic register; removed "what might be termed" |
| Section 5.8 parallel "For X..." | Collapsed 6 blocks into 3 thematic groups (under-reliance majority, stagnant non-engagers, at-risk trajectories) |
| "This suggests a specific intervention need" | Lead with substance, cut meta-commentary |
| "Convergence...strengthens confidence" (x3) | Consolidated: kept full version in 5.3, cross-referenced in others |
| "First large-scale" repeated verbatim | Differentiated Conclusion opener |
| Future Research gerund parallelism | Broke structure in 2 of 4 paragraphs; framed gaps before directions |
| "The key insight is that" | Replaced with direct statement of the insight |

**Estimated post-fix AI probability:** ~40-45% (within normal range for computationally-assisted academic writing)

---

## 8. Final Output

### 8.1 Word Document
- **File:** `manuscript/Paper4_APA7th_FINAL.docx`
- **Size:** 1,639.6 KB
- **Tables:** 5 (auto-generated from CSV data)
- **Figures:** 6 (embedded at 300 DPI)
- **Abstract:** 173 words (Word generator version)
- **CHB Elements:** Highlights (5), CRediT, Competing Interest, AI Disclosure, Data Availability, Acknowledgments

### 8.2 Task Checklist
- [x] Figure 4 reconceptualized (3D → 2D phase portrait)
- [x] Figure 5 legend fix (ggplot2 2-panel with bottom legend)
- [x] Figure 7 removed
- [x] Section 5.2 class interpretations rewritten with hedging
- [x] Section 1.2 social context added (Introduction)
- [x] Discussion 5.4 social context added (under-reliance vs policy)
- [x] Discussion 5.8 restructured (calibration-aware design)
- [x] Data inconsistencies fixed (accuracy values, negative improvements, Table 3)
- [x] 5 hallucinated/incorrect references fixed
- [x] 10 new references added
- [x] CHB formatting applied (abstract, highlights, declarations)
- [x] AI writing patterns humanized (10 patterns addressed)
- [x] Word document regenerated
- [x] Final documentation completed

---

## 9. Decision Record

| Date | Decision |
|------|----------|
| 2026-03-13 | Figure 4 reconceptualized: 3D → R_b × Gap (rejected) → R_b × P faceted (adopted) |
| 2026-03-13 | Figure 5 regenerated: matplotlib with inset → ggplot2 2-panel with bottom legend |
| 2026-03-13 | Figure 7 removed from manuscript |
| 2026-03-14 | Section 5.2 rewritten with hedging language and interpretive caveat |
| 2026-03-14 | Data inconsistency audit: 4 accuracy values corrected, 2 negative improvements disclosed |
| 2026-03-14 | Section 1.2 "AI in Education: Between Panic and Promise" inserted |
| 2026-03-14 | Discussion 5.4 social context (policy narrative tension) inserted |
| 2026-03-14 | Discussion 5.8 restructured into 3 thematic intervention groups |
| 2026-03-14 | Reference verification: 5 references corrected (Holmes, Kaur, Schemmer, Guo, Choudhury) |
| 2026-03-14 | CHB formatting: abstract shortened (291→161), highlights, declarations added |
| 2026-03-14 | Humanization: 10 AI patterns identified and fixed, estimated ~74% → ~40-45% |
| 2026-03-14 | Word document regenerated: Paper4_APA7th_FINAL.docx (1,639.6 KB) |
| 2026-03-14 | Final documentation completed |

---

## 10. Interpretive Guidelines (Standing)

### 10.1 Language Protocol
All class interpretations must distinguish between:
- **Behavioral patterns** (empirical facts from data — assert directly)
- **Psychological mechanisms** (inferential — use "compatible with", "points toward", "suggests")
- **Causal claims** (not possible with observational data — explicitly disclaim)

### 10.2 Negative Improvement Disclosure
C1 (ΔP = -0.010) and C5 (ΔP = -0.003) are honestly reported and interpreted:
- C1: largest class (30%), AI adoption without benefit — questions the "productive calibration" narrative
- C5: heavy AI use with negative improvement — possible over-dependence signal
- Interpretive text added: "increasing behavioral reliance on AI did not uniformly translate into performance gains"
