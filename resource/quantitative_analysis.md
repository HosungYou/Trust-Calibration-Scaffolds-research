# Quantitative Analysis Summary — Trust Calibration Critical Review

**Data source:** coding_results_all.json (N=73 papers coded, of 128 in review corpus)
**Date:** 2026-03-02
**Note:** Statistics based on RAG-assisted coding with manual corrections applied for study_type/methodology mismatches (43 fixes) and DOI framework false positives (31 fixes).

---

## RQ1: Trust Conceptualization and Measurement

### Trust Construct
| Construct | Count | % |
|-----------|-------|---|
| trust_in_AI | 67 | 91.8% |
| trust_in_automation | 3 | 4.1% |
| interpersonal_trust | 2 | 2.7% |
| institutional_trust | 1 | 1.4% |

### Trust Definition
| Definition Level | Count | % |
|------------------|-------|---|
| None provided | 63 | 86.3% |
| Implicit | 6 | 8.2% |
| Explicit | 4 | 5.5% |

### Trust Dimension
| Dimension | Count | % |
|-----------|-------|---|
| Multidimensional | 64 | 87.7% |
| Not specified | 9 | 12.3% |

### Trust Measurement
| Measured? | Count | % |
|-----------|-------|---|
| No | 67 | 91.8% |
| Yes | 6 | 8.2% |

**Papers reporting trust measurement (n=6):**
- #13 Wang et al. (2026) — Creative Self-Efficacy scale reframed
- #41 Gökçearslan et al. (2026) — sum of scores
- #46 Hou et al. (2025)
- #47 Hou et al. (2025)
- #101 Carter et al. (2024) — Trust scale
- #126 Yakar et al. (2022) — media-based

### Calibration Measurement
| Measured? | Count | % |
|-----------|-------|---|
| No | 73 | **100%** |

**KEY FINDING: Zero papers in the educational AI corpus measured trust calibration accuracy.**

---

## RQ2: Theoretical Frameworks

### Framework Distribution (paper-level, corrected)
| Framework | Count | % |
|-----------|-------|---|
| None identified | 39 | 53.4% |
| TAM (incl. combinations) | 15 | 20.5% |
| AIED frameworks | 8 | 11.0% |
| UTAUT (incl. combinations) | 7 | 9.6% |
| DOI (genuine, conservative) | 5 | 6.8% |
| Lee & See (trust-in-automation) | 4 | 5.5% |
| SDT (Self-Determination Theory) | 3 | 4.1% |
| Hoff & Bashir (three-layer model) | 2 | 2.7% |
| SRL frameworks | 2 | 2.7% |

**Note:** 15 papers use multiple frameworks. Percentages exceed 100% due to overlap.

**Papers using TAM or UTAUT (technology acceptance): 17 (23.3%)**
**Papers with no theoretical framework: 39 (53.4%)**
**Papers using trust-specific frameworks (Lee_See + Hoff_Bashir): 5 (6.8%)**

### Framework Depth
| Depth | Count | % |
|-------|-------|---|
| None | 39 | 53.4% |
| Applied | 17 | 23.3% |
| Superficial | 15 | 20.5% |
| Foundational | 2 | 2.7% |

---

## RQ3: Calibration and Oversight

### Addresses Calibration
| Level | Count | % |
|-------|-------|---|
| Partially | 38 | 52.1% |
| No | 32 | 43.8% |
| Yes | 3 | 4.1% |

**Papers explicitly addressing calibration (n=3):**
- #12 Safarov et al. (2026) — Explainable GenAI and trust
- #13 Wang et al. (2026) — AI-supported higher-order thinking
- #101 Carter et al. (2024) — Human-Automation Trust Expectation Model (HATEM)

### Overtrust/Undertrust Discussion
| Discussed? | Overtrust | Undertrust |
|------------|-----------|------------|
| Yes | 24 (32.9%) | 23 (31.5%) |
| No | 49 (67.1%) | 50 (68.5%) |

### Scaffold Proposed
| Proposed? | Count | % |
|-----------|-------|---|
| Yes | 46 | 63.0% |
| No | 27 | 37.0% |

### Scaffold Type Distribution
| Type | Count | % |
|------|-------|---|
| None | 27 | 37.0% |
| Multiple | 18 | 24.7% |
| Transparency | 16 | 21.9% |
| Other | 9 | 12.3% |
| Metacognitive | 2 | 2.7% |
| Autonomy | 1 | 1.4% |

### Oversight Design
| Status | Count | % |
|--------|-------|---|
| None | 39 | 53.4% |
| Discussed | 34 | 46.6% |

---

## Methodological Profile

### Study Type (corrected)
| Type | Count | % |
|------|-------|---|
| Review | 45 | 61.6% |
| Empirical | 22 | 30.1% |
| Theoretical | 6 | 8.2% |

### Methodology (as coded)
| Methodology | Count | % |
|-------------|-------|---|
| Narrative review | 26 | 35.6% |
| Systematic review | 19 | 26.0% |
| Quantitative | 16 | 21.9% |
| Conceptual | 6 | 8.2% |
| Qualitative | 4 | 5.5% |
| Mixed methods | 2 | 2.7% |

### Relevance Score
| Score | Count | % |
|-------|-------|---|
| 4 | 49 | 67.1% |
| 3 | 9 | 12.3% |
| 5 | 7 | 9.6% |
| 2 | 7 | 9.6% |
| 1 | 1 | 1.4% |

---

## Data Quality Notes

1. **43 study_type/methodology mismatches corrected** — RAG pipeline query template overlap
2. **31 DOI framework false positives corrected** — regex matched Digital Object Identifiers
3. **25 generic key_findings (34.2%)** — "See full text for findings" placeholder entries
4. **55 of 128 papers uncoded** (45 with PDFs, 10 without) — 56.6% coverage
5. **Trust measurement quality concern** — Some trust_measured=yes entries appear to measure reliance or attitudes rather than trust specifically (#46, #47: use university enrollment data)
6. **Coding was AI-assisted** — All statistics should be interpreted with appropriate methodological caveats

---

## Key Narrative Statistics for Manuscript

- "Of N=73 coded papers, **zero (0%)** measured trust calibration accuracy"
- "Only 6 papers (8.2%) included any form of trust measurement"
- "86.3% of papers provided no explicit definition of trust"
- "Over half (53.4%) employed no identifiable theoretical framework"
- "Only 5 papers (6.8%) drew on trust-specific frameworks from the automation literature (Lee & See, 2004; Hoff & Bashir, 2015)"
- "Technology acceptance frameworks (TAM/UTAUT) guided 23.3% of studies — more than trust-in-automation frameworks by a factor of 3.4"
- "While 52.1% of papers partially addressed calibration, only 3 (4.1%) did so explicitly"
- "Overtrust was discussed in 32.9% of papers; undertrust in 31.5%"
- "63.0% proposed some form of scaffold, but only 2.7% specifically proposed metacognitive scaffolds"
