# Human Factors Manuscript Draft

This folder contains a working Human Factors-oriented manuscript draft based on
the 4TU loan approval reliance dataset.

## Files

- `Beyond_Over_Reliance_APA7_Draft.md`: Markdown source draft.
- `Beyond_Over_Reliance_APA7_Draft.docx`: APA 7-style Word draft.
- `figures/Figure_1_Theoretical_Framework.png`: Theoretical framework figure.
- `robustness_outputs/`: Supplemental robustness outputs generated from the
  processed 4TU calibration files.

## Rebuild

From the repository root:

```bash
python3 4TU/scripts/run_4tu_robustness.py
python3 4TU/scripts/generate_hf_apa7_draft.py
```

The manuscript-generation script writes both the Word and Markdown drafts. The
robustness script writes the task-fixed-effects models, planned condition
contrasts, and descriptive RAIR-minus-RSR checks.

## Scope

The draft is a secondary analysis, not a final submission package. Its central
claim is measurement-oriented: diagnostic trials can distinguish warranted AI
advice uptake from over-reliance and under-reliance. The 4TU loan approval task
is treated as a Human Factors and decision-support dataset, with educational AI
implications framed as a measurement bridge for future scaffold studies.
