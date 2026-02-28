# Systematic Search Strategy

## Overview

This document details the systematic literature search conducted for the scoping review on **Trust Calibration Scaffolds** in AI-assisted education.

- **Search date:** February 28, 2026
- **Databases:** Scopus, Web of Science (WoS), APA PsycINFO (via ProQuest)
- **Date range:** 2015--2026
- **Language:** English
- **Article type:** Peer-reviewed

---

## Search Queries

### 1. Scopus (951 results)

**Query:**
```
TITLE-ABS-KEY(
  ("trust in AI" OR "AI trust" OR "trust calibration" OR "calibrated trust"
   OR "overtrust" OR "over-trust" OR "undertrust" OR "over-reliance"
   OR "overreliance" OR "reliance on AI" OR "resistance to AI"
   OR "human-AI trust" OR "appropriate reliance" OR "appropriate trust"
   OR "trust in generative AI" OR "trust in ChatGPT"
   OR "trust in artificial intelligence" OR "AI trustworthiness"
   OR "trustworthy AI" OR "misplaced trust" OR "trust repair")
  AND
  ("higher education" OR "K-12" OR "intelligent tutoring" OR "AI tutor*"
   OR "AI-assisted learning" OR "AI chatbot*" OR "pedagogical agent*"
   OR "edtech" OR "classroom" OR "curriculum" OR "instructional"
   OR "student learning" OR "learner*" OR "undergraduate*"
   OR "educational technology" OR "online learning")
)
AND SUBJAREA(SOCI OR PSYC)
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND LANGUAGE(english)
```

**Filters:** Subject Area = Social Sciences OR Psychology

**Export file:** `Scopus_revised.csv`

---

### 2. Web of Science (188 results)

**Query:**
```
TS=(
  ("trust in AI" OR "AI trust" OR "trust calibration" OR "calibrated trust"
   OR "overtrust" OR "undertrust" OR "over-trust" OR "reliance on AI"
   OR "resistance to AI" OR "human-AI trust" OR "appropriate trust"
   OR "trust in generative AI" OR "trust in ChatGPT"
   OR "trust in artificial intelligence" OR "AI trustworthiness"
   OR "trustworthy AI")
  AND
  ("education*" OR "learning" OR "teaching" OR "higher education"
   OR "university" OR "K-12" OR "intelligent tutoring" OR "AI tutor*"
   OR "ChatGPT" OR "generative AI" OR "LLM" OR "edtech"
   OR "AI-assisted learning" OR "AI chatbot" OR "conversational agent")
)
AND PY=(2015-2026)
```

**Filters:** Web of Science Category = Education Educational Research

**Export file:** `WoS_new.xls`

---

### 3. APA PsycINFO via ProQuest (70 results)

**Query:**
```
(SU.EXACT("Trust") OR SU.EXACT("Distrust")
 OR ab("trust in AI" OR "AI trust" OR "trust calibration"
       OR "overtrust" OR "over-trust" OR "overreliance"
       OR "over-reliance" OR "appropriate reliance"
       OR "human-AI trust" OR "AI trustworthiness"
       OR "trustworthy AI"))
AND
ab("education" OR "higher education" OR "student*" OR "learner*"
   OR "K-12" OR "intelligent tutoring" OR "AI tutor*"
   OR "AI-assisted learning" OR "AI chatbot*"
   OR "pedagogical agent*" OR "classroom" OR "curriculum")
AND
ab("artificial intelligence" OR "generative AI" OR "ChatGPT"
   OR "large language model*" OR "LLM")
```

**Filters:** Peer Reviewed, 2015--2026, APA PsycINFO database only

**Export file:** `PsycINFO_ProQuest.xls`

---

## Results Summary

| Database | Results | Export Format | File |
|---|---|---|---|
| Scopus | 951 | CSV | `resource/Scopus_revised.csv` |
| Web of Science | 188 | XLS | `resource/WoS_new.xls` |
| PsycINFO (ProQuest) | 70 | XLS | `resource/PsycINFO_ProQuest.xls` |
| **Total (before dedup)** | **1,209** | | |

## Query Design Rationale

### Two-block structure
- **Block 1 (Trust):** AI-specific trust terms only (e.g., "trust in AI", "trust calibration", "overtrust"). General "trust" alone was avoided to prevent excessive noise from non-AI trust research.
- **Block 2 (Education):** Education-specific context terms. Standalone broad terms like "learning" (which captures machine learning papers) and "university" (which captures any university-affiliated study) were removed in the revised Scopus query.

### Key decisions
1. **Removed "distrust" from Scopus trust block** -- too broad without AI qualifier; captures general distrust studies in social psychology.
2. **Removed "ChatGPT", "generative AI", "LLM" from Scopus education block** -- these AI technology terms caused non-education AI papers to match. Trust block already captures "trust in ChatGPT" and "trust in generative AI".
3. **Added SUBJAREA(SOCI OR PSYC) to Scopus** -- excludes Computer Science and Engineering papers focused on technical trustworthiness.
4. **WoS uses Education category filter** -- more granular than Scopus subject areas; directly limits to education research.

### Iteration history
| Iteration | Scopus results | Change |
|---|---|---|
| v1 (initial) | 21,085 | Too broad; standalone "trust" in trust block |
| v2 | 7,934 | Compound AI-trust terms only |
| v3 | 3,056 | Added SUBJAREA(SOCI OR PSYC) |
| v4 (final) | 951 | Removed broad standalone terms from education block |

## Next Steps

1. **Deduplication** across all three databases (DOI + title matching)
2. **Title/Abstract screening** using inclusion/exclusion criteria
3. **Full-text review** of remaining articles
4. **Data extraction and synthesis**
