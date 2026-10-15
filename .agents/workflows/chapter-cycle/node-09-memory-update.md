# Node 9: MEMORY_UPDATE

- **Thực thi**: Điều phối cập nhật Sổ bộ sống của cuốn sách kết hợp CLI deterministic.
- **Lệnh thực thi cơ học (Deterministic CLI)**:
  1. Ghi nhận chống trùng lặp câu chuyện bằng CLI (0 lỗi format):
     ```bash
     python .agents/scripts/memory_cli.py record-story-usage --id S-XXX --chapter <chapter_id> --section <sec_id> --angle "Góc nhìn sử dụng" --function "vai_tro_trong_card"
     ```
  2. Hợp nhất trạng thái chương vào bộ não nhất quán:
     ```bash
     python .agents/scripts/memory_cli.py update-continuity --state-file chapters/<chapter_id>/chapter_state.json
     ```
- **Cập nhật Markdown SSOT**:
  1. Ghi tóm tắt nhận thức cuốn chiếu của chương vào `summaries.md` (Cognitive Payload Registry).
  2. Bổ sung các thuật ngữ mới phát sinh vào `terms.md`.
  3. Cập nhật các quyết định chiến lược và lằn ranh mới từ `chapters/<chapter_id>/intent_ledger.md` vào `decisions.md` (giữ tính đồng bộ SSOT toàn sách).
  4. Đọc `draft.md` của chương, viết 3 đến 5 ý chính (mỗi ý tối đa 8 từ) và tối đa 3 hình ảnh hoặc ví dụ cụ thể đã dùng (mỗi cái tối đa 6 từ). Rồi chạy `python .agents/scripts/memory_cli.py record-ideas-used --chapter <chapter_id> --ideas "<các ý, cách nhau bằng dấu chấm phẩy>" --images "<các hình ảnh, cách nhau bằng dấu chấm phẩy>"`.
- **DoD**: Sổ bộ và Continuity State được đồng bộ hoàn toàn với bản thảo chương vừa duyệt.
- **Ghi mốc bản thảo (Baseline Snapshot)**: Cuối cùng, ghi mốc bản thảo của chương để lần sau biết tác giả đã sửa gì: chạy `python .agents/scripts/memory_cli.py record-draft-baseline --chapter <chapter_id>`.
- **Transition Path**: `MEMORY_UPDATE` $\rightarrow$ `SPINE_CHECK`.
