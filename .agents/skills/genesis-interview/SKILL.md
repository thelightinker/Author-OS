---
name: genesis-interview
description: "Khai mở dự án sách phi hư cấu: Điều phối phỏng vấn Socratic 4 nhóm câu hỏi để chiết xuất Tuyên ngôn dự án (Manifesto), Chân dung tác giả, Lời hứa bìa sách, Quy chuẩn giọng văn (Voice) và khởi tạo ma trận khái niệm terms.md cùng story_bank.md. Kích hoạt khi bắt đầu viết sách mới hoặc khi tác giả muốn tái định vị toàn bộ cuốn sách."
when_to_use: "Khi bắt đầu một dự án sách mới, khởi động pha Book Genesis hoặc thực hiện tái định vị lớn (Pivot) tuyên ngôn cuốn sách."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Genesis Interview: Khai Mở Dự Án & Thiết Lập Bộ Gen Sách

> "Một cuốn sách phi hư cấu xuất sắc không bắt đầu từ mục lục chi tiết, mà bắt đầu từ một luận đề nhức nhối, một lời hứa không thể chối từ và một giọng văn độc bản."

## 0. Schema Authority & Context-Aware Grounding

- **Schema Authorities**:
  - `templates/manifesto-template.md`: Chuẩn cấu trúc bắt buộc cho `manifesto.md` (Luận đề, Độc giả 2h sáng, Lời hứa, Điều kiện biên).
  - `templates/voice-template.md`: Chuẩn cấu trúc bắt buộc cho `voice.md` (Đại từ xưng hô, 5–10 đoạn mẫu, anti-patterns, từ cấm).
- **Quy tắc Grounding**:
  - Khi khởi tạo `manifesto.md` hoặc `voice.md`, bắt buộc ground vào schema của template tương ứng.
  - **Context-Aware Exemption**: Nếu template hoặc artifact đã có mặt trong ngữ cảnh phiên làm việc hoặc đã được nạp qua workflow, **KHÔNG đọc lại** để tránh lãng phí token (Anti-Spam Invariant).

---

## 1. Giao Thức Phỏng Vấn Thích Ứng (Adaptive Socratic Inquiry Protocol)

> **Nguyên tắc cốt lõi**: Khóa chặt mục tiêu cần khai phá, không đếm số lượng câu hỏi. "Hiểu người trước, viết sau" (COLLAB-011). Hỏi từng câu một có giá trị thông tin cao nhất, thích ứng theo câu trả lời của tác giả.

1. **Quy tắc 1 Câu Hỏi / 1 Lượt & Giá Trị Thông Tin Cao Nhất (High-Information-Value Inquiry)**:
   - Gửi chính xác một câu hỏi có giá trị thông tin cao nhất tại một thời điểm (`Ask exactly one question at a time; wait for the answer before asking the next`).
   - Tuyệt đối cấm xả một chùm 3–4 câu hỏi cùng lúc làm loãng tiêu điểm và gây quá tải cho tác giả.
   - Không hỏi lan man, không hỏi những điều tác giả đã nói hoặc đã có trong `MEMORY.md`. Tập trung bóc tách điểm mù nhận thức, sự thật trần trụi và nguồn gốc trải nghiệm.

2. **Cổng Kiểm Tra Đủ Ngữ Cảnh Trước Khi Sinh (Understand Before Write Gate)**:
   - Trước khi khởi tạo hoặc trình duyệt bất kỳ artifact nào (`manifesto.md`, `voice.md`, `terms.md`, `story_bank.md`, `book_spine.md`):
     - Tự vấn: *Mình đã hiểu đủ góc nhìn, giá trị, trải nghiệm và ý định thật của tác giả chưa? Hay mình đang tự suy diễn/bịa đặt để lấp đầy file?*
     - Nếu còn thiếu dữ kiện cốt lõi: **BẮT BUỘC DỪNG LẠI VÀ HỎI/PHỎNG VẤN (PROBE OR YIELD, NEVER INVENT)**.
     - Cấm tuyệt đối thói quen thấy tác giả nói 1 câu ngắn ("ok", "anh muốn viết lại...") là vội vã sinh trọn file và thúc giục ký duyệt.
   - Luôn phân biệt rạch ròi 5 tầng nhận thức (`COLLAB-012`): Điều tác giả nói (`USER_STATED`) không được phép nhập nhèm với suy luận của Agent (`AGENT_INFERENCE`) hoặc giả thuyết (`HYPOTHESIS`). Chi tiết chưa biết (`UNKNOWN`) phải giữ nguyên là chưa biết.

3. **Bộ Khung Mục Tiêu Khai Phá (Core Discovery Goals)**:
   - *Mục tiêu 1 — Điểm Nhức Nhối & Luận Đề Đột Phá (Core Thesis)*: Đào sâu niềm tin sai lầm phổ biến trong ngành, sự thật trần trụi và thông điệp một câu duy nhất sống sót sau 5 năm.
   - *Mục tiêu 2 — Độc Giả Mục Tiêu & Lời Hứa Trang Bìa (Cover Promise)*: Xác định trạng thái bế tắc lúc 2h sáng và sự chuyển hóa từ Trạng thái A (bất lực) sang B (tự chủ).
   - *Mục tiêu 3 — Ma Trận Khái Niệm (`terms.md`)*: Bóc tách Khái niệm giải phóng, Phản đề độc hại cần lật đổ và Đích đến tối hậu.
   - *Mục tiêu 4 — Chân Dung Tác Giả & DNA Giọng Văn (`voice.md`)*: Đại từ xưng hô, các sáo ngữ cấm kỵ và văn bản mẫu thực tế của chính tác giả.
   - *Mục tiêu 5 — Kho Giai Thoại & Ký Ức Thực Tế (`story_bank.md`)*: Phỏng vấn trực tiếp bóc tách câu chuyện thật (0% bịa đặt, bắt buộc có 5 trường Epistemic Breakdown).

---

## 2. Các Bước Thực Thi Chi Tiết

1. **Phỏng vấn thích ứng tuần tự (Adaptive Sequential Inquiry)**:
   - Khởi động bằng câu hỏi khai mở trọng tâm nhất. Sau mỗi câu trả lời, phân tích xem đã đủ thông tin xác thực cho schema mục tiêu chưa.
   - Nếu phát hiện luận đề còn mơ hồ hoặc ngụy biện $\rightarrow$ đặt câu hỏi bẻ góc để thử thách hoặc làm sắc.
2. **Khởi tạo từng Sổ bộ Độc lập (Sequential Artifact Generation)**:
   - Chặng 1: Phỏng vấn đủ chiều sâu $\rightarrow$ Sinh `manifesto.md` $\rightarrow$ Thử tải $\rightarrow$ Gate 1 duyệt.
   - Chặng 2: Thu thập mẫu văn & giọng $\rightarrow$ Sinh `voice.md` $\rightarrow$ Gate 2 duyệt.
   - Chặng 3: Bóc tách hệ khái niệm từ luận đề $\rightarrow$ Sinh `terms.md` $\rightarrow$ Gate 3 duyệt.
   - Chặng 4: Phỏng vấn bóc tách câu chuyện thật (Cấm tự bịa) $\rightarrow$ Sinh `story_bank.md` $\rightarrow$ Gate 4 duyệt.
   - Chặng 5: Sinh `book_spine.md` & `promises.md` $\rightarrow$ Gate 5 duyệt.

---

## 3. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (Ghi chú phỏng vấn thô):
```
Tác giả là chuyên gia tài chính cá nhân 15 năm kinh nghiệm.
Ý tưởng: Muốn viết cuốn sách bảo mọi người ngừng ghi chép chi tiêu từng ly từng tí. Ghi chép chi tiêu là vô ích và làm người ta kiệt sức.
Luận điểm: Tự do tài chính đến từ việc kiểm soát 3 khoản chi lớn nhất (nhà cửa, xe cộ, đầu tư sự nghiệp) chứ không phải tiết kiệm ly cà phê 30k.
Giọng văn: Thực tế, hơi đanh thép, thẳng thắn, không dùng thuật ngữ học thuật phức tạp.
```

### Output (`manifesto.md` sơ bộ & `terms.md`):
```markdown
# Book Manifesto: Nghịch Lý Tiết Kiệm

## 1. Core Thesis (Luận đề Cốt lõi)
Tự do tài chính không bao giờ được tạo ra từ việc tự đày đọa bản thân bằng việc ghi chép từng ly cà phê 30,000đ. Nó là kết quả của việc ra quyết định chính xác tại 3 điểm đòn bẩy lớn: Nơi ở, Phương tiện và Năng lực tạo dòng tiền.

## 2. Target Reader & 2 AM Pain
Dân văn phòng độ tuổi 25–35, kiếm được thu nhập khá nhưng luôn sống trong cảm giác tội lỗi mỗi khi chi tiêu cho bản thân, cảm thấy kiệt sức với các app tài chính cá nhân sau 3 tuần sử dụng.

## 3. Terms Matrix Initialization
- **Khái niệm giải phóng**: "Điểm Đòn Bẩy Tài Chính" — Tập trung 95% năng lượng vào 3 quyết định lớn mỗi 5 năm thay vì 100 quyết định nhỏ mỗi ngày.
- **Phản đề**: "Bẫy Vi Tiết Kiệm" (Micro-Frugality Trap) — Cảm giác an tâm giả tạo khi bớt một cốc trà sữa nhưng lại mua một chiếc ô tô vượt quá 6 tháng thu nhập.
- **Đích đến**: Tự do nhận thức — Chi tiêu không cảm giác tội lỗi và tài sản ròng tự tích lũy.
```

---

## 4. Tiêu Chuẩn Nghiệm Thu

- [ ] Trích xuất rõ ràng Core Thesis không thể nhầm lẫn.
- [ ] Xác lập rõ ràng độc giả mục tiêu và tình huống nhức nhối lúc 2h sáng.
- [ ] Khởi tạo thành công `manifesto.md`, `voice.md`, `terms.md`, `story_bank.md`.
- [ ] Không có từ ngữ sáo rỗng hoặc mô tả mơ hồ.

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `falsification-steelmanning` | Đưa luận đề cốt lõi trong `manifesto.md` qua kiểm định đối nghịch và xác lập điều kiện biên trước Gate 1. |
| `spine-architecture` | Hiện thực hóa tuyên ngôn và lời hứa bìa sách thành khung xương 3 tầng với chuỗi nhân quả `Leads-to`. |
