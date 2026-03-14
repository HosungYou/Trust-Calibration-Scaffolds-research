# Trust-Reliability Matrix 3D 확장 분석

**Date:** 2026-03-11
**Context:** 2D Trust-Reliability Matrix의 3D 확장 후보축 탐색
**Related Papers:** Paper 1 (SLR), Paper 2 (TCRS), Paper 3 (TCR-Competency)

---

## 1. 현재 2D 모델

```
Trust (T)
  High │  Q3: Undertrust        Q1: Calibrated
       │  (Missed Benefit)      (Appropriate Use)
       │
       │─ ─ ─ ─ ─ ─ ─ y=x ─ ─ ─ ─ ─ ─ ─
       │                    ╱
  Low  │  Q4: Calibrated   ╱  Q2: Overtrust
       │  (Avoidance)     ╱   ("Bastani Trap")
       │                 ╱
       └──────────────────────────────────
         Low                        High
                AI Reliability (R)
```

**한계:** 정적 스냅샷. 같은 (T, R) 좌표에 있어도 그 사람이 그 상태를 인식하는지, 그 상태가 어떻게 변해가는지, 또는 그 상태의 결과가 얼마나 심각한지를 구분할 수 없음.

---

## 2. 후보 제3축 (4개)

### Axis A: Metacognitive Awareness (자기 인식 정확도)

**"나는 내가 이 AI를 얼마나 신뢰하는지 알고 있는가?"**

Z-axis: Awareness (A)
= 자신의 trust 수준에 대한 인식의 정확도 (0 → 1)
- A = 1: 자신의 trust level을 정확히 인식
- A = 0: 자신이 overtrust/undertrust하는지 모름

**8개 영역 (2³ cube):**

| T | R | A | State | Label |
|---|---|---|-------|-------|
| H | H | H | Calibrated + Aware | **Informed Reliance** — 최적 상태 |
| H | H | L | Calibrated + Unaware | **Lucky Calibration** — 우연히 교정됨, 취약 |
| H | L | H | Overtrust + Aware | **Recoverable Overtrust** — 인식하고 있으므로 교정 가능 |
| H | L | L | Overtrust + Unaware | **Blind Overtrust** — 가장 위험한 상태 |
| L | H | H | Undertrust + Aware | **Informed Skepticism** — 전략적 저신뢰 |
| L | H | L | Undertrust + Unaware | **Blind Undertrust** — 기회 상실 모름 |
| L | L | H | Calibrated Avoidance + Aware | **Informed Avoidance** — 적절한 회피 |
| L | L | L | Calibrated Avoidance + Unaware | **Accidental Avoidance** — 우연히 맞음 |

**Singularity 1 — "The Dunning-Kruger Trap" (T=H, R=L, A=L):**

```
                    Trust
                     High
                      │
          ┌───────────┼───────────┐
         ╱│          ╱│          ╱│
        ╱ │  BLIND  ╱ │ RECOVER ╱ │
       ╱  │OVERTRUST╱  │  ABLE  ╱  │
      ┌───────────┬───────────┐   │
      │ ★★★★★★★ │           │   │
      │ SINGULARITY│          │   │
      │ Point:     │          │   │   Awareness
      │ Intervention│         │   │     High
      │ fails here │          │   ├─ ─ ─ →
      │           │          │  ╱
      │           │          │ ╱
      └───────────┴──────────╱┘
      Low                  High
           AI Reliability
```

이 지점에서 개입(intervention)이 실패합니다. 투명성을 제공해도(R 정보를 줌) 자신이 과신하고 있다는 것을 인식하지 못하므로(A=Low) 정보를 무시합니다. 이것은 Bastani et al. (2025)이 발견한 정확한 현상: AI를 과신하는 학생들에게 AI의 한계를 알려줘도 행동이 변하지 않는 이유.

탈출 경로: 오직 productive failure (AI 오류 직접 경험)만이 A를 강제로 올려서 이 singularity에서 빠져나올 수 있음 → Framework의 Scaffold 3과 직접 연결.

**Singularity 2 — "Lucky Calibration Fragility" (T≈R, A=L):**

우연히 trust ≈ reliability인 상태이지만, 자신이 왜 calibrated인지 모름. AI의 reliability가 변하는 순간 (업데이트, 다른 도메인) 즉시 miscalibration에 빠지지만 인식하지 못함. False stability — 겉으로는 calibrated이지만 내적으로는 취약.

**Singularity 3 — "Awareness Paradox" (T=H, R=L, A=H):**

자신이 overtrust하고 있음을 알지만 행동을 바꾸지 못함 — Process Model에서 Judgment → Action gap. 인지 부조화 상태. 이것이 바로 3단계(Action)가 별도 역량인 이유의 경험적 근거가 됨.

---

### Axis B: Time / Experience (τ)

**"이 calibration 상태는 어떻게 변화해 왔는가?"**

Z-axis: Time (τ) = AI와의 상호작용 횟수 또는 경과 시간

**Singularity — Trust Hysteresis (신뢰 이력 현상):**

```
Trust
  │
H │        ╭──────────── Trust Building Path
  │       ╱               (slow, gradual)
  │      ╱
  │     ╱    ╲
  │    ╱      ╲ Trust Erosion Path
  │   ╱        ╲ (fast, steep)
  │  ╱          ╲
L │ ╱            ╰─────
  │╱
  └────────────────────── Time (τ)
       AI Error
       Event
```

신뢰 구축(building)과 신뢰 침식(erosion)의 경로가 다릅니다 — 이것이 hysteresis. 같은 reliability 수준이라도 "신뢰를 쌓아가는 중"인지 "신뢰가 무너진 후 회복 중"인지에 따라 trust level이 완전히 다름. 3D에서 이것은 나선형(spiral) 궤적으로 나타남.

**Catastrophe Theory 적용:**

```
        Trust
         │   ╱╲  Fold Surface
         │  ╱  ╲
         │ ╱    ╲ ← Catastrophe point:
         │╱      ╲   small R change →
         │        ╲  sudden T collapse
         │         ╲
         └──────────────── Reliability
                    ↑
            Critical threshold
```

Reliability가 점진적으로 감소할 때, trust는 서서히 감소하다가 임계점(critical threshold)에서 갑자기 붕괴합니다 (catastrophe). 이것은 Thom의 Catastrophe Theory와 직접 연결됨 — trust calibration에 적용한 사례가 없음.

---

### Axis C: Domain Expertise (E)

**"이 분야에 대해 얼마나 알고 있는가?"**

Z-axis: Domain Expertise (E) = 특정 AI 활용 도메인에서의 전문성 수준 (0 → 1)

**핵심 발견:**

| T | R | E | Meaning |
|---|---|---|---------|
| H | L | L | Novice overtrust — Bastani trap (가장 위험, 가장 흔함) |
| H | L | H | Expert complacency — 전문가도 과신할 수 있음 (다른 메커니즘) |
| L | H | L | Novice AI aversion — AI를 이해하지 못해 불신 |
| L | H | H | Expert algorithm aversion — 자기 전문성에 의한 불신 (Dietvorst et al., 2015) |

**Singularity — "Expertise Crossover Point":**

```
Calibration
Accuracy
  │
H │              ╭──── Expert: eventually calibrates
  │             ╱
  │            ╱
  │    ╳ ←── Crossover: Intermediate expertise
  │   ╱ ╲     produces WORST calibration
  │  ╱   ╲
  │ ╱     ╰── Novice: uncalibrated but consistent
L │╱
  └────────────────────────────── Domain Expertise
  Low                                          High
```

중간 전문성 수준에서 calibration이 가장 나빠집니다 — "a little knowledge is dangerous."

---

### Axis D: Task Criticality / Stakes (S)

**"이 결정의 결과가 얼마나 중요한가?"**

Z-axis: Stakes (S) = 잘못된 calibration의 결과 심각도 (0 → 1)

**Singularity — "The Cliff Edge" (High Stakes + Miscalibrated):**

```
Consequence
Severity
  │
  │                    ╱
  │                   ╱  ← Catastrophic zone:
  │                  ╱     Overtrust + High Stakes
H │                 ╱      = irreversible harm
  │                ╱
  │───────────────╱── Threshold
  │              ╱
  │             ╱
L │ Tolerable  ╱
  │ zone      ╱
  └──────────────────────── Miscalibration Magnitude
```

---

## 3. 초기 종합 비교

| Third Axis | Singularity Type | 이론적 혁신성 | 수학적 모델링 | Process Model 연결 | 초기 추천도 |
|------------|-----------------|-------------|------------|------------------|-----------|
| A: Awareness | Dunning-Kruger, Lucky Calibration, Awareness Paradox | ★★★★★ | ★★★☆☆ | 직접 연결 (Stage 1) | 1순위 |
| B: Time | Hysteresis, Catastrophe, Attractor/Repeller | ★★★★☆ | ★★★★★ | Adaptive Calibration Cycle | 2순위 |
| C: Expertise | Crossover Effect, Expert Complacency | ★★★★☆ | ★★★☆☆ | Alexander MDL 연결 | 3순위 |
| D: Stakes | Cliff Edge, Complacency-to-Catastrophe | ★★★☆☆ | ★★★★☆ | 약함 | 4순위 |

**초기 분석의 추천:** Axis A (Awareness)를 제3축으로, Axis B (Time)는 4D 미래 확장으로.

---

## 4. 저자 피드백 및 재분석

### 4.1 저자 우려

> "Time은 객관적인 지표로서 다른 두 개를 보완하는 역할인 것 같은데, Awareness는 내 Readiness와 겹쳐지는 역할을 수행할 것 같다."

### 4.2 겹침 분석: Awareness vs. Readiness

**TCRS Process Model (Paper 2):**
- Trust Calibration **Readiness** = Awareness (CA-Aw) + Judgment (CA-Jd) + Action (CA-Ac)
- Readiness는 전체 프로세스 모델 (3단계 전부)
- Awareness (CA-Aw)는 Readiness의 Stage 1 — 하위 구성요소

**제안된 3D Matrix: T × R × A (Awareness):**
- A = 자신의 trust 상태에 대한 메타인지적 인식 정확도
- 이것은 본질적으로 CA-Aw (Readiness의 Stage 1)와 동일한 구성개념

**겹침 문제의 핵심:**

```
                    Trust-Reliability Matrix        TCRS Process Model
                    (진단 도구)                     (역량 도구)
                    ─────────────────              ─────────────────
  현재 2D:          T × R                          Readiness = Aw + Jd + Ac

  제안 3D:          T × R × Awareness              Readiness = [Awareness] + Jd + Ac
                            ↑                                    ↑
                            └──── 겹침! ─────────────────────────┘
```

**3가지 개념적 문제:**

1. **역할 혼동:** Trust-Reliability Matrix는 *시스템 수준 진단 도구* (이 사람은 T×R 공간 어디에 있는가?). TCRS Readiness는 *개인 수준 역량* (이 사람은 calibration할 준비가 되어 있는가?). Awareness를 3D Matrix에 추가하면, 진단 도구 안에 역량 도구의 하위 요소가 포함되어 두 도구의 경계가 흐려짐.

2. **부분 포함:** Awareness는 Readiness의 일부(1/3)만 대표. 3D Matrix에 Readiness 전체가 아닌 Awareness만 넣으면, Judgment와 Action은 어디로 가는가? 이론적으로 불완전함.

3. **설명 방향 역전:** Matrix는 "상태(state)"를 기술하는 도구인데, Awareness는 "과정(process)"의 시작점. 상태 기술 도구에 과정 변수를 넣는 것은 범주 혼합(category mixing).

### 4.3 Time (τ)이 더 적합한 이유

| 비교 기준 | Awareness (A) | Time (τ) |
|-----------|--------------|----------|
| Readiness와의 독립성 | 낮음 — CA-Aw와 직접 겹침 | 높음 — Readiness와 완전히 독립 |
| 기존 구성개념 추가 vs 새 차원 | TCRS에 이미 있는 것의 반복 | 완전히 새로운 구조적 차원 |
| Matrix의 본질적 한계 해결 | 정적 스냅샷 한계를 해결하지 못함 | 정적 → 동적 전환으로 핵심 한계 해결 |
| 측정 독립성 | 주관적 (self-report) — T와 측정 방법 겹침 | 객관적 — T, R과 완전히 다른 측정 |
| 이론적 역할 | TCRS의 하위 구성요소를 Matrix에 이중 배치 | Matrix에 새로운 분석 역량 부여 |
| 수학적 모델링 | ★★★☆☆ | ★★★★★ |

### 4.4 수정된 프레임워크: 분업 구조

```
┌──────────────────────────────────────────────────────────────────────┐
│                    TRUST CALIBRATION ECOSYSTEM                       │
│                                                                      │
│   ┌────────────────────────┐    ┌────────────────────────────────┐  │
│   │  Trust-Reliability      │    │  TCRS Process Model             │  │
│   │  Matrix + Time (3D)     │    │  (Readiness)                    │  │
│   │                         │    │                                  │  │
│   │  역할: 진단 (WHERE)     │    │  역할: 역량 (HOW)               │  │
│   │                         │    │                                  │  │
│   │  T × R × τ              │    │  Awareness → Judgment → Action  │  │
│   │                         │    │  (CA-Aw)    (CA-Jd)    (CA-Ac) │  │
│   │  "이 학습자는 T×R       │    │                                  │  │
│   │   공간에서 어디에 있고,  │    │  "이 학습자는 calibration할     │  │
│   │   시간에 따라 어떻게    │    │   준비가 되어 있는가?"          │  │
│   │   이동하고 있는가?"     │    │                                  │  │
│   │                         │    │                                  │  │
│   │  출력: 궤적(trajectory) │    │  출력: readiness score           │  │
│   │  + 동태 패턴            │    │  (CA-Aw, CA-Jd, CA-Ac)         │  │
│   └────────────┬────────────┘    └──────────────┬───────────────────┘  │
│                │                                 │                     │
│                └────────── 연결 ─────────────────┘                    │
│                                                                       │
│    Readiness는 Matrix 내 이동의 MECHANISM을 설명:                     │
│    높은 Readiness → y=x 라인으로의 수렴 궤적                        │
│    낮은 Readiness → 발산 또는 정체 궤적                              │
│                                                                       │
│    Time 축은 이 이동을 VISUALIZE:                                     │
│    Readiness가 작동하는 과정을 시각적으로 추적 가능                   │
└──────────────────────────────────────────────────────────────────────┘
```

### 4.5 Time 축의 고유 기여 (Awareness가 제공할 수 없는 것들)

**1. Trust Hysteresis 현상 포착:**
```
Trust
  │
H │        ╭──────────── Building (slow)
  │       ╱
  │      ╱
  │     ╱    ╲
  │    ╱      ╲ Erosion (fast)
  │   ╱        ╲
L │ ╱            ╰─────
  │╱
  └────────────────────── Time (τ)
```
같은 T=Medium, R=High 좌표라도 "구축 중"인지 "붕괴 후 회복 중"인지 구분 가능. Awareness 축으로는 이 구분 불가.

**2. Catastrophe Theory 적용 가능:**
```
        Trust
         │   ╱╲  Fold Surface
         │  ╱  ╲
         │ ╱    ╲ ← Catastrophe point
         │╱      ╲
         │        ╲
         └──────────────── Reliability
                    ↑
            Critical threshold
```
R이 점진적으로 변할 때 T가 갑자기 붕괴하는 현상 — 시간 축 없이는 모델링 불가.

**3. 수렴/발산 패턴 분류:**
```
Pattern A: Convergent    Pattern B: Oscillating    Pattern C: Stagnant
(y=x로 수렴)            (진동하며 접근)            (변화 없음)

T│    ·····→            T│  ╱╲  ╱╲               T│ ──────────
 │  ╱     y=x           │ ╱  ╲╱  ╲──→            │
 │╱                      │╱        y=x            │        y=x
 └───── R                └───── R                  └───── R
```
Readiness 점수가 높으면 Pattern A로, 낮으면 Pattern C로 나타날 것이라는 **실증적 예측** 가능.

### 4.6 수정된 추천

| 순위 | 축 | 역할 | 근거 |
|------|---|------|------|
| **1순위** | **Time (τ)** | Matrix의 3D 확장 | Readiness와 독립적; 정적 한계 해결; 수학적 모델링 가능 |
| 2순위 | Expertise (E) | 조절변수로 활용 | MDL 연결; Matrix 외부에서 조절변수로 더 적합 |
| 보류 | Awareness (A) | TCRS에서 이미 담당 | Readiness(CA-Aw)와 겹침; 별도 축 불필요 |
| 보류 | Stakes (S) | 응용적 확장 | Process Model 연결 약함; 맥락 변수로 더 적합 |

### 4.7 결론: 분업이 핵심

Awareness를 3D Matrix에 넣는 것은 TCRS의 역할을 Matrix로 이중 배치하는 것이며, 이론적 깔끔함(parsimony)을 해칩니다. 대신:

- **Matrix (T × R × τ):** "어디에 있고, 어떻게 이동하는가?" (진단 + 동태)
- **TCRS (Readiness):** "왜 그렇게 이동하는가?" (메커니즘)

이 분업 구조가 Paper 3 (Conceptual Paper)의 핵심 기여가 될 수 있습니다:
> "We propose that the Trust-Reliability Matrix, extended with a temporal dimension, provides the diagnostic space within which trust calibration readiness — as measured by the TCRS — operates as the mechanism of movement."

---

## 5. 향후 작업

- [ ] T × R × τ 3D 시각화 생성 (Python matplotlib)
- [ ] Hysteresis 및 Catastrophe Theory 수학적 형식화
- [ ] 수렴/발산 패턴과 TCRS 점수의 관계 이론화
- [ ] Paper 3 원고에 통합

---

## 6. 관련 참고문헌

### Trust Dynamics & Time
- de Visser, E. J., et al. (2020). Towards a theory of longitudinal trust calibration in human-robot teams. *International Journal of Social Robotics*, 12, 459-478.
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50-80.
- Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors*, 57(3), 407-434.

### Catastrophe Theory
- Thom, R. (1975). *Structural Stability and Morphogenesis*. W.A. Benjamin.
- Guastello, S. J. (2002). *Managing Emergent Phenomena: Nonlinear Dynamics in Work Organizations*. Lawrence Erlbaum.

### Hysteresis in Trust
- Gao, J., & Lee, J. D. (2006). Extending the decision field theory to model operators' reliance on automation in supervisory control situations. *IEEE Transactions on Systems, Man, and Cybernetics*, 36(5), 943-959.

### Calibration Science
- Alexander, P. A. (2013). Calibration: What is it and why it matters? *Learning and Instruction*, 24, 1-3.
- Bastani, H., et al. (2025). Generative AI can harm learning. *PNAS*, 122(2).
