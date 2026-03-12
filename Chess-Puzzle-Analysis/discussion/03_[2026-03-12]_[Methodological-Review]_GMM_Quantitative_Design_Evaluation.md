# GMM 기반 궤적 분류 연구의 양적 설계 평가

**Date:** 2026-03-12
**Evaluator:** Quantitative Design Consultant (C1)
**Scope:** EdNet (N=4,568, 10 windows) + Chess Puzzle (N=100, 6 windows) GMM 분석
**Decision Status:** 평가 완료, 7개 영역별 구체적 개선 방안 제시

---

## 총괄 평가

이 연구는 이론적 프레임워크와 데이터 주도 분석의 정합성이라는 면에서 상당한 강점을 보유하고 있다. 그러나 방법론적 관점에서 **소표본 GMM의 신뢰도**, **시계열 길이의 적절성**, **분석적 선택에 대한 민감도 보고 부족**이라는 세 가지 핵심 우려가 존재한다. 아래에서 각 영역별로 문제를 진단하고 실행 가능한 해결책을 제안한다.

---

## 1. GMM 적절성 평가: 이 연구 질문에 맞는 방법인가?

### 1.1 현재 접근법의 정당성

mclust를 통한 Gaussian Mixture Model(GMM)은 이 연구의 핵심 질문인 "trust calibration 궤적의 잠재 유형이 존재하는가?"에 대해 **합리적이나 최적은 아닌** 선택이다.

**GMM의 강점 (이 연구 맥락에서):**
- 모형 기반(model-based) 클러스터링으로 통계적 불확실성 정량화 가능 (사후확률)
- BIC를 통한 모형 선택의 객관적 근거 제공
- mclust의 14가지 공분산 구조로 유연한 클러스터 형태 허용
- 연속형 다변량 데이터에 자연스러운 적합

**GMM의 한계 (이 연구 맥락에서):**
- **시간 구조 무시**: GMM은 wide-format 입력을 독립적 차원으로 취급하므로, W1-W2-W3-...-W10이라는 **순서적 의존성**을 모형 내에서 포착하지 못한다. 이는 "궤적" 분류에서 근본적 약점이다.
- **정규성 가정**: 비율 데이터(R_b, P, cal_gap)는 0-1 범위에 제한되어 정규분포 가정을 위반할 수 있다.
- **고차원 문제**: 20-30개 피처를 100개 관측치(Chess)에 적합하면 p/n 비율이 0.20-0.30으로, 고차원 과적합 위험이 상당하다.

### 1.2 대안 방법 비교

| 방법 | 시간 구조 반영 | 소표본 적합성 | 비정규 허용 | 모형 선택 | 이 연구 적합도 | 구현 난이도 |
|------|:-:|:-:|:-:|:-:|:-:|:-:|
| **GMM (mclust)** | 없음 | 중 (N>200 권장) | 제한적 | BIC | B+ | 낮음 |
| **LCGA/GBTM** | **있음** (다항식) | 중-높음 | 제한적 | BIC, BLRT | **A** | 중 |
| **Latent Class Growth Analysis** | **있음** | 중 | 제한적 | BIC, entropy | **A** | 중 |
| **K-means** | 없음 | 높음 | 자유 | 실루엣, Gap | B | 매우 낮음 |
| **계층적 클러스터링** | 없음 | 높음 | 자유 | 덴드로그램 | B- | 낮음 |
| **HMM** | **있음** (상태전이) | 낮음 | 유연 | BIC, AIC | B+ | 높음 |
| **Functional Data Analysis** | **있음** (함수 근사) | 중 | 유연 | CV | A- | 높음 |

### 1.3 핵심 권고: LCGA/GBTM 추가 실행

**Latent Class Growth Analysis (LCGA)** 또는 **Group-Based Trajectory Modeling (GBTM)**은 이 연구 질문에 이론적으로 가장 적합한 방법이다. 이유:

1. **시간 구조를 명시적으로 모형화**: 각 잠재 클래스 내에서 시간에 따른 다항식(또는 비선형) 궤적을 추정한다. GMM처럼 W1, W2, ...를 독립 차원으로 취급하는 것이 아니라, "시간이 흐르면서 이 변수가 어떤 곡선을 따르는가?"를 직접 모형화한다.

2. **리뷰어 기대 부합**: 궤적 분류 논문에서 리뷰어가 가장 먼저 기대하는 방법이 LCGA/GBTM이다. GMM만 사용하면 "왜 trajectory modeling을 하지 않았는가?"라는 질문이 거의 확실하게 나온다.

3. **Chess 데이터의 전환점(switch point) 모형화**: LCGA에서 piecewise linear 또는 spline 모형을 사용하면, Trial 20에서의 전환 효과를 궤적 함수 내에 직접 포함할 수 있다.

**구현 방법 (R):**
- `lcmm` 패키지: `hlme()` 또는 `lcmm()` 함수
- `flexmix` 패키지: 혼합 회귀 프레임워크
- `crimCV` 패키지: GBTM 특화
- Mplus: 가장 유연하나 상용 소프트웨어

**실행 제안:**
```
# lcmm 패키지를 이용한 LCGA 예시 구조
cal_gap ~ window + I(window^2) + (1 | subject), mixture = ~window + I(window^2), ng = 2:6
```

**Chess 데이터의 경우:**
```
# piecewise model: 전환점 = window 4.5
cal_gap ~ window_pre + window_post + (1 | session), ng = 2:5
# window_pre = min(window, 4), window_post = max(window - 4, 0)
```

### 1.4 GMM을 유지하되 보완하는 전략

LCGA 추가가 어렵다면, 최소한 다음을 수행해야 한다:

1. **GMM이 LCGA와 다른 방법임을 논문에서 명시적으로 인정**하고, GMM 선택의 근거를 제시
2. **Strategy 2 (trajectory features)**가 시간 구조의 요약 통계량(slope, reversals, switch_jump)을 포함하므로, 간접적으로 시간 의존성을 반영함을 주장
3. **K-means를 보완적 방법으로 실행**하여 GMM 결과의 삼각 검증(triangulation) 제공

---

## 2. 표본 크기 적절성

### 2.1 Chess Puzzle (N=100, 조건별 N=50)

이것은 이 연구의 **가장 심각한 방법론적 약점**이다.

**관련 문헌:**

- **Nylund et al. (2007)**: GMM/LCA에서 N<200일 때 BIC의 모형 선택 정확도가 급격히 저하됨. N=100에서 BIC가 올바른 클래스 수를 선택할 확률은 약 50-70% (참 클래스 수와 분리도에 따라 달라짐).
- **Tein et al. (2013)**: 잠재 클래스 모형에서 필요한 최소 표본 크기는 클래스 간 분리도, 클래스 수, 측정 변수 수에 따라 달라지며, 잘 분리된 3-class 모형에서도 N=200 이상을 권고.
- **Henson et al. (2007)**: 혼합 모형에서 소표본은 (a) 클래스 수 과대추정, (b) 수렴 실패, (c) boundary estimates (분산 = 0)의 위험을 높인다.
- **Lubke & Neale (2006)**: 클래스 간 Mahalanobis distance가 클수록 필요 표본이 줄어들지만, N=50에서 6-class 모형은 과도하게 복잡하다.

**Chess 데이터의 구체적 문제:**

| 우려 | 심각도 | 구체적 수치 |
|------|:-:|------|
| N=100에서 6-class GMM | **심각** | 클래스당 평균 N=16.7, 실제로는 N=2~30 |
| Class 6 (N=2) | **매우 심각** | 2개 관측치로 가우시안 추정 불가; mclust가 이를 추정했다면 공분산이 축퇴(degenerate)했을 가능성 |
| Class 4 (N=9) | **심각** | 20개 피처에 9개 관측치: p > n 문제 |
| 조건별 분리 GMM (N=50) | **매우 심각** | N=50에서 2-6개 클래스는 해석 가능한 최소 한계에 도달 |
| p/n 비율 (S2: 20 features) | **심각** | 20/100 = 0.20; 조건별이면 20/50 = 0.40 |

**완화 요인:**

1. **높은 사후확률(0.984-0.990)**: 이는 클래스 분리도가 매우 높다는 것을 의미. 그러나 소표본에서 높은 사후확률은 **과잉확신(overconfidence)**의 징후일 수도 있다 -- 특히 EII 모형(등방 공분산)이 선택된 경우, 모형이 지나치게 단순화되어 인위적으로 높은 분리도를 생성할 수 있다.

2. **C1/C2 완전 분리**: 이는 실험 조작 효과가 주 분산원이라는 것이며, GMM이 실질적으로 "조건"을 먼저 분리한 후 조건 내 개인차를 식별한 것이다. 이 자체는 방법론적 문제라기보다 설계적 특성이다.

3. **EdNet의 대규모 표본(N=4,568)으로 보완**: Chess의 소표본 결과를 EdNet의 대표본 결과가 지지한다면, 전체 논증이 강화된다.

### 2.2 EdNet (N=4,568)

EdNet의 표본 크기는 GMM에 **충분하다**. N=4,568은 6-8 class 모형에서도 클래스당 평균 570-760명을 확보할 수 있다. 다만 다음 사항을 주의해야 한다:

- **S2 재조작화의 완전 사례(complete cases)**: P_adaptive 결측으로 인해 실제 분석 대상이 N=4,568보다 줄어들 수 있음. 최종 분석 N을 명확히 보고해야 한다.
- **대표본에서의 BIC 과민성**: N>2,000에서 BIC는 미세한 차이에도 클래스 수를 증가시키는 경향이 있다. 이는 ICL이나 해석 가능성(interpretability)을 보완 기준으로 사용해야 하는 이유이다.

### 2.3 표본 크기에 대한 권고

**Chess 데이터:**
1. **논문에서 소표본 한계를 제1 제한점으로 명시**: "N=100 (50 per condition) is below the commonly recommended minimum of 200 for GMM. Results should be interpreted as suggestive rather than definitive."
2. **클래스 수 축소 검토**: G=6 대신 G=3-4로 줄여서 클래스당 N을 확보하는 대안 제시. 특히 Class 6(N=2)는 별도 논의가 아닌 이상 모형에서 제외하는 것이 안전하다.
3. **조건별 별도 GMM에서 G=2-3으로 제한**: N=50에서는 2-3개 클래스가 해석 가능한 최대치이다. G=4 이상은 과적합 위험이 높다.
4. **정규화(regularization)**: mclust의 제한적 공분산 모형(EII, EEI)을 의도적으로 사용하여 추정해야 할 모수 수를 줄이는 것이 소표본에서 합리적이다. 이미 EII가 선택된 것은 긍정적이지만, **이것이 데이터의 진정한 구조인지 아니면 소표본 때문에 복잡한 모형이 수렴하지 못한 것인지** 구분해야 한다.

---

## 3. 시계열 길이의 적절성

### 3.1 6개 윈도우 (Chess)는 충분한가?

**결론: 주요 패턴 식별에는 충분하나, 궤적의 세밀한 형태 구분에는 불충분하다.**

**문헌 근거:**

- **Nagin (2005, GBTM 원저)**: GBTM에서 최소 3개 시점을 권고하지만, 비선형 궤적(quadratic 이상)에는 최소 4-5개 시점이 필요하다. 6개 시점은 quadratic 모형까지 가능하나, cubic 이상은 과적합 위험이 있다.
- **Jung & Wickrama (2008)**: LCGA에서 4-5개 시점이 최소이며, 7-10개 시점이 이상적이라고 제안.
- **Curran et al. (2010)**: 성장 혼합 모형에서 시점 수가 적을수록 잠재 클래스 열거(class enumeration)의 정확도가 저하됨.

**Chess 데이터의 구체적 상황:**

6개 윈도우 중 4개가 pre-switch, 2개가 post-switch이다. 이는 다음을 의미한다:

1. **Pre-switch 궤적 (W1-W4)**: 4개 시점으로 선형 추세만 안정적으로 추정 가능. 학습 곡선의 비선형성(감속, 가속)을 포착하기 어렵다.
2. **Post-switch 적응 (W5-W6)**: 2개 시점은 "방향"만 알 수 있고, **적응의 속도나 형태**를 구분할 수 없다. 예를 들어, "빠른 적응 후 안정화"와 "점진적 적응 중"을 2개 시점으로 구분하는 것은 불가능하다.
3. **전환 효과의 크기(Cohen's d > 2.0)**: 이 극적인 효과 크기 덕분에, 6개 시점으로도 "전환이 일어났다"는 것은 명확히 감지된다. 문제는 전환 **이후**의 동적 과정이 시간적으로 undersampled되었다는 것이다.

### 3.2 10개 윈도우 (EdNet)는 충분한가?

10개 시점은 LCGA/GBTM에서 **양호한** 수준이다. Quadratic 및 cubic 궤적까지 추정 가능하며, 비단조적(oscillating) 패턴의 식별에도 적절하다. 다만:

- **윈도우 크기의 선택**: 각 윈도우 내 에피소드 수에 따라 윈도우 수준 통계량의 신뢰도가 달라진다. 윈도우가 너무 작으면 측정 잡음이 크고, 너무 크면 시간적 해상도가 낮아진다.
- **P_adaptive 결측**: 23.8%의 윈도우에서 adaptive 문제가 없어 P_adaptive가 결측된다. 이는 시계열에 불규칙적 결측(irregular missingness)을 유발하여, wide-format GMM에서 결측 처리(mean imputation)가 편향을 초래할 수 있다.

### 3.3 시계열 길이에 대한 권고

1. **Chess**: "6 time windows (4 pre-switch, 2 post-switch) limit the temporal resolution of post-switch adaptation dynamics"라고 명시하되, 전환 효과의 크기가 충분히 크므로 주요 패턴 식별은 가능했음을 주장.
2. **윈도우 크기 민감도 분석 (EdNet)**: 5시행/윈도우(=6윈도우) vs 3시행/윈도우(=10윈도우) vs 2시행/윈도우(=15윈도우)로 변경 시 GMM 결과가 얼마나 변하는지 확인. 이는 Section 5의 민감도 분석과 연결된다.
3. **Chess에서 3시행/윈도우(=10윈도우) 대안 분석**: 현재 5시행/윈도우 대신 3시행/윈도우로 재구성하면 10개 시점을 확보할 수 있다. 다만 윈도우당 시행 수가 줄어 측정 잡음이 증가하므로, trade-off를 보고해야 한다.

---

## 4. 모형 선택 기준의 적절성

### 4.1 BIC 사용의 평가

mclust는 기본적으로 BIC(Bayesian Information Criterion)를 모형 선택에 사용한다. 이는 널리 받아들여지는 기준이나, 몇 가지 주의가 필요하다.

**BIC의 강점:**
- 모형 복잡도에 대한 페널티가 일관됨 (log(N) * k)
- 대규모 비교(모형 유형 x 클래스 수)에서 효율적
- 점근적으로 참 모형 선택에 일관적(consistent)

**BIC의 한계 (이 연구 맥락에서):**

1. **소표본 성능**: BIC의 점근적 정당화는 대표본에 기반한다. N=100(Chess)에서 BIC의 모형 선택 성능은 상당히 저하된다. Nylund et al. (2007)의 시뮬레이션에 따르면, N=200 미만에서 BIC는 클래스 수를 과대추정하는 경향이 있다.

2. **BIC vs ICL**: Integrated Completed Likelihood (ICL)은 BIC에서 entropy 페널티를 추가한 것으로, **분류 목적**에 더 적합하다. ICL = BIC - 2 * entropy. 분류의 명확성을 중시할 때 ICL이 더 보수적이고 실용적인 선택이다. Phase 4에서 ICL을 이미 계산하고 있는 것은 **매우 긍정적**이나, ICL 결과가 BIC와 다른 클래스 수를 지지하는 경우 이를 논문에서 보고해야 한다.

3. **Bootstrap LRT (BLRT)**: Phase 4에서 이미 구현했다. BLRT는 "G개 클래스가 G-1개보다 유의하게 좋은가?"를 직접 검정하므로, BIC보다 명확한 증거를 제공한다. Nylund et al. (2007)은 BLRT가 BIC보다 정확한 클래스 수 선택을 보여준다고 보고했다. 특히 소표본에서 BLRT의 유형 I 오류율이 BIC보다 잘 통제된다.

### 4.2 소표본 보정

- **AIC_c (corrected AIC)**: Hurvich & Tsai (1989)의 소표본 보정 AIC. 단, AIC 자체가 일관적이지 않으므로 클래스 수 선택보다는 예측 정확도 목적에 적합.
- **BIC with small-sample correction**: Draper (1995)의 수정 BIC 또는 sample-size adjusted BIC (SABIC). SABIC = -2*loglik + k*ln((N+2)/24). Tein et al. (2013)은 SABIC가 소표본에서 BIC보다 나은 성능을 보인다고 보고.

### 4.3 교차 검증

K-fold cross-validation은 GMM의 모형 선택에 적용 가능하나, 소표본(N=100)에서 fold별 표본이 너무 작아져 불안정해진다. Leave-one-out은 계산 비용이 높지만 소표본에서 편향이 적다.

### 4.4 모형 선택에 대한 권고

**1순위: 다중 기준 보고 (필수)**

| 기준 | 용도 | 이미 구현? |
|------|------|:-:|
| BIC | 기본 모형 선택 | 예 |
| ICL | 분류 명확성 | 예 (Phase 4) |
| SABIC | 소표본 보정 | **아니오** |
| BLRT | 순차적 클래스 비교 | 예 (Phase 4) |
| Entropy (normalized) | 분류 품질 | 예 (Phase 4) |
| 평균 사후확률 | 분류 확실도 | 예 |

논문에서 최소 BIC, ICL, BLRT, entropy를 함께 보고하고, 이들이 일치하는지 확인해야 한다. 불일치 시 해석적 판단의 근거를 제시해야 한다.

**2순위: SABIC 추가 (권장)**

mclust에서 직접 제공하지 않으므로 수동 계산 필요:
```r
# SABIC 계산
k <- nPars(mc_fit)  # 추정 모수 수
N <- nrow(X)
sabic <- -2 * mc_fit$loglik + k * log((N + 2) / 24)
```

---

## 5. 분석적 선택에 대한 민감도

### 5.1 윈도우 크기 (Window Size)

현재: Chess 5시행/윈도우, EdNet ~15에피소드/윈도우 (추정).

**민감도 우려:**
- 윈도우 크기를 변경하면 시점 수, 윈도우 내 평균의 신뢰도, 그리고 궤적의 형태가 모두 변한다.
- 특히 Chess에서 전환점(Trial 20)이 윈도우 경계에 정확히 위치하도록 윈도우를 설계한 것은 의도적이지만, 다른 윈도우 경계(예: 4시행/윈도우 = 7.5윈도우, 전환점이 윈도우 중간에 위치)에서는 전환 효과가 희석될 수 있다.

**권고:** EdNet에서 최소 2개의 대안 윈도우 크기(예: ~10에피소드/윈도우, ~20에피소드/윈도우)로 GMM을 재실행하여 클래스 수와 클래스 비율의 안정성을 확인해야 한다. 이미 Phase 4에서 임계값 민감도를 수행한 것은 좋으나, 윈도우 크기 민감도가 누락되어 있다.

### 5.2 피처 스케일링 (Feature Scaling)

Strategy 2에서 `scale()` 함수로 z-score 정규화를 적용했다. 이는 합리적이나:

- 스케일링 전후의 GMM 결과가 상당히 달라질 수 있다 (특히 피처 간 분산 차이가 클 때).
- Strategy 1과 Strategy 3에서는 스케일링을 적용하지 않았다 (wide-format raw values 사용).
- **전략 간 비교의 공정성**: S1/S3(비스케일링)과 S2(스케일링)는 입력 공간 자체가 다르므로, ARI로 비교할 때 스케일링 효과와 피처 선택 효과가 혼재된다.

**권고:** S1에도 스케일링을 적용한 버전과 S2에 비스케일링을 적용한 버전을 추가 실행하여, 스케일링의 독립적 효과를 보고해야 한다.

### 5.3 공분산 구조 (Covariance Structure)

mclust는 14가지 공분산 모형을 비교하여 BIC 기준으로 최적을 선택한다.

**현재 결과:**
- Chess S1: EII (등방, 등분산) -- 가장 단순한 모형
- Chess S2: VEI (가변 부피, 등방향, 등분산)
- EdNet 원본: VEE (가변 부피, 등방향, 등분산)
- EdNet 재조작화 S2: VVV (완전 비제한) -- 가장 복잡한 모형

**우려:**
- Chess에서 EII가 선택된 것은 소표본 때문에 복잡한 모형의 모수 추정이 불가능했기 때문일 수 있다. EII는 모든 클래스가 동일한 구형(spherical) 공분산을 가정하는데, 이는 trust calibration 궤적에서 비현실적이다 (예: Catastrophic 클래스는 전환 후 분산이 크고, Convergent 클래스는 작을 수 있음).
- EdNet에서 VVV가 선택된 것은 대표본 덕분에 복잡한 모형이 추정 가능했기 때문이다. 그러나 VVV는 p(p+1)/2 * G개의 공분산 모수를 추정해야 하므로, 20개 피처 x 8클래스에서 20*21/2*8 = 1,680개의 공분산 모수가 필요하다. 이는 과적합 위험을 시사한다.

**권고:**
1. **Chess**: EII 외에 EEI, VII를 강제 적용한 결과도 보고하여, 공분산 구조 변경이 클래스 수에 미치는 영향을 확인
2. **EdNet**: VVV 외에 VEE, VEV, EEV를 비교하여 BIC 차이가 의미 있는지(ΔBIC > 10) 확인
3. **논문에서 선택된 모형의 공분산 구조와 그 의미를 기술**: "EII was selected for the Chess data, implying that clusters are approximately spherical with equal volume. This parsimonious structure may reflect the small sample size rather than the true data-generating process."

### 5.4 클래스 수 탐색 범위 (G Range)

- Chess: G=2:8
- EdNet 원본: G=1:7
- EdNet 재조작화: G=1:8

**우려:** G의 상한을 어디까지 탐색했는가에 따라 BIC가 다른 최적점을 찾을 수 있다. 특히 EdNet에서 G=7까지만 탐색했는데, G=8이나 G=9에서 BIC가 더 높을 수 있다.

**권고:** EdNet에서 G=1:10까지 탐색 범위를 확대하고, BIC 곡선이 G=6 부근에서 명확한 "elbow"를 보이는지 확인해야 한다.

### 5.5 피처 선택의 영향

세 가지 전략(S1: wide-format, S2: trajectory features, S3: wide-format extended)이 서로 상당히 다른 분류를 생성한다 (ARI 0.095-0.243). 이는 **피처 선택이 분류 결과를 지배한다**는 것을 의미하며, 어떤 피처를 입력하느냐에 따라 다른 "궤적 유형"을 발견하게 된다.

**이것은 심각한 문제인가?** 부분적으로 그렇다. 서로 다른 피처 공간에서 다른 클러스터가 발견되는 것은 자연스러우나, 이론에 기반한 핵심 패턴(Convergent, Catastrophic 등)이 **모든 전략에서 안정적으로 출현**하는지 확인해야 한다. 현재 보고에서는 S2 결과만 상세히 해석하고, S1/S3와의 정합성은 ARI로만 보고한다.

**권고:**
1. 각 전략에서 이론 패턴으로 해석 가능한 클래스를 식별하고, **전략 간 concordance table** (어떤 전략의 어떤 클래스가 다른 전략의 어떤 클래스에 대응하는가?)을 작성
2. **앙상블 접근**: 3개 전략의 클래스 할당이 일치하는 "핵심 멤버(core members)"를 식별하여 패턴의 안정성을 보여줌

---

## 6. 권고 견고성 분석 (우선순위 순서)

### Tier 1: 필수 (논문 수정 없이 제출 불가)

#### 6.1 조건별 별도 GMM + 부트스트랩 안정성 [이미 계획됨]

**검증 대상:** "C1/C2 완전 분리는 단순히 조건 효과가 아닌, 조건 내 개인차를 반영하는가?"
**방법:** C1(N=50)과 C2(N=50)에서 각각 G=2:4 범위로 GMM 실행. 부트스트랩 200회로 G 선택 안정성 확인. 이미 `chess_gmm_by_condition.R`에 구현되어 있으므로 결과만 보고하면 된다.
**중요:** N=50에서 G=4 이상은 보고하지 않는 것이 안전하다.

#### 6.2 다중 모형 선택 기준 보고

**검증 대상:** "BIC가 선택한 클래스 수가 다른 기준과 일치하는가?"
**방법:** BIC, ICL, SABIC, BLRT, normalized entropy를 모두 계산하고 표로 보고. 기준 간 불일치가 있을 경우 해석적 판단의 근거 제시. Phase 4 스크립트에서 BIC, ICL, BLRT, entropy는 이미 계산. SABIC만 추가.
**중요:** 기준 간 일치도가 높으면 결과의 신뢰성이 크게 강화된다.

#### 6.3 분류 품질 종합 보고

**검증 대상:** "GMM 분류가 얼마나 명확한가?"
**방법:** (a) 평균 사후확률 (per class), (b) 사후확률 > 0.70 비율, (c) normalized entropy, (d) odds of correct classification (OCC), (e) classification table (할당 vs 2순위 클래스). Phase 4와 Phase 2에서 대부분 계산됨.
**중요:** CHI/CSCW 수준 논문에서 이 정보는 필수적이다. 특히 N이 작은 Chess에서 높은 분류 품질을 보여야 소표본 우려를 완화할 수 있다.

### Tier 2: 강력 권고 (제출 가능하나 리뷰어 요구 예상)

#### 6.4 LCGA/GBTM 비교 분석

**검증 대상:** "시간 구조를 명시적으로 모형화하면 동일한 패턴이 발견되는가?"
**방법:** R의 `lcmm` 패키지로 EdNet과 Chess에서 LCGA 실행. Chess에서는 piecewise linear 모형(전환점 = W4.5) 사용.
**중요:** 리뷰어가 "왜 LCGA를 하지 않았는가?"를 질문할 확률이 매우 높다. 선제적으로 GMM과 LCGA 결과를 비교하면 방법론적 엄밀성이 크게 향상된다.

#### 6.5 Mixed-Effects Model을 통한 통계적 추론

**검증 대상:** "궤적 패턴의 차이가 통계적으로 유의한가?"
**방법:** `cal_gap ~ window * condition + (window | participant)` 형태의 혼합효과모형으로 (a) 전환 효과의 유의성, (b) 개인차 분산의 크기, (c) GMM 클래스를 예측변수로 추가한 모형 비교. 이미 Discussion 02에서 계획되어 있다.
**중요:** GMM은 분류 도구이지 추론 도구가 아니다. "이 패턴들이 정말 다른가?"에 대한 통계적 검정은 별도로 필요하다.

#### 6.6 K-Means / 계층적 클러스터링 삼각 검증

**검증 대상:** "GMM 결과가 방법에 의존하지 않는가?"
**방법:** 동일 피처에 K-means(k=3:8, 실루엣 기준)와 Ward 계층적 클러스터링 적용. GMM 분류와의 ARI 비교.
**중요:** GMM이 유일한 방법이 아니라, 다른 방법도 유사한 구조를 감지한다는 것을 보여주면 결과의 견고성이 강화된다.

### Tier 3: 선택적 (차별화 요소)

#### 6.7 피처 중요도 분석

**검증 대상:** "어떤 변수가 클래스 분리에 가장 기여하는가?"
**방법:** (a) permutation importance (각 피처를 무작위 치환했을 때 분류 정확도 하락), (b) 변수별 ANOVA (F-통계량), (c) 주성분 공간에서의 클래스 시각화.
**의의:** 이론적 주장("cal_gap이 핵심 구분자")에 대한 데이터 기반 근거 제공.

#### 6.8 교차 데이터셋 예측 검증

**검증 대상:** "EdNet에서 학습한 GMM이 Chess에서도 유사한 분류를 생성하는가?"
**방법:** EdNet S2 모형의 클래스 중심(centroids)과 Chess 데이터의 유사한 피처를 비교. 직접 예측은 피처 공간이 다르므로 어렵지만, conceptual correspondence를 정량화할 수 있다.
**의의:** 두 데이터셋 간 "개념적 재현"의 정량적 증거.

#### 6.9 시뮬레이션 검증

**검증 대상:** "이론적 5패턴에서 생성된 시뮬레이션 데이터에 GMM을 적용하면 5개 클래스를 복원하는가?"
**방법:** 각 이론 패턴에 대응하는 파라메트릭 모형(Bayesian trust update 등)으로 데이터 생성 후 GMM 적용. Discussion 02에서 이미 제안됨.
**의의:** GMM의 회복력(recovery)을 참 구조가 알려진 상태에서 검증. 특히 N=100에서 6개 참 클래스를 GMM이 정확히 복원하는지 확인하면, Chess 결과의 신뢰도에 대한 직접적 증거가 된다.

---

## 7. 보완적/대안적 방법

### 7.1 혼합효과모형 (Mixed-Effects Models)

**목적:** GMM의 분류적 접근을 보완하는 연속적 접근

**구체적 모형:**

```r
# 기본 모형: 전환 효과
library(lme4)
chess$post_switch <- ifelse(chess$window > 4, 1, 0)
chess$window_centered <- chess$window - 3.5

m1 <- lmer(cal_gap ~ window_centered * condition * post_switch +
           (window_centered + post_switch | participant),
           data = chess)

# 3-way interaction이 핵심:
# condition x post_switch = 조건별 전환 효과 차이
# window_centered x post_switch = 전환 후 적응 속도
```

**이 연구에서의 가치:**
- 전환 효과의 통계적 유의성 검정
- 개인별 random slopes의 분산이 GMM 클래스 간 차이를 설명하는지 확인
- GMM 클래스 멤버십을 covriate로 추가하여 분류의 유용성 검증

### 7.2 변화점 탐지 (Change Point Detection)

**목적:** 전환 시점을 사전 지정하지 않고 데이터에서 발견

**구체적 접근:**

```r
# 개인별 변화점 탐지
library(changepoint)
for (participant in unique(chess$participant_id)) {
  ts <- chess$cal_gap[chess$participant_id == participant]
  cp <- cpt.mean(ts, method = "PELT")
  # cp@cpts에 변화점 위치 저장
}
```

**이 연구에서의 가치:**
- Trial 20의 전환이 모든 참가자에게 동일한 시점에서 감지되는지, 아니면 일부 참가자는 더 일찍/늦게 반응하는지 확인
- 전환 시점의 개인차가 GMM 클래스와 상관하는지 확인 (예: Adaptive Reducer는 W5에서 즉시 변화, Persistent Over-Reliance는 변화점 미감지)
- **독립적 증거**: GMM과 무관한 방법으로 궤적의 이질성을 확인

### 7.3 함수적 데이터 분석 (Functional Data Analysis, FDA)

**목적:** 이산 시점의 데이터를 연속 함수로 근사한 후 함수 공간에서 클러스터링

**구체적 접근:**

```r
library(fda)
library(funFEM)  # 함수적 혼합 모형

# B-spline 기저 함수로 각 개인의 궤적을 함수로 변환
basis <- create.bspline.basis(rangeval = c(1, 6), nbasis = 5)
fd_obj <- smooth.basis(1:6, t(cal_gap_matrix), basis)

# 함수적 클러스터링
fem <- funFEM(fd_obj$fd, K = 2:6)
```

**이 연구에서의 가치:**
- 6개 시점이 적어서 직접 비교가 어려운 Chess 데이터에서, 함수 근사를 통해 연속적 궤적을 복원한 후 비교 가능
- 그러나 6개 시점에서 B-spline 근사의 신뢰도도 제한적이므로, 보완적 방법 정도로 활용

### 7.4 Hidden Markov Model (HMM)

**목적:** 관찰 불가능한 "상태"(state)와 상태 간 전이를 모형화

**이 연구에서의 가치:**
- "trust violation 인지"와 같은 잠재 상태를 직접 모형화 가능
- 전이 확률이 개인차를 반영 (예: "high trust" → "low trust" 전이 확률이 높은 참가자 vs 낮은 참가자)
- 그러나 6개 시점은 HMM 추정에 불충분하며, N=50에서 개인별 HMM은 비현실적

**권고:** EdNet(10 시점)에서만 탐색적으로 적용 가능. Chess에는 권장하지 않음.

### 7.5 방법 조합 전략 요약

| 방법 | EdNet 적용 | Chess 적용 | 목적 |
|------|:-:|:-:|------|
| GMM (mclust) | 이미 완료 | 이미 완료 | 기본 분류 |
| LCGA/GBTM | **강력 권고** | **강력 권고** | 시간 구조 반영 분류 |
| Mixed-Effects | **강력 권고** | **강력 권고** | 통계적 추론 |
| K-Means | 권고 | 권고 | 삼각 검증 |
| Change Point | 선택적 | **권고** | 전환 시점 이질성 |
| FDA | 선택적 | 선택적 | 함수적 비교 |
| HMM | 선택적 | 비권고 | 상태 전이 모형 |

---

## 8. 타당도 위협 분석

### 8.1 내적 타당도

| 위협 | 심각도 | 설명 | 대응 |
|------|:-:|------|------|
| **사후적 패턴 매칭** | 중간 | GMM이 이론의 5패턴을 "발견"했다고 하지만, 패턴 라벨은 연구자가 사후적으로 부여함 | Pre-registration 부재 인정; 확인적 분석(조건별 별도 GMM)으로 보완; 시뮬레이션 검증 |
| **분석적 유연성** | 중간-높음 | 3개 전략 중 "가장 유망한" 것을 선택하는 과정에서 탐색적 자유도가 높음 | 모든 전략의 결과를 부록에 보고; 사전 지정 기준(BIC) 준수 |
| **윈도우 경계 효과** | 중간 | Chess에서 전환점이 윈도우 경계에 정확히 위치하도록 설계됨. 이것이 결과를 과대추정할 수 있음 | 대안 윈도우 크기 분석 |

### 8.2 외적 타당도

| 위협 | 심각도 | 설명 | 대응 |
|------|:-:|------|------|
| **도메인 특수성** | 중간 | 체스와 수학 학습은 특수한 과제 | 두 도메인에서 동일 패턴 발견으로 부분 대응; 추가 데이터셋(ImageNet-16H) 적용 권고 |
| **참가자 특성** | 중간 | Chess 50명은 MTurk/대학생 표본일 가능성 (원논문 확인 필요) | 표본 특성 기술 필수 |
| **AI 유형** | 중간 | 규칙 기반 AI 추천 vs 실제 ML 모형 | 한계로 기술 |

### 8.3 구성 타당도

| 위협 | 심각도 | 설명 | 대응 |
|------|:-:|------|------|
| **R_b 조작화 차이** | 중간 | EdNet(feature adoption) vs Chess(move acceptance)는 다른 구인 | "Conceptual replication" 프레이밍; 차이를 명시적으로 기술 |
| **P_adaptive 결측** | 높음 (EdNet) | 23.8% 결측 + mean imputation은 편향 유발 가능 | 다중 대체(multiple imputation) 또는 결측 패턴 분석 |
| **cal_gap의 해석** | 낮음 | R_b - AI_accuracy는 직관적이고 양쪽 데이터에서 일관됨 | 강점 |

---

## 9. 종합 우선순위 실행 계획

```
즉시 실행 (1-2일)
├── [6.1] 조건별 별도 GMM 결과 정리 (이미 스크립트 존재)
├── [6.2] SABIC 계산 추가 (EdNet + Chess 모두)
├── [6.3] 분류 품질 종합 표 작성
└── [4.4] BIC/ICL/SABIC/BLRT/entropy 비교 표 작성

단기 (3-5일)
├── [6.4] LCGA/GBTM 구현 (lcmm 패키지, EdNet 먼저)
├── [6.5] Mixed-effects model 실행 (lme4)
├── [6.6] K-means 삼각 검증
└── [5.1] 윈도우 크기 민감도 분석 (EdNet)

중기 (1-2주)
├── [6.4] Chess LCGA (piecewise model)
├── [6.7] 피처 중요도 분석
├── [7.2] 변화점 탐지 (Chess)
└── [6.9] 시뮬레이션 검증 (선택적)

논문 보고 필수 항목
├── 모형 선택 기준 비교 표 (BIC, ICL, SABIC, BLRT, entropy)
├── 클래스별 평균 사후확률 + entropy
├── 부트스트랩 G 안정성 결과
├── 조건별 별도 GMM 결과
├── 소표본 한계 및 해석적 주의사항
└── 최소 2개 방법(GMM + 1) 결과 비교
```

---

## 10. 결론

이 연구의 가장 큰 강점은 **이론-실증 정합성**과 **두 독립 데이터셋에서의 패턴 재현**이다. 특히 AI Benefit Emergence의 Gap 값이 두 데이터셋에서 -0.600/-0.601로 거의 동일하다는 것은 인상적이다. 그러나 방법론적 엄밀성 측면에서 다음 세 가지가 가장 시급하다:

1. **LCGA/GBTM 추가**: "궤적 분류" 논문에서 궤적 모형을 사용하지 않은 것은 리뷰어의 가장 큰 비판 포인트가 될 것이다. GMM은 보완적 방법으로 유지하되, LCGA가 주 분석이 되어야 한다.

2. **Chess 소표본 한계의 정직한 보고**: N=100에서 6-class GMM의 결과는 "시사적(suggestive)"이지 "확정적(definitive)"이 아니다. 특히 N=2 클래스와 N=9 클래스의 해석은 극도로 주의해야 한다.

3. **다중 기준에 의한 모형 선택**: BIC만으로는 부족하다. ICL, SABIC, BLRT가 일관된 클래스 수를 지지하는지 보여야 한다.

이 세 가지를 해결하면, 현재의 B+ 수준 방법론이 A- 이상으로 상승하며, CHI/Human Factors/IJAIED 수준의 상위 저널 게재가 충분히 가능하다.

---

## 참고 문헌

- Curran, P. J., Obeidat, K., & Losardo, D. (2010). Twelve frequently asked questions about growth curve modeling. *Journal of Cognition and Development*, 11(2), 121-136.
- Henson, J. M., Reise, S. P., & Kim, K. H. (2007). Detecting mixtures from structural model differences using latent variable mixture modeling. *Structural Equation Modeling*, 14(2), 202-226.
- Jung, T., & Wickrama, K. A. S. (2008). An introduction to latent class growth analysis and growth mixture modeling. *Social and Personality Psychology Compass*, 2(1), 302-317.
- Lubke, G., & Neale, M. C. (2006). Distinguishing between latent classes and continuous factors: Resolution by maximum likelihood? *Multivariate Behavioral Research*, 41(4), 499-532.
- Nagin, D. S. (2005). *Group-based modeling of development*. Harvard University Press.
- Nylund, K. L., Asparouhov, T., & Muthen, B. O. (2007). Deciding on the number of classes in latent class analysis and growth mixture modeling: A Monte Carlo simulation study. *Structural Equation Modeling*, 14(4), 535-569.
- Tein, J.-Y., Coxe, S., & Cham, H. (2013). Statistical power to detect the correct number of classes in latent profile analysis. *Structural Equation Modeling*, 20(4), 640-657.
