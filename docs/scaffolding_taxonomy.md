---
title: "Educational Scaffolding Taxonomy for Trust Calibration"
date: 2026-02-28
status: draft
---

# Educational Scaffolding Taxonomy for Trust Calibration

**Project:** Trust Calibration as the Missing Link in Educational AI Design
**Date:** 2026-02-28
**Status:** Draft

---

## Overview

This document develops a detailed taxonomy of educational scaffolding types as they apply to trust calibration in AI-mediated learning environments. The taxonomy serves two functions: (1) it grounds the trust calibration scaffold concept in the established educational scaffolding literature, demonstrating that trust calibration scaffolds are not a novel design category invented for this project but an application of well-theorized scaffolding principles to a new domain; (2) it provides a design resource — a structured classification of scaffold types, their trust calibration functions, and concrete implementation examples — that can support curriculum designers, AI system developers, and educators who wish to implement trust calibration scaffolding in practice.

The taxonomy is organized in three layers: (a) the established scaffolding types from Hannafin et al. (1999), which constitute the theoretical base; (b) a mapping of each scaffold type to its specific trust calibration function; and (c) six trust calibration scaffold mechanisms derived from the mapping, grounded in specific theoretical traditions.

---

## 1. Established Scaffolding Types: Hannafin et al. (1999)

Hannafin, Land, & Oliver's (1999) taxonomy of scaffolding in open-ended learning environments identifies five types of scaffolding that differ in the cognitive and motivational processes they target. This taxonomy was developed for technology-enhanced learning environments and therefore translates directly to the educational AI context.

### 1.1 Cognitive Scaffolding

**Definition:** Cognitive scaffolding supports the learner's core task-relevant thinking processes — comprehension, analysis, synthesis, problem-solving, and reasoning. It reduces the cognitive load associated with difficult aspects of a task while preserving the cognitive challenge that produces learning.

**Mechanism:** Cognitive scaffolds work by structuring the problem space: they decompose complex tasks into manageable steps, provide worked examples or analogical cases, and offer prompts that direct attention to relevant features of the task.

**Classic examples:** Worked examples that show problem-solving steps; concept maps that organize domain relationships; problem decomposition guides that break a complex task into sub-goals.

**Trust calibration relevance:** In the AI trust context, cognitive scaffolds help learners reason about AI outputs — they support the process of evaluating AI responses, identifying potential errors, and comparing AI reasoning to independent analysis. Cognitive scaffolds for trust calibration are primarily concerned with the quality of the learner's analytical engagement with AI output, not just whether the learner verified it.

**Trust calibration application example:** A scaffold that provides a structured evaluation framework ("Consider the source, check the reasoning, identify any missing alternatives") for assessing an AI response. The scaffold reduces the cognitive effort of knowing what to look for, while preserving the cognitive challenge of doing the looking.

### 1.2 Metacognitive Scaffolding

**Definition:** Metacognitive scaffolding supports learners' monitoring and regulation of their own thinking — their awareness of what they know and do not know, their ability to detect comprehension failures, and their capacity to adjust their strategies in response to monitoring results.

**Mechanism:** Metacognitive scaffolds work by creating explicit monitoring events — moments in the learning process where the learner is prompted to step back, assess the current state of their understanding or performance, and make a deliberate regulatory decision. They externalize the monitoring process that expert learners perform internally.

**Classic examples:** Prediction prompts ("What do you expect the outcome to be? Why?"); self-explanation prompts ("Explain in your own words what you just read"); judgment-of-learning tasks ("Rate your confidence that you could solve a similar problem"); comprehension monitoring checklists.

**Trust calibration relevance:** Metacognitive scaffolding is the most directly relevant scaffold type for trust calibration. Trust calibration is fundamentally a metacognitive task: it requires the learner to monitor the alignment between their trust disposition and the AI system's actual performance — to maintain an accurate model of an external system's capabilities through active, ongoing assessment. Metacognitive trust prompts that require learners to explicitly articulate their trust assessment before, during, and after AI interaction are the core implementation of this scaffold type.

**Trust calibration application example:** "Before you look at the AI's answer, write your own answer to this question. After you read the AI's answer, compare it to yours and rate how much you trust the AI's response (1–5). What specific evidence would help you decide whether the AI is right?"

### 1.3 Motivational Scaffolding

**Definition:** Motivational scaffolding supports learners' engagement, persistence, self-efficacy, and willingness to take on challenging tasks. It addresses the affective dimension of learning, recognizing that cognitive capability alone is insufficient if learners are not motivated to deploy it.

**Mechanism:** Motivational scaffolds work by shaping the learner's perception of the task and their relationship to it — reducing anxiety, building confidence through success experience, connecting the task to learner goals, and providing encouragement that is specific and credible.

**Classic examples:** Goal-setting prompts; progress visualization; success-experience sequences (deliberately sequenced from easier to harder tasks); interest connection activities that link academic content to learner-relevant contexts.

**Trust calibration relevance:** Motivational scaffolding addresses the undertrust problem. Learners who have had negative AI experiences — or who approach AI with strong skepticism — may refuse to engage with AI systems even when those systems are genuinely useful. Motivational trust calibration scaffolds gradually rebuild trust by providing structured evidence of AI capability, beginning with task contexts where AI performance is high and transparent.

**Trust calibration application example:** Present a sequence of AI interactions in task domains where the AI is demonstrably accurate. Provide explicit feedback on AI accuracy after each interaction. Build in reflective prompts: "In this type of question, the AI was [X]% accurate. Does this change your assessment of how much to trust AI on this type of question?" The scaffold builds a calibrated positive trust baseline before introducing AI interactions in more uncertain domains.

### 1.4 Strategic Scaffolding

**Definition:** Strategic scaffolding supports learners in selecting, applying, and adapting task-specific strategies. It provides learners not just with the tools to perform a task but with guidance on when and why to use those tools.

**Mechanism:** Strategic scaffolds work by making expert strategies explicit and teachable — by naming the strategy, demonstrating its application, and providing structured opportunities for learners to practice strategy selection in varied contexts.

**Classic examples:** Reading strategy instruction (before/during/after strategies); problem-solving strategy menus; evaluation frameworks (CRAAP test for source evaluation; SIFT for misinformation detection).

**Trust calibration relevance:** Strategic scaffolding supports learners in developing and applying systematic verification strategies for AI outputs. Learners need not only the motivation to verify AI (motivational scaffolding) and the metacognitive awareness that verification is needed (metacognitive scaffolding) but also the strategic knowledge of how to verify — what evidence to seek, where to find it, and how to weigh it.

**Trust calibration application example:** Teach an explicit AI verification strategy: (1) Identify the type of claim the AI is making (factual, interpretive, procedural). (2) Identify the appropriate verification source for that claim type (primary source, peer-reviewed literature, mathematical derivation). (3) Locate and consult the verification source. (4) Compare the AI's claim to the verification source and update your trust rating. Scaffold application of this strategy through guided practice before fading to independent use.

### 1.5 Procedural Scaffolding

**Definition:** Procedural scaffolding supports learners in navigating the tools, interfaces, and processes of a learning environment. It addresses the operational dimension of learning — ensuring that procedural unfamiliarity with the learning system does not block access to the substantive learning task.

**Mechanism:** Procedural scaffolds work by reducing the cognitive overhead associated with tool use — tutorials, help menus, templates, and structured workflows that allow learners to focus cognitive resources on the learning task rather than on figuring out how the system works.

**Classic examples:** Step-by-step walkthroughs of software tools; templates that structure complex documents (lab reports, argumentative essays); interface tooltips and contextual help.

**Trust calibration relevance:** Procedural scaffolding in the AI trust context supports appropriate patterns of AI usage — ensuring that learners know how to use AI tools in ways that promote calibration rather than bypassing it. This includes guidance on when to consult AI, how to interpret AI uncertainty displays, and how to use AI-provided explanations as evidence for trust assessment rather than simply accepting AI outputs.

**Trust calibration application example:** An AI usage protocol that specifies: "Use the AI to generate an initial response. Review the AI's confidence score and explanation. Identify one aspect of the AI's response you want to verify. Use the verification tool to check that aspect. Update your trust rating before submitting your final answer." The protocol structures the entire AI interaction workflow to embed calibration steps as a matter of procedural routine.

---

## 2. Trust Calibration Function Mapping

The following table maps each scaffolding type to its specific trust calibration function and provides a concrete implementation example.

| Scaffold Type | Trust Calibration Function | Implementation Example |
|---|---|---|
| Metacognitive | Overtrust prevention: requires explicit trust assessment before reliance | "Write your own answer before the AI shows its response; then rate your trust in the AI's answer and explain your rating" |
| Strategic | Critical verification induction: provides systematic methods for evaluating AI accuracy | "Find 3 pieces of evidence to evaluate the AI's answer — at least one must be from a primary source" |
| Motivational | Undertrust mitigation: builds calibrated positive trust through structured success experience | Present AI in domains where it performs reliably and transparently; show accuracy statistics; build gradual trust |
| Procedural | Appropriate usage pattern formation: embeds calibration steps in AI interaction workflow | AI usage guidelines and structured protocols that specify when, how, and with what verification to use AI |
| Cognitive | Analytical depth: supports quality reasoning about AI outputs, not just verification | Structured evaluation framework for analyzing AI responses; domain-specific checklists |
| Strategic + Metacognitive | Calibration monitoring: combining strategy and self-reflection to develop ongoing calibration capacity | "After using the AI, assess: Did I verify appropriately? Was my initial trust rating accurate? What will I do differently next time?" |

---

## 3. Six Trust Calibration Scaffold Mechanisms

Drawing on the scaffolding taxonomy above and the broader literature reviewed in `theoretical_foundation.md`, six specific trust calibration scaffold mechanisms are identified. Each mechanism is grounded in a specific theoretical tradition and targets a specific aspect of the trust calibration process.

### 3.1 Metacognitive Prompts (Schraw, 1998; Guo et al., 2022)

**Theoretical basis:** Schraw's (1998) framework for metacognitive instruction; Guo et al.'s (2022) meta-analysis (g = 0.50 for SRL outcomes; g = 0.40 for learning outcomes).

**Mechanism description:** Prompts that require learners to externalize their thinking about AI responses before, during, and after AI consultation. These prompts interrupt the default pattern of passive AI consumption and create explicit metacognitive monitoring events.

**Trust calibration function:** Overtrust prevention. By requiring learners to formulate independent judgments before seeing AI responses, metacognitive prompts prevent the automatic adoption of AI answers without scrutiny.

**Core implementation form:** "Formulate your hypothesis / answer / position before seeing the AI's response. After seeing the AI's response, compare it to your own and rate your trust in the AI's response (1–5). Provide a one-sentence justification for your rating."

**Variations:**
- Pre-AI prompt only: "What do you expect the AI to say, and why?"
- Post-AI prompt only: "Now that you have seen the AI's response, how confident are you that it is correct? What would increase or decrease your confidence?"
- Pre-and-post prompt: Full cycle including prediction, review, and trust rating update.
- Error-detection prompt: "Is there anything in the AI's response that surprises you or seems inconsistent with what you already know? If so, describe it."

**Fading implementation:** Begin with pre-and-post prompts for all AI interactions. Fade to post-AI prompt only as calibration accuracy improves (measured by alignment between trust ratings and AI accuracy). Fade to on-demand prompts (available but not required) as calibration reaches proficiency threshold.

**Evidence grounding:** Guo et al. (2022) meta-analysis provides the strongest quantitative evidence base. Effect sizes (g = 0.50 for SRL; g = 0.40 for learning) are substantial and were robust across subject areas and educational levels. Prompt specificity moderated effects: more specific prompts produced larger effects.

### 3.2 Desirable Difficulties (Bjork & Bjork, 1994, 2011)

**Theoretical basis:** Bjork & Bjork's (1994, 2011) research program demonstrating that conditions that slow acquisition enhance long-term retention and transfer.

**Mechanism description:** Design features that introduce productive friction into AI interaction, slowing the consumption of AI outputs and requiring active learner engagement before or instead of immediate AI assistance.

**Trust calibration function:** Dependency prevention and calibration deepening. By slowing AI access, desirable difficulty mechanisms prevent the habit formation of reflexive AI reliance and create space for calibrated trust assessment.

**Core implementation forms:**
- **Response delay:** AI response is not immediately displayed; learner is required to type their own answer first, or wait a specified period, before AI output appears.
- **Evidence requirement:** Before the AI response is displayed or before the learner can proceed, they must identify at least one corroborating source or piece of evidence.
- **Spaced AI access:** In some task sequences, AI access is withheld during initial problem-solving, available only after a defined period of independent engagement.
- **Interleaved verification tasks:** AI assistance is interleaved with independent verification tasks; the learner alternates between consulting AI and checking their own understanding without AI.

**Trust calibration function specifics:**
- Response delay promotes independent thinking and reduces anchoring on AI output.
- Evidence requirement builds the verification habit and strategic scaffold for source evaluation.
- Spaced access builds independent capability that makes trust calibration possible (a learner who has no independent capability cannot meaningfully assess whether AI capability exceeds their own).

**Fading implementation:** Reduce delay length and evidence requirements as calibration accuracy improves. Ultimately, the goal is a learner who self-imposes productive friction — who delays AI consultation and seeks verification without external prompt — because they have internalized the value of calibrated trust.

**Evidence grounding:** Bjork & Bjork's program spans three decades and includes laboratory and applied studies. The desirable difficulty effect is robust across skill domains. The specific application to AI trust is an extension of the underlying mechanism, not a direct replication.

### 3.3 Productive Failure Points (Kapur, 2008)

**Theoretical basis:** Kapur's (2008) productive failure research demonstrating the learning benefits of error experience before direct instruction.

**Mechanism description:** Deliberately designed sequences in which learners encounter AI errors before receiving instruction in verification techniques. The error encounter creates a productive failure state — the learner experiences the mismatch between their trust and the AI's actual performance — which prepares the learner to engage deeply with subsequent verification instruction.

**Trust calibration function:** Error experience activation; verification instruction readiness; overtrust correction through direct evidence.

**Core implementation sequence:**
1. **Error exposure:** Present learners with a task where the AI makes a specific type of error (factual error, reasoning error, hallucination, scope violation). Provide minimal guidance; allow learners to engage with the AI output as they would normally.
2. **Discovery support:** Provide a hint or partial cue that directs attention toward the error without fully revealing it. Monitor whether learners detect the error independently.
3. **Error revelation:** Reveal the error explicitly, with an explanation of what went wrong and why.
4. **Verification instruction:** Provide direct instruction in a verification technique targeted at the type of error encountered. Connect the instruction explicitly to the error experience: "The AI made this type of error because [reason]. To catch this type of error in the future, use [verification technique]."
5. **Re-engagement:** Return to AI-assisted tasks with the verification scaffold in place; learners now have both error experience and a verification strategy.

**Trust calibration function specifics:** Productive failure in the trust domain activates prior knowledge (what the learner thought AI could do), creates surprise (the mismatch between expectation and experience), and establishes the problem that verification instruction solves. This sequence produces deeper understanding of the verification technique than instruction-first approaches.

**Design considerations:** Error selection matters. The error chosen for the productive failure sequence should be: (a) representative of a genuine and common AI failure mode; (b) detectable by a learner with appropriate domain knowledge; (c) consequential enough to motivate verification without being so catastrophic as to produce generalized undertrust. Common productive AI errors for educational contexts include: plausible-sounding factual errors, overconfident claims about uncertain matters, domain scope violations (answering outside the AI's competence), and reasoning errors that produce correct-sounding but logically invalid arguments.

**Evidence grounding:** Kapur (2008) and subsequent replications provide the theoretical and empirical basis. The specific application to AI trust is a novel extension, warranting empirical validation.

### 3.4 AI Uncertainty Transparency (XAI Literature)

**Theoretical basis:** Explainable AI (XAI) literature; Gunning et al. (2019); Lee & See (2004) calibration criterion.

**Mechanism description:** System-level design features that make AI uncertainty, confidence levels, and capability boundaries visible to learners. Uncertainty transparency gives learners external, system-provided information that supports trust calibration — they do not have to infer AI capability entirely from output quality; the system communicates its own uncertainty.

**Trust calibration function:** Calibration support through external information; reducing the inference burden on the learner; enabling learners to match their trust to system-disclosed confidence.

**Core implementation forms:**
- **Confidence score display:** AI responses are accompanied by a numerical or categorical confidence score (e.g., "High confidence," "Medium confidence," "Low confidence — verify this response").
- **Uncertainty flagging:** Specific claims within an AI response are flagged with uncertainty indicators (e.g., italics, color coding, or tooltip explanations) when the AI's confidence is below a threshold.
- **Capability scope disclosure:** The AI system explicitly states the domains and task types within which it is reliable and those in which it is not (e.g., "I am more reliable on factual recall tasks than on interpretive or creative tasks in this domain").
- **Source attribution:** AI responses include attribution to sources where the information originates, enabling learners to evaluate source quality as a proxy for AI reliability.

**Trust calibration function specifics:** Uncertainty transparency does not replace learner calibration monitoring; it supplements it. A learner who sees a low-confidence indicator is provided with a signal that prompts verification — but they must still perform the verification. Transparency reduces the effort of determining when to verify (the system signals this) while preserving the learning value of the verification task itself.

**Design considerations:** Confidence scores must be meaningful and calibrated to be useful. A system that displays high confidence for all outputs does not support trust calibration; it actively misleads it. Effective uncertainty transparency requires that confidence scores are correlated with actual accuracy — a property that requires careful system design and validation. Poorly calibrated confidence scores can produce calibration damage: learners who trust the confidence scores will be miscalibrated in proportion to the scores' inaccuracy.

**Evidence grounding:** XAI literature provides the theoretical basis; empirical evidence on the trust calibration effects of specific uncertainty display formats is an active research area. Existing evidence suggests that calibrated confidence displays reduce overtrust in high-accuracy contexts and support appropriate skepticism in low-accuracy contexts (consistent with Lee & See's calibration criterion).

### 3.5 Socratic Dialogue

**Theoretical basis:** Socratic method (Plato); Collins & Stevens (1982) Socratic tutoring model; retained from prior project materials as an established educational term.

**Mechanism description:** A structured dialogue format in which the AI (or the teacher, or a peer) responds to learner statements not by providing information but by asking questions that require the learner to examine the basis of their claims, identify assumptions, and reason to conclusions independently.

**Trust calibration function:** Epistemic autonomy preservation; critical engagement with AI outputs; resistance to passive reliance.

**Core implementation forms in AI trust contexts:**
- **AI-initiated Socratic dialogue:** Instead of (or before) providing a direct answer, the AI responds with a question: "What do you think the answer is, and what is your reasoning?" After the learner responds, the AI provides its own answer and the learner compares.
- **Teacher-facilitated dialogue about AI output:** Teacher poses Socratic questions about AI responses students have received: "Why do you think the AI answered this way? What assumptions is the AI making? Can you find a case where this answer would be wrong?"
- **Peer Socratic discussion:** Students in pairs or small groups discuss AI responses Socratically: one student defends the AI's answer; the other challenges it with questions.

**Trust calibration function specifics:** Socratic dialogue resists the passive acceptance of AI outputs by requiring the learner to engage argumentatively with the AI's reasoning. It builds the habit of asking "why" and "on what basis" — habits that are directly transferable to trust calibration monitoring. Unlike metacognitive prompts (which prompt reflection without dialogue), Socratic dialogue builds the capacity for sustained critical interrogation of AI claims.

**Retention from prior materials:** "Socratic dialogue" is retained from prior project materials as a recognized and well-grounded educational term. Unlike "checkpoint" and other deprecated terms, "Socratic dialogue" already meets the criteria for established educational research terminology: it has deep historical roots, a recognized theoretical basis in instructional design (Collins & Stevens, 1982), and a clear, consistent referent.

**Evidence grounding:** Socratic questioning has strong empirical support in the critical thinking literature. Collins & Stevens' (1982) formalization of Socratic tutoring provides a systematic implementation basis. Effects on AI trust calibration specifically require empirical investigation.

### 3.6 Progressive Fading (Wood, Bruner, & Ross, 1976)

**Theoretical basis:** Wood, Bruner, & Ross (1976) scaffolding theory; Collins et al. (1989) cognitive apprenticeship; Vygotsky (1978) Zone of Proximal Development.

**Mechanism description:** A scaffold management protocol in which the intensity, frequency, and prescriptiveness of trust calibration scaffolds are gradually reduced as learner calibration accuracy improves. Progressive fading transforms externally regulated calibration (the system prompts verification, requires evidence, delays responses) into internally regulated calibration (the learner self-initiates verification, seeks evidence without prompt, self-imposes delays).

**Trust calibration function:** Transfer of calibration regulation from system to learner; development of autonomous trust calibration as a durable, generalized competence.

**Core fading protocol:**
Stage 1 — Full scaffolding: All trust calibration scaffold mechanisms active. Metacognitive prompts required before and after every AI interaction. Evidence requirement active. Response delay at maximum. AI uncertainty transparency fully displayed.

Stage 2 — Partial scaffolding: Metacognitive prompts required before or after AI interaction (not both). Evidence requirement active for high-stakes tasks only. Response delay reduced. AI uncertainty transparency displayed on request.

Stage 3 — Minimal scaffolding: Metacognitive prompts available on demand but not required. Evidence requirement active only for tasks flagged as high-uncertainty by AI confidence display. Response delay eliminated. Uncertainty transparency available but default-off.

Stage 4 — Independent performance: All scaffolding removed. Learner self-initiates calibration monitoring. Teacher or system observes for calibration failure (overtrust or undertrust) and can re-introduce scaffolding if needed.

**Calibration-accuracy-linked fading:** The fading protocol is ideally linked to measured calibration accuracy rather than to time elapsed or task count. A formal implementation would compute a learner's trust calibration score (e.g., gamma correlation between trust ratings and AI accuracy scores across a set of interactions) and trigger stage transitions when the score crosses defined thresholds. This makes fading adaptive and data-driven rather than fixed-schedule.

**Evidence grounding:** Wood, Bruner, & Ross (1976) provide the foundational theoretical basis. Collins et al. (1989) cognitive apprenticeship model elaborates fading as a core component of expert-to-novice skill transfer. Hattie (2009) d = 0.82 for scaffolding provides the meta-analytic benchmark.

---

## 4. The Fading Principle and Adaptive Calibration

### 4.1 Core Scaffolding Property

Fading is not an optional feature of scaffolding — it is definitional. Scaffolding that does not fade is not scaffolding; it is permanent support, which defeats the developmental purpose of the educational enterprise. Wood, Bruner, & Ross (1976) define scaffolding precisely in terms of its temporary, contingent character. Collins et al. (1989) make fading one of the four core components of cognitive apprenticeship alongside modeling, coaching, and articulation.

For trust calibration scaffolds, this means that the goal of the design intervention is not to create learners who rely on scaffolds to verify AI appropriately — it is to create learners who have internalized the calibration monitoring process so that they can perform it autonomously. The scaffold is scaffolding toward this autonomy.

### 4.2 Applied to Trust Calibration: The Inverse Relationship

The fading principle applied to trust calibration produces a clear design proposition:

**Calibration Accuracy UP → Scaffold Intensity DOWN**

As a learner demonstrates improving alignment between their trust ratings and AI accuracy (increasing calibration accuracy), the intensity of the trust calibration scaffold should decrease correspondingly. This inverse relationship is the operational form of the fading principle in the trust calibration domain.

Conversely, if calibration accuracy decreases — if a learner who had been well-calibrated begins to show overtrust or undertrust patterns — scaffold intensity should increase. This responsive re-scaffolding is the implementation of the contingency principle: scaffolding is always calibrated to the current level of learner competence, adjusting as competence changes.

**Formal expression:**
Scaffold Intensity (SI) is inversely proportional to Calibration Accuracy (CA):

SI ∝ 1 / CA

Where CA is measured by the alignment between learner trust ratings and AI response accuracy scores across a defined interaction set. As CA approaches its maximum value (perfect calibration), SI approaches its minimum value (no scaffolding). As CA decreases (miscalibration), SI increases (stronger scaffolding).

This is a design ideal, not an implemented algorithm; the formal expression serves as a conceptual guide for adaptive scaffold design.

### 4.3 Vygotsky's ZPD Connection

Vygotsky's (1978) Zone of Proximal Development (ZPD) defines the space between what a learner can do independently and what they can do with support. Scaffolding operates within the ZPD: it is calibrated to the current upper limit of independent performance and provides the minimum support needed to extend performance to the upper limit of supported performance.

Applied to trust calibration: the ZPD for trust calibration is the distance between a learner's current autonomous calibration accuracy and the calibration accuracy achievable with optimal trust calibration scaffold support. The scaffold operates within this zone, providing support that is sufficient to enable calibration without so much support that the learner is not developing the underlying capacity.

As scaffolding successfully develops calibration capacity, the ZPD shifts upward: what was previously possible only with scaffold support becomes possible independently, and a new ZPD is established at a higher level. The fading protocol tracks this shift: as the lower boundary of the ZPD rises (independent calibration accuracy improves), scaffold intensity is reduced to maintain the scaffold's operation within the new ZPD.

This Vygotskian framing has a practical implication for design: scaffold intensity should be the minimum sufficient to enable calibration in the current ZPD, not the maximum available. Over-scaffolding — providing more support than necessary for the current ZPD — prevents the development of independent capacity and stalls the ZPD shift. This is the scaffolding equivalent of the desirable difficulty principle: some productive struggle within the ZPD is necessary for development.

---

## 5. SDT Tension Resolution

### 5.1 The Tension: Friction vs. Autonomy

Self-Determination Theory (Deci & Ryan, 1985, 2000) identifies autonomy as one of three universal psychological needs (alongside competence and relatedness) whose satisfaction is necessary for intrinsic motivation, engagement, and well-being. SDT predicts that external constraints on learner behavior — including verification requirements, response delays, and evidence mandates — will undermine autonomy satisfaction and reduce intrinsic motivation.

Trust calibration scaffolds introduce friction: they require verification before reliance, delay AI access, and mandate evidence-seeking. This friction is, by SDT's logic, a threat to autonomy satisfaction and therefore a potential motivation risk.

This creates a genuine tension in trust calibration scaffold design: scaffolds that are effective at promoting calibration through constraint may simultaneously undermine the motivational conditions that make learning sustainable.

### 5.2 Resolution 1: Temporary Scaffolding Until Competence Is Secured

The tension is substantially resolved by the fading principle. SDT's autonomy need is not violated by temporary constraint that builds the competence required for meaningful autonomy. A learner who is constrained by verification scaffolds during the development of trust calibration competence is not permanently autonomy-deprived; they are temporarily constrained in the service of developing the capacity for meaningful, calibrated autonomy in AI use.

SDT distinguishes between autonomy (self-direction according to one's own values and goals) and independence (freedom from external constraint). Trust calibration scaffolds constrain independence but can support autonomy if learners understand and endorse the rationale for the scaffold. Rationale provision — explaining to learners why verification scaffolds are in place and how they serve the learner's own goals — is therefore a critical component of motivationally sustainable trust calibration scaffold design.

**Implementation:** Accompany trust calibration scaffolds with explicit rationale provision:
- "This verification step is here to help you develop the judgment to use AI effectively on your own."
- "Checking the AI's answer now builds your ability to know when to trust AI in the future, when these checks won't be required."
- "This is temporary — as your trust judgment develops, you'll have more freedom in how you use AI tools."

Rationale provision transforms external regulation (the scaffold is a rule to comply with) toward identified regulation (the scaffold is a tool the learner chooses to use because they endorse its purpose) — a move SDT identifies as preserving autonomy satisfaction within constrained contexts.

### 5.3 Resolution 2: ZPD Connection — Scaffolding Within the Zone

Vygotsky's ZPD framework provides a second resolution to the SDT tension. Scaffolding that operates within the ZPD is neither frustratingly beyond the learner's reach nor boringly within already-established competence. It is optimally challenging: difficult enough to require effort and scaffold support, achievable enough to produce success with that support.

This optimal challenge is precisely the condition that Csikszentmihalyi (1990) associates with flow — the deeply engaged, intrinsically motivated state in which challenge and skill are in dynamic balance. When trust calibration scaffolds are calibrated to the learner's current ZPD, they create conditions for optimal challenge rather than frustrating constraint.

**Design implication:** Trust calibration scaffold difficulty (the complexity of the verification task, the stringency of the evidence requirement, the length of the response delay) should be calibrated to the learner's current calibration competence. Scaffolds that are too demanding — requiring verification processes beyond the learner's current strategic repertoire — produce frustration and autonomy threat. Scaffolds calibrated within the ZPD produce productive engagement.

### 5.4 Resolution 3: Competence as the Path to Autonomy

SDT's competence need — the need to feel effective and capable — provides a third resolution. Trust calibration scaffolds, when effective, increase competence: learners who use them develop more accurate trust assessments and more reliable verification strategies. This competence gain supports SDT's competence need directly.

Moreover, the competence developed through trust calibration scaffolding is competence that enables richer, more meaningful autonomy in AI use. A learner who has developed calibrated trust can use AI more flexibly, more selectively, and more strategically — because they have the judgment to know when AI assistance is appropriate and when it is not. This expanded autonomy is the goal toward which trust calibration scaffolding is directed. The temporary constraint of the scaffold produces the competence that makes genuine autonomy possible.

**Summary of tension resolution:**

| SDT Need | Tension Source | Resolution |
|---|---|---|
| Autonomy | Scaffolds constrain learner behavior | Fading removes constraints as competence develops; rationale provision supports autonomous endorsement of scaffold |
| Competence | Scaffolds may signal learner incompetence | Scaffolds build competence; calibration accuracy feedback makes growth visible |
| Relatedness | Scaffolds are impersonal system constraints | Teacher-mediated verification integrates human relationship into scaffolded AI interaction |
