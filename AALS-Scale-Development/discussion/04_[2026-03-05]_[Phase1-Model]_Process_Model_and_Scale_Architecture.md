# Phase 1: Process Model and Scale Architecture

**Date:** 2026-03-05
**Status:** Model confirmed, proceeding to item development
**Key Decision:** Process model adopted over parallel 3D model

---

## 1. The Process Model (Researcher's Insight)

### 1.1 Origin

From the researcher's handwritten sketch: a regression line represents the ideal relationship between trust and AI reliability. A learner stands at the optimal point. Trust can push them up (overtrust) or down (distrust). The sketch identified two key cognitive operations:

1. **Knowing where they are → Metacognition**
2. **Knowing where is optimal point → Calibration**

### 1.2 The Process Model

```
METACOGNITION (Foundation)
  "Do I know how much I currently trust this AI?"
  = Self-monitoring of one's own trust state
  Includes: AI system understanding + task context recognition
      ↓
TRUST (Variable / Force)
  "Is this trust level pushing me toward overtrust or distrust?"
  = The force that displaces from optimal
  This is what is BEING calibrated, not what does the calibrating
      ↓
HUMAN AGENCY (Regulation Mechanism)
  "Do I recognize the gap and actively adjust?"
  = Intentional evaluation, comparison, and regulation behavior
      ↓
CALIBRATION (Outcome)
  "Have I reached appropriate trust for this situation?"
  = Trust matches AI reliability = optimal point reached
```

### 1.3 Theoretical Grounding

| Component | Theory | Key Concept |
|-----------|--------|-------------|
| Metacognition | Winne & Hadwin (1998) | Self-monitoring in SRL — awareness of one's cognitive state |
| Trust | Lee & See (2004) | Trust as attitude influencing reliance; overtrust → misuse, distrust → disuse |
| Human Agency | Bandura (2001) | Intentionality, self-reactiveness, self-reflectiveness |
| Calibration | SRL Calibration (Stone, 2000) | Accuracy of self-judgments relative to actual performance |

### 1.4 Why This Is Better Than the Parallel 3D Model

| Issue | Old 3D Parallel Model | New Process Model |
|-------|----------------------|-------------------|
| Relationship between dimensions | Unclear — why these 3? | Clear — foundation → variable → mechanism → outcome |
| Role of trust | Absent as explicit concept | Central — trust is the variable being calibrated |
| Role of metacognition | Implicit in CA | Explicit foundation — knowing where you are |
| Role of agency | One of 3 parallel dimensions | The mechanism that enables calibration |
| Theoretical coherence | Three separate theories cited | Three theories connected in a causal process |
| Visual metaphor | Abstract 2x2x2 cube | Intuitive — person on regression line, pushed up/down |

### 1.5 The Regression Line Metaphor (Figure 1 for Paper)

```
Y-axis: Trust Level (learner's subjective trust in AI)
X-axis: AI Reliability (actual AI performance/accuracy)

Diagonal line = Perfect Calibration (trust matches reliability)

Person at optimal point on the line:
  ↑ Over-trust (above line): trusting more than AI deserves
  ↓ Distrust (below line): trusting less than AI deserves
  ★ Calibrated: trust matches reliability

Metacognition = knowing WHERE on this space you currently are
Calibration knowledge = knowing WHERE the optimal point is
Agency = the ACT of moving toward the optimal point
```

---

## 2. Scale Architecture Under the Process Model

### 2.1 Three Subscales as Process Stages

The three subscales are NOT independent parallel constructs. They are **sequential stages of a single calibration process**, measured as parallel subscales within one instrument:

| Subscale | Process Stage | What It Measures | Response Format |
|----------|--------------|-----------------|-----------------|
| **Subscale 1: Calibration Awareness** (CA-Aw) | Recognition | Awareness of one's own trust state + AI/task context | 7-point Likert (Agree-Disagree) |
| **Subscale 2: Calibration Judgment** (CA-Jd) | Evaluation | Ability to judge whether trust is appropriate for the situation | 7-point Likert (Agree-Disagree) |
| **Subscale 3: Calibration Action** (CA-Ac) | Regulation | Active behaviors to verify, compare, and adjust trust | 7-point Likert (Never-Always) |

### 2.2 Mapping from Old to New

| Old 3D Model | New Process Model | Change |
|-------------|-------------------|--------|
| AAR (AI Autonomy Recognition) | Folded into **Subscale 1: Calibration Awareness** | AAR items become part of "context recognition" within awareness |
| TTD (Task-Specific Trust Differentiation) | Folded into **Subscale 2: Calibration Judgment** | TTD items become part of "situational evaluation" within judgment |
| CA (Calibration Agency) | Becomes **Subscale 3: Calibration Action** | Reframed as the behavioral output of the process |

### 2.3 Can Three Parallel Subscales Measure a Sequential Process?

**Yes, this is standard practice.** Examples:

- **MSLQ (Motivated Strategies for Learning Questionnaire):** Measures SRL stages (planning, monitoring, regulation) as parallel subscales within one instrument, even though they are theoretically sequential
- **MAI (Metacognitive Awareness Inventory):** Knowledge of cognition + Regulation of cognition — two phases of metacognition measured as parallel subscales
- **Clinical thermometer analogy:** A single blood test measures three sequential markers (absorption → processing → output) simultaneously

The key: each subscale measures the learner's **readiness/capacity** at that stage, not the real-time execution of the process. A cross-sectional survey captures a snapshot of preparedness at each stage.

### 2.4 Subscale Independence vs. Correlation

Expected empirical pattern:
- **Moderate positive correlations** between subscales (r = .40-.60) — theoretically expected because people strong in metacognition tend to show better judgment and action
- **Not identical** — a person can have high awareness but low action (knows but doesn't act), or high action but low awareness (acts habitually without reflective awareness)
- **Bifactor model** may reveal a general factor ("calibration readiness") plus specific factors at each stage
- **This is healthy** — moderate correlation supports both a total score and subscale-level interpretation

---

## 3. Revised Paper Direction

### 3.1 Title Options

1. "Trust Calibration in Educational AI: A Process Model and Scale Development"
2. "From Metacognition to Calibration: Developing a Scale for Trust Calibration Readiness in Educational AI"
3. "Knowing Where You Stand: A Process Model and Scale for Trust Calibration Readiness in AI-Enhanced Education"

### 3.2 Paper Story Line

```
1. PROBLEM (from SLR, Paper 1)
   → 83.5% of studies below calibration threshold
   → No instrument measures learner-side calibration readiness

2. THEORETICAL FRAMEWORK
   → Calibration is a PROCESS, not a trait
   → Three stages: Awareness (Winne) → Trust evaluation (Lee & See) → Agency (Bandura)
   → Visual: regression line metaphor (Figure 1)

3. SCALE DEVELOPMENT
   → Item pool from theory + existing scales + expert panel + cognitive interviews
   → Study 1: EFA (N=300-350) — how many factors emerge? 2? 3? Data decides.
   → Study 2: CFA (N=300-350) + convergent/discriminant validity
   → Falsification built in: if subscales collapse, report honestly

4. RESULTS & DISCUSSION
   → Calibration Readiness profiles
   → Implications for AI literacy education
   → Limitations (cross-sectional, self-report, causal claims deferred)
   → Future: longitudinal validation of process sequence
```

### 3.3 Key Methodological Decisions Confirmed

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Scale format | Standard Likert (no SJT, no embedded tasks) | Feasibility, generalizability |
| Study design | Study 1 (EFA) + Study 2 (CFA + validity) | Standard scale development |
| Factor structure | EFA determines (2 or 3 factors) | Empirically honest |
| TTD falsification | CT scale included in Study 2 | If TTD ↔ CT r ≥ .60, fold into awareness |
| Construct framing | "Trust Calibration Readiness" | Self-report = readiness, not accuracy |
| Process vs. trait | Theorized as process; measured as readiness levels | Cross-sectional limitation acknowledged |
| Causal claims | Deferred to future longitudinal research | Honest about design limitations |

---

## 4. Next Steps

1. **Item pool development** (Phase 0) — generate 36-45 items mapped to the three process stages
2. **Expert panel** (Phase 1) — validate content against the process model
3. **Cognitive interviews** (Phase 2) — test whether learners understand the items
4. **OSF preregistration** — register before data collection
5. **Data collection** (Studies 1 & 2) — N = 600-700, online survey

---

## 5. Key References for the Process Model

- Bandura, A. (2001). Social cognitive theory: An agentic perspective. *Annual Review of Psychology, 52*, 1–26.
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80.
- Stone, N. J. (2000). Exploring the relationship between calibration and self-regulated learning. *Educational Psychology Review, 12*(4), 437–475.
- Winne, P. H., & Hadwin, A. F. (1998). Studying as self-regulated learning. In D. J. Hacker et al. (Eds.), *Metacognition in educational theory and practice*. Erlbaum.
- Schraw, G. (2009). Measuring metacognitive judgments. In D. J. Hacker et al. (Eds.), *Handbook of metacognition in education*. Routledge.
- Sperber, D., et al. (2010). Epistemic vigilance. *Mind & Language, 25*(4), 359–393.
