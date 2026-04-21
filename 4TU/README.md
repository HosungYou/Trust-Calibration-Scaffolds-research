# 4TU Loan Approval Reliance Dataset

This directory contains the reproducible analysis scaffold for the 4TU loan
approval reliance dataset:

<https://doi.org/10.4121/f211863d-331b-44e5-a184-c21a18ac831a>

The local raw deposit and extracted files are intentionally excluded from git.
They should be downloaded from the DOI and placed locally under `4TU/` before
rebuilding the processed files.

## Files

- `scripts/build_4tu_calibration_dataset.py` rebuilds the trial-level and
  participant-level calibration datasets.
- `scripts/run_4tu_baseline_models.R` runs the baseline mixed-effects models.
- `scripts/run_4tu_robustness.py` runs supplemental task-fixed-effects and
  user-clustered robustness checks for the manuscript.
- `scripts/generate_hf_apa7_draft.py` regenerates the Human Factors-oriented
  APA 7 draft, including the theoretical framework figure.
- `processed/4tu_trial_level_calibration.csv` is the generated trial-level
  analysis dataset.
- `processed/4tu_participant_summary_calibration.csv` is the generated
  participant-level summary dataset.
- `processed/data_profile.md` reports key counts and descriptive rates.
- `processed/model_outputs/` stores baseline model output files.
- `manuscript/Beyond_Over_Reliance_APA7_Draft.md` is the working manuscript
  draft in Markdown.
- `manuscript/Beyond_Over_Reliance_APA7_Draft.docx` is the APA 7-style Word
  draft for review and revision.
- `manuscript/figures/Figure_1_Theoretical_Framework.png` is the
  construct-to-measurement framework figure.
- `manuscript/robustness_outputs/` stores supplemental robustness outputs.
- `docs/4tu_trust_calibration_analysis_plan.md` documents the analysis plan.
- `docs/4tu_manuscript_content_strategy.md` documents the manuscript direction.

## Manuscript Rebuild

After rebuilding the processed calibration files, run:

```bash
python3 4TU/scripts/run_4tu_robustness.py
python3 4TU/scripts/generate_hf_apa7_draft.py
```

The Python manuscript scripts require `python-docx`, `pillow`, `pandas`,
`numpy`, `scipy`, and `statsmodels`.

## Positioning

The 4TU data are best treated as a behavioral reliance calibration measurement
study, not as direct evidence that educational AI scaffolds improve learning.
The main contribution is to separate over-reliance on wrong AI advice from
under-reliance on correct AI advice using diagnostic trials where the
participant's initial decision disagreed with the AI recommendation.

For manuscript development, the preferred venue family is human factors,
cognitive engineering, or HCI/decision-support rather than education-AI
journals. The education connection should be framed as a measurement bridge for
later scaffold design.
