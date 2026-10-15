# Writing Agent Memory Router (SSOT Hub)

> **Kiến Trúc Bộ Nhớ Hybrid Lean 4 Tầng & JIT Runtime**  
> *Nguyên tắc cốt lõi*: **Memory là Source of Truth | CLI là truy vấn & validate | Agent là reasoning**.  
> Tuyệt đối cấm nạp toàn bộ file vào prompt; chỉ dùng JIT CLI để nạp đúng phần ngữ cảnh cần thiết.

---

## 1. Bản Đồ Phân Tầng Nhận Thức

- 🧬 [author/identity.md](./author/identity.md) — Bản sắc Bản sắc tác giả, 3 tầng giá trị, ranh giới đạo đức.
- 🎙️ [author/voice.yaml](./author/voice.yaml) — Nhịp thở câu (cadence), từ vựng preferred/avoid, signature moves.
- 📚 [experience/story_bank.md](./experience/story_bank.md) — Author Canonical Story Bank (SSOT) với 5 trường Epistemic Breakdown + Timeline Sanity.
- 🔬 [experience/evidence.json](./experience/evidence.json) — Case studies, nghiên cứu khoa học kiểm chứng (EV-XXX).
- 🎯 [experience/usage.json](./experience/usage.json) — Sổ cái khai thác đa sách (Cross-book consumption ledger & collision arbitration).
- 📖 [project/book_bible.md](./project/book_bible.md) — Khung sườn 3 phần, luận đề trung tâm của cuốn sách hiện tại.
- 🧠 [project/continuity.json](./project/continuity.json) — 5 Trụ cột nhất quán: facts, concepts, metaphors, claims, open loops.
- 📝 [project/chapter_digests/](./project/chapter_digests/) — Bản tóm tắt cô đọng 1 trang/chương để nạp liên chương.
- 🔄 [evolution/style_drift.md](./evolution/style_drift.md) — Bẫy lệch giọng AI và quy tắc nắn chỉnh hồi quy.
- 💬 [evolution/feedback.jsonl](./evolution/feedback.jsonl) — Event stream ghi nhận góp ý thực tế từ độc giả/editor.

### 1.1. Architecture Contract: 3-Tier Story Governance
> **Overarching Invariant:** *"One story, one canonical truth; many contextual projections; usage history is not truth."*

1. **Single Truth Vault (SSOT):** System Memory (`.agents/memory/experience/story_bank.md`) là SSOT duy nhất của Canonical Story + provenance + confirmed facts + unknowns. Từng cuốn sách tuyệt đối không định nghĩa lại hay fork sự thật cuộc đời tác giả.
2. **Book Projection:** Cuốn sách không sở hữu `story_bank.md` độc lập; chỉ sở hữu `books/<slug>/foundation/story_projections.md` chứa `{ref_id, angle, function, target_chapter, emphasis, omission}`, tuyệt đối không copy thân bài câu chuyện gốc.
3. **Ingest Lifecycle:** Quy trình nạp ký ức đơn hướng:
   `Raw/Candidate Memory → Verify Socratic → Canonical Story (System Vault) → Book Projection → Consume (Draft Section)`.
4. **Usage Ledger:** `.agents/memory/experience/usage.json` chỉ lưu lịch sử sử dụng và điều phối va chạm (`DUPLICATE-RISK` vs `REUSED-DIFFERENT-ANGLE`), không phải knowledge source.

---

## 2. JIT CLI Quick Reference (`python .agents/scripts/memory_cli.py`)

| Tình huống sử dụng | Lệnh JIT CLI tương ứng |
| :--- | :--- |
| **Soạn thảo / Nắn giọng** | `python .agents/scripts/memory_cli.py get-voice` |
| **Tìm chuyện kể mở đầu** | `python .agents/scripts/memory_cli.py get-story --tag 10_meter_paradox` |
| **Ghi nhận đã dùng chuyện** | `python .agents/scripts/memory_cli.py record-story-usage --id S-001 --chapter ch_01 --section 00_open --angle "Mô tả góc kể"` |
| **Trích dẫn luận cứ** | `python .agents/scripts/memory_cli.py get-evidence --tag cognitive_load` |
| **Nạp ngữ cảnh viết chương**| `python .agents/scripts/memory_cli.py get-continuity --chapter ch_02` |
| **Cập nhật fact sau chương**| `python .agents/scripts/memory_cli.py update-continuity --state-file chapter_state.json` |
| **Kiểm toán mâu thuẫn/lặp** | `python .agents/scripts/memory_cli.py audit-continuity` |

---

## 3. Ranh Giới Kiểm Thử & Kiểm Toán
- **CLI Audit**: Kiểm định cấu trúc nhị phân (trùng ID, hỏng ref, loop quá hạn, duplicate-risk trong cùng cuốn sách).
- **LLM Audit**: Thẩm định mâu thuẫn ngữ nghĩa và chất lượng văn phong trước khi xuất bản.
