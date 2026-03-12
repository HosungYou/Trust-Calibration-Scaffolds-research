# 패널 데이터셋 구조 비교: T × R × τ 모델 검증용

**Date:** 2026-03-11
**Context:** 주요 후보 데이터셋의 데이터 구조 상세 조사 결과

---

## 최종 비교표

| 기준 | Pew ATP | EdNet KT3 | ASSISTments 2012-13 | LISS | GSOEP |
|------|---------|-----------|---------------------|------|-------|
| **True Panel?** | ✅ YES (`QKEY`) | ✅ YES (per-student file) | ✅ YES (`user_id`) | ✅ YES | ✅ YES |
| **N** | ~3,600-11,200/wave | 297,915 students | 27,066 students | ~7,500 | ~30,000 |
| **AI Trust 직접 측정** | ✅ YES (concern/excitement) | ❌ NO (behavioral proxy) | ❌ NO (behavioral proxy) | △ 단일 wave만 | △ 불확실 |
| **반복 측정 횟수** | 5+ waves (2021-2025) | 평균 441 interactions/student | 평균 94 problems/student | 1회 (AI 모듈) | 확인 필요 |
| **시간 범위** | 4년 (2021-2025) | 1년 3개월 | 1학년 (9월-6월) | - | - |
| **교육 맥락** | ❌ 일반 대중 | ✅ AI 튜터링 (TOEIC) | ✅ 수학 ITS | ❌ | ❌ |
| **무료 다운로드** | ✅ (등록 후) | ✅ (즉시) | ✅ (즉시) | ✅ (등록 후) | ❌ 계약 필요 |
| **한국 맥락** | ❌ 미국 | ✅ 한국 학습자 | ❌ 미국 | ❌ 네덜란드 | ❌ 독일 |

---

## 1순위: Pew American Trends Panel (ATP)

### 핵심 발견: 개인 수준 AI 신뢰 궤적 분석 가능!

- **`QKEY`** 변수가 모든 wave에 걸쳐 동일 응답자를 추적
- **종단 가중치** 제공 (예: `WEIGHT_W80_W84`)
- 핵심 AI 질문이 **동일 문항으로 5회 이상 반복:**

> "Thinking about the increased use of artificial intelligence in daily life, would you say you feel more excited than concerned, more concerned than excited, or an equal mix of excitement and concern?"

**반복 측정 wave:**

| Wave | 시기 | N | AI 주제 |
|------|------|---|---------|
| Wave 99 | 2021.11 | 10,260 | AI concern/excitement, 얼굴인식, 자율주행 |
| Wave 119 | 2022.12 | 11,004 | AI concern/excitement, AI awareness 6문항 척도 |
| Wave 132 | 2023.8 | 11,201 | AI concern/excitement (52% concerned) |
| Wave 152 | 2024.8 | 5,410 | AI concern/excitement, AI risks/regulation |
| Wave 173 | 2025.6 | 5,023 | AI concern/excitement, 사회적 영향 |

**추가 AI 질문:** AI 규제 신뢰, ChatGPT 인식, 직장 AI 영향, AI 도메인별 태도 (의료, 자율주행, 채용 등)

**인구통계:** 연령, 성별, 인종, 교육, 소득, 정당, 종교, 지역 — 모두 wave 간 일관

**T × R × τ 매핑:**
- T = AI concern/excitement (개인 수준 태도 변화)
- R = AI에 대한 인식/지식 수준 (AI awareness scale, Wave 119)
- τ = Wave (2021 → 2022 → 2023 → 2024 → 2025)

**분석 가능성:**
1. `QKEY`로 5개 wave 병합 → 개인별 AI 신뢰 궤적 추출
2. Latent Class Growth Analysis → 궤적 유형 분류
3. 인구통계 변수 → 궤적 유형 예측
4. 2023년 ChatGPT 충격 전후 개인 수준 변화 분석

**주의사항:**
- 모든 panelist가 모든 wave에 응답하지는 않음 → 다수 wave 참여자 부분집합 식별 필요
- 종단 가중치가 모든 wave 조합에 제공되지 않을 수 있음
- 3점 척도 (excited/mixed/concerned) → 세밀한 변이 포착 제한

---

## 2순위: EdNet KT3 (한국 AI 튜터링)

### 데이터 구조 상세

**형식:** 학생당 1 CSV 파일, 297,915개 파일, 4.3GB uncompressed
**다운로드:** Google Drive (bit.ly/ednet-kt3), 로그인 불필요

**KT3 스키마:**

| 컬럼 | 설명 |
|------|------|
| `timestamp` | Unix ms (프라이버시를 위해 고정값 이동, 상대 순서 보존) |
| `action_type` | `enter`, `respond`, `submit`, `quit` |
| `item_id` | `q{int}` (문제), `e{int}` (해설), `l{int}` (강의) |
| `source` | `sprint`, `tutor`, `adaptive_offer`, `todays_recommendation` 등 |
| `user_answer` | a-d |
| `platform` | `mobile` / `web` |

**Trust/Reliance Proxy 구성 방법:**

| Proxy | 구성 방법 | Trust Calibration 해석 |
|-------|---------|----------------------|
| **해설 열람률** | `e{int}` enter/quit 빈도 + 체류 시간 | 정답 후 해설 건너뜀 = 높은 자신감; 오답 후 해설 안 봄 = 과신 |
| **답변 변경 횟수** | 동일 문제 내 `respond` 반복 수 | 높으면 불확실/저신뢰 |
| **시스템 추천 수용률** | `source = adaptive_offer` 따라가기 비율 | AI 추천 수용도 = 직접적 reliance 측정 |
| **응답 시간** | `elapsed_time` | 빠른 정답 = 높은 자신감; 느린 응답 = 숙고 |
| **강의 소비** | `l{int}` enter/quit | 자발적 학습 = 적극적 calibration |

**한계:**
- 자기보고 trust/confidence 없음 (행동 proxy만)
- 문항 내용 비공개 (ID만 제공)
- Skill tag 의미 비공개 (293개 태그, 명칭 없음)
- 인구통계 없음
- 한국 TOEIC 맥락

---

## 3순위: ASSISTments 2012-13 (수학 ITS + Affect)

### 데이터 구조 상세

**다운로드:** Google Drive (~659 MB), 즉시 가능
**규모:** 27,066 students, 2,541,201 interactions, 1 school year

**핵심 변수:**

| 변수 | 설명 |
|------|------|
| `user_id` | 학생 고유 ID |
| `correct` | 첫 시도 정답 여부 (1/0) |
| `hint_count` | 요청한 힌트 수 |
| `hint_total` | 해당 문제의 최대 힌트 수 |
| `first_action` | 0=시도, 1=힌트 요청, 2=scaffolding |
| `bottom_hint` | 정답 힌트까지 도달 여부 (1/0) |
| `attempt_count` | 답변 제출 횟수 |
| `ms_first_response` | 첫 행동까지 시간 (ms) |
| `skill_id` / `skill_name` | Knowledge component |
| `opportunity` | 해당 skill 누적 연습 횟수 |
| `start_time` / `end_time` | 타임스탬프 |
| **`Avg_confidence(FRUSTRATED)`** | 좌절감 예측 (0-1) |
| **`Avg_confidence(CONFUSED)`** | 혼란 예측 (0-1) |
| **`Avg_confidence(CONCENTRATING)`** | 집중 예측 (0-1) |
| **`Avg_confidence(BORED)`** | 지루함 예측 (0-1) |

**Affect 측정 방식:** 자기보고 아님! BROMP 프로토콜로 교실 관찰 → ML 모델 훈련 → 전체 데이터에 예측값 적용 (A' ~0.63-0.68)

**Trust Proxy 매핑:**

| ASSISTments 패턴 | Trust Calibration 해석 |
|-----------------|----------------------|
| Low hint + correct | 적절한 자기 의존 (calibrated) |
| Low hint + incorrect | AI 도움 부족 의존 (overconfidence) |
| High hint + learning gain | 적절한 AI 의존 |
| Bottom-hint + no learning | 과도한 AI 의존 (cognitive offloading) |
| first_action=1 (즉시 힌트) | 과신뢰 (즉시 AI에 의존) |

**한계:**
- Hint은 학생 주도(pull) ≠ AI 추천(push) 모델
- 자기보고 confidence 없음
- Affect 예측 정확도 중간 수준
- Skill tags 16% 결측

---

## 패널 서베이 결과 (부적합 판정)

### LISS Panel (네덜란드)
- True panel이지만 AI trust 모듈이 **단일 wave만** 시행됨
- AI trust 종단 분석 **불가**
- 향후 새 모듈 제안은 가능 (assembled study)

### Harvard GenAI Market Pulse (한국)
- Likely **repeated cross-section** (quota sampling)
- 2 waves only (2026.1, 2026.2)
- 개인 수준 추적 **불가**

### Understanding Society (UK)
- True panel이지만 AI/trust 문항 **없음**
- 기기 사용 + 인터넷 활동만

### GSOEP (독일)
- Digitalization module (2020~) 있으나 반복 여부 불확실
- 데이터 접근에 계약 필요
- Trust in predictive analytics (2018) = SOEP-IS 단일 시행

### OECD Trust Survey
- Repeated cross-section, AI 문항 1개만
- 개인 수준 추적 **불가**

---

## 최종 추천

### 선생님의 연구 맥락에 최적인 조합:

**Option A: Pew ATP (AI 신뢰 태도 궤적)**
- 장점: 유일하게 동일 개인의 AI 신뢰 변화를 5개 시점에서 추적 가능
- 분석: LCGA로 궤적 유형 분류 → convergent/oscillating/stagnant 패턴 검증
- 논문 기여: "미국 성인의 AI 신뢰가 2021-2025 사이 어떤 궤적 유형으로 분화되는가?"

**Option B: EdNet KT3 (AI 튜터링 의존도 궤적)**
- 장점: 한국 맥락, 교육 AI, 대규모, 행동 데이터
- 분석: System recommendation compliance trajectory → AI 의존도 변화 패턴
- 논문 기여: "AI 튜터링에서 학습자의 시스템 의존도가 시간에 따라 어떤 궤적을 보이는가?"

**Option C: 두 데이터셋 병용**
- Pew ATP = macro-level (사회적 AI 신뢰 궤적)
- EdNet KT3 = micro-level (개인 AI 의존도 궤적)
- 다중 수준에서 T × R × τ 모델의 일반화 가능성 검증

---

## 참고문헌

### Pew ATP
- Pew Research Center. ATP Codebook and Instructions. https://www.pewresearch.org/wp-content/uploads/2018/05/Codebook-and-instructions-for-working-with-ATP-data.pdf
- Growing Public Concern About AI. Aug 28, 2023.
- How the US Public and AI Experts View AI. Apr 3, 2025.
- AI Impact on People and Society. Sep 17, 2025.

### EdNet
- Choi, Y., et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. AIED 2020. https://arxiv.org/abs/1912.03072

### ASSISTments
- San Pedro, M. O. Z., Baker, R., Gowda, S., & Heffernan, N. (2013). Predicting Student Affect.
- Aleven, V., Roll, I., McLaren, B., & Koedinger, K. (2016). Help Helps, But Only So Much. IJAIED, 26(1), 205-223.
