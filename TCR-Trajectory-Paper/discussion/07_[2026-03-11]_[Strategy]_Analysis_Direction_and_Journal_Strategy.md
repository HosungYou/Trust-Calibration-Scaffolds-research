# 분석 방향 및 저널 전략

**Date:** 2026-03-11
**Context:** EdNet KT3 데이터 확보 후 연구 방향 설계

---

## 핵심 전략 질문: Paper 3의 성격 재정의

### 현재 상태

Paper 3은 원래 **순수 개념 논문**으로 설계됨:
- "Trust Calibration Readiness as an Educational Competency"
- 타겟: Educational Psychologist (개념 논문 환영)
- IRB 불필요

그러나 T × R × τ 3D 확장과 EdNet KT3 데이터 확보로, **실증적 검증 가능성**이 열림.

### 3가지 옵션

#### Option A: Paper 3 = 개념 논문 (유지) + Paper 4 = 실증 논문 (신설)

| | Paper 3 | Paper 4 (NEW) |
|---|---------|---------------|
| **성격** | 순수 개념/이론 | 실증 (secondary data analysis) |
| **핵심 기여** | TCR을 교육적 역량으로 정립 | T × R × τ 궤적 유형 실증 검증 |
| **데이터** | 없음 | EdNet KT3 + Tier 1 실험 데이터 |
| **저널** | Educational Psychologist | 아래 참조 |
| **Alexander 협업** | ✅ 적합 | ❌ 부적합 |
| **IRB** | 불필요 | 불필요 (공개 데이터) |

**장점:** 각 논문의 기여가 명확. EP에 개념 논문 적합도 유지. 실증 분석이 별도 논문으로 독립적 가치.
**단점:** 연구 프로그램이 3편 → 4편으로 확장. 작업량 증가.

#### Option B: Paper 3 = 개념 + 실증 예시 (Empirical Illustration)

- 개념 논문 구조 유지하되, Section 7에 "Empirical Illustration" 추가
- EdNet KT3 일부 분석 결과를 개념 모델의 예시로 포함
- 형식: "To illustrate the theoretical predictions, we examined..."

**장점:** 한 편으로 완결. 개념이 공허하지 않음을 보여줌.
**단점:** Educational Psychologist가 실증 section을 원하지 않을 수 있음. 분석의 깊이가 제한됨.

#### Option C: Paper 3 자체를 실증 논문으로 전환

- "Trust Calibration Trajectories in AI Tutoring: A Secondary Analysis of EdNet"
- 개념 프레임워크(T × R × τ) + 실증 검증을 하나로

**장점:** 실증 증거가 강력. 데이터 기반 저널에 적합.
**단점:** 원래 Paper 3의 교육적 역량 논의가 약화. Alexander 협업 근거 소실. 연구 프로그램 3편 구조 붕괴.

### 추천: Option A (Paper 3 유지 + Paper 4 신설)

**이유:**
1. Paper 3의 핵심 기여(TCR = 교육적 역량)는 개념적 논증이 필요한 것이지, 데이터가 아님
2. EdNet KT3 분석은 그 자체로 충분한 실증 기여 (N=86,700+, 궤적 유형 분류)
3. 4편 구조가 연구 프로그램을 더 강화함:

```
Paper 1 (SLR): "무엇이 문제인가?" → Calibration Gap 발견
Paper 2 (Scale): "어떻게 측정하는가?" → TCRS 척도 개발
Paper 3 (Conceptual): "왜 중요한가?" → TCR = 교육적 역량
Paper 4 (Empirical): "실제로 그런가?" → 궤적 유형 실증 검증
```

---

## Paper 4: 데이터 분석 방향

### 제목 (Working Title)

**"Trust Calibration Trajectories in AI-Assisted Learning: Evidence from 86,000+ Learners"**

또는

**"How Learners Calibrate Trust in AI: A Growth Mixture Analysis of Behavioral Trajectories"**

### 연구 질문

| RQ | 질문 | 분석 방법 |
|----|------|---------|
| **RQ1** | AI 튜터링에서 학습자의 신뢰/의존도 궤적은 몇 가지 유형으로 분류되는가? | Growth Mixture Modeling (GMM) / LCGA |
| **RQ2** | 이론적으로 예측된 3가지 패턴(convergent, oscillating, stagnant)이 실증적으로 관찰되는가? | GMM 결과 vs 이론적 예측 비교 |
| **RQ3** | 궤적 유형을 예측하는 학습 행동 요인은 무엇인가? | Multinomial logistic regression |
| **RQ4** | 신뢰 교정이 학습 성과(정확도 향상)와 연관되는가? | 궤적 유형별 학습 성과 비교 |

### 분석 전략 (3단계)

#### Phase 1: 변수 생성 (Trust Proxy Construction)

EdNet KT3 raw log → 학습자별 시계열 변수:

| 변수 | 조작적 정의 | T/R/τ 매핑 |
|------|-----------|-----------|
| **AI_reliance** | `adaptive_offer` 추천 수용률 (rolling window 20 episodes) | **T** (Trust/Reliance) |
| **explanation_depth** | 해설(e{int}) 체류 시간 / 해당 문제 응답 시간 비율 | **T** (깊은 처리 = 적극적 calibration) |
| **system_accuracy** | 학습자의 최근 20문제 정답률 (AI 추천 문제 vs 자기 선택) | **R** (System Reliability proxy) |
| **answer_switching** | 동일 문제 내 respond 반복 횟수 | 불확실성/저신뢰 지표 |
| **lecture_seeking** | 자발적 강의 시청 빈도 | 적극적 학습 행동 |
| **episode_index** | 문제풀이 에피소드 순번 | **τ** (Time) |

**핵심 변수: Calibration Gap**
```
Calibration_Gap = |AI_reliance - System_accuracy|
```
- Gap이 작을수록 = 잘 교정된 신뢰 (calibrated)
- Gap이 클수록 = 과신뢰(overtrust) 또는 과불신(undertrust)

#### Phase 2: 궤적 분류 (Growth Mixture Modeling)

1. **대상 선별:** 50+ 에피소드 학생 (~86,700명) → 100+ 에피소드 (~68,100명) 권장
2. **시간 정규화:** 학습자마다 에피소드 수가 다르므로, 10분위(decile) 또는 20분위(ventile)로 정규화
3. **모델 비교:**
   - 1-class ~ 6-class GMM 비교
   - BIC, AIC, Entropy, BLRT로 최적 클래스 수 결정
4. **이론적 예측 대조:**

| 예측 궤적 | 행동 패턴 예상 | Guo & Yang (2021) 대응 |
|-----------|-------------|---------------------|
| **Convergent** | Calibration gap이 시간에 따라 감소 → 0에 수렴 | "Bayesian decision maker" |
| **Oscillating** | Calibration gap이 감쇠 진동 (damped oscillation) | "Oscillator" |
| **Stagnant** | Calibration gap이 일정 수준 유지 또는 증가 | "Disbeliever" |

#### Phase 3: 예측 및 성과 분석

1. **궤적 유형 예측 모델:**
   - 초기 학습 행동 (첫 10 에피소드) → 궤적 유형 예측
   - 변수: 초기 정확도, 초기 해설 열람률, 플랫폼 (mobile/web), part 선호도

2. **학습 성과 비교:**
   - 궤적 유형별 최종 정확도 비교
   - Convergent > Oscillating > Stagnant 순서 예측

3. **강건성 검증:**
   - 다른 Trust proxy 조합으로 재분석
   - 다른 시간 윈도우 크기로 민감도 분석
   - Tier 1 실험 데이터 (Rittenberg, Zouhar)에서 동일 패턴 재현

### 보조 분석: Tier 1 실험 데이터 교차 검증

| 데이터셋 | 역할 | N | Trust 측정 |
|---------|------|---|----------|
| **Rittenberg et al. (2024)** | Gold standard 검증 | 147 | VAS 0-100, 30 시점 |
| **Zouhar et al. (2023)** | 다른 맥락 재현 | 332 | Betting behavior, 56 trials |
| **Lu & Yin (2021)** | Self-report + behavioral | ~300 | 7-point trust + switching |

EdNet에서 발견한 궤적 유형이 통제 실험에서도 재현된다면, 모델의 일반화 가능성 확보.

---

## 타겟 저널 전략

### Paper 3 (개념 논문) — 유지

| 순위 | 저널 | IF | 적합도 | 이유 |
|------|------|-----|--------|------|
| 1 | **Educational Psychologist** | ~10.1 | ★★★★★ | 개념 논문 환영, calibration 담론 중심지, Alexander 편집위원 |
| 2 | **Learning and Instruction** | ~6.2 | ★★★★☆ | Alexander 2013 special issue 게재지 |
| 3 | **Review of Educational Research** | ~11.2 | ★★★★☆ | 체계적 논증 환영, 높은 영향력 |

### Paper 4 (실증 논문) — 신규

| 순위 | 저널 | IF | 적합도 | 이유 |
|------|------|-----|--------|------|
| 1 | **Computers & Education** | ~12.0 | ★★★★★ | AI + 교육 + 대규모 실증, 최고 영향력 |
| 2 | **British Journal of Ed Tech (BJET)** | ~6.7 | ★★★★☆ | EdTech 실증 환영, 합리적 리뷰 기간 |
| 3 | **IJAIED** | ~4.7 | ★★★★★ | AI in Education 전문, EdNet 데이터 사용 연구 게재 이력 |
| 4 | **Learning and Instruction** | ~6.2 | ★★★★☆ | 학습 과정 궤적 분석 적합 |
| 5 | **Human Factors** | ~3.3 | ★★★☆☆ | Trust dynamics 전통, 교육 맥락 제한적 |

### 저널별 논문 프레이밍

**Computers & Education 프레이밍:**
- "AI 튜터링에서 학습자의 신뢰 교정 궤적 유형 — 86,000명 종단 행동 데이터 분석"
- 강조: 대규모 secondary data, 학습 설계 시사점, 적응형 AI 설계 제안

**IJAIED 프레이밍:**
- "Growth Mixture Modeling of Trust Calibration in an AI Tutoring System"
- 강조: AI tutoring context, Knowledge Tracing 커뮤니티와의 연결, EdNet 기반

**BJET 프레이밍:**
- "Beyond Binary Trust: Identifying Learner Trust Calibration Patterns in AI-Assisted Learning"
- 강조: 교육 실천 시사점, AI literacy 연결, 교수자용 진단 프레임워크

---

## 디렉토리 구조 확정

```
TCR-Competency-Paper/
├── README.md
├── discussion/                     # 연구 논의 기록 (한글)
│   ├── 01-07_*.md
├── figures/                        # 출판용 시각화
│   ├── Figure_1-5_*.png
│   └── generate_3d_figures.py
├── manuscript/                     # 원고 (to be created)
├── references/                     # 참고문헌
├── data/                           # 데이터
│   ├── ednet-kt3/
│   │   ├── raw/KT3/               # → symlink to _Data/EdNet (297,915 CSV, 4.2GB)
│   │   ├── metadata/              # questions.csv, lectures.csv
│   │   └── processed/             # 전처리된 분석용 데이터
│   ├── pew-atp/                   # Pew ATP (다운로드 시)
│   │   ├── raw/
│   │   └── processed/
│   └── tier1-experiments/         # Rittenberg, Zouhar 등
├── analysis/
│   ├── scripts/                   # Python/R 분석 스크립트
│   ├── notebooks/                 # Jupyter notebooks
│   └── outputs/                   # 분석 결과물
```

---

## 타임라인 제안

| 단계 | 작업 | 예상 기간 |
|------|------|---------|
| **1** | EdNet KT3 전처리 스크립트 작성 (Trust proxy 생성) | 1주 |
| **2** | 86,700명 대상 Trust proxy 시계열 생성 | 1주 (계산 시간 포함) |
| **3** | GMM/LCGA 분석 (R: tidyLPA/mclust) | 2주 |
| **4** | Tier 1 데이터 교차 검증 | 1주 |
| **5** | 시각화 및 결과 해석 | 1주 |
| **6** | Paper 4 초고 작성 | 3-4주 |
| **7** | Paper 3 개념 논문 (병행 가능) | 별도 진행 |

---

## 미결정 사항 (선생님의 판단 필요)

1. **Paper 3/4 분리 vs 통합** — Option A/B/C 중 선택
2. **Paper 4 타겟 저널** — C&E vs IJAIED vs BJET
3. **EdNet KT3 분석 범위** — 전체 86,700명 vs 표본 추출 (계산 비용)
4. **보조 데이터** — Pew ATP, Tier 1 실험 데이터 포함 여부
5. **분석 도구** — Python (scikit-learn) vs R (tidyLPA/mclust/lcmm) vs Mplus
6. **Alexander 교수 협업** — Paper 3에만? Paper 4에도?
