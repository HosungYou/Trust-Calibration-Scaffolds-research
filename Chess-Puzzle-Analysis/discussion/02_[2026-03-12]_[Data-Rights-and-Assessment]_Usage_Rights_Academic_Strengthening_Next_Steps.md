# 데이터 사용 권한, 학술적 강화 가능성 평가, 이후 절차

**Date:** 2026-03-12
**Context:** Chess Puzzle 분석 완료 후, 논문 활용 전 법적/윤리적/학술적 평가
**Decision Status:** 평가 완료, 사용자 결정 필요

---

## 1. 데이터 사용 권한: 사용해도 되는가?

### 1.1 법적 근거

| 항목 | 상태 | 근거 |
|------|:----:|------|
| 라이선스 | **CC BY 4.0** | Mendeley Data 플랫폼 기본 라이선스 |
| 상업적 이용 | ✅ 허용 | CC BY는 상업적 이용도 허용 |
| 2차 분석 | ✅ 허용 | "adapt — remix, transform, and build upon the material" 명시 |
| 재배포 | ✅ 허용 | 단, 원저작자 표시(attribution) 필수 |
| 저자 허가 | **불필요** | CC BY 4.0 하에서 별도 허가 없이 사용 가능 |

**CC BY 4.0의 유일한 의무:** 적절한 크레딧(citation) 제공, 라이선스 명시, 변경 사항 표시

**필수 인용:**
> Bondi, A. B., Richardson, D. C., Butters, J. S., & Morina, F. (2023). Role of confidence and AI reliance on decision-making in chess [Data set]. Mendeley Data, V1. https://doi.org/10.17632/ng33vg479n.1

### 1.2 학술 윤리 측면

| 항목 | 판단 | 설명 |
|------|:----:|------|
| IRB 필요성 | **면제 가능** | 공개 데이터의 2차 분석은 대부분 IRB exempt (PSU IRB Category 4) |
| 개인식별 위험 | **없음** | 데이터에 이름/이메일 등 식별정보 없음, participant_id만 존재 |
| 데이터 무결성 | **확인 필요** | 원논문의 결과를 우리 파이프라인이 재현하는지 확인하면 신뢰도 상승 |
| Scooping 위험 | **낮음** | 원저자와 다른 분석 프레임워크(GMM trajectory) 적용이므로 독창성 확보 |

### 1.3 결론

**법적으로 완전히 허용되며, 별도의 저자 연락이나 허가가 필요 없다.**
다만, 학술적 예의(courtesy)로서:
- 논문에서 원 데이터의 출처를 명확히 밝히고
- 원 연구의 설계와 기여를 충분히 기술하며
- 가능하다면 출판 후 저자에게 결과를 공유하는 것이 좋은 관행

### 1.4 PSU IRB 절차

Penn State IRB에서 공개 데이터 2차 분석은 일반적으로:
- **Category 4 Exemption** 해당: "Secondary research for which consent is not required"
- CATS IRB 시스템에서 "Not Human Subjects Research (NHSR)" determination 요청 가능
- 또는 간단한 exemption application 제출 (보통 1-2주 소요)
- EdNet (CC BY-NC 4.0) + Chess Puzzle (CC BY 4.0) 모두 하나의 신청서로 처리 가능

---

## 2. 학술적 강화 가능성: 객관적 평가

### 2.1 강점 (Strengths)

#### S1. 이론-실증 완전 대응 — 가장 큰 강점

| 이론 패턴 | 실증 확인 | 데이터 원천 | 강도 |
|-----------|:--------:|-----------|:----:|
| Convergent | ✅ | EdNet + Chess | 강 |
| Oscillating | ✅ | EdNet(약) + Chess(중) | 중 |
| Stagnant | ✅ | EdNet | 중 |
| Catastrophic | ✅ | Chess only | **매우 강** |
| AI Benefit Emergence (NEW) | ✅ | EdNet + Chess | **강** |

5개 이론적 패턴 **모두** 실증적으로 확인됨. 특히 Catastrophic과 AI Benefit Emergence는 **data-driven GMM이 사전 지정 없이 자연발생적으로 식별**한 것이므로, 사후적 정당화(post-hoc rationalization)라는 비판을 피할 수 있다.

#### S2. 재현 가능성 (Replicability)

AI Benefit Emergence가 **두 개의 독립적 데이터셋**에서 확인됨:
- EdNet (관찰, N=4,568, 교육 도메인): S2 Class 4, Gap = −0.601
- Chess (실험, N=100, 의사결정 도메인): S2 Class 4, Gap = −0.600

서로 다른 설계, 다른 도메인, 다른 표본에서 Gap 값이 −0.600으로 거의 동일하다는 것은 **우연이라 보기 어렵다.** 이는 패턴의 구조적 재현성을 강하게 지지한다.

#### S3. 효과 크기의 극단성

cal_gap switch effect의 Cohen's d = ±2.0은 사회과학에서 극히 드문 크기이다. 이는 실험적 조작의 타당성과 cal_gap 변수의 민감도를 동시에 입증한다.

#### S4. 새로운 이론적 기여

기존 Trust Calibration 문헌은 **over-reliance(misuse)에 편향**되어 있다. AI Benefit Emergence는 **under-reliance(disuse)의 동적 궤적**이라는 상대적으로 덜 연구된 현상에 대한 이론적 설명을 제공한다. 이는 Parasuraman & Riley (1997)의 3분류(misuse/disuse/abuse)를 **시간 차원으로 확장**한 것이다.

#### S5. 상보적 연구 설계

| EdNet의 강점 | Chess의 강점 |
|-------------|-------------|
| 대규모 (N=4,568) | 높은 구성 타당도 |
| 생태학적 타당성 (실제 학습 플랫폼) | 실험적 통제 (AI reliability 조작) |
| 장기간 관찰 (~150 에피소드) | Trust violation event 존재 |
| Stagnant 패턴 식별 | Catastrophic 패턴 식별 |

### 2.2 약점 및 한계 (Weaknesses)

#### W1. Chess Puzzle 표본 크기

| 우려 | 심각도 | 완화 방안 |
|------|:------:|----------|
| N=100 (50명 × 2조건) | **중간** | within-subject 설계로 검정력 보완됨 |
| GMM에 100 관측치 | **중간-높음** | G=6에 100개는 소표본; 클래스당 N이 2-30으로 불균등 |
| Class 6 (N=2)의 해석 | **높음** | 2명만으로는 일반화 불가; "극단적 사례" 정도로만 보고 가능 |
| Class 4 (N=9)의 안정성 | **중간** | 부트스트랩 검증 또는 leave-one-out 분석 필요 |

**평가:** N=50/조건은 실험 연구에서 중간 규모이지만, GMM의 소표본 클래스(N=2, N=9)는 결과의 안정성에 대한 우려를 야기한다. 논문에서 이를 명시적으로 limitation으로 기술해야 한다.

#### W2. 30시행의 짧은 시계열

- 6개 윈도우(5시행/윈도우)는 궤적의 세밀한 변화를 포착하기 어려움
- 특히 전환 후 2개 윈도우(10시행)만으로 적응 과정의 전체 양상을 보기 부족
- EdNet의 10개 윈도우에 비해 시간적 해상도가 낮음

**평가:** 이 한계는 원 데이터의 설계에서 비롯되므로 해결 불가. 단, 전환 효과의 크기가 충분히 크므로(d > 2.0) 6개 윈도우로도 주요 패턴은 식별 가능하다.

#### W3. 조건-클래스 완전 분리 문제

GMM이 C1과 C2를 완전히 분리한 것은 실험 조작의 효과이지만, 동시에 **"같은 조건 내에서의 개인차"를 과소평가**할 위험이 있다. 조건 효과를 제거한 후(C1/C2 각각 별도 GMM) 개인차를 분석하는 추가 분석이 필요하다.

#### W4. 도메인 특수성

체스 퍼즐은 매우 특수한 과제이다:
- 전문적 지식 수준이 크게 다를 수 있음
- 이진적 정답/오답이 명확한 과제 (실세계 의사결정과 다름)
- AI 조언이 "하나의 수"로 제한됨 (실세계에서는 더 복잡)

**평가:** 이 한계는 EdNet과의 **도메인 다양성**으로 일부 보완된다. 체스와 수학 학습이라는 서로 다른 도메인에서 동일한 패턴이 발견되면, 도메인 특수성을 넘어선 일반적 현상임을 주장할 수 있다.

#### W5. 조작화의 차이

EdNet과 Chess에서 동일한 변수명(R_b, cal_gap)을 사용하지만, 조작적 정의가 다르다:
- EdNet R_b = feature adoption ratio (연속적, 간접적)
- Chess R_b = follow rate (이진 의사결정의 비율, 직접적)

**평가:** 이는 약점이기도 하지만, 다른 조작화에도 불구하고 동일 패턴이 나타난다면 **구성 타당도의 수렴적 증거(convergent evidence)**가 된다. 논문에서 이를 "conceptual replication"으로 프레이밍할 수 있다.

### 2.3 위협 요인 (Threats)

#### T1. 리뷰어의 예상 비판

| 비판 | 심각도 | 대응 |
|------|:------:|------|
| "N=100은 GMM에 너무 작다" | 높음 | 높은 사후확률(0.99), 부트스트랩 검증, EdNet(N=4,568) 보완 |
| "C1/C2 분리는 당연한 결과" | 높음 | 조건 내 개인차 분석(C1 내 Class 5 vs 1) 강조, 조건별 별도 GMM |
| "사후적 이론 맞추기" | 중간 | GMM이 사전 지정 없이 식별, pre-registration 부재는 인정 |
| "원 논문과의 차별성" | 중간 | 원 논문은 confidence/reliance 관계, 우리는 trajectory classification |
| "6윈도우로 trajectory 분석?" | 중간 | 제한 인정, 효과 크기가 충분히 크다는 점 강조 |

#### T2. Self-Plagiarism / 자기 반복 위험

EdNet 분석과 Chess 분석이 동일한 GMM 파이프라인을 사용하므로, 방법론적 차별화가 부족하다는 비판이 가능. 해결: 두 분석의 목적이 다름을 명확히 (EdNet = 탐색적 발견, Chess = 확인적 검증).

### 2.4 종합 평가

| 차원 | 등급 | 이유 |
|------|:----:|------|
| **이론적 기여** | **A** | 5개 패턴 모두 실증, 새 패턴(ABE) 발견, 시간 차원 확장 |
| **방법론적 엄밀성** | **B+** | GMM 적절하나 소표본 우려, 사전등록 부재 |
| **재현 가능성** | **A−** | 두 독립 데이터셋에서 ABE 재현, 단 표본 크기 차이 |
| **실용적 함의** | **B+** | 교육 및 의사결정 시스템 설계에 시사점, 단 개입 검증 미실시 |
| **출판 가능성** | **A−** | 상위 학회/저널 수준, 추가 분석으로 B+ → A 보완 가능 |

**종합:** 현재 상태에서도 출판 가능한 수준이나, 아래의 강화 분석을 수행하면 **상위 저널(CHI, CSCW, Computers & Education, IJAIED)** 수준으로 끌어올릴 수 있다.

---

## 3. 학술적 강화를 위한 구체적 절차

### Phase 1: 즉시 실행 (1-2일)

#### 1-1. 조건별 별도 GMM

현재 GMM은 C1/C2가 완전 분리되므로, **각 조건 내에서** 별도로 GMM을 실행해야 한다:
- C1 only (N=50): 30명이 Class 5(catastrophic), 20명이 Class 1(convergent)로 나뉘는가?
- C2 only (N=50): convergent, oscillating, ABE가 분리되는가?

이 분석이 중요한 이유: "조건이 다르니까 클래스가 다른 것 아니냐"는 리뷰어 비판에 대한 직접적 답변이 된다. 같은 조건 내에서도 **개인차**에 의한 클래스 분리가 일어남을 보여야 한다.

#### 1-2. 부트스트랩 안정성 검증

N=100에서의 GMM 해 안정성을 확인:
- 1,000회 부트스트랩 리샘플링
- 각 리샘플에서 최적 G와 클래스 비율 기록
- 소표본 클래스(Class 4: N=9, Class 6: N=2)의 안정적 출현 빈도 확인

#### 1-3. 원 논문 결과 재현 확인

Bondi et al. (2023)의 주요 결과를 우리 파이프라인에서 재현하여 데이터 무결성을 검증:
- 원 논문의 주요 통계량(예: 조건별 follow rate, confidence 변화)과 비교
- 일치하면 데이터 무결성 확인, 불일치하면 원인 파악

### Phase 2: 단기 보완 (3-5일)

#### 2-1. Mixed-Effects Model

GMM은 분류 도구이지만, **통계적 추론**을 위해서는 mixed-effects model이 필요:

```
cal_gap ~ window * condition + (window | participant)
R_b ~ window * condition + (window | participant)
```

- window × condition 상호작용 검증
- 전환 시점(W4 vs W5) 전후 비교 (contrast coding)
- 개인별 기울기(random slope)의 분산이 GMM 클래스 간 차이를 설명하는지

#### 2-2. 개인별 궤적 시각화

- 각 GMM 클래스에서 대표적 참가자 2-3명의 시행별 궤적 시각화
- Spaghetti plot + 클래스 평균 궤적 overlay
- 전환 시점을 수직선으로 표시

#### 2-3. 원 논문과의 차별화 분석

원 논문(Bondi et al., 2023)이 보고하지 않은 분석을 강조:
- 원 논문: confidence와 reliance의 상관 분석 → 정적 관계
- 우리: 시간에 따른 **궤적 분류** → 동적 패턴
- 원 논문: 조건 간 평균 비교
- 우리: 조건 **내** 개인차에 기반한 하위 유형 식별

### Phase 3: 논문 작성 (1-2주)

#### 3-1. 논문 프레이밍 결정

세 가지 옵션:

**Option A: Chess Puzzle 독립 논문 (권장)**
- "Trust Calibration Trajectories in Human-AI Decision Making: A GMM Analysis"
- Chess 데이터만으로 완결된 논문
- 장점: 간결하고 집중적, EdNet 논문과 별도로 출판 가능
- 단점: EdNet과의 시너지를 놓침

**Option B: EdNet 논문에 Chess를 "Study 2"로 포함**
- Study 1 (EdNet): 대규모 관찰 데이터 탐색적 분석
- Study 2 (Chess): 실험 데이터 확인적 분석
- 장점: 가장 강력한 논문 (탐색 + 확인), 재현 가능성 입증
- 단점: 두 연구의 프레이밍이 다르므로 통합이 어려울 수 있음

**Option C: 이론 논문에 양쪽을 증거로 활용**
- "A Taxonomy of Trust Calibration Trajectories: Theory and Evidence"
- 이론적 프레임워크를 전면에, 양 데이터를 증거로
- 장점: 이론적 기여 극대화
- 단점: 두 데이터셋의 방법론적 디테일을 충분히 보고하기 어려움

#### 3-2. 타겟 저널/학회

| 저널/학회 | 적합성 | 이유 |
|-----------|:------:|------|
| **CHI** | ★★★★★ | Human-AI interaction 핵심 학회, trajectory 분석 참신 |
| **CSCW** | ★★★★☆ | Collaborative AI 의사결정 적합 |
| **IJAIED** | ★★★★☆ | AI 교육 특화, EdNet 활용 시 최적 |
| **Computers & Education** | ★★★★☆ | EdNet 포함 시 |
| **Human Factors** | ★★★★☆ | Trust/reliance calibration 전통 학회 |
| **IJHCS** | ★★★★☆ | Human-computer studies, trust dynamics 적합 |
| **JDM (Journal of Decision Making)** | ★★★☆☆ | 의사결정 특화 |

#### 3-3. Pre-registration (사후등록)

현재 분석은 탐색적(exploratory)이므로 사전등록이 없다. 두 가지 대응:
1. **정직한 보고:** "The analysis was exploratory; pattern labels were assigned post-hoc based on theoretical correspondence"라고 명시
2. **사후 등록:** OSF에 현재까지의 분석 결과를 등록하고, **추가 확인적 분석**(예: 조건별 별도 GMM)을 사전등록한 후 실행

Option 2가 더 강력하다. 이미 발견한 패턴에 대해 "이 패턴이 조건 내에서도 나타나는가?"를 확인적 가설로 설정할 수 있다.

### Phase 4: 추가 강화 (선택적, 2-3주)

#### 4-1. 추가 데이터셋 적용

Discussion 12에서 식별한 대안 데이터셋에 동일 파이프라인 적용:
- **ImageNet-16H (Steyvers 2022)**: N=145, ~200 시행, OSF 공개
- **HAIID (Vodrahalli 2022)**: N=1,100+, GitHub 공개
- 3개 이상의 데이터셋에서 동일 패턴 재현 → 매우 강력한 증거

#### 4-2. 시뮬레이션 검증

이론적 프레임워크에서 5개 패턴을 생성하는 **에이전트 기반 시뮬레이션**:
- Bayesian trust update model로 convergent 생성
- Asymmetric update rate로 oscillating 생성
- Zero update rate로 stagnant 생성
- Trust violation event로 catastrophic 생성
- Slow positive update로 AI Benefit Emergence 생성
- 시뮬레이션 결과에 동일 GMM 적용 → 이론적 예측과 실증의 정합성 검증

#### 4-3. Chung & Yang (2024) 데이터 확보

Discussion 12에서 "이론적 최적 매치"로 평가한 데이터:
- 130명 × 100 시행, 저자가 이미 3가지 trust trajectory 유형 식별
- University of Michigan 연락 → 데이터 공유 요청
- 성공 시 가장 강력한 확인적 증거

---

## 4. 권장 우선순위 로드맵

```
즉시 (오늘-내일)
├── 1-1. C1/C2 별도 GMM 실행
├── 1-2. 원 논문 주요 결과 재현 확인
└── 1-3. PSU IRB exempt 신청 준비

단기 (이번 주)
├── 2-1. Mixed-effects model 실행
├── 2-2. 개인별 궤적 시각화
├── 2-3. 논문 프레이밍 결정 (Option A/B/C)
└── 2-4. OSF 사후등록 + 확인적 가설 사전등록

중기 (2-3주)
├── 3-1. 논문 초안 작성
├── 3-2. 부트스트랩 안정성 검증
└── 3-3. 타겟 저널 선정 및 형식 맞춤

선택적 강화
├── 4-1. 추가 데이터셋 (ImageNet-16H)
├── 4-2. 시뮬레이션 검증
└── 4-3. Chung & Yang 데이터 요청
```

---

## 5. 의사결정 기록

| 날짜 | 결정 |
|------|------|
| 2026-03-12 | 데이터 사용 권한 확인: CC BY 4.0, 저자 허가 불필요 |
| 2026-03-12 | PSU IRB Category 4 exempt 해당 확인 |
| 2026-03-12 | 학술적 강화 가능성 A− 평가 (추가 분석으로 A 가능) |
| 2026-03-12 | 즉시 필요: 조건별 별도 GMM, 원논문 재현, IRB 신청 |
| 2026-03-12 | 논문 프레이밍 결정 대기: Option A(독립) vs B(Study 2) vs C(이론) |
