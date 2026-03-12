# Patterns of AI Reliance Calibration Among Learners: A Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System

**Authors:** [AUTHORS TBD]

**Target Journal:** Computers & Education / British Journal of Educational Technology

**Date:** March 2026

**Status:** Draft v1

---

## Abstract

As artificial intelligence (AI) becomes increasingly embedded in educational systems, understanding how learners calibrate their reliance on AI recommendations remains a critical yet understudied phenomenon. This study investigates longitudinal patterns of AI reliance calibration among learners using a large-scale AI tutoring platform. Drawing on trust-in-automation theory (Lee & See, 2004) and the concept of appropriate reliance (Schemmer et al., 2023), we operationalize reliance calibration as the evolving alignment between behavioral AI reliance and task performance over time. Using data from 4,568 students in the EdNet KT3 dataset (Choi et al., 2020), we applied Gaussian Mixture Modeling (GMM) to identify distinct trajectory classes across 10 temporal windows spanning each learner's usage history. Six trajectory classes emerged: Gradual Adopters (29.9%), Steady Calibrators (34.6%), Strong Calibrators (18.8%), High Performers with Low Reliance (9.9%), Heavy Adopters (5.3%), and Early Heavy Users (1.5%). These classes exhibited meaningfully different patterns of reliance-performance alignment, with convergent calibration trajectories (Classes 2 and 3) showing the greatest performance improvement over time, while the highest-performing class (Class 4) maintained stable but low AI reliance. Multinomial logistic regression revealed that early explanation-seeking behavior was the strongest predictor of trajectory class membership (|coefficient| = 1.00), achieving 49.4% classification accuracy (approximately three times chance level). These findings provide the first large-scale empirical evidence of heterogeneous reliance calibration trajectories in AI-assisted learning, offering a behavioral foundation for the theoretical construct of trust calibration and suggesting pathways for adaptive, class-specific pedagogical interventions.

**Keywords:** reliance calibration, trust in AI, AI tutoring systems, growth mixture modeling, learner trajectories, appropriate reliance, educational technology

---

## 1. Introduction

### 1.1 The Promise and Peril of AI in Education

Artificial intelligence has rapidly transformed the educational landscape, with AI-powered tutoring systems, adaptive learning platforms, and intelligent recommendation engines now serving millions of learners worldwide (Holmes et al., 2022; Zawacki-Richter et al., 2019). These systems promise personalized learning experiences by adapting content difficulty, pacing, and instructional strategies to individual learner characteristics (VanLehn, 2011). Yet the effectiveness of such systems depends not only on the quality of their recommendations but also on how learners interact with and respond to AI-generated guidance (Nazaretsky et al., 2022).

A fundamental challenge emerges at this intersection: learners must develop an appropriate level of reliance on AI recommendations — neither blindly following every suggestion nor categorically ignoring potentially beneficial guidance. This challenge parallels a well-documented problem in human factors research known as the calibration of trust in automation (Lee & See, 2004; Parasuraman & Riley, 1997). When human operators over-trust automated systems, they may fail to detect errors; when they under-trust, they forfeit the benefits of automation. The same dynamics apply in educational contexts, where miscalibrated reliance on AI tutoring can undermine learning outcomes (Kaur et al., 2022).

### 1.2 Reliance Calibration as a Behavioral Construct

A critical distinction must be drawn between *trust* and *reliance*. Following Lee and See's (2004) seminal framework, trust is an attitude — a psychological state reflecting the willingness to be vulnerable to the actions of an automated agent based on the expectation that it will perform a particular action important to the trustor. Reliance, by contrast, is a behavior — the observable act of depending on the automated system's output in decision-making. Trust *guides* reliance, but the two are not isomorphic: a learner may trust an AI system yet choose not to rely on it for strategic reasons, or may rely on it out of convenience without genuine trust.

This distinction carries important methodological implications. Measuring trust requires access to cognitive and affective states, typically assessed through self-report instruments (e.g., Jian et al., 2000; Körber, 2019). Measuring reliance, however, requires only behavioral observation — the degree to which individuals accept, follow, or depend on system recommendations. In large-scale educational datasets where self-report data are unavailable, behavioral reliance becomes the accessible and appropriate construct.

We therefore adopt the term *reliance calibration* to describe the phenomenon under investigation: the degree to which a learner's behavioral reliance on AI recommendations aligns with their actual performance level over time. This framing is consistent with Schemmer et al.'s (2023) conceptualization of appropriate reliance as a behavioral outcome of trust calibration processes, and with de Visser et al.'s (2020) emphasis on the dynamic, evolving nature of human-automation trust relationships.

### 1.3 Conceptual Framework

This study is situated within a broader research program on trust calibration in AI-assisted learning. The conceptual foundation draws on two key frameworks.

First, the *Trust-Reliability Matrix* conceptualizes the alignment space between a learner's reliance on AI and the system's actual reliability [Figure 1]. When reliance matches reliability, calibration is achieved. Deviations in either direction — over-reliance (reliance exceeds reliability) or under-reliance (reliance falls below reliability) — represent miscalibration. This matrix provides a static snapshot of calibration states.

Second, we extend this framework into a dynamic, longitudinal perspective by modeling reliance calibration as a trajectory through a three-dimensional space defined by behavioral reliance ($R_b$), performance ($P$), and time ($\tau$) [Figure 2]. Within this $R_b \times P \times \tau$ space, different trajectory shapes correspond to different calibration dynamics: convergent trajectories (where the gap between $R_b$ and $P$ narrows), divergent trajectories (where the gap widens), oscillating trajectories (where the gap fluctuates), and stagnant trajectories (where the gap remains constant). These theoretically predicted trajectory shapes serve as referents against which empirically observed patterns can be compared.

### 1.4 The Research Gap

Despite growing interest in trust and reliance on AI in educational settings (Nazaretsky et al., 2022; Siau & Wang, 2018), empirical research on how learners' reliance patterns evolve over time remains sparse. Most existing studies adopt cross-sectional designs, measuring trust or reliance at a single point (or at best, pre-post), and treat learner populations as homogeneous (Kaur et al., 2022). Three specific gaps motivate this study.

First, there is a lack of *longitudinal trajectory* studies examining how reliance calibration unfolds across extended learning episodes. Trust and reliance are inherently dynamic (Lee & See, 2004), yet the temporal evolution of these constructs in educational AI contexts has received limited empirical attention.

Second, there is a lack of *person-centered* approaches that acknowledge heterogeneity in calibration trajectories. Variable-centered methods (e.g., regression) estimate average effects but mask meaningful subgroup differences. Growth mixture modeling (GMM) and related latent class approaches can uncover qualitatively distinct trajectory classes within seemingly homogeneous populations (Nagin, 2005; Ram & Grimm, 2009).

Third, there is a disconnect between theoretical predictions about calibration dynamics and empirical evidence. While frameworks predict various trajectory shapes (convergent, divergent, oscillating, stagnant), no study has systematically tested whether these patterns emerge in real-world learner data.

### 1.5 Research Questions and Hypotheses

This study addresses four research questions:

**RQ1:** How many distinct reliance calibration trajectory classes can be identified among learners using an AI tutoring system, and what characterizes each class?

**RQ2:** To what extent do the empirically observed trajectory classes correspond to theoretically predicted calibration patterns (convergent, divergent, oscillating, stagnant)?

**RQ3:** Can early learning behaviors predict subsequent trajectory class membership?

**RQ4:** Do trajectory classes differ in learning outcomes (overall accuracy and accuracy improvement)?

Based on the theoretical framework and prior literature, we advance the following hypotheses:

- **H1:** At least three distinct reliance calibration trajectory classes will emerge, reflecting heterogeneity in how learners calibrate their AI reliance over time.
- **H2a:** At least one class will exhibit a convergent calibration pattern, with the reliance-performance gap narrowing toward zero.
- **H2b:** At least one class will exhibit an oscillating pattern, with the gap fluctuating across time windows.
- **H2c:** At least one class will exhibit a stagnant pattern, with the gap remaining relatively constant.
- **H3:** Early explanation-seeking behavior (a proxy for metacognitive engagement) will significantly predict trajectory class membership.
- **H4:** Convergent calibration trajectories will be associated with the best learning outcomes, reflecting the theoretical advantage of calibrated reliance.

### 1.6 Contribution

This study makes three primary contributions. First, it provides the first large-scale, person-centered analysis of reliance calibration trajectories in AI-assisted learning, moving beyond cross-sectional and population-average approaches. Second, it offers an empirical test of theoretically predicted calibration dynamics, grounding abstract frameworks in behavioral data. Third, it identifies early behavioral markers that predict long-term calibration patterns, offering practical implications for early detection and adaptive intervention in AI tutoring systems. This paper constitutes the fourth study in a programmatic research effort on trust calibration in AI-assisted education, building on a systematic literature review (Paper 1), a psychometric instrument development study (Paper 2), and a conceptual framework paper (Paper 3). While Papers 1 through 3 established the theoretical and measurement foundations, this paper contributes empirical behavioral evidence, serving as a behavioral consistency check examining whether the patterns predicted by the conceptual framework are observable in large-scale learning data.

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

### 2.3 Growth Mixture Modeling in Educational Research

Growth mixture modeling (GMM; Muthén, 2004; Nagin, 2005) and the related group-based trajectory modeling approach (Nagin & Land, 1993) have become increasingly popular in educational research for identifying latent subgroups that follow qualitatively distinct developmental trajectories. Unlike traditional growth curve models that assume a single population trajectory with individual variation around the mean, GMM allows for the possibility of multiple latent classes, each with its own trajectory parameters.

In educational contexts, GMM and its variants have been applied to study diverse phenomena including reading development (Boscardin et al., 2008), mathematics learning trajectories (Musu-Gillette et al., 2015), engagement patterns in online learning (Guo & Yang, 2021), and self-regulated learning processes (Broadbent & Poon, 2015). These studies consistently demonstrate that treating learner populations as homogeneous obscures meaningful subgroup differences that carry implications for intervention design.

Methodologically, GMM in educational research faces several challenges including model selection (determining the optimal number of classes), class assignment uncertainty (entropy and posterior probability diagnostics), and the risk of extracting spurious classes driven by non-normality rather than genuine subgroups (Bauer & Curran, 2003). Best practices recommend combining statistical fit indices (BIC, AIC, entropy) with substantive interpretability and theoretical grounding when determining the number of classes (Nylund et al., 2007; Ram & Grimm, 2009).

### 2.4 AI Tutoring Systems and Learner Behavior Research

Intelligent tutoring systems (ITS) have a decades-long history of research demonstrating their effectiveness for personalized learning (VanLehn, 2011; du Boulay, 2016). More recent AI-powered tutoring platforms leverage knowledge tracing algorithms, collaborative filtering, and deep learning to adaptively recommend content to learners (Abdelrahman et al., 2023). Research on learner behavior within these systems has examined patterns of help-seeking (Aleven et al., 2003), hint usage (Baker et al., 2008), persistence and disengagement (Baker et al., 2010), and strategic behavior (Baker et al., 2004).

The EdNet dataset (Choi et al., 2020) represents one of the largest publicly available educational datasets, comprising interaction logs from the Santa AI tutoring platform for standardized test preparation in South Korea. Studies using EdNet have examined knowledge tracing algorithms (Ghosh et al., 2020), question difficulty estimation (Choi et al., 2020), and adaptive learning system design (Shin et al., 2021). However, no prior study has used EdNet — or any comparable large-scale dataset — to examine reliance calibration trajectories.

The current study addresses this gap by applying mixture modeling to longitudinal patterns of AI reliance and performance in the EdNet dataset, bringing together trust-in-automation theory, person-centered statistical methods, and large-scale educational data analytics.

---

## 3. Method

### 3.1 Data Source

This study used the EdNet KT3 dataset (Choi et al., 2020), a large-scale educational interaction log from the Santa AI tutoring application. Santa is a mobile-based AI tutoring platform designed to help Korean students prepare for the Test of English for International Communication (TOEIC). The platform uses a knowledge tracing algorithm combined with collaborative filtering to generate adaptive recommendations for practice questions and explanatory content. The KT3 variant of the dataset includes detailed interaction-level data encompassing question-answering episodes, adaptive content recommendations (tagged as `adaptive_offer`), explanation-viewing behavior, timestamps, and correctness indicators.

The full KT3 dataset contains records from 297,915 unique students. The dataset is publicly available and has been widely used in educational data mining research (Choi et al., 2020). Because the data were collected as de-identified system logs from a commercial platform, individual informed consent was not required; the dataset was released by the platform developers under a research license.

### 3.2 Participants and Filtering Criteria

From the initial pool of 297,915 students, we applied a series of filtering criteria designed to ensure sufficient data density for longitudinal trajectory analysis while retaining students who meaningfully engaged with the AI adaptive recommendation system. The filtering criteria and their rationale were as follows:

1. **Adaptive offer engagement ratio >= 0.10.** Students were required to have at least 10% of their total episodes classified as `adaptive_offer` interactions. This threshold ensured that included students had meaningful exposure to the AI recommendation system, as students with negligible adaptive engagement could not exhibit meaningful reliance calibration patterns. The 10% threshold was chosen to balance inclusivity with analytical validity.

2. **Minimum 60 total episodes.** Students were required to have completed at least 60 learning episodes across their entire usage history. This minimum ensured sufficient data points for dividing the usage history into 10 temporal windows (see Section 3.4), with at least 6 episodes per window on average.

3. **Minimum 5 adaptive episodes.** Beyond the ratio criterion, students were required to have at least 5 absolute adaptive offer episodes. This floor ensured that the behavioral reliance measure ($R_b$) was based on a non-trivial number of AI recommendation interactions.

4. **Minimum 1 day of platform usage.** Students were required to have used the platform across at least 1 calendar day. This criterion excluded students whose entire usage history occurred within a single brief session, which would not permit meaningful longitudinal analysis.

After applying all four filters, the analytic sample comprised **N = 4,568** students.

### 3.3 Variables

#### 3.3.1 Temporal Windows

Each student's complete episode sequence was divided into 10 non-overlapping temporal windows based on deciles of their individual episode count. That is, for a student with 100 episodes, window 1 ($\tau = 1$) comprised episodes 1–10, window 2 ($\tau = 2$) comprised episodes 11–20, and so on through window 10 ($\tau = 10$). This within-person normalization ensured that all students were represented on a common temporal scale regardless of differences in total usage volume, facilitating comparison of trajectory shapes across students with different engagement levels.

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

#### 3.3.5 Early Behavior Features (for RQ3)

To investigate whether early behavior predicted subsequent trajectory class membership (RQ3), we extracted several features from the first temporal window ($\tau = 1$) and, where applicable, from the first two windows ($\tau = 1, 2$):

- **Early reliance rate** (`early_R_b`): $R_b(\tau = 1)$, the proportion of adaptive episodes in the first window.
- **Early exploration rate** (`early_expl_rate`): the proportion of episodes in the first window where the student viewed explanatory content following a question attempt. This variable serves as a proxy for metacognitive engagement, as explanation-seeking behavior reflects a disposition to understand underlying reasoning rather than merely attempting and moving on.
- **Early average explanation duration** (`early_avg_expl_dur_s`): the mean time (in seconds) that students spent viewing explanation content in the first window. Longer durations may indicate deeper processing of explanatory material.
- **Early performance** (`early_P`): $P(\tau = 1)$, accuracy in the first window.

#### 3.3.6 Outcome Variables (for RQ4)

Two outcome variables were computed for examining class differences in learning outcomes:

- **Overall accuracy**: the proportion of correctly answered questions across the student's entire episode history.
- **Accuracy improvement**: computed as $P(\tau = 10) - P(\tau = 1)$, capturing the change in performance from the first to the last temporal window.

### 3.4 Analytical Approach

#### 3.4.1 Phase 1: Data Preparation

The filtered dataset (N = 4,568) was processed to compute the 10-window time series for each student. For each student, the episode sequence was divided into decile-based windows, and $R_b(\tau)$ and $P(\tau)$ were computed within each window. This yielded a wide-format dataset with 20 features per student: $R_b(1), R_b(2), \ldots, R_b(10), P(1), P(2), \ldots, P(10)$.

#### 3.4.2 Phase 2: Gaussian Mixture Modeling (RQ1, RQ2)

To identify distinct trajectory classes, we employed Gaussian Mixture Modeling (GMM) using the `mclust` package (Scrucca et al., 2016) in R. The choice of GMM over the originally planned latent class mixed model via the `lcmm` package (Proust-Lima et al., 2017) was driven by empirical necessity: the planned parametric-process GMM (PP-GMM) models failed to converge due to the severe zero-inflation in the $R_b$ variable. Many students had $R_b = 0$ in early windows, creating a point mass at zero that violated the distributional assumptions of the `lcmm` mixed-effects framework. The wide-format GMM approach via `mclust` does not require specifying a parametric growth function and accommodates non-standard distributions more flexibly, albeit at the cost of not modeling individual-level random effects.

The `mclust` algorithm performs model-based clustering by fitting a finite mixture of Gaussian distributions to the multivariate data. It simultaneously estimates the number of components (classes), the component means and covariance structures, and the posterior class membership probabilities for each observation. The algorithm evaluates 14 different parameterizations of the covariance matrix (ranging from spherical to unconstrained) across a range of class numbers (1 through $K_{\max}$), selecting the optimal model based on the Bayesian Information Criterion (BIC).

**Model selection.** We evaluated models with 1 through 9 classes across all covariance parameterizations supported by `mclust`. The optimal model was selected based on: (a) BIC, where higher values (in `mclust`'s convention) indicate better model fit penalized for complexity; (b) entropy, a measure of classification certainty ranging from 0 (ambiguous) to 1 (certain), computed from the posterior class membership probabilities; and (c) substantive interpretability, following recommendations in the GMM literature (Nylund et al., 2007; Ram & Grimm, 2009).

**Class assignment.** Each student was assigned to the class for which their posterior membership probability was highest (modal assignment). Entropy was computed as:

$$E = 1 - \frac{-\sum_{i=1}^{N}\sum_{k=1}^{K} \hat{p}_{ik} \log(\hat{p}_{ik})}{N \log(K)}$$

where $\hat{p}_{ik}$ is the posterior probability of student $i$ belonging to class $k$.

**Sensitivity analyses.** The robustness of the six-class solution was evaluated through four complementary approaches. First, we compared forced solutions from four to seven classes (all VEE covariance structure). While a seven-class solution yielded a marginally higher BIC (140,115.1 vs. 139,900.6), the six-class solution exhibited superior classification quality: highest entropy (0.824 vs. 0.802), highest ICL (137,011.2 vs. 136,602.6), and no class smaller than 1.7% of the sample. The seven-class solution introduced a 53-student class (1.2%), raising interpretability concerns.

Second, bootstrap likelihood ratio tests (100 replications, VEE model) indicated that each incremental class from two through eight contributed statistically significant improvement (*p* < .01 for all). Because the LRT provided no natural stopping point, we relied on the BIC-ICL-entropy consensus described above to adjudicate among solutions.

Third, a split-half validation procedure randomly divided the sample into two halves (*n* = 2,284 each; seed = 42). Both halves independently selected the same model (VEE, *G* = 6). The mean correlation between matched class centroids across halves was *r* = .970, indicating high replicability of trajectory shapes. The mean cross-validated adjusted Rand index was .503, a moderate but typical value for GMM solutions with overlapping clusters.

Fourth, we examined sensitivity to the adaptive ratio inclusion threshold. At threshold ≥ 0.15 (*n* = 1,193), BIC selected four classes; at ≥ 0.20 (*n* = 300), five classes. In both cases, the smaller sample size reduced statistical power to detect peripheral subgroups (Classes 5 and 6), while core classes remained stable (ARI with original assignments: .44 and .38, respectively). These results suggest that the six-class solution is specific to the ≥ 0.10 threshold but that the major trajectory patterns (Classes 1–4) replicate under stricter criteria.

#### 3.4.3 Phase 3a: Multinomial Logistic Regression (RQ3)

To examine whether early learning behaviors predict trajectory class membership, we fitted a multinomial logistic regression model with the GMM-assigned class as the dependent variable and the early behavior features (`early_R_b`, `early_expl_rate`, `early_avg_expl_dur_s`, `early_P`) as predictors. Model performance was evaluated using 10-fold cross-validation, reporting mean classification accuracy and comparison against chance-level performance (1/6 = 16.7% for six classes). Predictor importance was assessed using the absolute values of standardized coefficients averaged across class contrasts.

#### 3.4.4 Phase 3b: ANOVA with Post-Hoc Comparisons (RQ4)

To examine differences in learning outcomes across trajectory classes, we conducted one-way analyses of variance (ANOVA) with trajectory class as the between-subjects factor and two dependent variables: overall accuracy and accuracy improvement. Effect sizes were reported as eta-squared ($\eta^2$). Post-hoc pairwise comparisons were conducted using Tukey's HSD test with family-wise error rate correction. Given the large sample size (N = 4,568), we emphasize effect sizes alongside statistical significance in interpreting results.

### 3.5 Ethical Considerations

The EdNet dataset is a publicly available, de-identified educational dataset released for research purposes by the platform developers (Choi et al., 2020). No personally identifiable information is present in the dataset. The research protocol was reviewed by [IRB INFORMATION TBD] and was determined to be exempt from full review as it involves secondary analysis of existing de-identified data.

---

## 4. Results

### 4.1 Descriptive Statistics

The analytic sample of 4,568 students exhibited considerable variability in engagement and performance. [Table 1] presents the descriptive statistics for the key variables across the 10 temporal windows.

Across all students and windows, the mean behavioral reliance ($R_b$) was relatively low, reflecting the overall tendency for students to engage more with self-selected content than AI-recommended content. Mean $R_b$ increased from approximately 0.04 in the first window to approximately 0.16 in the tenth window, indicating a general trend toward greater adoption of adaptive content over time. Mean performance ($P$) was more stable, hovering around 0.56–0.58 across windows, with a slight upward trend. The reliance-performance gap was negative across all windows (mean Gap ranging from approximately −0.52 in window 1 to −0.40 in window 10), indicating pervasive under-reliance relative to performance across the sample.

### 4.2 RQ1: Identification of Trajectory Classes

#### 4.2.1 Model Selection

The GMM analysis, conducted using `mclust` on the 20-dimensional wide-format data ($R_b \times 10 + P \times 10$), evaluated models with 1 through 9 classes across all 14 covariance parameterizations. The BIC-based model selection identified a **VEE (variable volume, equal shape, equal orientation) model with 6 classes** as optimal, achieving a BIC of **139,751.3**. The entropy of this solution was **0.82**, indicating good classification certainty.

[Table 2] presents the BIC values for the top competing models. The 6-class VEE model provided the best balance of fit and parsimony. The 5-class and 7-class solutions were also examined; the 5-class solution merged two substantively distinct classes (combining what became Classes 2 and 3), while the 7-class solution split one class into two small and poorly differentiated subgroups. These comparisons supported the substantive interpretability of the 6-class solution.

#### 4.2.2 Description of the Six Trajectory Classes

[Table 3] presents the characteristics of the six identified trajectory classes, and [Figure 3] displays the mean $R_b$ and $P$ trajectories for each class across the 10 temporal windows. [Figure 4] displays the corresponding gap trajectories. Below, we describe each class.

**Class 1: Gradual Adopters (n = 1,367; 29.9%).** This was the second-largest class. Students in this class began with very low AI reliance ($R_b$ increasing from 0.05 in window 1 to 0.14 in window 10) and maintained stable, moderate performance ($P \approx 0.59$ throughout). The reliance-performance gap widened slightly in the positive direction ($\Delta$ Gap = +0.09), reflecting gradually increasing adoption of AI recommendations without corresponding performance change. This class represents learners who progressively warmed to the AI system's recommendations but whose performance neither benefited from nor was harmed by this increasing reliance.

**Class 2: Steady Calibrators (n = 1,582; 34.6%).** This was the largest class. Students began with very low reliance ($R_b = 0.03$) and slightly below-average performance ($P = 0.53$), with both measures increasing steadily over time ($R_b$ to 0.17, $P$ to 0.56). The reliance-performance gap change ($\Delta$ Gap = +0.10) reflected reliance increasing faster than performance, but the concurrent improvement in both variables suggests a calibration process in which increasing reliance co-occurred with learning gains.

**Class 3: Strong Calibrators (n = 859; 18.8%).** Students in this class showed a pattern similar to Class 2 but with more pronounced changes. Starting from low reliance ($R_b = 0.04$) and the lowest initial performance ($P = 0.50$), they exhibited the strongest simultaneous increase in both reliance ($R_b$ to 0.19) and performance ($P$ to 0.54). The gap change ($\Delta$ Gap = +0.11) was the second-largest, yet this class demonstrated the greatest performance improvement of any class (see RQ4 results below). This pattern is consistent with a calibration process in which learners who began struggling increasingly turned to AI recommendations and benefited from doing so.

**Class 4: High Performers with Low Reliance (n = 451; 9.9%).** This class exhibited a distinctive profile: the highest and most stable performance ($P \approx 0.65$) paired with consistently low AI reliance ($R_b$ increasing modestly from 0.06 to 0.11). The gap change was minimal ($\Delta$ Gap = +0.03), reflecting a stagnant calibration trajectory. These students performed well without substantial reliance on AI recommendations, suggesting they either did not need AI support or had alternative learning strategies.

**Class 5: Heavy Adopters (n = 240; 5.3%).** This smaller class showed the highest terminal reliance ($R_b = 0.23$ in window 10) among all classes that began with low reliance. Starting from moderate initial reliance ($R_b = 0.09$) and average performance ($P \approx 0.57$), these students sharply increased their AI reliance while maintaining stable performance. The large gap change ($\Delta$ Gap = +0.13) was the largest of any class, representing an escalating reliance pattern that outpaced any performance gains.

**Class 6: Early Heavy Users (n = 69; 1.5%).** This was the smallest and most distinctive class. Students began with the highest initial reliance ($R_b = 0.33$) — far exceeding all other classes — and their reliance actually *decreased* slightly over time ($R_b$ to 0.29). Performance was moderate and stable ($P \approx 0.59$). The gap change was negative ($\Delta$ Gap = −0.02), the only class showing a declining gap. This class may represent students who arrived with strong prior engagement with AI recommendation systems or who initially over-relied on the system and gradually self-corrected.

### 4.3 RQ2: Theory-Empirical Comparison

The theoretical framework predicted four trajectory shapes: convergent (gap narrowing toward zero), divergent (gap widening from zero), oscillating (gap fluctuating), and stagnant (gap remaining constant) [Figure 2]. We evaluated the empirical classes against these predictions.

**Convergent calibration patterns (H2a: Partially Supported).** Classes 2 (Steady Calibrators) and 3 (Strong Calibrators) best approximated the convergent prediction, showing concurrent increases in both reliance and performance. However, the convergence was partial: the reliance-performance gap narrowed in a relative sense (as the gap was initially very negative, and the increase in $R_b$ brought it closer to alignment), but the gap did not reach zero. The persistent under-reliance (gap remaining negative) suggests that full calibration — in the sense of reliance matching performance — was not achieved within the observed time frame.

**Oscillating patterns (H2b: Not Supported).** No class exhibited a clear oscillating pattern. The gap trajectories were monotonic or near-monotonic for all six classes, without the alternating increases and decreases that would characterize oscillation. This null finding may reflect the smoothing effect of aggregating episodes into 10 broad windows, which could obscure finer-grained oscillatory dynamics.

**Stagnant patterns (H2c: Supported).** Class 4 (High Performers, Low Reliance) exhibited a stagnant calibration pattern, with minimal change in the reliance-performance gap across windows. These students maintained a stable equilibrium of high performance and low reliance, neither increasing nor decreasing their engagement with AI recommendations.

Beyond the hypothesized patterns, two additional empirically observed patterns merit theoretical attention:

**Escalating divergence.** Classes 1 (Gradual Adopters) and 5 (Heavy Adopters) showed a pattern of escalating reliance without proportional performance gains, creating a widening gap. This pattern, while not divergent in the sense of moving away from calibration (the gap was initially very negative and moved toward zero), represents a trajectory that could become over-reliant if the trend continued beyond the observation period.

**Self-correcting over-reliance.** Class 6 (Early Heavy Users) showed a unique pattern of decreasing reliance from an initially high level, representing a trajectory that moved toward (though did not reach) calibration from the over-reliance side.

[Figure 5] presents the empirical trajectories overlaid on the theoretical prediction framework, facilitating visual comparison of theory and data.

### 4.4 RQ3: Early Behavior as a Predictor of Trajectory Class

The multinomial logistic regression model predicting 6-class membership from early behavioral features yielded a cross-validated classification accuracy of **49.4%** (SD across folds = 2.1%). Given that chance-level accuracy for six equally probable classes is 16.7%, the model achieved approximately **3.0 times chance performance**, indicating meaningful predictive power from early behavior alone.

[Table 4] presents the standardized coefficients and significance levels for each predictor across class contrasts.

**Predictor importance.** The strongest predictor was **early exploration rate** (`early_expl_rate`), with a mean absolute standardized coefficient of 1.00 (the highest among all predictors). This variable — the proportion of first-window episodes in which the student viewed explanatory content — differentiated classes in several key contrasts. Specifically, higher early explanation rates were associated with membership in Classes 2 (Steady Calibrators) and 3 (Strong Calibrators) relative to Class 1 (Gradual Adopters) and Class 4 (High Performers, Low Reliance).

The second most important predictor was **early average explanation duration** (`early_avg_expl_dur_s`), with a mean absolute coefficient of 0.60. Students who spent more time per explanation view tended toward the calibrating classes (2 and 3), suggesting that not merely viewing explanations but engaging deeply with them was associated with subsequent calibration trajectories.

**Early reliance rate** (`early_R_b`) was the third predictor in importance (mean |coefficient| = 0.30), primarily distinguishing Class 6 (Early Heavy Users) from all other classes, as expected given their uniquely high initial reliance.

These results support H3 — early explanation-seeking behavior was the strongest predictor of trajectory class membership. The dominance of explanation-related features (rate and duration) over initial reliance and initial performance suggests that metacognitive engagement patterns, rather than starting levels of reliance or ability, are the primary behavioral markers of subsequent calibration trajectories.

### 4.5 RQ4: Class Differences in Learning Outcomes

#### 4.5.1 Overall Accuracy

A one-way ANOVA comparing overall accuracy across the six trajectory classes yielded a statistically significant result: **F(5, 4562) = 177.46, p = 4.66 × 10⁻¹⁷³, $\eta^2$ = 0.163**. The effect size was large, indicating that trajectory class membership accounted for approximately 16.3% of the variance in overall accuracy.

[Table 5] presents the class means and post-hoc comparisons. Class 4 (High Performers, Low Reliance) had the highest overall accuracy (M = .649, SD = .08), significantly exceeding all other classes (all Tukey HSD p < .001). Class 3 (Strong Calibrators) had the lowest overall accuracy (M = .518, SD = .07), significantly lower than all other classes except Class 2 (Steady Calibrators; M = .547). The remaining classes fell between these extremes: Class 6 (M = .591), Class 1 (M = .589), Class 5 (M = .572), and Class 2 (M = .547).

#### 4.5.2 Accuracy Improvement

A one-way ANOVA comparing accuracy improvement ($P(\tau = 10) - P(\tau = 1)$) across classes was also significant: **F(5, 4562) = 25.08, p = 5.04 × 10⁻²⁵, $\eta^2$ = 0.027**. The effect size was small, indicating that trajectory class membership explained approximately 2.7% of the variance in accuracy improvement.

[Table 6] presents the improvement means and post-hoc comparisons. Class 3 (Strong Calibrators) showed the greatest improvement (M = +.048, SD = .11), significantly exceeding Classes 1 and 4 (p < .001). Class 4 (High Performers, Low Reliance) showed the least improvement (M = +.008, SD = .09), consistent with a ceiling effect — students who began with high performance had less room for improvement.

#### 4.5.3 The Performance-Improvement Inverse Relationship

A notable pattern emerged from the joint consideration of overall accuracy and accuracy improvement: the classes ranked in approximately inverse order on these two outcomes. Class 4, with the highest overall accuracy, showed the least improvement. Class 3, with the lowest overall accuracy, showed the most improvement. This inverse relationship is consistent with a ceiling effect interpretation: students with initially high performance have less room for growth, while initially struggling students who engage in calibration processes may show the greatest gains.

This finding provides **modified support for H4**. The convergent calibration class (Class 3, Strong Calibrators) was associated with the greatest *improvement* in performance, consistent with the theoretical prediction that calibrated reliance facilitates learning. However, this same class had the lowest *absolute* performance, and the class with the highest absolute performance (Class 4) followed a stagnant, not convergent, calibration trajectory. Thus, the relationship between calibration and outcomes depends on whether the outcome is defined in terms of level or growth.

**Classification quality and robustness.** The overall average posterior probability for assigned classes was .820, with 76.4% of students assigned with posterior probability exceeding .70 and 62.2% exceeding .80. Classification quality varied across classes: Classes 3 (*M* = .891), 6 (*M* = .913), and 5 (*M* = .874) were most clearly separated, while Classes 1 (*M* = .779) and 4 (*M* = .797) showed the most overlap. A cross-classification analysis revealed that Class 1 students were most frequently confused with Classes 2 and 4, consistent with their intermediate trajectory positions. The normalized entropy of .760 indicated that approximately 76% of classification certainty was retained, supporting the interpretability of the class assignments. Sensitivity analyses (see Method) confirmed that the core class structure replicated across split-half samples and that the ANOVA effects were driven primarily by well-separated classes (3, 5, 6), bolstering confidence in the reported between-class differences.

---

## 5. Discussion

### 5.1 Summary of Findings

This study investigated longitudinal patterns of AI reliance calibration among 4,568 learners using the Santa AI tutoring platform. Using Gaussian Mixture Modeling on joint trajectories of behavioral reliance and performance across 10 temporal windows, we identified six distinct trajectory classes that differed meaningfully in their calibration dynamics, early behavioral signatures, and learning outcomes. The key findings are: (a) substantial heterogeneity exists in how learners calibrate their reliance on AI recommendations over time; (b) some but not all theoretically predicted trajectory shapes were observed; (c) early explanation-seeking behavior is the strongest predictor of subsequent calibration trajectories; and (d) the relationship between calibration and learning outcomes is nuanced, with convergent calibrators showing the greatest improvement but not the highest absolute performance.

### 5.2 Interpretation of the Six Trajectory Classes

The six classes identified in this study map onto distinct learner profiles with different implications for educational practice.

**Gradual Adopters (Class 1)** represent nearly a third of the sample — students who slowly increased their engagement with AI recommendations while maintaining stable performance. These learners may be cautious or skeptical, requiring extended positive experience before increasing reliance. From an intervention perspective, these students might benefit from targeted trust calibration scaffolds that help them evaluate AI recommendation quality, potentially accelerating the adoption of beneficial recommendations.

**Steady Calibrators (Class 2)** and **Strong Calibrators (Class 3)** together comprise over half the sample (53.4%) and represent the most theoretically interesting classes. Both show concurrent increases in reliance and performance, suggesting a productive calibration process. The distinction between them lies in starting point and magnitude: Class 3 students began with lower performance and showed more dramatic improvement, suggesting they had more to gain from (and were more responsive to) AI-guided learning. These classes provide the strongest evidence that reliance calibration — when it proceeds in a convergent direction — is associated with learning gains.

**High Performers with Low Reliance (Class 4)** present a theoretically informative case: students who perform well without substantial AI engagement. Several interpretations are possible. These students may possess strong prior knowledge, making AI recommendations redundant. They may have effective self-regulated learning strategies that obviate the need for external guidance. Or they may harbor dispositional skepticism toward AI systems. Regardless of the mechanism, their stagnant calibration trajectory suggests they have reached a stable equilibrium that, while effective for maintaining current performance, may limit opportunities for further growth.

**Heavy Adopters (Class 5)** represent students whose reliance on AI recommendations increased more rapidly than their performance. This trajectory raises the possibility of developing over-reliance if the trend continued, though within the observed period, their gap remained in the under-reliance range (i.e., performance still exceeded reliance). This class warrants monitoring: if reliance continues to increase without proportional performance gains, intervention to prevent automation complacency (Parasuraman & Manzey, 2010) may be warranted.

**Early Heavy Users (Class 6)**, while small (1.5%), represent a unique trajectory of decreasing reliance from an initially high level. These students may have arrived with strong familiarity with AI systems, initial over-reliance that was self-corrected through experience, or different usage patterns driven by external factors. Their declining reliance, paired with stable performance, suggests a self-regulatory process not captured by the other classes.

### 5.3 The Dominance of Under-Reliance

A striking finding across all classes and time windows was the predominance of under-reliance: the reliance-performance gap was negative throughout, meaning students' performance consistently exceeded their behavioral reliance on AI recommendations. Even Class 6, with the highest reliance levels, maintained a gap near zero rather than crossing into over-reliance territory.

This finding has several possible explanations. First, $R_b$ as operationalized in this study (proportion of adaptive offer episodes) may structurally tend toward low values if the AI system offered recommendations infrequently or if the user interface did not strongly prompt engagement with adaptive content. Second, under-reliance may be the normative behavioral pattern in educational AI systems, where learners are intrinsically motivated to demonstrate independent competence and may view AI reliance as a crutch. Third, under-reliance in the context of TOEIC preparation may reflect the specific goal structure of standardized test preparation, where students aim to develop independent test-taking ability rather than dependence on external support.

Regardless of the explanation, the ubiquity of under-reliance challenges assumptions from high-stakes automation domains where over-reliance is the primary concern (Parasuraman & Manzey, 2010). In educational AI contexts, the risk may be primarily one of under-utilization rather than over-trust — a finding consistent with research on help-avoidance in intelligent tutoring systems (Aleven et al., 2003; Baker et al., 2008).

### 5.4 Reliance, Trust, and the Behavioral-Cognitive Bridge

This study deliberately operationalized its construct at the behavioral level (reliance calibration) rather than the cognitive-attitudinal level (trust calibration). This choice was driven by data availability — the EdNet dataset contains behavioral logs but not self-report measures of trust. However, the relationship between reliance and trust carries important theoretical implications.

Following Lee and See's (2004) model, trust is the attitudinal precursor that guides reliance behavior. If this pathway holds in educational contexts, then the behavioral reliance patterns observed in this study are downstream manifestations of underlying trust dynamics. The trajectory classes, while defined by behavioral reliance and performance, may correspond to different trust calibration processes:

- The *convergent* reliance patterns of Classes 2 and 3 may reflect students who are developing appropriately calibrated trust through positive experience with the AI system.
- The *stagnant* pattern of Class 4 may reflect stable distrust or indifference, where trust remains low and thus does not guide greater reliance.
- The *escalating* patterns of Classes 1 and 5 may reflect growing trust that is translating into increasing reliance.
- The *self-correcting* pattern of Class 6 may reflect trust recalibration following initial over-trust.

These interpretations remain speculative in the absence of direct trust measurement. Future research combining behavioral log data with periodic trust assessments would enable direct testing of the trust-to-reliance pathway in educational contexts.

### 5.5 Connection to the Trust Calibration as Competency Framework

This study serves as a behavioral consistency check for the conceptual framework developed in Paper 3 of this research program, which proposed trust calibration readiness (TCR) as an educational competency comprising three dimensions: Awareness (recognizing AI capabilities and limitations), Judgment (evaluating AI output quality), and Action (making appropriate reliance decisions). The behavioral patterns observed in this study speak primarily to the Action dimension — the observable reliance decisions that learners make.

Several observations are consistent with the Paper 3 framework. First, the heterogeneity in trajectory classes supports the proposition that calibration is a skill that varies across individuals, not a uniform developmental outcome. Second, the association between early explanation-seeking behavior and subsequent calibration trajectories is consistent with the Awareness and Judgment dimensions: students who actively engage with explanatory content may be developing the evaluative skills necessary for calibrated reliance decisions. Third, the existence of a stagnant class (Class 4) is consistent with the framework's prediction that some learners may stabilize at a particular action pattern without progressing through the full calibration competency cycle.

Importantly, this behavioral evidence does not validate the Paper 3 framework in a confirmatory sense — the data are observational, the constructs are measured at the behavioral rather than cognitive level, and the study was not designed to test the specific mechanisms (Awareness, Judgment, Action) proposed in the framework. Rather, the findings provide a consistency check: the behavioral patterns predicted by the framework are, in broad terms, observable in large-scale learning data. This consistency supports the plausibility of the framework while highlighting the need for more direct, mechanism-focused empirical tests.

### 5.6 Educational Implications

The identification of distinct trajectory classes suggests that a one-size-fits-all approach to supporting AI reliance in educational settings is suboptimal. Different classes may benefit from different interventions:

**For Gradual Adopters (Class 1):** Interventions might focus on structured opportunities to experience the benefits of AI recommendations, such as guided trials where students compare their performance with and without AI support. Trust calibration scaffolds that make AI reliability transparent could accelerate the adoption of beneficial recommendations.

**For Steady and Strong Calibrators (Classes 2, 3):** These students appear to be on productive calibration trajectories. Interventions should be supportive rather than directive — maintaining the conditions that facilitate ongoing calibration while monitoring for signs of over-reliance.

**For High Performers with Low Reliance (Class 4):** These students may benefit from challenges beyond their current performance level, where AI recommendations become more relevant. Alternatively, they may benefit from meta-awareness interventions that help them recognize situations where AI support could enhance performance on novel or especially difficult material.

**For Heavy Adopters (Class 5):** Monitoring for potential over-reliance is advisable. Interventions might include periodic prompts to attempt questions independently before viewing AI recommendations, fostering a more balanced reliance pattern.

**For Early Heavy Users (Class 6):** Given their self-correcting trajectory, minimal intervention may be needed; however, understanding why they arrived with high initial reliance could inform onboarding design.

### 5.7 The Early Detection Opportunity

The finding that early explanation-seeking behavior predicts trajectory class membership with approximately three times chance accuracy has practical significance for adaptive educational systems. Within the first decile of a learner's engagement — which may correspond to only a few sessions — behavioral indicators are already informative about the student's likely long-term calibration trajectory.

This early predictability opens a window for proactive intervention. AI tutoring platforms could monitor early exploration and explanation engagement patterns, flagging students whose early behavior profiles suggest trajectories associated with suboptimal outcomes (e.g., persistent under-reliance with low improvement). Adaptive scaffolds could then be deployed early, before maladaptive patterns become entrenched.

However, the 49.4% accuracy — while substantially above chance — also means that over half of students would be misclassified by early behavior alone. This limits the confidence with which early intervention decisions can be made and argues for continuous monitoring and classification updating rather than a single early-stage classification decision.

### 5.8 Limitations

Several limitations qualify the interpretation of these findings.

**Behavioral observation only.** The most fundamental limitation is that this study observed behavioral reliance patterns without access to the underlying cognitive processes of trust formation, judgment, or decision-making. The trajectory classes are defined by observable behavior, and the interpretations offered regarding trust, metacognition, and calibration processes remain inferential. Future research should combine behavioral log data with direct assessments of trust and metacognition.

**Single platform, single domain.** All data come from a single AI tutoring platform (Santa) in a single educational domain (TOEIC preparation) with a specific student population (Korean learners). The extent to which these findings generalize to other platforms, domains, age groups, and cultural contexts is unknown. Cross-platform and cross-cultural replication is needed.

**Operationalization of $R_b$.** Behavioral reliance was operationalized as the proportion of adaptive offer episodes, a platform-specific measure that reflects the Santa app's particular recommendation delivery mechanism. Different operationalizations (e.g., acceptance of specific recommendations, time allocated to AI-recommended content) might yield different trajectory patterns. The $R_b$ measure is also bounded by the platform's adaptive offer frequency — students cannot exhibit high $R_b$ if the system rarely offers adaptive content.

**Zero-inflation and methodological adaptation.** The severe zero-inflation in $R_b$ necessitated a shift from the planned longitudinal GMM (via `lcmm`) to a wide-format cross-sectional GMM (via `mclust`). While the `mclust` approach effectively identified trajectory classes, it does not model individual-level growth parameters and may be less sensitive to within-class trajectory variation than a true longitudinal mixed model.

**Temporal aggregation.** The use of 10 decile-based windows imposes a relatively coarse temporal resolution that may obscure finer-grained dynamics, including possible oscillation patterns (H2b). The windows are also defined by episode count rather than calendar time, meaning that a window may span different real-time durations for different students.

**Causal inference.** The study is entirely observational. The associations between trajectory class and outcomes cannot support causal claims. Students who followed convergent calibration trajectories may have done so because of characteristics (e.g., motivation, metacognitive skill) that independently caused both the calibration pattern and the learning gains.

### 5.9 Future Research Directions

Several directions for future research emerge from this study.

**Hysteresis testing.** The trust-in-automation literature predicts hysteresis effects — trust builds slowly but erodes quickly following failures (Muir & Moray, 1996). Testing whether reliance calibration trajectories show similar asymmetric dynamics in educational contexts would bridge the human factors and educational technology literatures. This could be examined using event-level analysis within the EdNet data, examining reliance changes following incorrect AI recommendations.

**Cross-platform validation.** Replicating this analysis across different AI tutoring platforms, educational domains, and student populations is essential for establishing the generalizability of the trajectory typology. Datasets from platforms such as Khan Academy, Duolingo, or ALEKS could provide comparative evidence.

**Multimodal measurement.** Combining behavioral log data with self-report trust measures, cognitive load assessments, and potentially physiological indicators (e.g., eye-tracking in lab-based studies) would enable direct testing of the trust-to-reliance pathway and the cognitive dimensions of calibration.

**Intervention studies.** The class-specific intervention recommendations offered in this study are speculative. Experimental studies testing targeted interventions for different trajectory classes (e.g., trust calibration scaffolds for Gradual Adopters, independent practice prompts for Heavy Adopters) would provide evidence on the practical utility of trajectory classification.

**Real-time classification.** Developing online algorithms that classify students into trajectory types in real-time — updating classification as more data accumulates — would be a necessary step toward implementing the early detection and adaptive intervention approach discussed above.

---

## 6. Conclusion

This study provides the first large-scale, person-centered analysis of AI reliance calibration trajectories in an educational setting. Using data from 4,568 learners on the Santa AI tutoring platform, we identified six distinct trajectory classes that differ in their patterns of AI reliance adoption, their alignment between reliance and performance, their early behavioral signatures, and their learning outcomes.

The findings demonstrate that learners are not homogeneous in how they calibrate their reliance on AI recommendations. Some learners gradually adopt AI support and show convergent calibration dynamics associated with learning gains. Others maintain high performance with consistently low reliance, exhibiting stagnant calibration that, while effective, may limit future growth opportunities. Still others rapidly escalate reliance without proportional performance benefits, warranting monitoring for potential over-reliance.

Crucially, early explanation-seeking behavior — a proxy for metacognitive engagement with AI-provided content — emerged as the strongest predictor of long-term calibration trajectories. This finding underscores the importance of how learners interact with AI systems, not merely whether they do so. The depth of engagement with AI-provided explanations, rather than the mere frequency of AI recommendation acceptance, appears to distinguish productive calibration trajectories from less adaptive ones.

These results contribute to the growing literature on trust and reliance in AI-assisted education by moving beyond cross-sectional and population-average approaches to reveal the heterogeneous, dynamic processes through which learners develop their relationships with AI systems. As AI becomes increasingly integral to educational practice, understanding and supporting the development of appropriate reliance becomes not merely a technical optimization problem but an educational imperative — one that requires attention to the diverse trajectories that learners follow and the early signals that can inform timely, targeted support.

---

## References

[FULL LIST TBD — Key references included below]

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys, 55*(11), 1–37. https://doi.org/10.1145/3569576

Aleven, V., Stahl, E., Schworm, S., Fischer, F., & Wallace, R. (2003). Help seeking and help design in interactive learning environments. *Review of Educational Research, 73*(3), 277–320. https://doi.org/10.3102/00346543073003277

Baker, R. S. J. d., Corbett, A. T., & Koedinger, K. R. (2004). Detecting student misuse of intelligent tutoring systems. In J. C. Lester, R. M. Vicari, & F. Paraguaçu (Eds.), *Intelligent Tutoring Systems* (pp. 531–540). Springer.

Baker, R. S. J. d., Corbett, A. T., Koedinger, K. R., & Wagner, A. Z. (2004). Off-task behavior in the cognitive tutor classroom: When students "game the system." In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 383–390). ACM.

Baker, R. S. J. d., Corbett, A. T., Roll, I., & Koedinger, K. R. (2008). Developing a generalizable detector of when students game the system. *User Modeling and User-Adapted Interaction, 18*(3), 287–314. https://doi.org/10.1007/s11257-007-9045-6

Baker, R. S. J. d., D'Mello, S. K., Rodrigo, M. M. T., & Graesser, A. C. (2010). Better to be frustrated than bored: The incidence, persistence, and impact of learners' cognitive-affective states during interactions with three different computer-based learning environments. *International Journal of Human-Computer Studies, 68*(4), 223–241. https://doi.org/10.1016/j.ijhcs.2009.12.003

Bauer, D. J., & Curran, P. J. (2003). Distributional assumptions of growth mixture models: Implications for overextraction of latent trajectory classes. *Psychological Methods, 8*(3), 338–363. https://doi.org/10.1037/1082-989X.8.3.338

Boscardin, C. K., Muthén, B., Francis, D. J., & Baker, E. L. (2008). Early identification of reading difficulties using heterogeneous developmental trajectories. *Journal of Educational Psychology, 100*(1), 192–208. https://doi.org/10.1037/0022-0663.100.1.192

Broadbent, J., & Poon, W. L. (2015). Self-regulated learning strategies & academic achievement in online higher education learning environments: A systematic review. *The Internet and Higher Education, 27*, 1–13. https://doi.org/10.1016/j.iheduc.2015.04.007

Chen, J. Y. C., Procci, K., Boyce, M., Wright, J., Garcia, A., & Barnes, M. (2014). *Situation awareness-based agent transparency* (ARL-TR-6905). U.S. Army Research Laboratory.

Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., ... & Heo, J. (2020). EdNet: A large-scale hierarchical dataset in education. In *Proceedings of the 21st International Conference on Artificial Intelligence in Education* (pp. 69–73). Springer. https://doi.org/10.1007/978-3-030-52240-7_13

Choudhury, A., Asan, O., & Stahelin, L. (2020). Effect of AI explanation on trust and decision-making in healthcare. In *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 64*(1), 704–708. https://doi.org/10.1177/1071181320641165

de Visser, E. J., Peeters, M. M., Jung, M. F., Kohn, S., Shaw, T. H., Pak, R., & Neerincx, M. A. (2020). Towards a theory of longitudinal trust calibration in human–robot teams. *International Journal of Social Robotics, 12*, 459–478. https://doi.org/10.1007/s12369-019-00596-x

du Boulay, B. (2016). Artificial intelligence as an effective classroom assistant. *IEEE Intelligent Systems, 31*(6), 76–81. https://doi.org/10.1109/MIS.2016.93

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The role of trust in automation reliance. *International Journal of Human-Computer Studies, 58*(6), 697–718. https://doi.org/10.1016/S1071-5819(03)00038-7

Ghosh, A., Heffernan, N., & Lan, A. S. (2020). Context-aware attentive knowledge tracing. In *Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2330–2339). https://doi.org/10.1145/3394486.3403282

Guo, P. J., & Yang, D. (2021). MOOC learner behaviors by country and culture: An exploratory analysis. In *Proceedings of the Eighth ACM Conference on Learning @ Scale* (pp. 127–137). ACM.

Holmes, W., Bialik, M., & Fadel, C. (2022). *Artificial intelligence in education: Promises and implications for teaching and learning* (2nd ed.). Center for Curriculum Redesign.

Jian, J. Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. *International Journal of Cognitive Ergonomics, 4*(1), 53–71. https://doi.org/10.1207/S15327566IJCE0401_04

Kaur, H., Nori, H., Jenkins, S., Caruana, R., Wallach, H., & Wortman Vaughan, J. (2022). Interpreting interpretability: Understanding data scientists' use of interpretability tools for machine learning. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–14). ACM.

Körber, M. (2019). Theoretical considerations and development of a questionnaire to measure trust in automation. In S. Bagnara et al. (Eds.), *Proceedings of the 20th Congress of the International Ergonomics Association* (pp. 13–30). Springer.

Lee, J. D., & Moray, N. (1994). Trust, self-confidence, and operators' adaptation to automation. *International Journal of Human-Computer Studies, 40*(1), 153–184. https://doi.org/10.1006/ijhc.1994.1007

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50.30392

Muir, B. M. (1994). Trust in automation: Part I. Theoretical issues in the study of trust and human intervention in automated systems. *Ergonomics, 37*(11), 1905–1922. https://doi.org/10.1080/00140139408964957

Muir, B. M., & Moray, N. (1996). Trust in automation: Part II. Experimental studies of trust and human intervention in a process control simulation. *Ergonomics, 39*(3), 429–460. https://doi.org/10.1080/00140139608964474

Musu-Gillette, L. E., Wigfield, A., Harring, J. R., & Eccles, J. S. (2015). Trajectories of change in students' self-concepts of ability and values in math and college major choice. *Educational Research and Evaluation, 21*(4), 343–370. https://doi.org/10.1080/13803611.2015.1057161

Muthén, B. (2004). Latent variable analysis: Growth mixture modeling and related techniques for longitudinal data. In D. Kaplan (Ed.), *The SAGE handbook of quantitative methodology for the social sciences* (pp. 345–368). SAGE.

Nagin, D. S. (2005). *Group-based modeling of development*. Harvard University Press.

Nagin, D. S., & Land, K. C. (1993). Age, criminal careers, and population heterogeneity: Specification and estimation of a nonparametric, mixed Poisson model. *Criminology, 31*(3), 327–362. https://doi.org/10.1111/j.1745-9125.1993.tb01133.x

Nazaretsky, T., Ariely, M., Cukurova, M., & Alexandron, G. (2022). Teachers' trust in AI-powered educational technology and a professional development program to improve it. *British Journal of Educational Technology, 53*(4), 914–931. https://doi.org/10.1111/bjet.13232

Nylund, K. L., Asparouhov, T., & Muthén, B. O. (2007). Deciding on the number of classes in latent class analysis and growth mixture modeling: A Monte Carlo simulation study. *Structural Equation Modeling, 14*(4), 535–569. https://doi.org/10.1080/10705510701575396

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253. https://doi.org/10.1518/001872097778543886

Proust-Lima, C., Philipps, V., & Liquet, B. (2017). Estimation of extended mixed models using latent classes and latent processes: The R package lcmm. *Journal of Statistical Software, 78*(2), 1–56. https://doi.org/10.18637/jss.v078.i02

Ram, N., & Grimm, K. J. (2009). Growth mixture modeling: A method for identifying differences in longitudinal change among unobserved groups. *International Journal of Behavioral Development, 33*(6), 565–576. https://doi.org/10.1177/0165025409343765

Schemmer, M., Kuehl, N., Benz, C., Bartos, A., Satzger, G., & Dennerlein, A. (2023). Appropriate reliance on AI advice: Conceptualization and the effect of explanations. In *Proceedings of the 28th International Conference on Intelligent User Interfaces* (pp. 410–422). ACM. https://doi.org/10.1145/3581641.3584066

Scrucca, L., Fop, M., Murphy, T. B., & Raftery, A. E. (2016). mclust 5: Clustering, classification and density estimation using Gaussian finite mixture models. *The R Journal, 8*(1), 289–317. https://doi.org/10.32614/RJ-2016-021

Shin, D., Shim, Y., Yu, H., Lee, S., Kim, B., & Choi, Y. (2021). SAINT+: Integrating temporal features for EdNet correctness prediction. In *LAK21: 11th International Learning Analytics and Knowledge Conference* (pp. 490–496). ACM. https://doi.org/10.1145/3448139.3448188

Siau, K., & Wang, W. (2018). Building trust in artificial intelligence, machine learning, and robotics. *Cutter Business Technology Journal, 31*(2), 47–53.

VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. https://doi.org/10.1080/00461520.2011.611369

Zawacki-Richter, O., Marín, V. I., Bond, M., & Gouverneur, F. (2019). Systematic review of research on artificial intelligence applications in higher education — where are the educators? *International Journal of Educational Technology in Higher Education, 16*(1), 39. https://doi.org/10.1186/s41239-019-0171-0

---

## Appendix A: Supplementary Tables and Figures

[Table 1: Descriptive Statistics for $R_b$ and $P$ Across 10 Temporal Windows — TO BE INSERTED]

[Table 2: BIC Values for Competing GMM Models — TO BE INSERTED]

[Table 3: Characteristics of the Six Trajectory Classes — TO BE INSERTED]

[Table 4: Multinomial Logistic Regression Coefficients — TO BE INSERTED]

[Table 5: Post-Hoc Comparisons of Overall Accuracy Across Classes — TO BE INSERTED]

[Table 6: Post-Hoc Comparisons of Accuracy Improvement Across Classes — TO BE INSERTED]

[Figure 1: Trust-Reliability Matrix — TO BE INSERTED]

[Figure 2: Theoretical Trajectory Predictions in $R_b \times P \times \tau$ Space — TO BE INSERTED]

[Figure 3: Mean $R_b$ and $P$ Trajectories by Class — TO BE INSERTED]

[Figure 4: Gap ($R_b - P$) Trajectories by Class — TO BE INSERTED]

[Figure 5: Theory-Empirical Overlay — TO BE INSERTED]

---

*Manuscript word count: approximately 9,200 words (excluding references and appendices)*
