# 상세 분석 설계도: Trust Calibration Trajectories in AI-Assisted Learning

**Date:** 2026-03-11
**Target Journal:** Computers & Education (IF ~12.0)
**Data:** EdNet KT3 (297,915 students) + Tier 1 실험 데이터 (교차 검증)

---

## 시각적 참조

아래 시각화들이 `figures/` 폴더에 생성되어 있습니다:

| 파일 | 내용 |
|------|------|
| `Analysis_A_Pipeline_Overview.png` | 전체 분석 파이프라인 (3단계) |
| `Analysis_B_Trust_Proxy_Construction.png` | Trust Proxy 변수 구성 과정 |
| `Analysis_C_Expected_Trajectory_Patterns.png` | 이론적 예측 궤적 4유형 |
| `Analysis_D_GMM_Model_Selection.png` | GMM 모델 선택 기준 |
| `Analysis_E_Cross_Validation_Strategy.png` | 교차 검증 전략 (EdNet → Tier 1) |
| `Analysis_F_Technical_Architecture.png` | Python ↔ R 기술 아키텍처 |

---

## 1. 연구 질문 및 가설

### 연구 질문

| RQ | 질문 | 분석 기법 |
|----|------|---------|
| **RQ1** | AI 튜터링에서 학습자의 Trust Calibration 궤적은 몇 가지 질적으로 구분되는 유형으로 분류되는가? | Growth Mixture Modeling (GMM) |
| **RQ2** | 이론적으로 예측된 궤적 패턴(convergent, oscillating, stagnant)이 실증적으로 관찰되는가? | GMM 결과 vs 이론 예측 대조 |
| **RQ3** | 학습자의 초기 행동 특성이 궤적 유형을 예측하는가? | Multinomial logistic regression |
| **RQ4** | 궤적 유형에 따라 학습 성과(정확도 향상)에 차이가 있는가? | ANOVA / Kruskal-Wallis |

### 가설

| ID | 가설 | 이론적 근거 |
|----|------|-----------|
| **H1** | 3개 이상의 질적으로 구분되는 궤적 유형이 존재한다 | Guo & Yang (2021): 3 유형 발견 |
| **H2a** | Convergent 유형: Calibration gap이 시간에 따라 단조 감소한다 | "Bayesian decision maker" (Guo & Yang) |
| **H2b** | Oscillating 유형: Calibration gap이 감쇠 진동 패턴을 보인다 | "Oscillator" (Guo & Yang) |
| **H2c** | Stagnant 유형: Calibration gap이 일정 수준을 유지하거나 증가한다 | "Disbeliever" (Guo & Yang) |
| **H3** | 초기(첫 10%) 해설 열람 시간과 adaptive_offer 경험이 궤적 유형을 예측한다 | TCRS process model: 초기 Awareness가 궤적 결정 |
| **H4** | Convergent 유형의 학습 성과 향상이 가장 크다 | 신뢰 교정 → 적절한 AI 활용 → 학습 성과 |

---

## 2. Phase 1: Data Wrangling (Python)

### 2.1 학생 필터링

**파이프라인:** `analysis/scripts/01_filter_students.py`

```
297,915 전체 학생
  ↓ 필터 1: 파일 크기 > 0 (비어있는 파일 제거)
  ↓ 필터 2: action 수 ≥ 100 (최소 분석 가능 기준)
  ↓ 필터 3: 시간 범위 ≥ 1일 (단일 세션 제외)
  ↓ 필터 4: question-solving episodes ≥ 50 (해설/강의만 있는 학생 제외)
~68,000 분석 대상 학생 (추정)
```

**출력:** `data/ednet-kt3/processed/filtered_student_list.csv`
- 컬럼: `user_id`, `n_actions`, `n_episodes`, `time_span_hours`, `has_adaptive_offer`

### 2.2 에피소드 파싱

**파이프라인:** `analysis/scripts/02_parse_episodes.py`

하나의 "에피소드"는 하나의 문제 풀이 세션:

```
enter(bundle) → [respond(question)]* → submit(bundle)
                                         ↓
                              [enter(explanation) → quit(explanation)]  (선택적)
                              [enter(lecture) → quit(lecture)]          (선택적)
```

**에피소드 단위 추출 변수:**

| 변수 | 계산 방법 | 의미 |
|------|---------|------|
| `episode_id` | 순번 (1, 2, 3, ...) | 시간 순서 |
| `timestamp` | enter(bundle) 시점 | 절대 시간 |
| `source` | enter action의 source 필드 | sprint / adaptive_offer / tutor / ... |
| `is_adaptive` | source가 'adaptive_offer' 포함 여부 | AI 추천 에피소드인가? |
| `n_questions` | bundle 내 question 수 | 문제 수 |
| `n_correct` | user_answer == correct_answer | 정답 수 (metadata/questions.csv 참조) |
| `accuracy` | n_correct / n_questions | 정답률 |
| `n_respond` | respond action 수 | 답변 변경 횟수 포함 |
| `answer_changes` | 동일 question에 대한 respond 수 - 1 | 불확실성 지표 |
| `read_explanation` | explanation enter 존재 여부 | 해설 열람 여부 |
| `explanation_duration_s` | quit(e) - enter(e) 타임스탬프 차이 (초) | 해설 열람 시간 |
| `watched_lecture` | lecture enter 존재 여부 | 강의 시청 여부 |
| `lecture_duration_s` | quit(l) - enter(l) (초) | 강의 시청 시간 |
| `solving_time_s` | submit - enter(bundle) (초) | 문제 풀이 시간 |
| `platform` | mobile / web | 플랫폼 |

**출력:** `data/ednet-kt3/processed/all_episodes.parquet` (~68K students × 평균 150 episodes)

### 2.3 Trust Proxy 변수 생성

**파이프라인:** `analysis/scripts/03_compute_trust_proxies.py`

Rolling window (w=20 episodes) 기반 시계열 변수:

| 변수 | 조작적 정의 | T/R/τ | 해석 |
|------|-----------|-------|------|
| **`AI_reliance`** | window 내 adaptive_offer 에피소드 비율 | **T** | 높으면 AI 추천에 더 많이 의존 |
| **`sys_accuracy`** | window 내 정답률 | **R** | 학습자가 경험하는 시스템 "정확도" |
| **`calibration_gap`** | \|AI_reliance − sys_accuracy\| | **핵심** | 신뢰와 성능 간 괴리 |
| `explanation_rate` | window 내 해설 열람 비율 | 보조 | 정보 탐색 행동 |
| `explanation_depth` | 평균 해설 열람 시간 (초) | 보조 | 처리 깊이 |
| `answer_change_rate` | window 내 답변 변경 비율 | 보조 | 불확실성 |
| `lecture_rate` | window 내 강의 시청 비율 | 보조 | 자발적 학습 |

**calibration_gap 해석:**

```
                    높은 AI_reliance + 낮은 accuracy = OVERTRUST
                    (AI에 많이 의존하지만 성과는 낮음)

calibration_gap     ┌─────────────────────────────────────────┐
= |T - R|          │                                         │
                    │  gap = 0 → CALIBRATED (이상적)          │
                    │  gap > 0 → MISCALIBRATED                │
                    │                                         │
                    └─────────────────────────────────────────┘

                    낮은 AI_reliance + 높은 accuracy = UNDERTRUST
                    (AI를 안 쓰지만 쓰면 도움이 될 수 있음)
```

**주의사항:**
- `adaptive_offer`가 없는 학생도 많음 (85%). 이 경우 AI_reliance = 0이므로 calibration_gap = sys_accuracy.
  → **대안 접근:** AI_reliance 대신 `explanation_depth`를 주 Trust proxy로 사용하는 모델도 병렬 실행
- 두 가지 calibration_gap 정의를 모두 분석하여 민감도 확인:
  - **Gap_A:** |adaptive_offer_rate − accuracy| (AI 추천 의존도 기반)
  - **Gap_B:** |1 − explanation_depth_normalized − accuracy| (정보 탐색 기반, 높은 설명 무시 = 높은 자신감)

### 2.4 시간 정규화 (Ventile Matrix)

**파이프라인:** `analysis/scripts/04_time_normalize.py`

학생마다 에피소드 수가 다르므로 (50~60,000), 20분위(ventile)로 정규화:

```
Student A (400 episodes):  episodes 1-20 → ventile 1, 21-40 → ventile 2, ...
Student B (100 episodes):  episodes 1-5 → ventile 1, 6-10 → ventile 2, ...
Student C (2000 episodes): episodes 1-100 → ventile 1, 101-200 → ventile 2, ...
```

각 ventile에서 해당 window의 평균 calibration_gap 계산.

**출력:** `data/ednet-kt3/processed/ventile_matrix.csv`
- 형식: 학생 ID × 20 ventile columns
- 각 셀: 해당 ventile의 평균 calibration_gap
- 크기: ~68,000 rows × 22 columns (id + 20 ventiles + metadata)

---

## 3. Phase 2: Trajectory Classification (R)

### 3.1 Growth Mixture Modeling

**스크립트:** `analysis/scripts/05_gmm_analysis.R`

**사용 패키지:** `mclust` (Gaussian mixture), `tidyLPA` (interface), `lcmm` (latent class mixed model)

**모델 비교:**

| 모델 | K (class 수) | 설명 |
|------|-------------|------|
| M1 | 1 | 단일 궤적 (모든 학습자 동일 패턴) |
| M2 | 2 | 두 유형 |
| **M3** | **3** | **이론 예측 (convergent / oscillating / stagnant)** |
| M4 | 4 | 3 + catastrophic? |
| M5 | 5 | 과적합 가능성 |
| M6 | 6 | 과적합 가능성 |

**모델 선택 기준:**

| 기준 | 해석 | 임계값 |
|------|------|--------|
| **BIC** | 낮을수록 좋음 (parsimony 보상) | 가장 낮은 K 선택 |
| **AIC** | 낮을수록 좋음 (BIC보다 유연) | 참고 |
| **Entropy** | 1에 가까울수록 분류 명확 | ≥ 0.80 권장 |
| **BLRT** | K vs K-1 비교 p-value | p < .05 → K가 유의하게 나음 |
| **Class proportion** | 각 class의 최소 비율 | ≥ 5% (N=3,400 이상) |
| **Interpretability** | 이론과 부합 | 주관적 판단 |

**R 코드 핵심 구조:**

```r
library(tidyLPA)
library(mclust)

# Read ventile matrix
data <- read.csv("ventile_matrix.csv")
ventile_cols <- paste0("V", 1:20)

# Fit models K=1 to K=6
results <- data[, ventile_cols] %>%
  estimate_profiles(1:6,
    variances = "varying",      # 각 class별 다른 분산
    covariances = "zero"        # 공분산 = 0 (독립)
  )

# Compare models
compare_solutions(results, statistics = c("AIC", "BIC", "Entropy", "BLRT"))

# Best model extraction
best <- results[[3]]  # K=3 (예상)
assignments <- get_data(best)
write.csv(assignments, "class_assignments.csv")
```

### 3.2 모델 변형 (Sensitivity Analysis)

| 변형 | 설명 | 목적 |
|------|------|------|
| **Varying variances** | class별 분산 허용 | 기본 모델 |
| **Equal variances** | class 간 동일 분산 | 강건성 |
| **Free covariances** | ventile 간 공분산 허용 | 시간 자기상관 반영 |
| **lcmm 접근** | Latent class mixed model | 연속 시간 모델링 |

```r
# lcmm 접근 (latent class mixed model)
library(lcmm)

# Long format 필요
data_long <- pivot_longer(data, ventile_cols, names_to = "ventile", values_to = "gap")
data_long$ventile_num <- as.numeric(gsub("V", "", data_long$ventile))

# K=3 모델
m3 <- hlme(gap ~ ventile_num + I(ventile_num^2),
           mixture = ~ ventile_num + I(ventile_num^2),
           subject = "user_id",
           ng = 3,
           data = data_long)
```

### 3.3 예상 결과 시나리오

**시나리오 A: 이론 확인 (K=3, 예측 패턴 일치)**

| Class | 이름 | 예상 비율 | 궤적 | Guo & Yang 대응 |
|-------|------|---------|------|---------------|
| 1 | Convergent | 30-40% | Gap 감소 → 0 | Bayesian decision maker |
| 2 | Oscillating | 30-40% | Gap 진동 → 감소 | Oscillator |
| 3 | Stagnant | 20-30% | Gap 유지/증가 | Disbeliever |

**시나리오 B: 부분 확인 (K=3이지만 패턴이 다름)**
- 예: Convergent 대신 "Early vs Late converger" 분화
- → 이론 수정 제안 가능

**시나리오 C: K≠3 (4 또는 5 유형)**
- → 추가 유형(Catastrophic, Late bloomer 등) 발견
- → 이론 확장 제안

**시나리오 D: K=1 또는 2 (궤적 유형 미분화)**
- → 교육 맥락에서는 궤적 분화가 덜 뚜렷할 수 있음
- → negative result도 C&E에 기여 가능 (behavioral proxy의 한계 논의)

---

## 4. Phase 3: Validation & Outcomes (Python + R)

### 4.1 궤적 유형 예측 모델 (RQ3)

**스크립트:** `analysis/scripts/06_predict_trajectory.py`

학습자의 **초기 행동** (첫 10% 에피소드)으로 궤적 유형 예측:

| 예측 변수 | 계산 | 가설 |
|-----------|------|------|
| `initial_accuracy` | 첫 10% 에피소드 정답률 | 높으면 Convergent 가능성↑ |
| `initial_expl_rate` | 첫 10% 해설 열람 비율 | 높으면 Convergent (적극적 모니터링) |
| `initial_expl_depth` | 첫 10% 평균 해설 시간 | 깊으면 Convergent |
| `initial_adaptive` | 첫 10%에서 adaptive_offer 경험 여부 | 시스템 경험 차이 |
| `platform_ratio` | mobile vs web 비율 | 학습 맥락 차이 |
| `session_regularity` | 세션 간 시간 간격의 CV | 규칙적 학습 = Convergent? |
| `part_diversity` | 풀이한 TOEIC part 종류 수 | 학습 폭 |

**분석:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Multinomial logistic regression
model = LogisticRegression(multi_class='multinomial', max_iter=1000)
scores = cross_val_score(model, X_initial, y_trajectory, cv=10, scoring='accuracy')
```

### 4.2 학습 성과 비교 (RQ4)

**학습 성과 지표:**

| 지표 | 계산 | 의미 |
|------|------|------|
| `accuracy_gain` | 마지막 20% 정답률 − 첫 20% 정답률 | 학습 향상도 |
| `final_accuracy` | 마지막 20% 에피소드 정답률 | 최종 수준 |
| `efficiency` | accuracy_gain / log(n_episodes) | 학습 효율성 |

**예상 결과:**

```
                   Accuracy Gain
Convergent    ████████████████████ (가장 높음)
Oscillating   ████████████████     (중간)
Stagnant      ████████             (가장 낮음)
```

**통계 검정:**
- 정규성 확인 (Shapiro-Wilk)
- 정규: One-way ANOVA + Tukey HSD post-hoc
- 비정규: Kruskal-Wallis + Dunn's test
- 효과 크기: η² (ANOVA) 또는 ε² (K-W)

### 4.3 교차 검증: Tier 1 실험 데이터

**목적:** EdNet에서 발견한 K개 궤적 유형이 통제된 실험 데이터에서도 재현되는가?

| 데이터셋 | N | 시점 수 | Trust 측정 | 접근 |
|---------|---|--------|----------|------|
| **Rittenberg et al. (2024)** | 147 | 30 | VAS 0-100 | 직접 trust 측정 |
| **Zouhar et al. (2023)** | 332 | 56 | Betting amount | 행동적 trust |
| **Lu & Yin (2021)** | ~300 | ~15 | 7-point + switching | 자기보고 + 행동 |

**분석:**
1. 각 데이터셋에서 동일 GMM 절차 적용
2. 최적 K 수 비교 (EdNet K와 일치하는가?)
3. 궤적 형태 비교 (slope, curvature 유사성)
4. 결론: 일치하면 → 모델 일반화, 불일치하면 → 맥락 의존성 논의

---

## 5. 예상 논문 구조 (Computers & Education)

### 제목

**"How Learners Calibrate Trust in AI: Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System"**

### 구조

| Section | 내용 | 예상 분량 |
|---------|------|---------|
| **1. Introduction** | AI trust calibration 문제, T × R × τ 모델, 궤적 유형 예측, RQ 제시 | 2-3 pages |
| **2. Theoretical Background** | Lee & See (2004), Guo & Yang (2021) 3유형, Calibration Gap 개념 | 3-4 pages |
| **3. Method** | EdNet KT3 소개, Trust proxy 구성, GMM 절차, 교차 검증 전략 | 4-5 pages |
| **4. Results** | RQ1-4 결과, 궤적 시각화, 모델 비교표, 예측 모델, 성과 비교 | 5-6 pages |
| **5. Cross-Validation** | Tier 1 데이터 결과 (재현 여부) | 2-3 pages |
| **6. Discussion** | 이론적 함의, 교육적 시사점, 한계, 향후 연구 | 3-4 pages |
| **합계** | | ~20-25 pages |

### 핵심 Figures (예상)

| Figure | 내용 |
|--------|------|
| Fig 1 | T × R × τ 이론 모델 (2D matrix + 3D 확장) |
| Fig 2 | Trust proxy 구성 과정 다이어그램 |
| Fig 3 | BIC/Entropy 모델 비교 |
| Fig 4 | **궤적 유형별 Calibration Gap 시계열** (핵심 figure) |
| Fig 5 | 궤적 유형별 학습 성과 비교 |
| Fig 6 | 교차 검증 결과 (EdNet vs Tier 1) |

### 핵심 Tables

| Table | 내용 |
|-------|------|
| Table 1 | EdNet KT3 기술통계 (전체 + 분석 대상) |
| Table 2 | Trust proxy 변수 조작적 정의 |
| Table 3 | GMM 모델 비교 (K=1~6, BIC, AIC, Entropy, BLRT) |
| Table 4 | 궤적 유형별 기술통계 (N, %, 평균 gap, 평균 accuracy) |
| Table 5 | Multinomial logistic regression 결과 |
| Table 6 | 궤적 유형별 학습 성과 비교 |
| Table 7 | 교차 검증 결과 요약 |

---

## 6. 예상 기여 및 한계

### 기여

| # | 기여 | Computers & Education 적합도 |
|---|------|---------------------------|
| C1 | AI 튜터링에서 Trust calibration 궤적의 실증적 유형 분류 (N=68K) | ★★★★★ 대규모 실증 |
| C2 | T × R × τ 이론 모델의 첫 실증 검증 | ★★★★☆ 이론-실증 연결 |
| C3 | 행동 로그 기반 Trust proxy 구성 방법론 제안 | ★★★★★ 방법론 기여 |
| C4 | 초기 행동으로 궤적 예측 → 조기 개입 가능성 | ★★★★★ 교육적 시사점 |
| C5 | 교차 검증으로 도메인 간 일반화 확인 | ★★★★☆ 견고성 |

### 예상 한계 및 대응

| 한계 | 심각도 | 대응 |
|------|--------|------|
| Trust proxy는 자기보고가 아닌 행동 추론 | ⚠️ 중간 | Tier 1 자기보고 데이터로 교차 검증 |
| adaptive_offer가 전체의 5%에 불과 | ⚠️ 중간 | Gap_B (explanation 기반) 병렬 분석 |
| 인구통계 변수 없음 | ⚠️ 낮음 | 연구 맥락에서 불필요 (행동 궤적 자체가 초점) |
| TOEIC 맥락 특수성 | ⚠️ 낮음 | Tier 1 다양한 도메인으로 일반화 확인 |
| 시간 정규화의 정보 손실 | ⚠️ 낮음 | 절대 시간 기반 보조 분석 |

---

## 7. 실행 계획

### 스크립트 목록

| 순서 | 파일명 | 언어 | 입력 | 출력 |
|------|--------|------|------|------|
| 1 | `01_filter_students.py` | Python | raw/KT3/ | filtered_student_list.csv |
| 2 | `02_parse_episodes.py` | Python | raw/KT3/ + questions.csv | all_episodes.parquet |
| 3 | `03_compute_trust_proxies.py` | Python | all_episodes.parquet | trust_proxies.parquet |
| 4 | `04_time_normalize.py` | Python | trust_proxies.parquet | ventile_matrix.csv |
| 5 | `05_gmm_analysis.R` | R | ventile_matrix.csv | class_assignments.csv + model_comparison.csv |
| 6 | `06_predict_trajectory.py` | Python | all_episodes + assignments | prediction_results.csv |
| 7 | `07_learning_outcomes.py` | Python | all_episodes + assignments | outcome_comparison.csv |
| 8 | `08_cross_validation.R` | R | tier1 data files | cross_validation_results.csv |
| 9 | `09_generate_figures.py` | Python | all results | figures/*.png |
| 10 | `run_pipeline.py` | Python | — | 전체 파이프라인 실행 (subprocess) |

### Python ↔ R 인터페이스

```python
# run_pipeline.py 핵심 구조
import subprocess

# Steps 1-4: Python
exec(open('01_filter_students.py').read())
exec(open('02_parse_episodes.py').read())
exec(open('03_compute_trust_proxies.py').read())
exec(open('04_time_normalize.py').read())

# Step 5: R (via subprocess)
subprocess.run(['Rscript', '05_gmm_analysis.R'], check=True)

# Steps 6-9: Python
exec(open('06_predict_trajectory.py').read())
exec(open('07_learning_outcomes.py').read())

# Step 8: R (via subprocess)
subprocess.run(['Rscript', '08_cross_validation.R'], check=True)

# Step 9: Final figures
exec(open('09_generate_figures.py').read())
```

### 계산 비용 추정

| 단계 | 대상 | 예상 시간 |
|------|------|---------|
| 필터링 | 297,915 파일 | ~10분 (파일 크기만 확인) |
| 에피소드 파싱 | ~68,000 파일 | ~30분-1시간 |
| Trust proxy | ~68,000 × 150 episodes | ~15분 |
| 시간 정규화 | ~68,000 학생 | ~5분 |
| GMM (K=1~6) | 68,000 × 20 matrix | ~1-4시간 (R mclust) |
| 전체 파이프라인 | — | ~3-6시간 |

---

## 8. 미해결 설계 결정

### 결정 필요 사항

| # | 질문 | 옵션 | 현재 기본값 |
|---|------|------|-----------|
| D1 | Calibration gap 주 정의 | Gap_A (adaptive) vs Gap_B (explanation) vs 둘 다 | **둘 다** (민감도) |
| D2 | Rolling window 크기 | 10 / 20 / 30 episodes | **20** |
| D3 | 최소 에피소드 기준 | 50 / 100 / 200 | **100** |
| D4 | Ventile 수 | 10 / 20 / 30 | **20** |
| D5 | GMM variance 구조 | varying / equal | **varying** |
| D6 | Tier 1 데이터 포함 범위 | Rittenberg만 / 3개 모두 | **3개 모두** |

이 기본값들은 Phase 1 완료 후 예비 분석 결과를 보고 조정할 수 있음.

---

## 참고문헌

- Guo, Y., & Yang, X. J. (2021). Modeling and predicting trust dynamics in human-robot teaming. *IJSR*, 12, 459-478.
- Chung, S., & Yang, X. J. (2024). Predicting trust dynamics with personal characteristics. *HFES*, 68(1).
- Lee, J. D., & See, K. A. (2004). Trust in automation. *Human Factors*, 46(1), 50-80.
- Choi, Y., et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. *AIED 2020*.
- Rittenberg, B., et al. (2024). Trust with increasing and decreasing reliability. *Human Factors*, 66(11).
- Zouhar, V., et al. (2023). A diachronic perspective on user trust in AI under uncertainty. *EMNLP 2023*.
- Lu, Z., & Yin, M. (2021). Human reliance on ML models. *CHI 2021*.
- Muthén, B. (2004). Latent variable analysis: Growth mixture modeling. *Handbook of Quantitative Methodology for the Social Sciences*.
- Jung, T., & Wickrama, K. A. S. (2008). An introduction to latent class growth analysis and growth mixture modeling. *Social and Personality Psychology Compass*, 2(1), 302-317.
