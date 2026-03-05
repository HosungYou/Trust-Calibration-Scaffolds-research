# Phase 1: Conceptualization — 3D Framework and Scale Design

**Date:** 2026-03-05
**Paper Title:** Agentic AI Literacy: A Three-Dimensional Framework and Scale Development for Trust Calibration in Educational AI
**Status:** Conceptualization
**Related:** Trust-Calibration-Scaffolds-research (SLR, Paper 1)

---

## 1. Origin and Motivation

### 1.1 From SLR to Scale Development

Paper 1 (SLR: "The Calibration Gap") identified that **83.5% of 97 studies** on trust in educational AI fall below the **calibration threshold** — the boundary between merely recognizing that trust matters (D4: Awareness) and actually measuring whether trust matches AI reliability (D5: Calibration). Critically, **zero studies** simultaneously measure both trust and AI reliability.

This finding raises a fundamental question: *How can learners calibrate trust if they cannot distinguish what kind of AI system they are interacting with, or what kind of task they are performing?*

### 1.2 The Agency Insight

The initial idea emerged from distinguishing **automation** from **agent**:
- **Automation**: AI that produces trackable, verifiable results (e.g., math problem solving, code generation) — reactive, deterministic
- **Agent**: AI that proactively reasons and generates outcomes for tasks requiring operational definition (e.g., essay feedback, career counseling) — proactive, autonomous

This led to a conceptual harmony:
- **AI Agent** (system-level agency): The AI's capacity for autonomous, proactive behavior
- **Human Agency** (learner-level agency): The learner's capacity to critically evaluate and calibrate trust

The interplay between these two forms of agency is what trust calibration ultimately requires.

---

## 2. Three-Dimensional Framework

### 2.1 Dimension 1: AI Autonomy (System Behavior)

**Theoretical Basis:** Wooldridge & Jennings (1995); Parasuraman, Sheridan, & Wickens (2000)

| Level | Label | Characteristics | Educational Example |
|-------|-------|----------------|-------------------|
| Low | Tool/Automation | Reactive, executes predefined functions, deterministic output | Spell checker, calculator, auto-grading |
| High | Agent | Proactive, reasons and discovers, generates emergent output | AI tutor adapting strategy, research assistant synthesizing literature |

**Key Distinction:** Not merely about complexity, but about whether the system exhibits autonomous goal-directed behavior (Wooldridge & Jennings' BDI model).

### 2.2 Dimension 2: Task Verifiability (Task Structure)

**Theoretical Basis:** Hammond (1987) Cognitive Continuum Theory; Simon (1973) well-structured vs. ill-structured problems

| Level | Label | Characteristics | Educational Example |
|-------|-------|----------------|-------------------|
| High | Intellective | Objectively verifiable correct answer exists | Math solutions, code compilation, factual Q&A |
| Low | Judgmental | Requires human evaluation, subjective criteria | Essay quality, counseling appropriateness, creative feedback |

**Key Distinction:** Verifiability is not synonymous with difficulty. A complex math proof is verifiable; a simple compliment on writing is not.

### 2.3 Dimension 3: Human Agency (Learner Behavior)

**Theoretical Basis:** Bandura (2001) Social Cognitive Theory; Winne & Hadwin (1998) SRL

| Level | Label | Characteristics | Behavioral Indicator |
|-------|-------|----------------|---------------------|
| Low | Passive Acceptance | Accepts AI output without evaluation | Copies AI suggestion directly, no verification |
| High | Active Calibration | Evaluates AI output against evidence and context | Checks AI answer, adjusts trust based on reliability signals |

**Key Distinction:** This is the learner's metacognitive capacity to regulate trust — the human-side complement to AI autonomy.

### 2.4 The 2×2×2 Interaction Space

The three binary dimensions create **8 cells**, each representing a distinct trust calibration scenario:

| AI Autonomy | Task Verifiability | Human Agency | Scenario | Calibration Difficulty |
|------------|-------------------|--------------|----------|----------------------|
| Low (Tool) | High (Intellective) | High (Active) | Student verifies calculator output | Easiest |
| Low (Tool) | High (Intellective) | Low (Passive) | Student blindly trusts auto-grader | Low risk, correctable |
| Low (Tool) | Low (Judgmental) | High (Active) | Student critically evaluates grammar suggestions | Moderate |
| Low (Tool) | Low (Judgmental) | Low (Passive) | Student accepts all writing feedback | Moderate risk |
| High (Agent) | High (Intellective) | High (Active) | Student verifies AI tutor's math reasoning | Challenging but feasible |
| High (Agent) | High (Intellective) | Low (Passive) | Student trusts AI coding assistant blindly | High risk, hidden errors |
| High (Agent) | Low (Judgmental) | High (Active) | Student evaluates AI counselor's advice critically | Hardest but most valuable |
| High (Agent) | Low (Judgmental) | Low (Passive) | Student follows AI career advice without question | **Most dangerous** |

**Core Argument:** Trust calibration difficulty increases multiplicatively as AI Autonomy rises and Task Verifiability decreases. Human Agency is the only modifiable dimension that can compensate.

---

## 3. Scale Design: Agentic AI Literacy Scale (AALS)

### 3.1 Overview

- **Construct:** Agentic AI Literacy — the capacity to recognize AI autonomy levels, differentiate trust by task verifiability, and actively calibrate trust
- **Format:** Self-report Likert scale (7-point, Strongly Disagree to Strongly Agree)
- **Target Population:** Higher education students (undergraduate and graduate)
- **Administration:** Online survey

### 3.2 Subscale 1: AI Autonomy Recognition (AAR)

*"Can the learner distinguish what kind of AI system they are interacting with?"*

**Example Items:**
1. I can distinguish between AI that follows fixed rules and AI that makes its own decisions.
2. I recognize when an AI system is proactively suggesting actions versus simply responding to my commands.
3. I understand that different AI tools operate with varying levels of independence.
4. When using AI tools, I consider how much autonomous decision-making the system performs.

**Item Pool Target:** 12–15 items → EFA reduction to 4–6 items

### 3.3 Subscale 2: Task-Specific Trust Differentiation (TTD)

*"Does the learner adjust trust based on whether the task has a verifiable answer?"*

**Example Items:**
1. I trust AI more for tasks where I can easily check if the answer is correct.
2. My confidence in AI-generated feedback changes depending on whether the task has a clear right answer.
3. I apply different standards when evaluating AI output for objective versus subjective tasks.
4. I am more cautious about AI suggestions when the task requires personal judgment.

**Item Pool Target:** 12–15 items → EFA reduction to 4–6 items

### 3.4 Subscale 3: Calibration Agency (CA)

*"Does the learner actively evaluate and adjust trust rather than passively accepting?"*

**Example Items:**
1. When an AI tool gives me a suggestion, I check it against other sources before accepting it.
2. I adjust my level of trust in AI tools based on my past experiences with their accuracy.
3. I actively seek evidence to confirm or challenge AI-generated outputs.
4. I change how much I rely on an AI tool depending on the specific situation.

**Item Pool Target:** 12–15 items → EFA reduction to 4–6 items

### 3.5 Scoring

- **Subscale scores:** Mean of items within each subscale
- **Total AALS score:** Mean of three subscale scores (if supported by higher-order factor analysis)
- **Profile interpretation:** Low AAR + High TTD + High CA = different intervention need than High AAR + Low TTD + Low CA

---

## 4. Methodology

### 4.1 Study Design Overview

| Study | Purpose | N | Method |
|-------|---------|---|--------|
| Study 1 | Item Development & EFA | 300 | Online survey |
| Study 2a | CFA & Convergent/Discriminant Validity | 300 | Online survey |
| Study 2b | Behavioral Validation | 80–100 | Online survey + task platform |

**Total N ≈ 700** (Study 1 + Study 2a can be collected simultaneously with random split)

### 4.2 Study 1: Item Development & EFA

**Phase 1: Item Pool Generation**
- Literature review → initial 40–45 items
- Expert panel review (5–7 experts in AI literacy, educational technology, psychometrics)
- Cognitive interviews (8–10 students) for clarity and comprehension
- Revised pool: ~36 items (12 per subscale)

**Phase 2: Data Collection & EFA**
- N = 300, online survey
- Platform: Qualtrics or similar
- Recruitment: University students across disciplines
- Inclusion: Currently using at least one AI tool for academic purposes

**Phase 3: Analysis**
- Parallel analysis + scree plot for factor retention
- EFA with oblique rotation (Promax or Geomin)
- Item retention criteria: loading ≥ .40, no cross-loading ≥ .32, communality ≥ .30
- Target: 4–6 items per subscale, 12–18 total items
- Reliability: Cronbach's α ≥ .70 per subscale

### 4.3 Study 2a: CFA & Validity

**Phase 4: Confirmatory Factor Analysis**
- N = 300, independent sample
- CFA fit criteria: CFI ≥ .95, RMSEA ≤ .06, SRMR ≤ .08
- Compare models: 3-factor correlated, 3-factor with higher-order, bifactor

**Phase 5: Convergent & Discriminant Validity**
- Convergent: Correlations with existing scales
  - AI Literacy Scale (Laupichler et al., 2023 or similar)
  - Digital Literacy Scale
  - Critical Thinking Disposition
- Discriminant: Low correlations with
  - General Self-Efficacy
  - Technology Anxiety (should be inversely related but distinct)
- Criterion validity: Correlation with self-reported AI usage patterns

### 4.4 Study 2b: Behavioral Validation (Substudy)

**Purpose:** Demonstrate that AALS scores predict actual trust calibration behavior

**Design:**
- n = 80–100 participants from Study 2a sample
- Task platform presenting AI-generated outputs across the 2×2 framework:
  - Tool × Intellective (calculator check)
  - Tool × Judgmental (grammar suggestion)
  - Agent × Intellective (AI tutor math explanation)
  - Agent × Judgmental (AI writing feedback)
- Each scenario: AI output with varying reliability (correct vs. subtly incorrect)
- Measure: Acceptance rate, verification behavior, trust adjustment

**AI System Construction Requirement:**
- **Full AI system is NOT needed**
- Use **pre-designed vignette/scenario-based approach** with controlled AI outputs
- Wizard-of-Oz or pre-programmed responses sufficient
- Web-based platform (simple survey with embedded scenarios) adequate
- Each scenario presents: context → AI output → response options
- This is standard in trust calibration research (Dzindolet et al., 2003; Yin et al., 2019)

### 4.5 Analysis Plan for Study 2b

- Known-groups validity: Compare high vs. low AALS scorers on behavioral measures
- Regression: AALS subscales predicting acceptance rates controlling for demographics
- Interaction effects: AAR × Task type, TTD × AI type on calibration accuracy

---

## 5. AI System Construction: Is It Needed?

### 5.1 For the Main Scale Paper (Study 1 + Study 2a): NO

The core of this paper is a self-report scale validated through survey methodology. No AI system is needed.

### 5.2 For Study 2b (Behavioral Validation): Minimal

A full AI system is **not** required. What's needed is:

1. **Scenario/vignette platform** — A web-based interface presenting pre-designed AI interaction scenarios
2. **Controlled AI outputs** — Pre-written correct and incorrect AI responses (not live AI)
3. **Response measurement** — Accept/reject/verify decisions and confidence ratings

**Implementation options (simplest to most complex):**
- **Option A (Simplest):** Qualtrics survey with embedded scenarios (text + screenshots) — no development needed
- **Option B (Moderate):** Simple web interface simulating AI interaction — basic web development
- **Option C (Most realistic):** Wizard-of-Oz platform with pre-programmed AI responses — moderate development

**Recommendation:** Start with **Option A** for the initial paper. The psychometric contribution (3D framework + validated scale) is the primary value. Behavioral validation with simulated scenarios is well-established and sufficient for a scale development paper.

### 5.3 For Future Empirical Studies: Yes, Eventually

A full experimental study (the Direction A design from previous discussion) would eventually require an actual AI task platform. But that's a separate, future paper.

---

## 6. Critiques and Limitations

### 6.1 Self-Report Limitation
- AALS is self-report; actual calibration behavior may differ
- Study 2b partially addresses this with behavioral validation
- Future work: Behavioral scale or observational protocol

### 6.2 Rapidly Evolving AI Landscape
- Items referencing specific AI behaviors may become outdated
- Mitigation: Frame items at the construct level, not technology-specific
- Plan for periodic re-validation

### 6.3 Cultural and Disciplinary Variation
- Trust calibration norms likely vary across cultures and academic disciplines
- Initial validation with Korean university students; cross-cultural validation needed
- Disciplinary subgroup analysis in Study 2a

### 6.4 Dimensional Independence Assumption
- The three dimensions are theorized as independent but may interact
- CFA and bifactor analysis will empirically test this
- Interaction effects explored in Study 2b

### 6.5 Measurement Feasibility Paradox
- Trust calibration is easiest to measure where verifiability is high (intellective tasks)
- But it matters most where verifiability is low (judgmental tasks)
- The scale attempts to capture awareness and disposition, not just behavior

---

## 7. Publication Strategy

### 7.1 Submission Order
1. **Paper 1 (SLR)** → Computers & Education (in revision)
2. **Paper 2 (AALS)** → Target journals (see below)

### 7.2 Target Journals for Paper 2

| Priority | Journal | Rationale |
|----------|---------|-----------|
| 1st | Computers & Education | Natural follow-up to SLR; strong readership overlap |
| 2nd | Internet and Higher Education | Scale development + higher education focus |
| 3rd | Educational Technology Research & Development | Methodology-focused; welcomes scale development |
| Alt | British Journal of Educational Technology | International audience; AI in education |

### 7.3 Timeline (Estimated)

| Phase | Activity | Duration |
|-------|----------|----------|
| Phase 1 | Literature review + item pool generation | 4–6 weeks |
| Phase 2 | Expert panel review + cognitive interviews | 3–4 weeks |
| Phase 3 | IRB approval | 2–4 weeks |
| Phase 4 | Data collection (Study 1 + 2a simultaneously) | 4–6 weeks |
| Phase 5 | EFA + CFA analysis | 3–4 weeks |
| Phase 6 | Study 2b data collection | 2–3 weeks |
| Phase 7 | Study 2b analysis + manuscript writing | 6–8 weeks |
| **Total** | | **~6–9 months** |

---

## 8. Key Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Research focus | 3D Framework + Scale Development (AALS) | Standalone contribution; builds directly on SLR |
| Data collection method | Online survey | Feasibility, large N, standard for scale development |
| AI system construction | Not required for main paper | Vignette/scenario approach sufficient for Study 2b |
| Submission order | SLR first, then AALS | SLR provides theoretical foundation cited by AALS |
| Scale format | 7-point Likert, self-report | Standard for educational measurement |
| Validation approach | EFA → CFA → Behavioral | Gold standard for scale development |

---

## 9. Open Questions for Next Phase

1. **Item pool development:** What existing AI literacy scales should be reviewed for item adaptation?
2. **Expert panel composition:** Which specific experts to recruit (AI literacy, educational measurement, trust research)?
3. **Sample characteristics:** Which universities/departments to target for recruitment?
4. **Scenario design (Study 2b):** Which specific AI tools/outputs to simulate?
5. **Language:** Korean-language development with English back-translation, or English-first?

---

## 10. References (Key)

- Bandura, A. (2001). Social cognitive theory: An agentic perspective. *Annual Review of Psychology, 52*, 1–26.
- DeVellis, R. F., & Thorpe, C. T. (2021). *Scale development: Theory and applications* (5th ed.). Sage.
- Hammond, K. R. (1987). Toward a unified approach to the study of expert judgment. In J. Mumpower et al. (Eds.), *Expert judgment and expert systems*. Springer.
- Laupichler, M. C., et al. (2023). Development and validation of the Scale for the Assessment of Non-experts' AI Literacy (SNAIL). *Computers in Human Behavior Reports, 12*, 100338.
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80.
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics, 30*(3), 286–297.
- Simon, H. A. (1973). The structure of ill-structured problems. *Artificial Intelligence, 4*, 181–201.
- Winne, P. H., & Hadwin, A. F. (1998). Studying as self-regulated learning. In D. J. Hacker et al. (Eds.), *Metacognition in educational theory and practice*. Erlbaum.
- Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and practice. *Knowledge Engineering Review, 10*(2), 115–152.
