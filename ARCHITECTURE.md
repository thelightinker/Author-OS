# Book Writing Agent Kit — Living Architecture SSOT

## 1. System Topology & 4 Functional Roles
The kit deploys a clean `orchestrator-specialists-critic` topology (1 L0 System Controller + 2 L1 Specialists + 1 L1 Quality Auditor = 4 Agents):
- **L0 System Controller (`master-orchestrator`):** Governs lifecycle transitions, inspects filesystem state, enforces sequential isolation, and coordinates human gates. *Contract Exemption:* L0 Controller is strictly exempt from the specialist "Agent → invoke ≥ 1 Skill" contract. Zero fake routing skills.
- **L1 Specialist 1 (`book-architect`):** Macro Strategist, Spine & Leads-to Engineer, Evidence Ledger Formulator, Genesis Thesis Stress-Tester. Owns 3 skills + 1 shared skill (**4 bindings**).
- **L1 Specialist 2 (`chapter-crafter`):** Socratic Interviewer, Chapter Blueprinter, Modular Section Craftsman, and 3-Pass Surgical Revision Craftsman. Owns 6 skills + 1 shared skill (**7 bindings**).
- **L1 Critic (`quality-auditor`):** Independent Reader Advocate, Dual-Lens Chapter Reviewer (Prose & Reader Experience), and Whole-Book Cold Read Evaluator. Owns 1 skill + 1 shared skill (**2 bindings**).
- **Topology Formula:** 1 Controller + 2 Specialists + 1 Critic = 4 Agents | 10 Unique Skills | 13 Bindings.

## 2. Anti-Regression Routing Constitution (ROUTE-001 to ROUTE-007)
- **`ROUTE-001` (Single Authoritative Dispatch Registry):** The Orchestrator Phase Routing Matrix in `master-orchestrator.md` is the sole SSOT. Zero external regex scripts or scattered intent indexes.
- **`ROUTE-002` (State & Goal-Driven Routing + Free-Form Fallback):** Route = $f(\text{Current Phase}, \text{Target Artifact})$. Free-form commands inspect project file state first; if ambiguous, Orchestrator asks the author with 2 concrete options.
- **`ROUTE-003` (Canonical Multi-Book Storage Contract):** Canonical storage structure: `Books/<book_slug>/foundation/` (9 living registers: `manifesto.md`, `voice.md`, `book_spine.md`, `promises.md`, `terms.md`, `story_bank.md`, `evidence_ledger.md`, `decisions.md`, `summaries.md`), `Books/<book_slug>/chapters/<chapter_id>/card.md`, `sections/*.md`, `draft.md` (assembled view), and `Books/<book_slug>/outputs/manuscript.md`. Strict separation between Vietnamese `book_title` and filesystem `book_slug` (e.g. `nhan-danh-dieu-vi-dai`). Generic placeholders like `Mybook` / `my-book` are permanently barred.
- **`ROUTE-004` (Workflow-Only Execution Mandate):** Master Orchestrator strictly routes into declared workflows (`book-genesis`, `chapter-cycle`, `book-assembly`). Ad-hoc parallel pipelines are barred.
- **`ROUTE-005` (State As Persistent Transition Guard):** Lifecycle states map directly to filesystem artifacts. Zero zombie state keys (`read_by: []` banned).
- **`ROUTE-006` (Loop Circuit Breaker & Plateau Exit):** Max 3 revision rounds stored persistently in `card.md` metadata (`revision_round: 1/3`). Detecting `[PLATEAU]` triggers mandatory human escalation.
- **`ROUTE-007` (Bimodal Interaction Spectrum):** Interactive Mode (free dialogue, brainstorming, rapid advisory) vs. Production Mode (strict workflow execution, mechanical gates, and atomic commits).

## 3. Strict Sequential Execution & Context Isolation (SEQ-001 to SEQ-008)
- **`SEQ-001` (Strict Single Active Agent):** Exactly ONE Agent is active per execution step. Zero multi-agent bundles or co-activation in a single node.
- **`SEQ-002` (Sequential Verification Precondition):** Downstream agents cannot activate until current agent passes verification.
- **`SEQ-003` (Explicit Artifact-Bound Handoff):** Transfers occur 100% via persistent artifacts on disk (`card.md`, `draft.md`, `audit_verdict.md`, `evidence_request.md`), never through implicit conversation memory.
- **`SEQ-004` (Zero Preloading of Downstream Roles & Skills):** An active agent never loads prompts or skills of downstream roles.
- **`SEQ-005` (Exclusive Transition Authority):** Master Orchestrator and Workflow State Machines are the sole authorities for agent switching; specialist agents cannot delegate to each other.
- **`SEQ-006` (Clean Activation & Context Reset Boundary):** Switching agents mandates an explicit Context Reset. The incoming agent loads only its declared prompt, owned skills, and declared input files.
- **`SEQ-007` (Prohibition of Parallel Execution in Prose Generation):** Parallel generation is permanently prohibited; prose construction is strictly sequential cumulative progression.
- **`SEQ-008` (Role Integrity & Anti-Self-Approval):** Crafter cannot approve its own drafts for PASS; Auditor cannot mutate section prose.
- **Shared Skill Isolation Invariant:** `Shared Skill != Shared Context`. `falsification-steelmanning` lives once on disk but is loaded independently with Context Reset between roles.

## 4. Modular Section Architecture & Heading Standards (P0 Invariant)
To eliminate LLM brevity traps and hallucinated truncations, writing and revision occur 100% within `chapters/<chapter_id>/sections/*.md` (800–1,500 words/section):
- **Heading H2 Standard:** Each section opens with an H2 heading (`## [Section Title]`) as a cognitive compass, followed by continuous CONV-001 prose.
- **Multi-Tier Hierarchy:** Supports flexible 3-tier (`Part > Chapter > Section`) or 4-tier (`Part > Chapter > Section > Subsection/Beat`) outlines.
- **Flexible 1–3 Skills Co-Pilot:** Crafter may co-activate `chapter-drafting` + `humanizer` (eliminating AI prose tells at draft-time) + `story-enrichment`.
- **Sequential Section Cadence:** Sections are drafted and reviewed sequentially (Section $i$ $\rightarrow$ short preview checkpoint $\rightarrow$ Section $i+1$). Direct prose authoring into `draft.md` is strictly forbidden.

## 5. Living Memory Architecture (100% Pure Markdown SSOT)
- **Kit-Level Memory (`.agents/memory/MEMORY.md`):** Cross-book evolutionary memory containing `## User Preferences` (permanent author stylistic DNA), `## Feedback & Negative Patterns` (accumulated craft critique across projects), and `## Validated Patterns` (proven structure templates).
- **Book-Level Living Memory (`books/<book_slug>/foundation/`):**
  1. `manifesto.md`: Thesis, target audience, cover promise, and validated boundary conditions.
  2. `voice.md`: Concrete voice corpus, tone anchors, approved/banned vocabulary.
  3. `book_spine.md`: 3–4 tier TOC spine with governing lines and mandatory `Leads-to` linkages.
  4. `promises.md`: Reader expectation vs chapter payoff matrix.
  5. `evidence_ledger.md`: Empirical citations (Tier 1–2 sources only).
  6. `decisions.md`: Strategic Decision Log tracking `DISSENT` and author overrides.
  7. `summaries.md`: Rolling chapter summaries and cognitive progression anchors.
  8. `terms.md`: Living Concept Matrix with strategic roles (liberating concept vs. counter-thesis).
  9. `story_projections.md`: Book-specific narrative projections (referencing Canonical Stories via `ref_id`, `angle`, `function`, `emphasis/omission`; zero duplication of canonical story text).

### 5.1. 3-Tier Story Governance Architecture Contract
> **Overarching Invariant:** *"One story, one canonical truth; many contextual projections; usage history is not truth."*

1. **Single Truth Vault (SSOT):** System Memory (`.agents/memory/experience/story_bank.md`) is the sole Single Source of Truth for Canonical Stories, provenance tiers, confirmed facts, and unknowns. Books never redefine biographical truth.
2. **Book Projection:** Individual books do NOT possess a local `story_bank.md`; they strictly maintain `story_projections.md` containing `{ref_id, angle, function, target_chapter, emphasis, omission}`. Canonical story bodies are never copied into book foundations.
3. **Ingest Lifecycle:** All biographical and real-world memories follow the strict unidirectional pipeline:
   `Raw/Candidate Memory → Verify → Canonical Story (System Vault) → Book Projection → Consume (Draft Section)`.
4. **Usage Ledger:** `.agents/memory/experience/usage.json` serves exclusively as an append-only consumption ledger and collision arbitration index (`DUPLICATE-RISK` vs `REUSED-DIFFERENT-ANGLE`). It is an index/arbitration layer, never a knowledge source.

## 6. Qualitative Context Budgeting & Progressive Disclosure
Context loading is budgeted qualitatively by phase to prevent cognitive dilution:
- **Genesis Phase:** Minimal project context (manifesto drafting, terms initialization, kit memory preferences).
- **Drafting & Revision Phase:** Section-local context (voice golden paragraphs, active card beats, active section file, assigned story card where not in `Used In`, prior section summary). Unreferenced stories and external chapters are never loaded.
- **Assembly Phase:** Macro-level book context (spine Leads-to chain, chapter summaries, story bank audit, terms matrix, compiled manuscript text).

## 7. Quality Engine & Human Gates
- **Layer 1 (Mechanical Screen):** Deterministic Python stdlib auto-repair & lint (`scripts/repair_invariants.py --lint`). Zero external dependencies.
- **Layer 2 (Informed Review):** Executed by `quality-auditor` in Chapter Review Mode (Draft + Card + Payload Registry in `summaries.md` + `terms.md` + `voice.md` under Strict Context Masking; NO manifesto/sources) using `editorial-revision` and `falsification-steelmanning`.
- **Layer 3 (Cold Read):** Executed by `quality-auditor` in Whole-Book Review Mode reading `outputs/manuscript.md` ONLY under Absolute Blind Barrier. Evaluates 10 High-Leverage Hypotheses with Qualitative Risk Tiers (`LOW / MEDIUM / HIGH RISK`) and 4 advisory editorial verdicts: `Ship / Conditional / Major Revise / Kill`.
- **Voice Audit Diagnostic Rubric:** Read-only scan of assembled chapters against `voice.md` producing `outputs/voice_drift_report.md` without modifying manuscript text.
- **Sequential Human Gates:**
  1. *Gate 1–5 (Genesis 5-Stage Gates):* `GATE_1_MANIFESTO` $\rightarrow$ `GATE_2_VOICE` $\rightarrow$ `GATE_3_TERMS` $\rightarrow$ `GATE_4_STORIES` $\rightarrow$ `GATE_5_SPINE`.
  2. *Gate 3 (Blueprint Approval):* Governed by Trust Escalation Enum (`always_ask` $\rightarrow$ `sample_first` $\rightarrow$ `auto_proceed`) with sequential section checkpoints.
  3. *Gate 4 (Final Publishing Determination):* Author Sovereignty over Cold Read advisory report in Book Assembly.

## 8. Epistemic Provenance & Collaboration Governance (P0 Invariants)
- **`COLLAB-011` (Understand Before Write & Insufficient-Context Gate):** Strict mandate: "Hiểu người trước, viết sau." When foundational context regarding author perspective, values, real-life experience, or anecdotes is missing or ambiguous, the agent MUST STOP AND INTERVIEW/PROBE (`YIELD_TO_INTERVIEW`), never fill gaps with hallucination. Questions must possess high information entropy reduction (1 focused question at a time).
- **`COLLAB-012` (5-Level Epistemic Hierarchy):** Every statement and story element is partitioned into 5 levels:
  1. `VERIFIED_FACT`: Empirical SSOT citation or objective documentation.
  2. `USER_STATED`: Direct statement from author in chat/interview.
  3. `AGENT_INFERENCE`: AI logical deduction (explicitly labeled; forbidden from masquerading as author statement).
  4. `HYPOTHESIS`: Unconfirmed creative proposal.
  5. `UNKNOWN`: Unverified gap (strictly preserved as unknown, never fabricated).
  *Anti-Escalation Invariant:* Levels 3–5 can never be escalated to Levels 1–2 without author confirmation.
- **Story Integrity Protocol & 5-Part Epistemic Breakdown:** Every card in `story_bank.md` must declare `Provenance Tier` (A/B/C/D), `Confirmed Facts`, `Interview Content`, `Author Interpretation`, `Agent Inferences`, and `Unknown Details`. Zero tolerance for fabricated sensory details, dialogue, or timelines.
- **Deterministic Timeline Sanity:** Stories must mechanically match the author's birth year and biographical facts in `identity.md`. Checked automatically during mechanical screen (`repair_invariants.py --lint`).

## 9. Architectural Status & Craft Glossary
- **Status:** Epistemic governance, Insufficient-Context Gate, and Story Integrity mechanically enforced.
- **Modular Sections:** Atomic markdown files (`00_open.md`, `01_sec1.md`) preserving word count integrity.
- **Story Bank:** Anecdote registry enforcing 5-part Epistemic Breakdown and zero unauthorized recycling via `Used In: []`.
- **Strategic Concept Roles:** Clear classification of concepts in `terms.md` (liberating concept vs. counter-thesis).
- **Leads-to:** Causality thread where the conclusion of Chapter N creates the psychological demand for Chapter N+1.
- **WHAT TO KEEP:** Compulsory identification of core sentences that must survive editing before revising a section.
- **Self-Steelmanning:** Crafter Pass 1 adversarial check testing up to 3 core claims against counter-arguments.
- **Thesis Stress-Test:** Genesis adversarial attack establishing Boundary Conditions ("Đúng khi nào, Sai khi nào?").
- **Scoped Cascade Snapshot:** Targeted backup of affected files to `snapshots/` prior to spine restructures.
- **CONV-001:** Layout standard enforcing 1 continuous narrative paragraph per block (no artificial bulleting in prose).
