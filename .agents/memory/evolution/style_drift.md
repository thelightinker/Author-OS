# Style Drift Log & Voice Calibration

> Ghi nhận các điểm lệch giọng văn, thói quen sáo ngữ lặp lại của AI trong quá trình viết các chương sách để tiến hành nắn chỉnh kịp thời.

---

## 1. Known AI Drift Traps (Các Bẫy Lệch Giọng Điển Hình)

- **Bẫy Đơn Điệu Nhịp Câu (Monotone Cadence Drift)**:
  - *Hiện tượng*: AI có xu hướng viết toàn bộ các câu có độ dài đều chằn chặn 15–20 từ.
  - *Cách sửa*: Luôn xen kẽ các cú đấm dứt khoát 1–6 từ ("Không phải vì thiếu động lực. Mà vì kiệt sức.") sau một câu phân tích dài phức hợp.
- **Bẫy Tóm Tắt Trừu Tượng (Abstract Summation Trap)**:
  - *Hiện tượng*: Khi chuyển đoạn, AI hay dùng các cụm từ đệm sáo rỗng: *"Tóm lại", "Nói cách khác", "Điều này cho thấy bức tranh toàn cảnh..."*.
  - *Cách sửa*: Bỏ hoàn toàn câu đệm, nhảy thẳng vào chi tiết hiện trường hoặc đưa ra một câu hỏi tự phản tỉnh dứt khoát.
- **Bẫy Giọng Guru Giáo Điều (Preachy Guru Drift)**:
  - *Hiện tượng*: Sử dụng đại từ nhân xưng dạy bảo: *"Bạn hãy nhớ rằng", "Chúng ta nên...", "Đừng bao giờ..."*.
  - *Cách sửa*: Kéo về vị thế người đồng đội: *"Tôi đã từng...", "Có những đêm...", "Chúng ta cùng nhìn lại..."*.
- **Bẫy Tối Ưu Hóa Cực Đoan (Extreme Optimization Drift)**:
  - *Hiện tượng*: Dùng từ ngữ đao to búa lớn, ép buộc hy sinh: *"dồn toàn lực giải quyết dứt điểm", "duy nhất một mục tiêu chuyển hóa", "nói không với chín mươi chín phần trăm những việc còn lại"*.
  - *Cách sửa*: Trở về tinh thần **HUMAN FIRST**. Tiêu điểm là sự ưu tiên có chủ đích trong một giai đoạn; không triệt tiêu các nhánh rẽ nuôi dưỡng tâm hồn (sức khỏe, quan hệ, niềm vui bình dị). Có giai đoạn Tiêu điểm là phục hồi thân tâm hay tìm lại phương hướng.
- **Bẫy Trộn Lẫn Ẩn Dụ (Mixed Metaphors Trap — KU-5STAR-003)**:
  - *Hiện tượng*: Nhồi nhét 4–5 ẩn dụ khác nhau vào cùng 1 chương (nước sôi 60 độ, quân domino, bộ nhớ đệm máy tính, tấm đệm giảm xóc).
  - *Cách sửa*: Áp dụng quy tắc **1 Metaphor duy nhất cho toàn chương** (`five_star`). Chọn ẩn dụ có tính chất vật lý tương thích 100% với bản chất vấn đề (với sự chú ý và Tiêu điểm: dùng **Dòng Nước**).
- **Bẫy Gán Ghép Cơ Chế Thần Kinh Giả Tạo (Ungrounded Mechanism / Neuro-Babble)**:
  - *Hiện tượng*: Tùy tiện lôi "dopamine", "liên kết nơ-ron", "cơ chế sinh hóa" vào giải thích tâm lý hành vi.
  - *Cách sửa*: Cấm tiệt neuro-babble; kéo về quan sát nội tâm và trải nghiệm tâm lý thực tế đời thường.

---

## 2. Regression Rules & Calibration History
- **2026-10-01**: Khởi tạo baseline từ Global Author Profile V2.0 và The Lightinker Identity.
- **2026-10-12**: Hiệu chỉnh chu kỳ Chương 02: Khóa quy tắc 1 Metaphor duy nhất (Dòng Nước), chuẩn hóa liêm chính tự sự S-003 (xem nhiều/không ghi chép), tái định vị Tiêu Điểm Human First, rà soát khử trùng lặp liên chương (Cross-Chapter Dedup).

---

## 3. Feedback Carry-Forward Register

> Ghi nhận các chỉ dẫn điều chỉnh viết mà tác giả đã xác nhận là pattern lặp lại xuyên section/chương.  
> Crafter đối chiếu mục này trước khi chấp bút section mới.

### 📌 Pattern 1: Trùng Lặp Giác Quan & Mô Típ Nhân Vật Liên Chương (Cross-Chapter Redundancy)
- **Pattern**: Chương sau lặp lại chi tiết mô tả cơ thể ("vai mỏi nhừ, mắt căng tức dán vào màn hình", cảnh 5h chiều trống rỗng) và mô típ so sánh đối lập 2 người (bận rộn việc nhỏ vs trôi dạt xem video ngắn) đã được chương trước giải quyết trọn vẹn.
- **Feedback của tác giả**: Không lặp lại mô tả hay cấu trúc đã xử lý ở chương trước. Chương sau phải bắt nhịp tiếp nối từ nấc nhận thức mới của người đọc (`Reader Progression`).
- **Scope áp dụng**: Toàn bộ các đoạn mở đầu (00_open) và chuyển tiếp giữa các chương.

### 📌 Pattern 2: Độc Quyền Một Ẩn Dụ Trục Xuyên Suốt (Single Governing Metaphor)
- **Pattern**: Rải nhiều ẩn dụ cạnh tranh nhau trong một chương, gây ô nhiễm thị giác và làm loãng tâm trí độc giả.
- **Feedback của tác giả**: Đúng 1 metaphor duy nhất cho toàn chương (`five_star`), và ẩn dụ đó phải trùng khớp 100% tính chất vật lý với bản chất vấn đề (ví dụ: Dòng Nước khơi thông dòng chính vs rạch rãnh mương nông).
- **Scope áp dụng**: Thiết kế kiến trúc chương và chấp bút toàn bộ các sections.

### 📌 Pattern 3: Liêm Chính Tự Sự Tuyệt Đối & Cấm Bịa Đặt Chi Tiết Ký Ức (Story Integrity Invariant)
- **Pattern**: Tự ý suy diễn các chi tiết hư cấu thêm vào ký ức tác giả (như bịa tác giả "cặm cụi ghi chép vào sổ tay", bịa bối cảnh "môi trường đại học chuyên ngành kỹ thuật", bịa "khách hàng không trả tiền...").
- **Feedback của tác giả**: *"câu chuyện đang sai lệch kìa tôi ko cs ghi chép nhưng xem rất nhiều"*. Thời cấp ba tác giả chỉ xem bạt mạng nội dung, không hề ghi chép; giai đoạn sau học sâu hóa học và tự kiếm tiền. CẤM TUYỆT ĐỐI thêm thắt chi tiết ngoài Confirmed Facts.
- **Scope áp dụng**: Toàn bộ các sections sử dụng Story Bank (`S-XXX`).

### 📌 Pattern 4: Tiêu Điểm Tự Nhiên & Bản Sắc Human First
- **Pattern**: Đẩy Tiêu điểm thành bài toán tối ưu hóa cực đoan, hy sinh mọi mặt đời sống, coi việc tập trung như một sự cưỡng bức khắc khổ.
- **Feedback của tác giả**: Tiêu điểm là sự ưu tiên có chủ đích trong một giai đoạn; không triệt tiêu các nhánh rẽ nuôi dưỡng tâm hồn (sức khỏe, quan hệ, niềm vui bình dị). Có những giai đoạn Tiêu điểm là phục hồi thân tâm hay tìm lại phương hướng. Bản chất của Tiêu điểm là thoát khỏi trôi dạt phân tán để ở lại đủ lâu, không phải là làm việc mạnh hơn hay kỷ luật sắt.
- **Scope áp dụng**: Các chương về Tiêu điểm, Kế hoạch 12 tuần và Hệ thống hành động (Part I, Part II, Part III).

### 📌 Pattern 5: Mở Rộng Điểm Xuất Phát Của Độc Giả (Full-Spectrum Reader Inclusivity)
- **Pattern**: Mặc định nhân vật trong sách là người chăm chỉ, bận rộn với email và to-do list.
- **Feedback của tác giả**: Độc giả là một phổ nhận thức linh hoạt (người bận việc nhỏ, người trôi dạt trì hoãn, người sống bình dị chưa rõ phương hướng). Không phán xét, mở rộng điểm xuất phát đa chiều để người đọc tự nhận ra mình.
- **Scope áp dụng**: Mở đầu các chương và mọi đoạn phân tích hành vi độc giả.

### 📌 Pattern 6: Tinh Giản Hệ Từ Vựng Ẩn Dụ & Điều Kiện Biên Thực Tế (Metaphor Vocabulary Pruning & Real-World Boundaries)
- **Pattern**: Lạm dụng quá nhiều biến thể rải rác của cùng một ẩn dụ (rãnh mương, hồ chứa, cửa xả, cánh đồng, bãi bồi, lòng sông), hoặc vô tình tạo cảm giác ngộ nhận rằng ai cũng có sẵn lượng năng lượng dồi dào như nhau, cứ gom đủ lực là cuốn trôi mọi trở ngại.
- **Feedback của tác giả**:
  - Dòng nước chỉ diễn tả hướng đi và sự phân tán của sự chú ý, không phải quy luật rằng gom đủ lực thì mọi trở ngại đều bị cuốn trôi. Năng lượng, sức khỏe, hoàn cảnh mỗi người khác nhau; có giai đoạn cần khơi sâu, có giai đoạn cần phục hồi, giảm tải hoặc tìm lại phương hướng.
  - Tinh giản hệ hình ảnh gọn gàng đúng 4 khái niệm: *rãnh nông, dòng chính, vùng đất gồ ghề, lưu vực*. Không ép câu nào cũng phải có nước.
  - Khóa Dòng Nước làm mạch xuyên suốt 3 chương đầu (Chương 1: Dòng chảy phân tán $\rightarrow$ Chương 2: Khơi sâu dòng chính $\rightarrow$ Chương 3: Lưu vực nâng đỡ đời sống).
- **Scope áp dụng**: Toàn bộ Part I (Chương 01, 02, 03) và các tài liệu kiến trúc.

### 📌 Pattern 7: Kỷ Luật Thực Thi Bắt Buộc Manuscript Formatting (Mandatory Manuscript Formatting Pre-flight)
- **Pattern**: Agent không tự giác kích hoạt và rà soát triệt để quy chuẩn `manuscript-formatting` trước khi nộp bản thảo hoặc xuất file PDF; để sót dấu em-dash dính liền chữ (`—`), colon kịch tính, ngắt dòng staccato làm vỡ bố cục trình bày, khiến tác giả phải soi và yêu cầu sửa thủ công.
- **Feedback của tác giả**: *"lỗi formating nè / lưu lỗi agent ko dùng manuscrip format lm cứ phk sửa ?"*
- **Quy tắc bắt buộc (Hard Pre-Flight Gate)**:
  - BẮT BUỘC thực thi quy trình rà soát `manuscript-formatting` (từ `FORMAT-001` đến `FORMAT-006`) trên 100% các file `sections/*.md` trước khi bàn giao cho tác giả hoặc chạy xuất bản PDF.
  - Quét sạch mọi dấu em-dash dính chữ (`—`), colon kịch tính không cần thiết, staccato line-breaks. Tái cấu trúc cú pháp (Syntactic Re-anchoring) thay vì để dấu nẹp lười biếng.
  - Phải kiểm tra visual layout của bản xuất (PDF/in ấn) để đảm bảo không có lỗi dãn dòng hay xô lệch justify trước khi thông báo hoàn tất.
- **Scope áp dụng**: Toàn bộ chu kỳ sản xuất chương (Chapter Cycle), toàn bộ các bản nháp và mọi tác vụ xuất bản PDF.


