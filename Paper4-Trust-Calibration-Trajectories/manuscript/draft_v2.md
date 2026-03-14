# Behavioral Evidence for Trust Calibration Trajectory Theory: A Model-Based Clustering Analysis of AI Reliance Patterns in a Large-Scale Educational Platform

**Author:** Hosung You

College of Education, Pennsylvania State University

**Target Journal:** Computers in Human Behavior

**Date:** March 2026

**Status:** Draft v2

---

## Highlights

- Six distinct AI reliance calibration trajectories identified among 4,568 learners
- Under-reliance on AI, not over-reliance, was the dominant pattern across all classes
- AI Benefit Emergence: AI effectiveness rose while learner reliance stayed flat
- Early explanation-seeking predicted trajectory class at 3x chance accuracy
- Model-based clustering and LCGA converged on key findings via triangulation

## Abstract

This study examines how learners calibrate their reliance on AI recommendations over time using behavioral data from 4,568 students on the EdNet AI tutoring platform. Drawing on trust-in-automation theory, we operationalize reliance calibration as the evolving alignment between behavioral AI reliance ($R_b$) and task performance ($P$). Two complementary methods — model-based clustering (MBC) and latent class growth analysis (LCGA) — identified six and four trajectory classes, respectively, converging on two key findings: under-reliance dominated across all classes and time windows, and both convergent and stagnant calibration patterns were present. Both methods independently identified a novel trajectory termed AI Benefit Emergence (ABE), in which AI effectiveness increased while learner reliance remained flat. Multinomial logistic regression revealed that early explanation-seeking behavior was the strongest predictor of trajectory class membership, achieving 49.4% accuracy (approximately three times chance level). These findings provide the first large-scale behavioral evidence for trust calibration trajectory theory and challenge the prevailing assumption that over-reliance is the primary risk in educational AI contexts.

**Keywords:** reliance calibration, trust in AI, AI tutoring systems, model-based clustering, latent class growth analysis, learner trajectories, appropriate reliance, educational technology

---

## 1. Introduction

### 1.1 The Promise and Peril of AI in Education

Artificial intelligence has rapidly transformed the educational landscape, with AI-powered tutoring systems, adaptive learning platforms, and intelligent recommendation engines now serving millions of learners worldwide (Holmes et al., 2019; Zawacki-Richter et al., 2019). These systems promise personalized learning experiences by adapting content difficulty, pacing, and instructional strategies to individual learner characteristics (VanLehn, 2011). Yet the effectiveness of such systems depends not only on the quality of their recommendations but also on how learners interact with and respond to AI-generated guidance (Nazaretsky et al., 2022).

A fundamental challenge emerges at this intersection: learners must develop an appropriate level of reliance on AI recommendations — neither blindly following every suggestion nor categorically ignoring potentially beneficial guidance. This challenge parallels a well-documented problem in human factors research known as the calibration of trust in automation (Lee & See, 2004; Parasuraman & Riley, 1997). When human operators over-trust automated systems, they may fail to detect errors; when they under-trust, they forfeit the benefits of automation. The same dynamics apply in educational contexts, where miscalibrated reliance on AI tutoring can undermine learning outcomes (Kaur et al., 2020).

### 1.2 AI in Education: Between Panic and Promise

The release of ChatGPT in late November 2022 marked an inflection point in public discourse about artificial intelligence in education. Within weeks, institutions worldwide moved to restrict or ban the tool: Sciences Po in Paris prohibited its use in January 2023, several U.S. universities quickly followed, and by mid-2023 a UNESCO survey found that fewer than 10% of educational institutions had any formal guidance on generative AI in their classrooms (UNESCO, 2023). Institutional responses have since been inconsistent — cycling from prohibition to cautious integration, with some institutions now requiring syllabi statements on AI use (Kasneci et al., 2023; Mollick & Mollick, 2023). Throughout this oscillation, one concern has remained remarkably stable in public and policy rhetoric: the fear that students will over-rely on AI, outsource their thinking, and erode the critical reasoning skills that formal education is designed to cultivate (Baidoo-Anu & Ansah, 2023; Crompton & Burke, 2023). This narrative — the *over-reliance assumption* — has become the default framing for AI-in-education policy at every level, from K-12 district guidelines to national regulatory frameworks.

Yet the over-reliance assumption rests on surprisingly thin empirical ground, at least in the domain of AI-assisted learning. Research on intelligent tutoring systems has long documented that the more common student behavior is not the abuse of system-provided help but its avoidance: learners systematically under-utilize available hints and scaffolding, even when doing so would improve their performance (Aleven et al., 2016; Roll et al., 2011). This help-avoidance phenomenon is theoretically grounded in self-determination theory's emphasis on autonomy needs (Ryan & Deci, 2000) and in the face-threat model of help-seeking, both of which predict that learners will resist AI assistance to preserve a sense of independent competence. The human factors literature has established that under-reliance on automated decision support — failing to act on valid machine recommendations — is at least as prevalent as the automation complacency that dominates popular concern (Parasuraman & Manzey, 2010). The present study enters this gap between assumption and evidence. By examining behavioral traces of over 4,500 learners interacting with an AI recommendation system across thousands of learning episodes, we provide large-scale empirical evidence on whether the dominant pattern in human-AI educational interaction is in fact over-reliance, or whether a different and less discussed phenomenon — systematic under-reliance — better characterizes how learners calibrate their trust in AI over time.

### 1.3 Reliance Calibration as a Behavioral Construct

A critical distinction must be drawn between *trust* and *reliance*. Following Lee and See's (2004) seminal framework, trust is an attitude — a psychological state reflecting the willingness to be vulnerable to the actions of an automated agent based on the expectation that it will perform a particular action important to the trustor. Reliance, by contrast, is a behavior — the observable act of depending on the automated system's output in decision-making. Trust *guides* reliance, but the two are not isomorphic: a learner may trust an AI system yet choose not to rely on it for strategic reasons, or may rely on it out of convenience without genuine trust.

This distinction carries important methodological implications. Measuring trust requires access to cognitive and affective states, typically assessed through self-report instruments (e.g., Jian et al., 2000; Körber, 2019). Measuring reliance, however, requires only behavioral observation — the degree to which individuals accept, follow, or depend on system recommendations. In large-scale educational datasets where self-report data are unavailable, behavioral reliance becomes the accessible and appropriate construct.

We therefore adopt the term *reliance calibration* to describe the phenomenon under investigation: the degree to which a learner's behavioral reliance on AI recommendations aligns with their actual performance level over time. This framing is consistent with Schemmer et al.'s (2023) conceptualization of appropriate reliance as a behavioral outcome of trust calibration processes, and with de Visser et al.'s (2020) emphasis on the dynamic, evolving nature of human-automation trust relationships.

### 1.4 Conceptual Framework

This study is situated within a broader research program on trust calibration in AI-assisted learning. The conceptual foundation draws on two key frameworks.

First, the *Trust-Reliability Matrix* conceptualizes the alignment space between a learner's reliance on AI and the system's actual reliability. When reliance matches reliability, calibration is achieved. Deviations in either direction — over-reliance (reliance exceeds reliability) or under-reliance (reliance falls below reliability) — represent miscalibration. This matrix provides a static snapshot of calibration states.

Second, we extend this framework into a dynamic, longitudinal perspective by modeling reliance calibration as a trajectory through a three-dimensional space defined by behavioral reliance ($R_b$), performance ($P$), and time ($\tau$). Within this $R_b \times P \times \tau$ space, different trajectory shapes correspond to different calibration dynamics: convergent trajectories (where the gap between $R_b$ and $P$ narrows), divergent trajectories (where the gap widens), stagnant trajectories (where the gap remains constant), and catastrophic trajectories (where a sudden failure disrupts calibration). These theoretically predicted trajectory shapes serve as referents against which empirically observed patterns can be compared. The central question of this study is whether these theoretically predicted patterns are observable in behavioral data from a large-scale educational platform.

### 1.5 The Research Gap

Despite growing interest in trust and reliance on AI in educational settings (Nazaretsky et al., 2022; Siau & Wang, 2018), empirical research on how learners' reliance patterns evolve over time remains sparse. Most existing studies adopt cross-sectional designs, measuring trust or reliance at a single point (or at best, pre-post), and treat learner populations as homogeneous (Kaur et al., 2020). Three specific gaps motivate this study.

First, there is a lack of *longitudinal trajectory* studies examining how reliance calibration unfolds across extended learning episodes. Trust and reliance are inherently dynamic (Lee & See, 2004), yet the temporal evolution of these constructs in educational AI contexts has received limited empirical attention.

Second, there is a lack of *person-centered* approaches that acknowledge heterogeneity in calibration trajectories. Variable-centered methods (e.g., regression) estimate average effects but mask meaningful subgroup differences. Model-based clustering (MBC) and growth mixture modeling (GMM) approaches can uncover qualitatively distinct trajectory classes within seemingly homogeneous populations (Nagin, 2005; Ram & Grimm, 2009).

Third, there is a disconnect between theoretical predictions about calibration dynamics and empirical evidence. While frameworks predict various trajectory shapes (convergent, divergent, stagnant, catastrophic), no study has systematically tested whether these patterns emerge in real-world learner data.

### 1.6 Research Questions and Hypotheses

This study addresses five research questions:

**RQ1:** How many distinct reliance calibration trajectory classes can be identified among learners using an AI tutoring system, and what characterizes each class?

**RQ2:** Does latent class growth analysis of calibration gap trajectories replicate the trajectory typology identified by model-based clustering?

**RQ3:** To what extent do the empirically observed trajectory classes correspond to theoretically predicted calibration patterns (convergent, divergent, stagnant)?

**RQ4:** Can early learning behaviors predict subsequent trajectory class membership?

**RQ5:** Do trajectory classes differ in learning outcomes (overall accuracy and accuracy improvement)?

Based on the theoretical framework and prior literature, we advance the following hypotheses:

**H1:** At least three distinct reliance calibration trajectory classes will emerge, reflecting heterogeneity in how learners calibrate their AI reliance over time.

**H2a:** At least one class will exhibit a convergent calibration pattern, with the reliance-performance gap narrowing toward zero.

**H2b:** At least one class will exhibit a stagnant calibration pattern, with the gap remaining relatively constant.

**H3:** Early explanation-seeking behavior (a proxy for metacognitive engagement) will significantly predict trajectory class membership.

**H4:** Convergent calibration trajectories will be associated with the best learning outcomes, reflecting the theoretical advantage of calibrated reliance.

### 1.7 Contribution

This study makes four primary contributions. First, it provides the first large-scale, person-centered analysis of reliance calibration trajectories in AI-assisted learning, moving beyond cross-sectional and population-average approaches. Second, it offers behavioral evidence for theoretically predicted calibration dynamics, testing whether patterns derived from trust-in-automation theory are observable in large-scale educational behavioral data. Third, it employs methodological triangulation by applying two complementary approaches — model-based clustering (MBC) and latent class growth analysis (LCGA) — to the same phenomenon, strengthening conclusions through cross-method convergence. Fourth, it reports the inductive discovery of a fifth trajectory pattern, AI Benefit Emergence (ABE), in which the AI system's effectiveness improves but learner reliance lags behind — a pattern not predicted by the original theoretical framework. This paper constitutes the fourth study in a programmatic research effort on trust calibration in AI-assisted education, building on a systematic literature review (Paper 1), a psychometric instrument development study (Paper 2), and a conceptual framework paper (Paper 3). While Papers 1 through 3 established the theoretical and measurement foundations, this paper contributes empirical behavioral evidence, testing whether the patterns predicted by the conceptual framework are observable in large-scale learning data.

---

## 2. Literature Review

### 2.1 Trust in Automation: Foundational Theory

The study of trust in automated systems has a rich history in human factors and ergonomics research. Parasuraman and Riley (1997) established foundational distinctions between misuse (over-reliance on automation), disuse (under-utilization of automation), and abuse (inappropriate application of automation by designers). These concepts have proven remarkably durable, forming the basis for subsequent theorizing about human-automation interaction.

Lee and See (2004) provided the most comprehensive theoretical framework for understanding trust in automation, defining trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 54). Critically, their model distinguishes trust (an attitude) from reliance (a behavior), proposing that trust serves as a mediating variable that guides reliance decisions. This distinction implies that trust calibration — the alignment of trust with system trustworthiness — is a necessary but not sufficient condition for appropriate reliance; contextual factors, individual differences, and task characteristics also influence how trust translates into behavior.

Muir (1994) and Muir and Moray (1996) were among the first to examine the dynamics of trust over time, demonstrating that trust increases gradually with positive experience but can decrease precipitously following automation failures. This asymmetry between trust building and trust erosion has been replicated extensively (Dzindolet et al., 2003; Lee & Moray, 1994). More recently, de Visser et al. (2020) introduced the concept of trust repair — mechanisms by which human-automation trust can be restored following a violation — further underscoring the dynamic, evolving nature of trust processes.

### 2.2 Appropriate Reliance and the Calibration Problem

While trust theory provides the attitudinal foundation, the behavioral outcome of interest is *appropriate reliance* — the extent to which individuals rely on automated systems in a manner proportional to system reliability. Schemmer et al. (2023) conducted a comprehensive review of appropriate reliance on AI, identifying key antecedents including system transparency, task complexity, individual differences in propensity to trust, and experience with the system over time.

The calibration problem — maintaining alignment between trust/reliance and actual system capability — has been studied primarily in high-stakes domains such as aviation (Parasuraman & Manzey, 2010), healthcare (Choudhury et al., 2020), and military operations (Chen et al., 2014). In these domains, miscalibration can have life-or-death consequences. Education represents a different but no less important domain: while the stakes per decision are lower, the cumulative effect of systematic miscalibration over hundreds or thousands of learning interactions can substantially shape learning trajectories and skill development.

de Visser et al. (2020) highlighted the temporal dimension of calibration, noting that humans continuously update their mental models of automation reliability through experience. This updating process is not uniform across individuals — personal characteristics, prior experience, and the nature of feedback all influence calibration speed and accuracy. Yet research on individual differences in calibration trajectories remains limited, particularly in educational contexts.

### 2.3 Model-Based Clustering and Mixture Modeling in Educational Research

Model-based clustering (MBC; Fraley & Raftery, 2002; Scrucca et al., 2016) and the related growth mixture modeling (GMM; Muthén, 2004; Nagin, 2005) and latent class growth analysis (LCGA; Nagin & Land, 1993) approaches have become increasingly popular in educational research for identifying latent subgroups that follow qualitatively distinct developmental trajectories. Unlike traditional growth curve models that assume a single population trajectory with individual variation around the mean, these mixture approaches allow for the possibility of multiple latent classes, each with its own trajectory parameters.

Model-based clustering, as implemented in the mclust framework (Scrucca et al., 2016), identifies clusters by fitting finite mixtures of Gaussian distributions to multivariate data. This approach is particularly flexible because it does not require specifying a parametric growth function, instead operating on the full multivariate feature space. By contrast, LCGA (Proust-Lima et al., 2017) explicitly models growth curves within a latent class framework, estimating class-specific intercepts and slopes for a specified outcome variable over time. The two approaches offer complementary strengths: MBC captures complex multivariate patterns across multiple indicators simultaneously, while LCGA directly models temporal change and provides interpretable growth parameters.

In educational contexts, mixture modeling approaches have been applied to study diverse phenomena including reading development (Boscardin et al., 2008), mathematics learning trajectories (Musu-Gillette et al., 2015), and self-regulated learning processes (Broadbent & Poon, 2015). These studies consistently demonstrate that treating learner populations as homogeneous obscures meaningful subgroup differences that carry implications for intervention design.

Methodologically, mixture modeling in educational research faces several challenges including model selection (determining the optimal number of classes), class assignment uncertainty (entropy and posterior probability diagnostics), and the risk of extracting spurious classes driven by non-normality rather than genuine subgroups (Bauer & Curran, 2003). Best practices recommend combining statistical fit indices (BIC, AIC, entropy) with substantive interpretability and theoretical grounding when determining the number of classes (Nylund et al., 2007; Ram & Grimm, 2009). The use of multiple analytical approaches — such as combining MBC with LCGA — can further strengthen conclusions by demonstrating convergence (or informative divergence) across methods that make different distributional and structural assumptions.

### 2.4 AI Tutoring Systems and Learner Behavior Research

Intelligent tutoring systems (ITS) have a decades-long history of research demonstrating their effectiveness for personalized learning (VanLehn, 2011; du Boulay, 2016). More recent AI-powered tutoring platforms leverage knowledge tracing algorithms, collaborative filtering, and deep learning to adaptively recommend content to learners (Abdelrahman et al., 2023). Research on learner behavior within these systems has examined patterns of help-seeking (Aleven et al., 2003), hint usage (Baker et al., 2008), persistence and disengagement (Baker et al., 2010), and strategic behavior (Baker et al., 2004).

The EdNet dataset (Choi et al., 2020) represents one of the largest publicly available educational datasets, comprising interaction logs from the Santa AI tutoring platform for standardized test preparation in South Korea. Studies using EdNet have examined knowledge tracing algorithms (Ghosh et al., 2020), question difficulty estimation (Choi et al., 2020), and adaptive learning system design (Shin et al., 2021). However, no prior study has used EdNet — or any comparable large-scale dataset — to examine reliance calibration trajectories.

The current study addresses this gap by applying both model-based clustering and latent class growth analysis to longitudinal patterns of AI reliance and performance in the EdNet dataset, bringing together trust-in-automation theory, person-centered statistical methods, and large-scale educational data analytics.

---

## 3. Method

### 3.1 Data Source

This study used the EdNet KT3 dataset (Choi et al., 2020), a large-scale educational interaction log from the Santa AI tutoring application. Santa is a mobile-based AI tutoring platform designed to help Korean students prepare for the Test of English for International Communication (TOEIC). The platform uses a knowledge tracing algorithm combined with collaborative filtering to generate adaptive recommendations for practice questions and explanatory content. The KT3 variant of the dataset includes detailed interaction-level data encompassing question-answering episodes, adaptive content recommendations (tagged as `adaptive_offer`), explanation-viewing behavior, timestamps, and correctness indicators.

The full KT3 dataset contains records from 297,915 unique students. The dataset is publicly available and has been widely used in educational data mining research (Choi et al., 2020). Because the data were collected as de-identified system logs from a commercial platform, individual informed consent was not required; the dataset was released by the platform developers under a research license.

### 3.2 Participants and Filtering Criteria

From the initial pool of 297,915 students, we applied a series of filtering criteria designed to ensure sufficient data density for longitudinal trajectory analysis while retaining students who meaningfully engaged with the AI adaptive recommendation system. The filtering criteria and their rationale were as follows:

First, students were required to have an adaptive offer engagement ratio of at least 0.10. That is, at least 10% of their total episodes were classified as `adaptive_offer` interactions. This threshold ensured that included students had meaningful exposure to the AI recommendation system, as students with negligible adaptive engagement could not exhibit meaningful reliance calibration patterns. The 10% threshold was chosen to balance inclusivity with analytical validity.

Second, students were required to have completed at least 60 total episodes across their entire usage history. This minimum ensured sufficient data points for dividing the usage history into 10 temporal windows (see Section 3.3.1), with at least 6 episodes per window on average.

Third, beyond the ratio criterion, students were required to have at least 5 absolute adaptive offer episodes. This floor ensured that the behavioral reliance measure ($R_b$) was based on a non-trivial number of AI recommendation interactions.

Fourth, students were required to have used the platform across at least 1 calendar day. This criterion excluded students whose entire usage history occurred within a single brief session, which would not permit meaningful longitudinal analysis.

After applying all four filters, the analytic sample comprised **N = 4,568** students.

### 3.3 Variables

#### 3.3.1 Temporal Windows

Each student's complete episode sequence was divided into 10 non-overlapping temporal windows based on deciles of their individual episode count. That is, for a student with 100 episodes, window 1 ($\tau = 1$) comprised episodes 1--10, window 2 ($\tau = 2$) comprised episodes 11--20, and so on through window 10 ($\tau = 10$). This within-person normalization ensured that all students were represented on a common temporal scale regardless of differences in total usage volume, facilitating comparison of trajectory shapes across students with different engagement levels.

#### 3.3.2 Behavioral Reliance ($R_b$)

For each temporal window $\tau$, behavioral reliance was operationalized as:

$$R_b(\tau) = \frac{\text{Number of adaptive\_offer episodes in window } \tau}{\text{Total number of episodes in window } \tau}$$

This measure captures the proportion of a student's activity in a given window that involved engaging with AI-recommended content, bounded between 0 and 1. Higher values indicate greater behavioral reliance on the AI recommendation system. We note that $R_b$ reflects the learner's acceptance of AI-offered content rather than a binary accept/reject decision; the platform surfaces adaptive offers as recommended content, and engaging with this content (versus self-selecting other content) constitutes the behavioral reliance decision.

#### 3.3.3 Performance ($P$)

For each temporal window $\tau$, performance was operationalized as:

$$P(\tau) = \frac{\text{Number of correct responses in window } \tau}{\text{Total number of question-answering episodes in window } \tau}$$

This measure captures the proportion of questions answered correctly, bounded between 0 and 1. Higher values indicate better performance.

#### 3.3.4 Reliance-Performance Gap

The signed gap between reliance and performance was computed as:

$$\text{Gap}(\tau) = R_b(\tau) - P(\tau)$$

Positive values indicate over-reliance (reliance exceeds performance), negative values indicate under-reliance (performance exceeds reliance), and values near zero indicate calibration. The trajectory of this gap across windows captures the calibration dynamics central to our theoretical framework.

#### 3.3.5 Alternative Performance Operationalization: Adaptive Performance ($P_{\text{adaptive}}$)

To detect calibration patterns that may be invisible under the original operationalization, we introduced an alternative performance measure that isolates student performance on AI-recommended questions specifically. This operationalization was motivated by the recognition that a learner's overall accuracy ($P$) conflates performance on self-selected questions with performance on AI-recommended questions, potentially masking the degree to which the AI system's recommendations are benefiting the learner.

Adaptive performance was defined as accuracy on AI-recommended questions only:

$$P_{\text{adaptive}}(\tau) = \frac{\text{Correct responses on adaptive questions in window } \tau}{\text{Total adaptive questions in window } \tau}$$

Similarly, non-adaptive performance was defined as:

$$P_{\text{non-adaptive}}(\tau) = \frac{\text{Correct responses on self-selected questions in window } \tau}{\text{Total self-selected questions in window } \tau}$$

The AI benefit metric was computed as the difference:

$$\text{AI\_benefit}(\tau) = P_{\text{adaptive}}(\tau) - P_{\text{non-adaptive}}(\tau)$$

Across the sample, the mean $P_{\text{adaptive}}$ was 0.738, the mean $P_{\text{non-adaptive}}$ was 0.554, and the mean AI benefit was +0.187, indicating that students performed substantially better on AI-recommended questions than on self-selected questions. This finding is consistent with the adaptive algorithm successfully identifying questions at an appropriate difficulty level.

The alternative calibration gap was then defined as:

$$\text{Gap}_{\text{new}}(\tau) = R_b(\tau) - P_{\text{adaptive}}(\tau)$$

This reformulation captures a wider range of variation because $P_{\text{adaptive}}$ tends to be higher than overall $P$, producing more negative gap values and greater sensitivity to patterns where the AI system's effectiveness changes over time. Approximately 23.8% of student-window observations were missing $P_{\text{adaptive}}$ values because no adaptive questions were attempted in those windows, necessitating a reduced subsample for analyses using this operationalization.

#### 3.3.6 Early Behavior Features (for RQ4)

To investigate whether early behavior predicted subsequent trajectory class membership (RQ4), we extracted several features from the first temporal window ($\tau = 1$) and, where applicable, from the first two windows ($\tau = 1, 2$):

Early reliance rate (`early_R_b`) was defined as $R_b(\tau = 1)$, the proportion of adaptive episodes in the first window. Early exploration rate (`early_expl_rate`) was defined as the proportion of episodes in the first window where the student viewed explanatory content following a question attempt. This variable serves as a proxy for metacognitive engagement, as explanation-seeking behavior reflects a disposition to understand underlying reasoning rather than merely attempting and moving on. Early average explanation duration (`early_avg_expl_dur_s`) was defined as the mean time in seconds that students spent viewing explanation content in the first window. Longer durations may indicate deeper processing of explanatory material. Early performance (`early_P`) was defined as $P(\tau = 1)$, accuracy in the first window.

#### 3.3.7 Outcome Variables (for RQ5)

Two outcome variables were computed for examining class differences in learning outcomes. Overall accuracy was defined as the proportion of correctly answered questions across the student's entire episode history. Accuracy improvement was computed as $P(\tau = 10) - P(\tau = 1)$, capturing the change in performance from the first to the last temporal window.

[INSERT TABLE 1 HERE: Descriptive statistics for $R_b$, $P$, and Gap across 10 temporal windows]

### 3.4 Analytical Approach

#### 3.4.1 Phase 1: Data Preparation

The filtered dataset (N = 4,568) was processed to compute the 10-window time series for each student. For each student, the episode sequence was divided into decile-based windows, and $R_b(\tau)$ and $P(\tau)$ were computed within each window. This yielded a wide-format dataset with 20 features per student: $R_b(1), R_b(2), \ldots, R_b(10), P(1), P(2), \ldots, P(10)$.

#### 3.4.2 Phase 2A: Model-Based Clustering (RQ1)

To identify distinct trajectory classes, we employed model-based clustering (MBC) using the `mclust` package (Scrucca et al., 2016) in R. The choice of MBC over the originally planned latent class mixed model via the `lcmm` package (Proust-Lima et al., 2017) was driven by empirical necessity: the planned parametric-process models failed to converge due to the severe zero-inflation in the $R_b$ variable. Many students had $R_b = 0$ in early windows, creating a point mass at zero that violated the distributional assumptions of the `lcmm` mixed-effects framework. The wide-format MBC approach via `mclust` does not require specifying a parametric growth function and accommodates non-standard distributions more flexibly, albeit at the cost of not modeling individual-level random effects.

The `mclust` algorithm performs model-based clustering by fitting a finite mixture of Gaussian distributions to the multivariate data. It simultaneously estimates the number of components (classes), the component means and covariance structures, and the posterior class membership probabilities for each observation. The algorithm evaluates 14 different parameterizations of the covariance matrix (ranging from spherical to unconstrained) across a range of class numbers (1 through $K_{\max}$), selecting the optimal model based on the Bayesian Information Criterion (BIC).

Model selection proceeded as follows. We evaluated models with 1 through 9 classes across all covariance parameterizations supported by `mclust`. The optimal model was selected based on: (a) BIC, where higher values (in `mclust`'s convention) indicate better model fit penalized for complexity; (b) entropy, a measure of classification certainty ranging from 0 (ambiguous) to 1 (certain), computed from the posterior class membership probabilities; and (c) substantive interpretability, following recommendations in the mixture modeling literature (Nylund et al., 2007; Ram & Grimm, 2009).

Each student was assigned to the class for which their posterior membership probability was highest (modal assignment). Entropy was computed as:

$$E = 1 - \frac{-\sum_{i=1}^{N}\sum_{k=1}^{K} \hat{p}_{ik} \log(\hat{p}_{ik})}{N \log(K)}$$

where $\hat{p}_{ik}$ is the posterior probability of student $i$ belonging to class $k$.

Sensitivity analyses were conducted to evaluate the robustness of the identified class solution through four complementary approaches. First, we compared forced solutions from four to seven classes (all VEE covariance structure). While a seven-class solution yielded a marginally higher BIC (140,115.1 vs. 139,900.6), the six-class solution exhibited superior classification quality: highest entropy (0.824 vs. 0.802), highest ICL (137,011.2 vs. 136,602.6), and no class smaller than 1.7% of the sample. The seven-class solution introduced a 53-student class (1.2%), raising interpretability concerns.

Second, bootstrap likelihood ratio tests (100 replications, VEE model) indicated that each incremental class from two through eight contributed statistically significant improvement (*p* < .01 for all). Because the LRT provided no natural stopping point, we relied on the BIC-ICL-entropy consensus described above to adjudicate among solutions.

Third, a split-half validation procedure randomly divided the sample into two halves (*n* = 2,284 each; seed = 42). Both halves independently selected the same model (VEE, *G* = 6). The mean correlation between matched class centroids across halves was *r* = .970, indicating high replicability of trajectory shapes. The mean cross-validated adjusted Rand index was .503, a moderate but typical value for MBC solutions with overlapping clusters.

Fourth, we examined sensitivity to the adaptive ratio inclusion threshold. At threshold >= 0.15 (*n* = 1,193), BIC selected four classes; at >= 0.20 (*n* = 300), five classes. In both cases, the smaller sample size reduced statistical power to detect peripheral subgroups (Classes 5 and 6), while core classes remained stable (ARI with original assignments: .44 and .38, respectively). These results suggest that the six-class solution is specific to the >= 0.10 threshold but that the major trajectory patterns (Classes 1--4) replicate under stricter criteria.

#### 3.4.3 Phase 2B: Model-Based Clustering with Alternative Operationalization

To explore patterns that might be masked by the original performance measure, we conducted a second MBC analysis using the alternative operationalization described in Section 3.3.5. This analysis employed the $R_b \times P_{\text{adaptive}}$ feature space with the VVV (variable volume, variable shape, variable orientation) covariance structure, applied to the subsample of students with sufficient $P_{\text{adaptive}}$ data. BIC-based model selection identified an 8-class solution as optimal. This alternative analysis served primarily as a discovery tool, enabling the identification of calibration patterns — particularly those involving changes in AI benefit — that were invisible under the original operationalization.

#### 3.4.4 Phase 2C: Latent Class Growth Analysis (RQ2)

To provide a complementary analytical perspective and test the replicability of the trajectory typology, we conducted a latent class growth analysis (LCGA) using the `lcmm` package (Proust-Lima et al., 2017) in R. Unlike the MBC approach, which operates on the full multivariate feature space without specifying a growth function, LCGA explicitly models the growth curve of a single outcome variable within a latent class framework, estimating class-specific intercepts and slopes.

The outcome variable for the LCGA was the alternative calibration gap ($\text{Gap}_{\text{new}} = R_b - P_{\text{adaptive}}$), which provided greater sensitivity to calibration dynamics than the original gap measure. The analysis was conducted on a subsample of N = 3,204 students who had at least 7 valid $P_{\text{adaptive}}$ windows (i.e., windows containing at least one adaptive question), ensuring sufficient longitudinal data for growth curve estimation.

A linear growth model with latent classes was specified, with the calibration gap as the dependent variable and time (window number) as the independent variable. Within-class variance in random effects was fixed to zero (consistent with the LCGA specification, which assumes homogeneity within classes). Models were estimated for $G$ = 1 through $G$ = 7 classes, with 30 random starting values per model to guard against local maxima. Model selection was based on BIC, with entropy used as a supplementary indicator of classification quality. The optimal model was refit to the full subsample data.

#### 3.4.5 Phase 3a: Multinomial Logistic Regression (RQ4)

To examine whether early learning behaviors predict trajectory class membership, we fitted a multinomial logistic regression model with the MBC-assigned class as the dependent variable and the early behavior features (`early_R_b`, `early_expl_rate`, `early_avg_expl_dur_s`, `early_P`) as predictors. Model performance was evaluated using 10-fold cross-validation, reporting mean classification accuracy and comparison against chance-level performance (1/6 = 16.7% for six classes). Predictor importance was assessed using the absolute values of standardized coefficients averaged across class contrasts.

#### 3.4.6 Phase 3b: ANOVA with Post-Hoc Comparisons (RQ5)

To examine differences in learning outcomes across trajectory classes, we conducted one-way analyses of variance (ANOVA) with trajectory class as the between-subjects factor and two dependent variables: overall accuracy and accuracy improvement. Effect sizes were reported as eta-squared ($\eta^2$). Post-hoc pairwise comparisons were conducted using Tukey's HSD test with family-wise error rate correction. Given the large sample size (N = 4,568), we emphasize effect sizes alongside statistical significance in interpreting results.

### 3.5 Ethical Considerations

This study involved secondary analysis of the publicly available, de-identified EdNet KT3 dataset (Choi et al., 2020). As no personally identifiable information was accessed and the data were not collected for this study, this research does not constitute human subjects research under 45 CFR 46 and was therefore exempt from Institutional Review Board review.

---

## 4. Results

### 4.1 Descriptive Statistics

The analytic sample of 4,568 students exhibited considerable variability in engagement and performance. Across all students and windows, the mean behavioral reliance ($R_b$) was relatively low, reflecting the overall tendency for students to engage more with self-selected content than AI-recommended content. Mean $R_b$ increased from approximately 0.04 in the first window to approximately 0.16 in the tenth window, indicating a general trend toward greater adoption of adaptive content over time. Mean performance ($P$) was more stable, hovering around 0.56--0.58 across windows, with a slight upward trend. The reliance-performance gap was negative across all windows (mean Gap ranging from approximately -0.52 in window 1 to -0.40 in window 10), indicating pervasive under-reliance relative to performance across the sample.

### 4.2 RQ1: Identification of Trajectory Classes via Model-Based Clustering

#### 4.2.1 Model Selection

The MBC analysis, conducted using `mclust` on the 20-dimensional wide-format data ($R_b \times 10 + P \times 10$), evaluated models with 1 through 9 classes across all 14 covariance parameterizations. The BIC-based model selection identified a **VEE (variable volume, equal shape, equal orientation) model with 6 classes** as optimal, achieving a BIC of **139,751.3**. The entropy of this solution was **0.82**, indicating good classification certainty.

[INSERT TABLE 2 HERE: MBC model comparison — BIC, entropy, and class sizes for G = 4 to 7]

The 6-class VEE model provided the best balance of fit and parsimony. The 5-class and 7-class solutions were also examined; the 5-class solution merged two substantively distinct classes (combining what became Classes 2 and 3), while the 7-class solution split one class into two small and poorly differentiated subgroups. These comparisons supported the substantive interpretability of the 6-class solution.

#### 4.2.2 Description of the Six Trajectory Classes

[INSERT FIGURE 1 HERE: 6-class mean trajectories ($R_b$ and $P$, 6-panel display)]

[INSERT FIGURE 2 HERE: Gap ($R_b - P$) trajectories by class]

**Class 1: Gradual Adopters (n = 1,367; 29.9%).** This was the second-largest class. Students in this class began with very low AI reliance ($R_b$ increasing from 0.05 in window 1 to 0.14 in window 10) and maintained stable, moderate performance ($P \approx 0.59$ throughout). The reliance-performance gap widened slightly in the positive direction ($\Delta$Gap = +0.09), reflecting gradually increasing adoption of AI recommendations without corresponding performance change. This class represents learners who progressively warmed to the AI system's recommendations but whose performance neither benefited from nor was harmed by this increasing reliance.

**Class 2: Steady Calibrators (n = 1,582; 34.6%).** This was the largest class. Students began with very low reliance ($R_b = 0.03$) and slightly below-average performance ($P = 0.53$), with both measures increasing steadily over time ($R_b$ to 0.17, $P$ to 0.56). The reliance-performance gap change ($\Delta$Gap = +0.10) reflected reliance increasing faster than performance, but the concurrent improvement in both variables suggests a calibration process in which increasing reliance co-occurred with learning gains.

**Class 3: Strong Calibrators (n = 859; 18.8%).** Students in this class showed a pattern similar to Class 2 but with more pronounced changes. Starting from low reliance ($R_b = 0.04$) and the lowest initial performance ($P = 0.50$), they exhibited the strongest simultaneous increase in both reliance ($R_b$ to 0.19) and performance ($P$ to 0.54). The gap change ($\Delta$Gap = +0.11) was the second-largest, yet this class demonstrated the greatest performance improvement of any class (see RQ5 results below). This pattern is consistent with a calibration process in which learners who began struggling increasingly turned to AI recommendations and benefited from doing so.

**Class 4: High Performers with Low Reliance (n = 451; 9.9%).** This class exhibited a distinctive profile: the highest and most stable performance ($P \approx 0.65$) paired with consistently low AI reliance ($R_b$ increasing modestly from 0.06 to 0.11). The gap change was minimal ($\Delta$Gap = +0.03), reflecting a stagnant calibration trajectory. These students performed well without substantial reliance on AI recommendations, suggesting they either did not need AI support or had alternative learning strategies.

**Class 5: Heavy Adopters (n = 240; 5.3%).** This smaller class showed the highest terminal reliance ($R_b = 0.23$ in window 10) among all classes that began with low reliance. Starting from moderate initial reliance ($R_b = 0.09$) and average performance ($P \approx 0.57$), these students sharply increased their AI reliance while maintaining stable performance. The large gap change ($\Delta$Gap = +0.13) was the largest of any class, representing an escalating reliance pattern that outpaced any performance gains.

**Class 6: Early Heavy Users (n = 69; 1.5%).** This was the smallest and most distinctive class. Students began with the highest initial reliance ($R_b = 0.33$) — far exceeding all other classes — and their reliance actually *decreased* slightly over time ($R_b$ to 0.29). Performance was moderate and stable ($P \approx 0.59$). The gap change was negative ($\Delta$Gap = -0.02), the only class showing a declining gap. This class may represent students who arrived with strong prior engagement with AI recommendation systems or who initially over-relied on the system and gradually self-corrected.

### 4.3 RQ2: Replication via Latent Class Growth Analysis

#### 4.3.1 LCGA Model Selection

The LCGA analysis, conducted on the subsample of N = 3,204 students with sufficient $P_{\text{adaptive}}$ data, modeled the growth trajectory of the alternative calibration gap ($\text{Gap}_{\text{new}} = R_b - P_{\text{adaptive}}$) across temporal windows. The following table presents the model fit statistics for solutions ranging from 1 to 5 classes.

| G | Log-likelihood | BIC | Entropy |
|---|----------------|-----|---------|
| 1 | 505.9 | -982.5 | --- |
| 2 | 568.2 | -1085.2 | 0.822 |
| 3 | 591.7 | -1110.3 | 0.830 |
| 4 | 607.1 | -1119.2 | --- |
| 5 | 611.3 | -1105.6 | --- |

The 4-class solution achieved the lowest (most negative) BIC of -1119.2, indicating the best balance of fit and parsimony. BIC improved substantially from 1 to 4 classes, with the 5-class model showing a reversal (BIC = -1105.6), supporting 4 as the optimal number of classes. The full data refit of the 4-class model yielded a BIC of -2795.2.

#### 4.3.2 Description of the Four LCGA Classes

The four LCGA classes are described below in terms of their calibration gap trajectories, using the alternative operationalization ($R_b - P_{\text{adaptive}}$).

**LCGA Class 1: Stagnant Under-Reliance (n = 2,662; 83.1%).** This was the dominant class, comprising the vast majority of the subsample. Students exhibited low and slowly increasing reliance ($R_b$ from 0.054 to 0.148) paired with high but slowly declining adaptive performance ($P_{\text{adaptive}}$ from 0.807 to 0.726). The calibration gap remained deeply negative and relatively constant, moving from -0.698 to -0.562 ($\Delta$Gap = +0.136). This pattern represents persistent under-reliance with minimal calibration change over time — students performed well on AI-recommended questions but rarely followed the AI's recommendations.

**LCGA Class 2: Near-Calibrated Fluctuators (n = 75; 2.3%).** This small class exhibited moderate reliance ($R_b$ from 0.127 to 0.231) and moderate adaptive performance ($P_{\text{adaptive}}$ from 0.467 to 0.455). The calibration gap hovered near zero and fluctuated without a clear directional trend, moving from -0.214 to -0.196 ($\Delta$Gap = -0.018). These students were the closest to calibration of any class, with reliance approximately matching their performance on AI-recommended questions.

**LCGA Class 3: Convergent Learners (n = 290; 9.1%).** Students in this class showed increasing reliance ($R_b$ from 0.064 to 0.212) paired with declining adaptive performance ($P_{\text{adaptive}}$ from 0.710 to 0.515). The calibration gap narrowed substantially from -0.573 to -0.280 ($\Delta$Gap = +0.293). This convergent pattern is consistent with the theoretical prediction of gap narrowing: as reliance increased and the performance advantage of adaptive questions diminished, students moved closer to calibration. The convergence was driven both by increasing $R_b$ and by a decline in $P_{\text{adaptive}}$ that brought the two measures closer together.

**LCGA Class 4: AI Benefit Emergence / Divergent (n = 177; 5.5%).** This class exhibited a distinctive and theoretically novel pattern. Reliance fluctuated and then declined slightly ($R_b$ from 0.090 to 0.147), while adaptive performance increased dramatically ($P_{\text{adaptive}}$ from 0.473 to 0.722). The calibration gap widened from -0.301 to -0.543 ($\Delta$Gap = -0.242). In this class, the AI system appeared to become increasingly effective for the student (as measured by rising $P_{\text{adaptive}}$), but the student's reliance on the AI did not keep pace. This pattern, which we term AI Benefit Emergence (ABE), represents a form of under-reliance that intensifies precisely as the AI becomes more beneficial — a paradoxical divergence not predicted by the original theoretical framework.

### 4.4 RQ3: Theory-Empirical Comparison

The theoretical framework predicted four trajectory shapes: convergent (gap narrowing toward zero), divergent (gap widening from zero), stagnant (gap remaining constant), and catastrophic (sudden disruption). We evaluated the empirical classes from both the MBC and LCGA analyses against these predictions.

#### 4.4.1 Convergent Calibration Patterns (H2a: Supported)

Both analytical methods identified convergent calibration patterns. In the MBC analysis, Classes 2 (Steady Calibrators) and 3 (Strong Calibrators) best approximated the convergent prediction, showing concurrent increases in both reliance and performance. The convergence was partial: the reliance-performance gap narrowed in a relative sense (as the gap was initially very negative, and the increase in $R_b$ brought it closer to alignment), but the gap did not reach zero. In the LCGA analysis, Class 3 (Convergent Learners) exhibited the clearest convergent pattern, with the calibration gap narrowing by 0.293 units across the observation period. The persistent under-reliance (gap remaining negative) suggests that full calibration — in the sense of reliance matching performance — was not achieved within the observed time frame, but the directionality of change was consistent with the theoretical prediction.

[INSERT FIGURE 3 HERE: Theory vs. empirical overlay]

[INSERT FIGURE 4 HERE: Trajectory classes in the behavioral reliance-performance state space]

Figure 4 presents the six MBC trajectory classes as paths through the behavioral reliance × performance ($R_b \times P$) state space, with each panel showing one class's mean trajectory from window 1 (open circle) to window 10 (filled circle) against grey background traces of all other classes for positional reference. The classes occupy distinct regions of the state space and exhibit qualitatively different movement patterns. Classes 2 and 3 display the clearest convergent behavior, with simultaneous rightward (increasing $R_b$) and upward (increasing $P$) movement — the former from moderate starting values, the latter from the lowest initial performance. Class 4 occupies the high-$P$, low-$R_b$ region and uniquely exhibits a retreat pattern in later windows. Class 6, positioned at the highest $R_b$ values, shows volatile fluctuations rather than directional movement. The spatial separation of classes in the $R_b \times P$ space illustrates the multivariate basis of the MBC classification: classes differ not only in their gap trajectories (Figure 2) but in their absolute levels and movement patterns across both reliance and performance dimensions.

#### 4.4.2 Stagnant Calibration Patterns (H2b: Supported)

Both methods also identified stagnant calibration patterns. In the MBC analysis, Class 4 (High Performers with Low Reliance) exhibited minimal change in the reliance-performance gap across windows ($\Delta$Gap = +0.03). These students maintained a stable equilibrium of high performance and low reliance. In the LCGA analysis, Class 1 (Stagnant Under-Reliance), comprising 83.1% of the subsample, exhibited a gap that remained deeply negative throughout, with only modest change ($\Delta$Gap = +0.136 over 10 windows). The dominance of this stagnant pattern across both methods underscores the pervasiveness of stable under-reliance in the sample.

#### 4.4.3 Escalating Reliance Without Proportional Performance Gains

Classes 1 (Gradual Adopters) and 5 (Heavy Adopters) from the MBC analysis showed a pattern of escalating reliance without proportional performance gains, creating a widening gap. This pattern, while not divergent in the sense of moving away from calibration (the gap was initially very negative and moved toward zero), represents a trajectory that could become over-reliant if the trend continued beyond the observation period.

#### 4.4.4 Self-Correcting Over-Reliance

Class 6 (Early Heavy Users) from the MBC analysis showed a unique pattern of decreasing reliance from an initially high level, representing a trajectory that moved toward (though did not reach) calibration from the over-reliance side.

#### 4.4.5 Beyond Predicted Patterns: AI Benefit Emergence

A novel trajectory pattern emerged from both the alternative-operationalization MBC analysis (Phase 2B) and the LCGA (Phase 2C) that was not predicted by the theoretical framework. In the Phase 2B MBC analysis using the VVV 8-class model, Class 4 (n = 256; 5.7%) exhibited a dramatic increase in adaptive performance ($P_{\text{adaptive}}$ from 0.275 to 0.852) paired with minimal increase in reliance ($R_b$ from 0.020 to 0.171). The calibration gap widened from -0.039 to -0.601, indicating that as the AI system's recommendations became increasingly effective for these students, their reliance failed to keep pace. In the LCGA analysis, Class 4 (n = 177; 5.5%) showed a strikingly parallel pattern: $P_{\text{adaptive}}$ increasing from 0.473 to 0.722 while $R_b$ remained low and fluctuating, with the gap widening from -0.301 to -0.543.

We term this pattern AI Benefit Emergence (ABE). It represents a situation in which the AI tutoring system becomes increasingly beneficial for a learner — as evidenced by rising accuracy on AI-recommended questions — but the learner does not proportionally increase their engagement with the system's recommendations. The convergence of this finding across two independent analytical methods, each using different operationalizations and modeling assumptions, strengthens confidence that ABE represents a genuine behavioral pattern rather than a methodological artifact.

[INSERT FIGURE 5 HERE: AI Benefit Emergence — the fifth trajectory pattern]

Figure 5 visualizes the ABE pattern across both analytical methods. Panel A presents the LCGA Class 4 trajectory: the blue line ($P_{\text{adaptive}}$) rises steadily from 0.47 to 0.72, indicating that the AI system's recommendations become progressively more effective for these learners, while the red dashed line ($R_b$) remains flat and even declines in later windows (from a peak of 0.19 in window 6 to 0.15 by window 10). The shaded area between the two lines represents the growing calibration gap — a widening chasm between what the AI can offer and what the learner actually utilizes. By window 10, this gap has nearly doubled from 0.30 to 0.54. Panel B shows the MBC Phase 2B Class 4 trajectory, which exhibits a strikingly parallel pattern with an even more dramatic divergence: $P_{\text{adaptive}}$ rises from 0.28 to 0.85 while $R_b$ increases only modestly from 0.02 to 0.17, producing a gap that widens from 0.26 to 0.68. The convergence of this "scissors" pattern across two independent methods — each using different samples, operationalizations, and modeling frameworks — strengthens the case that ABE represents a genuine behavioral phenomenon rather than a methodological artifact.

The ABE pattern can be understood through several theoretical mechanisms from the trust-in-automation literature. Parasuraman and Riley's (1997) concept of disuse — the neglect of available automation — provides the broadest framing: these students are failing to utilize an AI resource that demonstrably improves their performance. Lee and Moray's (1994) trust asymmetry hypothesis offers a more specific mechanism: if these students experienced early negative interactions with the AI system (e.g., poor recommendations during initial sessions), the resulting distrust may persist even as the system's recommendations improve, because trust builds more slowly than it erodes. Anchoring effects may also play a role: early impressions of AI utility may anchor subsequent reliance decisions, making students slow to update their behavior even when the evidence for AI benefit accumulates.

This empirically discovered pattern extends the theoretical framework beyond its original four predicted trajectories. ABE represents a fifth trajectory type — a mirror image of the catastrophic pattern (in which sudden AI failure causes a trust violation) but operating in the opposite direction: gradual AI improvement that fails to generate a corresponding trust and reliance update.

### 4.5 RQ4: Early Behavior as a Predictor of Trajectory Class

[INSERT FIGURE 6 HERE: Early behavioral predictors of trajectory class membership]

The multinomial logistic regression model predicting 6-class membership from early behavioral features yielded a cross-validated classification accuracy of **49.4%** (SD across folds = 2.1%). Given that chance-level accuracy for six equally probable classes is 16.7%, the model achieved approximately **3.0 times chance performance**, indicating meaningful predictive power from early behavior alone.

[INSERT TABLE 3 HERE: Multinomial logistic regression coefficients]

The strongest predictor was **early exploration rate** (`early_expl_rate`), with a mean absolute standardized coefficient of 1.00 (the highest among all predictors). This variable — the proportion of first-window episodes in which the student viewed explanatory content — differentiated classes in several key contrasts. Specifically, higher early explanation rates were associated with membership in Classes 2 (Steady Calibrators) and 3 (Strong Calibrators) relative to Class 1 (Gradual Adopters) and Class 4 (High Performers with Low Reliance).

The second most important predictor was **early average explanation duration** (`early_avg_expl_dur_s`), with a mean absolute coefficient of 0.60. Students who spent more time per explanation view tended toward the calibrating classes (2 and 3), suggesting that not merely viewing explanations but engaging deeply with them was associated with subsequent calibration trajectories.

**Early reliance rate** (`early_R_b`) was the third predictor in importance (mean |coefficient| = 0.30), primarily distinguishing Class 6 (Early Heavy Users) from all other classes, as expected given their uniquely high initial reliance.

These results support H3 — early explanation-seeking behavior was the strongest predictor of trajectory class membership. The dominance of explanation-related features (rate and duration) over initial reliance and initial performance suggests that metacognitive engagement patterns, rather than starting levels of reliance or ability, are the primary behavioral markers of subsequent calibration trajectories.

### 4.6 RQ5: Class Differences in Learning Outcomes

#### 4.6.1 Overall Accuracy

A one-way ANOVA comparing overall accuracy across the six trajectory classes yielded a statistically significant result: **F(5, 4562) = 177.46, p = 4.66 x 10^-173, $\eta^2$ = 0.163**. The effect size was large, indicating that trajectory class membership accounted for approximately 16.3% of the variance in overall accuracy.

[INSERT TABLE 4 HERE: Class outcome differences — overall accuracy, accuracy improvement, and post-hoc comparisons]

Class 4 (High Performers with Low Reliance) had the highest overall accuracy (M = .649, SD = .04), significantly exceeding all other classes (all Tukey HSD p < .001). Class 3 (Strong Calibrators) had the lowest overall accuracy (M = .536, SD = .10), significantly lower than all other classes except Class 2 (Steady Calibrators; M = .570). The remaining classes fell between these extremes: Class 1 (M = .598, SD = .05), Class 6 (M = .581, SD = .11), Class 5 (M = .576, SD = .05), and Class 2 (M = .570, SD = .07).

#### 4.6.2 Accuracy Improvement

A one-way ANOVA comparing accuracy improvement ($P(\tau = 10) - P(\tau = 1)$) across classes was also significant: **F(5, 4562) = 25.08, p = 5.04 x 10^-25, $\eta^2$ = 0.027**. The effect size was small, indicating that trajectory class membership explained approximately 2.7% of the variance in accuracy improvement.

Class 3 (Strong Calibrators) showed the greatest improvement (M = +.048, SD = .18), significantly exceeding Classes 1 and 4 (p < .001). Class 2 (Steady Calibrators) also showed positive improvement (M = +.023, SD = .13). Class 4 (High Performers with Low Reliance) showed minimal improvement (M = +.010, SD = .07), consistent with a ceiling effect. Class 1 (Gradual Adopters), despite increasing AI engagement, showed a slight decline in accuracy (M = -.010, SD = .09), as did Class 5 (Heavy Adopters; M = -.003, SD = .08). These negative improvement values, while small in magnitude, are noteworthy: they indicate that increasing behavioral reliance on AI did not uniformly translate into performance gains, consistent with the observational design's inability to establish causal relationships between AI use and learning outcomes.

#### 4.6.3 The Performance-Improvement Inverse Relationship

A notable pattern emerged from the joint consideration of overall accuracy and accuracy improvement: the classes ranked in approximately inverse order on these two outcomes. Class 4, with the highest overall accuracy, showed the least improvement. Class 3, with the lowest overall accuracy, showed the most improvement. This inverse relationship is consistent with a ceiling effect interpretation: students with initially high performance have less room for growth, while initially struggling students who engage in calibration processes may show the greatest gains.

This finding provides **modified support for H4**. The convergent calibration class (Class 3, Strong Calibrators) was associated with the greatest *improvement* in performance, consistent with the theoretical prediction that calibrated reliance facilitates learning. However, this same class had the lowest *absolute* performance, and the class with the highest absolute performance (Class 4) followed a stagnant, not convergent, calibration trajectory. Thus, the relationship between calibration and outcomes depends on whether the outcome is defined in terms of level or growth.

#### 4.6.4 Classification Quality and Robustness

The overall average posterior probability for assigned classes was .820, with 76.4% of students assigned with posterior probability exceeding .70 and 62.2% exceeding .80. Classification quality varied across classes: Classes 3 (M = .891), 6 (M = .913), and 5 (M = .874) were most clearly separated, while Classes 1 (M = .779) and 4 (M = .797) showed the most overlap. A cross-classification analysis revealed that Class 1 students were most frequently confused with Classes 2 and 4, consistent with their intermediate trajectory positions. The normalized entropy of .760 indicated that approximately 76% of classification certainty was retained, supporting the interpretability of the class assignments. Sensitivity analyses confirmed that the core class structure replicated across split-half samples and that the ANOVA effects were driven primarily by well-separated classes (3, 5, 6), bolstering confidence in the reported between-class differences.

[INSERT TABLE 5 HERE: Sensitivity analysis summary]

---

## 5. Discussion

### 5.1 Summary of Findings

This study investigated longitudinal patterns of AI reliance calibration among 4,568 learners using the Santa AI tutoring platform, employing two complementary analytical methods to test whether theoretically predicted trajectory patterns are observable in behavioral data. Using model-based clustering on joint trajectories of behavioral reliance and performance across 10 temporal windows, we identified six distinct trajectory classes. Using latent class growth analysis on calibration gap growth curves in a subsample of 3,204 students, we identified four trajectory classes that converged with the MBC findings on key structural features. Across both methods, a novel fifth trajectory pattern — AI Benefit Emergence — was discovered that extends the theoretical framework. The key findings are: (a) substantial heterogeneity exists in how learners calibrate their reliance on AI recommendations over time (H1 supported); (b) both convergent and stagnant calibration patterns predicted by theory were observed in the data (H2a and H2b supported); (c) early explanation-seeking behavior is the strongest predictor of subsequent calibration trajectories (H3 supported); (d) the relationship between calibration and learning outcomes is nuanced, with convergent calibrators showing the greatest improvement but not the highest absolute performance (H4 partially supported); and (e) the ABE pattern represents an empirically grounded extension to the theoretical framework.

### 5.2 Interpretation of the Six MBC Trajectory Classes

The six classes identified by the MBC analysis occupy distinct regions of the behavioral reliance–performance ($R_b \times P$) state space (Figure 4), exhibiting qualitatively different movement patterns that suggest heterogeneous calibration dynamics. The following interpretations are offered as theoretically motivated accounts consistent with the observed behavioral patterns; however, because the data capture behavioral outcomes rather than psychological processes, the underlying mechanisms remain inferential.

**Gradual Adopters (Class 1; 29.9%)** occupy a high-performance, low-reliance region of the state space and move primarily rightward — increasing $R_b$ with minimal change in $P$. These learners are incrementally increasing AI engagement without corresponding performance change; AI adoption for this group appears functionally neutral within the observed period. From an intervention perspective, these students might benefit from targeted trust calibration scaffolds that help them evaluate AI recommendation quality, potentially accelerating the adoption of beneficial recommendations.

**Steady Calibrators (Class 2; 34.6%)** and **Strong Calibrators (Class 3; 18.8%)** together comprise over half the sample and exhibit the clearest convergent movement in the $R_b \times P$ space: simultaneous rightward and upward displacement indicating co-occurring increases in reliance and performance. The key distinction lies in their starting positions and displacement magnitudes. Class 3 begins at the lowest performance level ($P \approx 0.50$) and exhibits the largest diagonal displacement in the state space, while Class 2 starts at a moderate position and shows more gradual change. The co-movement of reliance and performance is the behavioral signature one would expect from a productive calibration process, though the observational design precludes causal attribution — shared underlying characteristics such as motivation or metacognitive engagement may independently drive both behavioral changes.

**High Performers with Low Reliance (Class 4; 9.9%)** occupy the upper-left corner of the state space — the highest performance combined with the lowest AI engagement. Uniquely among the six classes, Class 4 exhibits a retreat pattern: after initial rightward movement (windows 1–7), $R_b$ decreases in later windows while $P$ remains stable (Figure 4, panel C4). The most parsimonious account is deliberate disengagement: these high-performing students tried the AI system and found it unnecessary. Alternative explanations — strong prior knowledge rendering recommendations redundant, or effective self-regulated learning strategies obviating external guidance — point in the same direction. This stagnant-to-retreating trajectory represents a stable equilibrium that, while effective for maintaining current performance, may limit opportunities for AI-mediated growth.

**Heavy Adopters (Class 5; 5.3%)** show rapid rightward movement with moderate upward change — substantial increases in AI engagement accompanied by performance gains that decelerate in later windows. This is a diminishing-returns trajectory: the marginal benefit of additional AI engagement appears to decrease beyond a certain threshold. Within the observed period, the reliance-performance gap remained in the under-reliance range; however, the trajectory's direction suggests that continued escalation could eventually approach or cross the calibration boundary.

**Early Heavy Users (Class 6; 1.5%)**, while comprising only 69 students, exhibit the most distinctive pattern in the state space: a volatile trajectory with large oscillations in both $R_b$ and $P$ dimensions. Starting at the highest $R_b$ values ($\approx 0.33$), this class's trajectory is marked by erratic fluctuations rather than directional movement. The volatility may partly reflect the small class size, but it also points toward an unstable engagement dynamic in which reliance and performance are weakly coupled.

An important interpretive caveat applies to all of the above accounts. The psychological characterizations offered — cautious exploration, productive calibration, deliberate disengagement, diminishing returns — describe behavioral patterns that are *compatible with* these motivational and cognitive mechanisms but are not directly evidenced by the data. $R_b$ serves as a behavioral proxy for AI reliance, but adaptive content selection may be driven by factors other than trust or calibration judgments, including habit, curiosity, or interface design. Similarly, performance changes may reflect independent learning, practice effects, or content difficulty variation rather than AI-mediated benefit. These behavioral trajectories generate testable hypotheses about underlying mechanisms that future research — combining behavioral logs with self-report measures of trust, motivation, and self-efficacy — should directly assess.

### 5.3 Methodological Triangulation: Model-Based Clustering and Latent Class Growth Analysis

A distinctive contribution of this study is the application of two complementary analytical methods to the same phenomenon. The MBC approach via mclust and the LCGA approach via lcmm differ in their assumptions, operationalizations, and structural features, yet both yielded findings that converge on key substantive conclusions while also providing unique insights.

The MBC analysis captured six fine-grained trajectory classes based on the joint $R_b \times P$ feature space, identifying nuanced distinctions among classes that share similar gap trajectories but differ in the absolute levels and shapes of their reliance and performance curves. This multivariate approach is sensitive to patterns in both the level and shape of trajectories and does not require specifying a parametric growth function, making it well-suited for exploratory identification of trajectory types.

The LCGA analysis captured four broader trajectory classes based on the growth curve of the calibration gap. By modeling the gap directly as a function of time, LCGA provides interpretable growth parameters (intercepts and slopes) and a more parsimonious representation of calibration dynamics. The use of the alternative operationalization ($R_b - P_{\text{adaptive}}$) further distinguished the LCGA from the MBC by targeting a more sensitive measure of calibration.

The correspondence between the two solutions, while not one-to-one, reveals meaningful convergence. LCGA Class 1 (Stagnant Under-Reliance, 83.1% of the subsample) corresponds broadly to MBC Classes 1, 2, and 4 (combined approximately 75% of the full sample), all of which are characterized by persistent under-reliance with limited calibration change. LCGA Class 3 (Convergent Learners) corresponds to MBC Classes 2 and 3, both showing gap-narrowing dynamics. LCGA Class 4 (ABE/Divergent) identified a pattern that was also detected in the Phase 2B alternative MBC analysis but not in the original Phase 2A MBC analysis, demonstrating the value of the alternative operationalization. The cross-method adjusted Rand index was 0.045, which is expected given that the two methods used different operationalizations (original $R_b \times P$ vs. alternative $R_b - P_{\text{adaptive}}$), different modeling frameworks (multivariate Gaussian mixture vs. linear growth with latent classes), and different samples (N = 4,568 vs. N = 3,204).

The convergence of both methods on two key findings — the dominance of under-reliance and the existence of both convergent and stagnant calibration patterns — strengthens confidence in these conclusions. At the same time, the unique contribution of each method (e.g., the finer class distinctions afforded by MBC, the discovery of the ABE pattern via LCGA's sensitivity to the alternative operationalization) demonstrates that methodological triangulation yields a richer understanding than either approach alone.

### 5.4 The Dominance of Under-Reliance

A striking finding across all classes, time windows, and analytical methods was the predominance of under-reliance: the reliance-performance gap was negative at the class mean level throughout, meaning students' mean performance consistently exceeded their mean behavioral reliance on AI recommendations. Even Class 6, with the highest reliance levels, maintained a mean gap near zero rather than crossing into over-reliance territory.

This pattern is not a structural artifact of the operationalization. At the individual observation level, over-reliance ($R_b > P$) was observed in 1.67% of student-window observations (765 out of 45,680), spanning 12.7% of students (581 out of 4,568). Students who exhibited over-reliance windows were characterized by higher adaptive engagement (mean adaptive ratio = 0.172 vs. 0.133) and lower accuracy (mean $P$ = 0.512 vs. 0.590) — a profile matching theoretical predictions of over-reliance as high AI dependence paired with low personal competence. Over-reliance prevalence also increased over time (0.4% in window 1 to 2.4% in window 10), tracking the general increase in $R_b$ across windows. That over-reliance is structurally possible, empirically present at the individual level, yet absent from all class mean trajectories strengthens the conclusion that under-reliance is the dominant and stable behavioral pattern in this educational AI context.

This finding has several possible explanations. First, $R_b$ as operationalized in this study (proportion of adaptive offer episodes) tends toward low values because the platform does not aggressively promote adaptive content — adaptive episodes constitute only approximately 13% of total episodes even among students meeting the inclusion threshold. Second, under-reliance may be the normative behavioral pattern in educational AI systems, where learners are intrinsically motivated to demonstrate independent competence and may view AI reliance as a crutch. Third, under-reliance in the context of TOEIC preparation may reflect the specific goal structure of standardized test preparation, where students aim to develop independent test-taking ability rather than dependence on external support.

Regardless of the explanation, the ubiquity of under-reliance at the trajectory class level challenges assumptions from high-stakes automation domains where over-reliance is the primary concern (Parasuraman & Manzey, 2010). In educational AI contexts, the risk appears to be primarily one of under-utilization rather than over-trust — a pattern well-documented in the help-avoidance literature on intelligent tutoring systems (Aleven et al., 2003; Baker et al., 2008).

These findings sit in sharp tension with the prevailing policy narrative around AI in education. Since the emergence of widely accessible generative AI tools in late 2022, the dominant institutional response has centered on preventing over-reliance — universities have oscillated between outright bans and cautious adoption policies, driven largely by concerns that students will become excessively dependent on AI assistance (UNESCO, 2023; Kasneci et al., 2023). The under-reliance patterns documented in this study suggest that these concerns, while not unfounded at the individual level (1.67% of observations showed over-reliance), may be misdirected at the population level. The primary behavioral challenge in this educational AI context was not that students trusted the AI too much, but that they trusted it too little.

This reframing carries practical significance. If under-reliance is indeed the dominant pattern, then policies focused exclusively on preventing over-reliance may inadvertently reinforce existing barriers to productive AI use. Students who could benefit from AI-recommended content may be further discouraged from engaging with it. A more nuanced policy approach would recognize both risks — monitoring for the minority who may over-rely while actively supporting the majority who under-utilize available AI resources (Mollick & Mollick, 2023).

### 5.5 AI Benefit Emergence: A Novel Fifth Trajectory Pattern

Perhaps the most significant theoretical contribution of this study is the discovery of the AI Benefit Emergence (ABE) pattern — a trajectory in which the AI system becomes increasingly effective for the learner (as measured by rising $P_{\text{adaptive}}$) but the learner's reliance on the AI does not proportionally increase. This pattern was identified independently by two analytical methods: in the Phase 2B MBC analysis using the alternative operationalization (Class 4, n = 256, 5.7% of the subsample) and in the LCGA analysis (Class 4, n = 177, 5.5% of the subsample). That two independent methods — using different operationalizations, modeling frameworks, and samples — both isolated this pattern reduces the likelihood that it is a methodological artifact.

ABE can be formally defined as a trajectory in which $P_{\text{adaptive}}$ increases substantially over time while $R_b$ remains stable or increases only modestly, resulting in a widening calibration gap. This is the mirror image of the catastrophic pattern predicted by trust-in-automation theory: whereas the catastrophic pattern involves a sudden decline in AI reliability that disrupts previously calibrated trust, the ABE pattern involves a gradual improvement in AI effectiveness that fails to elicit a corresponding trust and reliance update. Both patterns reflect the same underlying asymmetry in human-automation trust dynamics — the well-documented finding that trust erodes faster than it builds (Lee & Moray, 1994; Muir & Moray, 1996) — but operating in opposite directions.

Three mechanisms from the trust-in-automation literature offer candidate explanations for the ABE pattern. First, Parasuraman and Riley's (1997) concept of disuse provides a broad framing: ABE learners are neglecting a beneficial automated resource, potentially due to stable negative attitudes toward AI formed during early interactions. Second, trust hysteresis — the phenomenon whereby trust, once lost, requires disproportionate positive evidence to recover — may explain why gradually improving AI performance fails to shift reliance upward. If these learners experienced poor initial recommendations, the resulting distrust may persist long after the AI system's recommendations have improved. Third, anchoring effects (Tversky & Kahneman, 1974) may contribute: early experiences with the AI system may establish an anchor for reliance decisions that is resistant to updating, even as accumulating evidence suggests that the AI's recommendations have become more beneficial.

The educational implications of the ABE pattern are distinctive. Unlike stagnant under-reliance (where the AI's effectiveness is stable and the learner simply does not engage), ABE represents a dynamic situation in which the AI system is becoming more helpful but the learner is missing out on these growing benefits. ABE learners need a different kind of support: not encouragement to use AI more, but feedback that makes the AI's improving track record visible. Transparency features displaying the system's recent recommendation accuracy, or periodic prompts inviting learners to re-evaluate the AI's utility based on recent performance, would give these learners the evidence their reliance decisions are currently missing.

### 5.6 Reliance, Trust, and the Behavioral-Cognitive Bridge

This study deliberately operationalized its construct at the behavioral level (reliance calibration) rather than the cognitive-attitudinal level (trust calibration). This choice was driven by data availability — the EdNet dataset contains behavioral logs but not self-report measures of trust. However, the relationship between reliance and trust carries important theoretical implications that position the behavioral findings of this study as evidence for the broader theory of trust calibration.

Following Lee and See's (2004) model, trust is the attitudinal precursor that guides reliance behavior. If this pathway holds in educational contexts, then the behavioral reliance patterns observed in this study are downstream manifestations of underlying trust dynamics. The trajectory classes, while defined by behavioral reliance and performance, map onto distinct trust states in this framework. Classes 2 and 3 look like trust building in action — their convergent reliance-performance co-movement is what calibration theory predicts when learners accumulate positive experience with an AI system. Class 4's stable high performance with declining AI engagement suggests settled indifference rather than active distrust; these students assessed the system and moved on. The escalating patterns of Classes 1 and 5 are compatible with growing trust translating into increasing reliance, while Class 6's self-correcting trajectory suggests trust recalibration following an initial period of over-engagement. The ABE pattern is perhaps the most theoretically revealing: trust damaged early appears not to recover despite improving AI performance — precisely the hysteresis dynamic that the automation literature would predict.

These interpretations remain speculative in the absence of direct trust measurement. Future research combining behavioral log data with periodic trust assessments would enable direct testing of the trust-to-reliance pathway in educational contexts. Nevertheless, the behavioral patterns observed here align with theoretical predictions about how trust calibration should manifest in observable behavior, providing what we term *behavioral evidence* for trust calibration trajectory theory.

### 5.7 Connection to Trust Calibration Theory: Behavioral Evidence

This study provides behavioral evidence for the conceptual framework developed in this research program, which proposed trust calibration readiness (TCR) as an educational competency comprising three dimensions: Awareness (recognizing AI capabilities and limitations), Judgment (evaluating AI output quality), and Action (making appropriate reliance decisions). The behavioral patterns observed in this study speak primarily to the Action dimension — the observable reliance decisions that learners make.

The behavioral data speak to the TCR framework in four ways. First, the heterogeneity in trajectory classes supports the proposition that calibration is a skill that varies across individuals, not a uniform developmental outcome. The framework predicts that individuals at different levels of calibration readiness will follow different trajectory shapes, and the identification of six distinct MBC classes and four LCGA classes confirms this prediction. Second, the association between early explanation-seeking behavior and subsequent calibration trajectories speaks to the Awareness and Judgment dimensions: students who actively engage with explanatory content may be developing the evaluative skills necessary for calibrated reliance decisions. Third, the existence of stagnant classes (MBC Class 4; LCGA Class 1) aligns with the framework's prediction that some learners may stabilize at a particular action pattern without progressing through the full calibration competency cycle. Fourth, the discovery of the ABE pattern extends the framework by identifying a trajectory type that was not originally predicted, suggesting that trust calibration dynamics in educational contexts may be more complex than initially theorized.

The use of two complementary analytical methods strengthens the evidentiary value of these findings. As discussed in Section 5.3, MBC and LCGA converge on the existence of convergent, stagnant, and ABE patterns despite different operationalizations and modeling assumptions — triangulated evidence that these trajectory types are robust features of the data. This moves the evidence base for trust calibration theory beyond consistency checking toward behavioral confirmation.

### 5.8 Educational Implications

These trajectory classes are not uniformly served by the same instructional design. Three intervention profiles emerge from the data.

*The under-reliance majority* (Classes 1, 2, and 3 — comprising 83% of the sample) would benefit from support that facilitates productive AI engagement. Gradual Adopters (Class 1) might receive structured opportunities to compare their performance with and without AI support, making AI benefit tangible. Steady and Strong Calibrators (Classes 2 and 3) appear to be on productive calibration trajectories already; interventions should be supportive rather than directive — maintaining the conditions that facilitate ongoing calibration while monitoring for signs of over-reliance.

*The stagnant non-engagers* (Class 4, 9.9%) present a different design challenge. These high performers may benefit from challenges beyond their current level, where AI recommendations become more relevant, or from meta-awareness interventions that help them recognize situations where AI support could enhance performance on novel or especially difficult material.

*The at-risk trajectories* (Classes 5, 6, and ABE) each warrant distinct monitoring strategies. Heavy Adopters (Class 5) could benefit from periodic prompts to attempt questions independently before viewing AI recommendations. Early Heavy Users (Class 6), given their self-correcting trajectory, may need minimal intervention — though understanding why they arrived with high initial reliance could inform onboarding design. ABE learners require perhaps the most targeted support: not encouragement to use AI more, but transparency dashboards and periodic A/B comparisons between AI-selected and self-selected question outcomes that close the awareness gap underlying their pattern. These learners are not simply ignoring the AI — they may be operating on outdated mental models of the AI's utility.

More broadly, these findings argue for calibration-aware instructional design — an approach that moves beyond binary AI-on/AI-off decisions to consider how different learners interact with AI support over time. Appropriate reliance is not a single target state but a moving relationship — each learner's optimal AI engagement shifts as their performance and the system's recommendation quality evolve together. Educational systems should be designed to support this diversity rather than enforce a single model of AI interaction (Long & Magerko, 2020).

### 5.9 The Early Detection Opportunity

The finding that early explanation-seeking behavior predicts trajectory class membership with approximately three times chance accuracy has practical significance for adaptive educational systems. Within the first decile of a learner's engagement — which may correspond to only a few sessions — behavioral indicators are already informative about the student's likely long-term calibration trajectory.

This early predictability opens a window for proactive intervention. AI tutoring platforms could monitor early exploration and explanation engagement patterns, flagging students whose early behavior profiles suggest trajectories associated with suboptimal outcomes (e.g., persistent under-reliance with low improvement). Adaptive scaffolds could then be deployed early, before maladaptive patterns become entrenched.

However, the 49.4% accuracy — while substantially above chance — also means that over half of students would be misclassified by early behavior alone. This limits the confidence with which early intervention decisions can be made and argues for continuous monitoring and classification updating rather than a single early-stage classification decision.

### 5.10 Limitations

Five limitations qualify the interpretation of these findings.

The most fundamental limitation is that this study observed behavioral reliance patterns without access to the underlying cognitive processes of trust formation, judgment, or decision-making. The trajectory classes are defined by observable behavior, and the interpretations offered regarding trust, metacognition, and calibration processes remain inferential. Future research should combine behavioral log data with direct assessments of trust and metacognition.

All data come from a single AI tutoring platform (Santa) in a single educational domain (TOEIC preparation) with a specific student population (Korean learners). The extent to which these findings generalize to other platforms, domains, age groups, and cultural contexts is unknown. Cross-platform and cross-cultural replication is needed.

Behavioral reliance was operationalized as the proportion of adaptive offer episodes, a platform-specific measure that reflects the Santa app's particular recommendation delivery mechanism. Different operationalizations (e.g., acceptance of specific recommendations, time allocated to AI-recommended content) might yield different trajectory patterns. The $R_b$ measure is also bounded by the platform's adaptive offer frequency — students cannot exhibit high $R_b$ if the system rarely offers adaptive content.

The severe zero-inflation in $R_b$ necessitated a shift from the planned longitudinal GMM (via `lcmm`) to a wide-format MBC (via `mclust`) for the primary analysis. While the `mclust` approach effectively identified trajectory classes, it does not model individual-level growth parameters and may be less sensitive to within-class trajectory variation than a true longitudinal mixed model.

The LCGA analysis, while providing a complementary longitudinal perspective, has its own limitations. The analysis was conducted on a subsample of N = 3,204 students (those with at least 7 valid $P_{\text{adaptive}}$ windows), which may not be fully representative of the broader sample. The linear growth specification may not capture nonlinear calibration dynamics, and the fixed-to-zero within-class variance assumption (inherent in LCGA as opposed to full GMM) may overstate between-class heterogeneity. Convergence was achieved for all models up to $G$ = 5, but entropy values were not available for the 4- and 5-class solutions, limiting one dimension of model evaluation.

The use of 10 decile-based windows imposes a relatively coarse temporal resolution that may obscure finer-grained dynamics. The windows are also defined by episode count rather than calendar time, meaning that a window may span different real-time durations for different students.

The study is entirely observational. The associations between trajectory class and outcomes cannot support causal claims. Students who followed convergent calibration trajectories may have done so because of characteristics (e.g., motivation, metacognitive skill) that independently caused both the calibration pattern and the learning gains.

### 5.11 Future Research Directions

Four empirical questions follow directly from these findings.

The trust-in-automation literature predicts hysteresis effects — trust builds slowly but erodes quickly following failures (Muir & Moray, 1996). Testing whether reliance calibration trajectories show similar asymmetric dynamics in educational contexts would bridge the human factors and educational technology literatures. This could be examined using event-level analysis within the EdNet data, examining reliance changes following incorrect AI recommendations. The ABE pattern discovered in this study is particularly relevant to hysteresis testing, as it may represent a case in which trust recovery lags behind improving AI performance.

Replicating this analysis across different AI tutoring platforms, educational domains, and student populations is essential for establishing the generalizability of the trajectory typology. Datasets from platforms such as Khan Academy, Duolingo, or ALEKS could provide comparative evidence. Of particular interest would be replication of the ABE pattern, which, if confirmed across contexts, would warrant its formal incorporation into trust calibration theory.

A critical gap remains between behavior and cognition. No study has yet paired fine-grained behavioral log analysis with concurrent trust and metacognition measurement in educational AI contexts. Combining the behavioral trajectories identified here with periodic self-report trust assessments, cognitive load measures, and potentially eye-tracking data would enable direct testing of the trust-to-reliance pathway hypothesized in Section 5.6.

The class-specific intervention recommendations offered in this study remain speculative. Experimental studies testing targeted interventions for different trajectory classes (e.g., trust calibration scaffolds for Gradual Adopters, AI benefit visibility features for ABE learners, independent practice prompts for Heavy Adopters) would provide evidence on the practical utility of trajectory classification.

Finally, implementing the early detection approach discussed in Section 5.9 would require online algorithms that classify students into trajectory types in real-time, updating classification as more behavioral data accumulates.

---

## 6. Conclusion

The behavioral record examined here — 4,568 learners across thousands of learning episodes — offers the first person-centered test of trust calibration trajectory theory in a deployed educational AI system. Two complementary analytical methods, model-based clustering and latent class growth analysis, converge on key findings: learners exhibit substantial heterogeneity in their calibration dynamics, with both convergent and stagnant patterns predicted by trust-in-automation theory observable in behavioral data.

The findings demonstrate that learners are not homogeneous in how they calibrate their reliance on AI recommendations. Some learners gradually adopt AI support and show convergent calibration dynamics associated with learning gains. Others maintain high performance with consistently low reliance, exhibiting stagnant calibration that, while effective, may limit future growth opportunities. Still others rapidly escalate reliance without proportional performance benefits, warranting monitoring for potential over-reliance.

The discovery of the AI Benefit Emergence pattern extends the theoretical framework by identifying a fifth trajectory type not predicted by the original theory. ABE learners — found by both MBC and LCGA — experience increasing AI effectiveness but fail to update their reliance accordingly, reflecting the trust asymmetry and hysteresis dynamics well-documented in the automation literature but previously undemonstrated in educational contexts. This pattern carries specific implications for educational AI design: systems should not merely improve their recommendations but also communicate their improving effectiveness to learners.

Crucially, early explanation-seeking behavior — a proxy for metacognitive engagement with AI-provided content — emerged as the strongest predictor of long-term calibration trajectories. This finding underscores the importance of how learners interact with AI systems, not merely whether they do so. The depth of engagement with AI-provided explanations, rather than the mere frequency of AI recommendation acceptance, appears to distinguish productive calibration trajectories from less adaptive ones.

These results contribute to the growing literature on trust and reliance in AI-assisted education by moving beyond cross-sectional and population-average approaches to reveal the heterogeneous, dynamic processes through which learners develop their relationships with AI systems. The convergence of findings across two complementary analytical methods strengthens confidence in the robustness of the identified trajectory types and provides behavioral evidence for trust calibration trajectory theory. As AI becomes increasingly integral to educational practice, understanding and supporting the development of appropriate reliance becomes not merely a technical optimization problem but an educational imperative — one that requires attention to the diverse trajectories that learners follow and the early signals that can inform timely, targeted support.

---

## CRediT Author Statement

**Hosung You:** Conceptualization, Methodology, Software, Formal Analysis, Investigation, Data Curation, Writing -- Original Draft, Writing -- Review & Editing, Visualization.

## Declaration of Competing Interest

The author declares that there are no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Declaration of Generative AI and AI-assisted Technologies in the Writing Process

During the preparation of this work, the author used Claude (Anthropic) to assist with data analysis scripting, figure generation, and manuscript drafting. The author reviewed and edited all AI-generated content and takes full responsibility for the content of the published article.

## Data Availability

This study used the publicly available EdNet KT3 dataset (Choi et al., 2020), accessible at https://github.com/riiid/ednet. Analysis code and derived datasets are available in the supplementary materials.

## Acknowledgments

The author thanks the Riiid AI Research team for making the EdNet dataset publicly available.

---

## References

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys, 55*(11), 1--37. https://doi.org/10.1145/3569576

Aleven, V., Stahl, E., Schworm, S., Fischer, F., & Wallace, R. (2003). Help seeking and help design in interactive learning environments. *Review of Educational Research, 73*(3), 277--320. https://doi.org/10.3102/00346543073003277

Aleven, V., Roll, I., McLaren, B. M., & Koedinger, K. R. (2016). Help helps, but only so much: Research on help seeking with intelligent tutoring systems. *International Journal of Artificial Intelligence in Education, 26*(1), 205--223. https://doi.org/10.1007/s40593-015-0089-1

Baker, R. S. J. d., Corbett, A. T., & Koedinger, K. R. (2004). Detecting student misuse of intelligent tutoring systems. In J. C. Lester, R. M. Vicari, & F. Paraguacu (Eds.), *Intelligent Tutoring Systems* (pp. 531--540). Springer.

Baker, R. S. J. d., Corbett, A. T., Koedinger, K. R., & Wagner, A. Z. (2004). Off-task behavior in the cognitive tutor classroom: When students "game the system." In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 383--390). ACM.

Baker, R. S. J. d., Corbett, A. T., Roll, I., & Koedinger, K. R. (2008). Developing a generalizable detector of when students game the system. *User Modeling and User-Adapted Interaction, 18*(3), 287--314. https://doi.org/10.1007/s11257-007-9045-6

Baker, R. S. J. d., D'Mello, S. K., Rodrigo, M. M. T., & Graesser, A. C. (2010). Better to be frustrated than bored: The incidence, persistence, and impact of learners' cognitive-affective states during interactions with three different computer-based learning environments. *International Journal of Human-Computer Studies, 68*(4), 223--241. https://doi.org/10.1016/j.ijhcs.2009.12.003

Baidoo-Anu, D., & Ansah, L. O. (2023). Education in the era of generative artificial intelligence (AI): Understanding the potential benefits of ChatGPT in promoting teaching and learning. *Journal of AI, 7*(1), 52--62. https://doi.org/10.61969/jai.1337500

Bauer, D. J., & Curran, P. J. (2003). Distributional assumptions of growth mixture models: Implications for overextraction of latent trajectory classes. *Psychological Methods, 8*(3), 338--363. https://doi.org/10.1037/1082-989X.8.3.338

Boscardin, C. K., Muthen, B., Francis, D. J., & Baker, E. L. (2008). Early identification of reading difficulties using heterogeneous developmental trajectories. *Journal of Educational Psychology, 100*(1), 192--208. https://doi.org/10.1037/0022-0663.100.1.192

Broadbent, J., & Poon, W. L. (2015). Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review. *The Internet and Higher Education, 27*, 1--13. https://doi.org/10.1016/j.iheduc.2015.04.007

Chen, J. Y. C., Procci, K., Boyce, M., Wright, J., Garcia, A., & Barnes, M. (2014). *Situation awareness-based agent transparency* (ARL-TR-6905). U.S. Army Research Laboratory.

Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., ... & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Proceedings of the 21st International Conference on Artificial Intelligence in Education* (pp. 69--73). Springer. https://doi.org/10.1007/978-3-030-52240-7_13

Choudhury, A., Asan, O., & Bayrak, A. E. (2020). Artificial intelligence and human trust in healthcare: Focus on clinicians. *Journal of Medical Internet Research, 22*(6), e15154. https://doi.org/10.2196/15154

Crompton, H., & Burke, D. (2023). Artificial intelligence in higher education: The state of the field. *International Journal of Educational Technology in Higher Education, 20*(1), 22. https://doi.org/10.1186/s41239-023-00392-8

de Visser, E. J., Peeters, M. M., Jung, M. F., Kohn, S., Shaw, T. H., Pak, R., & Neerincx, M. A. (2020). Towards a theory of longitudinal trust calibration in human--robot teams. *International Journal of Social Robotics, 12*, 459--478. https://doi.org/10.1007/s12369-019-00596-x

du Boulay, B. (2016). Artificial intelligence as an effective classroom assistant. *IEEE Intelligent Systems, 31*(6), 76--81. https://doi.org/10.1109/MIS.2016.93

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The role of trust in automation reliance. *International Journal of Human-Computer Studies, 58*(6), 697--718. https://doi.org/10.1016/S1071-5819(03)00038-7

Fraley, C., & Raftery, A. E. (2002). Model-based clustering, discriminant analysis, and density estimation. *Journal of the American Statistical Association, 97*(458), 611--631. https://doi.org/10.1198/016214502760047131

Ghosh, A., Heffernan, N., & Lan, A. S. (2020). Context-aware attentive knowledge tracing. In *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2330--2339). https://doi.org/10.1145/3394486.3403282

Holmes, W., Bialik, M., & Fadel, C. (2019). *Artificial intelligence in education: Promises and implications for teaching and learning*. Center for Curriculum Redesign.

Jian, J. Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics, 4*(1), 53--71. https://doi.org/10.1207/S15327566IJCE0401_04

Kasneci, E., Sessler, K., Kuechemann, S., Bannert, M., Dementieva, D., Fischer, F., ... & Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences, 103*, 102274. https://doi.org/10.1016/j.lindif.2023.102274

Kaur, H., Nori, H., Jenkins, S., Caruana, R., Wallach, H., & Wortman Vaughan, J. (2020). Interpreting interpretability: Understanding data scientists' use of interpretability tools for machine learning. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1--14). ACM. https://doi.org/10.1145/3313831.3376219

Korber, M. (2019). Theoretical considerations and development of a questionnaire to measure trust in automation. In S. Bagnara et al. (Eds.), *Proceedings of the 20th Congress of the International Ergonomics Association* (pp. 13--30). Springer.

Lee, J. D., & Moray, N. (1994). Trust, self-confidence, and operators' adaptation to automation. *International Journal of Human-Computer Studies, 40*(1), 153--184. https://doi.org/10.1006/ijhc.1994.1007

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50--80. https://doi.org/10.1518/hfes.46.1.50.30392

Loibl, K., & Rummel, N. (2014). Knowing what you don't know makes failure productive. *Learning and Instruction, 34*, 74--85. https://doi.org/10.1016/j.learninstruc.2014.08.004

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1--16). ACM. https://doi.org/10.1145/3313831.3376727

Muir, B. M. (1994). Trust in automation: Part I. Theoretical issues in the study of trust and human intervention in automated systems. *Ergonomics, 37*(11), 1905--1922. https://doi.org/10.1080/00140139408964957

Muir, B. M., & Moray, N. (1996). Trust in automation: Part II. Experimental studies of trust and human intervention in a process control simulation. *Ergonomics, 39*(3), 429--460. https://doi.org/10.1080/00140139608964474

Mollick, E. R., & Mollick, L. (2023). Using AI to implement effective teaching strategies in classrooms: Five strategies, including prompts. *The Wharton School Research Paper*. https://doi.org/10.2139/ssrn.4391243

Musu-Gillette, L. E., Wigfield, A., Harring, J. R., & Eccles, J. S. (2015). Trajectories of change in students' self-concepts of ability and values in math and college major choice. *Educational Research and Evaluation, 21*(4), 343--370. https://doi.org/10.1080/13803611.2015.1057161

Muthen, B. (2004). Latent variable analysis: Growth mixture modeling and related techniques for longitudinal data. In D. Kaplan (Ed.), *The SAGE handbook of quantitative methodology for the social sciences* (pp. 345--368). SAGE.

Nagin, D. S. (2005). *Group-based modeling of development*. Harvard University Press.

Nagin, D. S., & Land, K. C. (1993). Age, criminal careers, and population heterogeneity: Specification and estimation of a nonparametric, mixed Poisson model. *Criminology, 31*(3), 327--362. https://doi.org/10.1111/j.1745-9125.1993.tb01133.x

Nazaretsky, T., Ariely, M., Cukurova, M., & Alexandron, G. (2022). Teachers' trust in AI-powered educational technology and a professional development program to improve it. *British Journal of Educational Technology, 53*(4), 914--931. https://doi.org/10.1111/bjet.13232

Nylund, K. L., Asparouhov, T., & Muthen, B. O. (2007). Deciding on the number of classes in latent class analysis and growth mixture modeling: A Monte Carlo simulation study. *Structural Equation Modeling, 14*(4), 535--569. https://doi.org/10.1080/10705510701575396

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381--410. https://doi.org/10.1177/0018720810376055

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230--253. https://doi.org/10.1518/001872097778543886

Proust-Lima, C., Philipps, V., & Liquet, B. (2017). Estimation of extended mixed models using latent classes and latent processes: The R package lcmm. *Journal of Statistical Software, 78*(2), 1--56. https://doi.org/10.18637/jss.v078.i02

Ram, N., & Grimm, K. J. (2009). Growth mixture modeling: A method for identifying differences in longitudinal change among unobserved groups. *International Journal of Behavioral Development, 33*(6), 565--576. https://doi.org/10.1177/0165025409343765

Roll, I., Aleven, V., McLaren, B. M., & Koedinger, K. R. (2011). Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system. *Learning and Instruction, 21*(2), 267--280. https://doi.org/10.1016/j.learninstruc.2010.07.004

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist, 55*(1), 68--78. https://doi.org/10.1037/0003-066X.55.1.68

Schemmer, M., Kuehl, N., Benz, C., Bartos, A., & Satzger, G. (2023). Appropriate reliance on AI advice: Conceptualization and the effect of explanations. In *Proceedings of the 28th International Conference on Intelligent User Interfaces* (pp. 410--422). ACM. https://doi.org/10.1145/3581641.3584066

Scrucca, L., Fop, M., Murphy, T. B., & Raftery, A. E. (2016). mclust 5: Clustering, classification and density estimation using Gaussian finite mixture models. *The R Journal, 8*(1), 289--317. https://doi.org/10.32614/RJ-2016-021

Shin, D., Shim, Y., Yu, H., Lee, S., Kim, B., & Choi, Y. (2021). SAINT+: Integrating temporal features for EdNet correctness prediction. In *LAK21: 11th International Learning Analytics and Knowledge Conference* (pp. 490--496). ACM. https://doi.org/10.1145/3448139.3448188

Siau, K., & Wang, W. (2018). Building trust in artificial intelligence, machine learning, and robotics. *Cutter Business Technology Journal, 31*(2), 47--53.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124--1131. https://doi.org/10.1126/science.185.4157.1124

UNESCO. (2023). *Guidance for generative AI in education and research*. United Nations Educational, Scientific and Cultural Organization. https://doi.org/10.54675/EWZM9535

VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197--221. https://doi.org/10.1080/00461520.2011.611369

Zawacki-Richter, O., Marin, V. I., Bond, M., & Gouverneur, F. (2019). Systematic review of research on artificial intelligence applications in higher education -- where are the educators? *International Journal of Educational Technology in Higher Education, 16*(1), 39. https://doi.org/10.1186/s41239-019-0171-0

---

## Appendix A: Supplementary Materials

### A.1 R Code Availability

All R code used for data processing, model-based clustering (mclust), latent class growth analysis (lcmm), multinomial logistic regression, and ANOVA analyses is available in the supplementary materials accompanying this article.

### A.2 LCGA Model Fit Details

Detailed model fit statistics for all LCGA solutions (G = 1 through G = 7), including log-likelihood values, number of parameters, BIC, AIC, and entropy (where available), are provided in Supplementary Table S1. Convergence diagnostics, including the number of random starts that converged to the best solution for each G, are provided in Supplementary Table S2. Class-specific growth parameter estimates (intercepts and slopes) with standard errors for the optimal 4-class solution are provided in Supplementary Table S3.

---

*Manuscript word count: approximately 12,500 words (excluding references and appendices)*
