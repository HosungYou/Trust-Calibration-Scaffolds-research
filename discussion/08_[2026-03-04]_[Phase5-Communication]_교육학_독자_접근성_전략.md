# 08. 교육학 독자를 위한 접근성 전략

**날짜:** 2026-03-04
**맥락:** "The Calibration Gap" 논문의 타겟 독자(교육공학/교육심리학 연구자)가 SRL calibration에는 익숙하지만 trust-in-automation calibration에는 익숙하지 않다는 전제 하에, 논문의 접근성을 높이기 위한 전략 수립.

---

## 1. SRL Calibration에서 Trust Calibration으로의 브릿지 매핑

### 1.1 SRL Calibration이란 무엇인가

SRL(Self-Regulated Learning) calibration은 교육심리학에서 30년 이상 연구된 핵심 개념이다(Winne & Hadwin, 1998; Zimmerman, 2000; Nelson & Narens, 1990). 그 핵심은 다음과 같다.

**정의**: 학습자가 자신의 지식 상태와 수행 능력에 대해 내리는 메타인지적 판단의 정확도.

**조작화**: 전형적으로 학습자의 자기 예측(예: "이 시험에서 80점을 받을 것이다")과 실제 수행(예: 실제 점수 65점) 사이의 불일치(discrepancy)로 측정된다. 이 불일치가 작을수록 calibration이 높다.

**교정 실패의 두 방향**:
- 과추정(overestimation): "나는 안다"고 생각하지만 실제로는 모른다 --> Dunning-Kruger 효과의 교육적 발현
- 과소추정(underestimation): "나는 모른다"고 생각하지만 실제로는 안다 --> 불필요한 불안, 과도한 학습 시간 투자

**왜 중요한가**: 수십 년간의 연구가 SRL calibration이 학업 성취의 강력한 예측 변수임을 확인했다(Dunlosky & Rawson, 2012). 잘 교정된 학습자는 자신이 무엇을 모르는지 정확히 알기 때문에, 학습 전략을 효율적으로 배분할 수 있다. 메타인지적 모니터링(metacognitive monitoring)이 그 작동 메커니즘이다(Nelson & Narens, 1990).

**교육학 독자에게 이 개념은**: 완전히 친숙하다. Pieschl(2009)의 확장 모형, Panadero(2017)의 SRL 모델 리뷰, Greene & Azevedo(2007)의 Winne-Hadwin 모델 재검토 등을 통해 교육학 커뮤니티는 이 개념을 자기 것으로 체화하고 있다.

---

### 1.2 Trust Calibration이란 무엇인가

Trust calibration은 인간공학(human factors) 및 자동화 신뢰(trust-in-automation) 전통에서 발전한 개념이다(Lee & See, 2004; Hoff & Bashir, 2015).

**정의**: 사용자가 외부 자동화 시스템(여기서는 AI)의 능력에 대해 내리는 판단의 정확도. 즉, 사용자의 신뢰 수준과 시스템의 실제 신뢰성(reliability) 사이의 대응(correspondence) 정도.

**조작화**: 사용자의 주관적 신뢰 판단(예: "이 AI는 이 과제를 90% 정확하게 수행할 수 있다")과 AI의 실제 수행 정확도(예: 실제 정확도 60%) 사이의 불일치로 측정된다.

**교정 실패의 두 방향**:
- 과잉신뢰(overtrust): AI의 능력을 실제보다 높게 평가 --> 무비판적 수용, 인지적 오프로딩
- 과소신뢰(undertrust): AI의 능력을 실제보다 낮게 평가 --> 유익한 AI 지원의 거부

**왜 중요한가**: 자동화/HCI 분야에서는 이미 96편 이상의 논문이 신뢰와 시스템 신뢰성을 동시에 측정하는 연구를 수행했다(Wischnewski et al., 2023). 이 분야에서 trust calibration은 성숙한 연구 프로그램이다.

**교육학 독자에게 이 개념은**: 생소하다. Lee & See(2004)나 Hoff & Bashir(2015)는 교육학 독자가 일상적으로 접하는 문헌이 아니다. "trust calibration"이라는 용어 자체가 교육학 데이터베이스에서 거의 검색되지 않는다(본 리뷰에서 81개 DB 검색 논문 중 D5 도달은 3편, 3.7%에 불과).

---

### 1.3 공유하는 개념적 DNA

두 개념은 동일한 인지적 아키텍처 위에 서 있다. 이것이 바로 교육학 독자에게 전달해야 하는 핵심 메시지다.

| 공유 특성 | SRL Calibration | Trust Calibration |
|---|---|---|
| **본질** | 메타인지적 판단의 정확도 | 메타인지적 판단의 정확도 |
| **구조** | 주관적 판단 vs. 객관적 기준 | 주관적 판단 vs. 객관적 기준 |
| **측정 논리** | 예측-수행 불일치 | 신뢰-신뢰성 불일치 |
| **실패 방향** | 과추정 / 과소추정 | 과잉신뢰 / 과소신뢰 |
| **핵심 메커니즘** | 메타인지적 모니터링 | 메타인지적 모니터링 |
| **교육적 함의** | 부정확한 자기 판단 --> 비효율적 학습 전략 | 부정확한 AI 판단 --> 비적절한 AI 의존 |
| **개선 경로** | 내성적 훈련(자기평가, 반성적 저널) | 외부 지향적 훈련(AI 검증, 오류 패턴 인식) |

**핵심 공식**:
```
SRL Calibration  = f(자기 판단의 정확도) = |자기 예측 - 실제 수행|
Trust Calibration = f(AI 판단의 정확도)  = |AI에 대한 신뢰 - AI 실제 신뢰성|
```

두 공식의 구조는 동형(isomorphic)이다. 변수만 다르고, 판단 정확도를 측정하는 논리는 동일하다.

---

### 1.4 핵심 차이: 불확실성의 소재지(Locus of Uncertainty)

공유하는 DNA에도 불구하고, 두 개념 사이에는 근본적 차이가 존재한다.

**SRL Calibration의 소재지 = 자기(Self)**
- 판단의 대상: 나 자신의 지식, 능력, 수행
- 접근 경로: 내성(introspection), 자기 모니터링
- 개선 메커니즘: 자기평가 훈련, 반성적 저널, 오류 분석
- 정보 접근성: 원칙적으로 학습자 자신에게 접근 가능한 정보

**Trust Calibration의 소재지 = 외부 시스템(External System)**
- 판단의 대상: AI 시스템의 능력, 신뢰성, 한계
- 접근 경로: 시스템 관찰, 출력 검증, 성능 모니터링
- 개선 메커니즘: AI 리터러시 교육, 도메인별 성능 경험, 오류 패턴 학습
- 정보 접근성: 시스템이 불투명(opaque)하고, 맥락에 따라 성능이 극적으로 달라짐

**이 차이가 왜 결정적인가**:

SRL calibration을 높이기 위해 효과적인 개입(자기평가 활동, 메타인지적 프롬프트)은 trust calibration에 직접 전이되지 않는다. 왜냐하면 AI 시스템의 능력은 학습자의 내성을 통해 파악할 수 없기 때문이다. 자신이 미적분을 모른다는 것은 내성적으로 발견할 수 있지만, ChatGPT가 미적분을 얼마나 정확하게 푸는지는 내성이 아니라 시스템 관찰과 검증을 통해서만 파악할 수 있다.

**교육학 독자에게 전달할 핵심 문장**:

> "교육 연구자들이 잘 알고 있는 SRL calibration과 본 논문이 다루는 trust calibration은 동일한 메타인지적 판단 정확도라는 인지적 아키텍처를 공유한다. 그러나 판단의 대상이 '자기'에서 '외부 AI 시스템'으로 이동하면서, 필요한 정보 유형, 개선 메커니즘, 교육적 개입이 근본적으로 달라진다. SRL calibration이 높은 학습자라도 trust calibration이 자동으로 높지는 않다 -- 이 두 가지는 독립적인 교육 목표다."

---

### 1.5 논문이 이 브릿지를 더 효과적으로 활용하는 방법

현재 논문(Section 2.2, "SRL Calibration Versus Trust Calibration")은 이 구분을 이미 다루고 있다. 그러나 다음과 같은 보강이 필요하다.

**(1) 브릿지를 서론(Introduction)에서부터 미리 놓기**

현재 구조: 서론에서 Bastani et al. --> trust calibration 개념 도입 --> Section 2.2에서야 SRL과의 관계 설명.

제안 구조: 서론에서 Bastani et al. --> "이 현상의 핵심은 calibration의 실패다" --> "교육 연구자들은 calibration 개념에 이미 익숙하다 -- SRL calibration이 바로 그것이다" --> "그러나 AI 시대에는 새로운 유형의 calibration이 필요하다: 자기가 아닌 AI 시스템에 대한 판단의 정확도, 즉 trust calibration" --> 이 한 문단으로 교육학 독자가 '아, 이건 내가 아는 calibration의 확장이구나'라고 즉시 인식하게 만든다.

**(2) SRL을 출발점으로 삼는 서술 전략**

현재 서술은 Lee & See(2004)에서 출발한다. 이것은 인간공학/HCI 독자에게는 자연스럽지만, 교육학 독자에게는 낯선 문헌에서 시작하는 셈이다.

제안: Section 2를 SRL calibration의 간략한 요약에서 시작하고 ("교육 연구에서 calibration은 다음을 의미한다..."), 그 다음에 "이 동일한 논리를 AI 시스템에 대한 판단에 적용하면..."이라는 전환을 통해 trust calibration을 도입한다. Lee & See(2004)는 이 전환 이후에 trust calibration의 형식적 정의를 제공하는 역할로 배치한다.

이렇게 하면 서술의 방향이 "교육학 독자가 아는 것(SRL calibration) --> 교육학 독자가 모르는 것(trust calibration)"이 되어, 독자의 인지적 부하를 최소화한다.

**(3) "이중 교정(Dual Calibration)" 프레임 명시화**

논문이 궁극적으로 말하고 싶은 것은, AI 통합 학습 환경에서 학습자는 두 가지 교정 과제를 동시에 안고 있다는 것이다:
1. 자기 능력에 대한 교정 (SRL calibration) -- 이미 연구됨
2. AI 능력에 대한 교정 (trust calibration) -- 거의 연구되지 않음

이것을 "이중 교정 과제(dual calibration challenge)"로 명명하고, 기존 SRL 연구가 (1)만 다루고 (2)를 간과해 왔음을 지적하면, 교육학 독자가 논문의 기여를 자신의 기존 지식 체계 안에서 즉시 위치화할 수 있다.

---

## 2. 초록 재작성

### 2.1 현재 초록의 문제 진단

현재 초록은 매우 밀도 높은 전문 용어로 작성되어 있다. 구체적 문제점:

1. **첫 문장부터 결론**: "do learners trust AI systems appropriately?"라는 질문은 좋지만, 교육학 독자가 이 질문의 중요성을 체감할 여유 없이 바로 Bastani et al.의 세부 수치(17%)로 들어간다.

2. **용어의 밀도**: "trust calibration maturity spectrum", "calibration threshold", "Trust-AI Reliability Matrix" 등이 정의 없이 한 문단 안에 등장한다.

3. **독자의 인지적 앵커 부재**: 교육학 독자가 자신의 기존 지식과 연결할 수 있는 다리(SRL calibration, metacognition 등)가 초록에 전혀 없다.

4. **수사적 구조의 부재**: 현재 초록은 "결과1 + 결과2 + 함의"의 나열 구조인데, "문제 --> 갭 --> 발견 --> 의미"의 서사 구조가 더 효과적이다.

### 2.2 재작성된 초록

아래 초록은 교육학 독자의 접근성을 최대화하면서도 핵심 주장을 모두 보존한다. 약 290단어.

---

**[재작성 초록]**

When AI tutoring tools harm rather than help learning, the culprit is not the technology itself but how learners judge its capabilities. Bastani et al. (2025) found that unrestricted ChatGPT access reduced exam performance by 17% -- not because the AI failed, but because students accepted its outputs uncritically, bypassing the cognitive effort that produces learning. This pattern reflects a calibration failure: students' trust in AI did not match the AI's actual reliability.

Education researchers are deeply familiar with calibration as a concept. In the self-regulated learning (SRL) tradition, calibration refers to the accuracy of learners' judgments about their own knowledge (Winne & Hadwin, 1998). Trust calibration extends this same logic to a new object: the accuracy of learners' judgments about an external AI system's capabilities (Lee & See, 2004). While both involve metacognitive judgment accuracy, they require fundamentally different informational inputs -- self-monitoring versus system monitoring -- and thus different educational supports.

This critical review of 97 studies on trust in educational AI (2015-2026) reveals that the field has not yet made this extension. We introduce a 5-domain Research Orientation Typology classifying the literature along a calibration maturity spectrum. The analysis exposes a pronounced calibration gap: 83.5% of studies remain below the calibration threshold; 84.5% provide no explicit trust definition; only 7.2% measure trust empirically; and no study simultaneously measures both learner trust and AI reliability -- the minimum requirement for calibration assessment. Meanwhile, 96 studies in the automation field routinely perform such dual measurement (Wischnewski et al., 2023).

We argue for a paradigm shift from "Do learners trust AI?" to "Is their trust calibrated?" and introduce the Trust-AI Reliability Matrix as a diagnostic tool. The findings underscore that without calibration-oriented measurement and theory, education cannot distinguish warranted trust from dangerous overreliance.

---

### 2.3 재작성의 핵심 전략 분석

| 전략 | 현재 초록 | 재작성 초록 |
|---|---|---|
| **시작점** | 추상적 질문 | Bastani의 구체적 결과(서사적 훅) |
| **SRL 연결** | 없음 | 두 번째 문단 전체가 SRL --> Trust Calibration 브릿지 |
| **독자 위치** | 밖에서 바라보는 관찰자 | "교육 연구자들은 이미 calibration을 알고 있다"로 독자를 내부에 위치시킴 |
| **96 vs 0 대비** | 없음 | 명시적으로 포함 |
| **용어 밀도** | 매우 높음 | 핵심 용어만 남기고 설명과 함께 도입 |
| **서사 구조** | 나열형 | 문제 --> 익숙한 개념 --> 확장 --> 갭 발견 --> 전환 제안 |

---

## 3. 섹션별 접근성 개선 제안

### 3.1 Introduction: 교육학 독자를 즉시 사로잡는 전략

**현재 구조의 강점**: Bastani et al.(2025)의 17% 성과 감소라는 충격적 사실로 시작하는 것은 매우 효과적이다. 이 훅은 유지해야 한다.

**개선 방향 1: SRL 교정을 서론에서 미리 언급**

현재 서론의 "The Conceptual Problem: Trust Level Is Not Trust Calibration" 소절(Line 33)에서 trust calibration을 설명할 때, SRL calibration과의 관계를 2-3문장으로 미리 짚어주는 것이 효과적이다. 예시:

> "Education researchers are well acquainted with the calibration concept through the self-regulated learning tradition, where it denotes the accuracy of learners' self-judgments (Winne & Hadwin, 1998). Trust calibration extends this logic from self to system: it captures whether a learner's trust in AI corresponds to the AI's actual capabilities (Lee & See, 2004)."

이 2문장만 추가하면, 교육학 독자는 "calibration"이라는 단어를 처음 접하는 순간부터 자신의 기존 지식과 연결할 수 있다.

**개선 방향 2: "왜 TAM이 문제인가"를 교육학 독자의 경험에 연결**

현재 서론의 "Existing Research Limitations" (Line 41-47)은 TAM/UTAUT/SRL 프레임워크의 한계를 나열하지만, 교육학 독자의 일상적 경험과 연결하지 않는다. 개선 제안:

> "Many education researchers have experienced this firsthand: a student reports high confidence in ChatGPT across all subjects, yet the AI's actual accuracy varies dramatically from historical summaries (high) to mathematical proofs (low). Current survey instruments capture the student's undifferentiated trust but cannot detect this domain-specific miscalibration."

이런 구체적 시나리오가 한두 개 있으면, 독자는 "맞아, 이런 게 진짜 문제지"라고 공감하며 읽게 된다.

**개선 방향 3: RQ를 교육학 네이티브 언어로 프레이밍**

현재 RQ는 기능적이지만 다소 건조하다. 교육학 독자에게 더 울림을 주는 표현:

- RQ1 (현재): "How does existing research approach trust in educational AI?"
  - (제안): "What does the educational AI literature see -- and what does it miss -- when it examines learner trust?" (교육 연구 문헌이 학습자 신뢰를 바라볼 때 무엇을 보고 무엇을 놓치는가)

- RQ2 (현재): "To what extent does current research address trust calibration?"
  - (제안): "How wide is the gap between the field's awareness of trust problems and its capacity to measure them?" (신뢰 문제의 '인식'과 '측정 능력' 사이의 간극은 얼마나 큰가)

- RQ3 (현재): "What theoretical and methodological reframing is needed?"
  - (제안): 유지하되, "...to equip education researchers with the tools they currently lack?" 추가 (교육 연구자들이 현재 갖추지 못한 도구를 확보하기 위해)

---

### 3.2 Conceptual Foundation: SRL에서 Trust Calibration으로의 전환 시퀀싱

**현재 구조 (Section 2)**:
1. Trust Calibration: From Automation to Education (Lee & See 중심)
2. SRL Calibration Versus Trust Calibration
3. Why TAM/UTAUT Cannot Capture Calibration

**제안 구조 (독자 친화적 순서)**:
1. **"교정"이란 무엇인가: 교육 연구의 오랜 친구** (SRL calibration에서 시작)
   - 교육학 독자가 이미 아는 것에서 출발
   - "학습자가 자기 능력을 얼마나 정확하게 판단하는가"
   - 이것이 왜 중요한지: 30년간의 실증 증거

2. **AI 시대의 새로운 교정 과제: 자기에서 시스템으로** (Trust calibration 도입)
   - "이제 학습자는 자기 자신뿐 아니라 AI 시스템에 대해서도 정확한 판단을 내려야 한다"
   - Lee & See(2004)의 trust calibration 정의를 여기서 도입
   - 두 calibration의 공유 DNA와 핵심 차이 분석
   - 적분학 예시: 높은 SRL calibration이 높은 trust calibration을 보장하지 않음

3. **왜 기존 프레임워크는 이 새로운 교정을 포착하지 못하는가**
   - SRL 프레임워크의 한계: 외부 시스템에 대한 판단을 다루지 않음
   - TAM/UTAUT의 한계: 신뢰를 최대화 대상으로만 봄, 교정 축 부재
   - 이 두 한계의 결합이 현재의 "교정 갭"을 구조적으로 생산

**이 재순서화의 효과**: 독자가 "아는 것"(SRL calibration)에서 "모르는 것"(trust calibration)으로 자연스럽게 이동한다. Lee & See(2004)라는 낯선 문헌은 독자가 이미 개념적 기반을 마련한 후에 등장하므로, "이게 뭐지?"가 아니라 "아, SRL calibration의 확장을 공식화한 사람이구나"로 수용된다.

---

### 3.3 Findings: 유형론을 더 직관적으로 제시하기

**현재 구조의 강점**: 5-domain typology는 이 논문의 핵심 기여이며, 구조 자체는 강력하다.

**접근성 개선 전략**:

**(1) 유형론을 "성숙도 여정(maturity journey)"으로 프레이밍**

현재 제시 방식: 5개 도메인을 D1부터 D5까지 순서대로 설명하는 백과사전적 나열.

제안: "imagine the field is on a journey toward understanding trust calibration"라는 은유로 시작하고, 각 도메인을 여정의 단계로 제시한다.

- D1 = "AI를 사용할 것인가?" (수용의 질문)
- D2 = "신뢰가 중요한가?" (개념적 인식)
- D3 = "어떻게 신뢰를 설계할 것인가?" (설계적 대응)
- D4 = "신뢰가 잘못될 수 있는가?" (문제 인식)
- D5 = "신뢰가 실제로 정확한가?" (교정 측정)

이 한 줄 요약이 각 도메인 설명 앞에 붙으면, 독자는 전체 유형론의 논리를 즉시 파악한다.

**(2) "교정 임계선(calibration threshold)"을 시각적으로 강화**

D4와 D5 사이의 임계선은 이 논문의 핵심 발견이다. "83.5%가 임계선 아래"라는 통계는 강력하지만, 독자가 이것을 체감하려면 시각적 장치가 필요하다. Figure 2에서 이미 빨간 점선으로 표시하고 있지만, 텍스트에서도 이 임계선의 의미를 교육학 언어로 풀어줘야 한다:

> "83.5%의 연구가 이 임계선 아래에 있다는 것은, 교육 AI 분야가 '학습자의 신뢰가 정확한가?'라는 질문을 아직 묻지 못하고 있다는 뜻이다. 이것은 SRL 연구에 비유하면, 학습자의 자신감을 측정하면서 실제 수행 점수는 측정하지 않는 것과 같다 -- 과신인지 적정 자신감인지를 구별할 수 없는 상태다."

이 SRL 비유 한 문장이, 교육학 독자에게 갭의 심각성을 즉각적으로 전달한다.

**(3) D4의 "인식-측정 간극"을 교육학 독자의 경험에 연결**

D4가 42.3%로 가장 큰 도메인이라는 발견은 중요하다. 이것을 교육학 독자에게 더 와닿게 만드는 방법:

> "D4에 해당하는 연구들은 '학생들이 AI를 너무 믿는다' 또는 '학생들이 AI를 안 믿는다'고 말하지만, 실제로 그 판단이 맞는지 확인하지는 않는다. 이것은 교사가 '이 학생은 수학을 과신한다'고 말하면서 실제로 학생의 수학 점수를 확인하지 않는 것과 같다."

---

### 3.4 Discussion: 교육학 네이티브 언어로 함의 프레이밍

**현재 구조의 강점**: 연구 아젠다 5개 우선순위가 체계적이고 구체적이다.

**접근성 개선 전략**:

**(1) 패러다임 전환을 교육학의 역사적 전환에 비유**

현재 Kuhn(1962)의 패러다임 전환을 인용하는 것은 적절하지만, 교육학 독자에게 더 와닿는 비유가 있다:

> "교육 평가 분야가 '학생이 얼마나 자신감 있는가?'에서 '학생의 자신감이 실제 능력과 일치하는가?'로 전환한 것이 SRL calibration 연구의 탄생이었다. 본 논문은 AI 신뢰 연구에서 정확히 동일한 전환을 요구한다: '학습자가 AI를 신뢰하는가?'에서 '학습자의 신뢰가 AI의 실제 능력과 일치하는가?'로."

**(2) 실천적 함의를 교실 시나리오로 구체화**

Priority 3(Calibration interventions)에서 제안하는 개입들(메타인지적 프롬프팅, 생산적 실패, 불확실성 투명성)이 실제 교실에서 어떻게 보일지 1-2문장으로 구체화:

> "예를 들어, AI가 에세이 피드백을 제공한 후 학습자에게 '이 피드백의 어느 부분이 가장 정확하고, 어느 부분이 의심스러운가?'를 평가하도록 요청하는 메타인지적 프롬프트는, 학습자의 trust calibration을 능동적으로 훈련시키는 동시에 SRL calibration도 강화한다."

**(3) 연구 아젠다를 교육학 저널의 관심사에 연결**

Priority 4(Longitudinal calibration development)는 Computers & Education 독자에게 특히 매력적이다. 이것을 더 교육학적으로 프레이밍:

> "SRL calibration이 한 학기에 걸쳐 어떻게 발달하는지는 풍부하게 연구되어 왔다. Trust calibration의 발달 궤적은 전혀 알려져 있지 않다. 학생이 AI 도구를 처음 사용하는 순간부터 학기 말까지, trust calibration은 자연스럽게 향상되는가, 아니면 명시적 교육이 필요한가? 이것은 교육 설계에 직접적 함의를 가지는 실증적 질문이다."

---

## 4. 용어 전략: "Trust Calibration"을 그대로 쓸 것인가

### 4.1 대안 용어 분석

| 대안 용어 | 장점 | 단점 | 판정 |
|---|---|---|---|
| **Trust Calibration** (현행) | 학술적 정확성 최고; Lee & See(2004) 직접 계승; SRL calibration과 병렬 구조 형성 | 교육학 독자에게 생소; "calibration"이 기술적으로 들릴 수 있음 | **유지 (권장)** |
| **Trust Accuracy** | 직관적; 판단의 "정확도"라는 의미 명확 | 기존 문헌에서 확립되지 않은 새 용어; accuracy는 AI 시스템의 정확도와 혼동 가능 | 부적절 |
| **Appropriate Trust** | 교육학에서 자연스러움; "적절한 신뢰"라는 일상 언어 | 측정 불가능한 규범적 판단처럼 들림; 조작화가 어려움; Mehrotra et al.(2024)이 이미 사용하나 정의가 모호 | 보조적 사용 가능 |
| **Warranted Trust** | 인식론적 전통에 뿌리; "정당화된 신뢰"라는 의미 명확 | 철학적 과부하; 측정과의 연결이 약함 | 수사적 맥락에서만 |
| **Trust-Reliability Alignment** | 매트릭스의 두 축을 직접 반영; 측정 논리가 용어에 내재 | 너무 길고 기술적; 기존 문헌에 없는 완전한 신조어 | 설명적 맥락에서만 |

### 4.2 권장 전략: "Trust Calibration" 유지 + 브릿지 표현 병용

**핵심 결정**: "Trust calibration"을 논문 전체의 공식 용어로 유지한다.

**이유**:
1. Lee & See(2004)의 공식 용어를 그대로 사용하는 것이 학문적 계보를 명확히 한다.
2. SRL calibration과의 병렬 구조("SRL calibration = 자기 판단의 정확도" / "trust calibration = AI 판단의 정확도")가 이 논문의 핵심 이론적 장치이므로, "calibration"이라는 공유 용어가 필수적이다.
3. 교육학에서 이 용어가 생소한 것 자체가 논문의 발견이다. 81개 교육 AI 논문 중 3편만이 calibration 관점을 채택했다는 것이 calibration gap의 증거다. 용어를 희석하면 이 발견의 날카로움도 희석된다.

**단, 접근성을 위한 브릿지 표현을 체계적으로 사용**:

- **첫 등장 시**: "trust calibration -- the accuracy of learners' judgments about an AI system's capabilities, analogous to the SRL concept of calibration applied to self-knowledge (Winne & Hadwin, 1998)"
- **이후 반복 시**: 필요에 따라 "whether learner trust matches AI reliability" 등의 풀어쓴 표현을 병용
- **수사적 맥락에서**: "appropriate trust", "warranted trust"를 보조적으로 사용 가능 (예: "the field cannot distinguish warranted trust from dangerous overreliance")
- **제목/소제목에서**: "Trust Calibration"을 그대로 사용하되, 부제에서 교육학 언어로 보충 (예: "Trust Calibration: When Does Trust Match Reality?")

### 4.3 피해야 할 함정

- **"Appropriate Trust"를 주 용어로 사용하지 않기**: 이 표현은 직관적이지만 조작화가 불가능하다. "적절한"이라는 판단을 누가 어떤 기준으로 내리는가? Calibration은 측정 가능하다(신뢰 수준 - 실제 신뢰성 = 교정 오차). Appropriateness는 측정 가능하지 않다.
- **용어를 자주 바꾸지 않기**: 같은 개념을 "trust calibration", "appropriate trust", "trust-reliability alignment"로 번갈아 쓰면 독자가 서로 다른 개념인지 같은 개념인지 혼동한다. 핵심 용어는 일관되게 "trust calibration"으로 통일하되, 풀어쓴 설명은 변형해도 된다.

---

## 5. 시각적 커뮤니케이션 전략

### 5.1 "논문을 대충 훑는" 교육학 독자의 읽기 행동 분석

교육공학/교육심리학 연구자가 새 논문을 처음 접할 때의 전형적 읽기 순서:

1. 제목 (2초)
2. 초록 (30초)
3. Figure/Table 훑기 (1분) -- **이 단계에서 "읽을 가치가 있는가"를 판단**
4. 서론 마지막 단락 (연구 질문/기여) (30초)
5. 결론 (30초)
6. (여기까지 통과하면) 전문 읽기

따라서 **Figure와 Table만 봐도 논문의 핵심 주장이 전달되어야** 한다.

### 5.2 현재 Figure/Table과 개선 제안

**Figure 1: PRISMA-style Flow Diagram** -- 유지. 리뷰 논문의 표준 요소.

**Figure 2: Research Orientation Typology Distribution** -- 핵심 개선 필요.

현재: 5개 도메인의 분포를 보여주는 막대 그래프 + 빨간 점선(calibration threshold).

개선 제안: 이 그래프를 "계단형 성숙도 다이어그램(staircase maturity diagram)"으로 전환한다.

```
[제안 시각화 구조]

                                              ----
                                             | D5 |  Trust Calibration
                                             | 16 |  (16.5%)
                                        -----|    |
                                       |    D4    |  Trust Awareness
                                       |    41    |  (42.3%)
                                  -----|          |
                                 |      D3        |  Trust Design
                                 |      24        |  (24.7%)
                            -----|                |
                           |       D2             |  Trust Conceptualization
                           |       11             |  (11.3%)
                      -----|                      |
                     |        D1                  |  Trust Adoption
                     |         5                  |  (5.2%)
                     |____________________________|

                     <--- 교정 미달 (83.5%) --->|<-- 교정 도달 (16.5%)
                                                ^
                                         교정 임계선
                                     (Calibration Threshold)
```

이 시각화의 장점:
- "성숙도가 높아진다"는 것이 공간적으로 즉시 드러남
- D4-D5 사이의 임계선이 "절벽(cliff)"처럼 보여서 갭의 심각성 전달
- 각 계단의 높이(비율)가 면적으로 비교 가능

**Figure 3: Calibration Gap Funnel** -- 핵심 개선 필요.

현재: 좌측 패널(97 --> 1 감소 깔때기) + 우측 패널(96 vs 0 비교).

개선 제안: 이 Figure를 교육학 독자에게 가장 충격적인 하나의 이미지로 축약한다.

**"이중 깔때기(Dual Funnel)" 디자인**:
- 좌측: 교육 AI 연구의 깔때기 (97 --> 51 --> 42 --> 16 --> 7 --> 1 --> 0)
  - 각 단계에 교육학 언어 라벨: "신뢰 언급" --> "과잉/과소신뢰 논의" --> "교정 부분 인식" --> "교정 명시적 연구" --> "신뢰 실증 측정" --> "교정 정확도 측정" --> "신뢰 + 신뢰성 동시 측정"
- 우측: 자동화/HCI 연구의 깔때기 (96편이 이미 동시 측정)
- 두 깔때기를 나란히 배치하면, "같은 질문에 대해 한 분야는 96편, 다른 분야는 0편"이라는 학제 간 단절이 시각적으로 즉시 전달됨

**Figure 4: Trust-AI Reliability Matrix** -- 기본 유지, 교육학 라벨 보강.

현재: 2x2 매트릭스, 4사분면.

개선 제안: 각 사분면에 교육 시나리오 예시를 1줄씩 추가한다.

| | 높은 AI 신뢰성 | 낮은 AI 신뢰성 |
|---|---|---|
| **높은 학습자 신뢰** | Q1: 교정된 적절한 사용 (예: 역사적 사실 요약에 AI 활용) | Q2: "Bastani Trap" -- 위험한 과잉신뢰 (예: 수학 증명에 AI를 무비판적으로 수용) |
| **낮은 학습자 신뢰** | Q3: 교정되지 않은 과소신뢰 (예: AI의 문법 교정을 불필요하게 불신) | Q4: 교정된 회피 (예: 임상추론에서 AI를 신중하게 회피) |

이 교육 시나리오 예시가 있으면, 교육학 독자가 매트릭스를 "이론적 도구"가 아니라 "내 교실에서 일어나는 일의 지도"로 인식한다.

**Figure 5: Theoretical Framework Landscape** -- 유지하되, 교육학 독자에게 의미 있는 하이라이트 추가.

개선 제안: "49.5% 무프레임워크" 영역을 "기회의 창(Window of Opportunity)"으로 라벨링. 이 논문의 주장은 이 49.5%가 TAM에 잠기지 않았기 때문에 calibration 패러다임으로 전환 가능하다는 것이므로, 시각적으로 이것을 강조한다.

### 5.3 추가로 필요한 새 시각화 제안

**[신규] Table: SRL Calibration vs. Trust Calibration 비교표**

이 비교표를 Section 2에 삽입하면, 논문의 핵심 이론적 기여를 한눈에 전달할 수 있다.

| 차원 | SRL Calibration | Trust Calibration |
|---|---|---|
| **판단의 대상** | 자기 자신의 지식/능력 | AI 시스템의 능력/신뢰성 |
| **불확실성의 소재지** | 자기(Self) | 외부 시스템(External System) |
| **핵심 질문** | "나는 이것을 아는가?" | "이 AI는 이것을 할 수 있는가?" |
| **측정 공식** | \|자기 예측 - 실제 수행\| | \|AI에 대한 신뢰 - AI 실제 신뢰성\| |
| **과추정의 형태** | "나는 안다" (실제로 모름) | "AI가 맞다" (실제로 틀림) |
| **과소추정의 형태** | "나는 모른다" (실제로 앎) | "AI는 못한다" (실제로 잘함) |
| **개선 메커니즘** | 자기평가, 반성적 저널, 메타인지 훈련 | AI 리터러시, 도메인별 검증 경험, 오류 패턴 학습 |
| **연구 성숙도** | 성숙 (30년+, 수백 편의 실증 연구) | 초기 (교육 맥락에서 거의 0편) |
| **교육학적 함의** | 비효율적 학습 전략 선택 | AI에 대한 비적절한 의존 패턴 |
| **핵심 이론가** | Winne & Hadwin (1998); Nelson & Narens (1990); Zimmerman (2000) | Lee & See (2004); Hoff & Bashir (2015) |

이 표 하나가 논문의 전체 이론적 기여를 압축한다.

**[신규] Figure: "이중 교정 과제" 개념도**

AI 통합 학습 환경에서 학습자가 동시에 직면하는 두 가지 교정 과제를 시각화:

```
[학습자] --> [자기 판단] --> 나는 이것을 아는가? --> SRL Calibration
    |                                                    (이미 연구됨)
    |
    +-----> [AI 판단]  --> 이 AI는 이것을 할 수 있는가? --> Trust Calibration
                                                           (연구 갭)
```

이 간단한 다이어그램이 "왜 SRL calibration으로는 충분하지 않은가"를 즉시 전달한다. AI 이전에는 학습자가 자기 자신만 교정하면 되었지만, AI 통합 환경에서는 자기와 시스템 모두를 교정해야 한다는 메시지.

**[신규] Table: 96 vs. 0 대비표**

논문에서 가장 강력한 수사적 장치인 "96 vs. 0"을 독립적인 Table로 격상시키는 것을 제안:

| 측정 유형 | 자동화/HCI (Wischnewski et al., 2023) | 교육 AI (본 리뷰, N=97) |
|---|:---:|:---:|
| 신뢰 수준 측정 | 96편 모두 포함 | 7편 (7.2%) |
| AI 신뢰성 측정 | 96편 모두 포함 | 측정 없음 |
| 두 변수 동시 측정 | **96편** | **0편** |
| 교정 정확도 계산 | 96편 | 1편 |

이 4행짜리 표가 "calibration gap"의 전체 논증을 압축한다.

---

## 6. 종합 요약: 핵심 접근성 전략 체크리스트

| # | 전략 | 적용 위치 | 효과 |
|---|---|---|---|
| 1 | SRL calibration을 서론에서 미리 언급하여 독자의 인지적 앵커 생성 | Introduction, Section 1 | 교육학 독자가 "calibration"을 처음 접하는 순간 기존 지식과 연결 |
| 2 | Conceptual Foundation을 SRL에서 시작하여 Trust Calibration으로 전환하는 순서로 재배치 | Section 2 | "아는 것 --> 모르는 것" 순서로 인지 부하 최소화 |
| 3 | 초록에 SRL-Trust Calibration 브릿지 삽입 | Abstract | 논문의 이론적 위치를 즉시 파악 가능 |
| 4 | 5-domain typology를 "성숙도 여정" 은유로 프레이밍 | Section 4 | 유형론의 논리를 직관적으로 전달 |
| 5 | 교정 갭을 SRL 비유로 설명 ("자신감은 재면서 점수는 안 재는 것") | Section 5 | 갭의 심각성을 교육학 독자의 경험에 연결 |
| 6 | SRL vs. Trust Calibration 비교표 삽입 | Section 2 (Table) | 핵심 이론적 기여를 한눈에 전달 |
| 7 | Trust-AI Reliability Matrix에 교육 시나리오 예시 추가 | Figure 4 | 이론적 도구를 교실 현실에 접지 |
| 8 | 96 vs. 0 대비를 독립 Table로 격상 | Section 5 | 가장 강력한 수사적 장치의 시각적 강화 |
| 9 | "Trust Calibration" 용어 유지 + 첫 등장 시 SRL 비유와 함께 도입 | 전체 | 학술적 정확성과 접근성의 균형 |
| 10 | RQ를 교육학 네이티브 언어로 보강 | Section 1 | 연구 질문이 교육학 독자의 관심사와 직결됨을 전달 |

---

*이 문서는 2026-03-04 교육학 독자 접근성 전략 논의의 기록이며, 원고 개선 작업의 기반 자료로 활용됩니다.*
