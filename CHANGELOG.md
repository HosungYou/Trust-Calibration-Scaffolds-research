# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2026-03-02

### Added
- Phase 2: Title/Abstract screening (799 → 128 articles)
  - 2-stage process: rule-based pre-screening + batch LLM screening
  - 115 Include, 671 Exclude, 13 Uncertain (kept for full-text review)
  - Exclusion codes: E1 (300), E3 (184), E5 (159), E4 (20), E2 (8)
- Screening batch data (`resource/screening_batches/`)
- Phase 2 results (`resource/phase2a_rule_based.json`, `resource/phase2_final_results.json`)
- Excel Sheet ⑥: 54 non-OA papers requiring institutional access for PDF download
- Updated Excel Sheet ① with color-coded screening decisions
- Updated Excel Sheet ② with 128 included articles for full-text review

## [0.2.0] - 2026-03-01

### Added
- Phase 1: Pre-screening cleanup (1,209 → 799 unique articles)
  - Removed: 4 non-English, 17 non-scholarly, 141 conference papers, 99 book chapters, 143 DOI duplicates, 6 dissertations/erratum
- Screening & coding Excel workbook (`resource/TCS_screening_coding_v1.xlsx`, 6 sheets)
- Coding manual (`resource/TCS_Coding_Manual_v1.docx`, 11 chapters + 3 appendices)
- Phase 1 output files (`resource/phase1_cleaned.csv`, `resource/phase1_removal_log.json`)
- Search strategy documentation (`docs/search_strategy.md`)

## [0.1.0] - 2026-02-28

### Added
- Initial repository structure
- Korean discussion files documenting critical review process (5 files)
- Theoretical documentation (`docs/`)
- Mermaid visualizations for Two-Level Framework and Trust-Reliability Matrix
- Full paper draft: "Trust Calibration as the Missing Link in Educational AI Design"
- Individual manuscript sections (`manuscript/sections/`)
- Integrated draft (`manuscript/draft.md`)
- Reference list (APA 7th edition)
- README with project overview, research questions, and directory guide
- CC BY 4.0 license

### Notes
- Paper type: Rapid Critical Review + Conceptual Framework
- Target journal: IJETHE (International Journal of Educational Technology in Higher Education)
- Target word count: ~8,000 words
- Data and analysis scripts are maintained in the companion repository:
  `Effects-of-Agentic-AI-on-Learning-Outcomes-Across-Educational-Contexts/scoping-review/`
