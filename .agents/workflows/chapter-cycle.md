---
name: chapter-cycle
description: "Quy trình sản xuất từng chương sách module hóa: Lập Blueprint, phỏng vấn bóc tách ký ức, chấp bút từng section, sàng lọc cơ học stdlib, biên tập phẫu thuật 3 lớp, ghép chương, kiểm định Layer 2 và cập nhật Story Bank."
version: 1.1.0
requires_agents: [master-orchestrator, book-architect, chapter-crafter, quality-auditor]
requires_skills: [chapter-blueprinting, author-excavation, story-enrichment, chapter-drafting, humanizer, editorial-revision, spine-architecture]
artifact_outputs: ["chapters/<chapter_id>/card.md", "chapters/<chapter_id>/sections/*.md", "chapters/<chapter_id>/draft.md", "chapters/<chapter_id>/audit_verdict.md"]
topology: orchestrator-workers
trigger: manual
max_retry_per_node: 3
initial_state: BLUEPRINT
terminal_states: [DONE]
nodes:
  BLUEPRINT:
    required_outcome: "chapter_card_created"
    human_gate: false
    transitions:
      - to: GATE_3_BLUEPRINT
        when: "card_file_exists == true"
  GATE_3_BLUEPRINT:
    required_outcome: "blueprint_approved"
    human_gate: true
    transitions:
      - to: KNOWLEDGE_EXCAVATION
        when: "blueprint_signed_off == true"
  KNOWLEDGE_EXCAVATION:
    required_outcome: "stories_enriched"
    human_gate: false
    transitions:
      - to: SECTION_DRAFTING
        when: "story_cards_interviewed == true && story_cards_ready == true"
  SECTION_DRAFTING:
    required_outcome: "all_sections_drafted"
    human_gate: false
    transitions:
      - to: MECHANICAL_SCREEN
        when: "all_section_files_exist == true"
  MECHANICAL_SCREEN:
    required_outcome: "mechanical_lint_passed"
    human_gate: false
    transitions:
      - to: CHAPTER_ASSEMBLY
        when: "lint_exit_code == 0"
      - to: GATE_3_BLUEPRINT
        when: "lint_exit_code == 3"
      - to: SECTION_REVISION
        when: "lint_exit_code != 0 && revision_round < 3"
      - to: INFORMED_REVIEW
        when: "lint_exit_code != 0 && revision_round >= 3"
  SECTION_REVISION:
    required_outcome: "surgical_edits_applied"
    human_gate: false
    transitions:
      - to: MECHANICAL_SCREEN
        when: "revision_cycle_completed == true && revision_round <= 3"
  CHAPTER_ASSEMBLY:
    required_outcome: "draft_md_assembled"
    human_gate: false
    transitions:
      - to: INFORMED_REVIEW
        when: "draft_file_exists == true"
  INFORMED_REVIEW:
    required_outcome: "layer_2_audit_passed"
    human_gate: false
    transitions:
      - to: MEMORY_UPDATE
        when: "audit_verdict == 'PASS'"
      - to: SECTION_REVISION
        when: "audit_verdict == 'REVISE' && revision_round < 3"
      - to: GATE_3_BLUEPRINT
        when: "audit_verdict == 'REVISE' && revision_round >= 3"
      - to: BLUEPRINT
        when: "audit_verdict == 'RESTRUCTURE'"
  MEMORY_UPDATE:
    required_outcome: "registers_and_story_bank_updated"
    human_gate: false
    transitions:
      - to: SPINE_CHECK
        when: "memory_update_complete == true"
  SPINE_CHECK:
    required_outcome: "spine_consistency_verified"
    human_gate: false
    transitions:
      - to: DONE
        when: "spine_check_passed == true"
---

# Workflow: /chapter-cycle (Chapter Production Cycle)

> **Mục tiêu**: Vận hành dây chuyền sản xuất khép kín cho một chương sách gồm **10 node thực thi tuần tự + 1 trạng thái kết thúc (`DONE`)**: từ bản vẽ card phân rã 3–5 sections đến chấp bút module độc lập, sàng lọc cơ học, lắp ráp tự động, thẩm định độc lập Layer 2 và cập nhật Sổ bộ tri thức chống trùng lặp.

---

## 1. INVARIANTS (Ràng buộc bất biến)

1. **Node-Scoped Grounding**: Khi chạy Node $X$, Agent chỉ nạp Spine Matrix + file `chapter-cycle/node-*.md` tương ứng + Skill của Stage đó. CẤM nạp chéo node khác.
2. **Context Isolation (SEQ-004/006)**: Tại Node 8 (`INFORMED_REVIEW`), `master-orchestrator` nạp `node-08-review.md` để brief context sạch cho `quality-auditor`; Auditor chỉ nạp bản thảo và [quality-engine.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/quality-engine.md).
3. **No Evidence → No Transition**: Mọi state transition đòi hỏi artifact tồn tại thực tế trên đĩa (DoD nhị phân).

---

## 2. Stage Bundle Map (5 Giai đoạn)

| Giai đoạn (Stage) | Agent Chủ Trì & Phối Hợp | Kỹ Năng / Tài Nguyên Nạp (Skill & Knowledge Bundle) | Mục Tiêu Giai Đoạn |
|---|---|---|---|
| **Stage 1: Foundation (Khởi tạo Nền tảng)** | `master-orchestrator` + `book-architect` | `author-excavation`, `terms.md`, `manifesto.md`, `voice.md` | Bóc tách nhân sinh quan, định vị độc giả và khung khái niệm. |
| **Stage 2: Architecture (Thiết kế Card v3)** | `book-architect` + `chapter-crafter` | `chapter-blueprinting`, `knowledge/structure/chapter_shapes.md` | Thiết kế Card v3: Core Thesis, Reader Promise, Beat Map, trần `budget_words_max`. |
| **Stage 3: Excavation (Đào sâu Chất liệu)** | `chapter-crafter` | `author-excavation` (mode `chapter` hoặc `capture`), `story-enrichment` | Khai thác sâu trải nghiệm thật, bổ sung chi tiết hiện trường không bịa đặt vào `story_bank.md`. |
| **Stage 4: Drafting (Chấp bút Từng Section)** | `chapter-crafter` | `chapter-drafting`, `humanizer` (co-pilot), `voice.md` | Chấp bút văn xuôi liên tục (CONV-001) trong trần từ, triệt tiêu AI tells ngay từ đầu. |
| **Stage 5: Revision & Audit (Kiểm định & Biên tập)** | `quality-auditor` + `chapter-crafter` | `quality-engine`, `editorial-revision`, `summaries.md` | Thẩm định độc lập 2 Lens (Sự thật & Trải nghiệm độc giả), biên tập phẫu thuật 3 lớp. |

---

## 3. STATE MACHINE NODES (Spine Matrix 10 Nodes)

| Node | Giai đoạn (Stage) | File Hợp Đồng Chi Tiết | Bất Biến & Chuỗi Kiểm Tra Cốt Lõi |
|---|---|---|---|
| **BLUEPRINT** | Stage 2: Architecture | [node-01-blueprint.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-01-blueprint.md) | Phân rã Card v3, 3–5 section files, trần `budget_words_max` (3,500–5,000 từ). |
| **GATE_3_BLUEPRINT** | Stage 2: Architecture | [node-02-goal-lock.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-02-goal-lock.md) | **Goal Lock** bất biến sau Gate 3 trên **Reader Promise**; mở khóa tường minh qua lệnh **GOAL_UNLOCK**. |
| **KNOWLEDGE_EXCAVATION** | Stage 3: Excavation | [node-03-excavation.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-03-excavation.md) | Bắt buộc phỏng vấn: `story_cards_interviewed == true && story_cards_ready == true`, kết nối **author-excavation**. |
| **SECTION_DRAFTING** | Stage 4: Drafting | [node-04-drafting.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-04-drafting.md) | Chấp bút tuần tự từng section H2, co-pilot humanizer, **Feedback Carry-Forward**, yield `[EVIDENCE-REQUEST: req_XX]`. |
| **MECHANICAL_SCREEN** | Stage 4: Drafting | [node-05-mechanical-screen.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-05-mechanical-screen.md) | L0 stdlib linter `repair_invariants.py`, 5 tiêu chuẩn nhị phân Layer 1 tại `quality-engine.md`. |
| **SECTION_REVISION** | Stage 5: Revision | [node-06-revision.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-06-revision.md) | Phẫu thuật sửa 1 file, `WHAT TO KEEP`, 3 Pass, conditional humanizer, hạn ngạch `revision_round <= 3`. |
| **CHAPTER_ASSEMBLY** | Stage 4: Drafting | [node-07-assembly.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-07-assembly.md) | L0 stdlib compiler `assemble_chapter.py`, ghép draft alphanumeric, banner nguồn sự thật. |
| **INFORMED_REVIEW** | Stage 5: Revision & Audit | [node-08-review.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-08-review.md) | **quality-auditor** trong **Chapter Review Mode**, hàng rào ngữ cảnh SEQ-004/006, phán quyết `PASS / REVISE / RESTRUCTURE`. |
| **MEMORY_UPDATE** | Stage 5: Revision & Audit | [node-09-memory-update.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-09-memory-update.md) | CLI deterministic: **record-story-usage** & **update-continuity**, cập nhật `summaries.md`, `terms.md`, `decisions.md`. |
| **SPINE_CHECK** | Stage 5: Revision & Audit | [node-10-spine-check.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle/node-10-spine-check.md) | Kiểm tra Leads-to, gắn cờ `SPINE-FLAG`, tính Blast Radius cập nhật `book_spine.md`, chuyển sang `DONE`. |

---

## 4. FAILURE & ESCALATION

- **Hard Stop Protocol (`ROUTE-006`)**: Khi `revision_round >= 3` hoặc phát hiện `[PLATEAU]`, Agent dừng ngay lập tức và kích hoạt `[ESCALATE_HUMAN]` xin chỉ đạo của tác giả.
- **Batch Planning Protocol**: Chạy lặp `BLUEPRINT → GATE_3` cho nhiều chương (`ch_01..ch_03`), dừng ở `PAUSE` trước `KNOWLEDGE_EXCAVATION`. **Bắt buộc**: Đối chiếu chéo các mã câu chuyện `S-XXX` đã gán trong các Card chị em để chống trùng lặp trước khi Node 9 ghi nhận `Used In`.
