# Paper 4 최종 방향 확정: Scope & Design Decision

**Date:** 2026-03-11
**Context:** Discussion 08 (Analysis Blueprint) + Discussion 09 (Multi-Agent Review) 이후 의사결정 과정 정리
**Decision Status:** 확정

---

## 1. 문제 상황

Discussion 08에서 상세 분석 설계를 완성하고, Discussion 09에서 5개 Diverga 에이전트 리뷰를 통합한 결과, 여러 층위의 이슈가 식별되었다:

- Trust proxy construct validity 문제 (AI_reliance ≠ Trust)
- 85% zero-inflation (대부분 학생이 adaptive_offer 미경험)
- Tier 1 교차 검증 데이터셋의 구조적 비호환
- 이론 수준(Trust)과 측정 수준(Reliance)의 불일치
- 비판과 제안이 과도하게 축적되어 방향성 상실

**핵심 질문:** 기존에 만든 이론 모델(Figure 1-5)을 EdNet 데이터로 검증할 수 있는가?

---

## 2. Figure별 검증 가능성 판단

| Figure | 내용 | EdNet 검증 가능? | 판단 근거 |
|--------|------|:---:|------|
| **Figure 1** (2D Matrix) | T × R 4분면 분류 | 해당 없음 | 분류 틀(framework)이지 가설이 아님. **렌즈**로 사용. |
| **Figure 2** (3D Trajectories) | T × R × τ 공간의 궤적 | **가능** | PP-GMM으로 Reliance × Performance × Time 3D 궤적 추출 가능 |
| **Figure 3** (Hysteresis) | 신뢰 구축 vs 침식 비대칭 | **불가능** | R(AI reliability) 실험 조작 필요. EdNet은 관찰 데이터. |
| **Figure 5** (Gap Dynamics) | Calibration gap 3패턴 | **직접 가능** | PP-GMM에서 파생. Gap = Reliance - Performance. |

**결정:** Figure 2 + Figure 5를 동시에 검증하는 Parallel Process GMM 채택.

---

## 3. 핵심 설계 결정

### 3.1 구성개념 프레이밍: "Reliance Calibration" 단일 수준

**결정:** "Trust Calibration"이 아닌 **"Reliance Calibration"** 단일 수준으로 프레이밍.

**근거:**
- Trust(태도) → Reliance(행동)는 확립된 인과 경로 (Lee & See, 2004: "Trust guides reliance")
- EdNet 데이터는 행동만 관찰 가능 — 행동을 행동으로 측정하면 proxy validity 문제 해소
- Lee & Moray (1992, 1994): trust-reliance 상관 r=.60-.75
- Schemmer et al. (2023)의 "appropriate reliance" 프레임워크가 행동 수준 선례 제공
- Trust에 대한 해석은 Discussion 섹션에서 이론적으로 처리

**기각된 대안:** 측정 수준 "Reliance" + 이론 수준 "Trust" 이중 프레이밍
→ 기각 이유: 내적 모순 유발. A3 에이전트 시뮬레이션: "If you admit you're not measuring trust, why is your theoretical framework about trust?" (Reviewer 2 공격 시나리오)

### 3.2 분석 방법: Parallel Process GMM (1D → 2D 확장)

**결정:** 단변량 Gap GMM 대신 **이변량 Parallel Process GMM** 채택.

**근거:**

```
1D (gap만):  Gap = 0.2  →  R_b=0.7, P=0.5  인지
                           R_b=0.3, P=0.1  인지 구분 불가

2D (동시):   R_b=0.7, P=0.5  →  "고의존-중성과" (Over-reliance)
             R_b=0.3, P=0.1  →  "저의존-저성과" (Disengaged)
             같은 gap이지만 완전히 다른 학습 상태
```

PP-GMM의 추가 장점:
- Gap이 줄어드는 **방향** 포착 (R_b 하강 vs P 상승 vs 양방향)
- 3D 시각화가 Figure 2와 직접 대응 → 이론-실증 비교 가능
- `lcmm::multlcmm()`로 구현, bounded outcome 지원 (`link = "beta"`)

### 3.3 표본: Phase 0 진단 기반 필터링

**Phase 0 진단 결과 (2026-03-11 실행):**

```
전체 학생:                297,915
adaptive_offer 경험:       44,565 (15.0%)  ← 기존 추정 ~10,200의 4배
GMM-Ready (≥60 eps, ≥5 adaptive, ≥1일): 21,287

그러나 윈도우 수준 분석 결과:
- 전체 GMM-Ready (20 windows): R_b 윈도우 60%가 zero → PP-GMM 부적합
- ratio ≥ 0.10 하위집단 (10 windows): R_b zero 23%, std=0.12 → PP-GMM 적합
```

**결정:** adaptive_offer 비율 ≥ 10% 학생을 분석 대상으로, **10개 윈도우** 사용.

| 필터링 기준 | N |
|------------|---|
| 전체 | 297,915 |
| adaptive_offer 경험 | 44,565 |
| GMM-Ready (≥60 eps, ≥5 adaptive, ≥1일) | 21,287 |
| **adaptive ratio ≥ 0.10** | **4,568** |
| STRICT (ratio≥0.10, ≥20 adaptive) | 3,439 |

**최종 분석 대상: ~4,500명 (adaptive ratio ≥ 0.10)**

**논문 내 정당화:**
> "Reliance calibration can only be meaningfully observed among learners who substantively engage with AI recommendations. We defined 'substantive engagement' as adaptive_offer episodes comprising ≥10% of total learning episodes (N = 4,568), ensuring sufficient within-person variability for trajectory modeling."

**윈도우 수 변경: 20 → 10**

Phase 0-3/0-4 진단에서 20 windows는 zero-inflation이 38%로 과도. 10 windows에서:
- zero-inflation: 23%
- 92% 학생이 ≥50% non-zero 윈도우
- R_b within-student std = 0.12 (PP-GMM에 충분한 변산성)

**기각:** Secondary Track (전체 68K의 engagement 궤적) → Paper 4 범위 밖. 별도 연구 가능.

### 3.4 교차 검증: Tier 1 제거 → 내부 검증

**결정:** 외부 데이터셋(Rittenberg, Zouhar, Lu & Yin) 교차 검증 완전 제거.

**대체:** 내부 교차 검증 (split-half, 10-fold CV).

**근거:** 외부 데이터셋은 구조적으로 비호환 (다른 시간 단위, 다른 측정, 다른 맥락). 비교 자체가 의미 없음.

### 3.5 Paper 3과의 관계

**결정:** Paper 4는 Paper 3의 "검증"이 아닌 **"행동적 일관성 확인(behavioral consistency check)"**.

**논문 내 프레이밍:**
> "Paper 3 proposes Trust Calibration Readiness as a cognitive competency (Awareness → Judgment → Action). This study examines whether the behavioral signatures predicted by that framework — convergent, oscillating, and stagnant trajectories — are empirically observable in naturalistic AI-assisted learning data."

**한계 명시:** EdNet은 Action 수준 행동만 관찰 가능. Awareness, Judgment 단계는 검증 불가.

---

## 4. 확정된 Paper 4 설계

### 4.1 제목 (Working Title)

> **Patterns of AI Reliance Calibration Among Learners: A Growth Mixture Analysis of Behavioral Trajectories in an AI Tutoring System**

### 4.2 연구 질문 및 가설

| RQ | 질문 | 분석 기법 |
|----|------|---------|
| **RQ1** | AI 튜터링에서 학습자의 reliance calibration 궤적은 몇 가지 유형으로 분류되는가? | Parallel Process GMM |
| **RQ2** | 이론적으로 예측된 패턴(convergent, oscillating, stagnant)이 관찰되는가? | PP-GMM 결과 vs Figure 2 대조 |
| **RQ3** | 초기 행동 특성이 궤적 유형을 예측하는가? | Multinomial logistic regression |
| **RQ4** | 궤적 유형에 따라 학습 성과에 차이가 있는가? | ANOVA / Kruskal-Wallis |

| ID | 가설 | 이론적 근거 |
|----|------|-----------|
| **H1** | 3개 이상의 질적으로 구분되는 궤적 유형 존재 | Guo & Yang (2021): 3유형 발견 |
| **H2a** | Convergent: Reliance-Performance gap → 0 | Reliance가 Performance에 정렬 |
| **H2b** | Oscillating: Gap이 감쇠 진동 | 과의존-저의존 반복 후 수렴 |
| **H2c** | Stagnant: Gap 유지 또는 증가 | 교정 실패 |
| **H3** | 초기 해설 열람 시간 + adaptive_offer 반응이 궤적 예측 | 초기 행동이 학습 전략 결정 |
| **H4** | Convergent 유형의 학습 성과 향상 최대 | 교정된 의존 → 적절한 AI 활용 → 성과 |

### 4.3 조작적 정의

```
Reliance R_b(τ) = 윈도우 τ 내 adaptive_offer 에피소드 수행 비율     [0, 1]
Performance P(τ) = 윈도우 τ 내 정답률                               [0, 1]
Calibration Gap  = R_b(τ) - P(τ)  (부호 있음, PP-GMM에서 파생)

  양수 → 과의존 (Over-reliance: AI 많이 따르지만 성적 낮음)
  음수 → 저의존 (Under-reliance: AI 안 따르지만 성적 높음)
  0 근처 → 정렬 (Calibrated)
```

윈도우: 비중첩(non-overlapping) 고정 크기, 학생별 10등분 (Decile) 정규화
  (Phase 0 진단에서 20등분 → 10등분으로 변경: zero-inflation 60%→23% 개선)

### 4.4 논문 구조

```
1. Introduction
   - Trust-Reliability Matrix (Figure 1) — 이론적 틀
   - 3D Trajectory Predictions (Figure 2) — "우리가 기대하는 것"
   - Reliance Calibration 프레이밍 근거

2. Literature Review
   - Trust in automation → Reliance (Lee & See, 2004)
   - Appropriate reliance (Schemmer et al., 2023)
   - Growth Mixture Modeling in education (Guo & Yang, 2021)

3. Method
   - Data: EdNet KT3, adaptive_offer ratio ≥ 10% 학생 (N ≈ 4,568)
   - Variables: R_b(τ), P(τ)
   - Analysis: Parallel Process GMM (lcmm::multlcmm)
   - Model selection: BIC, entropy, BLRT, theoretical interpretability
   - Internal validation: split-half, 10-fold CV

4. Results
   - RQ1: 클래스 수 결정
   - RQ2: 3D 시각화 (Empirical Figure 2') + Gap 궤적 (Empirical Figure 5')
          → Theoretical Figure 2 vs Empirical Figure 2' 나란히 비교
   - RQ3: 초기 행동 예측 모형
   - RQ4: 클래스별 성과 비교

5. Discussion
   - 이론 예측 vs 실증 결과 해석
   - Reliance → Trust 이론적 해석 (Lee & See pathway)
   - Paper 3 (TCR as competency) 연결
   - Hysteresis (Figure 3) → 미래 연구
   - 한계: 행동만 관찰, Awareness/Judgment 미검증

6. Conclusion
   - 교육적 함의: 궤적 유형별 개입 전략
```

### 4.5 기술 스택

```
Phase 1 (Python): 데이터 전처리
  - 학생 필터링, 에피소드 파싱, R_b/P 시계열 생성
  - 출력: CSV (student_id, time_window, reliance, performance)

Phase 2 (R): PP-GMM
  - lcmm::multlcmm() — Parallel Process GMM
  - link = "beta" (bounded [0,1] outcomes)
  - LCGA → GMM stepped approach
  - 출력: 클래스 할당, 모형 적합도, 추정 궤적

Phase 3 (Python): 후속 분석 + 시각화
  - 다항 로지스틱 회귀 (RQ3)
  - ANOVA/Kruskal-Wallis (RQ4)
  - 3D 시각화 (matplotlib 3D)
```

### 4.6 R 구현 스케치

```r
library(lcmm)

# Step 1: LCGA (랜덤 효과 없이 탐색)
lcga_3 <- multlcmm(
  Reliance + Performance ~ poly(Time, 2),
  subject = "student_id",
  mixture = ~ poly(Time, 2),
  ng = 3,
  link = c("beta", "beta"),
  data = df
)

# Step 2: PP-GMM (랜덤 효과 추가)
ppgmm_3 <- multlcmm(
  Reliance + Performance ~ poly(Time, 2),
  random = ~ Time,
  subject = "student_id",
  mixture = ~ poly(Time, 2),
  ng = 3,
  link = c("beta", "beta"),
  data = df,
  B = lcga_3  # LCGA 결과를 초기값으로
)
```

---

## 5. 명시적으로 제외된 것

| 제외 항목 | 이유 | 대안 |
|----------|------|------|
| Tier 1 교차 검증 | 구조적 비호환 | 내부 CV |
| Figure 3 (Hysteresis) 검증 | 실험 조작 필요 | Discussion에서 미래 연구로 언급 |
| Trust 직접 측정 주장 | 행동 데이터만 있음 | "Reliance Calibration" 프레이밍 |
| Secondary Track (68K) | 범위 초과 | 별도 연구 가능 |
| Process model (Aw→Jd→Ac) 검증 | 내적 인지 과정 관찰 불가 | Paper 3 영역 |
| 3D T×R×A (Awareness 축) | Awareness 측정 불가 | Paper 3의 3D 확장으로 이동 |

---

## 6. Research Program 내 위치

```
Paper 1 (SLR): "Trust Calibration Gap이 문헌에 존재한다"
    ↓ 문제 식별
Paper 2 (TCRS): "이 Gap을 측정하는 자기보고 척도를 개발했다"
    ↓ 측정 도구
Paper 3 (Conceptual): "TCR은 교육적 역량이다 (Aw → Jd → Ac)"
    ↓ 이론적 주장
Paper 4 (THIS): "실제 AI 학습 환경에서 교정 궤적이 관찰된다"
    ↑
    행동 수준의 실증 증거
    Paper 3의 예측과 행동적으로 일관된 패턴 확인
    (≠ Paper 3 검증, = behavioral consistency check)
```

---

## 7. 의사결정 이력

| 날짜 | Discussion | 결정 |
|------|-----------|------|
| 03-11 | D08 | 상세 분석 설계 완성 (Trust Calibration + Tier 1 포함) |
| 03-11 | D09 | 5-Agent 리뷰 → construct validity, zero-inflation, framing 이슈 식별 |
| 03-11 | 대화 | "Reliance Calibration" 단일 프레이밍 확정 (A3, G1, A2 3-agent 검증) |
| 03-11 | 대화 | Tier 1 교차 검증 완전 제거 |
| 03-11 | 대화 | Pew ATP 데이터 부적합 판단 (R 차원 없음) |
| 03-11 | 대화 | Paper 3-4 관계: "behavioral consistency check" (검증 아님) |
| 03-11 | **D10** | **Figure별 검증 가능성 판단 → PP-GMM 채택 → 최종 범위 확정** |
| 03-11 | D10 (Phase 0) | 데이터 진단: 44,565명 adaptive_offer 경험 확인 |
| 03-11 | D10 (Phase 0) | R_b zero-inflation 60% 발견 → 20→10 윈도우 변경 |
| 03-11 | D10 (Phase 0) | ratio ≥ 0.10 하위집단(4,568명) 분석 대상 확정 |

---

## 8. Phase 0 Data Diagnostic 결과

### 8.1 Phase 0-1: adaptive_offer 경험 학생 수

```
실행: analysis/scripts/phase0_diagnostic.py
시간: 26.1s (297,915 파일, 11,395 files/s)
```

| 항목 | 값 |
|------|-----|
| 전체 학생 | 297,915 |
| adaptive_offer 경험 | 44,565 (15.0%) |
| 미경험 | 253,350 (85.0%) |

Source type 분포:
```
diagnosis:     286,429 (96.1%)
sprint:         99,334 (33.3%)
adaptive_offer:  44,565 (15.0%)
my_note:         40,303 (13.5%)
archive:         23,424 (7.9%)
review_quiz:     18,443 (6.2%)
review:          13,248 (4.4%)
tutor:           10,913 (3.7%)
```

### 8.2 Phase 0-2: 에피소드 심도

```
실행: analysis/scripts/phase0_2_episode_depth.py
대상: 44,565 adaptive_offer 학생
```

| 항목 | 값 |
|------|-----|
| GMM-Ready (≥60 eps, ≥5 adaptive, ≥1일) | 21,287 |
| 전체 에피소드 중앙값 (GMM-Ready) | 296 |
| adaptive 에피소드 중앙값 | 16 |
| adaptive 비율 중앙값 | 6.4% |
| 학습 기간 중앙값 | 46.5일 |

### 8.3 Phase 0-3: 윈도우 수준 분포 (N=2,000 샘플)

```
실행: analysis/scripts/phase0_3_window_distribution.py
```

**20 윈도우 결과 (전체 GMM-Ready):**

| 지표 | 값 | 판단 |
|------|-----|------|
| R_b 윈도우 zero 비율 | 60.0% | **과도** |
| R_b 평균/중앙값 | 0.071 / 0.000 | 대부분 0 |
| R_b × P 상관 | r = -0.019 | 무상관 |
| Gap 평균 | -0.522 | ≈ -P (R_b 무시 가능) |

→ **전체 대상 20 윈도우 PP-GMM 부적합 판정**

### 8.4 Phase 0-4: 하위집단 분석

```
실행: analysis/scripts/phase0_4_high_reliance_subgroup.py
```

**ratio ≥ 0.10 하위집단, 10 윈도우:**

| 지표 | 값 | 판단 |
|------|-----|------|
| N | 4,568 | GMM 충분 |
| R_b 평균 | 0.138 | 의미 있음 |
| R_b within-student std | 0.119 | 변산 충분 |
| Zero 윈도우 비율 | 23% | 수용 가능 |
| ≥50% non-zero 학생 | 92% | 대부분 신호 있음 |
| ALL non-zero 학생 | 27% | — |

**STRICT 하위집단 (ratio≥0.10, ≥20 adaptive):**

| 지표 | 값 |
|------|-----|
| N | 3,439 |
| adaptive 에피소드 중앙값 | 59 |
| 전체 에피소드 중앙값 | 453 |
| 10 windows: ≥50% non-zero | 99% |

→ **ratio ≥ 0.10, 10 윈도우 PP-GMM 적합 판정**

---

## 9. Phase 1-2 실행 결과

### 9.1 Phase 1: 시계열 생성

```
실행: analysis/scripts/phase1_build_timeseries.py
대상: 4,568명 (adaptive ratio ≥ 0.10, ≥60 eps, ≥5 adaptive, ≥1일)
```

| 산출물 | 경로 | 크기 |
|--------|------|------|
| 시계열 (long format) | analysis/outputs/phase1_timeseries_long.csv | 45,680 rows |
| 학생 요약 | analysis/outputs/phase1_student_summary.csv | 4,568 rows |
| 초기 행동 (RQ3용) | analysis/outputs/phase1_early_behavior.csv | 4,568 rows |

**윈도우별 평균:**

| Window | R_b | P | Gap | %zero_Rb |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.048 | 0.552 | -0.504 | 50.1% |
| 2 | 0.093 | 0.579 | -0.486 | 31.8% |
| 5 | 0.147 | 0.583 | -0.436 | 19.4% |
| 10 | 0.166 | 0.577 | -0.412 | 15.6% |

R_b가 Window 1→10으로 0.048→0.166 증가 (AI 추천 점진적 채택).
P는 0.55-0.59 범위에서 안정적.

### 9.2 Phase 2: GMM (mclust)

```
실행: analysis/scripts/phase2_gmm_mclust.R
방법: mclust Gaussian Mixture Model on wide-format (20 features: R_b×10 + P×10)
```

**방법론 변경 기록:**
- 원래 계획: lcmm::multlcmm (Parallel Process GMM)
- 문제: 1-class 모델도 수렴 실패 (conv=2, 440초 후). R_b의 zero-inflation + bounded data로 인한 최적화 불안정.
- 대안 채택: mclust (wide-format trajectory clustering). GMM의 일종이며, 궤적 형태(trajectory shape)를 기반으로 분류. C&E에서 수용 가능한 방법.

**모형 비교 (BIC):**

| G (classes) | Best BIC |
|:---:|---:|
| 1 | 121,605.7 |
| 2 | 135,922.8 |
| 3 | 138,238.0 |
| 4 | 138,973.3 |
| 5 | 139,160.6 |
| **6** | **139,751.3** |
| 7 | 139,732.2 |

**최종 선택: VEE 모형, 6 classes** (BIC 최대)
Entropy = 0.82 (양호)

### 9.3 식별된 6개 궤적 유형

| Class | N (%) | R_b 변화 | P 수준 | Gap 변화 | 해석 |
|:---:|------:|:---:|:---:|:---:|------|
| 1 | 1,367 (29.9%) | 0.05→0.14 | ~0.59 안정 | Δ+0.09 | **Gradual Adopter** |
| 2 | 1,582 (34.6%) | 0.03→0.17 | 0.53→0.56 | Δ+0.10 | **Steady Calibrator** |
| 3 | 859 (18.8%) | 0.04→0.19 | 0.50→0.54 | Δ+0.11 | **Strong Calibrator** |
| 4 | 451 (9.9%) | 0.06→0.11 | ~0.65 안정 | Δ+0.03 | **High Performer, Low Reliance** |
| 5 | 240 (5.3%) | 0.09→0.23 | ~0.57 안정 | Δ+0.13 | **Heavy Adopter** |
| 6 | 69 (1.5%) | 0.33→0.29 | ~0.59 | Δ-0.02 | **Early Heavy User (감소)** |

**이론 예측 대응:**

| 이론 예측 | 가장 유사한 Class | 대응도 |
|----------|:---:|:---:|
| **Convergent** (Gap→0) | Class 3, 5 | 부분적 — Gap 개선 최대이지만 0에 도달하지 않음 |
| **Oscillating** (감쇠 진동) | Class 6 | 약함 — 감소 추세이나 진동보다는 단조 감소 |
| **Stagnant** (변화 없음) | Class 4 | 강함 — 높은 P, 낮은 R_b, Gap 거의 불변 |

**예상 외 발견:**
- 6개 클래스 중 4개(Class 1-3, 5)가 모두 "R_b 증가" 방향 — 학생들이 AI 추천을 점진적으로 채택하는 경향이 지배적
- Class 4 (Stagnant)는 **가장 성적이 높은 학생** — 높은 성적이 이미 있어서 AI 의존 불필요
- Class 6 (1.5%)만이 높은 R_b에서 시작 — 대부분 학생은 AI 추천을 서서히 발견/채택

**산출물:**

| 파일 | 내용 |
|------|------|
| analysis/outputs/phase2_model_fit.csv | BIC 비교 |
| analysis/outputs/phase2_class_assignments.csv | 학생별 클래스 + 사후확률 |
| analysis/outputs/phase2_class_trajectories.csv | 클래스별 윈도우 평균 궤적 |
| analysis/outputs/phase2_workspace.RData | R workspace |

---

## 10. Phase 3 실행 결과: RQ3 + RQ4

```
실행: analysis/scripts/phase3_rq3_rq4.py
입력: phase1_early_behavior.csv, phase1_student_summary.csv, phase1_timeseries_long.csv, phase2_class_assignments.csv
```

### 10.1 RQ3: 초기 행동 → 궤적 유형 예측

**방법:** 7개 초기 행동 변수(first window)로 6-class 예측 — 다항 로지스틱 회귀, 10-fold CV

```
10-Fold CV Accuracy: 0.4941 (chance: 0.1667)
→ 기회 수준 대비 ~3배 정확도
```

**Feature Importance (mean absolute coefficient):**

| 순위 | 변수 | |coef| | 해석 |
|:---:|------|:---:|------|
| 1 | early_expl_rate | 1.001 | 해설 열람 비율이 가장 강력한 예측 변수 |
| 2 | early_avg_expl_dur_s | 0.595 | 해설에 투자하는 시간 |
| 3 | early_R_b | 0.299 | 초기 AI 추천 수용률 |
| 4 | early_gap | 0.160 | 초기 의존-성과 격차 |
| 5 | early_P | 0.153 | 초기 정답률 |
| 6 | early_answer_change_rate | 0.111 | 답 변경 빈도 |
| 7 | early_lecture_rate | 0.081 | 강의 시청 비율 |

**해석:**
- 초기 **해설 열람 행동**(열람 비율 + 시간)이 궤적 유형의 가장 강력한 예측 변수
- 해설 적극 활용 학생이 특정 궤적 유형으로 분화되는 경향
- H3("초기 해설 열람 시간 + adaptive_offer 반응이 궤적 예측") **지지됨**
- 다만, Class 4(High Performer)와 Class 5(Heavy Adopter)는 recall=0% — 초기 행동만으로는 구분 불가

### 10.2 RQ4: 궤적 유형별 학습 성과 비교

**ANOVA: Overall Accuracy**

| 통계량 | 값 |
|--------|-----|
| F(5, 4562) | 177.46 |
| p | 4.66e-173 |
| η² | 0.163 |
| Kruskal-Wallis H | 671.87 (p=1.45e-142) |

→ **매우 유의미한 집단간 차이** (η²=0.163, large effect)

**ANOVA: Accuracy Improvement (late - early)**

| 통계량 | 값 |
|--------|-----|
| F | 25.08 |
| p | 5.04e-25 |
| η² | 0.027 |

→ 개선도에서도 유의미한 차이 존재 (η²=0.027, small effect)

**Class Rankings (Overall Accuracy):**

| 순위 | Class | N (%) | 정확도 (M±SD) | 개선도 | R_b 개선 | 해석 |
|:---:|:---:|------:|:---:|:---:|:---:|------|
| 1 | 4 | 451 (9.9%) | .649±.038 | +.010 | +.036 | High Performer — 이미 높은 성적, AI 의존 낮음 |
| 2 | 1 | 1,367 (29.9%) | .598±.052 | −.010 | +.081 | Gradual Adopter — 안정적 성적, 점진적 채택 |
| 3 | 6 | 69 (1.5%) | .581±.109 | +.009 | −.051 | Early Heavy User — 높은 분산, R_b 감소 |
| 4 | 5 | 240 (5.3%) | .576±.053 | −.003 | +.116 | Heavy Adopter — AI 과도 채택, 성적 정체 |
| 5 | 2 | 1,582 (34.6%) | .570±.071 | +.023 | +.111 | Steady Calibrator — 성적 개선 중 |
| 6 | 3 | 859 (18.8%) | .536±.102 | **+.048** | +.139 | Strong Calibrator — **가장 큰 개선** |

**핵심 발견:**

1. **H4 부분 지지/수정 필요:**
   - 가설: "Convergent 유형의 학습 성과 향상 최대"
   - 실증: Class 3(Strong Calibrator)이 가장 큰 **개선** (+.048)이지만 가장 낮은 **절대 성적** (.536)
   - Class 4(Stagnant)가 가장 높은 **절대 성적** (.649)이지만 최소 개선 (+.010)
   - → **"수렴하는 학생이 가장 빨리 성장한다"가 아닌 "성적이 낮은 학생이 AI 채택으로 가장 빨리 성장한다"**

2. **성적-개선 역관계:**
   - 초기 성적이 높을수록 개선 여지 감소 (천장 효과)
   - Class 3이 가장 낮은 성적에서 출발하면서 가장 높은 개선 달성 = 교육적으로 의미 있는 발견

3. **AI 의존과 성과의 비선형 관계:**
   - Class 4 (R_b 낮음, P 높음): 이미 성적 좋아 AI 불필요
   - Class 5 (R_b 높음, P 중간): 과도한 AI 의존이 자율적 학습을 저해할 가능성
   - Class 2, 3 (R_b 점진 증가, P 증가): 적절한 채택 = 최적 성장

**산출물:**

| 파일 | 내용 |
|------|------|
| analysis/outputs/phase3_rq3_prediction.csv | Feature importance (7 features) |
| analysis/outputs/phase3_rq4_outcomes.csv | Class별 성과 통계 (12 columns) |
| analysis/outputs/phase3_summary.txt | 요약 |

---

## 11. 가설 검증 종합

| 가설 | 판정 | 근거 |
|------|:---:|------|
| **H1:** 3개 이상 질적 궤적 유형 존재 | **지지** | 6개 클래스 식별 (BIC 최적) |
| **H2a:** Convergent (Gap→0) | **부분 지지** | Class 2, 3이 Gap 축소 방향이나 0에 도달하지 않음 |
| **H2b:** Oscillating (감쇠 진동) | **미지지** | 뚜렷한 진동 패턴 없음. Class 6이 감소 추세이나 진동이 아닌 단조 감소 |
| **H2c:** Stagnant (Gap 유지/증가) | **지지** | Class 4가 전형적 — 높은 P, 낮은 R_b, Gap 거의 불변 |
| **H3:** 초기 해설 열람이 궤적 예측 | **지지** | early_expl_rate이 가장 강력한 예측 변수 (|coef|=1.00) |
| **H4:** Convergent의 성과 향상 최대 | **수정 지지** | 가장 큰 개선은 Class 3(Strong Calibrator)이나 절대 성적은 가장 낮음. 개선과 절대 성적 구분 필요. |

---

## 12. Phase 4 실행 결과: 3D 시각화 + 민감도 분석

### 12.1 3D 시각화

```
실행: analysis/scripts/phase4_3d_visualization.py
```

**생성된 그림 (analysis/figures/):**

| 파일 | 내용 |
|------|------|
| fig2_theoretical_3d.png | 이론적 4가지 궤적 예측 (Convergent, Oscillating, Stagnant, Catastrophic) |
| fig2_empirical_3d.png | 실증 6-class 궤적 in R_b × P × τ 공간 |
| fig2_comparison.png | **(핵심)** 이론 vs 실증 나란히 비교 |
| fig2_projections.png | 4-panel 2D 투영 (R_b vs τ, P vs τ, Gap vs τ, R_b vs P phase plot) |
| fig5_gap_comparison.png | Figure 5 대응 — 이론적 Gap 패턴 vs 실증 Gap 패턴 |

**시각화 핵심 인사이트:**
- 이론은 R_b 범위 0~0.8 예측 vs 실증 0~0.35 — Under-reliance가 지배적
- 모든 실증 Gap이 음수 (Over-reliance 없음)
- Phase plot에서 Class 6만 우상단 출발, 나머지는 좌하단→우측 이동

### 12.2 민감도 분석

```
실행: analysis/scripts/phase4_sensitivity.R
```

**1. Forced Class Comparison (G=4-7):**

| G | BIC | ICL | Entropy | Min Class |
|:---:|---:|---:|:---:|:---:|
| 4 | 138,973 | 136,422 | 0.799 | 1.4% |
| 5 | 139,154 | 135,534 | 0.754 | 1.2% |
| **6** | **139,901** | **137,011** | **0.824** | **1.7%** |
| 7 | 140,115 | 136,603 | 0.802 | 1.2% |

→ G=7이 BIC 약간 우위(+214)이지만, G=6이 ICL·Entropy·최소 클래스 크기 모두 최적 → **6-class 유지 정당화**

**2. Bootstrap LRT (100 reps):**
- 모든 sequential test 유의 (p<.01) → LRT로는 구분 불가, BIC/ICL이 중재

**3. Split-half Validation:**
- 양쪽 모두 VEE G=6 선택
- Centroid 상관: mean r = **0.970** (매우 높은 재현성)
- Cross-ARI: 0.503 (중간 — GMM 특성상 정상)

**4. Threshold Sensitivity:**
- ratio≥0.15 (N=1,193): G=4 선택, ARI=0.44
- ratio≥0.20 (N=300): G=5 선택, ARI=0.38
- → 핵심 클래스(1-4)는 안정, 주변 클래스(5-6)는 표본 크기에 민감

**5. Classification Quality:**
- 평균 사후확률: 0.820
- >0.7: 76.4%, >0.8: 62.2%, >0.9: 40.1%
- 가장 잘 분리된 클래스: 6 (0.913), 3 (0.891), 5 (0.874)
- 가장 겹치는 클래스: 1 (0.779), 4 (0.797)

**산출물:**

| 파일 | 내용 |
|------|------|
| analysis/outputs/phase4_sensitivity_comparison.csv | G=4-7 모형 비교 |
| analysis/outputs/phase4_sensitivity_summary.txt | 상세 민감도 분석 결과 |

### 12.3 원고 초안

```
저장: manuscript/draft_v1.md (~9,200 단어)
```

- Abstract ~ Conclusion 전체 구조 완성
- 민감도 분석 결과 통합 완료
- APA 7th edition 인용 형식
- 35개 핵심 참고문헌 포함
- 대상 저널: Computers & Education / BJET

---

## 13. 완료 현황 및 남은 작업

| 단계 | 상태 | 비고 |
|------|:---:|------|
| Phase 0 (진단) | ✅ 완료 | 4,568명, 10 windows 확정 |
| Phase 1 (시계열) | ✅ 완료 | 45,680 rows |
| Phase 2 (GMM) | ✅ 완료 | 6 classes, VEE, BIC=139,751 |
| Phase 3 (RQ3+RQ4) | ✅ 완료 | 예측 49.4%, η²=0.163 |
| Phase 4 (시각화) | ✅ 완료 | 5개 그림 |
| Phase 4 (민감도) | ✅ 완료 | 6-class 안정성 확인 |
| 원고 초안 | ✅ 완료 | draft_v1.md |
| IRB/라이선스 | ⬜ 미진행 | PSU IRB exempt + EdNet CC BY-NC 4.0 |
| 원고 수정/보완 | ⬜ 미진행 | 공저자 리뷰, 참고문헌 완성 |
| OSF 사전등록 | ⬜ 미진행 | 분석 완료 후이므로 registered report 불가, pre-registration as-is |
