# Quantitative Analysis Summary — Trust Calibration Critical Review

**Data source:** coding_results_all.json (N=92 papers coded, of 147 in review corpus)
**Date:** 2026-03-03 (updated from N=73 → N=92)
**Note:** Statistics based on RAG-assisted coding. Phase 3B added 19 papers including 16 web-search trust calibration papers (#129-145). Previous manual corrections (43 study_type fixes, 31 DOI false positive fixes) still apply to original 73 papers.

---

## RQ1: Trust Conceptualization and Measurement

### Trust Construct
| Construct | Count | % |
|-----------|-------|---|
| trust_in_AI | 81 | 88.0% |
| trust_in_automation | 6 | 6.5% |
| institutional_trust | 3 | 3.3% |
| interpersonal_trust | 2 | 2.2% |

### Trust Definition
| Definition Level | Count | % |
|------------------|-------|---|
| None provided | 77 | 83.7% |
| Explicit | 9 | 9.8% |
| Implicit | 6 | 6.5% |

### Trust Dimension
| Dimension | Count | % |
|-----------|-------|---|
| Multidimensional | 83 | 90.2% |
| Not specified | 9 | 9.8% |

### Trust Measurement
| Measured? | Count | % |
|-----------|-------|---|
| No | 85 | 92.4% |
| Yes | 7 | 7.6% |

### Calibration Measurement
| Measured? | Count | % |
|-----------|-------|---|
| No | 91 | 98.9% |
| Yes | 1 | 1.1% |

**KEY FINDING: Only 1 of 92 papers measured trust calibration accuracy — confirming the critical gap.**

---

## RQ2: Theoretical Frameworks

### Framework Distribution (paper-level)
| Framework | Count | % |
|-----------|-------|---|
| None identified | 47 | 51.1% |
| TAM (incl. combinations) | 17 | 18.5% |
| DOI | 12 | 13.0% |
| AIED frameworks | 11 | 12.0% |
| UTAUT (incl. combinations) | 8 | 8.7% |
| Lee & See (trust-in-automation) | 7 | 7.6% |
| SRL frameworks | 5 | 5.4% |
| SDT (Self-Determination Theory) | 3 | 3.3% |
| Hoff & Bashir (three-layer model) | 2 | 2.2% |
| Mayer et al. (ABI model) | 2 | 2.2% |

**Note:** Multiple frameworks per paper. Percentages exceed 100% due to overlap.

### Framework Depth
| Depth | Count | % |
|-------|-------|---|
| None | 47 | 51.1% |
| Superficial | 22 | 23.9% |
| Applied | 19 | 20.7% |
| Foundational | 4 | 4.3% |

**Key change from N=73:** Web-search papers increased Lee & See from 4→7 and SRL from 2→5, reflecting their calibration focus.

---

## RQ3: Calibration and Oversight

### Addresses Calibration
| Level | Count | % |
|-------|-------|---|
| Partially | 41 | 44.6% |
| No | 35 | 38.0% |
| Yes | 16 | 17.4% |

**Major shift from N=73:** Papers explicitly addressing calibration increased from 3 (4.1%) to 16 (17.4%) — driven by 13 web-search papers that directly study trust calibration.

**Papers explicitly addressing calibration (n=16):**
- #12 Safarov et al. (2026) — Explainable GenAI and trust
- #13 Wang et al. (2026) — AI-supported higher-order thinking
- #101 Carter et al. (2024) — Human-Automation Trust Expectation Model (HATEM)
- #129 Okamura & Yamada (2020) — Adaptive trust calibration for human-AI collaboration ★
- #130 Li et al. (2024) — Miscalibrated AI confidence on user trust ★
- #132 Vasconcelos et al. (2023) — Explanations reduce overreliance ★
- #134 Ma et al. (2024) — Self-confidence calibration in AI-assisted decision making ★
- #136 Wischnewski et al. (2023) — Trust calibrations for automated systems survey ★
- #137 Mehrotra et al. (2024) — Systematic review fostering appropriate trust ★
- #138 Scharowski et al. (2025) — Trust scale validation ★
- #139 Tomsett et al. (2020) — Rapid trust calibration via XAI ★
- #140 Lee et al. (2025) — Metacognitive sensitivity and trust calibration ★
- #141 Steyvers et al. (2025) — Metacognition and uncertainty communication ★
- #142 Zhang et al. (2025) — Learning behaviors mediate metacognitive calibration ★
- #143 Lee & Bosch (2025) — Calibration discrepancy predicts metacognitive strategy ★
- #145 Pitts & Motamedi (2025) — Human-AI trust conceptual framework ★

(★ = web-search additions, mostly from HCI/cognitive science, not originally in educational AI databases)

### Overtrust/Undertrust Discussion
| Discussed? | Overtrust | Undertrust |
|------------|-----------|------------|
| Yes | 32 (34.8%) | 34 (37.0%) |
| No | 60 (65.2%) | 58 (63.0%) |
| Both | 16 (17.4%) | — |

### Scaffold Proposed
| Proposed? | Count | % |
|-----------|-------|---|
| Yes | 60 | 65.2% |
| No | 32 | 34.8% |

### Scaffold Type Distribution
| Type | Count | % |
|------|-------|---|
| Multiple | 24 | 26.1% |
| Transparency | 22 | 23.9% |
| Other | 9 | 9.8% |
| None (no scaffold) | 32 | 34.8% |
| Metacognitive | 3 | 3.3% |
| Autonomy | 2 | 2.2% |

### Oversight Design
| Status | Count | % |
|--------|-------|---|
| None | 50 | 54.3% |
| Discussed | 41 | 44.6% |
| Monitoring system | 1 | 1.1% |

---

## Methodological Profile

### Study Type
| Type | Count | % |
|------|-------|---|
| Review | 49 | 53.3% |
| Empirical | 34 | 37.0% |
| Theoretical | 8 | 8.7% |
| Mixed | 1 | 1.1% |

### Methodology
| Methodology | Count | % |
|-------------|-------|---|
| Narrative review | 30 | 32.6% |
| Quantitative | 25 | 27.2% |
| Systematic review | 22 | 23.9% |
| Conceptual | 8 | 8.7% |
| Qualitative | 4 | 4.3% |
| Mixed methods | 3 | 3.3% |

### Year Distribution
| Year | Count | % |
|------|-------|---|
| 2019 | 2 | 2.2% |
| 2020 | 4 | 4.3% |
| 2022 | 5 | 5.4% |
| 2023 | 3 | 3.3% |
| 2024 | 13 | 14.1% |
| 2025 | 58 | 63.0% |
| 2026 | 7 | 7.6% |

### AI System Types (top 10)
| System | Count |
|--------|-------|
| GenAI | 43 |
| ChatGPT | 36 |
| AI system (unspecified) | 30 |
| AI chatbot | 16 |
| LLM | 8 |
| GPT-4 | 3 |
| Recommendation system | 3 |
| AI teaching assistant | 3 |
| GPT-3 | 2 |
| AI assessment | 1 |

### Educational Context
| Context | Count | % |
|---------|-------|---|
| Higher education | 60 | 65.2% |
| Other/General | 14 | 15.2% |
| Healthcare/Medical | 11 | 12.0% |
| K-12 | 7 | 7.6% |

### Relevance Score
| Score | Count | % |
|-------|-------|---|
| 1 | 1 | 1.1% |
| 2 | 7 | 7.6% |
| 3 | 10 | 10.9% |
| 4 | 54 | 58.7% |
| 5 | 20 | 21.7% |

---

## The Calibration Gap — Cross-tabulation

| | Calibration Measured | Calibration NOT Measured |
|---|---|---|
| Trust Measured (n=7) | 1 (14.3%) | 6 (85.7%) |
| Trust NOT Measured (n=85) | 0 (0%) | 85 (100%) |

**Interpretation:** Even among the few papers that measure trust, almost none measure whether that trust is calibrated (appropriate) relative to AI reliability. This is the central empirical gap the paper addresses.

---

## Data Quality Notes

1. **43 study_type/methodology mismatches corrected** (original 73 papers)
2. **31 DOI framework false positives corrected** (original 73 papers)
3. **Review type inflation** — Many empirical papers classified as 'review' due to literature review sections in PDFs; requires manual verification
4. **55 of 147 papers uncoded** (37.4%) — awaiting institutional PDF access
5. **Coding was AI-assisted** — All statistics should be interpreted with appropriate methodological caveats
6. **Web-search papers (#129-147) intentionally selected** for calibration relevance — not representative of the broader corpus

---

## Key Narrative Statistics for Manuscript

- "Of N=92 coded papers, **only 1 (1.1%)** measured trust calibration accuracy"
- "Only 7 papers (7.6%) included any form of trust measurement"
- "83.7% of papers provided no explicit definition of trust"
- "Over half (51.1%) employed no identifiable theoretical framework"
- "Trust-specific frameworks from the automation literature (Lee & See; Hoff & Bashir) appeared in only 9 papers (9.8%) — yet these frameworks explicitly model calibration"
- "Technology acceptance frameworks (TAM/UTAUT) guided 27.2% of studies — 3× more common than trust-in-automation frameworks"
- "16 papers (17.4%) explicitly addressed calibration — but 13 of these came from web-search additions outside the original educational AI databases, revealing a disciplinary blind spot"
- "Overtrust was discussed in 34.8% of papers; undertrust in 37.0%; only 17.4% discussed both"
- "65.2% proposed some form of scaffold, but only 3.3% specifically proposed metacognitive scaffolds"
- "The most common scaffold type was transparency (23.9%), while metacognitive scaffolds — theoretically most aligned with calibration — appeared in only 3.3%"
