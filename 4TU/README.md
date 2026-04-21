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
- `processed/4tu_trial_level_calibration.csv` is the generated trial-level
  analysis dataset.
- `processed/4tu_participant_summary_calibration.csv` is the generated
  participant-level summary dataset.
- `processed/data_profile.md` reports key counts and descriptive rates.
- `processed/model_outputs/` stores baseline model output files.
- `docs/4tu_trust_calibration_analysis_plan.md` documents the analysis plan.
- `docs/4tu_manuscript_content_strategy.md` documents the manuscript direction.

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
