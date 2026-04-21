# 4TU Manuscript Content Strategy

## Working Identity

This manuscript should be written as a behavioral reliance calibration paper:

> AI advice calibration is not only a problem of excessive trust. In this
> dataset, users often failed to rely on correct AI advice, and simple accuracy
> disclosure or analogy-based explanation did not clearly correct that
> miscalibration.

The paper should not be framed as direct evidence that educational AI trust
calibration scaffolds improve learning. The stronger and more defensible claim
is that the 4TU dataset provides a construct-valid behavioral testbed for
measuring reliance calibration, which can later inform educational scaffold
design.

## Target Venue Logic

### Primary target: Human Factors

This is the strongest fit if the manuscript foregrounds:

- appropriate reliance on automated advice,
- decision support,
- human-AI system design,
- under-reliance as a performance and safety problem,
- diagnostic behavioral measurement rather than self-reported trust alone.

The paper should read as a human factors contribution to the design and
evaluation of AI advice systems.

### Secondary target: Journal of Cognitive Engineering and Decision Making

This is a strong alternative if the manuscript foregrounds:

- how people use decision support under uncertainty,
- cognitive work with algorithmic recommendations,
- whether transparency cues change advice uptake,
- training and support needs for calibrated reliance.

### Backup targets: IJHCI or Computers in Human Behavior

IJHCI is viable if the paper emphasizes human-AI interaction and interface
design implications. Computers in Human Behavior is viable if the paper is
written as a behavioral experiment on AI advice taking, null disclosure effects,
and under-reliance asymmetry.

### Education-AI venues

Computers & Education: AI, IJAIED, AIED, EDM, and Learning at Scale are not the
best home for a 4TU-only manuscript. The loan approval task is not educational,
and the dataset has no learning outcomes, scaffold fading, classroom context, or
longitudinal learning process.

These venues become plausible only if 4TU is positioned as one part of a broader
measurement program that also includes EdNet, AI-assisted chess puzzle behavior,
or a future educational scaffold experiment.

## Suggested Title Options

1. Beyond Over-Reliance: Diagnostic Evidence of Under-Reliance in Human Reliance
   on AI Advice
2. When Accuracy Disclosure Is Not Enough: Behavioral Calibration in AI Advice
   Taking
3. Measuring Appropriate Reliance on AI Advice: Diagnostic Evidence from a Loan
   Approval Task
4. The Limits of Accuracy Disclosure and Analogy Explanation for Calibrating AI
   Advice Reliance

## Core Contribution

The paper should make three contributions:

1. **Measurement contribution**: It shows why diagnostic trials are necessary for
   measuring behavioral reliance. If the user already agreed with the AI before
   seeing advice, final agreement is not a clean reliance signal.
2. **Empirical contribution**: It shows that stated accuracy and analogy
   explanation did not produce clear improvements in appropriate reliance in the
   main experiment.
3. **Conceptual contribution**: It challenges an overtrust-only view of AI
   miscalibration by showing that under-reliance on correct AI advice can be the
   dominant calibration failure.

## Recommended Abstract Shape

The abstract should not promise an intervention success story. A defensible
abstract structure is:

1. AI advice systems require calibrated reliance, not simply higher trust.
2. Existing work often emphasizes over-reliance, but under-reliance on correct AI
   advice can also reduce decision quality.
3. This study reanalyzes the 4TU loan approval reliance dataset using diagnostic
   trials where participants initially disagreed with AI advice.
4. We separate appropriate reliance, over-reliance, and under-reliance by
   aligning human follow/ignore behavior with AI correctness.
5. Stated accuracy and analogy-based explanation did not clearly improve
   diagnostic reliance relative to system-only advice.
6. Across condition-level summaries, under-reliance was larger than
   over-reliance.
7. The findings suggest that transparency cues alone are insufficient and that
   AI advice interfaces need supports that help users decide when to accept or
   resist AI recommendations.

## Introduction Content

The introduction should open with the practical problem:

> AI advice systems increasingly support consequential decisions, but their
> value depends on whether users rely on them appropriately: accepting helpful
> advice while resisting erroneous recommendations.

Then narrow the problem:

- Trust is often discussed as a quantity to increase or decrease, but the design
  target is calibration.
- Over-reliance has received substantial attention because users may defer to
  wrong AI advice.
- Under-reliance is equally important because users may reject correct AI advice
  and lose the potential benefit of decision support.
- Accuracy disclosure and analogy explanation are plausible transparency
  strategies, but their behavioral effect on reliance quality is uncertain.

The introduction should end with the study purpose:

> We use the 4TU loan approval dataset to test whether stated accuracy and
> analogy-based explanation improve behavioral reliance calibration, and whether
> miscalibration is driven primarily by over-reliance or under-reliance.

## Theory And Construct Framing

The theory section must keep three constructs separate:

| Construct | Meaning in this paper | 4TU operationalization |
| --- | --- | --- |
| Trust | Subjective attitude toward the AI system | Post-task trust or automation-attitude scales |
| Reliance | Behavioral use of AI advice | Final decision follows AI advice |
| Calibration | Quality of reliance conditional on AI correctness | Follow correct AI, resist wrong AI |

The key construct-validity move is:

> We define diagnostic trials as trials in which the participant's initial
> decision disagreed with the AI advice. These trials are the primary unit for
> measuring reliance because post-advice agreement is behaviorally informative
> only when the participant had to switch toward or resist the AI.

This framing imports the main lesson from the earlier EdNet and chess analyses:

- EdNet warned against treating platform feature use as trust.
- Chess showed that follow/ignore behavior aligned with AI correctness is a
  stronger calibration unit.
- 4TU provides the clearest available structure because it includes initial
  decision, AI advice, final decision, and known correctness.

## Research Questions

Use research questions rather than strong confirmatory hypotheses, because the
current baseline results do not support clear condition effects.

### RQ1. Accuracy disclosure

Does stated accuracy information improve appropriate reliance relative to
system-only AI advice?

Primary contrast: `system` vs `accuracy`.

Primary outcome: `appropriate_reliance_diagnostic`.

### RQ2. Analogy explanation

Does analogy-based explanation improve reliance calibration beyond numeric
accuracy information?

Primary contrast: `accuracy` vs `analogy`.

Secondary follow-up: within-subject comparison of analogy domains in the
follow-up study.

### RQ3. Miscalibration asymmetry

Is miscalibration driven more by over-reliance on wrong AI advice or
under-reliance on correct AI advice?

Primary outcomes: `over_reliance` and `under_reliance`.

### RQ4. Individual differences

Do numeracy, affinity for technology interaction, and subjective trust predict
behavioral reliance quality?

This should remain secondary unless the individual-difference variables are
fully cleaned and modeled.

## Methods Content

### Dataset

Report the dataset as a secondary analysis of the 4TU loan approval reliance
dataset. The data include:

- pre-advice participant decision,
- AI advice,
- post-advice participant decision,
- correct loan label,
- experimental group assignment,
- post-task trust and technology attitude measures.

Current processed analysis files contain:

- 5,786 trial-level rows,
- 529 participant-level rows,
- 281 main-experiment participants,
- 248 follow-up-study participants,
- 3,048 diagnostic trials.

### Conditions

Main experiment groups:

- `system`: system-only advice,
- `accuracy`: AI advice with stated accuracy information,
- `analogy`: AI advice with analogy-based accuracy explanation.

Follow-up:

- `loan_analogy` group with analogy-domain variation.

### Primary Measures

Use these definitions:

- `final_follows_ai`: whether the post-advice decision matched AI advice.
- `switch_to_ai`: whether the participant switched to the AI advice after
  initially disagreeing with it.
- `appropriate_reliance_diagnostic`: whether the participant made the correct
  final decision on a diagnostic trial.
- `over_reliance`: AI advice was wrong and the participant followed it.
- `under_reliance`: AI advice was correct and the participant rejected it.
- `reliance_sensitivity`: `P(follow AI | AI correct) - P(follow AI | AI wrong)`
  within diagnostic trials.

Avoid presenting raw final agreement as calibration.

## Analysis Plan For Manuscript

### Primary model

Use diagnostic trials in the main experiment:

```r
glmer(
  appropriate_reliance_diagnostic ~ user_group * ai_correct +
    task_position + (1 | user_id) + (1 | task_id),
  family = binomial,
  data = diagnostic_main
)
```

This tests whether condition effects differ depending on whether the AI advice
was correct.

### Over-reliance model

Use diagnostic trials where AI advice was wrong:

```r
glmer(
  over_reliance ~ user_group + task_position +
    (1 | user_id) + (1 | task_id),
  family = binomial,
  data = main_wrong_ai
)
```

### Under-reliance model

Use diagnostic trials where AI advice was correct:

```r
glmer(
  under_reliance ~ user_group + task_position +
    (1 | user_id) + (1 | task_id),
  family = binomial,
  data = main_correct_ai
)
```

### Follow-up analogy-domain model

Use diagnostic trials in the follow-up study:

```r
glmer(
  appropriate_reliance_diagnostic ~ analogy_domain * ai_correct +
    task_block + (1 | user_id) + (1 | task_id),
  family = binomial,
  data = follow_diag
)
```

## Results Narrative

The current results should be narrated cautiously.

### Descriptive pattern

Participant-level means suggest that under-reliance was larger than
over-reliance across all condition-level summaries:

| Study | Group | Appropriate reliance | Over-reliance | Under-reliance |
| --- | ---: | ---: | ---: | ---: |
| Main | Accuracy | .467 | .113 | .420 |
| Main | Analogy | .374 | .109 | .518 |
| Main | System | .423 | .114 | .463 |
| Follow-up | Loan analogy | .397 | .068 | .535 |

This is the descriptive center of the paper. It supports the claim that
miscalibration is not only blind deference to wrong AI advice.

### Main mixed-effects model

The baseline diagnostic model did not show clear evidence that the accuracy or
analogy condition improved appropriate reliance relative to system-only advice.
The relevant condition coefficients and condition-by-AI-correct interactions
were not statistically clear.

Manuscript wording:

> We did not observe clear evidence that stated accuracy or analogy-based
> explanation improved diagnostic appropriate reliance.

Avoid:

> Accuracy information had no effect.

The stronger version requires equivalence or Bayesian evidence.

### Over-reliance model

The baseline over-reliance model did not show clear condition differences. This
means the analogy condition did not clearly increase harmful deference to wrong
AI advice, but it also did not clearly reduce it.

### Under-reliance model

The baseline under-reliance model did not show clear condition differences, but
task position was positively associated with under-reliance. This suggests that
participants may have become less willing to accept correct AI advice over time,
or that later tasks differed in ways that made correct AI advice less persuasive.

This should be treated as a pattern requiring robustness checks, not as a final
theoretical conclusion.

### Follow-up model

The follow-up model showed a strong negative association for `ai_correctTRUE` in
the appropriate-reliance model. This is consistent with the broader
under-reliance pattern: when the AI was correct, participants often failed to
take advantage of that correct advice.

## Discussion Structure

### Contribution 1: Calibration requires diagnostic behavior

The paper should argue that calibration cannot be inferred from final accuracy
or final AI agreement alone. A participant who agrees with the AI after advice
may already have agreed before seeing the advice. Diagnostic trials isolate the
moments when AI advice could actually change the participant's decision.

### Contribution 2: Transparency is not sufficient

Stated accuracy and analogy explanations are plausible transparency tools, but
the current evidence does not show that they reliably produce better behavioral
calibration. This supports a design implication:

> AI advice interfaces should not merely tell users how accurate a system is;
> they should help users recognize when the system is likely to be more or less
> reliable than their own judgment.

### Contribution 3: Under-reliance matters

The dominant descriptive pattern is under-reliance on correct AI advice. This
extends the literature beyond an overtrust-only view of AI risk. The cost of
miscalibration is not only that users follow wrong recommendations, but also
that they fail to benefit from correct recommendations.

### Contribution 4: Bridge to educational AI

The education connection should be deliberately modest:

> For educational AI, this finding matters because learning-support systems must
> help students decide when to use AI feedback, hints, or recommendations and
> when to rely on their own reasoning. However, the present data do not test
> learning outcomes directly. They provide a measurement bridge for future
> scaffold studies.

## Limitations

The limitations section should be explicit:

- The task is loan approval, not an educational task.
- The data are not longitudinal in a learning sense.
- The study does not include scaffold fading, classroom context, or learning
  outcomes.
- The baseline condition effects are weak or unclear.
- Participant-level reliance sensitivity may be noisy because each participant
  has a limited number of diagnostic trials.
- The results are secondary analyses of an existing dataset, so causal claims
  should stay close to the original experimental design.

## Wording To Use

Use:

- behavioral reliance calibration
- diagnostic trials
- appropriate reliance
- over-reliance and under-reliance
- no clear evidence of improved calibration
- transparency cues alone may be insufficient
- measurement bridge for educational AI scaffold design

Avoid:

- trust improved
- analogy improved calibration
- accuracy disclosure calibrated trust
- educational scaffolds were effective
- trust was behaviorally measured
- users trusted or distrusted AI unless supported by self-report scales

## Revision Checklist Before Submission

Before submitting, add these robustness checks:

1. Condition balance table, including initial accuracy by group.
2. Sensitivity model controlling for initial correctness or initial accuracy.
3. Planned contrasts only: `system` vs `accuracy`, `accuracy` vs `analogy`.
4. Multiple-comparison correction for secondary outcomes.
5. Equivalence test or Bayesian evidence for null disclosure effects.
6. Task fixed-effects or task-by-condition sensitivity checks.
7. Separate reporting of over-reliance and under-reliance.
8. Reliability or shrinkage treatment for participant-level reliance
   sensitivity.
9. Clear separation of behavioral reliance and subjective trust scales.

## One-Paragraph Manuscript Pitch

This paper reanalyzes the 4TU loan approval reliance dataset to examine whether
stated accuracy and analogy-based explanation calibrate users' behavioral
reliance on AI advice. We focus on diagnostic trials where participants'
initial decisions disagreed with AI advice, allowing reliance to be measured as
switching toward correct AI advice or resisting incorrect AI advice. Across the
main experiment and follow-up summaries, miscalibration was characterized more
by under-reliance on correct AI advice than by over-reliance on wrong advice.
Mixed-effects models provided no clear evidence that stated accuracy or analogy
explanation improved diagnostic appropriate reliance. The findings suggest that
transparency cues alone are insufficient for calibrated reliance and that future
AI advice systems, including educational AI systems, need scaffolds that help
users decide when AI advice should be accepted, questioned, or ignored.
