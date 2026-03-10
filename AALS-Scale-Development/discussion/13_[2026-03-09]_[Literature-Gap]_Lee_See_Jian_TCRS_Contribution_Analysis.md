# Lee & See (2004), Jian et al. (2000), and TCRS Contribution Analysis

**Date:** 2026-03-09
**Context:** Analysis based on Wischnewski et al. (2023) CHI survey of 96 trust calibration studies

---

## 1. Lee & See (2004) Summary

Lee & See (2004) is the most influential theoretical framework paper in trust in automation.

**Key Definitions:**
- **Trust:** "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 54)
- **Trust Calibration:** "how well trust matches the true capabilities of the automation" (p. 57)

**Three factors determining calibration:**
1. **Performance:** What the automation does — reliability, predictability
2. **Process:** How the automation operates — algorithm transparency
3. **Purpose:** Why the automation was created — designer intent

**Critical limitation:** This is a PURELY THEORETICAL FRAMEWORK. It defines trust calibration and argues for its importance, but provides NO measurement instrument. It establishes "what should be" (trust should match capabilities) without offering tools to assess whether individuals are READY to achieve this alignment.

---

## 2. Jian et al. (2000) Summary

Jian et al. (2000) Trust in Automation Scale is the most widely used trust measurement instrument. Per Wischnewski et al. (2023), 16 of 96 studies (17%) used this scale.

**Scale characteristics:**
- 12-item self-report scale
- Measures trust LEVEL — "I trust this system" type items
- 7-point Likert scale

**Critical limitation:** Measures the AMOUNT of trust, not whether trust is CALIBRATED. Example:
- A user reports 7/7 trust → is this appropriate calibration (highly reliable system) or overtrust (unreliable system)?
- Calibration assessment requires comparing subjective trust + objective reliability; Jian's scale only measures the subjective side

---

## 3. Current Trust Calibration Measurement Practices (Wischnewski et al., 2023)

Current researchers measure trust calibration as:

> "statistical differences of trustworthiness perceptions of systems with high reliability and trustworthiness perceptions of systems with low-reliability groups"

This is GROUP-LEVEL measurement through experimental manipulation:
1. Expose participants to both high-reliability and low-reliability AI
2. Collect trust scores for each
3. Large difference = "calibrated"; small difference = "not calibrated"

**Problems with this approach:**
- Only confirms ORDINAL matching — "do you trust the more reliable system more?"
- Cannot capture INDIVIDUAL-LEVEL calibration processes
- Cannot explain calibration MECHANISMS (how and why calibration occurs)
- Wischnewski et al.'s own conclusion: "the measurement of the trust calibration often limits the interpretation of the effects of different interventions"

**Additional concepts from the survey:**
- Trust sensitivity (Merritt et al.): "reflects the extent to which a user's trust changes as the automation's actual reliability level changes"
- Four calibration dimensions: (1) exo vs endo, (2) warranted vs unwarranted, (3) static vs adaptive, (4) capabilities vs process-oriented

---

## 4. TCRS's Contribution: Bridging Three Gaps

### Gap 1: Theory → Measurement

| Dimension | Lee & See (2004) | Jian et al. (2000) | Current Methods | **TCRS** |
|-----------|------------------|---------------------|-----------------|----------|
| Provides | Calibration DEFINITION | Trust LEVEL | Calibration OUTCOME | Calibration READINESS |
| Level | Conceptual | Individual | Group | **Individual** |
| Measures calibration? | ✗ (definition only) | ✗ (trust only) | △ (ordinal) | **○ (process)** |
| Self-report? | N/A | ○ | △ (indirect) | **○ (direct)** |

### Gap 2: Outcome → Process

Current research only sees the RESULT (calibrated/not). TCRS decomposes the PROCESS into 3 stages:

- **CA-Aw (Calibration Awareness):** Ability to RECOGNIZE the relationship between one's trust level and AI's actual reliability
- **CA-Jd (Calibration Judgment):** Ability to EVALUATE the trust–reliability gap
- **CA-Ac (Calibration Action):** Ability to ADJUST behavior to reduce the gap

All three subscales maintain DUAL-REFERENT structure — referencing BOTH trust (subjective) AND AI reliability (objective).

### Gap 3: Group-Level → Individual-Level

Current calibration measurement requires experimental manipulation of system reliability across groups. TCRS enables individual-level assessment without experimental manipulation — practical for educational settings.

### Predictive Validity Criterion

TCRS measures readiness (process model stages 1-3). Calibration accuracy (stage 4: trust = reliability) is what TCRS should PREDICT.

> **Empirical test:** Do higher TCRS scores predict better trust-reliability correspondence?

This connects Lee & See's theoretical definition to empirical measurement.

---

## 5. Manuscript Integration Recommendation

**Wischnewski et al. (2023) should be cited in the manuscript at minimum 3 locations:**

1. **Literature Review (existing trust measures section):** Jian et al. as most-used trust scale (16/96 studies), but measures trust level not calibration
2. **Introduction or Theoretical Framework (gap argument):** Current field measures calibration at group level through experimental manipulation; no individual-level self-report instrument exists; "measurement often limits interpretation of intervention effects"
3. **Discussion (contribution):** TCRS addresses the measurement limitation identified by Wischnewski et al.'s systematic survey

---

## 6. Key References

- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. Human Factors, 46(1), 50-80.
- Jian, J. Y., Bisantz, A. M., & Drury, C. G. (2000). Foundations for an empirically determined scale of trust in automated systems. International Journal of Cognitive Ergonomics, 4(1), 53-71.
- Wischnewski, M., Krämer, N., & Müller, E. (2023). Measuring and understanding trust calibrations for automated systems: A survey of the state-of-the-art and future directions. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (pp. 1-16). ACM.
- Merritt, S. M., Heimbaugh, H., LaChapell, J., & Lee, D. (2013). I trust it, but I don't know why: Effects of implicit attitudes toward automation on trust in an automated system. Human Factors, 55(3), 520-534.
