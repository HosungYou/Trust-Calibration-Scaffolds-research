## 5. The Two-Level Trust Calibration Framework

This section presents the core contribution of this paper: a Two-Level Trust Calibration Framework integrating learner-level trust dynamics (Level 1) with system-level oversight design (Level 2) through an adaptive calibration cycle. The framework is evidence-informed and conceptual; its novelty lies not in the individual components, each grounded in established theory, but in their integration and application to trust calibration in educational AI.

### 5.1 From Fragmented Trust to Integrated Framework

As Section 4 documented, existing research addresses trust dynamics and system design in isolation. Studies of learner trust do not prescribe how systems should respond to miscalibration; studies of AI scaffolding rarely incorporate learner trust state as a design variable. No existing framework connects these levels through a dynamic feedback mechanism.

The Two-Level Trust Calibration Framework addresses this gap by drawing on four theoretical traditions: trust-in-automation theory (Lee & See, 2004; Hoff & Bashir, 2015), which provides the distinction between trust level and trust calibration; scaffolding theory (Wood et al., 1976), which supplies the pedagogical logic of contingent support and fading; self-regulated learning theory (Zimmerman, 2000; Winne & Hadwin, 1998), which structures the calibration cycle; and adjacent field evidence on desirable difficulties (Bjork & Bjork, 2011), productive failure (Kapur, 2008, 2016), and trust repair (de Visser et al., 2020), which provides specific calibration mechanisms with strong empirical grounding awaiting systematic application to educational AI. The framework is integrative: system-level design shapes the conditions under which learner-level calibration operates, and learner-level signals continuously inform system-level adjustments.

### 5.2 Level 1 --- Learner Trust Dynamics (Micro)

Level 1 models the cognitive and metacognitive processes through which learners form and revise trust judgments during AI interaction. Its structure adapts Wang et al.'s (2025) integrated model with a critical extension: explicit incorporation of metacognitive processes as mediators of trust calibration.

**Trust antecedents.** AI system characteristics --- transparency, observed accuracy, interface quality, behavioral consistency --- serve as informational inputs from which learners construct mental models of AI reliability that may be accurate or distorted depending on the learner's evaluative capacity and the information the system provides.

**Trust formation and metacognition.** Trust operates as a dynamic judgment interacting with metacognitive processes across three layers (Hoff & Bashir, 2015): *dispositional trust* (stable individual differences in technology trust propensity), *situational trust* (shaped by task difficulty, stakes, and immediate AI behavior), and *learned trust* (accumulated through direct experience and subject to updating). The learner's capacity for self-monitoring and strategic regulation (Zimmerman, 2000) determines whether trust judgments undergo reflective scrutiny or are accepted unreflectively --- the distinction separating calibrated trust from the uncritical reliance documented by Bastani et al. (2025).

**Internal calibration mechanisms.** Metacognitive monitoring enables learners to recognize discrepancies between their understanding and AI outputs. Critical evaluation skills support systematic assessment of output quality. AI literacy --- knowledge of how AI systems function, their capabilities, and characteristic failure modes (Long & Magerko, 2020) --- provides the foundation for informed trust judgments. Self-directed learning dispositions influence whether learners actively verify AI-provided information or passively consume it.

**Trust manifestation.** Behavioral output takes two forms: reliance (accepting AI output) and resistance (rejecting or modifying it). Neither is inherently appropriate; value depends on calibration to actual AI reliability. Excessive reliance on unreliable output constitutes overtrust --- the condition in Bastani et al. (2025) where unassisted performance deteriorated as students bypassed effortful processing. Excessive resistance to reliable output constitutes undertrust, resulting in missed learning opportunities (Parasuraman & Riley, 1997).

**Learning outcomes.** Overtrust degrades learning through cognitive offloading (Risko & Gilbert, 2016), reducing effortful processing necessary for durable encoding. Undertrust degrades learning through opportunity cost. Level 1 alone is descriptive; it models what happens within the learner but does not prescribe system intervention, motivating Level 2.

### 5.3 Level 2 --- System-Mediated Trust Calibration (Macro)

Level 2 specifies six Trust Calibration Scaffolds targeting specific dimensions of trust miscalibration. The term "scaffold" is deliberate: these interventions are contingent, fading, and responsibility-transferring --- the defining properties of pedagogical scaffolding (Wood et al., 1976).

**Scaffold 1: Metacognitive Prompts.** System-generated prompts requiring learners to articulate or evaluate their reasoning before, during, or after AI interaction (Schraw & Dennison, 1994; Bannert et al., 2009). Targets overtrust by activating self-monitoring processes that may remain dormant during fluent AI interaction. Guo et al.'s (2022) meta-analysis of metacognitive scaffolding reported a moderate-to-strong effect (*g* = 0.50) on self-regulated learning outcomes, providing evidence-informed support for this mechanism.

**Scaffold 2: Desirable Difficulties.** Deliberate challenges that impede immediate performance but enhance long-term learning and trust calibration (Bjork & Bjork, 2011) --- including requiring initial solution attempts before AI access and introducing response delays that prevent reflexive reliance. Restores effortful cognitive engagement that unconstrained AI access can eliminate.

**Scaffold 3: Productive Failure Points.** Learning sequences structured so learners first attempt problems without AI, experience knowledge boundaries, then receive AI support with explicit guidance on how the AI's contribution extends their attempts (Kapur, 2008, 2016). Evidence from mathematics education indicates substantial advantages over conventional instruction, and the mechanism directly addresses both overtrust (building awareness of one's capabilities) and undertrust (demonstrating where AI adds genuine value).

**Scaffold 4: AI Uncertainty Transparency.** Explicit communication of AI confidence levels, limitations, and domain boundaries, enabling informed trust judgments calibrated to system reliability rather than global impressions of AI competence (Lee & See, 2004). Implementation includes confidence visualizations and domain limitation disclosures. The goal is appropriately differentiated trust, not indiscriminate trust reduction.

**Scaffold 5: Socratic Dialogue.** AI-initiated questioning that probes learner understanding rather than providing direct answers (Chi et al., 2001). Shifts the interaction mode from answer-giving to thinking-prompting, disrupting cognitive offloading while maintaining productive engagement with AI as an intellectual partner.

**Scaffold 6: Progressive Autonomy Release.** Gradual reduction of scaffold intensity as evidence of improved calibration accumulates (Wood et al., 1976; Pea, 2004). Learners demonstrating calibrated trust receive less prompting, fewer imposed difficulties, and greater autonomy. Without fading, scaffolding risks creating dependence on external support rather than developing internal calibration capacity.

Two qualifications apply. First, while adjacent field evidence substantially grounds these scaffolds --- including de Visser et al.'s (2020) demonstration that calibration interventions can restore appropriate trust following automation failures --- direct empirical evidence for these mechanisms deployed specifically for trust calibration in educational AI is sparse. The framework is evidence-informed: its components draw on established theory from related fields, but the integrated application to educational AI trust calibration has not been empirically tested. This positioning as an evidence-informed conceptual framework is consistent with the legitimate purposes of critical reviews (Grant & Booth, 2009; Peters et al., 2020). Second, these six scaffolds are not exhaustive; they represent the mechanisms with the strongest current theoretical grounding.

### 5.4 The Adaptive Calibration Cycle

The Adaptive Calibration Cycle connects Level 1's descriptive model with Level 2's prescriptive design through continuous dynamic feedback, aligned with the cyclical structure of self-regulated learning theory (Zimmerman, 2000).

**Stage 1 --- PERFORMANCE.** The learner interacts with the AI system, generating observable behavioral data: output acceptance/rejection decisions, modifications to AI suggestions, time invested in verification, information-seeking actions, and usage patterns across task types. Trust is indexed through behavioral manifestations rather than self-report (Lee & See, 2004).

**Stage 2 --- MONITORING.** The system detects patterns signaling the learner's trust state --- acceptance ratios, modification rates, examination time, verification frequency, and consistency across reliability levels. System monitoring supplements the learner's own metacognitive monitoring; the framework progressively transfers monitoring responsibility to the learner as calibration improves.

**Stage 3 --- EVALUATION.** The system evaluates the learner's trust state as overtrust, undertrust, or calibrated by comparing trust-indexed behaviors against the AI's actual reliability profile. A learner who consistently accepts AI outputs is not necessarily overtrusting; if the AI is reliable for those tasks, the behavior may reflect calibrated efficiency. The same behavior directed at unreliable outputs constitutes overtrust. The Trust-Reliability Matrix below provides the evaluative framework.

**Stage 4 --- ADAPTATION.** Scaffold intensity is adjusted: overtrust triggers intensification (desirable difficulties, metacognitive prompts, Socratic dialogue); undertrust triggers transparency scaffolds (confidence information, guided comparison tasks); calibrated trust triggers progressive autonomy release with continued monitoring for calibration drift.

The Dynamic Scaffolding Principle formalizes this bidirectional responsiveness: oversight decreases as calibration improves through fading and expanded autonomy; oversight increases as calibration deteriorates through scaffold intensification. This distinguishes the framework from static designs that apply uniform constraints regardless of learner state.

**Figure 2** presents the Two-Level Framework visually: Level 2 in the upper register, Level 1 in the lower register, and the Adaptive Calibration Cycle as a central band. Bidirectional arrows indicate the sensing pathway (behavioral data flowing upward) and the adjusting pathway (scaffold modifications flowing downward).

**Figure 3** introduces the Trust-Reliability Calibration Matrix, mapping learner trust (high vs. low) against AI reliability (high vs. low) to produce four calibration states.

*Quadrant I: High Trust + High Reliability = Calibrated Appropriate Use.* Trust is warranted. Progressive autonomy release is appropriate; continued heavy scaffolding would be counterproductive.

*Quadrant II: High Trust + Low Reliability = Overtrust ("Bastani Trap").* The most dangerous miscalibration. The learner trusts unreliable AI outputs, resulting in cognitive offloading and skill atrophy --- precisely the condition documented by Bastani et al. (2025). Scaffold response: intensification through desirable difficulties, productive failure, and metacognitive prompts.

*Quadrant III: Low Trust + High Reliability = Undertrust / Missed Benefit.* Skepticism that is virtuous in Quadrant II is maladaptive here. Scaffold response: transparency mechanisms making reliability evidence visible, guided comparison tasks, and productive failure experiences demonstrating where AI assistance adds value.

*Quadrant IV: Low Trust + Low Reliability = Calibrated Avoidance.* Low trust accurately reflects low reliability. Scaffold response: reinforce verification habits and AI literacy, monitor for drift toward overtrust as AI systems improve.

**The Initialization Principle.** A potential circularity concern --- the system must know calibration state to select scaffolds, but calibration state is shaped by scaffolding --- is addressed through explicit initialization: when the learner's state is unknown, the system defaults to high oversight at maximum scaffold intensity. As behavioral data accumulates, the system refines its model and adjusts accordingly. This mirrors the foundational scaffolding principle of maximum initial support with progressive fading (Wood et al., 1976), reframing apparent circularity as adaptive operation under uncertainty.

### 5.5 Evidence Mapping

Table 2 maps each framework component to its evidence sources and strength assessment, ensuring transparency about the evidence base.

**Table 2.** Evidence mapping for Two-Level Trust Calibration Framework components.

| Framework Component | Primary Evidence Source | Evidence Type | Strength Assessment |
|---|---|---|---|
| Metacognitive Prompts | Guo et al. (2022); Bannert et al. (2009) | Direct (SRL, technology-enhanced learning) | Strong (*g* = 0.50 for SRL outcomes) |
| Desirable Difficulties | Bjork & Bjork (2011) | Adjacent (cognitive psychology) | Strong (robust across learning domains) |
| Productive Failure | Kapur (2008, 2016) | Adjacent (mathematics education) | Strong (substantial advantages over conventional instruction) |
| AI Uncertainty Transparency | XAI literature; Lee & See (2004) | Adjacent (HCI, human factors) | Moderate (demonstrated in automation, limited in educational AI) |
| Socratic Dialogue | Chi et al. (2001) | Adjacent (tutoring, dialogue-based learning) | Moderate (evidence for questioning over telling, limited in AI contexts) |
| Progressive Autonomy Release | Wood et al. (1976); Pea (2004) | Direct (scaffolding theory) | Strong (foundational principle; *d* = 0.82, Hattie, 2009) |
| Adaptive Calibration Cycle | Zimmerman (2000); Winne & Hadwin (1998) | Structural analogy (SRL theory) | Moderate (SRL cycle established; system-level application is novel) |
| Trust Calibration in Educational AI | Sparse | Gap identified | Weak (primary gap motivating this framework) |
| Two-Level Integration | Novel contribution | Conceptual synthesis | Framework-level (no direct precedent) |

The evidence mapping reveals two key patterns. First, individual scaffold components are grounded in established, well-replicated research. Second, the evidence base weakens at the points of novel contribution: application to AI-specific trust calibration and integration through the adaptive cycle. These gaps delineate the empirical questions that future research must address to move from evidence-informed conceptual framework to evidence-based prescriptive model. The framework's contribution is the systematic synthesis connecting learner trust dynamics, calibration scaffolds, and adaptive oversight within a unified architecture --- a positioning consistent with the critical review methodology's support for identifying conceptual gaps and proposing integrative frameworks (Grant & Booth, 2009; Peters et al., 2020).
