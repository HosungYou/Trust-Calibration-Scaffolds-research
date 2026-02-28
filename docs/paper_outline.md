---
title: "Paper Outline — Path C: Rapid Critical Review + Conceptual Framework"
paper_title: "Trust Calibration as the Missing Link in Educational AI Design: A Critical Review and Conceptual Framework"
target_journal: IJETHE
target_words: ~8,000
date: 2026-02-28
---

# Paper Outline — Path C: Rapid Critical Review + Conceptual Framework

**Paper Title:** Trust Calibration as the Missing Link in Educational AI Design: A Critical Review and Conceptual Framework
**Target Journal:** IJETHE
**Target Word Count:** ~8,000
**Date:** 2026-02-28

---

## Overview

This paper argues that trust calibration — the alignment between a learner's perceived and actual assessment of an AI system's capability — is the theoretical concept most urgently missing from the educational AI design literature. Drawing on a critical review of existing empirical and conceptual work, the paper maps the current landscape of trust research in educational AI, diagnoses a structural gap in calibration-focused design, and proposes a Two-Level Framework integrating learner-level trust dynamics with system-level oversight architecture.

---

## Section 1: Introduction (~800 words)

### 1.1 Hook

Open with the Bastani et al. (2025) PNAS finding: students who used AI assistance without structured oversight showed significant overtrust and reduced independent problem-solving ability compared to control groups. This finding is not an anomaly — it is a predictable consequence of deploying AI systems without attending to the mechanisms of trust calibration. The Bastani et al. result crystallizes a problem that has been latent in educational AI research since the first deployment of intelligent tutoring systems: learners do not automatically develop appropriate epistemic relationships with AI tools.

- Anchor the paper's urgency in an empirically documented, high-profile finding.
- Note that PNAS publication elevates the finding beyond education circles into broader scientific discourse.
- Avoid framing this as a cautionary tale against AI; frame it as diagnostic evidence that trust calibration is under-theorized and under-designed.

### 1.2 Problem Statement

AI systems in education occupy an increasingly autonomous role: they provide explanations, generate feedback, evaluate work, and recommend learning pathways. This expanded autonomy raises a fundamental design tension: How much should learners defer to AI judgment, and how should educational systems be designed to support appropriate deference?

- The automation literature (Lee & See, 2004) identifies this tension as a calibration problem: overtrust leads to uncritical reliance, undertrust leads to disuse or productive disengagement.
- In education, this tension has a unique character: the goal is not merely task efficiency but the development of learner agency and metacognitive competence.
- Current educational AI design largely optimizes for engagement, accuracy, and learning outcomes, while treating trust as a byproduct rather than a design target.

### 1.3 Trust as the Missing Variable

Introduce the core claim: trust calibration is the missing theoretical and design variable in educational AI research.

- Existing reviews (e.g., Wang et al., 2025) identify trust as an important mediating variable in AI-assisted learning but do not distinguish between trust formation, trust calibration, and trust repair.
- The SRL literature has a robust calibration concept (Winne & Hadwin, 1998; Zimmerman, 2000), but this concept refers to learners' accuracy about their own capabilities, not about an external AI system's capabilities.
- A conceptual gap exists at the intersection: calibration of trust in AI systems in educational contexts has neither a settled theoretical framework nor an established design methodology.

### 1.4 Purpose of the Paper

State four purposes explicitly:

(a) Map the current landscape of trust research in educational AI, identifying how trust is conceptualized, theorized, and measured.
(b) Identify the calibration gap: the absence of trust calibration as a first-class design target.
(c) Propose a Two-Level Framework connecting learner-level trust dynamics (Level 1: Micro) to system-level oversight design (Level 2: Macro).
(d) Derive design implications and a research agenda from the framework.

### 1.5 Research Questions

- **RQ1:** How is trust in AI conceptualized and measured in educational AI research?
- **RQ2:** What theoretical frameworks guide trust research in educational AI, and what are their explanatory strengths and limitations?
- **RQ3:** To what extent does existing research address trust calibration and the design of human oversight mechanisms?
- **RQ4:** What does a two-level framework connecting learner trust dynamics to oversight design look like, and what are its theoretical foundations?

### 1.6 Scope and Contribution

- Scope: K-12 and higher education contexts; AI systems including intelligent tutoring systems, generative AI tools, AI-assisted feedback systems; 2015–2026.
- Contribution: (1) first systematic identification of trust calibration as a gap in educational AI design literature; (2) Two-Level Framework as a theoretically grounded design resource; (3) research agenda with concrete, testable propositions.

---

## Section 2: Conceptual Foundation (~1,800 words)

### 2.1 Trust in Automation: Origins and Educational Translation

Ground the paper's use of "trust" in the automation literature before translating it to education.

**Core references:**
- Lee & See (2004): Definitive formulation — trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability." Three dimensions: performance (ability to do the task), process (understandable and predictable methods), purpose (alignment of agent goals with user goals).
- Hoff & Bashir (2015): Three-layer model — dispositional trust (stable personal trait), situational trust (context-sensitive adjustment), learned trust (experience-based updating). This layering has direct implications for educational design: dispositional trust varies across learners; situational trust is sensitive to AI presentation; learned trust is the target of calibration interventions.
- de Visser et al. (2020): Trust repair in human-agent teams — trust can be degraded and rebuilt; the mechanisms of repair are systematic and teachable.

**Translation notes:**
- In automation research, trust is studied primarily in high-stakes task contexts (aviation, military, medical). Educational contexts differ: the cost of overtrust is epistemic (reduced independent thinking) rather than physical; the time horizon is developmental rather than task-specific.
- Educational AI introduces a third party: the teacher or institution that designs the learning environment. Trust calibration in education is therefore not a dyadic (learner-AI) but a triadic (learner-AI-designer) problem.
- This triadic structure motivates the Two-Level Framework.

### 2.2 Trust Calibration: Core Concept and the SRL Distinction (KEY)

Define trust calibration with precision and draw the SRL distinction that is the paper's unique conceptual contribution.

**Trust calibration defined:**
- Calibration refers to the alignment between a learner's perceived assessment of an AI system's capability and the AI system's actual capability in a given context.
- Overtrust: perceived capability exceeds actual capability; results in uncritical reliance, reduced verification behavior, and skill atrophy.
- Undertrust: perceived capability falls below actual capability; results in disuse, redundant verification effort, and failure to leverage AI's genuine strengths.
- Calibrated trust: perceived and actual capability are aligned; learner defers to AI appropriately and applies critical scrutiny when warranted.

**The SRL Calibration vs. Trust Calibration Distinction (CRITICAL):**

This distinction is the paper's most important conceptual contribution. It must be stated with clarity and defended against potential conflation.

*SRL Calibration (Winne & Hadwin, 1998; Zimmerman, 2000):*
- Refers to the accuracy of learners' judgments about their own capabilities.
- The classic measure: comparing a learner's confidence in a task performance with their actual performance on that task.
- The locus of uncertainty is the SELF: "How well can I do this?"
- Theoretical home: self-regulated learning, metacognition, Flavell's (1979) metacognitive monitoring.
- Design interventions: confidence calibration prompts, prediction-then-verification tasks, portfolios.

*Trust Calibration (Lee & See, 2004, extended to education):*
- Refers to the accuracy of learners' judgments about an external AI system's capabilities.
- The relevant measure: comparing a learner's confidence in an AI response with the AI response's actual accuracy or appropriateness.
- The locus of uncertainty shifts from SELF to SYSTEM: "How well can this AI do this?"
- Theoretical home: automation trust, human-computer interaction, XAI.
- Design interventions: uncertainty transparency displays, verification scaffolds, trust calibration scaffolds.

*Why the distinction matters:*
- Conflating SRL calibration with trust calibration obscures a fundamental difference in epistemic target.
- A learner may be well-calibrated about their own abilities (high SRL calibration) while being poorly calibrated about an AI system's abilities (low trust calibration), or vice versa.
- Designing for SRL calibration does not automatically produce trust calibration; separate, targeted design interventions are required.
- This distinction creates a clear theoretical space for the present paper's contribution.

### 2.3 Wang et al. (2025) S-O-R Model: Strengths, Limitations, and Extension

Engage seriously with the most influential recent theoretical framework in AI trust in education.

**Model structure:**
- S (Stimulus): AI agent characteristics — accuracy, transparency, explanation quality, interface design.
- O (Organism): Internal states — trust formation, self-efficacy, cognitive load.
- R (Response): Behavioral and learning outcomes — AI reliance, task performance, engagement.

**Strengths:**
- Distinguishes trust from reliance: trust is an attitudinal state; reliance is a behavioral response. This distinction is theoretically important and empirically testable.
- Provides a systematic causal account connecting AI design features to learning outcomes via trust.
- Integrates individual difference variables (dispositional trust, prior AI experience) as moderators.

**Limitations:**
- Behaviorist lineage: the S-O-R framework inherits a behaviorist logic that treats the organism primarily as a responder to stimuli. This underweights the learner's active, metacognitive role in regulating trust.
- Stops at the individual level: the model does not address the role of educational system design (curriculum, teacher oversight, institutional policy) in shaping trust calibration.
- Single dependency risk: building an educational AI trust framework on a single recently published model creates intellectual dependency; the Two-Level Framework diversifies this by integrating multiple theoretical traditions.

**Extension:**
- Add metacognitive self-regulation to the Organism layer: the learner is not only a trust-former but a trust-regulator who can monitor, evaluate, and adjust their trust dispositions.
- Add a system-level layer above the S-O-R structure to account for institutional and pedagogical scaffolding.

### 2.4 Toward the Two-Level Framework: Preview and Scaffolding Theory Connection

Preview the Two-Level Framework introduced in Section 5 by connecting it to scaffolding theory.

- Wood, Bruner, & Ross (1976): scaffolding as contingent, fading support that transfers responsibility to the learner as competence develops.
- Scaffolding theory provides the mechanism for moving from miscalibration (the problem diagnosed in Sections 3–4) to calibration (the design target of the Two-Level Framework).
- Trust calibration scaffolds are defined as structured, contingent, fading support mechanisms designed to align learner trust with AI system capability.
- The Two-Level Framework integrates scaffolding theory at Level 1 (learner-facing calibration interventions) and Level 2 (system-level oversight architecture).

---

## Section 3: Review Approach (~500 words)

### 3.1 Search Strategy

- Databases: Web of Science and Scopus.
- Date range: 2015–2026 (covering the period from early intelligent tutoring system proliferation through generative AI adoption).
- Search terms: ("trust" OR "trust calibration") AND ("artificial intelligence" OR "AI" OR "machine learning") AND ("education" OR "learning" OR "higher education" OR "K-12").
- Initial yield: approximately 400–600 records after deduplication.

### 3.2 Literature Selection Criteria

- Inclusion: empirical studies or theoretical papers examining trust in AI in educational contexts; papers addressing trust formation, trust calibration, or human oversight in AI-assisted learning; English-language publications in peer-reviewed journals or conference proceedings.
- Exclusion: papers using "trust" in a purely social or interpersonal sense without reference to AI systems; papers outside educational contexts without clear transferability; opinion pieces without theoretical grounding.
- Final corpus: approximately 60–80 papers selected for detailed analysis.

### 3.3 Analysis Approach

- Thematic analysis: identify dominant conceptualizations of trust, theoretical frameworks cited, measurement instruments used.
- Gap analysis: identify what is absent — specifically, trust calibration as an explicit design target and human oversight design as a system-level concern.
- Limitations acknowledgment: the review is critical and selective rather than exhaustive; the goal is theoretical contribution, not comprehensive coverage. Publication bias toward positive findings may underrepresent null or negative results on AI trust interventions.

---

## Section 4: Literature Landscape (~1,500 words)

### 4.1 Trust Conceptualizations in Educational AI Research

Survey how trust is conceptualized across the reviewed literature.

- Dominant conceptualization: trust as a mediating attitudinal variable between AI design features and learning/engagement outcomes. Trust is treated as something learners have or do not have, and more trust is generally treated as better.
- Secondary conceptualization: trust as a function of perceived accuracy and reliability. Studies in this cluster measure trust via self-report scales and correlate with AI error rates or explanation quality.
- Emergent conceptualization: trust as a dynamic, contextually variable state that can be appropriate or inappropriate depending on AI system capability. This is the conceptualization most aligned with trust calibration but remains undertheorized in the literature.

**Key finding:** The vast majority of studies treat trust as a unidimensional positive variable — something to be increased — rather than as a calibration target to be aligned with actual system capability.

### 4.2 Theoretical Frameworks in Educational AI Trust Research

Map the theoretical frameworks used across the reviewed literature.

- **Mayer et al. (1995)** trustworthiness model (ability, benevolence, integrity): widely cited, provides a stable three-factor structure for trustworthiness perceptions.
- **Lee & See (2004)** automation trust model: cited frequently but rarely used to distinguish trust from calibration.
- **Technology Acceptance Model (TAM)**: Davis (1989); used in many quantitative studies; conflates trust with perceived usefulness and ease of use.
- **Wang et al. (2025) S-O-R Model**: emerging as a new reference framework; strengths and limitations addressed in Section 2.3.

**Key finding:** Theoretical frameworks in this literature are largely borrowed from technology acceptance and organizational trust contexts. Frameworks specifically designed for calibration-focused analysis are absent.

### 4.3 Trust Measurement in Educational AI Research

Summarize measurement approaches.

- Dominant method: self-report Likert-scale trust surveys adapted from automation or technology acceptance contexts.
- Common instruments: adapted versions of Jian et al. (2000) Checklist for Trust between People and Automation; custom scales with limited validation.
- Behavioral measures: rare; include verification behavior frequency, AI override rates, time spent checking AI responses.
- Calibration-specific measures: nearly absent; no study in the corpus uses a formal trust calibration score (comparing trust ratings to AI accuracy in a systematic framework).

**Key finding:** The measurement infrastructure for trust calibration in educational AI research does not yet exist. Studies measure trust level but not calibration quality.

### 4.4 The Calibration Gap (KEY Finding)

Synthesize the three preceding subsections into the paper's diagnostic core.

- The literature conceptualizes trust incompletely (as a positive unidimensional variable rather than a calibration target).
- The literature uses theoretical frameworks not designed for calibration analysis.
- The literature measures trust level but not calibration quality.
- Together, these three gaps constitute the calibration gap: the absence of trust calibration as a first-class theoretical construct and design target in educational AI research.
- This gap is consequential: without calibration-focused design, educational AI systems will produce the overtrust effects documented by Bastani et al. (2025) at scale.

---

## Section 5: Two-Level Framework (~1,800 words) — Core Contribution

### 5.1 From Fragmented Trust to Integrated Framework

Motivate the framework by characterizing what it integrates.

- Current research addresses trust at the individual level (how learners form and update trust) without connecting to system-level design (how educational environments can scaffold calibration).
- The Two-Level Framework bridges this gap by connecting learner-level trust dynamics (Level 1: Micro) to system-level oversight architecture (Level 2: Macro).
- The framework is integrative rather than additive: it does not simply combine existing theories but proposes a new causal structure in which Level 2 system design shapes the conditions under which Level 1 calibration processes operate.

### 5.2 Level 1 (Micro): Learner Trust Dynamics

Describe the learner-level layer of the framework in detail.

**Core processes:**
- Trust formation: initial trust dispositions shaped by dispositional trust (Hoff & Bashir, 2015), prior AI experience, and first-encounter AI presentation.
- Trust updating: experience-based revision of trust assessments; governed by confirmation bias, error salience, and explanation quality.
- Calibration monitoring: metacognitive process through which learners assess the alignment between their trust dispositions and AI performance; the target of trust calibration scaffolds.
- Trust regulation: strategic adjustment of trust and reliance behavior based on calibration monitoring results.

**Learner variables:**
- Prior AI experience: shapes initial calibration baseline.
- Epistemic curiosity: moderates verification behavior.
- Metacognitive awareness: determines the depth of calibration monitoring.
- Domain knowledge: enables more accurate assessment of AI response quality.

**Calibration failure modes:**
- Overtrust: insufficient calibration monitoring; excessive reliance on AI.
- Undertrust: overcorrection from negative experience or dispositional skepticism.
- Pseudo-calibration: superficial calibration behavior without genuine epistemic adjustment.

### 5.3 Level 2 (Macro): System-Mediated Trust Calibration

Describe the system-level layer of the framework in detail.

**Core components:**
- Trust calibration scaffolds: structured, contingent, fading support mechanisms embedded in the learning environment to promote calibration monitoring and trust regulation.
- AI uncertainty transparency: system-level display of AI confidence and capability boundaries; enables learners to calibrate based on system-provided information rather than inference alone.
- Teacher-mediated verification: human oversight mechanisms through which teachers monitor learner trust states and intervene when miscalibration is detected.
- Institutional oversight architecture: curriculum-level and policy-level structures that define when and how learners interact with AI, creating the conditions for calibration.

**Design principles for Level 2:**
1. Calibration before engagement: require learners to articulate their trust expectations before AI interaction.
2. Uncertainty display as default: make AI confidence scores and capability boundaries visible.
3. Verification scaffolding: require evidence-seeking behavior before high-stakes AI reliance.
4. Teacher oversight integration: provide teachers with trust calibration dashboards.
5. Progressive fading: reduce scaffolding intensity as calibration accuracy improves.

### 5.4 Adaptive Calibration Cycle

Describe the dynamic interaction between Level 1 and Level 2 as a cycle.

**Cycle phases:**
1. Encounter: learner encounters AI output in a designed learning context.
2. Trust Activation: learner activates trust disposition (Level 1).
3. Scaffold Engagement: system presents trust calibration scaffold (Level 2) — prompt, verification task, or uncertainty display.
4. Calibration Monitoring: learner engages in metacognitive assessment of trust alignment (Level 1).
5. Trust Regulation: learner adjusts trust and reliance behavior (Level 1).
6. System Feedback: system provides feedback on verification quality or calibration accuracy (Level 2).
7. Scaffold Fading: as calibration accuracy improves, scaffold intensity reduces (Level 2).
8. Transfer: learner applies calibrated trust in new AI interaction contexts.

**Adaptive mechanism:**
- The cycle is adaptive because scaffold intensity (Level 2) is continuously adjusted based on calibration accuracy signals (Level 1).
- This creates a feedback loop that drives the system toward calibrated trust over time.

### 5.5 Evidence Mapping

Connect the framework's components to existing empirical evidence.

- Metacognitive prompts → Guo et al. (2022): g = 0.50 for SRL outcomes; g = 0.40 for learning outcomes.
- Desirable difficulties → Bjork & Bjork (1994, 2011): slowing AI response to require active engagement.
- Productive failure → Kapur (2008): allowing learners to encounter AI errors before direct instruction on verification.
- Uncertainty transparency → XAI literature: confidence displays reduce overtrust in high-accuracy contexts.
- Progressive fading → Wood, Bruner, & Ross (1976); Hattie (2009) effect size 0.82 for scaffolding.
- Trust repair → de Visser et al. (2020): structured repair protocols can restore calibrated trust after AI failure.

---

## Section 6: Implications (~800 words)

### 6.1 For AI Designers: Five Design Principles

Translate the Two-Level Framework into actionable design guidance.

1. **Calibration-First Design:** Trust calibration should be a design requirement, not a byproduct. Design specifications for educational AI should include explicit calibration targets and metrics.
2. **Uncertainty as Curriculum:** AI uncertainty displays should be treated as pedagogical content — they teach learners about the nature of AI capability and the appropriate scope of reliance.
3. **Verification as Workflow:** Build verification tasks into AI interaction workflows; do not treat verification as optional or supplementary.
4. **Adaptive Scaffolding Architecture:** Design scaffolding systems that reduce intensity as learner calibration accuracy improves; avoid one-size-fits-all scaffolding.
5. **Teacher Integration:** Design teacher-facing dashboards that make learner trust states visible and provide intervention protocols for miscalibration.

### 6.2 For Educators: Trust Calibration as Learning Objective

Reframe trust calibration as a curricular and pedagogical target.

- Trust calibration in AI contexts is a new form of epistemic competence: it requires learners to maintain accurate models of external AI system capabilities, not just their own abilities.
- This competence should be explicitly taught, practiced, and assessed alongside domain content.
- Trust calibration scaffolds (metacognitive prompts, verification tasks, productive failure sequences) are pedagogical tools that educators can deploy in any AI-integrated classroom.
- Professional development for educators should include trust calibration literacy: understanding overtrust and undertrust, recognizing calibration failure, and designing calibration interventions.

### 6.3 For Researchers: Research Agenda

Identify the most critical research priorities generated by the Two-Level Framework.

- **Measurement:** develop and validate a trust calibration score for educational contexts that formally compares learner trust ratings with AI performance.
- **Experimental studies:** test the effect of specific trust calibration scaffolds on calibration accuracy and learning outcomes.
- **Longitudinal studies:** track trust calibration development across extended AI interaction; test the fading hypothesis.
- **Teacher mediation:** examine how teacher oversight and intervention affect learner trust calibration.
- **Cross-context studies:** test whether trust calibration generalizes across different AI systems, subjects, and educational levels.

---

## Section 7: Conclusion (~600 words)

### 7.1 Limitations

Acknowledge limitations with specificity.

- The review is critical and selective, not exhaustive; comprehensiveness was sacrificed for theoretical depth.
- The Two-Level Framework is conceptual; it requires empirical validation in designed experimental studies.
- The framework was developed primarily with reference to higher education and secondary school contexts; applicability to early childhood or vocational education contexts requires further examination.
- The paper does not address the ethical dimensions of trust calibration design (e.g., the risk that calibration interventions could be used to increase AI reliance rather than calibrate it).

### 7.2 Core Argument Restatement

Return to the paper's central claim with full theoretical grounding.

- Trust calibration — the alignment between learners' perceived and actual assessments of AI system capability — is the missing theoretical and design variable in educational AI research.
- The calibration gap identified in this review is not a peripheral oversight; it is a structural absence that will produce predictable overtrust effects at scale as AI adoption in education accelerates.
- The Two-Level Framework provides a theoretically grounded, empirically anchored, and practically oriented response to this gap.

### 7.3 Closing Question

End with a forward-looking provocation.

- As AI systems become more capable and more autonomous in educational contexts, the question of how learners form and regulate trust will become increasingly consequential.
- The deeper question is not whether AI can be trusted in education, but whether educational systems can be designed to produce learners who trust AI appropriately — learners who know when to defer, when to verify, and when to exercise independent judgment.
- Trust calibration is not an obstacle to AI adoption; it is the condition that makes AI adoption educationally defensible.
