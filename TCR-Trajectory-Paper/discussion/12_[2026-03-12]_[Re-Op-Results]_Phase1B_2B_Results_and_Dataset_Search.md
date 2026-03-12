# Phase 1B/2B 재조작화 결과 및 대안 데이터셋 탐색

**Date:** 2026-03-12
**Context:** Phase 1B (P 분리), Phase 2B (GMM 재실행), GitHub/OSF 데이터셋 검색 완료
**Decision Status:** 결과 정리, 다음 단계 결정 필요

---

## 1. Phase 1B 결과: P_adaptive / P_non_adaptive 분리

### 1.1 핵심 발견

| 지표 | 값 | 의미 |
|------|-----|------|
| P_adaptive 평균 | **0.738** | AI 추천 문제 정답률 74% |
| P_non_adaptive 평균 | 0.554 | 비추천 문제 정답률 55% |
| AI_benefit 평균 | **+0.187** | AI 추천이 18.7%p 정답률 향상 |
| AI_benefit > 0 비율 | **78.6%** | 대부분 윈도우에서 AI 도움됨 |
| Over-reliance 윈도우 (Gap_new > 0) | **5.0%** | 원래 0%에서 변화 |

### 1.2 새 Calibration Gap 특성

| 비교 | Old gap (R_b − P) | New gap (R_b − P_adaptive) |
|------|---|---|
| 평균 | −0.443 | −0.560 |
| Within-student SD | 0.161 | **0.255** (+58%) |
| 범위 | [−0.73, −0.08] | **[−1.00, +0.78]** |

**→ 새 gap은 양방향 가능, 58% 더 많은 시간적 변동 포착**

### 1.3 패턴 후보

| 패턴 | 기준 | N (%) |
|------|------|------|
| Converging | cal_gap slope > +0.005 | 2,762 (61.1%) |
| Stagnant | \|slope\| ≤ 0.005 | 398 (8.8%) |
| Diverging | slope < −0.005 | 1,361 (30.1%) |
| Oscillating 후보 | cal_gap reversals ≥ 5 | 1,372 (30.3%) |
| Catastrophic 후보 | max_drop > 0.20 | 3,904 (86.4%) |

### 1.4 P_adaptive 비단조성

P_adaptive reversals 분포:
- 0-2회: 42.1% (단조적)
- 3-4회: 32.8% (약간 변동)
- **5+회: 24.9%** (비단조적, oscillation 가능)

### 1.5 주의점

- 윈도우당 adaptive 문제 수 적음 (평균 4-10개) → P_adaptive 분산 일부는 측정 잡음
- Missing data: 23.8% 윈도우에 adaptive 문제 없음 → P_adaptive 결측
- Catastrophic 후보 86.4%는 과대 추정 (낮은 임계값 + 소표본 잡음)

---

## 2. Phase 2B 결과: GMM 재실행 (3 전략)

### 2.1 전략 비교

| 전략 | 입력 | 모형 | G | Avg Posterior | ARI vs Original |
|------|------|------|---|---|---|
| S1: R_b + P_adaptive wide | 20 features | VEV | 7 | **0.955** | 0.095 |
| S2: Trajectory features | 20 features (scaled) | VVV | 8 | **0.964** | 0.129 |
| S3: R_b + P_ad + AI_ben wide | 30 features | VEE | 8 | 0.872 | 0.243 |

**ARI가 모두 낮음** → 새 조작화가 근본적으로 다른 분류를 생성 (예상대로)

### 2.2 Strategy 2 (Trajectory Features) — 가장 유망

8개 클래스 중 이론적으로 의미 있는 패턴:

#### Class 4 (N=256, 5.7%): "AI Benefit Emergence" ★ 새 발견

| Window | P_adaptive | AI_benefit | Gap_new |
|:---:|:---:|:---:|:---:|
| 1 | **0.275** | **−0.311** | −0.039 |
| 5 | 0.643 | +0.166 | −0.378 |
| 10 | **0.852** | **+0.354** | −0.601 |

- 처음 AI가 해로움 → 시간이 지나며 AI가 매우 효과적으로 변함
- 학생의 R_b가 이를 따라잡지 못함 → **Gap 확대** (divergent)
- 이론에 없는 새 패턴: "AI 효과 변화에 대한 적응 실패"

#### Class 7 (N=270, 6.0%): "Oscillating Convergent" ★ 이론 대응 개선

| Window | R_b | P_adaptive | Gap_new |
|:---:|:---:|:---:|:---:|
| 1 | 0.067 | 0.703 | −0.367 |
| 5 | 0.176 | 0.674 | −0.356 |
| 8 | 0.236 | 0.657 | −0.267 |
| 10 | 0.252 | 0.567 | **−0.181** |

- Gap −0.367 → −0.181 **수렴** + **4 reversals** (비단조적)
- 이론의 convergent + oscillating 특성 동시 보유

### 2.3 이론 대응도 비교

| 이론 패턴 | 원래 6-class | Strategy 2 (8-class) | 변화 |
|---|---|---|---|
| **Convergent** | Class 2,3 (부분적) | Class 7 (Gap→−0.18, 4 reversals) | ★ 개선 |
| **Oscillating** | ❌ 없음 | Class 7 (4 rev), Class 1 (4 rev) | ★ 신규 |
| **Stagnant** | Class 4 (강함) | 명확한 대응 없음 | 약화 |
| **Catastrophic** | ❌ 없음 | ❌ 여전히 없음 | 불변 |
| **새 발견** | — | Class 4: AI Benefit Emergence | ★ 이론 확장 |

---

## 3. GitHub/OSF 데이터셋 검색 결과

### 3.1 Tier 1: 즉시 다운로드 가능 + 이론 검증 적합

| # | 데이터셋 | N | 시행/인 | AI 신뢰성 변동 | 수용/거부 | URL |
|---|---------|---|---------|:---:|:---:|-----|
| 1 | **Chess Puzzle (Bondi 2023)** | 100 | 30 | ✅ 80%→20% 전환 | ✅ | [Mendeley](https://data.mendeley.com/datasets/ng33vg479n/1) |
| 2 | **Pothole Inspection (Okamura 2020)** | 116 | 다수 | ✅ 변동 | ✅ rely/manual | [figshare](https://doi.org/10.6084/m9.figshare.11538792.v1) |
| 3 | **ImageNet-16H (Steyvers 2022)** | 145 | ~200 | ✅ 난이도별 | 암묵적 | [OSF](https://osf.io/2ntrf/) |
| 4 | **HAIID (Vodrahalli 2022)** | 1,100+ | 8-16 | ✅ | ✅ | [GitHub](https://github.com/kailas-v/human-ai-interactions) |
| 5 | **Complementary Perf (Bansal 2021)** | ~500 | 50 | 고정 84% | ✅ | [GitHub](https://github.com/uw-hai/Complementary-Performance) |
| 6 | **Human-Alignment Study** | 703 | 24 | ✅ 조건별 | ✅ | [GitHub](https://github.com/Networks-Learning/human-alignment-study) |
| 7 | **Trustworthy-ML (Ming Yin lab)** | 다수 | 다수 | ✅ | ✅ | [GitHub](https://github.com/ZhuoranLu/Trustworthy-ML) |
| 8 | **BiasedHumanAI (UCL)** | 1,401 | 다수 | ✅ biased/noisy AI | ✅ | [GitHub](https://github.com/affective-brain-lab/BiasedHumanAI) |

### 3.2 Tier 1+: 요청 필요하지만 이론적 최적 매치

| # | 데이터셋 | N | 시행/인 | 특징 | 상태 |
|---|---------|---|---------|------|------|
| 1 | **Chung & Yang 2024 (Michigan)** | 130 | **100** | 3가지 trust dynamics 유형 식별 (Bayesian, disbelievers, oscillators) | 저자 연락 필요 |
| 2 | **Yang et al. 2023 (Human Factors)** | 75 | 40 | Trial-by-trial trust dynamics | 저자 연락 필요 |

### 3.3 평가: 이론 검증에 가장 적합한 데이터셋

**1순위: Chess Puzzle (Bondi 2023)**
- ✅ 즉시 다운로드 가능 (Mendeley)
- ✅ AI reliability 80%→20% 전환 → **trust violation event 존재!**
- ✅ 시행별 수용/거부 + 자신감 평정
- ⚠️ N=100, 30 시행 (50 기준 미달, 그러나 신뢰성 전환이 핵심)
- → **Oscillating + Catastrophic 패턴이 나올 가능성 가장 높음**

**2순위: ImageNet-16H (Steyvers 2022)**
- ✅ 즉시 다운로드 가능 (OSF)
- ✅ ~200 시행/인 (GMM에 충분)
- ✅ 난이도별 AI 정확도 변동
- ⚠️ 명시적 수용/거부 아닌 독립 분류
- → **대규모 반복측정 가능, agreement/disagreement로 reliance 추론**

**3순위: Chung & Yang 2024**
- ✅ 130명 × 100 시행
- ✅ **연구자가 이미 3가지 trust trajectory 유형 식별** (우리 이론과 직접 대응!)
- ⚠️ 저자 연락 필요
- → **이론적 최적 매치. 연락 가치 있음.**

---

## 4. 종합 평가 및 권장 경로

### 현재 상황

| 달성 | 미달성 |
|------|--------|
| ✅ EdNet 재조작화로 구성 타당도 개선 | ❌ Catastrophic 패턴 (trust violation 부재) |
| ✅ Oscillating 유사 패턴 탐지 (S2 Class 7) | ❌ Over-reliance 명확한 클래스 |
| ✅ 새 패턴 발견 (AI Benefit Emergence) | ❌ 4패턴 모두 에 대한 실증 |
| ✅ 대안 데이터셋 다수 식별 | |

### 권장 경로

**Path A: EdNet 재조작화 논문 (현실적, 2-3주)**
- 원래 분석 + 재조작화 분석을 모두 보고
- "구성 타당도 민감도 분석"으로 프레이밍
- 장점: 데이터 이미 확보, 분석 완료
- 한계: H2b(oscillating) 부분 지지, catastrophic 미지지

**Path B: Chess Puzzle 파이프라인 적용 (1주 추가)**
- Bondi 2023 데이터 다운로드 → 동일 GMM 파이프라인
- AI reliability 전환 (80%→20%)이 있으므로 oscillating + catastrophic 가능
- N=100 × 30 시행 = 소규모이지만 구성 타당도 높음
- EdNet(대규모 관찰) + Chess(소규모 실험) = **dual-evidence 논문**

**Path C: Chung & Yang 데이터 확보 시도 (불확실)**
- University of Michigan 연락
- 성공 시 최강 논문, 실패 시 시간 낭비

---

## 5. AI Benefit Emergence: 제5의 궤적 패턴에 대한 이론적 해석

### 5.1 패턴 정의

**AI Benefit Emergence** (또는 **Divergent Under-Adaptation**)는 기존 4패턴(Convergent, Oscillating, Stagnant, Catastrophic)에 포함되지 않는 새로운 제5의 궤적 유형이다.

| 특성 | 설명 |
|------|------|
| **정의** | AI의 효과가 시간에 따라 증가하지만, 학습자의 의존도(reliance)가 이를 따라잡지 못하여 Gap이 점진적으로 확대되는 패턴 |
| **수학적 표현** | R(t) ↑↑ while T(t) ↑ → |T(t) − R(t)| → ∞ (divergent) |
| **방향** | Under-reliance 방향으로의 발산 (T < R, gap 확대) |
| **시간 역학** | 점진적 (gradual), 비돌발적 — Catastrophic과 대조적 |
| **EdNet 실증** | Strategy 2 Class 4 (N=256, 5.7%): P_adaptive 0.275→0.852, R_b 0.020→0.171, Gap −0.039→−0.601 |

### 5.2 기존 4패턴과의 차별점

| 비교 | AI Benefit Emergence | 유사 패턴 | 핵심 차이 |
|------|---------------------|-----------|----------|
| vs **Convergent** | Gap 확대 (divergent) | Gap 축소 (convergent) | 방향 반대 |
| vs **Stagnant** | AI 효과 & 의존 모두 변화 중 | 변화 없음 | 동적 vs 정적 |
| vs **Catastrophic** | 점진적 발산 | 돌발적 단절 | tempo의 차이 |
| vs **Oscillating** | 단방향 발산 | 양방향 진동 | 비정렬의 방향성 |

**핵심 구분:** Catastrophic은 외부 사건(trust violation)에 의한 **급격한** gap 변화인 반면, AI Benefit Emergence는 내적 적응 실패에 의한 **점진적** gap 확대이다.

### 5.3 이론적 메커니즘

#### 메커니즘 1: Parasuraman & Riley (1997)의 "Disuse"

Parasuraman & Riley는 자동화에 대한 부적절한 사용을 세 가지로 분류했다:
- **Misuse**: 자동화를 과도하게 신뢰 (over-reliance)
- **Disuse**: 신뢰할 수 있는 자동화를 사용하지 않음 (under-reliance)
- **Abuse**: 자동화의 부적절한 적용

AI Benefit Emergence는 **disuse의 동적 형태**에 해당한다. 학습자가 처음에 AI가 도움이 되지 않는다고 학습한 후(초기 P_adaptive 낮음), AI의 효과가 개선되어도 기존 신념(AI는 도움이 안 됨)이 행동 변화를 억제한다.

#### 메커니즘 2: Lee & Moray (1992)의 Trust-Reliability 비대칭

Lee & Moray의 실험은 신뢰의 비대칭적 역학을 발견했다:
- 신뢰 **감소**: 신뢰성 저하에 빠르게 반응 (fast negative update)
- 신뢰 **회복**: 신뢰성 향상에 느리게 반응 (slow positive update)

이 비대칭성이 AI Benefit Emergence의 핵심 메커니즘이다. AI의 효과적 추천이 축적되더라도, 한번 형성된 낮은 신뢰는 천천히만 회복되므로, 의존도(T)와 AI 효과(R)의 격차가 벌어진다.

#### 메커니즘 3: Anchoring & Insufficient Adjustment (Tversky & Kahneman, 1974)

학습자의 초기 AI 평가(낮은 효과)가 **앵커(anchor)**로 작용하여, 이후 긍정적 증거에도 불구하고 불충분한 조정(insufficient adjustment)만 일어난다. R_b가 0.020→0.171로 증가하긴 하지만, P_adaptive 0.275→0.852의 극적 변화에 비하면 현저히 부족하다.

### 5.4 T × R × τ 3차원 모델에서의 위치

```
기존 4패턴:
  Convergent:   T와 R이 τ축을 따라 수렴 → 3D 궤적이 대각선(T=R)에 접근
  Oscillating:  T가 R 주위를 감쇠진동 → 나선형 궤적
  Stagnant:     T와 R 모두 정지 → 점에 머무름
  Catastrophic: T가 급격히 이탈 → 궤적에 불연속점

새 패턴:
  AI Benefit Emergence: R이 빠르게 상승하는데 T는 천천히 따라감
    → 3D 궤적이 R축 방향으로 기울어진 발산 곡선
    → T=R 대각선에서 점점 멀어짐 (R >> T)
    → 2D Gap 그래프에서: |T-R|이 0에서 시작하여 점진적으로 증가
```

### 5.5 실무적 함의

| 함의 | 설명 |
|------|------|
| **학습 시스템 설계** | AI 추천 품질이 향상될 때, 학습자에게 이를 명시적으로 알려야 함 |
| **개입 시점** | Gap이 확대되기 시작하는 윈도우에서 "AI 추천 정확도가 X% 향상되었습니다" 피드백 제공 |
| **Scaffolding** | 메타인지적 촉진: "최근 AI 추천 문제에서의 정답률을 확인해 보세요" |
| **이론적 기여** | 기존 Trust Calibration 문헌이 over-reliance(misuse)에 편향된 반면, under-reliance(disuse)의 동적 궤적에 대한 설명 제공 |

### 5.6 Chess Puzzle 데이터와의 연결

Bondi et al. (2023) Chess Puzzle 데이터의 **Condition 2 (Low→High reliability)**는 AI Benefit Emergence의 실험적 유사체이다:
- Pre-switch: AI 부정확 (20%) → 학습자 낮은 의존 형성
- Post-switch: AI 정확 (80%) → 그러나 의존은 천천히 회복

예비 분석 결과:
- Post-switch에서 정확한 AI를 무시한 비율: **37.2%** (under-reliance events)
- 이 중 오답으로 이어진 비율: **80.6%** (missed opportunity cost)
- Under-reliance post-switch 해당 세션: 18/50 (36%)

→ 이는 AI Benefit Emergence가 **실험 데이터에서도 확인됨**을 시사하며, EdNet(관찰) + Chess Puzzle(실험) 양방향 증거를 구성한다.

---

## 6. 의사결정 기록

| 날짜 | 결정 |
|------|------|
| 2026-03-12 | Phase 1B 완료: P_adaptive/P_non_adaptive/AI_benefit 계산 |
| 2026-03-12 | Phase 2B 완료: 3 전략 GMM → Strategy 2 (8-class) 가장 유망 |
| 2026-03-12 | GitHub/OSF 검색 완료: Chess Puzzle (Bondi 2023) 1순위 |
| 2026-03-12 | 이론 대응도: oscillating 신규 탐지, catastrophic 여전히 부재 |
| 2026-03-12 | 다음 단계 결정 필요: Path A (EdNet only) vs Path B (dual-evidence) |
| 2026-03-12 | AI Benefit Emergence 이론적 해석 추가: Parasuraman & Riley disuse, Lee & Moray 비대칭, Anchoring |
| 2026-03-12 | Chess Puzzle 예비 분석 완료: C1 over-reliance 39%, C2 under-reliance 37.2%, 양조건 모두 catastrophic jump |
| 2026-03-12 | 제5의 궤적 패턴 "AI Benefit Emergence"를 이론 프레임워크에 공식 추가 |
