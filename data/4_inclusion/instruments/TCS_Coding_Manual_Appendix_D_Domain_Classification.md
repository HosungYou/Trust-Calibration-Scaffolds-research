# Appendix D: Post-Hoc Research Orientation Domain Classification

## D.1 Purpose

This appendix describes the derivation of the `research_domain` variable, a post-hoc classification applied to the 97 coded papers to characterize their research orientation along a trust calibration maturity spectrum. The classification uses existing coded variables (addresses_calibration, overtrust_discussed, undertrust_discussed, scaffold_proposed, theoretical_framework) and requires no additional coding.

Purpose: To organize the corpus into meaningful clusters that reveal the field's progression (or lack thereof) toward trust calibration research, supporting the paper's central argument about the "calibration gap."

## D.2 Domain Definitions

### D1: Trust Adoption (n=5, 5.2%)
- **Definition**: Studies that exclusively employ technology acceptance frameworks (TAM, UTAUT, DOI) to examine trust as a predictor of AI adoption, without addressing trust calibration, overtrust/undertrust, or scaffold design.
- **Theoretical orientation**: Trust = adoption predictor
- **Calibration relevance**: None — trust is structurally positioned as a variable to be maximized, not calibrated.

### D2: Trust Conceptualization (n=11, 11.3%)
- **Definition**: Studies that discuss trust in educational AI at a general conceptual level without proposing specific design interventions or addressing calibration/miscalibration.
- **Theoretical orientation**: Trust as a general concept
- **Calibration relevance**: Minimal — trust is acknowledged but not operationalized for calibration purposes.

### D3: Trust Design (n=24, 24.7%)
- **Definition**: Studies that propose scaffolds, design features, or interventions related to trust in AI, but without calibration criteria (i.e., without reference to whether trust should be increased, decreased, or aligned with system reliability).
- **Theoretical orientation**: Trust as a design target
- **Calibration relevance**: Indirect — design proposals may affect trust levels but lack calibration benchmarks.

### D4: Trust Awareness (n=41, 42.3%)
- **Definition**: Studies that recognize and discuss overtrust and/or undertrust as problems, partially address calibration, but do not explicitly measure or systematically address trust calibration.
- **Theoretical orientation**: Trust miscalibration as a recognized problem
- **Calibration relevance**: Partial — the problem is identified but not measured or solved.

#### D4 Subcategories:
- **D4a: Overtrust Recognition** (n=16, 16.5%): Studies that discuss overtrust/overreliance but not undertrust.
- **D4b: Undertrust Recognition** (n=18, 18.6%): Studies that discuss undertrust/rejection but not overtrust.
- **D4c: Bidirectional Awareness** (n=7, 7.2%): Studies that discuss both overtrust and undertrust.

### D5: Trust Calibration (n=16, 16.5%)
- **Definition**: Studies that explicitly address trust calibration — the alignment between trust and system reliability — as a construct, measurement target, or intervention goal.
- **Theoretical orientation**: Trust calibration as an explicit research focus
- **Calibration relevance**: Direct — calibration is explicitly studied.
- **Source note**: 3 papers from original database searches; 13 from supplementary citation tracking. This distribution itself evidences the disciplinary blind spot documented in the review.

## D.3 Classification Priority Rules

Papers are classified using the following priority rules (highest priority first). Each paper is assigned to exactly one domain.

| Priority | Rule | Domain |
|----------|------|--------|
| 1 | `addresses_calibration == "yes"` | D5 |
| 2 | (`overtrust_discussed == "yes"` OR `undertrust_discussed == "yes"`) AND `addresses_calibration == "partially"` | D4 |
| 2a | D4 AND `overtrust_discussed == "yes"` AND `undertrust_discussed == "no"` | D4a |
| 2b | D4 AND `overtrust_discussed == "no"` AND `undertrust_discussed == "yes"` | D4b |
| 2c | D4 AND `overtrust_discussed == "yes"` AND `undertrust_discussed == "yes"` | D4c |
| 3 | `scaffold_proposed == "yes"` AND NOT already D4/D5 | D3 |
| 4 | `theoretical_framework` contains TAM/UTAUT/DOI AND NOT already D3/D4/D5 | D1 |
| 5 | All remaining papers | D2 |

**Key design decisions:**
- Priority ordering ensures that papers meeting multiple criteria are classified at their highest maturity level.
- D4 requires both a trust direction indicator (overtrust or undertrust) AND partial calibration engagement.
- D1 is restricted to papers whose only theoretical contribution is through acceptance frameworks, ensuring that TAM-using papers with calibration awareness or design proposals are classified at higher levels.

## D.4 Coding Examples

### Example 1: D5 Classification
**Paper #129 — Okamura & Yamada (2020)**
- addresses_calibration = "yes"
- overtrust_discussed = "yes", undertrust_discussed = "yes"
- Rule 1 applies → **D5**
- Rationale: Explicitly measures and intervenes on trust calibration in human-AI collaboration.

### Example 2: D4c Classification
**Paper #19 — Abubakar et al. (2025)**
- addresses_calibration = "partially"
- overtrust_discussed = "yes", undertrust_discussed = "yes"
- Rule 2 applies, Rule 2c for subcategory → **D4c (Bidirectional Awareness)**
- Rationale: Recognizes both overtrust and undertrust but does not explicitly measure calibration.

### Example 3: D3 Classification
**Paper #26 — Ang et al. (2025)**
- addresses_calibration = "no"
- overtrust_discussed = "no", undertrust_discussed = "no"
- scaffold_proposed = "yes"
- Rule 3 applies → **D3**
- Rationale: Proposes design scaffolds without calibration criteria or trust direction awareness.

### Example 4: D1 Classification
**Paper #25 — Amin et al. (2025)**
- addresses_calibration = "no"
- overtrust_discussed = "no", undertrust_discussed = "no"
- scaffold_proposed = "no"
- theoretical_framework = "UTAUT"
- Rule 4 applies → **D1**
- Rationale: Uses UTAUT to study trust as an adoption predictor without any calibration, design, or awareness elements.

### Example 5: D2 Classification
**Paper #1 — Amjad et al. (2026)**
- addresses_calibration = "no"
- overtrust_discussed = "no", undertrust_discussed = "no"
- scaffold_proposed = "no"
- theoretical_framework = "none"
- Rule 5 applies → **D2**
- Rationale: Discusses trust conceptually without framework, design, or calibration elements.

## D.5 Intercoder Reliability Protocol

The domain classification is a **derived variable** computed algorithmically from existing coded variables. Therefore, intercoder reliability for the domain classification itself is determined by the reliability of its input variables:

- `addresses_calibration`: Included in the intercoder reliability assessment (20-30% subsample coded by second coder)
- `overtrust_discussed`: Included in the intercoder reliability assessment
- `undertrust_discussed`: Included in the intercoder reliability assessment
- `scaffold_proposed`: Included in the intercoder reliability assessment
- `theoretical_framework`: Included in the intercoder reliability assessment

Cohen's kappa values for these input variables are reported in Section 3.3 of the manuscript. Because the domain classification applies deterministic priority rules to these variables, its reliability is bounded by the reliability of the input variables.

**Validation procedure**: After independent coding of the subsample, domain classifications were computed separately from each coder's data and compared. Any discrepancies were traced to the input variable(s) causing the difference and resolved through discussion.

## D.6 Distribution Summary

| Domain | Label | n | % |
|--------|-------|---|---|
| D1 | Trust Adoption | 5 | 5.2% |
| D2 | Trust Conceptualization | 11 | 11.3% |
| D3 | Trust Design | 24 | 24.7% |
| D4 | Trust Awareness | 41 | 42.3% |
| — D4a | Overtrust Recognition | 16 | 16.5% |
| — D4b | Undertrust Recognition | 18 | 18.6% |
| — D4c | Bidirectional Awareness | 7 | 7.2% |
| D5 | Trust Calibration | 16 | 16.5% |
| **Total** | | **97** | **100%** |

---

*This appendix should be integrated into the main coding manual (TCS_Coding_Manual_v1.docx) as Appendix D.*
