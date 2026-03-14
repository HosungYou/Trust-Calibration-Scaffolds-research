# Pew ATP vs EdNet KT3: 병렬 탐색 최종 종합

**Date:** 2026-03-11
**Context:** 두 데이터셋의 실제 구조를 병렬 탐색한 결과 종합

---

## 1. Pew ATP 탐색 결과

### 1.1 포털 현황
- **URL:** pewresearch.org/internet/datasets/
- **접근:** 무료 계정 생성 후 다운로드 (SPSS/CSV)
- **포털 게시 현황:** Wave 160 (2025.1)까지 공개, Wave 166/173은 미공개
- **Topline PDF:** 로그인 없이 공개 접근 가능

### 1.2 AI Trust 핵심 변수 (Wave별)

| Wave | 시기 | 핵심 AI 변수 | N |
|------|------|-------------|---|
| **Wave 99** | 2021.11 | `CNCEXC_W99` (concern/excitement), 얼굴인식, 자율주행 | 10,260 |
| **Wave 119** | 2022.12 | `CNCEXC_W119`, `AI_HEARD_W119`, `USEAI_W119`, `AIKNOW1-7_W119` (6문항 AI 인식 척도) | 11,004 |
| **Wave 132** | 2023.8 | `CNCEXC_W132` (52% concerned), ChatGPT 인식 | 11,201 |
| **Wave 152** | 2024.8 | `CNCEXC_W152`, `AICONTROL1/2`, `TRSTAIPRS`, `AICONCERN_a-g` (7개 도메인) | 5,410 |
| **Wave 173** | 2025.6 | `CNCEXC_W173`, 사회적 영향 | 5,023 |

### 1.3 핵심 반복 측정 문항

**CNCEXC (AI Concern/Excitement) — 5개 wave 반복:**
> "Thinking about the increased use of artificial intelligence in daily life, would you say you feel more excited than concerned, more concerned than excited, or an equal mix of excitement and concern?"

**응답 척도:** 3점 (More excited / Equal mix / More concerned)

### 1.4 추가 AI 문항 (Wave 152 — 가장 풍부)
- `TRSTAIPRS`: AI 기업 신뢰도
- `AICONTROL1/2`: AI 통제 가능성 인식
- `AICONCERN_a-g`: 7개 도메인별 AI 우려 (의료, 채용, 자율주행, 감시 등)
- `AIJOBS`: AI 직장 영향
- `AIREGULATION`: AI 규제 태도

### 1.5 개인 추적 메커니즘
- **`QKEY`**: 모든 wave에 걸친 고유 응답자 ID
- **종단 가중치**: `WEIGHT_W{a}_W{b}` 형식으로 특정 wave 쌍에 제공
- **인구통계**: 연령, 성별, 인종, 교육, 소득, 정당, 종교, 지역 — wave 간 일관

### 1.6 T × R × τ 매핑 평가

| 차원 | 매핑 | 평가 |
|------|------|------|
| **T (Trust)** | CNCEXC (3점 concern/excitement) | ⚠️ 3점 척도 → 변이 제한, 그러나 5개 시점 반복 |
| **R (Reliability)** | 없음 (AI 성능 직접 측정 없음) | ❌ AI 시스템 성능을 직접 경험하지 않음 |
| **τ (Time)** | Wave (2021→2022→2023→2024→2025) | ✅ 4년간 5개 시점 |

**핵심 한계:** R(AI Reliability) 차원이 부재. 이것은 "AI에 대한 일반적 태도 변화"이지, "특정 AI 시스템 성능에 대한 신뢰 교정" 연구가 아님. T × R × τ 모델의 핵심인 "시스템 성능(R)에 따른 신뢰(T) 교정"을 직접 검증할 수 없음.

**가능한 분석:**
- AI 태도 궤적 유형 분류 (LCGA) → 궤적 패턴은 검증 가능
- ChatGPT 출시(2022.11) 전후 개인 수준 태도 변화 → 외적 충격 효과
- 인구통계 변수 → 궤적 유형 예측

---

## 2. EdNet KT3 탐색 결과

### 2.1 실제 데이터 다운로드 완료

**저장 경로:** `/Volumes/External SSD/Projects/_Data/EdNet/`

| 파일 | 내용 | 크기 |
|------|------|------|
| `EdNet-Contents.zip` | 메타데이터 (questions, lectures, skills) | — |
| `questions.csv` | 13,169 문항 × 4 선택지 | — |
| `lectures.csv` | 1,021 강의 (189 skill tags) | — |
| `kt3_sample_2000.csv` | KT3 원시 데이터 2,000행 샘플 | — |
| `kt3_u562823.csv` | 학생 1명 전체 원시 데이터 (1,771 actions) | — |
| `kt3_u562823_episodes.csv` | 파싱된 334 문제풀이 에피소드 | — |
| `kt3_u562823_trajectory.csv` | 윈도우 기반 Trust/Reliance 궤적 (33개 시점) | — |

### 2.2 KT3 스키마 (실제 확인)

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `timestamp` | Unix ms (상대 순서 보존) | 1554889227015 |
| `action_type` | enter, respond, submit, quit | respond |
| `item_id` | q{int} (문제), e{int} (해설), l{int} (강의) | q4091 |
| `source` | sprint, tutor, adaptive_offer 등 | sprint |
| `user_answer` | a-d | b |
| `platform` | mobile / web | mobile |

### 2.3 Trust Proxy 실제 측정 결과 (학생 u562823)

**334 에피소드, 5.6일간 학습 궤적:**

| 궤적 단계 | 정확도 | 해설 열람 시간 | adaptive_offer | 해석 |
|-----------|--------|-------------|----------------|------|
| 초기 (ep 1-50) | 0.68-0.86 | 7-22초 | 0% | 빠른 해설 확인, 자기 주도적 |
| 중기 (ep 100-200) | 0.52-0.80 | 40-116초 | 0-10% | 해설 깊이 읽기 시작, 어려운 문제 직면 |
| 후기 (ep 200-300) | 0.55-0.85 | 32-96초 | 15-30% | AI 추천 수용 증가, 강의 활용 |
| 말기 (ep 300-334) | 0.72-0.81 | 67-96초 | 0-15% | 안정화 |

**핵심 발견:**
- **해설 열람 시간 3배 증가**: 초기 ~20초 → 중기 ~80초 (더 깊은 처리)
- **adaptive_offer 출현**: Episode 200 이후 급증 (6.4% → 최대 30%)
- **adaptive_offer compliance = 100%**: 이 학생은 AI 추천을 항상 수용
- **강의 소비**: 중후기부터 자발적 강의 시청 시작

### 2.4 분석 가능 규모

| 기준 | 수 |
|------|---|
| 전체 학생 수 | 297,915 |
| 50+ 상호작용 학생 | ~86,700 (29%) |
| 100+ 상호작용 학생 | ~52,000 (추정) |
| 평균 상호작용/학생 | 441 |

### 2.5 T × R × τ 매핑 평가

| 차원 | 매핑 | 평가 |
|------|------|------|
| **T (Trust/Reliance)** | adaptive_offer compliance, 해설 열람 패턴, 답변 변경 | ⚠️ 행동 proxy (자기보고 아님), 그러나 직접적 AI 의존도 |
| **R (Reliability)** | AI 추천 정확도 × 학습자 정답률 | ✅ 문제별 정답/오답 피드백 존재 |
| **τ (Time)** | Episode sequence (1-334+) | ✅ 수백 개 시점, 고해상도 |

**핵심 강점:** T × R × τ 세 차원 모두 매핑 가능. AI 시스템과의 실제 상호작용에서 발생하는 신뢰 교정 과정을 관찰.

---

## 3. 직접 비교

| 기준 | Pew ATP | EdNet KT3 |
|------|---------|-----------|
| **T × R × τ 3차원 매핑** | T, τ만 가능 (R 부재) | **T, R, τ 모두 가능** |
| **Trust 측정** | 자기보고 3점 척도 | 행동 proxy (AI 추천 수용률) |
| **시간 해상도** | 5개 시점 (연 단위) | 수백 시점 (분 단위) |
| **N** | ~3,600-11,200/wave | 86,700+ (50+ 상호작용) |
| **AI 시스템 직접 경험** | ❌ 일반적 태도 | ✅ AI 튜터와 실제 상호작용 |
| **교육 맥락** | ❌ | ✅ TOEIC AI 튜터링 |
| **한국 맥락** | ❌ 미국 | ✅ 한국 |
| **인구통계** | ✅ 풍부 | ❌ 없음 |
| **분석 난이도** | 낮음 (구조화된 서베이) | 중간 (raw log 전처리 필요) |
| **궤적 유형 분류** | LCGA (5 시점, 3점 척도) | GMM/LCGA (수백 시점, 연속 변수) |
| **논문 기여도** | 사회적 AI 태도 변화 | **AI 시스템과의 신뢰 교정 역학** |

---

## 4. 최종 추천

### EdNet KT3가 T × R × τ 모델 검증에 더 적합한 이유

1. **R 차원 존재**: Pew ATP의 치명적 한계는 AI Reliability(R) 차원 부재. 응답자는 특정 AI 시스템을 사용하지 않으므로, "시스템 성능 변화에 따른 신뢰 교정"이라는 모델의 핵심 메커니즘을 검증할 수 없음.

2. **시간 해상도**: 5개 연간 시점 vs 수백 개 에피소드. Trust calibration은 분-시간 단위의 미세 역학이 중요.

3. **교육 맥락 직결**: 선생님의 연구 프로그램이 "교육에서의 AI Trust Calibration"이므로, AI 튜터링 데이터가 직접적.

4. **한국 맥락**: 국내 학습자 데이터로 문화적 맥락 관련성 높음.

### 그러나 두 데이터셋 병용이 가장 강력

| 분석 수준 | 데이터셋 | 역할 |
|-----------|---------|------|
| **Micro (개인-AI 상호작용)** | EdNet KT3 | T × R × τ 궤적 유형 직접 검증, GMM으로 convergent/oscillating/stagnant 분류 |
| **Macro (사회적 태도)** | Pew ATP | AI 태도 궤적 유형 보조 검증, 사회적 맥락에서의 일반화 가능성 |

### 권장 분석 전략

**Phase 1: EdNet KT3 — 핵심 검증 (우선)**
1. HuggingFace에서 KT3 전체 다운로드 (4.3GB)
2. 50+ 에피소드 학생 ~86,700명 필터링
3. Trust proxy 변수 생성:
   - `adaptive_compliance`: AI 추천 수용률 (rolling window)
   - `explanation_depth`: 해설 체류 시간 (정규화)
   - `self_reliance`: 독립 풀이 vs AI 의존 비율
4. Growth Mixture Modeling → 궤적 유형 수 및 패턴 결정
5. Guo & Yang (2021)의 3 유형과 비교

**Phase 2: Pew ATP — 보조 검증 (선택)**
1. Pew 계정 생성 후 Wave 99, 119, 132, 152 다운로드
2. QKEY로 4개 wave 병합 → 다수 wave 참여자 식별
3. CNCEXC 궤적 LCGA → 유사 패턴 확인
4. 인구통계 변수 → 궤적 예측 모델

**Phase 3: TIER 1 실험 데이터 — 교차 검증 (선택)**
- Rittenberg et al. (2024): 30-point trust trajectory, N=147
- Zouhar et al. (2023): 56-trial betting data, N=332
- 이들은 통제된 실험 환경에서의 "gold standard" 검증

---

## 5. EdNet KT3 전체 다운로드 정보

### 다운로드 옵션

**Option A: Google Drive (원본)**
- URL: bit.ly/ednet-kt3
- 크기: ~0.8 GB compressed, 4.3 GB uncompressed
- 형식: 297,915개 CSV 파일 (학생당 1 파일)

**Option B: HuggingFace (미러)**
- URL: huggingface.co/datasets/riiid/ednet
- 형식: Parquet (더 효율적 접근)
- 장점: `datasets` 라이브러리로 프로그래매틱 접근

### 필요한 보조 파일
- `questions.csv`: 13,169 문항 × 4 선택지 (정답 포함)
- `lectures.csv`: 1,021 강의 × skill tags
- Skill tag 매핑: 189개 태그 (명칭 비공개, ID만)

---

## 참고

### 샘플 궤적 시각화 데이터 (학생 u562823)

해설 열람 시간 변화 (초):
```
초기:  21 → 19 → 14 → 8 → 16 → 18 → 19 → 28 → 34 → 31
중기:  24 → 39 → 83 → 116 → 78 → 40 → 42 → 42 → 74
후기:  90 → 72 → 71 → 58 → 35 → 35 → 32 → 34 → 58 → 77
말기:  67 → 83 → 96
```

adaptive_offer 비율 변화:
```
초기:  0% → 0% → 10% → 10% → 0% → 0% → 10% → 10% → 0% → 0%
중기:  0% → 0% → 0% → 0% → 0% → 0% → 0% → 10% → 10%
후기:  10% → 30% → 20% → 20% → 30% → 20% → 15% → 15% → 10% → 0%
말기:  0% → 0% → 15%
```

이 학생은 후기에 AI 추천 수용이 급증하는 패턴 → "Convergent" 유형의 가능성

---

## 참고문헌

- Choi, Y., et al. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. *AIED 2020*.
- Pew Research Center. American Trends Panel. https://www.pewresearch.org/
- Guo, Y., & Yang, X. J. (2021). Modeling and predicting trust dynamics in human-robot teaming. *IJSR*, 12, 459-478.
- Chung, S., & Yang, X. J. (2024). Predicting trust dynamics with personal characteristics. *HFES*, 68(1).
