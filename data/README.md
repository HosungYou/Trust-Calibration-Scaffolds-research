# Data Directory — Trust Calibration in Educational AI

This directory contains all data supporting the systematic review and analysis reported in:

> **"The Calibration Gap: A Critical Review of Trust Research in Educational AI and the Case for a Paradigm Shift"**

## PRISMA Flow Overview

```
IDENTIFICATION (1_identification/)
  WoS: 578 → Scopus: 489 → PsycINFO: 136 = 1,203 records
          ↓
  Duplicates removed: 143 (DOI) + 0 (title)
  Non-English: 4
  Non-article: 257
          ↓
SCREENING (2_screening/)
  Title/Abstract screened: 799
  Phase 2 decisions: Include=115, Exclude=671, Uncertain=13
          ↓
ELIGIBILITY (3_eligibility/)
  Full-text assessed: 147 (115 from DB + 16 supplementary + 16 from citation tracking)
  Excluded (no PDF access): 50
          ↓
INCLUSION (4_inclusion/)
  Final coded papers: N = 97
    - Database-sourced: 81 (papers #1–#128)
    - Supplementary (HCI/human factors): 16 (papers #129–#145)
```

## Directory Structure

### `1_identification/` — Database Exports (Raw)
| File | Description |
|------|-------------|
| `WoS_new.xls` | Web of Science export (2015–2026) |
| `Scopus_revised.csv` | Scopus export (2015–2026) |
| `PsycINFO_ProQuest.xls` | PsycINFO via ProQuest export (2015–2026) |

**Search query:** `("trust" OR "trustworthiness") AND ("artificial intelligence" OR "AI" OR "generative AI" OR "ChatGPT" OR "large language model") AND ("education" OR "learning" OR "student" OR "learner")`

### `2_screening/` — Title/Abstract Screening
| File | Description |
|------|-------------|
| `phase1_cleaned.csv` | Deduplicated records after Phase 1 cleanup (N=799) |
| `phase1_removal_log.json` | Log of removed records (duplicates, non-English, non-articles) |
| `phase2_final_results.json` | Phase 2 screening decisions (I=Include, X=Exclude, U=Uncertain) |
| `phase2a_rule_based.json` | Initial rule-based screening results |
| `screening_batches/` | Batch-by-batch screening records (8 batches) |

### `3_eligibility/` — Full-Text Assessment
| File | Description |
|------|-------------|
| `paper_numbering.json` | Master list of 147 papers with numbering scheme (#1–#145) |
| `additional_papers_tracking.csv` | Supplementary papers identified via citation tracking (n=19) |
| `pdf_inventory.json` | PDF availability status for all papers |

### `4_inclusion/` — Final Coded Papers (N=97)

#### `4_inclusion/coding/`
| File | Description |
|------|-------------|
| `coding_results_all.json` | Complete coding data (97 papers × 32 fields + domain classification) |
| `coding_results_all.xlsx` | **Excel version** with 3 sheets: Coded Papers, Domain Summary, Key Statistics |
| `quantitative_analysis.md` | Descriptive statistics and cross-tabulations |

#### `4_inclusion/instruments/`
| File | Description |
|------|-------------|
| `TCS_Coding_Manual_v1.docx` | Trust Calibration Scaffolds Coding Manual (32 coding fields) |
| `TCS_Coding_Manual_Appendix_D_Domain_Classification.md` | Appendix D: 5-Domain Research Orientation Typology classification rules |
| `TCS_screening_coding_v1.xlsx` | Original screening and coding worksheet |

#### `4_inclusion/pdfs/`
Contains 16 supplementary PDFs (papers #129–#145) from HCI/human factors literature.
Database-sourced PDFs (#1–#128) are stored locally but not included in the repository due to copyright restrictions.

## Research Orientation Typology (5 Domains)

| Domain | Label | N | % | Classification Rule |
|--------|-------|---|---|---------------------|
| D1 | Trust Adoption | 5 | 5.2% | TAM/UTAUT/DOI framework only |
| D2 | Trust Conceptualization | 11 | 11.3% | General trust discussion |
| D3 | Trust Design | 24 | 24.7% | Scaffold proposed, no calibration |
| D4 | Trust Awareness | 41 | 42.3% | Overtrust/undertrust recognized |
| D4a | — Overtrust Recognition | 16 | 16.5% | Only overtrust discussed |
| D4b | — Undertrust Recognition | 18 | 18.6% | Only undertrust discussed |
| D4c | — Bidirectional Awareness | 7 | 7.2% | Both directions discussed |
| D5 | Trust Calibration | 16 | 16.5% | Calibration explicitly addressed |

## Coding Scheme (32 Fields)

Core variables: `paper_no`, `authors`, `year`, `title`, `doi`, `source`, `study_type`, `methodology`, `sample_context`, `ai_system_type`, `sample_size`, `trust_definition`, `trust_construct`, `trust_dimension`, `theoretical_framework`, `framework_depth`, `trust_measured`, `measurement_type`, `calibration_measured`, `instrument_name`, `addresses_calibration`, `overtrust_discussed`, `undertrust_discussed`, `scaffold_proposed`, `scaffold_type`, `oversight_design`, `calibration_notes`, `relevance_score`, `key_finding`, `notes`

Derived variables: `research_domain` (D1–D5), `research_subdomain` (D4a/D4b/D4c)
