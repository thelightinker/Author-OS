---
description: "Quy trình tổng hợp toàn bộ bản thảo: Rà soát tính nhất quán liên chương, kiểm định mạch Leads-to, làm mượt chuyển tiếp, biên dịch toàn sách deterministic, chẩn đoán giọng văn read-only, đọc mù Layer 3 (Cold Read) và đóng gói xuất bản."
---

# Workflow: Book Assembly (/book-assembly)

> **Mục tiêu**: Hợp nhất toàn bộ các chương đã qua kiểm định riêng lẻ thành một bản thảo hoàn chỉnh thống nhất: bảo đảm tính nhất quán của hệ thống thuật ngữ, kiểm tra độ liền mạch của chuỗi nhân quả `Leads-to`, biên dịch bản thảo toàn cuốn tự động bằng compiler deterministic, quét chẩn đoán giọng điệu (Read-Only Voice Audit), thực thi kiểm định mù Layer 3 (Cold Read) và đóng gói xuất bản.

---

## ⚡ Chỉ Dẫn Chạy Node Độc Lập (Standalone Invocation)

Khi cần thực hiện kiểm định hoặc thao tác độc lập trên toàn bộ bản thảo:
- **Lệnh cú pháp**: `/book-assembly --node <NODE_NAME>`
- *Ví dụ*:
  - Chạy lại biên dịch bản thảo: `/book-assembly --node MANUSCRIPT_COMPILATION`
  - Chạy lại kiểm định Đọc Mù Layer 3: `/book-assembly --node COLD_READ`
  - Quét chẩn đoán giọng văn: `/book-assembly --node VOICE_AUDIT`
  - Kiểm tra tính nhất quán: `/book-assembly --node CONSISTENCY_PASS`

---

## 🔄 Chi Tiết 8 Node Hợp Nhất & Kiểm Định Cuối Cùng

### [NODE 1: CONSISTENCY_PASS]
- **Vai trò thực thi**: `book-architect` nạp skill `spine-architecture`.
- **Thực thi bổ trợ cơ học**: Chạy `python .agents/scripts/memory_cli.py audit-continuity` trước tiên để kiểm tra nhị phân (0 tokens).
- **Input**: `terms.md`, `promises.md`, `story_bank.md`, toàn bộ `chapters/*/card.md` và `draft.md`.
- **Human Gate**: `false`
- **Mục tiêu hành động**:
  1. *Kiểm toán Thuật ngữ*: Bảo đảm các khái niệm trong `terms.md` được dùng nhất quán.
  2. *Thanh lý Cam kết*: Đối chiếu `promises.md` để xác nhận mọi lời hứa gieo ở các chương đầu đều đã được trả nợ trọn vẹn.
  3. *Story Bank Duplication Audit*: Quét toàn bộ trường `Used In` trong `story_bank.md` để bảo đảm **0 giai thoại nào bị kể lặp lại 2 lần**.
  4. *Cognitive Payload Registry Audit*: Quét Sổ bộ nhận thức trong `summaries.md` để đối chiếu chéo giữa các chương, đảm bảo **0 hiện tượng lặp ý toàn sách (Whole-Book Semantic De-duplication)**.
- **DoD**: Báo cáo kiểm toán nhất quán hoàn tất, 0 vi phạm thuật ngữ hay trùng lặp nhận thức.
- **Transition Path**: `CONSISTENCY_PASS` $\rightarrow$ `ARGUMENT_THREAD_CHECK`.

---

### [NODE 2: ARGUMENT_THREAD_CHECK]
- **Vai trò thực thi**: `book-architect` nạp skill `falsification-steelmanning`.
- **Input**: Chuỗi các dòng `Governing Line` và `Leads-to` trong `book_spine.md` đối chiếu với kết thúc từng chương (`04_close.md`).
- **Human Gate**: `false`
- **Mục tiêu**:
  - Xác nhận rằng cái kết của Chương N tạo ra sự tò mò bức thiết dẫn thẳng vào vấn đề của Chương N+1.
- **DoD**: Toàn bộ ranh giới liên chương vượt qua bài kiểm tra chuỗi domino nhận thức.
- **Transition Path**: `ARGUMENT_THREAD_CHECK` $\rightarrow$ `TRANSITION_SMOOTHING`.

---

### [NODE 3: TRANSITION_SMOOTHING]
- **Vai trò thực thi**: `chapter-crafter` nạp skill `editorial-revision`.
- **Input**: Các đoạn mở đầu (`00_open.md`) và kết thúc (`04_close.md`) của các chương giáp ranh.
- **Human Gate**: `false`
- **Mục tiêu**:
  - Gọt giũa các câu nối chuyển tiếp (Bridge sentences) giữa các chương để trải nghiệm đọc mượt mà, tự nhiên.
  - Sửa đổi phẫu thuật tối thiểu, không làm xáo trộn cấu trúc nội dung bên trong chương.
- **DoD**: Các đoạn chuyển tiếp liên chương được làm mượt hoàn tất.
- **Transition Path**: `TRANSITION_SMOOTHING` $\rightarrow$ `MANUSCRIPT_COMPILATION`.

---

### [NODE 4: MANUSCRIPT_COMPILATION]
- **Thực thi**: L0 Direct (Deterministic Compiler stdlib — Zero LLM Intervention).
- **Lệnh thực thi**: `python scripts/assemble_chapter.py --all --commit`
- **Input**: Toàn bộ `Books/<book_slug>/chapters/*/draft.md`.
- **Output Artifact**: `Books/<book_slug>/outputs/manuscript.md` (Artifact trung gian chuẩn mực trước mọi bước whole-book audit).
- **Human Gate**: `false`
- **Mục tiêu**:
  - Tự động sắp xếp các chương theo thứ tự tự nhiên (`ch_01`, `ch_02`, ...).
  - Ghép nối các bản thảo chương thành `outputs/manuscript.md` kèm header và phân cách trang chuẩn markdown (`\n\n---\n\n`).
  - Kiểm tra tính đầy đủ của 100% các chương đã hoàn thành (exit code 0).
- **DoD**: File `outputs/manuscript.md` được sinh ra tự động và sẵn sàng cho các pass audit mù.
- **Transition Path**: `MANUSCRIPT_COMPILATION` $\rightarrow$ `VOICE_AUDIT`.

---

### [NODE 5: VOICE_AUDIT]
- **Vai trò thực thi**: `chapter-crafter` trong chế độ **Diagnostic Read-Only Pass** (tuân thủ quy chuẩn Voice Audit Scan tại [manuscript-cold-read.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/manuscript-cold-read.md)).
- **Input**: `voice.md` và file bản thảo hợp nhất `outputs/manuscript.md`.
- **Output Artifact**: `outputs/voice_drift_report.md`.
- **Human Gate**: `false`
- **Nguyên tắc bất biến**:
  - **TUYỆT ĐỐI CẤM SỬA VĂN BẢN TRONG NODE NÀY**: Node chẩn đoán thuần túy (Diagnostic Only).
  - Quét toàn bộ bản thảo để phát hiện độ lệch giọng điệu, tần suất từ cấm.
- **DoD**: File `outputs/voice_drift_report.md` được sinh ra, 0 sửa đổi phát sinh trên bản thảo.
- **Transition Path**: `VOICE_AUDIT` $\rightarrow$ `COLD_READ`.

---

### [NODE 6: COLD_READ]
- **Vai trò thực thi**: `quality-auditor` trong **Whole-Book Review Mode** (Critic độc lập — tuân thủ quy chuẩn SSOT tại [manuscript-cold-read.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/manuscript-cold-read.md)).
- **Hàng rào mù tuyệt đối (Absolute Blind Barrier - `SEQ-006`)**:
  - **ĐƯỢC ĐỌC**: Duy nhất file `outputs/manuscript.md` vừa được biên dịch từ Node 4.
  - **CẤM ĐỌC**: `book_spine.md`, `terms.md`, `summaries.md`, `manifesto.md`, hay bất kỳ biên bản ghi nhớ nào.
  - Auditor đóng vai độc giả mua sách ngoài tiệm: đánh giá trải nghiệm đọc xuyên suốt từ đầu đến cuối.
- **10 Giả Thuyết Thẩm Định Đòn Bẩy Cao (10 High-Leverage Non-Fiction Hypotheses)**:
  1. *Transformation Payoff*: Lời hứa cốt lõi có được trả nợ trọn vẹn ở trang cuối không?
  2. *Chapter Rent*: Mỗi chương có tự trả tiền thuê nhà không?
  3. *Whole-Book Semantic De-duplication*: Có chương nào khám phá lại điều chương trước đã chứng minh xong không?
  4. *Cognitive Escalation*: Độ leo thang nhận thức có liền mạch không?
  5. *Drop-Off Danger Zones*: Vùng trũng gây bỏ đọc nằm ở đâu?
  6. *The Dinner Table Metric*: Khả năng truyền miệng trong 2 phút trên bàn ăn.
  7. *Counter-Intuitive Reframe*: Có ít nhất 2–3 góc nhìn bẻ gãy trực giác thông thường không?
  8. *Friction & Reality Contact*: Tác giả có xử lý các rào cản và ma sát thực tế khi áp dụng không?
  9. *Insight Density*: Mật độ đòn bẩy nhận thức/1,000 từ có đủ cao không?
  10. *Ending Payoff & Autonomy*: Lời kết có giải phóng và trao quyền tự chủ cho độc giả không?
- **Phân Tầng Rủi Ro Định Tính**: `LOW / MEDIUM / HIGH RISK` kèm bằng chứng trích dẫn hiện trường cụ thể.
- **4 Phán Quyết Biên Tập Tư Vấn**: `Ship`, `Conditional`, `Major Revise`, `Kill`.
- **DoD**: Báo cáo `outputs/cold_read_assessment.md` hoàn tất với phán quyết rõ ràng.
- **Cấu trúc hàng đợi sửa đổi (Actionable Fix Queue)**: Cuối `outputs/cold_read_assessment.md` phải có mục `## Danh sách cần sửa` gồm tối đa 8 dòng, xếp theo mức ảnh hưởng đến độc giả từ cao xuống thấp. Mỗi dòng đúng định dạng: `- Tên chương đúng như trong bản thảo | Tiêu đề H2 đúng như trong bản thảo | <mã_bệnh_học> | <targeted_action> | một câu mô tả lỗi nhìn từ phía độc giả`. Hành động sửa chỉ được chọn trong danh sách hành động của skill `editorial-revision`. Không nhắc tên file hay mã chương nội bộ (người đọc mù chỉ thấy bản thảo). Nếu không có lỗi đáng sửa, ghi `Không có`.
- **Transition Path**: `COLD_READ` $\rightarrow$ `GATE_4_FINAL`.

---

### [NODE 7: GATE_4_FINAL]
- **Human Gate**: `true (Chủ quyền tác giả tối cao)`
- **Mục tiêu**: Trình báo cáo Đọc Mù (Cold Read Assessment) và Voice Drift Report cho tác giả đưa ra quyết định xuất bản cuối cùng.
- **Hai lựa chọn cho tác giả**: Trình bày cho tác giả hai lựa chọn bằng lời thường: (A) Xuất bản ngay. (B) Sửa theo danh sách cần sửa, một vòng, rồi xem lại. Nếu tác giả chọn B, xử lý TUẦN TỰ từng dòng trong danh sách, mỗi lần một dòng: tìm file bằng cách tìm tiêu đề H2 của dòng đó trong `chapters/*/sections/*.md`. Nếu không tìm được đúng một file thì bỏ dòng đó và báo tác giả. Với file tìm được: SECTION_REVISION (chỉ file đó, chỉ làm hành động ghi trong dòng, theo nguyên tắc sửa tối thiểu) rồi MECHANICAL_SCREEN rồi CHAPTER_ASSEMBLY của chapter-cycle cho chương đó. Khi xong mọi dòng, chạy lại MANUSCRIPT_COMPILATION và quay lại GATE_4_FINAL. Chỉ cho phép một vòng B. Lần quay lại chỉ còn lựa chọn A hoặc tác giả tự sửa tay. Không chạy lại COLD_READ trừ khi tác giả yêu cầu.
- **Nguyên tắc Chủ quyền Tác giả**: Báo cáo Đọc Mù chỉ đóng vai trò tư vấn chuyên môn. Tác giả có quyền quyết định `Ship` bất kể phán quyết; nếu tác giả ghi đè phán quyết biên tập, Orchestrator ghi nhận `DISSENT` vào `decisions.md` và tiến hành xuất bản.
- **Transition Path**: Tác giả chấp thuận (A) $\rightarrow$ `EXPORT`; Tác giả chọn (B) $\rightarrow$ Vòng sửa 1 lần $\rightarrow$ `MANUSCRIPT_COMPILATION` $\rightarrow$ `GATE_4_FINAL`.

---

### [NODE 8: EXPORT]
- **Vai trò thực thi**: `master-orchestrator`.
- **Input**: `outputs/manuscript.md` đã được duyệt ở Gate 4.
- **Output Artifacts**:
  - Hướng dẫn chuyển đổi sang PDF và EPUB (Pandoc/typst notes).
  - Đóng gói bản thảo hoàn chỉnh sẵn sàng phục vụ dàn trang.
- **DoD**: Bản thảo được đóng gói hoàn tất.
- **Transition Path**: `EXPORT` $\rightarrow$ `DONE`.