# Humanization Report: G5 Audit + G6 Transformation

**Date:** 2026-03-10
**Pipeline:** Diverga G5 (Audit) + G6 (Balanced Mode Transformation)
**Target:** TCRS_Theoretical_Background_APA7.docx

---

## Phase 1: Em Dash Removal

| Metric | Value |
|--------|-------|
| Em dashes found | 93 |
| Em dashes remaining | 0 |
| Replacement rules | 60 (paired em dashes = 1 rule per pair) |
| Word-loss fixes | 15 paragraphs corrected |

### Replacement Strategy
- Paired (parenthetical) -> commas `, X,` (~70%)
- Paired (list/naming) -> parentheses `(X)` (~5%)
- Single (appositive) -> comma `, X` (~15%)
- Single (elaboration) -> colon `: X` (~5%)
- Single (new sentence) -> period `. X` (~3%)
- Special (caption/title) -> colon/parentheses (~2%)

---

## Phase 2: G5 Audit Results

| Metric | Score |
|--------|-------|
| AI Probability Score | 67/100 (MEDIUM Risk) |
| Burstiness CV | 0.24 (AI range; human = 0.40-0.65) |
| MTLD (vocabulary diversity) | 68 (low-end AI range; human = 75-95) |
| Active patterns | 17/28 |
| HIGH severity | 4 patterns |
| MEDIUM severity | 8 patterns |
| LOW severity | 5 patterns |

### HIGH Severity Patterns
1. **P1**: "It is important to note" (6 instances)
2. **X1**: Hedge-intensifier sandwich (11 instances, 3 identical in section 2.4)
3. **L1**: Hedging overuse (31+ instances)
4. **S2**: Uniform sentence length (CV = 0.24)

---

## Phase 3: G6 Transformation (Balanced Mode)

### Changes Applied

**Priority 1 (HIGH impact, LOW effort):**
- P1: Deleted all 6 "It is important to note" + 7 "Importantly,"
- X3: Deleted all "follows established precedent" (3 instances)
- P5: Replaced weak conclusion with concrete claim
- X1: Simplified hedge-intensifier patterns

**Priority 2 (HIGH impact, MEDIUM effort):**
- S9: Section 1.3 opening changed from taxonomy to argument
- D2: Varied paragraph openings (2 modified)

**Priority 3 (MEDIUM impact):**
- L1: Reduced hedging in Limitations ("is expected to be" -> direct assertion)
- S3: Fixed comma splice from em-dash removal (colon substitution)
- M3: Removed redundant "see Table 1" references

### Before/After Examples

| Pattern | Before | After |
|---------|--------|-------|
| P1 | "It is important to note that the process model describes..." | "The process model describes..." |
| P1 | "Importantly, CA-Aw measures..." | "CA-Aw measures..." |
| X3 | "This approach follows established precedent. The MSLQ..." | "The MSLQ similarly uses..." |
| P5 | "...may prove to be one of the most important literacies..." | "...constitutes a core literacy that educators can no longer afford to leave unmeasured." |
| S9 | "The field of AI literacy measurement has grown rapidly..." | "Sixteen validated AI literacy scales now exist..., yet none addresses..." |
| L1 | "Self-report validity is expected to be strongest for..." | "Self-report validity is strongest for..." |
| D2 | "The scope of this problem is substantial." | "How widespread is the problem?" |

### Estimated Post-Transformation Score
- Pre-transformation: 67/100
- Post-transformation (estimated): 45-50/100 (MEDIUM -> LOW Risk)

---

## Remaining Opportunities (Not Yet Applied)

1. **S2**: Insert 6-8 short sentences (<12 words) for burstiness improvement
2. **S6/S8**: Further vary subscale paragraph structures in section 2.4
3. **D2**: More paragraph opening variation (6 more targets)
4. **L3**: Nominalization reduction in body text
5. **D4**: Discussion through-line argument strengthening

These would require more extensive rewriting and are recommended for the next revision pass.
