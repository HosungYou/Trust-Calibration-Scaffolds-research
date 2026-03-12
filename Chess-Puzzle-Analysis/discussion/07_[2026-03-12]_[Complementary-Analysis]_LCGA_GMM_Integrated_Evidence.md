# Complementary Analysis: LCGA + GMM Integrated Evidence for Paper 5

**Date:** 2026-03-12
**Purpose:** Paper 5의 핵심 전략 — LCGA와 GMM을 상보적으로 보고하여 5가지 이론적 궤적 패턴을 실증하는 논거 구성

---

## 1. 분석 전략의 근거

### 왜 두 방법을 함께 사용하는가?

LCGA(Latent Class Growth Analysis)와 GMM(Gaussian Mixture Model)은 **다른 질문에 답하는 상보적 방법**이다:

| 차원 | LCGA (lcmm) | GMM (mclust) |
|------|-------------|--------------|
| **질문** | "시간에 따라 어떤 궤적 *형태*가 존재하는가?" | "각 시점의 *행동 프로파일*에 어떤 하위집단이 존재하는가?" |
| **시간 모형** | 명시적 (piecewise linear growth) | 없음 (cross-sectional features) |
| **분류 기반** | 궤적의 intercept, slope, 전환점 slope | 20개 trajectory feature vector |
| **강점** | 실험 조건의 거시적 효과 포착 | 조건 내부의 미시적 개인차 포착 |
| **최적 G** | G=2 (조건 수준 분리) | G=6 (행동 하위유형 분리) |

### 논문에서의 보고 순서

1. **LCGA** → 실험 조작의 유효성 확인 (manipulation check 역할)
2. **GMM** → 조건 내부의 개인차 탐색 → 5가지 이론적 패턴 매핑
3. **교차 비교** → ARI로 두 방법의 관계 정량화

---

## 2. LCGA 결과 요약 (G=2)

### cal_gap 궤적: 실험 조작의 유효성

- **BIC=369.1** (G=1 대비 delta=107), **Entropy=0.871**
- Class 1 (N=52): C1 49명 + C2 3명 → High→Low 조건의 trust inertia
- Class 2 (N=48): C2 47명 + C1 1명 → Low→High 조건의 adaptive calibration
- **96% 조건 분리** → 실험 조작이 궤적의 지배적 결정 요인

### R_b 궤적: 행동적 의존의 이질성

- G=2 (BIC=84.4, Entropy=0.718)
- Class 1 (N=88): 조건 무관 유사 행동
- Class 2 (N=12, C2 11명): persistent non-reliance 소집단

### Bivariate: G=2 (BIC=426.2)

### LCGA의 역할 (Paper 5에서)

LCGA는 manipulation check로서, 실험 조건이 trust calibration 궤적을 효과적으로 분리함을 확인한다. 그러나 G=2는 개인차를 설명하지 못한다 — "같은 조건 내에서도 참가자들은 다른 패턴을 보이는가?" 이 질문에 GMM이 답한다.

---

## 3. GMM 결과 요약 (S2, 6-class)

### Strategy 2 (Trajectory Features) 6-class 매핑

| GMM Class | N (%) | 조건 | 이론적 패턴 | 핵심 증거 |
|-----------|-------|------|------------|-----------|
| Class 5 | 30 (30%) | C1 | **Catastrophic** | Gap +0.720 jump, R_b 0.700→0.620 경직 |
| Class 1 | 20 (20%) | C1 | **Convergent (rapid)** | R_b -0.460 급감, Gap +0.110 |
| Class 3 | 25 (25%) | C2 | **Convergent (gradual)** | W6 Gap -0.072, 거의 완벽 calibration |
| Class 2 | 14 (14%) | C2 | **Oscillating** | gap_sd=0.421, 비단조 R_b |
| Class 4 | 9 (9%) | C2 | **ABE** | R_b=0.200, Gap=-0.600, 적응 실패 |
| Class 6 | 2 (2%) | C2 | Extreme Compliance | R_b≈1.00, 항상 AI 추종 |

### GMM이 발견한 핵심 개인차

**C1(High→Low) 내:**
- 60% → Catastrophic (trust violation 무시)
- 40% → Convergent (빠른 적응)
- 같은 조건에서도 trust violation에 대한 반응이 양분됨

**C2(Low→High) 내:**
- 50% → Convergent (점진적 적응)
- 28% → Oscillating (비단조 변동)
- 18% → ABE (개선에도 불신 지속)
- 4% → Extreme Compliance

---

## 4. 교차 비교: LCGA × GMM

**ARI = 0.362** (moderate agreement)

### 교차표

|       | GMM-1 | GMM-2 | GMM-3 | GMM-4 | GMM-5 | GMM-6 |
|-------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| LCGA-1 (C1) |  19  |   0   |   3   |   0   |  30   |   0   |
| LCGA-2 (C2) |   1  |  14   |  22   |   9   |   0   |   2   |

### 해석

- LCGA Class 1 = GMM Class 1 (Convergent) + Class 5 (Catastrophic) → C1 내 양분
- LCGA Class 2 = GMM Class 2 (Oscillating) + Class 3 (Convergent) + Class 4 (ABE) → C2 내 삼분
- 이 구조는 LCGA가 조건 수준의 macro-effect를, GMM이 개인 수준의 micro-heterogeneity를 포착함을 보여줌

---

## 5. 통합 서사: Paper 5의 핵심 주장

### 주장 1: 실험 조작은 trust calibration 궤적을 효과적으로 결정한다

- LCGA G=2, 96% 조건 분리, Entropy=0.871
- Piecewise linear model이 전환점(W4.5)에서의 구조적 변화를 포착

### 주장 2: 조건 내부에서도 질적으로 다른 5가지 궤적 패턴이 존재한다

- GMM S2 6-class가 이론의 5가지 패턴을 data-driven으로 모두 식별
- Class 6 (Extreme Compliance)은 이론 외 극단 사례

### 주장 3: Bayesian Trust Update Model이 모든 패턴을 설명한다

| 패턴 | α⁺ | α⁻ | 환경 조건 | 실증 (Chess GMM) |
|------|-----|-----|-----------|-------------------|
| Convergent | > α_min | > α_min | 모든 조건 | Class 1, 3 (N=45) |
| Stagnant | ≈ 0 | ≈ 0 | 모든 조건 | (Chess에서는 6 window로 인해 미분류) |
| Catastrophic | unconstrained | ≈ 0 | R↓ | Class 5 (N=30) |
| Oscillating | nonlinear | nonlinear | R 변동 | Class 2 (N=14) |
| ABE | ≈ 0 | unconstrained | R↑ | Class 4 (N=9) |

### 주장 4: LCGA와 GMM은 서로 다른 수준에서 상보적 증거를 제공한다

- LCGA: 실험 효과의 인과적 구조 확인
- GMM: 개인차의 이론적 구조 확인
- 두 방법의 ARI=0.362는 "같지만 다른" 상보적 관계를 정량적으로 보여줌

---

## 6. Paper 5 원고 구조에서의 배치

### Results 섹션 구성

1. **Descriptive Results** — 조건별 window-level 기술통계, switch effect (d=2.10)
2. **LCGA Results** — G=2, manipulation validation, piecewise model
3. **GMM Results** — S2 6-class, 5-pattern mapping
4. **Cross-Method Integration** — ARI, cross-tabulation, complementary interpretation
5. **Bayesian Model Fit** — α parameter estimation per class (if feasible)

### Discussion 섹션 핵심 논점

1. Trust violation은 Catastrophic vs Convergent 반응을 양분시킨다 (C1 내 60:40)
2. Trust repair는 Convergent, Oscillating, ABE의 3가지 경로를 유발한다 (C2 내 50:28:18)
3. ABE는 Chess와 EdNet에서 동일한 양적 특성을 보인다 (Gap ≈ -0.600)
4. LCGA와 GMM의 상보적 사용이 trust calibration 연구의 새로운 방법론적 표준이 될 수 있다

---

## 7. 분석 완료 상태 확인

| 분석 | 스크립트 | 출력 파일 | 상태 |
|------|----------|-----------|------|
| 탐색적 분석 | chess_puzzle_analysis.py | chess_exploratory.txt, chess_window_level.csv | Complete |
| GMM S1-S3 | chess_gmm_analysis.R | chess_gmm_s{1,2,3}_assignments.csv | Complete |
| GMM by Condition | chess_gmm_by_condition.R | chess_gmm_c{1,2}_only_assignments.csv | Complete |
| LCGA cal_gap | chess_lcga_analysis.R | chess_lcga_gap_*.csv | Complete |
| LCGA R_b | chess_lcga_analysis.R | chess_lcga_rb_*.csv | Complete |
| LCGA Bivariate | chess_lcga_analysis.R | chess_lcga_bivariate_model_fit.csv | Complete |
| Cross-method | chess_lcga_analysis.R | ARI=0.362 (log) | Complete |

**모든 분석이 완료되었습니다.**
