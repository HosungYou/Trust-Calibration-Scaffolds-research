# 다운로드 가능한 공개 데이터셋: T × R × τ 모델 검증용

**Date:** 2026-03-11
**Context:** 실제 다운로드하여 분석 가능한 데이터셋만 검증 완료
**기준:** (1) 실제 다운로드 확인됨, (2) 개인 수준 반복 측정, (3) Trust/Reliance + System Performance + Time 매핑 가능

---

## TIER 1: 직접적 Trust Trajectory 분석 가능 (다운로드 확인)

### 1. Rittenberg et al. (2024) ★★★★★ — 가장 이상적

- **URL:** https://borealisdata.ca/citation?persistentId=doi:10.5683/SP3/BYDQF9
- **접근:** 로그인 불필요, 즉시 다운로드
- **형식:** TAB (집계), JSON (raw trial-level), R script
- **규모:** N=147 (Exp1: 98, Exp2: 49), 300 trials/person, **30 trust 측정점/person**
- **변수:** ID, Condition(Increasing/Decreasing), Trust(VAS 0-100), Confidence, Block, Reliability
- **T × R × τ 매핑:**
  - T = Trust (VAS 0-100, continuous) — 10 trials마다 측정
  - R = System reliability (50%→100% 또는 100%→50%, 체계적 변화)
  - τ = Trial number (1-300) / Block (1-6)
- **분석 가능성:**
  - Growth Mixture Modeling → 3가지 궤적 유형 분류
  - Increasing vs Decreasing 조건 비교 → Hysteresis 직접 검증
  - Change-point analysis → Catastrophe 임계점 탐색

### 2. Dhuliawala/Zouhar et al. (EMNLP 2023) ★★★★★

- **URL:** https://huggingface.co/datasets/zouharvi/trust-intervention + https://github.com/zouharvi/trust-intervention
- **접근:** 로그인 불필요
- **형식:** Parquet (1.02 MB, 18,664 rows) + JSONL
- **규모:** 332 users × ~56 trials/person, 9 experimental conditions
- **변수:** question_i, user_bet_val, user_decision (follow AI or not), ai_is_correct, ai_confidence, user_balance, timestamps
- **T × R × τ 매핑:**
  - T = Bet size (behavioral trust) + follow/reject decision
  - R = AI correctness + AI confidence
  - τ = Sequential trial index
- **분석 가능성:** 금전적 stakes 포함; intervention condition 비교; trust erosion 후 slow recovery 패턴 확인 가능

### 3. Trustworthy-ML — Lu & Yin (CHI 2021) ★★★★★

- **URL:** https://github.com/ZhuoranLu/Trustworthy-ML
- **접근:** 로그인 불필요
- **형식:** CSV + Jupyter/R notebooks
- **규모:** 3 experiments, trial-level data
- **변수:** workerId, taskId, selfPrediction, finalPrediction, switch, mlCorrect, competence, faith, reliability (7-point)
- **T × R × τ 매핑:**
  - T = Self-report trust (7-point) + behavioral switching
  - R = ML model accuracy (manipulated)
  - τ = Task sequence
- **분석 가능성:** Self-report + behavioral 동시 측정; feedback 유무 조건 비교

### 4. HAIID — Vodrahalli et al. (AIES 2022) ★★★★☆

- **URL:** https://github.com/kailas-v/human-ai-interactions
- **접근:** 로그인 불필요
- **형식:** CSV (8.8 MB) + codebook
- **규모:** 1,100+ participants, 30,000+ interactions, 5 domains
- **변수:** participant_id, task_name, response_1 (pre-advice), response_2 (post-advice), trust_in_advice, perceived_accuracy, helpfulness
- **T × R × τ 매핑:**
  - T = trust_in_advice (0-1) + response switching behavior
  - R = Advice accuracy (objective)
  - τ = Trial sequence per domain
- **분석 가능성:** Multi-domain → cross-domain trust transfer; 대규모

### 5. Chess AI Decision Making (Data in Brief 2023) ★★★★☆ — NEW

- **URL:** https://data.mendeley.com/datasets/ng33vg479n/1
- **접근:** Mendeley Data, 로그인 불필요
- **형식:** ZIP of 100 CSV files (1 per participant)
- **규모:** 100 participants × 30 experimental trials
- **변수:** Independent move, AI suggestion, final move, correctness feedback, self-confidence, **confidence-in-AI**
- **T × R × τ 매핑:**
  - T = Confidence-in-AI rating (trial-level)
  - R = AI accuracy + correctness feedback
  - τ = Trial number (1-30)
- **분석 가능성:** AI performance가 trial 20에서 방향 전환 → change-point 분석 이상적

### 6. Okamura & Yamada (PLOS ONE 2020) ★★★★☆

- **URL:** https://doi.org/10.6084/m9.figshare.11538792.v1
- **접근:** Figshare, 로그인 불필요, CC BY 4.0
- **형식:** XLSX (28 KB), 2 sheets
- **규모:** N=194, 15 repeated measurements/person
- **T × R × τ 매핑:** Group condition × 15 trust measurement points
- **분석 가능성:** 깨끗한 종단 구조, growth curve modeling 직접 적용

### 7. BiasedHumanAI — Affective Brain Lab ★★★☆☆

- **URL:** https://github.com/affective-brain-lab/BiasedHumanAI
- **접근:** 로그인 불필요
- **형식:** CSV + SPSS (.sav)
- **규모:** N=1,401 across 3 experiments, 12 evidence steps + AI per trial
- **변수:** evidence1-12, responseAI, changeMind, finalResponse
- **분석 가능성:** AI advice가 evidence accumulation을 어떻게 변형하는지; within-trial dynamics

### 8. Steyvers et al. ImageNet-16H (PNAS 2022) ★★★☆☆

- **URL:** https://osf.io/2ntrf/
- **접근:** OSF, 로그인 불필요
- **형식:** CSV (14 MB)
- **규모:** 145 participants × ~200 classifications
- **변수:** participant_id, confidence, classification_time, correct, noise_level
- **한계:** Explicit trust measure 없음; confidence calibration으로 활용

### 9. Automation Bias Impact (Agudo et al. 2023) ★★★☆☆ — NEW

- **URL:** https://osf.io/b6p4z/
- **형식:** OSF data files
- **내용:** AI 오류 시 human-in-the-loop 의사결정, trial-by-trial follow/override
- **접근:** OSF, 로그인 불필요

### 10. Judge-Advisor Learning (Schultze 2025) ★★★☆☆ — NEW

- **URL:** https://osf.io/8s3f5/
- **내용:** 3 experiments, advice-taking이 반복 문제에서 어떻게 변화하는지
- **접근:** OSF, 로그인 불필요

---

## TIER 2: 간접적 Trust Proxy 가능 (대규모 ITS/Learning Data)

### 11. ASSISTments ★★★★☆

- **URL:** https://sites.google.com/site/assistmentsdata/
- **다운로드:**
  - 2009-10: Google Drive 링크 (가장 많이 인용, 70+ papers)
  - 2012-13: etrialstestbed.org (affect labels 포함)
  - 2015: Google Drive
  - 2017: Google Form 등록 후 링크 제공
- **형식:** CSV
- **규모:** 2009-10: 4,217 students, 346,860 interactions
- **Trust proxy:** hint_count, attempt_count, first_action (hint vs attempt)
  - Hint avoidance → overconfidence/overtrust
  - Hint abuse → under-confidence

### 12. EdNet (Riiid/Santa) ★★★★☆

- **URL:** https://github.com/riiid/ednet
- **다운로드:** Google Drive, 로그인 불필요
  - KT1: 1.2 GB (5.6 GB uncompressed)
  - KT3: 0.8 GB (explanation-seeking 포함)
  - KT4: 1.2 GB (full behavioral log)
- **규모:** 784,309 students, 131M interactions
- **Trust proxy:** KT3의 explanation enter/quit → AI guidance 의존도

### 13. OULAD ★★★☆☆

- **URL:** https://analyse.kmi.open.ac.uk/open-dataset
- **다운로드:** 즉시, CC BY 4.0, 로그인 불필요
- **형식:** 7 CSV files
- **규모:** 32,593 students, 10.6M VLE click entries
- **Trust proxy:** Daily engagement trajectory + assessment scores

### 14. PSLC DataShop ★★★☆☆

- **URL:** https://pslcdatashop.web.cmu.edu/
- **다운로드:** Google SSO 로그인 후 가능
- **규모:** 188+ datasets, 42M+ student actions
- **Trust proxy:** Hint request patterns per knowledge component

### 15. KDD Cup 2010 ★★★☆☆

- **URL:** https://pslcdatashop.web.cmu.edu/KDDCup/
- **다운로드:** DataShop 계정 필요 (707 MB compressed)
- **Trust proxy:** Hint usage + opportunity count

---

## TIER 3: 기타 도메인 (다운로드 확인)

### 16. Zenodo: Adaptive Trust-Calibrated Human-AI Collaboration (Akande 2025)

- **URL:** https://zenodo.org/record/18431925
- **규모:** 350 participants × 4 conditions, trust calibration error 측정
- **형식:** XLSX (67 KB)
- **접근:** 즉시 다운로드

### 17. Trust Game Database — Fu et al. (Frontiers 2019)

- **URL:** https://datadryad.org/stash/share/I4_9eQgXJL0sjukj8I9ruT2TToTZ90RuZvSmJO5LnyY
- **규모:** 40 participants, iterated trust game + EEG
- **접근:** Dryad, 즉시 다운로드

### 18. AV Communication Strategies in VR (Ferenchak 2021)

- **URL:** https://zenodo.org/record/6430710
- **내용:** VR 환경 자율주행 반복 세션, trust/acceptance/comfort 측정
- **형식:** XLSX (68 KB)
- **접근:** 즉시 다운로드, CC BY 4.0

### 19. Bidirectional Trust in Human-Robot Collaboration

- **URL:** https://github.com/hazevedosa/bidirectional-trust
- **내용:** 양방향 trust 모델링 데이터
- **형식:** XLSX + MATLAB scripts
- **접근:** 즉시 다운로드

### 20. Collab-CXR: Radiologist-AI Collaboration (2025)

- **URL:** https://osf.io/z7apq
- **규모:** 227 radiologists × 324 cases, 104 pathologies
- **형식:** CC BY 4.0
- **접근:** OSF, 즉시 다운로드

### 21. Bastani et al. (PNAS 2025)

- **URL:** https://github.com/obastani/GenAICanHarmLearning
- **규모:** ~1,000 students, problem-level + 39.6 MB interaction logs
- **접근:** 즉시 다운로드

---

## TIER 4: 패널 서베이 (등록 필요)

### 22. Pew American Trends Panel

- **URL:** https://www.pewresearch.org/internet/datasets/
- **접근:** 무료 등록 후 다운로드
- **형식:** SPSS (.sav), CSV
- **패널 여부:** True panel (동일 응답자 반복), 단 AI 문항이 매 wave 동일하지 않을 수 있음
- **주의:** Cross-wave respondent linkage 가능 여부 확인 필요

### 23. LISS Panel (Netherlands)

- **URL:** https://www.lissdata.nl/
- **접근:** 무료 등록 후 다운로드
- **패널 여부:** True panel (2007~현재, ~7,500 individuals)
- **주의:** AI/technology trust 모듈 존재 여부 아카이브에서 확인 필요

### 24. Eurobarometer (GESIS)

- **URL:** https://www.gesis.org/en/eurobarometer-data-service
- **접근:** 무료 등록 후 다운로드
- **형식:** SPSS/Stata
- **주의:** Repeated cross-section (NOT panel) — 집단 수준 트렌드만 가능

### 25. Harvard Dataverse: Weekly GenAI Market Pulse Survey

- **URL:** https://dataverse.harvard.edu/ (DOI: 10.7910/DVN/MLTIHE)
- **접근:** Terms 동의 후 다운로드
- **특이점:** 2026년 2월부터 weekly 추적 — 매우 최신
- **주의:** 개인 패널 ID 제공 여부 확인 필요

---

## 비사용 (확인 결과 부적합)

| 데이터셋 | 이유 |
|---------|------|
| Langer et al. OSF | 데이터 미공개 (PDF supplementary만 존재) |
| CLeAR NUS trust transfer | N=32, 8 ratings only — 너무 작음 |
| Logg et al. OSF | Between-subjects 위주, trajectory 분석 한계 |
| TRUSTONOMY Pilot | N=14, 너무 작음 |

---

## 추천 분석 전략

### Phase 1: Proof of Concept (1-2주)

**데이터:** Rittenberg et al. (2024)
**방법:**
1. Borealis에서 다운로드
2. 개인별 30-point trust trajectory 추출
3. Growth Mixture Modeling (GMM) 또는 Latent Class Growth Analysis
4. 3가지 패턴 (convergent, oscillating, stagnant) 존재 여부 확인
5. Increasing vs Decreasing condition → Hysteresis 비대칭성 검증

**보완:** Zouhar dataset으로 다른 맥락에서 동일 패턴 재현

### Phase 2: Cross-Domain Generalization (2-4주)

**데이터:** HAIID (5 domains) + Chess AI + Trustworthy-ML
**방법:**
1. 도메인별 궤적 패턴 비교
2. 도메인 간 일반화 가능성 검증
3. Task characteristics → trajectory type 예측 모델

### Phase 3: Educational Context (선택)

**데이터:** ASSISTments 2012-13 (affect 포함)
**방법:**
1. Help-seeking behavior를 trust proxy로 매핑
2. Affect states와 reliance pattern 관계 분석
3. 학생 수준 calibration trajectory 추출

---

## 참고문헌

- Rittenberg, B., et al. (2024). Trust with increasing and decreasing reliability. *Human Factors*, 66(11).
- Dhuliawala, S., Zouhar, V., et al. (2023). A diachronic perspective on user trust in AI under uncertainty. *EMNLP 2023*.
- Lu, Z., & Yin, M. (2021). Human reliance on ML models when performance feedback is limited. *CHI 2021*.
- Vodrahalli, K., et al. (2022). Do humans trust advice more if it comes from AI? *AAAI/ACM AIES*.
- Okamura, K., & Yamada, S. (2020). Adaptive trust calibration for human-AI collaboration. *PLOS ONE*.
- Steyvers, M., et al. (2022). Bayesian modeling of human-AI complementarity. *PNAS*.
- Guo, Y., & Yang, X. J. (2021). Modeling and predicting trust dynamics in human-robot teaming. *IJSR*, 12, 459-478.
- Chung, S., & Yang, X. J. (2024). Predicting trust dynamics with personal characteristics. *HFES*, 68(1).
