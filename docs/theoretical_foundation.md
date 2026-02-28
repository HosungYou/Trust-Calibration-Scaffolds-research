---
title: "Theoretical Foundation"
date: 2026-02-28
status: revised
revision_notes: "SRL Calibration vs Trust Calibration distinction added; Scaffolding theory section added; All 'checkpoint' terminology replaced with 'scaffold'"
---

# Theoretical Foundation

**Paper:** Trust Calibration as the Missing Link in Educational AI Design: A Critical Review and Conceptual Framework
**Date:** 2026-02-28

---

## 1. Trust in Automation Literature

### 1.1 The Lee & See (2004) Formulation

The foundational theoretical resource for this paper is Lee & See's (2004) landmark review, "Trust in Automation: Designing for Appropriate Reliance," published in *Human Factors*. This paper remains the most cited and most analytically precise treatment of automation trust in the behavioral sciences, and it provides the definitional and structural basis for the trust calibration construct developed here.

Lee & See define trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability." Each term in this definition is theoretically load-bearing:

- **Attitude:** Trust is not a behavior (reliance) but an internal disposition — this distinction is critical for design, because the same trust level can produce different behaviors depending on context, and because trust can be misaligned with reliance in both directions.
- **Agent:** The trust target can be a person, an institution, or a technological system; the framework applies to AI agents in educational contexts.
- **Uncertainty and vulnerability:** Trust is only meaningful in situations where the outcome is not guaranteed and where the trusting party has something at stake. This characterizes most consequential educational contexts: learners are uncertain about AI accuracy and vulnerable to epistemic harm from miscalibrated reliance.

Lee & See identify three dimensions of trustworthiness — the properties of an agent that warrant trust:

1. **Performance:** The agent's ability to achieve the desired outcomes. In educational AI, this corresponds to the AI system's accuracy, reliability, and competence at the designated learning task.
2. **Process:** The understandability and predictability of the agent's methods. In educational AI, this corresponds to the transparency of AI reasoning, the interpretability of AI explanations, and the consistency of AI behavior across similar situations.
3. **Purpose:** The alignment of the agent's goals with the user's goals. In educational AI, this corresponds to whether the AI system is genuinely oriented toward learner development or toward engagement maximization, completion rates, or other metrics that may diverge from deep learning.

These three dimensions provide an analytic grid for evaluating whether trust in a specific AI system is warranted, which is the foundation of calibration: a learner's trust should be proportional to the AI's demonstrable performance, process transparency, and purpose alignment.

### 1.2 Hoff & Bashir (2015): The Three-Layer Model

Hoff & Bashir's (2015) synthesis, "Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust," extends Lee & See by proposing a three-layer model that distinguishes between structurally different types of trust operating at different timescales.

**Layer 1 — Dispositional Trust:**
A stable personal trait reflecting an individual's general tendency to trust automated systems. Dispositional trust is largely independent of specific system characteristics; it reflects prior experiences with technology, cultural background, personality variables (particularly agreeableness and openness), and general epistemic orientation. Dispositional trust shapes the initial calibration baseline: a learner with high dispositional trust will enter an AI-mediated learning environment already inclined toward reliance, creating an overtrust risk; a learner with low dispositional trust may resist reliance even when it is warranted, creating an undertrust risk.

**Layer 2 — Situational Trust:**
Context-sensitive trust adjustments driven by the immediate learning situation — the AI system's interface presentation, task type, perceived stakes, and environmental cues. Situational trust is more malleable than dispositional trust and is therefore the primary target of interface-level design interventions. Trust calibration scaffolds operate primarily at this layer: they create situations that promote accurate trust assessment rather than reliance on dispositional tendencies or superficial interface cues.

**Layer 3 — Learned Trust:**
Experience-based trust updating accumulated through repeated interaction with a specific AI system. Learned trust is the most accurate form of trust because it is grounded in direct evidence about the system's actual performance. However, learned trust is subject to well-documented cognitive biases: negative experiences (AI errors) are weighted more heavily than positive experiences (AI successes) due to negativity bias; early experiences have disproportionate influence due to anchoring; and learners may generalize from specific AI errors to general AI incompetence, producing undertrust that persists even when system accuracy is high.

The three-layer model has direct implications for the Two-Level Framework. The framework's Level 2 design components must address all three layers: modify the dispositional baseline through explicit trust calibration instruction; shape situational trust through scaffold design; and guide learned trust development through structured, interpretable AI interaction sequences.

### 1.3 de Visser et al. (2020): Trust Repair in Human-Agent Teams

de Visser et al.'s (2020) work on trust repair in human-robot and human-agent teams introduces a finding with significant implications for educational AI design: trust, once damaged by AI failure, does not automatically recover. Trust repair requires active, structured intervention.

The trust repair framework identifies three mechanisms:

1. **Acknowledgment:** Explicit recognition of the failure event. In educational AI, this could be implemented as an AI uncertainty display that acknowledges when a previous response was incorrect or uncertain.
2. **Explanation:** A causal account of why the failure occurred. In educational AI, this could be an XAI-generated explanation of the AI's reasoning process that reveals the limitation that produced the error.
3. **Demonstration:** Evidence of improved performance in the domain of the failure. In educational AI, this could be a structured re-engagement sequence that allows learners to test the AI's performance on similar tasks after a failure.

The trust repair framework extends the trust calibration scaffold concept beyond initial calibration to ongoing recalibration: when AI failures produce undertrust, trust repair scaffolds can restore appropriate calibration.

### 1.4 Translation to Educational Contexts

Translating the automation trust literature to educational contexts requires attention to three structural differences:

**Difference 1 — Developmental stakes:** In automation contexts, the primary concern is task performance (aviation safety, medical diagnosis accuracy). In educational contexts, the primary concern is learner development: the goal is not only to achieve correct outcomes but to develop the capacity to achieve correct outcomes independently. This shifts the design target from optimal task performance to optimal learning, which may require deliberately suboptimal AI support in the short term (desirable difficulties).

**Difference 2 — Triadic structure:** Automation trust research models a dyadic relationship between an operator and a system. Educational AI introduces a third party: the teacher or institutional designer who creates the learning environment. Trust calibration in education is a triadic problem — the designer must create conditions under which the learner-AI dyad operates with appropriate calibration. This triadic structure is the basis for the Two-Level Framework's distinction between Level 1 (learner-AI) and Level 2 (system design).

**Difference 3 — Metacognitive dimension:** Automation research treats the operator primarily as a perceiver and responder. Educational research foregrounds the learner as an active metacognitive agent who can monitor, evaluate, and regulate their own cognitive processes — including their trust dispositions. Trust calibration in education is therefore not only a design problem (what system features promote calibration) but a metacognitive learning objective (how learners develop the capacity to self-regulate their trust).

---

## 2. Trust Calibration

### 2.1 Core Definition

Trust calibration refers to the alignment between a learner's perceived assessment of an AI system's capability and the AI system's actual capability in a specific context and task domain. The definition has two essential components:

- **Perceived assessment:** The learner's attitudinal judgment of how capable, accurate, reliable, or appropriate the AI system is for the current task. This assessment is internal, subject to cognitive biases, and influenced by interface presentation, prior experience, and dispositional trust.
- **Actual capability:** The AI system's demonstrable performance on the current task, measured by accuracy, reliability, and fitness for purpose. This is the external reference standard against which perceived assessment is compared.

Calibration is a relational concept: it describes the quality of the relationship between the subjective and the objective, not the level of either in isolation. A high-trust learner may be well-calibrated if the AI system is genuinely highly capable; a low-trust learner may be well-calibrated if the AI system is genuinely limited. The design target is calibration, not trust level per se.

### 2.2 Lee & See (2004) Original Formulation

Lee & See (2004) introduce calibration as the central concept for trust design: the goal of automation design should be to produce calibrated trust — neither overtrust nor undertrust — rather than simply to maximize trust. This formulation represents a significant departure from most technology acceptance research, which treats increased trust as uniformly desirable.

Lee & See's calibration criterion states that trust should be commensurate with the system's actual capabilities and limitations. This implies that:

1. Trust design requires accurate characterization of system capabilities and limitations as a prerequisite.
2. Trust design must create conditions for learners to update their trust assessments based on evidence of actual system performance.
3. Trust design must resist the incentive to maximize trust at the expense of calibration, even when high trust produces better short-term engagement or performance metrics.

### 2.3 Overtrust and Undertrust as Miscalibration

Both overtrust and undertrust are failure modes — departures from calibration in opposite directions — with distinct consequences and distinct design responses.

**Overtrust:**
- Definition: Perceived AI capability substantially exceeds actual capability; the learner defers to AI without appropriate scrutiny.
- Consequences: Uncritical reliance, reduced independent problem-solving, failure to detect AI errors, skill atrophy, epistemic dependence.
- Key evidence: Bastani et al. (2025) — students using AI without oversight showed reduced independent performance; Goddard et al. (2012) — automation bias in medical contexts.
- Design response: Metacognitive prompts requiring independent judgment before AI consultation; verification scaffolds requiring evidence of AI accuracy; productive failure sequences exposing learners to AI errors.

**Undertrust:**
- Definition: Perceived AI capability substantially falls below actual capability; the learner disuses or over-verifies AI output.
- Consequences: Failure to leverage AI's genuine capabilities; redundant cognitive effort; reduced learning efficiency; potential disengagement from AI-integrated learning environments.
- Key evidence: Less studied than overtrust in educational contexts; documented in automation contexts (Lee & See, 2004); relevant in contexts where learners have had negative AI experiences.
- Design response: Gradual trust-building sequences; AI success demonstrations; transparency interventions that reveal AI reasoning quality.

### 2.4 The SRL Calibration vs. Trust Calibration Distinction (CRITICAL)

This distinction is the paper's most significant conceptual contribution to the literature. It must be understood with precision, as the conflation of these two constructs is a source of theoretical confusion in existing research.

**SRL Calibration (Winne & Hadwin, 1998; Zimmerman, 2000):**

Self-regulated learning calibration refers to the accuracy of a learner's judgments about their own capabilities — specifically, the degree of alignment between a learner's confidence in their own task performance and their actual task performance.

Core features of SRL calibration:
- The epistemic target is the SELF: "How capable am I? How well did I perform this task?"
- The reference standard is the learner's own task performance.
- Calibration is measured by comparing confidence ratings to performance scores.
- Theoretical grounding: Winne & Hadwin's (1998) COPES model of self-regulated learning; Zimmerman's (2000) cyclical model; Flavell's (1979) metacognitive monitoring framework.
- Standard measure: Gamma correlation between confidence ratings and performance scores across items; perfectly calibrated learners show gamma = 1.0.
- The locus of uncertainty is internal and self-directed: calibration concerns what the learner knows or can do.

The SRL calibration literature has developed robust measurement methods, design interventions (confidence calibration prompts, prediction-then-verification tasks, judgment-of-learning tasks), and theoretical accounts of calibration development across the lifespan.

**Trust Calibration (Lee & See, 2004, extended to education):**

Trust calibration in the context of educational AI refers to the accuracy of a learner's judgments about an external AI system's capabilities — the degree of alignment between a learner's confidence in an AI response and the AI response's actual accuracy or appropriateness.

Core features of trust calibration:
- The epistemic target is the SYSTEM: "How capable is this AI? How accurate is this AI response?"
- The reference standard is the AI system's actual performance on the task.
- Calibration is measured by comparing trust ratings of AI responses to AI response accuracy scores.
- Theoretical grounding: Lee & See (2004); Hoff & Bashir (2015); de Visser et al. (2020); XAI literature.
- The locus of uncertainty is external and other-directed: calibration concerns what the AI knows or can do.

**Why the distinction is theoretically necessary:**

1. Different epistemic targets require different metacognitive processes. Monitoring one's own performance (SRL calibration) draws on introspective access to one's own cognitive states. Monitoring an AI system's performance (trust calibration) requires assessment of an external system based on observable outputs, explanations, and track records — a fundamentally different epistemic task.

2. Interventions designed for SRL calibration do not automatically transfer to trust calibration. Prediction-then-verification tasks, for example, promote SRL calibration by requiring learners to commit to a judgment before receiving feedback. When adapted for trust calibration (commit to a trust judgment before seeing AI output), the same structural intervention targets a different epistemic object.

3. A learner may be well-calibrated on one dimension and poorly calibrated on the other. High SRL calibration (accurate self-assessment) combined with low trust calibration (inaccurate AI assessment) is a realistic and practically important profile: confident, metacognitively aware learners who nonetheless over- or under-trust AI systems because they lack specific experience or instruction in AI capability assessment.

4. The distinction opens a research space. Once trust calibration is distinguished from SRL calibration, research questions about the relationship between the two constructs become tractable: Does high SRL calibration predict high trust calibration? Does trust calibration training improve SRL calibration as a byproduct? Are there developmental sequences in which one precedes the other?

The failure to draw this distinction clearly is a significant source of conceptual confusion in the existing educational AI literature, where "calibration" is sometimes used to refer to SRL processes, sometimes to AI-trust processes, and sometimes to a vague combination of both. The present paper establishes the distinction as a terminological and theoretical standard for the field.

---

## 3. Wang et al. (2025) S-O-R Model

### 3.1 Model Structure

Wang et al. (2025) propose an S-O-R (Stimulus-Organism-Response) framework for understanding trust in AI-assisted learning. The model applies a classic behavioral framework from consumer psychology to the novel domain of educational AI, with modifications intended to capture the cognitive and motivational complexity of learning contexts.

**S — Stimulus: AI Agent Characteristics**
The stimulus layer encompasses the design features of the AI system that a learner encounters in the learning environment:
- Accuracy and reliability of AI outputs.
- Quality and clarity of AI explanations.
- Interface design and usability.
- AI personalization features and responsiveness.
- Transparency features (uncertainty displays, source attribution).

**O — Organism: Internal States**
The organism layer encompasses the learner's internal psychological states that mediate between AI characteristics and behavioral responses:
- Trust formation: the learner's developing attitudinal assessment of the AI system.
- Self-efficacy: confidence in one's own ability to use and evaluate AI effectively.
- Cognitive load: the mental effort required to process and evaluate AI outputs.
- Perceived usefulness: the learner's assessment of whether the AI is genuinely helpful.

Wang et al. importantly distinguish trust (an attitude toward the AI) from reliance (a behavioral response) — a distinction that is theoretically significant because it allows overtrust to be defined as a discrepancy between attitude and behavior where attitude (high trust) drives behavior (reliance) in ways that exceed the AI's actual capability.

**R — Response: Behavioral and Learning Outcomes**
The response layer encompasses observable behaviors and learning outcomes:
- AI reliance behavior: frequency and depth of AI consultation.
- Verification behavior: frequency of checking AI outputs against other sources.
- Learning outcomes: performance on tasks assessed independently of AI.
- Engagement: persistence and elaboration in AI-mediated learning activities.

### 3.2 Strengths

**Strength 1 — Trust-Reliance Distinction:** Wang et al.'s clearest theoretical contribution is the explicit distinction between trust (attitude) and reliance (behavior). This distinction creates theoretical space for the study of miscalibration: overtrust is precisely the condition in which trust (attitude) drives reliance (behavior) without appropriate calibration. Most prior educational technology research collapses this distinction, treating trust and use as nearly synonymous.

**Strength 2 — Systematic Causal Account:** The S-O-R framework provides a testable causal structure: AI characteristics (S) influence internal states (O), which drive behavioral responses (R). This structure enables hypothesis generation and experimental design.

**Strength 3 — Individual Difference Integration:** The model integrates individual difference variables (prior AI experience, dispositional trust, domain expertise) as moderators of the S-O pathway, acknowledging that the same AI design features will produce different trust responses in different learners.

### 3.3 Limitations

**Limitation 1 — Behaviorist Lineage:** The S-O-R framework inherits a stimulus-response logic from behaviorist psychology. This framing treats the organism primarily as a processor of environmental stimuli and a generator of behavioral outputs, underweighting the learner's active, metacognitive role in monitoring, evaluating, and regulating trust. A learner who deliberately reflects on their trust dispositions, seeks out evidence of AI accuracy, and strategically adjusts their reliance behavior is not well captured by the S-O-R structure, which has no mechanism for self-directed, goal-driven trust regulation.

**Limitation 2 — Individual-Level Ceiling:** The model stops at the individual level of analysis. It characterizes how individual learners form and act on trust but does not address the role of the educational system — curriculum design, teacher oversight, institutional policy — in shaping the conditions under which trust calibration occurs. This leaves the design implications of the model at the level of AI interface features, without reaching the system-level design questions that are central to the Two-Level Framework.

**Limitation 3 — Single Dependency Risk:** Building a theoretical framework primarily around a single recently published model creates intellectual dependency. If Wang et al.'s framework is revised, contested, or superseded, a framework built on it as a foundation becomes vulnerable. The Two-Level Framework diversifies this dependency by integrating multiple theoretical traditions (automation trust, scaffolding theory, SRL, XAI) into a structure that does not depend on the validity of any single source.

**Limitation 4 — Static Organism Layer:** The organism layer in Wang et al.'s model represents internal states at a point in time, without a mechanism for ongoing self-regulation or calibration updating. Trust is formed and then drives behavior; there is no looping structure in which behavior feeds back to inform trust updating. This is a significant limitation for educational contexts, where the goal is precisely to develop learners who can continuously update their trust assessments based on evidence.

### 3.4 Extension: Adding Metacognitive Self-Regulation

The Two-Level Framework extends Wang et al.'s model in two ways:

1. **Within the Organism layer:** Add metacognitive self-regulation as a second-order process that monitors and regulates trust formation and trust updating. The extended Organism layer includes not only trust formation and self-efficacy but also calibration monitoring (metacognitive assessment of trust accuracy) and trust regulation (strategic adjustment of trust and reliance).

2. **Above the S-O-R structure:** Add a system-level layer (Level 2 of the Two-Level Framework) that accounts for educational environment design. The system-level layer shapes the conditions under which Stimulus-Organism-Response processes operate: trust calibration scaffolds in the environment provide additional stimuli specifically designed to promote calibration monitoring and trust regulation in the Organism layer.

---

## 4. Scaffolding Theory

### 4.1 Wood, Bruner & Ross (1976): Original Scaffolding Concept

The term "scaffolding" was introduced by Wood, Bruner, & Ross (1976) in their foundational study of tutoring interactions between an expert adult and novice children in a block-stacking task. Scaffolding refers to the support provided by a more knowledgeable other that enables a learner to accomplish a task they could not accomplish independently, with the defining property that the support is contingent and temporary — designed to be withdrawn as learner competence develops.

Wood, Bruner, & Ross identify six tutoring functions that constitute scaffolding:
1. Recruiting the learner's interest in the task.
2. Reducing the degrees of freedom in the task by simplifying it.
3. Maintaining goal direction when the learner is distracted.
4. Marking critical features of the task.
5. Controlling frustration and risk.
6. Demonstrating an idealized version of the act to be performed.

The critical properties for trust calibration scaffold design are:
- **Contingency:** Scaffolding responds to the learner's current level of competence; the type and intensity of support adapts to what the learner can and cannot yet do. Applied to trust calibration: scaffold intensity should be calibrated to the learner's current calibration accuracy.
- **Fading:** Support is gradually withdrawn as competence develops; the goal is not permanent support but transfer of the supported competence to independent performance. Applied to trust calibration: as a learner's calibration accuracy improves, the intensity of trust calibration scaffolds decreases.
- **Transfer of responsibility:** The progression is from expert-regulated to learner-regulated performance. Applied to trust calibration: the progression is from system-regulated calibration (designed scaffolds enforce calibration monitoring) to learner-regulated calibration (the learner self-initiates calibration monitoring without prompt).

### 4.2 Core Properties and Their Application to Trust Calibration

**Contingency applied:**
Trust calibration scaffolds should be contingent on individual learner calibration profiles. A learner showing overtrust patterns (high trust ratings combined with failure to detect AI errors) should receive verification scaffolds. A learner showing undertrust patterns (low trust ratings combined with non-use of accurate AI) should receive trust-building scaffolds. A learner showing calibrated trust should receive minimal scaffolding to avoid unnecessary friction.

**Fading applied:**
Scaffold intensity should decrease as calibration accuracy improves. A formal fading protocol might define calibration accuracy thresholds (e.g., gamma correlation between trust ratings and AI accuracy) that trigger reductions in scaffold intensity. The end state is a learner who self-initiates calibration monitoring without scaffold prompting.

**Transfer of responsibility applied:**
The goal of trust calibration scaffolding is not to create permanent reliance on scaffolds but to develop the metacognitive capacity for autonomous trust regulation. Scaffolds that produce calibrated trust through external constraint without developing internal capacity have failed in their educational purpose.

### 4.3 Hattie (2009): Scaffolding Effect Size

Hattie's (2009) synthesis of meta-analyses in educational research, *Visible Learning*, reports an average effect size of d = 0.82 for scaffolding interventions across a large corpus of studies. This places scaffolding among the most effective educational interventions documented in the literature, substantially above the average effect size of approximately d = 0.40.

This evidence base provides strong empirical support for the use of scaffolding as the foundational design strategy in the Two-Level Framework. The trust calibration scaffold concept inherits the evidential warrant of the broader scaffolding literature, while extending it to the novel domain of AI trust calibration.

### 4.4 Hannafin et al. (1999): Scaffolding Taxonomy

Hannafin, Land, & Oliver (1999) provide a comprehensive taxonomy of scaffolding types in online learning environments:

- **Cognitive scaffolding:** Supports the processes of comprehension, analysis, and problem-solving.
- **Metacognitive scaffolding:** Supports learners' monitoring and regulation of their own thinking.
- **Motivational scaffolding:** Supports learners' engagement, persistence, and self-efficacy.
- **Strategic scaffolding:** Supports the selection and application of task-specific strategies.
- **Procedural scaffolding:** Supports the navigation of tools and processes.

This taxonomy provides the organizational structure for the trust calibration scaffold mechanisms described in Section 5 of the paper. Each mechanism maps onto one or more scaffold types, allowing the trust calibration scaffold concept to be grounded in established educational technology vocabulary.

### 4.5 Vygotsky's Zone of Proximal Development Connection

Scaffolding theory is grounded in Vygotsky's (1978) concept of the Zone of Proximal Development (ZPD): the distance between what a learner can accomplish independently and what they can accomplish with expert support. Scaffolding operates within the ZPD — it is calibrated to the learner's current independent capability and designed to expand that capability toward the upper limit of supported capability.

Applied to trust calibration: the ZPD for trust calibration is the distance between a learner's current calibration accuracy (independent performance) and the calibration accuracy achievable with trust calibration scaffolds (supported performance). As calibration accuracy increases under scaffold support, the scaffold is faded and a new ZPD is established at a higher level of calibration competence.

---

## 5. Adjacent Field Evidence

### 5.1 Bjork & Bjork (1994, 2011): Desirable Difficulties

Bjork & Bjork's research program on desirable difficulties demonstrates that learning conditions that slow or disrupt the acquisition process in the short term can enhance long-term retention and transfer. Specific desirable difficulties include: spacing (distributing practice over time rather than massing it); interleaving (mixing rather than blocking practice on different types of problems); testing (using retrieval practice rather than re-study); and reducing feedback frequency or immediacy.

Applied to trust calibration: providing learners with immediate, complete AI assistance is analogous to massed practice with abundant feedback — it produces short-term performance gains but limits the development of independent capacity. Trust calibration scaffolds that introduce delays (requiring learners to formulate their own answer before seeing the AI's response) or require evidence-seeking (requiring learners to find supporting sources before accepting AI claims) are educational analogs of desirable difficulties. They create productive friction that slows the immediate task but deepens the development of calibrated trust.

Operational applications in trust calibration scaffold design:
- **Response delay:** Require learners to articulate their own answer or hypothesis before the AI response is displayed.
- **Evidence requirement:** Require learners to identify one or two corroborating sources before accepting AI claims on high-stakes questions.
- **Spacing of AI access:** In some task sequences, withhold AI access during initial problem-solving to build independent engagement before AI consultation.

### 5.2 Kapur (2008): Productive Failure

Kapur's (2008) productive failure research demonstrates that allowing students to struggle with problems before instruction produces better conceptual understanding than direct instruction followed by practice, even though students in the struggle-first condition perform worse on immediate measures. The failure experience activates prior knowledge, increases engagement with subsequent instruction, and deepens understanding of why the instructed method works.

Applied to trust calibration: exposing learners to AI errors before instruction in AI verification is a productive failure sequence for trust calibration. Learners who encounter AI mistakes without a framework for understanding them are in a productive failure state: their experience of the mismatch between their trust and the AI's actual performance creates a readiness for the verification framework that trust calibration scaffolds subsequently provide.

Practical sequence:
1. Expose learners to a task where AI makes a specific type of error.
2. Allow learners to discover the error (or near-discover it) with minimal guidance.
3. Provide direct instruction in verification techniques targeted at that error type.
4. Return to AI-assisted tasks with the verification scaffold in place.

### 5.3 Guo et al. (2022): Metacognitive Prompts Meta-Analysis

Guo et al.'s (2022) meta-analysis of metacognitive prompt interventions in technology-enhanced learning environments provides quantitative evidence for the effectiveness of prompts that require learners to engage in explicit metacognitive monitoring. Key findings:

- Effect size g = 0.50 for SRL outcomes (metacognitive monitoring, strategic self-regulation).
- Effect size g = 0.40 for learning outcomes (performance on assessments).
- Effects were larger for higher-order thinking tasks than for factual recall tasks.
- Effects were moderated by prompt specificity: more specific prompts (e.g., "Write your prediction for this problem before seeing the AI's solution") were more effective than general reflection prompts.

These findings provide direct evidential support for the metacognitive prompt mechanism in trust calibration scaffold design. Prompts that require learners to articulate their trust assessment before consulting AI output are structurally analogous to the metacognitive prompts studied by Guo et al., and the effect sizes suggest they are likely to produce meaningful improvements in calibration-relevant outcomes.

### 5.4 de Visser et al. (2020): Trust Repair Through Calibration Cues

de Visser et al.'s (2020) experimental work on trust repair in human-robot teams demonstrates that structured interventions can restore appropriate calibration after trust damage. The study found that calibration cues — explicit demonstrations of system capability in the domain of prior failure — were more effective at restoring calibrated trust than general assurances or apologies.

The calibration cue mechanism has direct applications in educational AI contexts. When an AI system produces an error that damages learner trust, a trust repair sequence using calibration cues would:
1. Acknowledge the error explicitly (AI uncertainty display or teacher acknowledgment).
2. Explain the type of task or context in which the error occurred.
3. Demonstrate AI capability on related tasks where the system performs reliably.
4. Return to a scaffolded interaction sequence that allows the learner to re-establish calibrated trust through evidence.

This framework supports the recalibration function of trust calibration scaffolds: they are not only initial calibration tools but ongoing recalibration mechanisms that can restore appropriate trust following AI failure events.

---

## Terminology Note

Throughout this document and all associated manuscript materials, the term "trust calibration scaffold" is used in preference to "checkpoint." The term "scaffold" is grounded in the established educational research tradition (Wood et al., 1976; Hannafin et al., 1999; Hattie, 2009) and accurately captures the contingent, fading, responsibility-transferring character of the designed interventions. "Checkpoint" is not a standard educational research term and does not capture these theoretical properties. Where prior versions of project materials used "checkpoint," the term is updated to "trust calibration scaffold" throughout.
