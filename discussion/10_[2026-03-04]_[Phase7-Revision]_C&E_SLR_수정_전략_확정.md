# 10. C&E 투고를 위한 SLR 수정 전략 확정

**날짜:** 2026-03-04
**이전 논의:** 01-09번 discussion + Diverga G1/A3/F1 분석 종합
**타겟 저널:** Computers & Education (IF ~12-14)
**워드 리밋:** 8,000 words (참고문헌, 부록 제외)
**리뷰 유형 전환:** Critical Review → Systematic Review with Critical Synthesis

---

## 1. 확정된 전략적 결정

| 결정 사항 | 확정 |
|-----------|------|
| 타겟 저널 | Computers & Education |
| 리뷰 유형 | Systematic review with critical synthesis (PRISMA 2020) |
| 코더간 신뢰도 | 2차 코더 확보 가능 → 20% 서브샘플 코딩 후 Cohen's kappa 보고 |
| 50편 미코딩 | 추가 확보 불가 → title/abstract 스크리닝 + 민감도 분석으로 대체 |
| 6개 스캐폴드 / 적응적 사이클 | 별도 후속 논문으로 분리. 본 논문에서 삭제 |
| "Bastani Trap" 라벨 | 일반적 용어("Dangerous Overtrust" 또는 "Uncalibrated Overtrust")로 교체 |
| Table Y (96 vs 0) | 테이블 삭제 → 문장으로 전환 (방법론적 한정 포함) |
| DB(n=81) vs 보충(n=16) | 통계 분리 보고 |
| 논문 정체성 | 진단자(diagnostician): 2가지 기여만 |

---

## 2. 핵심 2가지 기여 (확정)

1. **5-Domain Research Orientation Typology**: 97편의 체계적 분류 → 인식-측정 간극의 정량적 문서화
2. **Paradigm Reframing**: "Do learners trust AI?" → "Is their trust calibrated?" — Trust-AI Reliability Matrix를 진단 도구(heuristic)로 제시

삭제 또는 분리:
- 6개 스캐폴드 상세 → 후속 논문
- 적응적 교정 사이클 → 후속 논문
- 5개 설계 원칙 → 삭제
- 2-수준 프레임워크 상세 → 후속 논문
- Educational AI Reliability 조작화 → 미래 연구 언급만

---

## 3. 수정 원고 구조 (8,000 words)

### 3.1 섹션별 워드 예산

| # | 섹션 | 워드 | 핵심 내용 |
|---|------|------|----------|
| - | Abstract | 250 | 08번 재작성 초록 기반, SRL 브릿지 포함 |
| 1 | Introduction | 700 | Bastani hook + 수렴 증거, SRL→Trust Cal 브릿지, RQs |
| 2 | Conceptual Background | 800 | SRL calibration 출발 → Trust calibration → 프레임워크 한계 |
| 3 | Method | 600 | PRISMA 2020, 검색, 코딩, 신뢰도, 한계 |
| 4 | Results | 2,800 | 5-domain typology + calibration gap 통합 |
| 5 | Discussion | 1,800 | Reframing + Matrix + 학제간 분석 + 연구 아젠다 |
| 6 | Limitations | 500 | 50편 미코딩, 단일 시점, 측정 가능성 역설 |
| 7 | Conclusion | 300 | |
| | **합계** | **~7,750** | Figure caption/table 여유 ~250 words |

### 3.2 Figure/Table 예산

| # | 유형 | 내용 | 비고 |
|---|------|------|------|
| Fig 1 | PRISMA 2020 Flow | 검색 및 선정 과정 | SLR 필수 |
| Fig 2 | Bar chart | 5-domain 분포 + calibration threshold 점선 | 핵심 발견 (08번의 계단형은 비수용) |
| Fig 3 | 2×2 Matrix | Trust-AI Reliability Matrix + 교육 시나리오 | 개념적 기여 (08번 §5.2 시나리오 적용) |
| Table 1 | 비교표 | SRL Calibration vs Trust Calibration (10행) | 이론적 기여 압축 (08번 §5.3) |
| Table 2 | 분포표 | 5-domain 상세 (n, %, 핵심 특성, 대표 연구) | |
| Table 3 | 코딩표 | 코딩 변수 요약 | 보충자료 이동 가능 |

---

## 4. 섹션별 수정 지침

### 4.1 Abstract (250 words)

08번 §2.2의 재작성 초록을 기반으로 하되:
- "critical review" → "systematic review"로 변경
- "paradigm shift" → "reframing"으로 약화
- SRL calibration 브릿지 유지 (두 번째 문단)
- "96 studies in the automation field" → 문장 내 방법론적 한정 추가

### 4.2 Introduction (700 words)

**서사 아크 (09번 §2.1 기반):**

1. **Hook** (150w): Bastani et al. (2025) + 수렴 증거
   - Bastani 외에 추가: Anthropic (2025) cognitive offloading, Gerlich (2025) critical thinking decline, Vössing et al. (2024) overreliance
   - "이 패턴은 단일 연구가 아닌 수렴하는 증거"

2. **Bridge** (200w): SRL calibration → Trust calibration
   - 08번 §3.1: "Education researchers are deeply familiar with calibration..."
   - Trust calibration 정의: "the accuracy of learners' judgments about an AI system's capabilities, analogous to the SRL concept of calibration applied to self-knowledge (Winne & Hadwin, 1998; Lee & See, 2004)"

3. **Gap statement** (150w): 이 확장이 아직 이루어지지 않았다
   - "Despite this conceptual readiness, the educational AI literature has not yet made this extension"

4. **RQs** (200w): 교육학 네이티브 언어 (08번 §3.1 제안 반영)
   - RQ1: "What research orientations characterize the educational AI trust literature, and how do they distribute along a calibration maturity spectrum?"
   - RQ2: "To what extent does current research address trust calibration, and where does a calibration gap persist?"
   - RQ3: "What reframing is needed to advance trust calibration research in educational AI?"

### 4.3 Conceptual Background (800 words)

**순서 전환 (08번 §3.2 — "아는 것에서 모르는 것으로"):**

1. **SRL Calibration** (300w): 교육학 독자가 아는 개념에서 출발
   - Winne & Hadwin (1998), Nelson & Narens (1990), Stone (2000)
   - 과추정/과소추정, 메타인지적 모니터링
   - "30년간의 실증 연구가 calibration이 학업 성취의 강력한 예측 변수임을 확인"

2. **Trust Calibration** (300w): SRL에서 자연스럽게 확장
   - Lee & See (2004), Hoff & Bashir (2015)
   - Table 1: SRL vs Trust Calibration 비교표
   - 핵심 차이: 불확실성의 소재지 (self vs external system)
   - "structurally analogous" (NOT "isomorphic")
   - 추가 차이 명시: 정보 비대칭, 기준 대상 안정성, 피드백 구조

3. **기존 프레임워크의 한계** (200w)
   - TAM/UTAUT: "structural limitation" (NOT "lock-in") — trust를 최대화 대상으로만 봄
   - SRL 프레임워크: 외부 시스템에 대한 판단 미포함
   - "Neither tradition addresses calibration of trust in external AI systems"

### 4.4 Method (600 words)

**SLR 전환을 위한 핵심 변경:**

- **리뷰 유형 선언**: "This systematic review follows PRISMA 2020 guidelines (Page et al., 2021), combining structured coding with critical synthesis for theoretical integration."
- **검색 전략**: DB 3개, 검색어, 날짜 범위 (2015-2026)
- **선정 기준**: 포함/배제 기준 명시
- **코딩**: 32-field scheme 요약 (상세는 보충자료)
- **코더간 신뢰도**: "Two researchers independently coded a 20% subsample (n=20). Cohen's kappa was calculated for each critical variable (addresses_calibration, overtrust_discussed, undertrust_discussed)."
- **보충 검색**: 목적과 방법 투명하게 보고. "A supplementary citation tracking search targeted adjacent disciplines (human factors, HCI, cognitive science) to identify calibration-focused work that may not appear in educational databases."
- **분석 전략**: "Statistics are reported separately for the database corpus (n=81) and the full corpus including supplementary papers (n=97) to ensure transparency."
- **50편 미코딩 처리**: "Fifty papers could not be accessed in full text. Title/abstract screening of these papers identified [X] as potentially calibration-relevant, yielding a sensitivity estimate of [range]."

### 4.5 Results (2,800 words)

**구조:**

4.1 **Overview** (300w): 97편 개관, 연도 분포, 연구 유형
- 5-domain typology 소개: post-hoc derived variable임을 투명하게 명시
- "성숙도 여정" 은유를 **텍스트에서** 사용:
  - D1 = "Will learners adopt AI?"
  - D2 = "Does trust matter?"
  - D3 = "How should we design for trust?"
  - D4 = "Can trust go wrong?"
  - D5 = "Is trust actually accurate?"
- Table 2: 5-domain 분포표 + Fig 2

4.2 **D1-D3** (500w): 압축하여 한 소절로 통합
- 각 도메인의 핵심 특성만 기술

4.3 **D4: Trust Awareness** (500w): 최대 도메인으로 상세
- D4a/D4b/D4c 분포
- D4b > D4a 발견의 해석
- 56% 프레임워크 부재 → 인식은 있으나 도구가 없음

4.4 **D5: Trust Calibration** (400w)
- DB 3편 vs 보충 13편 분리 보고
- D5의 학제적 출처 비대칭

4.5 **Cross-cutting patterns** (400w)
- Pattern 1: 인식-측정 간극 (D4 42.3%, 프레임워크 없음 56%)
- Pattern 2: 학제간 단절 (Lee & See 86% in D5; SRL 0% in D5)
- Pattern 3: 비계 비대칭 (투명성 24.7% vs 메타인지 3.1%)
- Pattern 4: D5 출처 비대칭

4.6 **The Calibration Gap** (700w)
- Definitional dimension (84.5% 무정의)
- Measurement dimension (97→7→1→0 깔때기) — Table Y를 문장으로 통합:
  "Wischnewski et al. (2023), surveying studies in automation/HCI that simultaneously measured trust and system reliability, identified 96 such studies. In the present corpus, no study measured both variables simultaneously. This disparity indicates a disciplinary disconnection rather than a methodological impossibility."
- Disciplinary dimension (13/16 D5 from adjacent fields)

### 4.6 Discussion (1,800 words)

5.1 **The Required Reframing** (400w)
- "paradigm shift" 대신 "reframing" 사용
- "trust level" → "trust calibration"으로의 확장
- SRL 역사 비유: "자신감 측정 → 자신감 정확도 측정" 전환

5.2 **Trust-AI Reliability Matrix** (400w)
- Fig 3: 2×2 Matrix + 교육 시나리오
- Q1: Calibrated Use (역사적 사실 요약에 AI 활용)
- Q2: Uncalibrated Overtrust (수학 증명에 AI 무비판적 수용) — "Bastani Trap" → "Dangerous Overtrust Zone"
- Q3: Uncalibrated Undertrust (문법 교정 AI를 불필요하게 불신)
- Q4: Calibrated Avoidance (임상추론에서 AI를 신중하게 회피)
- 진단 도구(heuristic)로 위치시킴

5.3 **학제간 사각지대 분석** (300w)
- SRL-Trust Calibration 미연결: SRL 5편 중 D5 = 0편
- AI 리터러시(D3)와 Calibration(D5)의 단절
- "Calibration 개념에 가장 가까운 두 전통이 수렴하지 못하고 있다"

5.4 **Research Agenda** (400w) — 5개 우선순위
- Priority 1: 동시 측정 연구 (검증 가능한 과제에서 시작)
- Priority 2: 측정 도구 개발 (과제-수준 trust calibration 척도)
- Priority 3: 교정 개입 설계 (메타인지적 프롬프팅, 생산적 실패)
- Priority 4: 종단 연구 (trust calibration 발달 궤적)
- Priority 5: 학제간 통합 (SRL + trust-in-automation)

5.5 **Practical Implications** (300w)
- 교육자: 도메인별 AI 성능 차이를 가르치기
- 설계자: 투명성 + 메타인지 비계 병행
- 정책: EU AI Act, UNESCO 가이드라인과의 연결

### 4.7 Limitations (500 words)

1. 50편 미코딩 (민감도 분석 결과 보고)
2. 단일 시점 스냅샷 (72% 2025-2026 논문)
3. 보충 검색의 selection effect (통계 분리 보고로 완화)
4. AI reliability 측정 가능성 스펙트럼 (수학/코딩 = 높음, 에세이 = 낮음)
5. "가장 필요한 곳에서 가장 어렵다"는 역설 → 연구 로드맵으로 전환

### 4.8 Conclusion (300 words)

- 핵심 발견 요약 (83.5%, 0 동시 측정, 학제간 단절)
- Reframing 요약
- "This review provides the diagnostic foundation; the empirical work remains to be done."

---

## 5. 용어 수정 목록

| 현재 | 수정 | 이유 |
|------|------|------|
| "critical review" | "systematic review with critical synthesis" | C&E 적합성 |
| "paradigm shift" | "reframing" / "extension" | 과대 주장 방지 |
| "TAM lock-in" | "structural limitation" | 허수아비 논증 방지 |
| "isomorphic" | "structurally analogous" | SRL 전문가 반발 방지 |
| "Bastani Trap" | "Dangerous Overtrust" / "Uncalibrated Overtrust" | 단일 연구 과대 부각 방지 |
| "operationalized through the Matrix" | "illustrated through the Matrix" | Matrix가 아직 경험적 검증 안 됨 |

---

## 6. 보충자료 (Supplementary Materials)

C&E에 함께 제출:
1. PRISMA 2020 체크리스트
2. 전체 코딩 스키마 (32-field)
3. 코더간 신뢰도 상세 결과
4. 97편 전체 코딩 결과표
5. 5-domain 분류 규칙 및 검증 결과
6. 50편 미코딩 논문 title/abstract 스크리닝 결과
7. 민감도 분석 결과

---

## 7. 수정 작업 순서

### Phase 0: 선행 작업 (코딩/분석)
- [ ] 2차 코더 확보 및 20% 서브샘플 코딩
- [ ] 50편 미코딩 논문 title/abstract 스크리닝
- [ ] 민감도 분석 수행
- [ ] Cohen's kappa 계산

### Phase 1: 구조 재편 (draft.md)
- [ ] 현재 Section 5의 6개 스캐폴드/적응적 사이클/설계 원칙 삭제
- [ ] Section 2 재순서화 (SRL first)
- [ ] Section 4와 5 통합 (Results로)
- [ ] Section 3 (Method) SLR 형식으로 전환

### Phase 2: 내용 수정
- [ ] Abstract 재작성 (08번 기반)
- [ ] Introduction에 수렴 증거 추가 + SRL 브릿지
- [ ] Table Y → 문장 전환
- [ ] Table 1 (SRL vs Trust Cal 비교표) 삽입
- [ ] Fig 3 (Matrix)에 교육 시나리오 추가
- [ ] 용어 교체 (6개 항목)
- [ ] DB(n=81) vs 보충(n=16) 통계 분리

### Phase 3: 검증 및 마무리
- [ ] Figure/Table 번호 재정렬
- [ ] 워드 카운트 확인 (8,000 이하)
- [ ] 내부 일관성 재점검
- [ ] References 업데이트 (Stone 2000, PRISMA 2020 등)
- [ ] PRISMA 2020 체크리스트 작성
- [ ] 보충자료 패키징
- [ ] draft.md → docx 재생성

---

## 8. 예상 비판 대응표 (최종)

| # | 예상 비판 | 대응 전략 |
|---|----------|----------|
| 1 | "50편 미코딩으로 통계 불확실" | 민감도 분석 + title/abstract 스크리닝 결과 보고 |
| 2 | "코더간 신뢰도 없음" | 20% 서브샘플 2차 코딩 완료 + kappa 보고 |
| 3 | "96 vs 0 비교 불공정" | 문장으로 전환 + 방법론적 한정 + "가능성의 증거"로 프레이밍 |
| 4 | "보충 논문이 통계 왜곡" | DB/보충 분리 보고 |
| 5 | "Bastani 단일 의존" | 수렴 증거 4-5편 추가 |
| 6 | "TAM 비판이 허수아비" | "structural limitation" + 49.5% 무프레임워크를 더 큰 문제로 부각 |
| 7 | "유형론이 post-hoc" | 투명하게 보고 + 도출 규칙 명시 + 재현 가능성 강조 |
| 8 | "SRL-Trust 독립성 미검증" | "structurally analogous" + 차이점 명시 + 경험적 검증 필요성 인정 |
| 9 | "패러다임 전환 과대" | "reframing" / "extension"으로 약화 |
| 10 | "프레임워크 검증 불가" | 진단적 기여로 한정 + 연구 아젠다로 전환 |

---

*이 문서는 01-09번 discussion과 Diverga G1/A3/F1 에이전트 분석의 종합이며, C&E 투고를 위한 최종 수정 전략입니다.*
*Phase 0(코더간 신뢰도, 민감도 분석) 완료 후 Phase 1-3 수정 작업을 진행합니다.*
