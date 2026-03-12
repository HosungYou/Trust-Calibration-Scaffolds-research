# 통합 실현가능성 리포트: Multi-Agent Review 종합

**Date:** 2026-03-11
**Reviewers:** G1 (Journal Matcher), A3 (Devil's Advocate), A4 (Research Ethics), C1 (Quantitative Design), E1 (Quantitative Analysis)
**Target:** Paper 4 — "How Learners Calibrate Trust in AI: Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System"
**Target Journal:** Computers & Education (IF ~12.0)

---

## Executive Summary

5개 에이전트의 독립 리뷰 결과, **하나의 일관된 핵심 문제**가 모든 리뷰어에 의해 식별되었습니다:

> **현재 설계의 calibration_gap은 85%의 학생에게 단순 학습 곡선(learning curve)을 측정하며, 이론적으로 주장하는 "trust calibration"과 측정 지표 간에 심각한 간극이 존재합니다.**

이 문제를 해결하기 위한 **수렴적 권고안**도 명확합니다:

1. **분석 대상을 adaptive_offer 경험자(~10,200명)로 한정**하거나
2. **"Trust calibration"에서 "AI recommendation reliance-performance alignment"로 재개념화**

**종합 판정: 조건부 진행 가능 (설계 수정 필수)**

---

## 1. 이슈 매핑: 5개 리뷰어의 발견 교차 분석

### 1.1 수렴 이슈 (3개 이상 리뷰어가 독립적으로 지적)

| 이슈 | G1 | A3 | A4 | C1 | E1 | 등급 |
|------|:--:|:--:|:--:|:--:|:--:|------|
| adaptive_offer 15% → 85% gap=accuracy | — | ✓ | — | ✓ | ✓ | **CRITICAL** |
| Trust proxy 구성타당도 결함 | — | ✓ | — | ✓ | ✓ | **CRITICAL** |
| calibration_gap ≠ trust calibration | — | ✓ | — | ✓ | ✓ | **CRITICAL** |
| Cross-validation 구조적 비호환성 | ✓ | — | — | ✓ | ✓ | **CRITICAL** |
| 과잉 검정력 (N=68K) | — | — | — | ✓ | ✓ | **MAJOR** |
| 사전등록(Pre-registration) 필요 | — | — | ✓ | — | ✓ | **MAJOR** |

### 1.2 고유 이슈 (단일 리뷰어의 독자적 발견)

| 이슈 | 리뷰어 | 등급 | 요약 |
|------|--------|------|------|
| SRL/메타인지 프레이밍 필요 | G1 | MAJOR | C&E 독자층에 적합한 교육학적 프레이밍 |
| Jingle fallacy (동일명칭, 상이구성) | C1 | CRITICAL | trust라 부르지만 실제는 학습궤적 |
| Rolling window 구조적 자기상관 | E1 | CRITICAL | w=20에서 인접 ventile 간 r>0.9 예상 |
| IRB formal exemption 필요 | A4 | MAJOR | 이차자료라도 공식 면제 판정 필수 |
| CC BY-NC + Elsevier 라이선스 충돌 | A4 | MAJOR | EdNet 라이선스 확인 필요 |
| Gap_B 이론적 근거 부재 | C1 | CRITICAL | explanation_depth ≠ (1 - trust) |
| GMM 정규성 가정 위반 (zero-inflated) | E1 | MAJOR | Gaussian mixture에 부적합 |
| Informative dropout | E1 | MINOR | 높은 gap 학생이 먼저 이탈 가능 |

---

## 2. CRITICAL 이슈 상세 분석 및 통합 권고

### Issue #1: Trust Proxy 구성타당도 — "무엇을 측정하고 있는가?"

**문제의 핵심 (A3 + C1 + E1 수렴):**

```
현재 설계                              실제 측정하는 것
─────────────                         ─────────────
AI_reliance (adaptive_offer 비율)  →  AI 추천 노출률 (학생 선택이 아닌 시스템 할당)
sys_accuracy (정답률)              →  학생의 현재 능력 수준 (≠ 시스템 신뢰도)
calibration_gap = |T - R|          →  85%: 단순 정답률
                                      15%: AI추천 노출률과 정답률의 괴리
```

**A3의 핵심 지적:** accuracy는 학생의 ability이지 시스템의 reliability가 아님. Lee & See (2004)의 calibration은 "주관적 trust와 시스템 actual capability의 대응"인데, 현재 설계는 둘 다 잘못 조작화됨.

**C1의 핵심 지적:** compliance(순응)는 trust의 결과(consequence)이지 trust 자체가 아님 (Parasuraman & Riley, 1997). 순응하지 않는 이유가 불신인지, 자기효능감인지, 무관심인지 구분 불가.

**E1의 핵심 지적:** 85%의 학생에게 AI_reliance=0이므로 calibration_gap = accuracy. GMM은 사실상 accuracy trajectory의 mixture를 추정하게 됨.

### ➜ 통합 권고안 A: "Two-Track Design"

| Track | 대상 | N (추정) | Trust Proxy | 프레이밍 |
|-------|------|---------|-------------|---------|
| **Primary** | adaptive_offer 경험자 | ~10,200 | AI_reliance = 수락률, System_quality = 수락 후 정답률 변화 | "AI Recommendation Reliance Calibration" |
| **Secondary** | 전체 분석 대상 | ~68,000 | explanation_depth, lecture_rate 등 | "Learning Engagement Trajectories" (trust 아님) |

- Primary track: 진정한 trust-adjacent 행동 (AI 추천 수락/거부 결정)을 분석
- Secondary track: 보조 분석으로 전체 학습자의 자기조절학습 궤적 탐색
- 두 track의 결과를 비교하여 "AI 추천 경험이 궤적에 미치는 영향" 논의

### Issue #1b: Calibration Gap 방향성 정보 손실 (C1 추가 발견)

**C1이 실제 데이터(u562823)를 분석하여 추가로 발견한 CRITICAL 이슈:**

`calibration_gap = |AI_reliance - sys_accuracy|`에서 **절대값이 overtrust와 undertrust를 구분 불가능하게 만듭니다.**

```
학생 A: AI_reliance = 0.8, accuracy = 0.3 → gap = 0.5 (OVERTRUST)
학생 B: AI_reliance = 0.2, accuracy = 0.8 → gap = 0.5 (UNDERTRUST)
→ GMM은 두 학생을 동일 class로 분류할 가능성 높음
```

Lee & See (2004)에서 overtrust와 undertrust는 질적으로 다른 현상이며, 교육적 개입도 완전히 다릅니다. 절대값 gap은 이 구분을 소멸시킵니다.

### ➜ 통합 권고안 A-2: 방향성 보존

1. **Signed gap 사용:** `signed_gap = AI_reliance - sys_accuracy` (양수=overtrust, 음수=undertrust)
2. **다변량 궤적 전환 (C1 + E1 수렴 권고):** 단일 calibration_gap 대신 `explanation_depth + accuracy + answer_change_rate`를 동시 모델링 → `lcmm::multlcmm()` 사용
3. 절대값 gap은 보조 보고만

### Issue #2: Cross-Validation 구조적 비호환성

**G1 + C1 + E1 수렴 지적:**

| 차원 | EdNet (본 연구) | Rittenberg | Zouhar | Lu & Yin |
|------|----------------|------------|--------|----------|
| N | ~68,000 | 147 | 332 | ~300 |
| 측정 | 행동 proxy | VAS 자기보고 | Betting 행동 | 혼합 |
| 도메인 | TOEIC 학습 | 의료 AI | 기계번역 | AI 의사결정 |
| 시간 | 수백 에피소드 | 30 시점 | 56 시행 | ~15 시점 |

"교차 타당화"라 부르기에는 측정 동등성이 전혀 확보되지 않음.

### ➜ 통합 권고안 B: Cross-Validation 재구조화

1. **내적 교차검증 추가** (E1 권고): 10-fold CV + split-half로 GMM 안정성 확인
2. **외적 분석 격하**: "교차 타당화" → "탐색적 일반화 분석 (Exploratory Generalizability Analysis)"
3. **독립 GMM 비교**: 각 Tier 1 데이터셋에서 독립적으로 GMM 실행 후 궤적 형태의 질적 유사성 비교
4. **대안**: Tier 1 데이터를 별도 후속 논문 (Paper 5)으로 분리 검토

### Issue #3: Rolling Window 구조적 자기상관

**E1 고유 발견 (CRITICAL):**

Rolling window w=20에서 인접 ventile 평균은 최대 19개 에피소드를 공유 → 인위적 자기상관(lag-1 ACF > 0.9 예상). 이는:
- GMM이 과도하게 평탄한 궤적을 추정하도록 편향
- 통계적으로 유의한 trajectory class를 과다 추출할 위험
- 진정한 행동 변화와 통계적 artifact를 구분 불가

### ➜ 통합 권고안 C: 자기상관 해소

1. **Non-overlapping windows** 사용 (rolling 대신 구간 평균)
2. lcmm에서 **AR(1) 잔차 구조** 명시
3. 자기상관 진단을 Phase 0에 포함 (ACF 계산 및 보고)

---

## 3. MAJOR 이슈 및 권고

### 3.1 과잉 검정력 대응 (C1 + E1)

N=68,000에서 Cohen's d = 0.02도 p < .001 → p-value가 무의미.

**권고:**
- 효과크기 + 95% CI를 모든 RQ의 primary 보고 지표로 설정
- 실질적 유의성 임계값 사전 정의 (η² > .02, Cohen's d > 0.20)
- GMM class 수 결정에 BIC + Entropy + 최소 class 크기(5%) + 해석가능성 종합 적용
- N=5,000 무작위 하위표본으로 결과 안정성 확인 (replication subsample)

### 3.2 저널 적합성 및 프레이밍 (G1)

**G1의 핵심 권고:**
- C&E는 대규모 학습 분석(learning analytics) 연구를 활발히 게재 → 강점
- 단, **SRL(자기조절학습)/메타인지 프레이밍** 필요 → trust calibration만으로는 교육학적 기여 불명확
- IJAIED를 고수용률 대안으로 고려 (AI + 교육 교차 영역)
- Tier 1 교차검증이 C&E에서는 차별화 요소 (→ 강화 필요)

### 3.3 연구윤리 (A4)

| 항목 | 현황 | 필요 조치 |
|------|------|-----------|
| IRB | 미제출 | Penn State IRB에 formal exemption 신청 |
| 데이터 라이선스 | CC BY-NC (EdNet) | Elsevier 게재 시 라이선스 호환성 확인 |
| 동의 | 원 수집 시 연구 동의 포함 여부 불명 | EdNet 원 논문의 ethics statement 확인 |
| 사전등록 | 미실시 | OSF pre-registration 권장 (A4 + E1 수렴) |
| trust profiling | 학생을 "Stagnant" 등으로 분류 | 라벨링의 윤리적 함의 논의 필요 |

### 3.4 분석 방법론 개선 (E1)

| 현재 계획 | 권고 변경 |
|-----------|-----------|
| mclust/tidyLPA (wide format) | **lcmm FMEM** (long format, random effects) |
| Gaussian mixture | **beta/splines link** (bounded outcome 적합) |
| Rolling window w=20 | **Non-overlapping ventile 구간 평균** |
| BIC/AIC/Entropy/BLRT | + **SABIC**, BLRT는 N>10K에서 무의미하므로 제외 |
| 단일 분석 | + **Multiverse analysis** (w, proxy, ventile 수 변동) |
| 외적 교차검증만 | + **내적 10-fold CV** + split-half |

### 3.5 프레이밍 전환 제안 (C1 고유)

C1은 가장 근본적인 해법으로 **프레이밍 자체의 전환**을 제안:

| | 현재 | 제안 |
|---|------|------|
| **구성개념** | Trust Calibration | Help-Seeking Calibration |
| **핵심 proxy** | AI_reliance (85% = 0) | explanation_depth, lecture_seeking (거의 모든 학생에게 존재) |
| **이론적 기반** | Lee & See (2004) | Karabenick & Berger (2013), Nelson-Le Gall (1981) |
| **측정 직접성** | 간접 proxy | 직접 측정 |
| **적용 범위** | 15% 학생 | 거의 전체 |

**장점:** adaptive_offer 의존도 문제 완전 해소, C&E에서 help-seeking은 확립된 주제
**단점:** 연구 프로그램(TCR) 전체 서사와의 일관성 문제 → 연구자 판단 필요

### 3.6 GMM 정규성 가정 위반 (E1)

calibration_gap은 [0,1] 범위의 절대값 → right-skewed + zero-inflated → Gaussian mixture 부적합.

**권고:** lcmm의 `link = "beta"` 또는 `link = "5-equi-splines"` 사용.

---

## 4. 대안적 설계 제안

### 4.1 C1 권고: Bivariate GMM (최적 추천)

adaptive_offer 경험자 대상, AI_reliance와 System_quality의 **공동 궤적(joint trajectory)**을 모형화:
- Trust의 두 차원 (의존도 + 시스템 품질 인식)의 동적 관계를 포착
- 단변량 calibration_gap보다 풍부한 정보

### 4.2 E1 권고: 단계적 분석 전략

```
Phase 0: 데이터 진단 (신규 추가)
  → Zero-inflation 확인, ACF 진단, 결측 패턴
  → 최소 에피소드 임계값 설정

Phase 1: 데이터 전처리 (Python)
  → Non-overlapping ventile 구간화
  → Gap_B를 secondary, AI_reliance gap을 primary (adaptive_offer 경험자만)

Phase 2: 탐색적 분석 (R)
  → KML로 빠른 탐색 → lcmm FMEM (beta link)으로 본 분석
  → 50+ 랜덤 초기값, N=5K pilot → N=full 확대

Phase 3: 모형 선택 및 검증
  → BIC/AIC/Entropy/SABIC 종합, split-half 안정성
  → Specification curve analysis

Phase 4: 교차검증
  → 내적: 10-fold CV with ARI
  → 외적: Tier 1 독립 GMM + 궤적 형태 비교

Phase 5: 결과 보고
  → 효과크기 + 95% CI 중심
  → Multiverse analysis 부록
```

### 4.3 C1 대안 2: Sequential Pattern Mining / HMM

GMM 대신 행동 시퀀스의 전이 패턴을 식별하는 접근. 정보 손실이 적으나 C&E 독자층에게 덜 친숙할 수 있음.

### 4.4 C1 대안 3: Propensity Score 기반 인과 추론

adaptive_offer 경험을 "처치"로 간주, PSM으로 인과 효과 추정. "trust" 대신 "AI 추천의 행동적 영향"이라는 더 방어 가능한 프레이밍.

---

## 5. 리뷰어별 독립 종합 판정

| 리뷰어 | 판정 | 핵심 조건 |
|--------|------|-----------|
| **G1** (Journal) | 게재 가능 (수정 후) | SRL 프레이밍 추가, Tier 1 교차검증 강화 |
| **A3** (Critique) | 근본 수정 필요 | trust proxy 재정의 또는 분석 대상 한정 |
| **A4** (Ethics) | 진행 가능 | IRB 면제, 사전등록, 라이선스 확인 |
| **C1** (Design) | 조건부 진행 | adaptive_offer 하위표본 주 분석, 개념 재정의 |
| **E1** (Analysis) | 조건부 진행 | lcmm FMEM, 자기상관 해소, 내적 CV 추가 |

---

## 6. 실행 우선순위 로드맵

### 즉시 필요 (코딩 시작 전)

| # | 행동 | 담당 | 예상 소요 |
|---|------|------|---------|
| 1 | **설계 결정: Two-Track vs 단일 Track** | 연구자 | 1일 |
| 2 | **Trust proxy 재정의 문서화** | 연구자 | 1일 |
| 3 | **Santa 앱 UX 문서 확보** (adaptive_offer 제시 방식) | 연구자 → Riiid Labs | 1-2주 |
| 4 | **IRB exemption 신청** (Penn State) | 연구자 | 2-4주 |
| 5 | **EdNet 라이선스 확인** (CC BY-NC + Elsevier 호환) | 연구자 | 1일 |
| 6 | **OSF Pre-registration 초안** | 연구자 | 2-3일 |

### Phase 0 추가 (코딩 첫 단계)

| # | 행동 | 예상 소요 |
|---|------|---------|
| 7 | adaptive_offer 경험자 정확한 N 확인 | 2시간 |
| 8 | Zero-inflation 진단 | 1시간 |
| 9 | ACF 진단 (rolling vs non-overlapping 비교) | 2시간 |
| 10 | 결측 패턴 분석 | 1시간 |
| 11 | N=5,000 pilot GMM | 4시간 |

### 분석 계획 수정

| # | 현재 → 변경 |
|---|------------|
| 12 | 전체 68K 분석 → **adaptive_offer 경험자 주 분석 + 전체 보조 분석** |
| 13 | Rolling window → **Non-overlapping ventile 구간 평균** |
| 14 | mclust/tidyLPA → **lcmm FMEM + beta link** |
| 15 | 외적 교차검증만 → **내적 10-fold CV + 외적 탐색적 비교** |
| 16 | p-value 중심 → **효과크기 + 95% CI 중심** |
| 17 | calibration_gap 단일 정의 → **Multiverse analysis** |

---

## 7. 논문 제목 및 프레이밍 수정안

### 현재

> "How Learners Calibrate Trust in AI: Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System"

### 수정 제안

**Option A (보수적, C1 + A3 권고):**
> "Trajectories of AI Recommendation Reliance in Adaptive Learning: A Growth Mixture Analysis of 10,000+ Learner Behavioral Logs"

**Option B (교육학 프레이밍, G1 권고):**
> "How Learners Engage with AI Recommendations Over Time: Identifying Trajectory Types in an AI Tutoring System"

**Option C (절충):**
> "From Trust to Action: Behavioral Trajectories of AI Recommendation Reliance in Adaptive Learning"

---

## 부록: 리뷰어별 참고문헌 종합

- Choi, Y., et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. *AIED 2020*.
- Guo, Y., & Yang, X. J. (2021). Modeling and predicting trust dynamics in human-robot teaming. *IJSR*, 12, 459-478.
- Lee, J. D., & See, K. A. (2004). Trust in automation. *Human Factors*, 46(1), 50-80.
- Nylund, K. L., et al. (2007). Deciding on the number of classes in latent class analysis. *SEM*, 14(4), 535-569.
- Nylund-Gibson, K., & Choi, A. Y. (2018). Ten frequently asked questions about latent class analysis. *TIPS*, 4(4), 440-461.
- Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230-253.
- Ram, N., & Grimm, K. J. (2009). Growth mixture modeling. *IJBD*, 33(6), 565-576.
- Thorndike, E. L. (1904). An introduction to the theory of mental and social measurements. *Science Press*.

---

*이 리포트는 5개 Diverga 에이전트(G1, A3, A4, C1, E1)의 독립 리뷰를 통합한 것입니다.*
*각 에이전트는 서로의 리뷰를 참조하지 않고 독립적으로 분석하였으며, CRITICAL 이슈에 대한 높은 수렴도는 해당 문제의 심각성을 반영합니다.*

---

## 부록 B: 원본 에이전트의 추가 상세 권고 (실제 데이터 기반)

C1과 E1의 원본 에이전트는 실제 샘플 데이터(kt3_u562823)를 직접 분석하여 다음의 추가 권고를 제시했습니다:

### E1 원본: 구체적 R 코드 권고

1. **lcmm 기반 LCGA→GMM 단계적 접근** (LCGA로 탐색 → 최적 K에서 random effects 추가)
2. **다중 초기값 전략**: 최소 20회 random start로 local optima 방지
3. **DTW/k-shape 교차 검증**: GMM과 비모수적 클러스터링 간 ARI > 0.60 확인
4. **TOST 동치 검정**: 효과크기가 "무시할 수 있을 만큼 작은가" 검정
5. **Bayesian 보완**: BayesFactor로 H1 vs H0 증거 강도 보고

### C1 원본: 다변량 궤적 모델링 코드

```r
# 다변량 잠재 클래스 혼합 모델 (권장)
library(lcmm)
multi_model <- multlcmm(
  explanation_depth + accuracy ~ time + I(time^2),
  mixture = ~ time + I(time^2),
  random = ~ time,
  subject = "user_id",
  ng = 3,
  data = data_long,
  link = c("linear", "linear")
)
```

### C1 원본: 분석 우선순위

| 순위 | 분석 | 이유 |
|------|------|------|
| 1 | 기술통계: adaptive_offer 경험 비율, 에피소드 분포 | 모든 설계 결정의 기반 |
| 2 | 단일 학생 궤적 시각화 100명 | 실제 궤적 형태 파악 |
| 3 | Gap_B 구성 + 타당성 확인 | 주 분석 변수 확정 |
| 4 | 무작위 10,000명에서 GMM 탐색 | 계산 효율 + 패턴 탐색 |
| 5 | 전체 표본 확인 분석 | 최종 결과 |

*전체 원본 리뷰: `/private/tmp/claude-501/-Users-hosung/tasks/` 참조*
