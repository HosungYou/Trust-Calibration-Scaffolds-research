# Trust Calibration as the Missing Link in Educational AI Design

**A Critical Review and Conceptual Framework**

## Overview

This repository contains the research workspace for a paper examining trust calibration in educational AI systems. The paper proposes a **Two-Level Trust Calibration Framework** that bridges the gap between learner-level trust dynamics and system-level oversight design.

- **Paper Title**: Trust Calibration as the Missing Link in Educational AI Design: A Critical Review and Conceptual Framework
- **Target Journal**: International Journal of Educational Technology in Higher Education (IJETHE, IF ~8.6)
- **Paper Type**: Rapid Critical Review + Conceptual Framework
- **Author**: Hosung You

## Core Thesis

Trust calibration — the alignment between learner trust in AI and actual AI capability — represents a critical missing link in educational AI design. When trust is miscalibrated (overtrust or undertrust), learning outcomes suffer. This paper identifies this calibration gap in the literature and proposes a framework to address it.

## Research Questions

1. **RQ1**: How is trust in AI conceptualized and measured in educational AI research?
2. **RQ2**: What theoretical frameworks guide trust research in educational AI?
3. **RQ3**: To what extent does existing research address trust calibration and human oversight design?
4. **RQ4**: What does a two-level framework connecting learner trust dynamics to system-mediated trust calibration look like?

## The Two-Level Framework

- **Level 1 (Micro)**: Learner Trust Dynamics — how trust forms, functions, and miscalibrates at the individual level
- **Level 2 (Macro)**: System-Mediated Trust Calibration — six trust calibration scaffolds grounded in educational theory
- **Adaptive Calibration Cycle**: Four-stage SRL-aligned cycle connecting both levels (Performance → Monitoring → Evaluation → Adaptation)

### Six Trust Calibration Scaffolds

| Scaffold | Theoretical Basis | Function |
|----------|------------------|----------|
| Metacognitive Prompts | Schraw & Dennison (1994) | Activate self-monitoring before/after AI interaction |
| Desirable Difficulties | Bjork & Bjork (2011) | Introduce beneficial challenges for calibration |
| Productive Failure | Kapur (2008) | Structured failure-then-instruction sequences |
| AI Uncertainty Transparency | XAI literature | Display confidence levels and limitations |
| Socratic Dialogue | Educational tradition | Question-based interaction over answer-giving |
| Progressive Autonomy Release | Wood et al. (1976) | Gradual scaffold fading as calibration improves |

## Directory Structure

```
├── README.md
├── CHANGELOG.md
├── LICENSE                              # CC BY 4.0
├── .gitignore
│
├── discussion/                          # Korean discussion records (한글)
│   ├── 01_종합_리뷰_구조적_약점.md       # 6 structural weakness diagnosis
│   ├── 02_용어_교체_논의.md              # Terminology replacement rationale
│   ├── 03_SRL_vs_Trust_Calibration.md   # SRL vs Trust calibration distinction
│   ├── 04_시각화_구조_설계.md            # Visualization design decisions
│   └── 05_연구_설계_비판_수정.md         # Research design critique (Path C)
│
├── docs/                                # Research documentation
│   ├── paper_outline.md                 # Paper outline (Path C structure)
│   ├── theoretical_foundation.md        # Theoretical foundations
│   ├── terminology_decisions.md         # Terminology change records
│   └── scaffolding_taxonomy.md          # Educational scaffolding taxonomy
│
├── manuscript/                          # Paper manuscript
│   ├── draft.md                         # Integrated full draft (~12,000 words)
│   ├── sections/
│   │   ├── 00_abstract.md
│   │   ├── 01_introduction.md
│   │   ├── 02_conceptual_foundation.md
│   │   ├── 03_review_approach.md
│   │   ├── 04_literature_landscape.md
│   │   ├── 05_two_level_framework.md
│   │   ├── 06_implications.md
│   │   └── 07_conclusion.md
│   └── references.md                   # APA 7th edition (~50 references)
│
├── visualizations/                      # Mermaid diagrams
│   ├── fig2_two_level_framework.md      # Two-Level Framework diagram
│   └── fig3_trust_reliability_matrix.md # 2x2 Trust-AI Reliability Matrix
│
├── figures/                             # Generated images
│   └── .gitkeep
│
└── resource/                            # Source data files
    ├── Scopus_revised.csv               # Scopus export (951 records)
    ├── WoS_new.xls                      # Web of Science export (188 records)
    ├── PsycINFO_ProQuest.xls            # PsycINFO export (70 records)
    ├── phase1_cleaned.csv               # Phase 1 output: 799 deduplicated articles
    ├── phase1_removal_log.json          # Phase 1 removal audit trail
    ├── phase2a_rule_based.json          # Phase 2a rule-based screening results
    ├── phase2_final_results.json        # Phase 2 final: 128 included for full-text
    ├── TCS_screening_coding_v1.xlsx     # Screening & coding Excel (6 sheets)
    ├── TCS_Coding_Manual_v1.docx        # Coding manual (11 chapters + appendices)
    └── screening_batches/               # LLM screening batch data (audit trail)
```

## Key Terminology Decisions

| Original Term | Replacement | Rationale |
|--------------|-------------|-----------|
| Checkpoint | Trust Calibration Scaffold | "Checkpoint" lacks theoretical grounding in education |
| Forced Friction | Desirable Difficulties | Bjork & Bjork (1994) established terminology |
| HITL | Teacher-Mediated Verification | Avoids engineering metaphor |
| Confidence Display | AI Uncertainty Transparency | More precise and theory-aligned |

## Relationship to Companion Repository

This research builds on preliminary scoping review infrastructure maintained in:

```
Effects-of-Agentic-AI-on-Learning-Outcomes-Across-Educational-Contexts/scoping-review/
```

That repository contains search strategies, data extraction scripts, and initial screening results. This repository references but does not duplicate those materials, focusing instead on the conceptual framework paper and its supporting documentation.

## Key References

- Bastani, H., et al. (2025). Generative AI can harm learning. *PNAS*, 122(2).
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1).
- Wang, X., et al. (2025). Trust in AI-powered educational agents. [Manuscript under review].
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *JCPP*, 17(2).
- Winne, P. H., & Hadwin, A. F. (1998). Studying as self-regulated learning.

## Screening Progress

| Phase | Input | Output | Status |
|-------|-------|--------|--------|
| Database search | 3 databases | 1,209 records | Done |
| Phase 1: Pre-screening | 1,209 | 799 unique articles | Done |
| Phase 2: T/A screening | 799 | 128 (115 I + 13 U) | Done |
| Phase 3: Full-text screening | 128 | ~40-60 target | Pending (PDF retrieval) |
| Phase 4: Thematic coding | ~40-60 | Coded dataset | Pending |

### Phase 2 Exclusion Breakdown

| Code | Reason | Count |
|------|--------|-------|
| E1 | Trust mentioned peripherally | 300 |
| E3 | Non-AI educational trust | 184 |
| E5 | No trust/reliance content | 159 |
| E4 | Non-educational context | 20 |
| E2 | Technical trustworthiness | 8 |

## Status

- [x] Repository structure
- [x] Korean discussion files (5/5)
- [x] Mermaid visualizations (2/2)
- [x] Documentation files (4/4)
- [x] Manuscript sections (8/8)
- [x] References compiled
- [x] Integrated draft
- [x] Systematic search across 3 databases (Scopus, WoS, PsycINFO)
- [x] Phase 1: Pre-screening cleanup (1,209 → 799)
- [x] Phase 2: Title/Abstract screening (799 → 128)
- [x] Screening template & coding manual
- [ ] PDF retrieval (74 OA + 54 institutional access)
- [ ] Phase 3: Full-text screening
- [ ] Phase 4: Thematic coding (4 RQ dimensions)
- [ ] Literature confirmation ([CONFIRM WITH LITERATURE] markers)
- [ ] Word count optimization (target: ~8,000 words)
- [ ] Final proofreading and revision

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
