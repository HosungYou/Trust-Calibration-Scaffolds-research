# 논문 분리 전략 및 수리적 모형 설계
## TCR Paper 4 구조 의사결정 + Bayesian Trust Update Model

**작성일:** 2026-03-12
**의사결정자:** Hosung You
**맥락:** 4개 리뷰어 팀 논의(Discussion 04) 이후 전략적 방향 결정

---

## 1. 논문 분리의 근거: 왜 합치면 안 되는가

### 1.1 데이터의 구조적 이질성

EdNet과 Chess Puzzle은 같은 이론적 프레임워크를 공유하지만, 방법론적으로 **다른 종(species)의 연구**이다.

| 차원 | EdNet KT3 | Chess Puzzle (Bondi 2023) |
|------|-----------|--------------------------|
| **설계** | 관찰(observational) | 실험(experimental, within-subject) |
| **표본** | N=4,568 세션 | N=100 세션 (50명 × 2조건) |
| **기간** | ~150 에피소드/학생 | 30 시행/조건 |
| **R_b 측정** | 간접 proxy (기능 채택 비율) | 직접 측정 (AI 수용/거부 이진 결정) |
| **AI_accuracy** | 존재하지 않음 (P_adaptive로 대리) | 직접 측정 (multiPV==1) |
| **Trust violation** | 없음 (자연주의적 환경) | 있음 (시행 20에서 신뢰성 전환) |
| **구성 타당도** | 중간 (Reviewer B 평가) | 높음 (Reviewer B 평가) |
| **탐지 가능 패턴** | Convergent, Stagnant, ABE | Convergent, Catastrophic, Oscillating, ABE |

이 차이들은 "보완적"이라고 포장할 수 있지만, 하나의 논문에 넣으면 리뷰어가 **즉시** 다음을 지적한다:

> "EdNet의 R_b는 feature adoption ratio이고 Chess의 R_b는 binary follow rate인데, 이 둘의 cal_gap을 같은 축 위에 놓고 수치를 비교하는 것의 측정 동치성(measurement equivalence) 근거가 어디 있는가?"

이 질문에 대한 만족스러운 답이 없다. 합치면 이 약점이 논문 전체를 관통하는 구조적 결함이 된다.

### 1.2 합칠 때의 구체적 위험

**위험 1: "독립적 재현" 유혹**

합치면 자연스럽게 "두 데이터셋에서 패턴이 재현되었다"는 서사로 흐른다. Reviewer A(Devil's Advocate)는 이를 "허구적 재현"으로 평가했다:
- 같은 연구자가 같은 파이프라인을 적용 → 파이프라인 독립성 부재
- Gap ≈ −0.600의 수치 수렴 → 수학적 필연이지 심리적 재현이 아닐 가능성
- 구성개념이 다르므로 "같은 패턴"이라는 주장 자체가 불안정

**위험 2: 방법론 섹션의 복잡화**

두 데이터셋의 전처리, 변수 정의, 윈도우 구성이 모두 다르므로, Method 섹션이 비대해진다. 리뷰어는 각 데이터셋별로 다른 방법론적 질문을 하게 되고, 저자는 두 전선에서 동시에 방어해야 한다.

**위험 3: 근거 수준의 평균화**

Chess의 Catastrophic 패턴은 GRADE "중간"으로 상당히 강력한 증거인데, EdNet의 Stagnant는 "낮음"이다. 합치면 각각의 강점이 희석되고, 전체 논문의 근거 수준이 "가장 약한 고리"에 의해 결정된다.

### 1.3 나눌 때의 이점

**Paper 4 (이론 + EdNet):**
- T × R × τ 이론적 프레임워크 제안이 주인공
- EdNet(N=4,568)은 대규모 탐색적 실증으로서 이론의 초기 증거 제공
- "Theory-generating exploratory study" 프레이밍에 완벽
- EdNet의 구성 타당도 한계를 솔직히 인정하되, 대규모 표본의 안정성으로 보완
- 타겟: IJHCS, CHB

**Paper 5 (Chess Puzzle 독립 연구):**
- Paper 4에서 제안된 이론의 **최초 실험적 탐색**
- Chess의 높은 구성 타당도가 빛남
- Trust violation/repair 조건이 Catastrophic/ABE에 대한 방향적 기대 검증 가능
- "Theory-testing exploratory study" (완전한 confirmatory는 아니지만, 방향적 기대가 선행)
- 타겟: Human Factors, IJHCS, Journal of Experimental Psychology: Applied

**논문 간 관계:**
```
Paper 4                           Paper 5
─────────                         ─────────
이론 제안 + 수리적 모형    →      이론의 실험적 탐색
EdNet 탐색적 실증                 Chess Puzzle
ABE 귀납적 발견                   Catastrophic/ABE 방향적 검증
                                  Trust violation 메커니즘 집중 분석
```

Paper 5의 Introduction에서 "You (2026)가 제안한 T × R × τ 프레임워크의 5개 궤적 유형 중, Trust violation이 유발하는 Catastrophic 패턴과 Trust repair에서의 AI Benefit Emergence 패턴을 실험적으로 탐색한다"로 시작하면, Paper 4가 선행 연구로 자연스럽게 인용된다.

### 1.4 의사결정

**결론: 분리한다.**

- Paper 4 = T × R × τ 이론 + 수리적 모형 + EdNet 탐색적 실증
- Paper 5 = Chess Puzzle 독립 실험 연구 (Paper 4 이론의 최초 실험적 탐색)
- 두 논문의 병렬 사용은 하지 않는다 (이전 결정 유지)
- 각 논문이 자기 완결적(self-contained)이어야 한다

---

## 2. 수리적 모형: Bayesian Trust Update Model

### 2.1 왜 수리적 모형이 필요한가

리뷰어 팀의 핵심 비판 중 하나는 "5개 패턴이 질적 기술(qualitative description)에 머문다"는 것이다. 패턴에 이름을 붙이는 것은 유형학(typology)이지, 이론(theory)이 아니다. 이론이 되려면 **메커니즘**을 명시하고, 메커니즘에서 **패턴이 도출**되어야 한다.

수리적 모형은 이 역할을 한다:
- 메커니즘 = "사람은 AI 성능에 대한 예측 오차를 통해 신뢰를 업데이트한다"
- 패턴 = "학습률(α)의 크기와 비대칭성에 따라 5개 궤적이 발생한다"

이 모형이 있으면 논문의 이론적 기여가 **유형학 제안**에서 **역학적 이론 제안**으로 격상된다.

### 2.2 기본 모형: 예측 오차 기반 신뢰 업데이트

심리학의 Rescorla-Wagner 학습 규칙과 Bayesian trust update 문헌(Guo & Yang, 2023; Xu & Dudek, 2015)에 기반한다.

#### 핵심 방정식

$$T_{t+1} = T_t + \alpha \cdot \delta_t$$

여기서:
- $T_t$ = 시점 t에서의 **행동적 신뢰** (관찰 가능: R_b에 대응)
- $R_t$ = 시점 t에서의 **AI 신뢰성** (관찰 가능: AI_accuracy에 대응)
- $\delta_t = R_t - T_t$ = **예측 오차** (AI 성능과 현재 신뢰 수준의 불일치)
- $\alpha$ = **학습률** (0 ≤ α ≤ 1, 개인차 파라미터)

**직관적 해석:**
- $\delta_t > 0$: AI가 기대보다 좋다 → 신뢰 증가 (양의 예측 오차)
- $\delta_t < 0$: AI가 기대보다 나쁘다 → 신뢰 감소 (음의 예측 오차)
- $\alpha$가 크면 빠르게 적응, 작으면 느리게 적응

#### 비대칭 확장: Dual Learning Rate

Lee & Moray (1992)의 신뢰 비대칭성(trust asymmetry)을 수학적으로 포착하기 위해 학습률을 방향에 따라 분리한다.

$$T_{t+1} = T_t + \begin{cases} \alpha^+ \cdot \delta_t & \text{if } \delta_t > 0 \text{ (AI가 기대보다 좋을 때)} \\ \alpha^- \cdot \delta_t & \text{if } \delta_t < 0 \text{ (AI가 기대보다 나쁠 때)} \end{cases}$$

여기서:
- $\alpha^+$ = **상향 학습률** (신뢰 증가 속도)
- $\alpha^-$ = **하향 학습률** (신뢰 감소 속도)
- 일반적으로 Lee & Moray에 따르면 $\alpha^- > \alpha^+$ (신뢰는 쉽게 깨지고 천천히 쌓인다)

#### Cal_gap과의 관계

모형에서 calibration gap은:

$$G_t = T_t - R_t$$

이 모형의 동역학에서:

$$G_{t+1} = T_{t+1} - R_{t+1}$$
$$= (T_t + \alpha \cdot \delta_t) - R_{t+1}$$
$$= T_t + \alpha(R_t - T_t) - R_{t+1}$$
$$= (1-\alpha)T_t + \alpha R_t - R_{t+1}$$

R이 일정할 때 ($R_t = R$): $G_{t+1} = (1-\alpha)T_t + \alpha R - R = (1-\alpha)(T_t - R) = (1-\alpha)G_t$

즉 **R이 일정하면 Gap은 기하급수적으로 0에 수렴**한다. 수렴 속도는 $(1-\alpha)$에 의해 결정된다.

### 2.3 5개 궤적 패턴의 수리적 도출

각 패턴이 모형의 어떤 파라미터 조건에서 발생하는지를 도출한다.

---

#### 패턴 1: Convergent (수렴형)

**파라미터 조건:**
- $\alpha^+ > 0$ 이고 $\alpha^- > 0$ (양방향 학습 활성)
- $\alpha^+ \approx \alpha^-$ (대칭적 학습) 또는 둘 다 충분히 큼

**역학:**
$$G_t \rightarrow 0 \text{ as } t \rightarrow \infty$$

R이 일정하든 변하든, 학습률이 충분히 크면 T는 R을 추적(track)한다. 수렴 시간은 $\tau_{conv} \approx -1/\ln(1-\alpha)$로 추정된다.

**실증 대응:**
- Chess Class 3 (Gradual Adaptor): $\alpha \approx 0.3-0.4$ (점진적 수렴)
- Chess Class 1 (Adaptive Reducer): $\alpha^- \approx 0.5-0.7$ (빠른 하향 적응)

**기존 문헌:** Lee & See (2004) — 신뢰는 경험 축적에 따라 적응적으로 업데이트된다

---

#### 패턴 2: Stagnant (정체형)

**파라미터 조건:**
- $\alpha^+ \approx 0$ 이고 $\alpha^- \approx 0$ (양방향 학습 거의 부재)

**역학:**
$$T_{t+1} \approx T_t \quad \forall t$$
$$G_t \approx G_0 = T_0 - R_t \text{ (T가 고정, R 변화에 무반응)}$$

Gap은 초기값에서 거의 변하지 않는다. 신뢰 업데이트 메커니즘 자체가 비활성화된 상태.

**메커니즘 해석:**
- 인지적 무관심(cognitive disengagement): AI 성능에 주의를 기울이지 않음
- 고정된 사전 신념(strong prior): 초기 신뢰 수준이 너무 강해서 증거에 의해 업데이트되지 않음
- 또는 Kahneman (2011)의 System 1 우세: 느린 분석적 처리(System 2) 없이 습관적 행동 유지

**실증 대응:**
- EdNet Class 4 (N=451): R_b ≈ 0.06-0.11, 거의 변화 없음

**기존 문헌:** Parasuraman & Riley (1997) — 자동화 편향(automation bias)의 지속; Goddard et al. (2012) — 신뢰 관성(trust inertia)

---

#### 패턴 3: Catastrophic (재앙형)

**파라미터 조건:**
- $\alpha^- \approx 0$ (AI가 나빠져도 신뢰를 내리지 않음)
- R이 급격히 하락하는 Trust violation event 발생

**역학:**

R이 $R_{high}$에서 $R_{low}$로 급락할 때:
$$\delta_t = R_{low} - T_t < 0 \text{ (큰 음의 예측 오차)}$$
$$T_{t+1} = T_t + \alpha^- \cdot \delta_t \approx T_t \text{ (α⁻ ≈ 0이므로)}$$

결과:
$$G_t = T_t - R_{low} \approx T_0 - R_{low} \gg 0$$

Gap이 급격히 양의 방향으로 폭증하고 지속된다. 신뢰(T)는 높은 수준에 머물러 있는데 실제 AI 성능(R)은 떨어졌으므로, 과의존(over-reliance)이 발생한다.

**Stagnant와의 차이:**
- Stagnant: $\alpha^+ \approx \alpha^- \approx 0$ (양방향 모두 학습 부재, R 변화 없이도 발생)
- Catastrophic: $\alpha^- \approx 0$ 이지만 R의 급격한 하락이 **조건**(trust violation event가 필요)

**메커니즘 해석:**
- Automation complacency (Parasuraman, Molloy, & Singh, 1993): 자동화 시스템에 대한 경계 약화
- 확증 편향: AI가 이전에 잘 작동했던 기억이 현재의 실패 증거를 억압
- Anchoring (Tversky & Kahneman, 1974): 초기 높은 신뢰가 앵커가 되어 하향 조정 불충분

**실증 대응:**
- Chess Class 5 (N=30, C1의 60%): AI_accuracy 1.000→0.200으로 급락, R_b 0.700→0.620 (미미한 감소), Gap −0.300→+0.420

**기존 문헌:** Lee & Moray (1992) — Trust violation 후 비대칭 회복; Dzindolet et al. (2003) — AI 성능 저하에 대한 과소반응

---

#### 패턴 4: Oscillating (진동형)

**파라미터 조건:**
- $\alpha^+$와 $\alpha^-$ 모두 존재하지만, 외부 R이 변동하거나 내적 기준(threshold)이 비선형적으로 작용

**역학 (두 가지 메커니즘):**

**메커니즘 A — 외부 R의 변동에 대한 과반응:**
$$\alpha > 1 \text{ (overshooting)}$$
$$T_{t+1} = T_t + \alpha(R_t - T_t) \text{에서 α > 1이면 T가 R을 넘어섬}$$

예: R=0.8에서 T=0.5일 때, α=1.2이면 T(t+1) = 0.5 + 1.2(0.3) = 0.86 > R. 다음 시점에서 δ < 0이 되어 T가 다시 감소 → 진동.

**메커니즘 B — 임계값 기반 전환 (threshold switching):**
$$\alpha = \begin{cases} \alpha_{high} & \text{if } |G_t| > \theta \text{ (gap이 임계값 초과 시 강한 반응)} \\ \alpha_{low} & \text{if } |G_t| \leq \theta \text{ (gap이 작으면 반응 약화)} \end{cases}$$

이 비선형 학습률은 limit cycle(한계 순환)을 만들어낸다: gap이 커지면 강하게 반응 → gap 감소 → 반응 약화 → gap 다시 증가.

**실증 대응:**
- Chess Class 2 (N=14): R_b가 비단조적으로 변동, gap_sd = 0.421

**기존 문헌:** Gao & Lee (2006) — 신뢰의 진동적 회복; Muir & Moray (1996) — 반복적 실패-회복 사이클

**참고:** 현재 데이터에서 Oscillating 패턴의 근거가 가장 약하다 (GRADE: Low). 30시행 6윈도우에서의 비단조성이 진동인지 잡음인지 구분이 어려움. 이 한계를 논문에서 명시해야 한다.

---

#### 패턴 5: AI Benefit Emergence (AI 혜택 출현형) — 귀납적 발견

**파라미터 조건:**
- $\alpha^+ \ll \alpha^-$ (상향 학습이 하향 학습보다 **현저히** 느림)
- R이 점진적으로 증가하는 환경

**역학:**

R이 $R_{low}$에서 $R_{high}$로 점진적으로 증가할 때:
$$\delta_t = R_t - T_t > 0 \text{ (양의 예측 오차, AI가 기대보다 좋음)}$$
$$T_{t+1} = T_t + \alpha^+ \cdot \delta_t$$

$\alpha^+$가 매우 작으므로:
$$T_t \approx T_0 + \alpha^+ \sum_{s=0}^{t} \delta_s$$

T의 증가가 R의 증가를 따라잡지 못하면:
$$G_t = T_t - R_t < 0 \text{ 이고 } |G_t| \text{가 시간에 따라 증가}$$

**핵심 비대칭:**
$$\frac{\alpha^+}{\alpha^-} \ll 1$$

이것이 Lee & Moray (1992)의 신뢰 비대칭성의 수학적 표현이다. 신뢰는 "한번 깨지면 쉽게 무너지고(α⁻ 큼), 개선 증거가 있어도 천천히 쌓인다(α⁺ 작음)." ABE 패턴은 이 비대칭성이 극단적으로 강한 개인들에서 나타난다.

**추가 메커니즘 — Anchoring:**
$$T_0 \text{가 낮은 값(초기 불신)에 앵커링된 경우,}$$
$$T_t \text{가 증가하더라도 } T_0 \text{에서 크게 벗어나지 못함}$$

이는 Tversky & Kahneman (1974)의 anchoring-and-insufficient-adjustment와 정합적이다.

**Catastrophic과의 대칭적 관계:**
```
Catastrophic:  R↓ but T stays high  → Gap > 0 (over-reliance)
    α⁻ ≈ 0, trust violation event 필요

ABE:           R↑ but T stays low   → Gap < 0 (under-reliance)
    α⁺ ≈ 0, trust repair opportunity에서 발생
```

두 패턴은 **수학적 거울상(mirror image)**이다. 하나는 하향 비적응(downward non-adaptation), 다른 하나는 상향 비적응(upward non-adaptation). 이 대칭성 자체가 이론적으로 흥미로운 발견이다.

**실증 대응:**
- EdNet Class 4 (N=256): P_adaptive 0.275→0.852, R_b 0.020→0.171, Gap→−0.601
- Chess Class 4 (N=9): AI_accuracy 0.000→0.800, R_b 0.267→0.200, Gap→−0.600

**기존 문헌:** Parasuraman & Riley (1997) — disuse; Lee & Moray (1992) — trust asymmetry

**주의:** 이 패턴은 EdNet 분석에서 귀납적으로 발견되었다. 논문에서 이를 명시하고, "나머지 4개 패턴은 선행 문헌에서 연역적으로 도출, ABE는 데이터에서 귀납적으로 발견 후 이론적으로 해석"으로 분류해야 한다.

### 2.4 파라미터 공간과 패턴 지도

5개 패턴을 ($\alpha^+$, $\alpha^-$) 2차원 파라미터 공간에 배치하면:

```
α⁻ (하향 학습률)
↑
1.0 ┤
    │          Convergent
    │        (α⁺ ≈ α⁻, 둘 다 중간-높음)
    │               ●
    │
0.5 ┤     Oscillating
    │    (α 큼 + 비선형,
    │     또는 α > 1)
    │          ●
    │
    │   ABE                    Stagnant
    │  (α⁺ ≪ α⁻)             (α⁺ ≈ α⁻ ≈ 0)
0.0 ┤    ●───────────────────────● ─────────→ α⁺
    │                          Catastrophic
    │                          (α⁻ ≈ 0, R↓ 조건)
    │                               ●
    └──────┬──────┬──────┬──────┬──────→
          0.0   0.25  0.50  0.75  1.0
                     α⁺ (상향 학습률)
```

이 그림이 논문의 **Figure 1**이 될 수 있다. T × R × τ의 3D 궤적 figure는 **Figure 2**.

**핵심 통찰:**
- α⁺ = α⁻ 대각선: 대칭적 학습 → Convergent
- α⁺ ≈ α⁻ ≈ 0 원점 근방: 학습 부재 → Stagnant
- α⁺ ≈ 0, α⁻ > 0: 상향 비적응 → ABE (R↑ 조건에서)
- α⁺ > 0, α⁻ ≈ 0: 하향 비적응 → Catastrophic (R↓ 조건에서)
- ABE와 Catastrophic은 원점에서 각각 y축, x축 방향으로 떨어진 **거울상**

### 2.5 모형의 범위와 한계

#### 이 모형이 하는 것:
1. 5개 패턴을 **통합된 메커니즘**(예측 오차 기반 학습)에서 도출
2. 패턴 간 관계(특히 Catastrophic ↔ ABE 대칭)를 수학적으로 명시
3. 개인차를 **두 개의 파라미터**($\alpha^+$, $\alpha^-$)로 환원 → 검증 가능한 예측 생성
4. 향후 연구의 가설 기반 제공 ("α⁺/α⁻를 측정하여 패턴을 예측할 수 있는가?")

#### 이 모형이 하지 않는 것:
1. α의 결정 요인을 설명하지 않음 (왜 어떤 사람은 α⁺가 낮은가? → 성격, 경험, 도메인 전문성 등)
2. R의 변화를 모형화하지 않음 (R은 외생적으로 주어진다고 가정)
3. 과제 특수적 요인(체스 전문성, 문제 난이도 등)을 포함하지 않음
4. **Paper 4에서 이 모형의 파라미터를 formal하게 추정하지 않는다** → illustrative level

#### 전략적 결정: Formal fitting 여부

**Option A — Illustrative only (권장):**
- 모형을 이론적 프레임워크로 제안하고, 각 패턴이 어떤 파라미터 조건에서 발생하는지 보여줌
- GMM 결과와 모형 예측의 **질적 일치**만 논의 ("Class 5의 행동은 α⁻ ≈ 0에 해당한다")
- Formal parameter estimation은 "향후 연구"로 남김

장점: 과적합 비판을 회피, 모형의 단순함 유지, 이론적 기여에 집중
단점: 리뷰어가 "왜 fitting을 안 했나" 질문 가능

**Option B — Simple fitting:**
- 각 참가자의 시행별 데이터에 모형을 fitting하여 개인별 ($\alpha^+$, $\alpha^-$) 추정
- 추정된 α 값의 분포가 GMM 클래스와 대응하는지 확인

장점: 더 강력한 증거, 모형 검증 가능
단점: 추가 분석 필요, 과적합 위험, EdNet에서는 R이 관찰 불가

**의사결정: Paper 4는 Option A (Illustrative). Paper 5(Chess)에서 Option B를 시도할 수 있다.**

Chess Puzzle은 시행 단위의 R(AI_accuracy)과 T(followed_ai) 모두 관찰 가능하므로, 개인별 α fitting이 구조적으로 가능하다. 이것이 Paper 5의 차별화된 기여가 될 수 있다.

---

## 3. 수정된 논문 구조

### Paper 4: Theory + EdNet

```
Title: "Trajectories of Trust Calibration in Human-AI Interaction:
        A Bayesian Learning Framework and Exploratory Evidence"

Target: IJHCS (1순위) 또는 CHB (2순위)

1. Introduction
   - 정적 신뢰 연구의 한계
   - 궤적 관점의 필요성
   - 연구 목적: 이론적 프레임워크 제안 + 탐색적 실증

2. Theoretical Framework
   2.1 T × R × τ 공간의 정의
   2.2 Bayesian Trust Update Model (α⁺, α⁻)
   2.3 4개 궤적 패턴의 연역적 도출
       (Convergent, Oscillating, Stagnant, Catastrophic)
   2.4 파라미터 공간 지도 (Figure 1)
   2.5 궤적의 3D 시각화 (Figure 2)

3. Exploratory Study: EdNet KT3
   3.1 데이터 및 변수 조작화 (R_b proxy의 한계 명시)
   3.2 GMM 분석 (탐색적 목적 명시)
   3.3 (추가) LCGA 비교 분석
   3.4 결과: 이론 패턴과의 일관성 + ABE 귀납적 발견
   3.5 제5 패턴: AI Benefit Emergence의 이론적 해석
       → Catastrophic의 거울상으로서의 ABE
       → α⁺ ≪ α⁻ 조건에서의 도출
       → 수리적 모형에의 통합 (2.2절 확장)

4. General Discussion
   4.1 이론적 기여: 5개 궤적 유형학 + Bayesian 메커니즘
   4.2 ABE의 의의: 귀납적 발견에서 이론적 통합으로
   4.3 한계
       - 탐색적 연구, 사전등록 부재
       - EdNet R_b의 구성 타당도 한계
       - GMM 과적합 가능성 (PCA + 다중기준으로 보완)
       - Stagnant의 대안 해석 (합리적 무의존 vs 정체)
   4.4 실용적 함의: 적응형 AI 시스템 설계
   4.5 향후 연구: 실험적 검증(→Paper 5), α fitting, 개입 설계
```

### Paper 5: Chess Puzzle (향후)

```
Title: "Trust Violation and Repair Trajectories in Human-AI Decision Making:
        An Experimental Study of Calibration Dynamics"

Target: Human Factors (1순위) 또는 J. Exp. Psych: Applied (2순위)

1. Introduction
   - You (2026)의 T × R × τ 프레임워크 요약
   - Trust violation/repair 조건에서의 구체적 예측
   - Chess Puzzle 실험의 이론적 위치

2. Theoretical Predictions (Paper 4 이론에서 도출)
   - C1 (High→Low): Catastrophic vs Convergent 분리 예측
   - C2 (Low→High): ABE vs Convergent 분리 예측
   - α 파라미터의 개인차가 패턴을 결정한다는 가설

3. Method
   - Bondi et al. (2023) 데이터 (CC BY 4.0)
   - 변수 정의, 윈도우 구성, 분석 전략

4. Results
   - GMM + LCGA
   - α fitting (개인별 학습률 추정)
   - 추정된 α와 패턴 대응
   - 조건별 분석 (C1/C2 별도)

5. Discussion
   - 이론의 실험적 지지/비지지 정리
   - Catastrophic (C1 60%)의 함의: 과의존의 보편성
   - ABE의 재확인: 방향적 일관성 vs 수치 수렴의 해석
   - 한계: N=50/조건, 소표본, 체스 전문성 미통제
```

---

## 4. 타겟 저널 최종 권고

### Paper 4

| 순위 | 저널 | IF | 적합 이유 |
|:----:|------|:--:|----------|
| 1 | **IJHCS** | ~5.4 | 이론 + 탐색적 실증의 조합에 최적, HCI 이론 논문 환영, 긴 논문 수용 |
| 2 | **CHB** | ~9.0 | 높은 IF, 넓은 독자층, 다만 방법론적 엄밀성 요구 높음 |
| 3 | **CSCW** | conf. | 인간-AI 협업 맥락, 다만 실증 중심 컨퍼런스 |

### Paper 5

| 순위 | 저널 | IF | 적합 이유 |
|:----:|------|:--:|----------|
| 1 | **Human Factors** | ~3.3 | Trust in automation의 본거지, Catastrophic 패턴의 자연스러운 집 |
| 2 | **IJHCS** | ~5.4 | Paper 4와 같은 저널에 연속 게재 전략 |
| 3 | **J. Exp. Psych: Applied** | ~3.9 | 실험적 의사결정 연구에 최적 |

---

## 5. 즉시 필요한 후속 질문

다음 의사결정이 필요하다:

1. **Paper 4의 LCGA 분석 범위:** EdNet에서만 할 것인가, 이론적 예시로만 사용할 것인가?
2. **수리적 모형의 표현 수준:** LaTeX 수식을 논문 수준으로 정리할 것인가, 아니면 직관적 서술로 충분한가?
3. **Paper 5의 시작 시점:** Paper 4 투고 후에 시작할 것인가, 병렬로 진행할 것인가?
4. **OSF 사전등록:** Paper 5의 Chess 분석 중 아직 미실행 항목(α fitting, LCGA)을 사전등록할 것인가?

---

*본 문서는 4개 전문 리뷰어 팀 논의(Discussion 04)의 합의사항과 연구자의 전략적 판단을 통합한 의사결정 기록이다.*
