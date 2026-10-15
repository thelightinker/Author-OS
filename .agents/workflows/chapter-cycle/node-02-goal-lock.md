# Node 2: GATE_3_BLUEPRINT & GOAL LOCK

- **Human Gate**: `true (Kiểm soát theo Bậc thang Tin cậy - Trust Escalation Enum)`
- **Giao Thức Khóa Mục Tiêu (Goal Lock Protocol)**:
  - Khi tác giả phê duyệt `card.md` tại Gate 3, hai trường **Core Thesis** và **Reader Promise** của Card v3 được **KHÓA BẤT BIẾN (GOAL LOCK)** trong toàn bộ chu trình chấp bút (Stage 4).
  - Chapter Crafter và Auditor không được tự ý bẻ lái luận điểm hoặc thay đổi cam kết chuyển hóa nhận thức đã hứa với độc giả.
  - Nếu trong quá trình viết phát sinh ý tưởng mới hoặc muốn thay đổi luận điểm: bắt buộc phải kích hoạt lệnh mở khóa tường minh (`GOAL_UNLOCK`) từ tác giả và cập nhật lại Card v3 trước khi viết tiếp.
- **Cơ chế phân tầng nghiệm thu Blueprint**:
  - **Bắt buộc 100% duyệt Card**: Tác giả trực tiếp phê duyệt `card.md` tại Gate 3 ở 100% các chương của cuốn sách. Tuyệt đối cấm cơ chế tự động bỏ qua (`auto_proceed`) ở cấp độ duyệt Blueprint; quyền kiểm soát kiến trúc thuộc độc quyền của tác giả.
  - `always_ask`: Tác giả duyệt Card trực tiếp qua hội thoại.
  - `sample_first`: Tác giả duyệt Card kèm bản nháp 1 section mẫu.
- **Transition Path**: Phê duyệt $\rightarrow$ `KNOWLEDGE_EXCAVATION`.
