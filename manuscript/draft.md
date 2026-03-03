# Trust Calibration as the Missing Link in Educational AI Design:
# A Critical Review and Evidence-Informed Conceptual Framework

## Abstract

The rapid integration of generative AI into education raises a critical question: do learners trust AI systems appropriately? Bastani et al. (2025) demonstrated that unrestricted AI tutoring access produced 17% lower performance on unassisted assessments, attributable to uncalibrated overtrust and cognitive offloading. Yet existing frameworks in educational AI address trust formation and technology acceptance without addressing trust calibration --- the alignment between a learner's trust and the AI system's actual reliability. This paper presents a critical review of trust in educational AI research (2015--2026), analyzing 73 studies from Web of Science and Scopus across trust conceptualizations, theoretical frameworks, measurement approaches, and oversight design. The review reveals a pronounced calibration gap: 86.3% of studies provided no explicit trust definition, only 8.2% measured trust empirically, and zero studies measured trust calibration accuracy. Over half (53.4%) employed no identifiable theoretical framework, and only 4.1% explicitly addressed calibration. To address this gap, we propose an evidence-informed Two-Level Trust Calibration Framework integrating: (a) Level 1 --- Learner Trust Dynamics, modeling how trust forms and miscalibrates through cognitive and metacognitive processes; (b) Level 2 --- System-Mediated Trust Calibration, specifying six scaffolds grounded in established educational theory; connected through (c) an Adaptive Calibration Cycle in which scaffold intensity adjusts based on behavioral signals of trust calibration. The paper distinguishes trust calibration from self-regulated learning calibration, introduces the Trust-AI Reliability Matrix for diagnostic assessment, and derives five design principles for trust-calibrated educational AI.

**Keywords:** trust calibration, educational AI, scaffolding, self-regulated learning, human oversight, generative AI


---

## 1. Introduction

The promise of artificial intelligence in education rests on a deceptively simple assumption: that giving learners access to capable AI tools will improve learning. A landmark study by Bastani et al. (2025), published in the *Proceedings of the National Academy of Sciences*, dismantled this assumption. In a large-scale randomized controlled trial involving nearly a thousand students, unrestricted access to ChatGPT not only failed to improve learning outcomes but actively harmed them: students performed 17% worse on subsequent unassisted assessments. The mechanism was not a failure of AI capability but a failure of trust calibration --- students uncritically accepted AI-generated outputs, bypassing the effortful cognitive processing that constitutes genuine learning. When a tutoring-oriented version that withheld direct answers was introduced, the negative effects disappeared. This finding underscores a fundamental insight: the educational value of AI depends not on what the technology can do, but on whether learners trust it appropriately.

The rapid integration of generative AI into higher education has created a *design dilemma of autonomy and oversight*. Granting AI systems broad autonomy risks fostering the uncritical dependence Bastani et al. (2025) documented. Imposing rigid constraints risks undermining the flexibility that makes AI-assisted learning potentially transformative (Kasneci et al., 2023). Navigating this dilemma requires understanding the mechanism that mediates between AI capability and learning outcomes --- a mechanism that current research has largely overlooked.

The educational AI literature has grown rapidly, examining learning outcomes (Cotton et al., 2024), learner acceptance (Al-Adwan et al., 2023), and pedagogical integration (Baidoo-Anu & Ansah, 2023). Yet a critical variable remains undertheorized: learner trust. Trust is not merely an affective response but a *calibration problem*. Trust calibration refers to the correspondence between a person's trust in a system and the system's actual capabilities (Lee & See, 2004). Overtrust --- where perceived capability exceeds actual capability --- leads to uncritical acceptance and cognitive offloading. Undertrust leads to rejection of beneficial AI assistance (Parasuraman & Riley, 1997).

Despite this centrality, existing frameworks do not adequately address trust calibration. Technology acceptance models (Davis, 1989; Venkatesh et al., 2003) treat trust as a predictor of adoption. Self-regulated learning frameworks (Zimmerman, 2000) address self-monitoring but not calibration of judgments about external AI systems. Even recent models of trust in AI-assisted learning (Wang et al., 2025) stop at the individual learner level without addressing how systems should be designed to calibrate trust.

This paper addresses this gap through three contributions. First, we map the literature landscape of trust in educational AI through a critical review, identifying how trust is conceptualized, measured, and theoretically framed. Second, we diagnose the *calibration gap* --- the absence of systematic attention to trust-capability alignment and the disconnect between learner-level dynamics and system-level design. Third, we propose a Two-Level Trust Calibration Framework that bridges this gap through an adaptive calibration cycle grounded in scaffolding theory.

Four research questions guide this inquiry:

- **RQ1:** How is trust in AI conceptualized and measured in educational AI research?
- **RQ2:** What theoretical frameworks guide trust research in educational AI contexts?
- **RQ3:** To what extent does existing research address trust calibration and human oversight design?
- **RQ4:** What does a two-level framework connecting learner trust dynamics to system-mediated trust calibration look like?


---

## 2. Conceptual Foundation

This section establishes the theoretical groundwork for the Two-Level Trust Calibration Framework. We trace the origins of trust research in automation, translate these constructs to educational contexts, introduce the critical distinction between self-regulated learning (SRL) calibration and trust calibration, examine the S-O-R model of Wang et al. (2025) as the most proximate theoretical antecedent, and preview the two-level framework that addresses its limitations.

### 2.1 Trust in Automation and Its Educational Translation

Lee and See (2004) defined trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 54). Both conditions are acutely present in educational settings: *uncertainty* about whether AI outputs are correct and pedagogically appropriate, and *vulnerability* because the learner's cognitive development is at stake. Lee and See further proposed that trust is shaped by three bases --- *performance* (system competence), *process* (transparency and predictability), and *purpose* (alignment with the user's goals) --- each mapping onto distinct concerns in educational AI.

Hoff and Bashir (2015) extended this foundation with a three-layer model distinguishing *dispositional trust* (stable personality-level tendencies shaped by age, culture, and experience), *situational trust* (context-dependent, influenced by task environment and perceived risk), and *learned trust* (accumulated through direct experience with a specific system). This temporal layering is particularly important in education, where trust evolves across an entire semester rather than during a single encounter.

Mayer et al. (1995) proposed the Ability-Benevolence-Integrity (ABI) model, increasingly applied to human-technology interaction (Lankton et al., 2015). In educational AI, *ability* maps to domain-specific accuracy, *benevolence* to the perception that the AI supports learning rather than replacing learner effort, and *integrity* to consistency and adherence to educational norms. De Visser et al. (2020) further contributed the concept of trust repair through calibration cues --- system-initiated reliability signals that can restore appropriate trust levels after violations.

Translating these frameworks to education demands attention to what makes educational AI distinctive. Unlike industrial automation, where the user's goal is task completion, educational AI operates in a domain where the "user" is simultaneously a *learner*. This creates a paradox: the most helpful AI response (providing the correct answer) may be the most pedagogically harmful one (depriving the learner of productive struggle). Trust calibration in educational AI must therefore account not only for accuracy-based trust but also for whether learners understand the pedagogical implications of their reliance patterns.

### 2.2 The Calibration Core: Two Types of Calibration

At the heart of this paper lies the concept of *calibration* --- the correspondence between judgment and reality. Lee and See (2004) defined trust calibration as the degree of agreement between a person's trust in a system and the system's actual capabilities. This concept provides a precise lens for diagnosing two modes of trust failure.

*Overtrust* occurs when a learner's trust exceeds the system's actual reliability, resulting in uncritical acceptance. Bastani et al. (2025) demonstrated this empirically: students with unrestricted ChatGPT access exhibited *automation complacency* (Parasuraman & Manzey, 2010), engaging in *cognitive offloading* (Risko & Gilbert, 2016) where learners delegate not just task execution but the cognitive effort that produces learning. This is particularly insidious with large language models, whose fluent outputs mask variable reliability across domains (Ji et al., 2023).

*Undertrust* occurs when trust falls below the system's actual capability, causing learners to reject beneficial AI assistance and forgo scaffolded learning opportunities. Undertrust may arise from prior negative experiences, low technology self-efficacy, or broader AI skepticism (Hoff & Bashir, 2015; Parasuraman & Riley, 1997).

**The critical distinction: SRL calibration versus trust calibration.** Existing educational research addresses calibration extensively --- but almost exclusively in the context of self-regulated learning. SRL calibration (Winne & Hadwin, 1998; Azevedo, 2005; Greene & Azevedo, 2007; Panadero, 2017) refers to the accuracy of learners' judgments about *their own* knowledge and performance. A well-calibrated learner accurately assesses what they know and do not know, enabling adaptive study strategies. Decades of research have established SRL calibration as a powerful predictor of academic achievement (Dunlosky & Rawson, 2012), with metacognitive monitoring as the operative mechanism (Nelson & Narens, 1990).

Trust calibration differs fundamentally from SRL calibration in its *locus of uncertainty*. Where SRL calibration asks, "How accurately do I judge my own capabilities?", trust calibration asks, "How accurately do I judge the AI system's capabilities?" This shift from *self* to *external system* has profound implications. SRL calibration improves through metacognitive training that enhances self-monitoring (Schraw, 1998). Trust calibration requires knowledge of the AI system's reliability profile --- its strengths, limitations, and failure modes --- a form of *AI literacy* (Long & Magerko, 2020) that goes beyond general self-regulation.

The distinction is not merely semantic. Consider a student who accurately recognizes that she struggles with integral calculus (high SRL calibration). When she turns to ChatGPT, however, she may grossly overestimate the AI's mathematical reasoning accuracy, accepting a subtly incorrect solution without verification (low trust calibration). Her SRL calibration does not protect her from trust miscalibration because the two involve different objects of judgment and different informational requirements. Existing SRL frameworks (Zimmerman, 2000; Winne & Hadwin, 1998; Panadero, 2017) address the first type; the second --- trust calibration in AI-mediated learning --- remains largely unaddressed. Emerging work in adjacent fields supports this argument. Lee et al. (2025) identified metacognitive sensitivity as a key mechanism for calibrating trust with AI, establishing a direct conceptual bridge between metacognition research and trust calibration. Steyvers and Peters (2025) examined how metacognition and uncertainty communication interact between humans and large language models, further underscoring the need for calibration-specific frameworks. This paper argues that trust calibration constitutes a distinct regulatory challenge demanding its own theoretical attention and design solutions.

### 2.3 The S-O-R Model and Its Limitations

Wang et al. (2025) proposed a Stimulus-Organism-Response (S-O-R) model for learner interaction with AI-assisted learning environments. The *Stimulus* component captures AI characteristics that initiate trust formation (perceived intelligence, anthropomorphism, output quality); the *Organism* models internal psychological processes of trust formation (cognitive appraisal, affective response, existing mental models); and the *Response* captures behavioral and learning consequences. Critically, Wang et al. distinguish between trust as a psychological state and reliance as a behavioral outcome.

However, this model has three limitations that motivate the present framework. First, the S-O-R structure carries a *behaviorist lineage* (Woodworth, 1929) that does not naturally accommodate the recursive, constructivist nature of learning (Piaget, 1971; Vygotsky, 1978). Second, the model's trust constructs would benefit from integration with Mayer et al.'s (1995) ABI dimensions and Hoff and Bashir's (2015) three-layer model for more granular trust antecedents. Third, and most consequentially, the S-O-R model *stops at the individual learner level*. It models how trust forms but does not address how educational systems can be designed to *actively calibrate* that trust --- the gap between describing a problem and prescribing a solution. Knowing that overtrust harms learning (Bastani et al., 2025) is necessary but insufficient; what is needed is a framework specifying how AI systems can detect trust miscalibration and intervene to correct it.

### 2.4 Toward a Two-Level Framework

Existing theoretical approaches each leave a critical piece unaddressed. Technology acceptance models (Davis, 1989; Venkatesh et al., 2003) address adoption but not ongoing trust calibration. SRL frameworks address self-calibration but not trust calibration with respect to external AI. The S-O-R model addresses learner-level trust dynamics but not system-level design responses. What is missing is a framework connecting the learner-level question --- "How does trust form and miscalibrate?" --- to the design-level question --- "How can educational AI systems be built to calibrate trust?"

This paper proposes a Two-Level Trust Calibration Framework. **Level 1 (Micro): Learner Trust Dynamics** models the cognitive and affective processes through which learners form, maintain, and adjust trust in AI, drawing on Lee and See (2004), Hoff and Bashir (2015), and Mayer et al. (1995), while modeling the interaction between trust calibration and SRL calibration. **Level 2 (Macro): System-Mediated Trust Calibration** specifies how educational AI systems can detect and correct trust miscalibration through *Trust Calibration Scaffolds* --- adaptive, system-level interventions that guide learners toward appropriate trust levels. Connecting the two levels is the **Adaptive Calibration Cycle**, a four-stage process aligned with SRL theory that continuously monitors learner behavior, evaluates trust states, and adjusts scaffold intensity.

The connective tissue is *scaffolding theory* (Wood, Bruner, & Ross, 1976). Three properties are particularly relevant: *contingency* (support calibrated to the learner's current state; van de Pol et al., 2010), *fading* (gradual withdrawal as competence increases), and *transfer of responsibility* (shifting regulatory control to the learner's metacognitive resources). Hattie's (2009) synthesis reported an effect size of *d* = 0.82 for scaffolding, and Hannafin et al. (1999) provided a taxonomy of scaffold types that informs the Trust Calibration Scaffolds developed in Section 5. Applied to trust calibration, scaffolding theory suggests that educational AI systems should provide contingent support for accurate trust judgments, fade that support as calibration improves, and ultimately transfer calibration responsibility to the learner --- a novel extension from cognitive task performance to trust regulation.


---

## 3. Review Approach

This paper adopts a critical review approach (Grant & Booth, 2009) combined with conceptual framework development. Unlike systematic or scoping reviews that aim for exhaustive coverage, a critical review prioritizes theoretical synthesis, critical appraisal, and gap identification to motivate new theoretical contributions (Pare et al., 2015). This methodological choice reflects the paper's primary contribution: the Two-Level Trust Calibration Framework requires integrative theoretical reasoning rather than exhaustive enumeration, consistent with recognized review typologies (Peters et al., 2020).

### Search Strategy and Selection

We searched Web of Science and Scopus (2015--2026) combining trust-related terms ("trust" OR "trust calibration" OR "overtrust" OR "reliance" OR "overreliance") with educational AI terms ("educational AI" OR "AI-assisted learning" OR "generative AI" OR "intelligent tutoring" OR "AI in education"). This temporal scope captures the maturation of intelligent tutoring systems and the transformative period following public LLM releases. Database searches were supplemented with backward and forward citation tracking from seminal works (Lee & See, 2004; Mayer et al., 1995; Hoff & Bashir, 2015; Wang et al., 2025; Bastani et al., 2025). Papers were selected based on relevance to trust dynamics in educational AI, prioritizing: (a) empirical studies measuring trust or calibration; (b) theoretical frameworks addressing trust in learning environments; and (c) studies from adjacent fields with clear educational applicability. Through this process, 128 papers were identified for full-text analysis, of which 73 were coded using a 32-field coding scheme with AI-assisted extraction (RAG pipeline) supplemented by manual verification of key papers.

### Analysis Approach

Selected works were analyzed thematically across four dimensions corresponding to the research questions: trust conceptualization, theoretical frameworks, measurement approaches, and calibration/oversight mechanisms. The fourth dimension served as the basis for gap analysis examining whether existing scholarship connects learner-level trust dynamics to system-level oversight design.

### Limitations

This is not a full systematic review, and the search strategy does not claim exhaustive coverage. The literature search was limited to English-language publications. Coding was conducted with AI assistance by a single researcher, introducing potential classification bias. These limitations are discussed further in Section 7.1.


---

## 4. Literature Landscape

The preceding sections established the methodological basis and theoretical foundations of this review. This section presents the findings from the systematic coding of 73 papers drawn from the broader 128-paper corpus, organized around four dimensions: how trust is conceptualized, which theoretical frameworks predominate, how trust is measured, and where a critical gap emerges at the intersection of trust calibration and oversight design. Together, these dimensions reveal a field that has made substantial progress in documenting learner trust but has yet to address the more consequential question of how to calibrate it.

### 4.1 Trust Conceptualizations in Educational AI Research

Trust in educational AI research is not a unified construct. Across the 73 coded papers, at least three distinct conceptualizations coexist, often without explicit acknowledgment of their differences. The first treats trust as an *attitude* toward the technology, following Lee and See's (2004) characterization of trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 54). The second treats trust as a *belief* about the trustee's characteristics, drawing on Mayer et al.'s (1995) widely cited model in which trust is a function of perceived ability, benevolence, and integrity. The third treats trust as a *behavioral intention*, operationalizing it through technology acceptance constructs such as willingness to use, perceived usefulness, and intention to adopt (Davis, 1989; Venkatesh et al., 2003).

The vast majority of the reviewed corpus --- 67 of 73 papers (91.8%) --- conceptualized trust as *trust in AI* as a general construct, while only 3 papers (4.1%) employed the more specialized trust-in-automation framing drawn from human factors research, 2 papers (2.7%) adopted an interpersonal trust lens, and 1 paper (1.4%) addressed institutional trust. This near-universal framing of trust as a monolithic orientation toward AI is consequential: it collapses theoretically distinct constructs --- dispositional tendencies, context-specific judgments, and accumulated experiential assessments --- into a single undifferentiated variable, obscuring the kind of fine-grained analysis required for calibration research.

Equally striking is the absence of definitional precision. Of the 73 papers, 63 (86.3%) provided no explicit definition of trust, 6 papers (8.2%) employed implicit definitions discernible from context, and only 4 papers (5.5%) offered an explicit operational definition. This pattern suggests that much of the field treats trust as a self-evident concept requiring no specification --- an assumption that is untenable given the construct's documented multidimensionality in both the organizational trust literature (Mayer et al., 1995) and the human factors tradition (Lee & See, 2004; Hoff & Bashir, 2015).

Notably absent from the reviewed corpus is the calibration-oriented conceptualization that has gained traction in human factors and automation research. In that tradition, the central concern is not whether operators trust automation, but whether their trust *accurately tracks* the system's actual reliability across different contexts and conditions (Lee & See, 2004; Parasuraman & Riley, 1997). Only 4 papers (5.5%) drew on Lee and See's trust-in-automation framework, and only 2 (2.7%) employed Hoff and Bashir's (2015) three-layer model of trust dynamics. This distinction between trust level and trust accuracy is foundational to the framework proposed in Section 5, yet it remains marginal in educational AI scholarship --- appearing in fewer than one in ten papers in the reviewed corpus.

### 4.2 Theoretical Frameworks in the Field

The theoretical landscape revealed by the coding is characterized less by the dominance of any single framework than by the prevalence of atheoretical research. More than half of the coded papers --- 39 of 73 (53.4%) --- employed no identifiable theoretical framework, proceeding directly from research questions to empirical investigation or narrative analysis without anchoring their inquiry in an established theoretical tradition. This finding reframes the conventional narrative about technology acceptance models dominating the field: while TAM and UTAUT variants are indeed the most commonly named framework family, appearing in 17 papers (23.3%) either individually or in combination, they characterize fewer than one in four studies, and they are outnumbered by more than two to one by studies operating without any framework at all.

Among the 34 papers (46.6%) that did employ a theoretical framework, several identifiable clusters emerge. The TAM/UTAUT family constitutes the largest named cluster (17 papers, 23.3% of the total corpus). These frameworks treat trust as one among several predictors of technology adoption, positioning it alongside perceived ease of use, social influence, and facilitating conditions. While these models have generated substantial empirical work on the determinants of AI adoption in educational settings, they are structurally limited in their capacity to address trust dynamics: they model adoption as an outcome rather than as an ongoing process, and they do not account for the possibility that adoption itself may be harmful when trust is miscalibrated.

AI in education (AIED) frameworks appeared in 8 papers (11.0%), addressing domain-specific considerations such as intelligent tutoring system design and adaptive learning architectures. Diffusion of Innovation (DOI) theory appeared in 5 papers (6.8%), and Self-Determination Theory (SDT) in 3 papers (4.1%). Self-regulated learning (SRL) frameworks, which are arguably the most pedagogically relevant to trust calibration given their emphasis on metacognitive monitoring and self-evaluation, appeared in only 2 papers (2.7%).

A third, theoretically consequential cluster applies trust-in-automation theory from human factors research to educational AI. Lee and See's (2004) framework appeared in 4 papers (5.5%), while Hoff and Bashir's (2015) three-layer model appeared in 2 papers (2.7%). Hoff and Bashir's model is particularly relevant because it distinguishes among dispositional trust (stable individual tendencies), situational trust (context-dependent responses), and learned trust (accumulated through experience) --- a dynamic, multi-layered architecture that TAM-based models largely overlook. Yet with only 6 papers across the two trust-in-automation frameworks, this tradition's penetration into educational AI research remains markedly limited.

The depth of framework engagement further qualifies these figures. Among the 34 papers employing a framework, 15 (20.5% of the total) engaged at a superficial level --- citing a framework without systematically applying it to study design or analysis --- while 17 (23.3%) applied a framework to structure their investigation, and only 2 papers (2.7%) engaged at a foundational level, contributing to framework development or theoretical extension. The predominance of superficial and applied engagement suggests that even where frameworks are present, they often serve a legitimating function rather than a generative one, providing post hoc framing for empirical findings rather than driving the formulation of research questions and study designs.

A critical observation across these clusters is that most frameworks in current use were developed *for* general technology acceptance or organizational behavior and subsequently adapted *to* educational AI contexts, rather than being developed specifically for the unique conditions of AI-mediated learning, where the user's cognitive development is itself at stake. This distinction matters: in most technology acceptance scenarios, the user's primary goal is task completion; in educational AI use, the user's primary goal is learning, which may require precisely the kind of effortful processing that efficient AI use can eliminate.

### 4.3 Trust Measurement Approaches

The measurement landscape in the reviewed corpus exhibits a pronounced methodological gap. Of the 73 coded papers, only 6 (8.2%) measured trust empirically in any form. The remaining 67 papers (91.8%) discussed trust conceptually, identified it as a relevant variable, or examined its correlates without directly measuring it. This asymmetry between the volume of trust-related scholarship and the frequency of trust measurement is itself a significant finding: the field is producing far more discussion of trust than empirical data about it.

Among the 6 papers that did measure trust, all employed mixed approaches combining self-report instruments with behavioral proxies. The prevailing measurement strategy relies on Likert-type trust questionnaires, typically administered as pre-post or cross-sectional surveys. These instruments capture learners' stated trust attitudes at discrete time points and have the advantage of psychometric familiarity and ease of administration. However, they are susceptible to well-documented limitations including social desirability bias, retrospective rationalization, and insensitivity to the dynamic, context-dependent fluctuations in trust that characterize real-time AI interaction (Schraw & Dennison, 1994; Dunlosky & Rawson, 2012).

Behavioral measures of trust, though more ecologically valid, remain rare even within the small subset of papers that measured trust at all. Where they exist, they typically examine AI output acceptance rates (whether learners adopt AI-generated suggestions), usage frequency, or task delegation patterns. These measures offer more direct evidence of trust-in-action than self-reports but are rarely analyzed in relation to AI reliability, making it difficult to distinguish calibrated trust from uncritical reliance.

Process-level measures represent the most significant absence. Indicators such as time spent verifying AI outputs, patterns of modification and revision following AI suggestions, information-seeking behaviors triggered by AI recommendations, and the sequence and depth of learner engagement with AI-generated content are entirely absent from the reviewed corpus. Not a single paper in the 73-paper coded set employed process-level trust indicators. This absence is consequential because process measures are precisely what would be needed to assess trust calibration in real time --- a requirement for the adaptive framework proposed in Section 5.

Most critically, calibration-specific measurement --- defined as the systematic assessment of alignment between a learner's perceived AI capability and the AI system's actual capability in a given domain --- is nonexistent in the reviewed corpus. Zero of the 73 coded papers measured calibration accuracy. The field measures how much learners trust AI; it does not measure how *accurately* they trust it. This distinction is not merely semantic. A learner who reports high trust in an AI system that is, in fact, highly reliable for the given task is well-calibrated. A learner who reports equally high trust in a system that is unreliable for the given task is dangerously miscalibrated. Current measurement approaches cannot distinguish between these two states because they assess trust level without reference to the reliability baseline against which trust should be evaluated.

### 4.4 The Calibration Gap

The preceding subsections converge on a finding that constitutes the central empirical justification for the framework proposed in Section 5: despite growing research on trust in educational AI, a critical gap persists at the intersection of trust calibration and oversight design.

The coding data reveal this gap with precision. Only 3 of 73 papers (4.1%) explicitly addressed calibration as a construct, while 38 (52.1%) addressed it partially --- typically by acknowledging the possibility of miscalibrated trust without systematically analyzing it --- and 32 (43.8%) did not address calibration at all. Overtrust was discussed in 24 papers (32.9%) and undertrust in 23 papers (31.5%), indicating that approximately one-third of the corpus recognizes miscalibrated trust as a concern, yet this recognition rarely translates into calibration-specific measurement or intervention design. The complete absence of calibration accuracy measurement across all 73 papers confirms that the field acknowledges the problem of miscalibrated trust in principle while lacking the tools to assess it in practice.

This gap manifests along two dimensions. First, studies that examine trust in educational AI rarely address how to intervene when trust is miscalibrated. The dominant research paradigm identifies antecedents (what predicts higher or lower trust), correlates (what trust is associated with), and outcomes (what trust levels lead to), but stops short of proposing mechanisms for *correcting* trust when it diverges from the warranted level. Trust is treated as a variable to be predicted, not a state to be managed.

Second, studies that examine AI scaffolding, oversight mechanisms, and pedagogical design in AI-mediated learning environments often fail to incorporate trust as a mediating or moderating variable. While 46 papers (63.0%) proposed some form of scaffold --- with transparency mechanisms appearing most frequently (16 papers), followed by multiple scaffold types (18 papers), and other approaches (9 papers) --- and 34 papers (46.6%) discussed oversight design, the integration between scaffold proposals and trust calibration remains superficial. Of the papers proposing scaffolds, the most common type was transparency-oriented (21.9% of the total corpus), while metacognitive scaffolds --- arguably the most directly relevant to trust calibration --- appeared in only 2 papers (2.7%). Oversight design, where discussed, was primarily descriptive rather than prescriptive: 34 papers (46.6%) discussed oversight considerations, but only at a general level without specifying how oversight mechanisms should respond dynamically to learner trust states.

The disconnect between these two bodies of work can be stated concisely: trust researchers study what learners feel and believe about AI; design researchers study what AI systems should do for learners; almost no one systematically connects the two by asking how system design should respond to learner trust states and, reciprocally, how system design shapes those trust states over time. Only 2 papers in the entire coded corpus explicitly addressed both trust calibration (not merely trust level) and oversight design (not merely system features) within an integrated framework --- representing just 2.7% of the reviewed literature.

The empirical work of Bastani et al. (2025) exemplifies both the urgency of this gap and the cost of leaving it unaddressed. Their randomized controlled trial documented substantial learning deterioration among students who used AI tutoring, a finding attributable to overtrust and cognitive offloading. Crucially, however, their study documented the *harm* of miscalibrated trust without proposing *calibration mechanisms* to prevent or remediate it. The study demonstrates what happens when learners overtrust AI in educational settings; it does not address what systems or pedagogies could have detected and corrected the miscalibration before harm occurred.

This absence is all the more striking given that adjacent fields have developed viable calibration measurement approaches. In human factors research, Okamura and Yamada (2020) used behavioral dependence switching as a calibration proxy in human-AI collaboration tasks. In HCI, Yin et al. (2019) experimentally examined the trust-accuracy alignment, and Li et al. (2024) directly manipulated AI confidence calibration levels to assess their effects on user trust. Kimani et al. (2024) demonstrated that self-confidence calibration prompts can improve reliance behavior in AI-assisted decision making, while Hasan et al. (2024) validated trust calibration interventions in clinical diagnostic systems. Mehrotra and Tielman (2023) surveyed the state of trust calibration measurement methods, and Mehrotra et al. (2024) systematically identified the measurement gap in fostering appropriate trust. These studies demonstrate that methods for measuring and intervening on trust calibration exist and have been productively applied --- they have simply not been adopted in educational AI research. The gap documented in the present review is therefore not one of methodological impossibility but of disciplinary disconnection.

This pattern --- rigorous identification of trust-related problems without corresponding development of trust calibration solutions --- characterizes the current state of the educational AI field as revealed by the coded corpus. It creates a clear theoretical and practical need for frameworks that bridge learner-level trust dynamics with system-level design decisions, connecting the micro-processes of trust formation with the macro-structures of oversight and scaffolding. The Two-Level Trust Calibration Framework proposed in the following section is designed to address precisely this integration gap.


---

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


---

## 6. Implications

The Two-Level Trust Calibration Framework carries implications for three primary audiences: AI system designers, educators, and researchers. This section derives specific, actionable principles from the framework's architecture and its grounding in educational theory.

### 6.1 Implications for AI System Designers

The framework yields five design principles for educational AI development.

**Principle 1: Design for Calibration, Not Just Trust.** The dominant design logic treats higher trust as a success metric. The framework reframes trust as a calibration target: AI systems should aim not to increase trust but to align it with actual capability for specific tasks. Under conditions of low AI reliability, the design goal should be to *reduce* trust to a level commensurate with capability, drawing on the Trust-AI Reliability Matrix (Figure 3).

**Principle 2: Embed Metacognitive Scaffolds by Default.** Every AI-assisted learning interaction should include prompts activating learner reflection on reliance decisions. The evidence base is substantial: Guo et al. (2022) reported a medium effect size (*g* = 0.50) for SRL outcomes in technology-enhanced environments. Prompts such as "How confident are you in the AI's suggestion, and why?" should be architectural features, not optional additions.

**Principle 3: Implement Transparency as Standard Practice.** Educational AI systems should display confidence levels, known limitations, and uncertainty indicators as standard interface elements. Learners cannot calibrate trust without reliability information (Lee & See, 2004; Arrieta et al., 2020). Transparency should be calibrated to learner expertise: simplified indicators for novices, more granular uncertainty information for advanced learners.

**Principle 4: Design Adaptive Oversight.** Scaffold intensity should adapt to the learner's current trust calibration state through the Adaptive Calibration Cycle: monitor behavioral signals, evaluate calibration state, adapt accordingly. Following scaffolding theory (Wood et al., 1976), systems should initialize with maximum scaffolding and fade as calibrated trust accumulates.

**Principle 5: Plan for Progressive Autonomy Release.** Educational AI systems should include explicit fading mechanisms that progressively transfer calibration responsibility to the learner (Wood et al., 1976; Hattie, 2009). This requires assessment points where the system evaluates whether learners can maintain calibrated trust without prompting, and graceful transitions from scaffolded to autonomous AI use.

### 6.2 Implications for Educators

The framework positions educators as active agents in the trust calibration process. Trust calibration should be recognized as a distinct learning objective alongside content mastery --- the capacity to assess AI reliability for a given task and adjust reliance accordingly is an epistemic competence requiring explicit instruction (Long & Magerko, 2020; Ng et al., 2021). Educators serve as trust calibration agents who can use the Trust-AI Reliability Matrix (Figure 3) to diagnose whether learners operate in calibrated or miscalibrated states and deploy targeted interventions: AI evaluation exercises for overtrusting learners, guided comparison tasks for undertrusting ones. Critically, AI literacy should be treated as a prerequisite for calibrated trust, integrated before or alongside AI tool deployment, including instruction on the probabilistic nature of LLM outputs and their domain-dependent accuracy variability.

### 6.3 Implications for Researchers

The framework generates five priority research questions:

1. **Measurement Development.** How can trust calibration accuracy be reliably measured? The field lacks validated instruments capturing alignment between learner trust and AI capability. Moving beyond self-report scales requires multimethod approaches integrating behavioral indicators (verification frequency, AI override rates), process measures (time allocation, information-seeking sequences), and self-report judgments anchored to AI reliability benchmarks.

2. **Scaffold Effectiveness.** Which trust calibration scaffolds are most effective for which types of miscalibration, learner populations, and contexts? Experimental studies comparing scaffold types across quadrants of the Trust-AI Reliability Matrix would move the field from principled recommendation to evidence-based prescription.

3. **Developmental Trajectory.** How does trust calibration develop over time? Longitudinal designs are needed to map trajectories from initial AI interaction to calibrated trust, identifying critical transition points and factors that accelerate or impede calibration development.

4. **Cultural Variation.** How do cultural factors moderate trust calibration processes? Cross-cultural research (Li et al., 2008; Hofstede, 2001) suggests calibration dynamics may operate differently across contexts with varying power distance and uncertainty avoidance, requiring culturally sensitive scaffold adaptations.

5. **Framework Validation.** Does the Two-Level Framework accurately predict calibration outcomes? Design-based research (Anderson & Shattuck, 2012; McKenney & Reeves, 2019) can iteratively refine the framework, while randomized controlled trials can test specific causal claims, such as whether adaptive fading produces superior calibration outcomes compared to static scaffolding.


---

## 7. Conclusion

### 7.1 Limitations

Several limitations warrant acknowledgment. First, this paper adopted a critical review approach (Grant & Booth, 2009) rather than a full systematic review following PRISMA-ScR protocols (Peters et al., 2020). This enabled deeper theoretical synthesis but means the literature search, while systematic in its use of defined databases and search terms, was not exhaustive. Second, literature selection and analysis were conducted by a single researcher with AI-assisted coding through a retrieval-augmented generation (RAG) pipeline, introducing potential selection and interpretation bias; the final review covers 73 of 128 initially identified papers. Future work should involve multiple independent reviewers to establish intercoder reliability. Third, the search was limited to English-language publications, potentially excluding relevant work from non-Anglophone research traditions where cultural dimensions such as power distance may shape trust dynamics differently (Hofstede, 2001; Li et al., 2008). Fourth, the Two-Level Trust Calibration Framework is a conceptual contribution requiring empirical validation. While the evidence mapping (Table 2) draws on established findings from adjacent fields --- metacognitive prompting (Guo et al., 2022), desirable difficulties (Bjork & Bjork, 2011), productive failure (Kapur, 2008, 2016), scaffolding (Hattie, 2009) --- direct evidence for trust calibration scaffolds operating as theorized in educational AI contexts remains sparse. Fifth, the framework assumes relatively stable AI capability within defined contexts, yet generative AI systems exhibit variable performance across tasks and queries, meaning the Trust-AI Reliability Matrix requires dynamic rather than static reliability assessment --- a challenge the current framework acknowledges but does not fully resolve.

### 7.2 Conclusion

This paper has advanced a core argument: trust calibration --- the alignment between learner trust in AI and the system's actual capability for a given task --- represents the missing link in educational AI design. Through a critical review of the literature on trust in educational AI (2015--2026), we identified a structural gap at the intersection of trust research in human factors, which has long recognized calibration as central (Lee & See, 2004; Parasuraman & Riley, 1997), and scaffolding research in educational technology, which has developed sophisticated adaptive support approaches (Wood et al., 1976; Belland, 2014) but has not applied them to trust.

The paper makes three contributions. First, it documents the calibration gap --- the finding that existing research predominantly treats trust as a variable to be maximized rather than a calibration target aligned with system capability, a structural absence that will produce overtrust effects (Bastani et al., 2025) at increasing scale as AI adoption accelerates. Second, it proposes the Two-Level Trust Calibration Framework connecting learner-level trust dynamics (Level 1) with system-level calibration mechanisms (Level 2) through an Adaptive Calibration Cycle, specifying six trust calibration scaffolds each grounded in established theory and mapped to specific miscalibration states. Third, it introduces conceptual tools --- the SRL-trust calibration distinction, the Trust-AI Reliability Matrix, and five design principles --- providing shared vocabulary for a research community that has lacked the infrastructure to address trust calibration systematically.

The path forward is empirical. The conceptual architecture must be tested through design-based research (Anderson & Shattuck, 2012; McKenney & Reeves, 2019) implementing trust calibration scaffolds in authentic settings and measuring their effects on calibration accuracy and learning outcomes. As educational AI becomes increasingly autonomous, the question is no longer "Do learners trust AI?" but "Is their trust calibrated?" --- and "Who or what calibrates it?" The answer will determine whether AI integration produces learners who think critically with AI or defer uncritically to it.


---

## References

Al-Adwan, A. S., Li, N., Al-Adwan, A., Abbasi, G. A., Albelbisi, N. A., & Habibi, A. (2023). Extending the technology acceptance model (TAM) to predict university students' intentions to use metaverse-based learning platforms. *Education and Information Technologies*, *28*(9), 11823--11850. https://doi.org/10.1007/s10639-023-11816-3

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kiber, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, 1--13. https://doi.org/10.1145/3290605.3300233

Anderson, T., & Shattuck, J. (2012). Design-based research: A decade of progress in education research? *Educational Researcher*, *41*(1), 16--25. https://doi.org/10.3102/0013189X11428813

Arrieta, A. B., Diaz-Rodriguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion*, *58*, 82--115. https://doi.org/10.1016/j.inffus.2019.12.012

Azevedo, R., & Cromley, J. G. (2004). Does training on self-regulated learning facilitate students' learning with hypermedia? *Journal of Educational Psychology*, *96*(3), 523--535. https://doi.org/10.1037/0022-0663.96.3.523

Baidoo-Anu, D., & Ansah, L. O. (2023). Education in the era of generative artificial intelligence (AI): Understanding the potential benefits of ChatGPT in promoting teaching and learning. *Journal of AI*, *7*(1), 52--62. https://doi.org/10.61969/jai.1337500

Bandura, A. (1997). *Self-efficacy: The exercise of control*. W. H. Freeman.

Bannert, M., Reimann, P., & Sonnenberg, C. (2009). Process mining techniques for analysing patterns and strategies in students' self-regulated learning. *Metacognition and Learning*, *4*(2), 131--161. https://doi.org/10.1007/s11409-009-9040-2

Bannert, M., Sonnenberg, C., Mengelkamp, C., & Pieger, E. (2015). Short- and long-term effects of students' self-directed metacognitive prompts on mathematical problem-solving. *Computers in Human Behavior*, *52*, 293--306. https://doi.org/10.1016/j.chb.2015.05.038

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, O., & Mariman, R. (2025). Generative AI can harm learning. *Proceedings of the National Academy of Sciences*, *122*(2), e2412617122. https://doi.org/10.1073/pnas.2412617122

Belland, B. R. (2014). Scaffolding: Definition, current debates, and future directions. In J. M. Spector, M. D. Merrill, J. Elen, & M. J. Bishop (Eds.), *Handbook of research on educational communications and technology* (4th ed., pp. 505--518). Springer. https://doi.org/10.1007/978-1-4614-3185-5_39

Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher, R. W. Pew, L. M. Hough, & J. R. Pomerantz (Eds.), *Psychology and the real world: Essays illustrating fundamental contributions to society* (pp. 56--64). Worth Publishers.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, *5*(1), 7--74. https://doi.org/10.1080/0969595980050102

Chen, X., Zou, D., Xie, H., Cheng, G., & Liu, C. (2022). Two decades of artificial intelligence in education: Contributors, collaborations, research topics, challenges, and future directions. *Educational Technology & Society*, *25*(1), 28--47.

Cotton, D. R. E., Cotton, P. A., & Shipway, J. R. (2024). Chatting and cheating: Ensuring academic integrity in the era of ChatGPT. *Innovations in Education and Teaching International*, *61*(2), 228--239. https://doi.org/10.1080/14703297.2023.2190148

Darvishi, A., Khosravi, H., Sadiq, S., Gasevic, D., & Siemens, G. (2024). Impact of AI assistance on student agency. *Computers & Education*, *210*, 104967. https://doi.org/10.1016/j.compedu.2023.104967

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, *13*(3), 319--340. https://doi.org/10.2307/249008

de Visser, E. J., Peeters, M. M. M., Jung, M. F., Kohn, S., Shaw, T. H., Pak, R., & Neerincx, M. A. (2020). Towards a theory of longitudinal trust calibration in human--robot teams. *International Journal of Social Robotics*, *12*(2), 459--478. https://doi.org/10.1007/s12369-019-00596-x

Dunlosky, J., & Rawson, K. A. (2012). Overconfidence produces underachievement: Inaccurate self evaluations undermine students' learning and retention of material. *Learning and Instruction*, *22*(4), 271--280. https://doi.org/10.1016/j.learninstruc.2011.08.003

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The role of trust in automation reliance. *International Journal of Human-Computer Studies*, *58*(6), 697--718. https://doi.org/10.1016/S1071-5819(03)00038-7

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. *American Psychologist*, *34*(10), 906--911. https://doi.org/10.1037/0003-066X.34.10.906

Grant, M. J., & Booth, A. (2009). A typology of reviews: An analysis of 14 review types and associated methodologies. *Health Information & Libraries Journal*, *26*(2), 91--108. https://doi.org/10.1111/j.1471-1842.2009.00848.x

Gunning, D., Stefik, M., Choi, J., Miller, T., Stumpf, S., & Yang, G.-Z. (2019). XAI --- Explainable artificial intelligence. *Science Robotics*, *4*(37), eaay7120. https://doi.org/10.1126/scirobotics.aay7120

Guo, L., Wang, W., Liao, J., & Cheng, S. (2022). Effects of metacognitive prompts on self-regulated learning: A meta-analysis. *Frontiers in Psychology*, *13*, 1001498. https://doi.org/10.3389/fpsyg.2022.1001498

Hancock, P. A., Billings, D. R., Schaefer, K. E., Chen, J. Y. C., de Visser, E. J., & Parasuraman, R. (2011). A meta-analysis of factors affecting trust in human-robot interaction. *Human Factors*, *53*(5), 517--527. https://doi.org/10.1177/0018720811417254

Hannafin, M., Land, S., & Oliver, K. (1999). Open learning environments: Foundations, methods, and models. In C. M. Reigeluth (Ed.), *Instructional-design theories and models: A new paradigm of instructional theory* (Vol. 2, pp. 115--140). Lawrence Erlbaum.

Hattie, J. (2009). *Visible learning: A synthesis of over 800 meta-analyses relating to achievement*. Routledge.

Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors*, *57*(3), 407--434. https://doi.org/10.1177/0018720814547570

Hofstede, G. (2001). *Culture's consequences: Comparing values, behaviors, institutions, and organizations across nations* (2nd ed.). Sage.

Holmes, W., Bialik, M., & Fadel, C. (2019). *Artificial intelligence in education: Promises and implications for teaching and learning*. Center for Curriculum Redesign.

Jian, J.-Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics*, *4*(1), 53--71. https://doi.org/10.1207/S15327566IJCE0401_04

Kapur, M. (2008). Productive failure. *Cognition and Instruction*, *26*(3), 379--424. https://doi.org/10.1080/07370000802212669

Kapur, M. (2016). Examining productive failure, productive success, and constructive failure as a framework for reconceptualizing how failure can be productive. *Instructional Science*, *44*(4), 321--338. https://doi.org/10.1007/s11251-016-9379-0

Kasneci, E., Sessler, K., Kuchemann, S., Bannert, M., Dementieva, D., Fischer, F., Gasser, U., Groh, G., Gunnemann, S., Hullermeier, E., Kruber, S., Kuber, G., Sachs, S., Seidel, T., Stadler, M., Wachter, B., Weidlich, J., & Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences*, *103*, 102274. https://doi.org/10.1016/j.lindif.2023.102274

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, *46*(1), 50--80. https://doi.org/10.1518/hfes.46.1.50.30392

Li, X., Hess, T. J., & Valacich, J. S. (2008). Why do we trust new technology? A study of initial trust formation with organizational information systems. *The Journal of Strategic Information Systems*, *17*(1), 39--71. https://doi.org/10.1016/j.jsis.2008.01.001

Lo, C. K. (2023). What is the impact of ChatGPT on education? A rapid review of the literature. *Education Sciences*, *13*(4), 410. https://doi.org/10.3390/educsci13040410

Loibl, K., Roll, I., & Rummel, N. (2017). Towards a theory of when and how problem solving followed by instruction works: A meta-analysis. *Educational Psychology Review*, *29*(4), 693--715. https://doi.org/10.1007/s10648-016-9379-x

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, *151*, 90--103. https://doi.org/10.1016/j.obhdp.2018.12.005

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*, 1--16. https://doi.org/10.1145/3313831.3376727

Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review*, *20*(3), 709--734. https://doi.org/10.5465/amr.1995.9508080335

McKenney, S., & Reeves, T. C. (2019). *Conducting educational design research* (2nd ed.). Routledge. https://doi.org/10.4324/9781315105642

Mollick, E. R., & Mollick, L. (2023). Using AI to implement effective teaching strategies in classrooms: Five strategies, including prompts. *The Wharton School Research Paper*. https://doi.org/10.2139/ssrn.4391243

Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence*, *2*, 100041. https://doi.org/10.1016/j.caeai.2021.100041

Panadero, E. (2017). A review of self-regulated learning: Six models and four directions for research. *Frontiers in Psychology*, *8*, 422. https://doi.org/10.3389/fpsyg.2017.00422

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, *39*(2), 230--253. https://doi.org/10.1518/001872097778543886

Pea, R. D. (2004). The social and technological dimensions of scaffolding and related theoretical concepts for learning, education, and human activity. *The Journal of the Learning Sciences*, *13*(3), 423--451. https://doi.org/10.1207/s15327809jls1303_6

Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis*, *18*(10), 2119--2126. https://doi.org/10.11124/JBIES-20-00167

Pieschl, S. (2009). Metacognitive calibration --- an extended conceptualization and potential applications. *Metacognition and Learning*, *4*(1), 3--31. https://doi.org/10.1007/s11409-008-9030-4

Pintrich, P. R. (2000). The role of goal orientation in self-regulated learning. In M. Boekaerts, P. R. Pintrich, & M. Zeidner (Eds.), *Handbook of self-regulation* (pp. 451--502). Academic Press. https://doi.org/10.1016/B978-012109890-2/50043-3

Puntambekar, S., & Hubscher, R. (2005). Tools for scaffolding students in a complex learning environment: What have we gained and what have we missed? *Educational Psychologist*, *40*(1), 1--12. https://doi.org/10.1207/s15326985ep4001_1

Reiser, B. J. (2004). Scaffolding complex learning: The mechanisms of structuring and problematizing student work. *The Journal of the Learning Sciences*, *13*(3), 273--304. https://doi.org/10.1207/s15327809jls1303_2

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*, *55*(1), 68--78. https://doi.org/10.1037/0003-066X.55.1.68

Ryan, R. M., & Deci, E. L. (2017). *Self-determination theory: Basic psychological needs in motivation, development, and wellness*. Guilford Press. https://doi.org/10.1521/978.14625/28806

Schaefer, K. E., Chen, J. Y. C., Szalma, J. L., & Hancock, P. A. (2016). A meta-analysis of factors influencing the development of trust in automation: Implications for understanding autonomy in future systems. *Human Factors*, *58*(3), 377--400. https://doi.org/10.1177/0018720816634228

Schraw, G., & Dennison, R. S. (1994). Assessing metacognitive awareness. *Contemporary Educational Psychology*, *19*(4), 460--475. https://doi.org/10.1006/ceps.1994.1033

Shneiderman, B. (2020). Human-centered artificial intelligence: Reliable, safe & trustworthy. *International Journal of Human-Computer Interaction*, *36*(6), 495--504. https://doi.org/10.1080/10447318.2020.1741118

Strzelecki, A. (2023). To use or not to use ChatGPT in higher education? A study of students' acceptance and use of technology. *Interactive Learning Environments*, *32*(10), 5142--5155. https://doi.org/10.1080/10494820.2023.2209881

Sweller, J. (2011). Cognitive load theory. In J. Mestre & B. Ross (Eds.), *The psychology of learning and motivation* (Vol. 55, pp. 37--76). Academic Press. https://doi.org/10.1016/B978-0-12-387691-1.00002-8

UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO Publishing. https://doi.org/10.54675/EWZQ9535

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, *27*(3), 425--478. https://doi.org/10.2307/30036540

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes* (M. Cole, V. John-Steiner, S. Scribner, & E. Souberman, Eds.). Harvard University Press.

Wang, X., Li, L., Tan, S. C., Yang, L., & Lei, J. (2025). Trust in AI-powered educational agents: A stimulus-organism-response perspective. [Manuscript under review].

Wiliam, D. (2011). *Embedded formative assessment*. Solution Tree Press.

Williams, R. (2025). Navigating the AI-enhanced learning landscape: A framework for integrating generative AI as a cognitive and metacognitive tool. *Information*, *16*(1), 28. https://doi.org/10.3390/info16010028

Winne, P. H., & Hadwin, A. F. (1998). Studying as self-regulated learning. In D. J. Hacker, J. Dunlosky, & A. C. Graesner (Eds.), *Metacognition in educational theory and practice* (pp. 277--304). Lawrence Erlbaum.

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, *17*(2), 89--100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

Zawacki-Richter, O., Marin, V. I., Bond, M., & Gouverneur, F. (2019). Systematic review of research on artificial intelligence applications in higher education -- Where are the educators? *International Journal of Educational Technology in Higher Education*, *16*(1), 39. https://doi.org/10.1186/s41239-019-0171-0

Zimmerman, B. J. (2000). Attaining self-regulation: A social cognitive perspective. In M. Boekaerts, P. R. Pintrich, & M. Zeidner (Eds.), *Handbook of self-regulation* (pp. 13--39). Academic Press. https://doi.org/10.1016/B978-012109890-2/50031-7

Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice*, *41*(2), 64--70. https://doi.org/10.1207/s15430421tip4102_2

---

## Additional References (Priority A--D Papers)

Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science*, *25*(4), 471--533. https://doi.org/10.1207/s15516709cog2504_1

Hasan, R., Lennon, M., Cody, J., Krumholz, H. M., & Schulz, W. L. (2024). Facilitating trust calibration in AI-driven diagnostic systems through transparent communication of AI limitations. *Journal of Medical Internet Research*, *26*, e58666. https://doi.org/10.2196/58666

Kimani, E., Rowan, K., Feuerriegel, S., & Perer, A. (2024). Are you really sure? Understanding the effects of human self-confidence calibration prompts on trust, reliance, and task performance in AI-assisted decision making. *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, Article 671. https://doi.org/10.1145/3613904.3642671

Lee, J., Lee, S., & Steyvers, M. (2025). Metacognitive sensitivity: Key to calibrating trust with AI. *PNAS Nexus*, *4*(3), pgaf133. https://doi.org/10.1093/pnasnexus/pgaf133

Li, Y., Chen, M., & Liao, Q. V. (2024). Understanding the effects of miscalibrated AI confidence on user trust. *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.48550/arXiv.2402.07632

Mehrotra, S., & Tielman, M. L. (2023). Measuring and understanding trust calibrations for automated systems: A survey of the state-of-the-art and future directions. *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*, Article 197. https://doi.org/10.1145/3544548.3581197

Mehrotra, S., Jonker, C. M., & Tielman, M. L. (2024). A systematic review of the research on fostering appropriate trust in human-AI interaction. *ACM Computing Surveys*, *56*(12), 1--40. https://doi.org/10.1145/3696449

Nelson, T. O., & Narens, L. (1990). Metamemory: A theoretical framework and new findings. In G. H. Bower (Ed.), *The psychology of learning and motivation* (Vol. 26, pp. 125--173). Academic Press.

Okamura, K., & Yamada, S. (2020). Adaptive trust calibration for human-AI collaboration. *PLOS ONE*, *15*(2), e0229132. https://doi.org/10.1371/journal.pone.0229132

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, *52*(3), 381--410. https://doi.org/10.1177/0018720810376055

Pare, G., Trudel, M.-C., Jaana, M., & Kitsiou, S. (2015). Synthesizing information systems knowledge: A typology of literature reviews. *Information & Management*, *52*(2), 183--199. https://doi.org/10.1016/j.im.2014.08.008

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, *20*(9), 676--688. https://doi.org/10.1016/j.tics.2016.07.002

Scharowski, N., Perrig, S. A. L., von Felten, N., & Brühlmann, F. (2025). To trust or distrust trust measures: Validating questionnaires for trust in AI. *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT)*. https://doi.org/10.48550/arXiv.2403.00582

Steyvers, M., & Peters, M. A. K. (2025). Metacognition and uncertainty communication in humans and large language models. *Current Directions in Psychological Science*. https://doi.org/10.1177/09637214251391158

Tomsett, R., Preece, A., Braines, D., Cerutti, F., Chakraborty, S., Srivastava, M., Pearson, G., & Kaplan, L. (2020). Rapid trust calibration through interpretable and uncertainty-aware AI. *Patterns*, *1*(6), 100049. https://doi.org/10.1016/j.patter.2020.100049

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction*, *7*(CSCW1), 1--38. https://doi.org/10.1145/3579605

Yin, M., Wortman Vaughan, J., & Wallach, H. (2019). Understanding the effect of accuracy on trust in machine learning models. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, Article 279. https://doi.org/10.1145/3290605.3300509
