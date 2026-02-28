---
title: "Terminology Decisions and Rationale"
date: 2026-02-28
status: finalized
---

# Terminology Decisions and Rationale

**Project:** Trust Calibration as the Missing Link in Educational AI Design
**Date:** 2026-02-28
**Status:** Finalized

---

## Overview

This document records all terminology decisions made for the manuscript, documentation, and visualizations associated with this project. Terminology decisions were made on the basis of three criteria: (1) grounding in established educational research literature; (2) theoretical accuracy relative to the constructs being described; and (3) consistency with the paper's conceptual framework and target journal conventions.

All decisions recorded here are binding across the manuscript, all supplementary documentation in this repository, and all figures and visualizations. Where prior versions of project materials use deprecated terms, the deprecated terms are preserved only in discussion documents as part of the historical record.

---

## 1. Primary Terminology Change: "Checkpoint" to "Trust Calibration Scaffold"

### 1.1 The Change

**Deprecated term:** Checkpoint (and related compound forms: checkpoint mechanism, checkpoint intervention, checkpoint design)

**Replacement term:** Trust Calibration Scaffold (and related compound forms: trust calibration scaffold mechanism, trust calibration scaffold intervention, trust calibration scaffold design)

### 1.2 Rationale for Deprecating "Checkpoint"

**Origin problem:** The term "checkpoint" originates in gaming (save points, level gates), software engineering (version control checkpoints, system state snapshots), and transportation (security checkpoints, quality control checkpoints). None of these usage contexts has an established translation into educational research theory. The term carries connotations of verification-as-gatekeeping rather than verification-as-learning, which conflicts with the paper's argument that calibration interventions are fundamentally pedagogical in character.

**Theoretical rootlessness:** No major educational research tradition uses "checkpoint" as a technical term. Searching the educational psychology, learning sciences, and instructional design literatures yields no established framework built around "checkpoint." Using the term in a journal article targeting educational technology researchers would therefore require extensive definitional work and would not leverage any existing theoretical inheritance.

**Ambiguity:** "Checkpoint" is ambiguous between at least three distinct educational activities: brief in-lesson comprehension checks (formative assessment), structured pauses for reflection (metacognitive prompts), and gating mechanisms that must be passed before proceeding (mastery gates). The term does not discriminate between these distinct activities and therefore lacks the conceptual precision required for rigorous theoretical work.

### 1.3 Rationale for Adopting "Trust Calibration Scaffold"

**"Scaffolding" has deep theoretical roots.** The scaffolding concept was introduced by Wood, Bruner, & Ross (1976) and is one of the most extensively theorized and empirically supported constructs in educational psychology. Hattie's (2009) *Visible Learning* meta-synthesis reports an average effect size of d = 0.82 for scaffolding interventions — among the strongest findings in the educational literature. By using "scaffold" as the base term, "trust calibration scaffold" inherits the theoretical and empirical warrant of the broader scaffolding tradition.

**"Calibration" is legitimate in SRL literature.** The term "calibration" has an established technical meaning in self-regulated learning research: it refers to the accuracy of a learner's judgments about their own capabilities (Winne & Hadwin, 1998; Zimmerman, 2000). Extending "calibration" to the trust domain is a deliberate theoretical move, one that the paper justifies and defends by drawing the distinction between SRL calibration (self-directed) and trust calibration (system-directed). The term is not borrowed from an unrelated field; it is extended with explicit theoretical justification from within the educational research tradition.

**"Trust" is a recognized construct in the relevant literature.** The automation trust literature (Lee & See, 2004; Hoff & Bashir, 2015) and the emerging educational AI trust literature (Wang et al., 2025) both treat trust as a technical construct with defined components and measurement approaches. Incorporating "trust" into the compound term directly names the construct the scaffold is designed to address.

**Compound term captures the mechanism.** "Trust Calibration Scaffold" describes: (1) the psychological construct being targeted (trust), (2) the process being promoted (calibration — alignment between perceived and actual AI capability), and (3) the pedagogical mechanism being used (scaffolding — contingent, fading, responsibility-transferring support). Each component is theoretically meaningful, and the compound term accurately describes the mechanism in terms that are legible to educational researchers.

---

## 2. Full Terminology Mapping Table

The following table maps the conceptual meaning of each design element to the established educational research term adopted for this project, with key theorists and literature citations.

| Framework Meaning | Established Education Term | Key Theorists / Sources |
|---|---|---|
| Brief in-lesson verification of learner comprehension | Checks for understanding | Wiliam (2011); Black & Wiliam (1998) |
| Assessment woven continuously into instruction | Embedded formative assessment | Wiliam (2011); Black & Wiliam (1998) |
| Prompts requiring explicit self-reflection on thinking | Metacognitive prompts | Schraw (1998); Bannert (2009); Guo et al. (2022) |
| Structured support that transfers responsibility to learner | Scaffolding | Wood, Bruner, & Ross (1976); Hannafin et al. (1999) |
| Deliberately imposed task difficulty to enhance long-term learning | Desirable difficulties | Bjork & Bjork (1994, 2011) |
| Designed struggle before direct instruction to deepen understanding | Productive failure | Kapur (2008) |
| Learner self-assessment accuracy relative to own performance | Calibration (in SRL) | Zimmerman (2000); Winne & Hadwin (1998) |
| Learner trust-assessment accuracy relative to AI system performance | Trust calibration | Lee & See (2004); extended to education in this paper |
| Structured protocol to interrupt automatic habit-driven behavior | Intentional interruption | Katz & Dack (2013) |
| Human oversight mechanism in AI-assisted systems | Human-in-the-loop (borrowed from engineering) | Russell (2019); engineering origin |
| Contingent, fading support reducing as learner competence grows | Progressive fading | Wood, Bruner, & Ross (1976); Collins et al. (1989) |
| AI system's disclosure of its own uncertainty or confidence | AI uncertainty transparency | XAI literature; Gunning et al. (2019) |
| Dialogue structure requiring learner to justify claims | Socratic dialogue | Plato; adapted by Collins & Stevens (1982) |
| Teacher oversight and intervention in AI-mediated learning | Teacher-mediated verification | Adapted from human-in-the-loop; this project |

---

## 3. Visualization Label Changes

The following table records all label changes applied to figures, diagrams, and visualizations associated with this project.

| Original Label | Replacement Label | Rationale |
|---|---|---|
| Checkpoint Mechanisms | Trust Calibration Scaffolds | "Checkpoint" deprecated; see Section 1 above |
| Forced Friction | Desirable Difficulties (Bjork) | "Forced friction" is not an educational research term; Bjork & Bjork (1994, 2011) is the authoritative source |
| HITL | Teacher-Mediated Verification | "HITL" (Human-in-the-loop) is an engineering term; "Teacher-mediated verification" is more precise for educational contexts and names the human agent |
| Confidence Display | AI Uncertainty Transparency | "Confidence display" is vague; "AI uncertainty transparency" is grounded in XAI literature and names both the information type and the design principle |
| Socratic Mode | Socratic Dialogue (retained) | "Socratic dialogue" is a recognized educational term; retained with minor formatting adjustment to "dialogue" from "mode" |
| Checkpoint Prompt | Metacognitive Trust Prompt | Replaces gaming-derived term with educational research terminology |
| Verification Gate | Calibration Verification Task | "Gate" implies blocking; "task" implies learning activity |
| Friction Layer | Desirable Difficulty Layer | Aligns with Bjork & Bjork terminology |
| Override Check | Human Oversight Verification | More precise and educationally grounded |

---

## 4. Usage Rules

The following rules govern terminology usage across all project documents, the manuscript, supplementary materials, and associated communications.

### 4.1 Primary Usage Rule

**Use "trust calibration scaffold" throughout.** This term is the primary designation for the design mechanism that the paper proposes. It appears in the paper's conceptual framework, design principles, implications, and research agenda. All documentation in this repository should use this term.

**Acceptable variant forms:**
- trust calibration scaffold (lowercase, full form — preferred in running text)
- Trust Calibration Scaffold (title case — acceptable in headings and figure labels)
- TCS (abbreviation — acceptable after first full use in a given document, but use sparingly)
- trust calibration scaffolding (gerund/noun form — acceptable when referring to the process)
- trust calibration scaffold mechanism (compound noun — acceptable when specifying the design mechanism)

### 4.2 Deprecated Term Handling

**"Checkpoint" is a deprecated term for this project.** It should not appear in the manuscript, abstract, keywords, figure labels, or primary documentation.

**Exception — historical record:** "Checkpoint" may appear in:
- Discussion documents that trace the project's conceptual development.
- The `discussion/` directory of this repository, where the term was used in earlier project phases.
- Direct citations of any external publications that use the term, in which case the citation should be followed by a bracketed clarification: [originally termed "checkpoint"].

**Example of correct citation usage:**
> "Some prior work has described similar mechanisms as 'checkpoints' [originally termed 'checkpoint'], but these mechanisms are more precisely theorized as trust calibration scaffolds within the framework proposed here."

### 4.3 SRL Calibration vs. Trust Calibration Usage

When the paper or project documents discuss calibration, the specific type of calibration must always be named:

- When referring to accuracy of learner self-assessment: use "SRL calibration" or "self-calibration."
- When referring to accuracy of learner assessment of AI capability: use "trust calibration."
- Never use "calibration" alone in contexts where the two types might be confused.

**Example of incorrect usage:** "Calibration improved in the intervention group."
**Example of correct usage:** "Trust calibration accuracy improved in the intervention group, as measured by the alignment between learner trust ratings and AI response accuracy scores."

### 4.4 Scaffolding-Specific Usage Rules

- When describing the fading property of scaffolding, use "progressive fading" to distinguish it from abrupt removal of support.
- When describing the contingency property, use "contingent scaffolding" or "adaptive scaffolding."
- When referencing the Zone of Proximal Development in connection with scaffolding, cite Vygotsky (1978) as the primary source.

### 4.5 Visualization and Figure Label Rules

- All figure labels must use the replacement terms specified in Section 3.
- Figure captions should include a parenthetical citation where the term is grounded in a specific theoretical source (e.g., "Desirable Difficulties (Bjork & Bjork, 2011)").
- Engineering-origin terms (HITL, S-O-R abbreviation) should be avoided in figures; if the S-O-R model is depicted, label the full words (Stimulus-Organism-Response) in figure labels.

### 4.6 Communication and Presentation Usage

- In conference presentations and seminar discussions, use the full term "trust calibration scaffold" at first mention; "TCS" is acceptable as an abbreviation thereafter.
- When explaining the term to non-specialist audiences, lead with the scaffolding metaphor: "Just as construction scaffolding supports a building's structure while it is being built and is then removed, trust calibration scaffolds support appropriate learner-AI trust while it is developing."

---

## 5. Change Log

| Date | Change | Rationale | Scope |
|---|---|---|---|
| 2026-02-28 | "Checkpoint" deprecated; "Trust Calibration Scaffold" adopted | Theoretical grounding; educational research alignment | All project documents, manuscript, visualizations |
| 2026-02-28 | "HITL" replaced with "Teacher-Mediated Verification" in visualizations | Engineering term; needs educational translation | Visualizations only |
| 2026-02-28 | "Forced Friction" replaced with "Desirable Difficulties (Bjork)" | Not an educational research term | Visualizations only |
| 2026-02-28 | "Confidence Display" replaced with "AI Uncertainty Transparency" | More precise; XAI grounding | Visualizations only |
| 2026-02-28 | SRL calibration / trust calibration distinction formalized | Prevents conflation; core conceptual contribution | Manuscript, theoretical_foundation.md |
