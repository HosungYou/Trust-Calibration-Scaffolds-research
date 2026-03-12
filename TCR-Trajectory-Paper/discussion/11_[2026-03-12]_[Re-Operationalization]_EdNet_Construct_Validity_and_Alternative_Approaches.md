# EdNet 재조작화 전략: 구성 타당도 개선 및 대안적 접근

**Date:** 2026-03-12
**Context:** Phase 0-4 완료 후, 이론-실증 괴리 분석 및 대안 탐색
**Decision Status:** 접근 A 실행 확정

---

## 1. 문제 진단: 왜 이론적 4패턴이 EdNet에서 나타나지 않았는가

### 1.1 이론적 예측 (Figure 2: T×R×τ 3D Trajectories)

| 패턴 | 설명 | 발생 조건 |
|------|------|----------|
| **Convergent** | \|Trust - Reliability\| → 0 (수렴) | 학습자가 AI 신뢰성을 학습, 의존도 조정 |
| **Oscillating** | 감쇠진동 | AI reliability 변동 → trust violation → repair 사이클 |
| **Stagnant** | Gap 불변 | 학습/조정 없음 |
| **Catastrophic** | Gap 급격 확대 | Trust violation event (AI 급격한 실패) |

### 1.2 실증 결과 (6-class GMM)

| Class | N (%) | R_b 변화 | P 수준 | 특징 |
|:---:|------:|:---:|:---:|------|
| 1 | 1,367 (29.9%) | 0.05→0.14 | ~0.59 안정 | Gradual Adopter — 단조 증가 |
| 2 | 1,582 (34.6%) | 0.03→0.17 | 0.53→0.56 | Steady Calibrator — 단조 증가 |
| 3 | 859 (18.8%) | 0.04→0.19 | 0.50→0.54 | Strong Calibrator — 단조 증가 |
| 4 | 451 (9.9%) | 0.06→0.11 | ~0.65 안정 | High Performer — 증가 후 감소 |
| 5 | 240 (5.3%) | 0.09→0.23 | ~0.57 안정 | Heavy Adopter — 증가 후 감소 |
| 6 | 69 (1.5%) | 0.33→0.29 | ~0.59 | Early Heavy User — 전반 감소 |

**핵심 관찰:**
- 6개 중 4개(Class 1-3, 5)가 R_b 단조 증가 (AI feature adoption)
- Gap = R_b - P가 **항상 음수** (−0.28 ~ −0.54)
- 이론이 예측한 oscillating, catastrophic 패턴 **부재**
- Over-reliance (R_b > P) 사례 **없음**

### 1.3 구조적 원인 (3가지)

#### 원인 1: R_b의 구성 타당도 문제

```
이론의 "Trust/Reliance":  "AI 조언을 수용할 것인가 거부할 것인가" (의사결정)
EdNet의 R_b:              "전체 에피소드 중 adaptive_offer 비율" (활동 비율)
```

R_b는 reliance **decision**이 아닌 feature **adoption**을 측정.
학생이 AI 추천을 "수용/거부"하는 것이 아니라, AI 추천 콘텐츠를 얼마나 경험하는지의 비율.
이는 플랫폼 사용 패턴에 가까우며, 시간이 지나면서 자연스럽게 증가하는 경향.

#### 원인 2: AI Reliability 불변 (관찰 데이터의 한계)

```
이론: AI reliability가 변할 때 → trust violation → oscillation/catastrophic
EdNet: AI 알고리즘 일정 → trust violation event 자체가 없음
```

EdNet은 관찰 데이터로, AI의 추천 품질이 실험적으로 조작되지 않음.
AI가 "실패"하는 국면이 없으므로, 학습자의 신뢰가 무너지는 상황이 구조적으로 발생하지 않음.

#### 원인 3: R_b와 P의 비공약성 (Incommensurability)

```
R_b: adaptive_offer 에피소드의 비율 [0, ~0.35]
P:   모든 문제의 정답률 [0.50, 0.65]
Gap = R_b - P: 항상 음수 (측정의 인공물, 실제 under-reliance가 아님)
```

두 변수가 서로 다른 것을 측정하고 있으므로, 그 차이(Gap)가 "calibration"을 반영한다고 보기 어려움.

---

## 2. 재조작화 대안 3가지

### 2.1 접근 A: P 분리 (P_adaptive / P_non_adaptive) — ★ 최우선 실행

**핵심 아이디어:** P를 adaptive/non-adaptive 문제별로 분리하여 "AI 추천의 효과"를 직접 측정

```
현재:   P = (모든 문제 정답) / (모든 문제)

개선:   P_adaptive     = (adaptive 문제 정답) / (adaptive 문제)
        P_non_adaptive = (non-adaptive 문제 정답) / (non-adaptive 문제)
        AI_benefit     = P_adaptive - P_non_adaptive
```

**이론적 근거:**
- `P_adaptive` ≈ AI 추천의 효과 (AI reliability proxy)
  - AI가 학생 수준에 맞는 문제를 추천 → P_adaptive 높음 → AI reliable
  - AI가 부적절한 문제 추천 → P_adaptive 낮음 → AI unreliable
- `AI_benefit` > 0 → AI 추천이 도움됨 → 의존 정당화
- `AI_benefit` < 0 → AI 추천이 오히려 해로움 → 의존 철회해야 함
- **핵심:** P_adaptive는 윈도우마다 비단조적으로 변동할 가능성 높음 (문제 난이도 변화)

**기대 효과:**
- R_b와 P_adaptive가 같은 공간(adaptive 콘텐츠)에서 측정 → 공약성 문제 해소
- AI_benefit 변수로 "AI가 도움이 되는가?" 직접 답변 → Figure 1 매트릭스 대응
- P_adaptive 변동이 R_b 변동과 비정렬 → oscillation 유사 패턴 가능성

**구현 계획:**
1. Phase 1 스크립트 수정: P_adaptive, P_non_adaptive, AI_benefit 추가 계산
2. 탐색적 분석: 새 변수의 분포, 윈도우 간 변동성, 비단조성 확인
3. 유망한 경우: R_b + P_adaptive + AI_benefit 기반 GMM 재실행
4. 결과 비교: 원래 6-class vs 새 분류의 이론 대응도

### 2.2 접근 B: Explanation-Conditional Reliance Quality

```
R_b_with_expl  = (adaptive 에피소드 중 해설 열람) / (adaptive 에피소드 총수)
R_b_blind      = (adaptive 에피소드 중 해설 미열람) / (adaptive 에피소드 총수)
Reliance_quality = R_b_with_expl / R_b_total
```

"Thoughtful reliance" (해설 읽고 AI 따름) vs "Blind acceptance" (그냥 따름) 구분.
이미 Phase 1에서 `expl_rate` 계산 중이므로 adaptive 에피소드에 한정하여 교차 분석 가능.

### 2.3 접근 C: Within-Student Variability 기반 분류

```
R_b_slope      = R_b의 선형 기울기 (증가/감소/정체)
R_b_variability = R_b의 SD (oscillation 정도)
R_b_reversals  = R_b 방향 전환 횟수 (비단조성 지표)
max_drop       = 연속 윈도우 간 최대 감소폭 (catastrophic 후보)
```

이 특성들로 분류하면:
- high variability + many reversals = oscillating 후보
- large max_drop = catastrophic 후보
- low variability + positive slope = convergent
- low variability + flat = stagnant

---

## 3. 재조작화로 가능한 것 vs 구조적 불가능

### 가능한 것 (EdNet 내에서)

| 항목 | 실현 가능성 | 근거 |
|------|:---:|------|
| 구성 타당도 개선 (R_b ↔ P_adaptive 공약성) | ✅ 높음 | 같은 공간에서 측정 |
| AI_benefit 변수로 "AI 효과" 직접 측정 | ✅ 높음 | P_adaptive - P_non_adaptive |
| Convergent 패턴 식별 | ✅ 가능 | R_b와 P_adaptive 수렴 |
| Stagnant 패턴 식별 | ✅ 가능 | 이미 Class 4에서 관찰 |
| Quasi-oscillation 탐지 | ⚠️ 제한적 | P_adaptive 변동 정도에 의존 |

### 구조적으로 불가능한 것

| 항목 | 불가능 이유 |
|------|----------|
| **진짜 Oscillating** (감쇠진동) | AI reliability 실험 조작 부재 → trust violation-repair 사이클 없음 |
| **Catastrophic pattern** | Trust violation event 자체가 EdNet에 존재하지 않음 |
| **Over-reliance** | adaptive_offer 비율이 구조적으로 낮음 (max ~0.35) |

**결론:** Oscillating과 catastrophic 패턴은 **AI reliability를 실험적으로 조작하는 데이터**에서만 나타날 수 있음. 이는 EdNet의 한계가 아닌, 관찰 데이터 vs 실험 데이터의 근본적 차이.

---

## 4. 추천 전략: Dual-Path Approach

### Path 1: EdNet 재조작화 (접근 A) — 즉시 실행

1. Phase 1 수정: P_adaptive / P_non_adaptive / AI_benefit 계산
2. 탐색적 분석: 새 변수 분포 확인
3. 유망 시 GMM 재실행
4. 논문 서사: "AI feature adoption → AI reliance calibration" 전환

### Path 2: 실험 데이터 발굴 — 병행 탐색

- GitHub/OSF에서 AI 조언 수용/거부 실험 데이터 검색 중
- 발굴 시: 동일 GMM 파이프라인 적용 → dual-evidence
- EdNet(대규모 관찰) + 실험(소규모 but 높은 구성 타당도) = 최강 논문

---

## 5. 의사결정 기록

| 날짜 | 결정 |
|------|------|
| 2026-03-12 | 이론-실증 괴리의 구조적 원인 3가지 식별 |
| 2026-03-12 | 재조작화 대안 3가지 도출 (A: P 분리, B: 해설 조건부, C: 변동성 기반) |
| 2026-03-12 | **접근 A (P_adaptive/P_non_adaptive 분리) 우선 실행 확정** |
| 2026-03-12 | 실험 데이터 병행 탐색 시작 |
