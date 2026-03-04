# 07. 5-도메인 Research Orientation Typology 매핑 논의

## 1. 배경 및 목적

97편 코딩 데이터를 연구 성숙도 관점에서 재분류하기 위한 post-hoc 파생 변수(derived variable) 개발 작업. 기존 코딩 변수들(addresses_calibration, overtrust_discussed, undertrust_discussed, scaffold_proposed, framework)로부터 각 논문의 "신뢰 교정(trust calibration)에 대한 연구 지향성"을 5단계 도메인으로 매핑하는 것이 목표.

이 분류는 원래 코딩 당시 설계된 것이 아니라, 분석 과정에서 패턴을 발견한 후 사후적으로(post-hoc) 도출된 것임을 명시. 논문에서 투명하게 보고해야 함.

---

## 2. 5-도메인 정의

### D1: Trust Adoption (n=5, 5.2%)

- **정의**: TAM(Technology Acceptance Model) / UTAUT / DOI(Diffusion of Innovation) 프레임워크를 전용으로 사용하는 논문. 신뢰 교정(calibration)과는 무관하며, AI 수용(adoption)의 선행 변수로서 신뢰를 다룸.
- **해당 논문**: #25, #55, #57, #17, #18
- **특징**: 신뢰를 종속변수(수용 의도의 예측 변수)로 취급. 교정 개념 부재.

### D2: Trust Conceptualization (n=11, 11.3%)

- **정의**: 신뢰에 대한 일반적·개념적 논의를 하되, 구체적인 설계 제안이나 교정 기준을 다루지 않는 논문.
- **해당 논문**: #1, #15, #45, #59, #67, #90, #95, #105, #118, #122, #127
- **특징**: 이론적·철학적 접근. "AI를 신뢰해야 하는가", "신뢰의 본질은 무엇인가" 등의 논의. 실증적 개입 없음.

### D3: Trust Design (n=24, 24.7%)

- **정의**: 신뢰 관련 스캐폴드(scaffold) 또는 개입(intervention)을 제안하지만, 명시적인 교정 기준(calibration standard)을 설정하지 않은 논문.
- **해당 논문**: #26, #34, #35, #40, #41, #62, #64, #68, #74, #76, #81, #82, #84, #91, #92, #93, #108, #116, #123, #124, #128, #144, #20, #51
- **특징**: 설계 중심. 투명성 인터페이스, 설명 가능성 도구, 신뢰 구축 전략 등을 제안하지만, 과잉/과소신뢰 문제는 직접 다루지 않음.

### D4: Trust Awareness (n=41, 42.3%)

- **정의**: 과잉신뢰(overtrust) 또는 과소신뢰(undertrust)의 문제를 인식하고 논의하며, 부분적 교정(partially addresses calibration)을 시도하는 논문.
- **특징**: D3보다 진전된 인식 수준. 교정 방향을 제시하지만 체계적 기준은 부재.

#### D4a: Overtrust Recognition (n=16)
- 과잉신뢰(AI에 대한 무비판적 의존, 자동화 편향 등)만을 주된 문제로 다루는 논문군.

#### D4b: Undertrust Recognition (n=18)
- 과소신뢰(AI에 대한 불신, 거부, 회피 등)만을 주된 문제로 다루는 논문군.

#### D4c: Bidirectional Awareness (n=7)
- 과잉신뢰와 과소신뢰를 동시에 인식하고 논의하는 논문군.

### D5: Trust Calibration (n=16, 16.5%)

- **정의**: 신뢰 교정을 명시적으로 다루는 논문. addresses_calibration == "yes"에 해당.
- **출처 구분**: 데이터베이스(DB) 검색 3편 vs. 보충(supplementary) 검색 13편
- **특징**: 교정 기준, 교정 측정, 교정 개입의 효과 등을 직접 다룸.

---

## 3. 분류 우선순위 규칙 (Priority Rules)

97편 전체에 순서대로 적용되는 배타적(mutually exclusive) 분류 규칙:

| 우선순위 | 조건 | 배정 도메인 |
|:---:|---|:---:|
| 1 | `addresses_calibration == "yes"` | **D5** |
| 2 | (`overtrust_discussed == "yes"` OR `undertrust_discussed == "yes"`) AND `addresses_calibration == "partially"` | **D4** |
| 2-a | overtrust만 해당 | D4a |
| 2-b | undertrust만 해당 | D4b |
| 2-c | 둘 다 해당 | D4c |
| 3 | `scaffold_proposed == "yes"` AND NOT (D4 또는 D5) | **D3** |
| 4 | framework에 TAM/UTAUT/DOI 포함 AND NOT (D3, D4, D5) | **D1** |
| 5 | 위 조건 모두 불해당 | **D2** |

> **주의**: 우선순위 규칙은 위에서 아래로 순서대로 적용되며, 먼저 해당되는 규칙에 의해 배정된 논문은 이후 규칙에서 제외됨.

---

## 4. D4 하위 분류 결과 및 해석

| 하위 범주 | n | 비율 | 내용 |
|---|:---:|:---:|---|
| D4a: Overtrust Recognition | 16 | 39.0% | 과잉신뢰만 논의 |
| D4b: Undertrust Recognition | 18 | 43.9% | 과소신뢰만 논의 |
| D4c: Bidirectional Awareness | 7 | 17.1% | 양방향 논의 |
| **D4 합계** | **41** | **100%** | |

### 주목할 발견: D4b > D4a

D4b(과소신뢰, n=18)가 D4a(과잉신뢰, n=16)보다 많다는 사실은 흥미로운 발견임.

- **일반적 예상**: 대중 담론에서는 AI에 대한 과잉신뢰(무비판적 수용, 자동화 편향)가 더 큰 문제로 부각됨.
- **실제 문헌 패턴**: 교육 맥락에서는 AI 불신·거부·회피 문제(과소신뢰)가 더 자주 논의됨.
- **해석 가능성**:
  1. 교육 연구자들이 학생과 교사의 AI 수용 저항(adoption resistance)을 더 가시적인 문제로 경험하고 있을 가능성.
  2. 과잉신뢰는 조용히(silently) 발생하므로 연구자가 문제로 인식하기 어려울 수 있음.
  3. 교육 맥락 특수성: 학생의 AI 의존을 "과잉신뢰"로 볼 것인지 "학습 전략"으로 볼 것인지 구분이 모호한 경우.

---

## 5. 핵심 결정 사항

### Q1. D4에 scaffold_proposed 조건을 포함할 것인가?

**결정: 포함하지 않음.**

- **이유**: D4의 핵심 정의 기준은 "과잉/과소신뢰에 대한 인식(awareness)"이지, "설계 제안(design proposal)"이 아님.
- scaffold를 제안하더라도 overtrust/undertrust를 부분적으로 다루는 논문은 D4로 분류.
- scaffold 없이도 overtrust/undertrust를 인식하는 논문이 D4의 전형적 사례.
- D3와 D4의 구분은 "무엇을 설계했는가"가 아니라 "무엇을 인식했는가"에 기반.

### Q2. D1의 범위를 어떻게 설정할 것인가?

**결정: TAM/UTAUT/DOI "전용" 논문으로 제한.**

- **이유**: TAM/UTAUT/DOI를 다른 프레임워크와 결합하여 사용하는 경우, 해당 논문의 주된 연구 지향성은 수용(adoption)이 아닌 다른 방향일 가능성이 높음.
- 다른 프레임워크와 결합된 경우: 우선순위가 높은 D5, D4, D3 규칙이 먼저 적용됨.
- 순수하게 수용 모델만을 사용하는 논문만 D1로 분류하여 범주의 개념적 순수성 유지.

### Q3. D5의 DB vs. 보충 구분을 어떻게 보고할 것인가?

**결정: 투명하게 보고함.**

- **이유**: 16편 중 13편(81.3%)이 보충 검색에서 발굴된 사실은 연구의 주요 발견 중 하나임.
- 이는 교육 분야 주요 DB(ERIC, PsycINFO 등)에서 "trust calibration"이 핵심어로 거의 등장하지 않는다는 것을 의미.
- 즉, 교육 AI 신뢰 교정 연구가 교육학 DB에서 marginal position에 있다는 증거.
- 이를 은폐하지 않고 방법론 섹션에서 명시적으로 보고하는 것이 연구의 투명성을 높임.

### Q4. D4 하위 분류를 몇 개로 할 것인가?

**결정: 3개(D4a/D4b/D4c)로 확정.**

- **이유**: 더 세분화(예: overtrust 유형별, undertrust 원인별)하면 각 하위 범주의 n이 너무 작아져 의미 있는 패턴 해석이 불가능.
- 현재 3분류는 개념적으로도 명확(과잉만/과소만/양방향)하고 통계적으로도 충분한 n 확보.
- D4a(n=16), D4b(n=18), D4c(n=7)의 구분은 논문의 주된 관심 방향을 포착하기에 적합.

---

## 6. 검증 결과

Python 스크립트를 통해 97편 전체에 대해 우선순위 규칙을 순차 적용한 결과:

| 도메인 | n | 비율 |
|---|:---:|:---:|
| D1: Trust Adoption | 5 | 5.2% |
| D2: Trust Conceptualization | 11 | 11.3% |
| D3: Trust Design | 24 | 24.7% |
| D4: Trust Awareness | 41 | 42.3% |
| D5: Trust Calibration | 16 | 16.5% |
| **합계** | **97** | **100%** |

검증 결과: 97편 합계 **PASS** (누락 없음, 중복 배정 없음).

---

## 7. 추후 활용 방안

- 본 5-도메인 분류는 논문의 Figure 1(연구 성숙도 피라미드 또는 분포도)에 시각화 예정.
- Table 2 또는 Appendix에서 각 도메인별 논문 목록 제시.
- 5-도메인 분류를 연구 질문(RQ)과 연결: D4b > D4a 패턴, D5의 DB 부재, D1-D3의 calibration 공백 등을 논의 섹션에서 해석.
- 교육 AI 신뢰 연구의 성숙도 궤적(maturity trajectory)을 D1 → D2 → D3 → D4 → D5로 개념화하여 이론적 기여 강화.
