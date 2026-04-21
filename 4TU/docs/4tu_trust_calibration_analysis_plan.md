# 4TU Loan Approval Dataset: Trust/Reliance Calibration Analysis Plan

LongTable consulted: Measurement Auditor + Methods Critic.

## 1. Purpose

This dataset should be used as a **behavioral trust/reliance calibration measurement study**, not as direct evidence that educational AI scaffolds improve learning.

The strongest use is to test whether accuracy information and analogy-based explanation change the quality of human reliance on AI advice:

> Do people become more appropriately reliant on AI advice when the system communicates its stated accuracy, and does analogy-based accuracy explanation improve or distort that calibration?

This is a better fit than EdNet for calibration measurement because the dataset contains:

- a participant decision before AI advice,
- AI advice,
- a participant decision after AI advice,
- known correct loan decision,
- deliberately wrong AI advice flags,
- experimental groups: system-only, stated accuracy, analogy,
- post-task trust/automation attitudes and numeracy/affinity measures.

It is weaker than a purpose-built educational AI scaffold study because it is not educational, not longitudinal in the learning sense, and does not include scaffold fading or adaptive intervention logs.

## 2. Lessons Carried Over From EdNet and Chess

### EdNet lesson

Do not treat platform usage as trust. EdNet's `adaptive_offer` behavior was closer to feature adoption than an explicit accept/reject decision. The 4TU dataset avoids this problem by providing pre-advice and post-advice choices on each task.

### Chess lesson

Trial-level alignment between AI correctness and human follow/ignore behavior is the right measurement unit. Chess showed that `follow AI | AI correct` and `follow AI | AI wrong` separate over-reliance from under-reliance more cleanly than a raw subtraction gap.

### 4TU consequence

The primary analysis should focus on **diagnostic trials**, where the participant's initial choice disagrees with the AI advice. If the participant already agreed with the AI before advice, final agreement cannot identify whether the AI changed their judgment.

## 3. Construct Map

| Construct | 4TU operational variable | Strength | Notes |
|---|---|---:|---|
| AI reliability | `ai_correct` | High | Reconstructed from correct loan label and wrong-advice flag. |
| Behavioral reliance | `final_follows_ai` | Medium | Agreement with AI after advice; includes non-diagnostic cases. |
| Advice uptake | `switch_to_ai` | High | Best reliance measure; restricted to initial disagreement. |
| Appropriate reliance | `appropriate_reliance_diagnostic` | High | On diagnostic trials, final correctness captures whether participant moved to the better source. |
| Over-reliance | `over_reliance` | High | AI wrong and participant follows AI on a diagnostic trial. |
| Under-reliance | `under_reliance` | High | AI correct and participant rejects AI on a diagnostic trial. |
| Trust attitude | TiA subscales | Medium | Treat as subjective trust, not behavior. |
| Calibration sensitivity | `reliance_sensitivity` | Medium | Participant-level `P(follow AI | AI correct) - P(follow AI | AI wrong)`; can be missing when a participant lacks both diagnostic advice types. |

Avoid using raw `final_follows_ai - ai_correct` as a calibration score. That repeats the EdNet problem of subtracting conceptually different quantities. Prefer conditional rates and model interactions.

## 4. Generated Analysis Files

The preprocessing script is:

`4TU/scripts/build_4tu_calibration_dataset.py`

It generates:

- `4TU/processed/4tu_trial_level_calibration.csv`
- `4TU/processed/4tu_participant_summary_calibration.csv`
- `4TU/processed/data_profile.md`

Current profile:

- Trial rows: 5,786
- Participant rows: 529
- Main experiment: 281 participants, 2,810 task trials
- Follow-up study: 248 participants, 2,976 task trials
- Diagnostic trials: 3,048 total

The profile suggests a notable under-reliance pattern: under-reliance rates are larger than over-reliance rates in every condition-level summary. This matches the earlier EdNet/Chess lesson that calibration failure is not only overtrust.

## 5. Research Questions

### RQ1. Accuracy communication and calibration

Does stated system accuracy improve appropriate reliance compared with system-only advice?

Primary contrast:

- `system` vs `accuracy` in the main experiment.

Primary outcome:

- `appropriate_reliance_diagnostic`.

Secondary outcomes:

- `switch_to_ai`
- `over_reliance`
- `under_reliance`
- `final_correct`
- `accuracy_gain`

### RQ2. Analogy explanation and calibration

Does analogy-based explanation improve reliance calibration beyond numeric stated accuracy?

Primary contrast:

- `accuracy` vs `analogy` in the main experiment.

Follow-up contrast:

- within-subject differences across `analogy_domain` in the follow-up study: `train`, `weather`, `vaccine`.

Interpretive caution:

An analogy may increase perceived understanding or trust without improving appropriate reliance. That distinction is central to this paper.

### RQ3. Over-reliance vs under-reliance asymmetry

Which calibration failure dominates?

Primary outcomes:

- `over_reliance`
- `under_reliance`

Expected contribution:

If under-reliance dominates, this supports the broader research program's counter-narrative that AI education policy should not focus only on overtrust.

### RQ4. Individual differences

Do numeracy, affinity for technology interaction, and TiA trust subscales predict reliance quality?

Participant-level predictors:

- `Numeracy_level`
- `ATI`
- `TiA-Reliability/Competence`
- `TiA-Understanding/Predictability`
- `TiA-Propensity to Trust`

Interpretive caution:

Subjective trust should be modeled as a predictor or correlate of reliance, not as interchangeable with reliance.

## 6. Recommended Models

### Model 1: Primary diagnostic trial model

Use diagnostic trials only:

```text
appropriate_reliance_diagnostic ~ user_group * ai_correct
                                + task_position
                                + (1 | user_id)
                                + (1 | task_id)
```

In Python:

```text
logit(appropriate_reliance_diagnostic)
```

In R:

```r
glmer(appropriate_reliance_diagnostic ~ user_group * ai_correct +
      task_position + (1 | user_id) + (1 | task_id),
      family = binomial, data = diagnostic_main)
```

Why this model:

- It avoids non-diagnostic agreement trials.
- It controls repeated measures by participant and task.
- It tests whether condition changes calibration differently when AI is correct vs wrong.

### Model 2: Over-reliance model

Use diagnostic trials where AI advice is wrong:

```text
over_reliance ~ user_group
              + task_position
              + initial_correct
              + (1 | user_id)
              + (1 | task_id)
```

This tests whether explanations increase harmful deference to wrong AI advice.

### Model 3: Under-reliance model

Use diagnostic trials where AI advice is correct:

```text
under_reliance ~ user_group
               + task_position
               + initial_correct
               + (1 | user_id)
               + (1 | task_id)
```

This tests whether participants fail to benefit from correct AI advice.

### Model 4: Final decision accuracy

Use all trials:

```text
final_correct ~ user_group * ai_correct
              + initial_correct
              + final_follows_ai
              + task_position
              + (1 | user_id)
              + (1 | task_id)
```

This is an outcome model, not a calibration model. It answers whether reliance behavior improves final task performance.

### Model 5: Participant-level sensitivity

Use participant summaries:

```text
reliance_sensitivity ~ user_group
                     + Numeracy_level
                     + ATI
                     + TiA subscales
```

Use this as a secondary analysis because participant-level sensitivity can be missing or noisy when participants have few diagnostic trials in both AI-correct and AI-wrong categories.

## 7. Reporting Strategy

Report three layers:

1. **Measurement layer**: diagnostic trial counts, AI-correct vs AI-wrong distribution, switch-to-AI rates.
2. **Calibration layer**: appropriate reliance, over-reliance, under-reliance, reliance sensitivity.
3. **Outcome layer**: final accuracy and accuracy gain from initial to final decision.

This prevents a common reviewer objection: better final accuracy does not necessarily mean better trust calibration, and higher AI agreement does not necessarily mean appropriate reliance.

## 8. Fit to the Broader Research Program

This dataset should be framed as:

> A construct-valid behavioral testbed for reliance calibration mechanisms that can inform educational AI scaffold design.

Do not frame it as:

> Direct evidence that educational trust calibration scaffolds improve learner trust.

The bridge to the education project is methodological: 4TU shows how to measure calibration properly when AI correctness and human advice uptake are both observable.

## 9. Next Implementation Step

Run model scripts on `4TU/processed/4tu_trial_level_calibration.csv`. The first executable target should be a descriptive + logistic baseline:

1. descriptives by `study`, `user_group`, `ai_correct`, and `diagnostic_trial`;
2. main-experiment diagnostic model for `appropriate_reliance_diagnostic`;
3. separate over-reliance and under-reliance models;
4. follow-up within-subject comparison by `analogy_domain`.

## 10. Baseline Model Outputs Created

The executable baseline model script is:

`4TU/scripts/run_4tu_baseline_models.R`

It writes outputs to:

`4TU/processed/model_outputs/`

Generated files:

- `descriptive_rates_by_condition.csv`
- `participant_level_rates.csv`
- `model_1_main_appropriate_reliance.txt`
- `model_2_main_over_reliance_wrong_ai.txt`
- `model_3_main_under_reliance_correct_ai.txt`
- `model_4_followup_analogy_domain.txt`

Preliminary read:

- In the main experiment, stated accuracy and analogy conditions do not show clear improvements in diagnostic appropriate reliance relative to system-only advice in the baseline mixed model.
- Over-reliance on wrong AI advice is not clearly reduced by the accuracy or analogy conditions.
- Under-reliance on correct AI advice is large descriptively across all conditions, and task position predicts under-reliance in the baseline main-experiment model.
- In the follow-up study, diagnostic appropriate reliance is significantly lower when AI advice is correct than when it is wrong, which is a strong under-reliance signal. Analogy-domain differences are not clear in the baseline model.

Interpret these as baseline checks, not manuscript-ready inferential claims. The next statistical refinement should add planned contrasts, robustness checks for participant exclusion, and clearer handling of participant-level sensitivity scores with missing one-sided diagnostic cells.
