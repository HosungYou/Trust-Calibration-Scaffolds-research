# Open Datasets for T × R × τ Model Validation

**Date:** 2026-03-11
**Context:** 공개 패널/종단 데이터를 통한 Trust Calibration Trajectory 가설 검증 가능성 탐색
**Research Question:** Trust-Reliability calibration이 시간에 따라 서로 다른 궤적 패턴(convergent, oscillating, stagnant)을 보이는가?

---

## 핵심 발견: 이미 동일한 3가지 궤적을 발견한 연구 존재!

### Guo & Yang (2021) / Chung & Yang (2024) — University of Michigan

**가장 중요한 발견:** 이 연구팀이 이미 실험적으로 우리가 이론적으로 예측한 3가지 궤적 유형을 발견했습니다:

| 우리의 이론적 예측 | Guo & Yang의 실험적 발견 | 일치 |
|-------------------|------------------------|------|
| **Convergent** (High Readiness) | **Bayesian decision maker** | ✓ Perfect match |
| **Oscillating** (Developing Readiness) | **Oscillator** | ✓ Perfect match |
| **Stagnant** (Low Readiness) | **Disbeliever** | ✓ Perfect match |

**Guo & Yang (2021):**
- N=39, 60 trials/person over 3 days, drone surveillance simulation
- T = self-reported trust (1-10 scale per trial)
- R = drone detection performance (objective, variable)
- τ = trial number (1-60 across 3 sessions)
- Paper: [IJSR](https://link.springer.com/article/10.1007/s12369-020-00703-3)

**Chung & Yang (2024) — 확장 연구:**
- N=130, 100 trials/person, automated threat detector
- 12 개인 특성(28 차원)이 궤적 유형을 예측
- 7개 특성이 유의미한 예측 변수
- Paper: [HFES](https://journals.sagepub.com/doi/full/10.1177/10711813241260383); [arXiv](https://arxiv.org/abs/2409.07406)
- **데이터 접근:** 저자 연락 필요 (X. Jessie Yang, University of Michigan)

**이론적 함의:** 우리의 T × R × τ 모델과 TCRS Readiness가 궤적을 예측한다는 가설이 이미 부분적으로 실증적 지지를 받음. 단, 그들은 "Readiness"라는 프레임으로 설명하지 않았으므로, 우리의 기여는 이 현상에 대한 이론적 설명(mechanism)을 제공하는 것.

---

## TIER 1: 즉시 사용 가능한 공개 데이터셋 (직접적 Trust-Reliability-Time 매핑)

### 1. Rittenberg et al. (2024) — 가장 이상적인 데이터셋 ★★★★★

- **제목:** "Trust with increasing and decreasing reliability"
- **저널:** Human Factors, 66(11)
- **데이터 URL:** https://doi.org/10.5683/SP3/BYDQF9 (Borealis repository)
- **참가자:** Exp 1: N=98 (53 increasing, 45 decreasing); Exp 2: N=49
- **시행 수:** 300 trials/person across 6 blocks of 50 trials
- **측정:** Trust in automation (VAS 0-100) 매 10 trials → **30 trust measurements per person**
- **변수 매핑:**
  - T = Trust in automation (VAS 0-100, continuous)
  - R = System reliability (50% → 100% or 100% → 50%, manipulated)
  - τ = Trial number (1-300) / Block (1-6)
- **접근성:** **완전 공개** (Borealis, 분석 스크립트 포함)
- **핵심 장점:**
  - 개인별 30개 trust 측정점 → 개인 수준 궤적 추출 가능
  - Reliability가 체계적으로 변화 → Hysteresis 검증 직접 가능
  - Increasing vs. Decreasing 조건 비교 → Trust building vs. erosion 비대칭성 검증
- **한계:** 교육 맥락이 아닌 일반적 자동화 과제

### 2. Dhuliawala/Zouhar et al. (EMNLP 2023) ★★★★☆

- **제목:** "A Diachronic Perspective on User Trust in AI under Uncertainty"
- **데이터 URL:** https://huggingface.co/datasets/zouharvi/trust-intervention; https://github.com/zouharvi/trust-intervention
- **측정:** NLP 시스템에 대한 sequential betting → bet size = behavioral trust
- **변수 매핑:**
  - T = Bet size (behavioral trust proxy)
  - R = System accuracy/calibration (manipulated)
  - τ = Trial sequence number
- **접근성:** **완전 공개** (HuggingFace + GitHub, 코드/데이터/인터페이스 모두)
- **핵심 장점:** Trust erosion 후 "very slow recovery" 패턴 발견 → Hysteresis 직접 증거
- **한계:** NLP 도메인; 행동적 trust 측정 (self-report 아님)

### 3. HAIID — Vodrahalli et al. (2022) ★★★★☆

- **제목:** "Do Humans Trust Advice More if it Comes from AI?" (AAAI/ACM AIES)
- **데이터 URL:** https://github.com/kailas-v/human-ai-interactions
- **참가자:** 1,100+ crowdworkers + expert dermatologists
- **상호작용:** 30,000+ interactions; 5 domains (Art, Census, Cities, Dermatology, Sarcasm)
- **변수 매핑:**
  - T = Trust rating (0-1) + reliance behavior (response switching)
  - R = Advice accuracy (objective)
  - τ = Trial sequence per participant
- **접근성:** **완전 공개** (GitHub, CSV format)
- **핵심 장점:** 대규모; multi-domain → domain transfer 분석 가능

### 4. Trustworthy-ML — Lu & Yin (2021) ★★★★☆

- **제목:** "Human Reliance on ML Models When Performance Feedback is Limited" (CHI 2021)
- **데이터 URL:** https://github.com/ZhuoranLu/Trustworthy-ML
- **변수:** selfPrediction, finalPrediction, prediction switching, trust (7-point), perceived accuracy
- **접근성:** **완전 공개** (GitHub, Jupyter notebooks + R Markdown)
- **핵심 장점:** Self-report trust + behavioral reliance 동시 측정; sequential trial design

### 5. Okamura & Yamada (2020) ★★★★☆

- **제목:** "Adaptive Trust Calibration for Human-AI Collaboration" (PLOS ONE)
- **데이터 URL:** https://doi.org/10.6084/m9.figshare.11538792.v1
- **참가자:** N=116, 30 checkpoints per person
- **핵심 장점:** Fluctuating reliability → calibration adaptation 직접 관찰
- **접근성:** **완전 공개** (Figshare)

### 6. Steyvers et al. (2022) — ImageNet-16H ★★★☆☆

- **제목:** "Bayesian modeling of human-AI complementarity" (PNAS)
- **데이터 URL:** https://osf.io/2ntrf/
- **참가자:** 145 classifiers, ~200 decisions/person
- **접근성:** **완전 공개** (OSF)
- **한계:** Confidence ratings only (no explicit trust scale)

### 7. CLeAR Lab (NUS) — Trust Transfer ★★★☆☆

- **데이터 URL:** https://github.com/clear-nus/human-trust-transfer
- **과제:** 12 tasks in household robot + 12 tasks in autonomous driving (VR)
- **접근성:** **완전 공개** (GitHub)
- **핵심 장점:** Cross-domain trust transfer 분석 가능

---

## TIER 2: 교육 맥락 데이터 (Behavioral Proxy로 Trust Calibration 추론)

### 8. ASSISTments (2012-2013) ★★★★☆

- **데이터 URL:** https://sites.google.com/site/assistmentsdata/
- **규모:** 27,066 students, 2,541,201 interactions
- **특이점:** Affect predictions (frustrated, confused, bored, engaged) 포함
- **변수 매핑:**
  - T = Hint reliance behavior (hint 요청 횟수 = system 의존도)
  - R = First-attempt correctness
  - τ = Problem sequence / assignment date
- **접근성:** **무료 다운로드**
- **핵심 장점:** Affect predictions → confidence/frustration 간접 측정; 대규모

### 9. PSLC DataShop (Cognitive Tutor) ★★★★☆

- **데이터 URL:** https://pslcdatashop.web.cmu.edu/
- **규모:** 188+ datasets, 42M+ student actions, 150,000+ student hours
- **변수 매핑:**
  - T = Help-seeking behavior (hint avoidance = overconfidence; hint abuse = under-confidence)
  - R = Step correctness
  - τ = Opportunity count (nth encounter with each KC)
- **접근성:** **무료** (로그인 후)
- **이론적 연결:** Aleven et al.의 help-seeking model이 help avoidance → overconfidence, help abuse → under-confidence 매핑을 검증

### 10. EdNet (Riiid/Santa) ★★★★☆

- **데이터 URL:** https://github.com/riiid/ednet
- **규모:** 784,309 students, 131,441,538 interactions
- **특이점:** 한국 TOEIC 준비 AI 튜터링 플랫폼 (Santa)
- **변수 매핑:**
  - T = Lecture/explanation consumption (system guidance 의존도)
  - R = Answer correctness
  - τ = Timestamps over weeks/months
- **접근성:** CC BY-NC 4.0

### 11. OULAD (Open University Learning Analytics) ★★★☆☆

- **데이터 URL:** https://analyse.kmi.open.ac.uk/open-dataset
- **규모:** 32,593 students, 22 module presentations
- **접근성:** CC BY 4.0, **무료 다운로드**

### 12. NEPS (National Educational Panel Study, Germany) ★★★★★

- **데이터 URL:** https://www.neps-data.de/
- **규모:** 수만 명, 다중 코호트, 수년간 추적
- **핵심 가치:** **유일한 true panel with repeated metacognitive measures**
  - T = Metacognitive self-assessment / self-concept
  - R = Competence test scores (reading, math, science)
  - τ = Wave/year (수년간 동일 개인 추적)
- **접근성:** 데이터 사용 계약 필요 (Bamberg Research Data Center)
- **핵심 장점:** 장기간 동일 개인의 반복 측정 → 진정한 calibration trajectory 모델링

---

## TIER 3: 교육 AI 특화 데이터

### 13. Bastani et al. (2025) ★★★☆☆

- **데이터 URL:** https://github.com/obastani/GenAICanHarmLearning
- **규모:** ~1,000 고등학생, 다수 practice sessions + exams
- **변수:** Performance scores, GPT conversation transcripts with timestamps
- **접근성:** **완전 공개** (GitHub)
- **한계:** Explicit trust measure 없음; reliance behavior로 추론 필요

### 14. El Fassi et al. (Scientific Reports, 2025) ★★★☆☆

- **4주간 weekly classroom 실험; AI-labeled vs. peer-labeled advice
- **한계:** 4 time points only

---

## TIER 4: 대규모 서베이 패널 (인구 수준 트렌드)

| 데이터셋 | 유형 | 접근성 | AI Trust 변수 | 한계 |
|---------|------|-------|-------------|------|
| Pew ATP (2021-2025) | Panel (일부 동일 응답자) | 무료 다운로드 | AI 우려/흥분 | AI 문항 파동마다 다름 |
| UK PADAI Tracker (Wave 1-4) | Repeated cross-section | UK Data Service | AI/Data trust | 개인 추적 불가 |
| Eurobarometer AI (2017-2024) | Repeated cross-section | GESIS 무료 | AI 태도 | 개인 추적 불가 |
| LISS Panel (Netherlands) | True panel | lissdata.nl | Technology adoption | AI-specific 모듈 확인 필요 |
| Edelman Trust Barometer | Repeated cross-section | 보고서만 공개 | Technology trust | 원시데이터 비공개 |

---

## 검증 전략: 단계별 접근

### Phase 1: 즉시 실행 가능 (공개 데이터 재분석)

**추천 데이터셋:** Rittenberg et al. (2024)
- 즉시 다운로드 가능
- 개인별 30개 trust 측정점 → 궤적 유형 분류 가능
- Increasing vs. Decreasing reliability → Hysteresis 검증
- **분석 방법:**
  1. Growth Mixture Modeling (GMM) 또는 Latent Class Growth Analysis (LCGA)로 궤적 유형 분류
  2. 3가지 패턴 (convergent, oscillating, stagnant) 존재 확인
  3. Guo & Yang (2021)의 결과와 비교 검증

**보완 분석:** HAIID + Trustworthy-ML
- 다른 과제 맥락에서 동일 패턴 확인 → 일반화 가능성 검증

### Phase 2: 교육 맥락 확장 (ITS 데이터)

**추천 데이터셋:** ASSISTments + PSLC DataShop
- Help-seeking behavior를 calibration proxy로 사용
- 궤적 패턴이 educational context에서도 나타나는지 확인
- 장기 데이터 (학기/학년 단위)

### Phase 3: 이론 통합 (저자 접촉)

**Chung & Yang (2024) 데이터 요청:**
- X. Jessie Yang (University of Michigan) 연락
- 130명 × 100 trials + 12 personal characteristics
- 개인 특성 → 궤적 유형 예측 데이터
- **우리의 기여:** TCRS Readiness가 그들의 "personal characteristics"보다 더 정확한 예측 변수가 될 수 있음을 이론적으로 주장

### Phase 4: 종단 패널 검증 (장기)

**NEPS 데이터 신청:**
- 수년간의 metacognitive self-assessment + competence test 반복 측정
- 진정한 장기 calibration trajectory 모델링

---

## Paper 3 통합 전략

이 데이터 검색 결과는 Paper 3 (Conceptual Paper)에 다음과 같이 활용:

1. **Guo & Yang의 3가지 궤적 유형을 "Empirical warrant"로 인용:**
   "Existing empirical evidence supports the existence of distinct trust calibration trajectories. Guo and Yang (2021) identified three trajectory types — Bayesian decision maker, oscillator, and disbeliever — in human-automation interaction, which correspond precisely to the convergent, oscillating, and stagnant patterns predicted by our T × R × τ framework."

2. **TCRS Readiness를 mechanism으로 제안:**
   "While Guo and Yang classified trajectories post hoc, we propose that trust calibration readiness — as measured by the TCRS — provides the upstream mechanism that predicts trajectory membership a priori."

3. **Future work로 실증 검증 로드맵 제시:**
   "This theoretical prediction is testable using existing open datasets (Rittenberg et al., 2024; Vodrahalli et al., 2022) and purpose-built longitudinal studies."

---

## 참고문헌

### 직접 관련
- Guo, Y., & Yang, X. J. (2021). Modeling and predicting trust dynamics in human-robot teaming. *IJSR*, 12, 459-478.
- Chung, S., & Yang, X. J. (2024). Predicting trust dynamics with personal characteristics. *HFES*, 68(1).
- Rittenberg, B., Holland, M., Barnhart, W., Gaudreau, M., & Neyedli, J. (2024). Trust with increasing and decreasing reliability. *Human Factors*, 66(11).
- Dhuliawala, S., Zouhar, V., et al. (2023). A diachronic perspective on user trust in AI under uncertainty. *EMNLP 2023*.
- Vodrahalli, K., Daneshjou, R., Gerstenberg, T., & Zou, J. (2022). Do humans trust advice more if it comes from AI? *AAAI/ACM AIES*.
- Lu, Z., & Yin, M. (2021). Human reliance on ML models when performance feedback is limited. *CHI 2021*.
- Okamura, K., & Yamada, S. (2020). Adaptive trust calibration for human-AI collaboration. *PLOS ONE*.
- Steyvers, M., et al. (2022). Bayesian modeling of human-AI complementarity. *PNAS*.

### 교육 데이터
- Bastani, H., et al. (2025). Generative AI can harm learning. *PNAS*, 122(2).
- Koedinger, K.R., et al. (2010). A data repository for the EDM community: The PSLC DataShop.
- Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171.
- Choi, Y., et al. (2020). EdNet: A large-scale hierarchical dataset in education. *AIED 2020*.
- Blossfeld, H.-P., et al. (2011). Education as a lifelong process: NEPS.
