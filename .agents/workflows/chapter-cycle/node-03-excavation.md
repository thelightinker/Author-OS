# Node 3: KNOWLEDGE_EXCAVATION

- **Vai trò thực thi**: `chapter-crafter` nạp skill `story-enrichment` kết hợp `author-excavation` (mode `chapter` hoặc `capture`).
- **Input**: Các thẻ câu chuyện được gán trong `card.md`, `chapters/<chapter_id>/intent_ledger.md`, `.agents/skills/author-excavation/references/insight_ladder.md`.
- **Quy tắc bắt buộc**: Nạp và tuân thủ tuyệt đối [story-integrity.md](../../rules/story-integrity.md) (liêm chính dữ liệu câu chuyện, cấm bịa đặt chi tiết chưa phỏng vấn).
- **Output Artifact**: Cập nhật chi tiết hiện trường trong `story_bank.md` và đồng bộ `chapters/<chapter_id>/intent_ledger.md`.
- **Human Gate**: `false`
- **Mục tiêu & Ràng buộc Understand-Before-Draft (COLLAB-011)**:
  - Đào sâu các câu hỏi `[OPEN]` trong `intent_ledger.md` và các insight gốc rễ, góc nhìn phản trực giác của tác giả; không hỏi lại điều đã `[CONFIRMED]`.
  - Khai thác Socratic đào sâu 4 khía cạnh (Giác quan, Tâm lý, Hành động, Vùng chưa chắc chắn) qua `story-enrichment` để hoàn thiện chi tiết hiện trường cho các câu chuyện xuất hiện trong chương.
  - Nếu thẻ câu chuyện chưa có sự kiện thật hoặc thiếu dữ kiện trọng yếu, **BẮT BUỘC DỪNG LẠI PHỎNG VẤN TÁC GIẢ** (Yield to Interview). CẤM tự ý chuyển sang `SECTION_DRAFTING` khi chưa phỏng vấn.
- **DoD**:
  - [ ] Đã hoàn thành phỏng vấn làm rõ các câu chuyện với tác giả (`story_cards_interviewed == true && story_cards_ready == true`).
  - [ ] Mọi câu chuyện gán cho chương đều có đủ chi tiết hiện trường và `Used In` hợp lệ; cập nhật các quyết định từ phỏng vấn vào `intent_ledger.md` (chuyển `[OPEN]` sang `[CONFIRMED]`).
- **Transition Path**: `KNOWLEDGE_EXCAVATION` $\rightarrow$ `SECTION_DRAFTING`.
