---
name: humanizer
description: |
  Biên tập văn xuôi loại bỏ các dấu hiệu AI writing (staging, not-X-but-Y, one-line closers, triads, dashes, bold labels, inflated claims). BẮT BUỘC kích hoạt khi biên tập và trau chuốt văn xuôi để văn bản đọc tự nhiên như con người, giữ nguyên sự thật và không bịa đặt.
license: MIT
metadata:
  version: "3.2.0"
---

# Humanizer: Khử Dấu Vết AI Trong Văn Xuôi

> "Biên tập lại câu chữ để văn bản đọc như một con người thực sự viết cho một độc giả cụ thể. Giữ nguyên toàn bộ sự thật và luận điểm. Tuyệt đối không bịa đặt."

---

## 📌 Phân loại & Ranh giới Kích hoạt
- **`when_to_use`**: Kích hoạt khi rà soát và biên tập bản thảo các section, loại bỏ mẫu hình câu cú máy móc của LLM (staging, one-line closer, not-X-but-Y, forced triads, lạm dụng em-dash, stock AI vocabulary).
- **Ranh giới bất biến (Hard Airbags)**:
  1. **Zero Invention**: Cấm thêm thắt tình tiết, con số, trích dẫn hoặc chi tiết cảm giác không có trong bản gốc.
  2. **Voice Preservation**: Đối chiếu `.agents/memory/author/voice.md` để giữ nhịp điệu và từ vựng đặc trưng của tác giả.
  3. **No Structural Inflation**: Cấm biến câu bình thường thành châm ngôn hoặc bài học đạo đức giả tạo.

---

## 1. Quy Trình 4 Bước Biên Tập (How to Work)

1. **Đánh dấu mẫu hình (Mark the Tells)**:
   - Đọc lướt toàn văn và đánh dấu các dấu hiệu AI từ mạnh đến yếu: Not-X-but-Y, One-line closers, Forced triads, Em-dash dày đặc, Từ khóa máy móc (delve, tapestry, minh chứng cho, bức tranh toàn cảnh...).
2. **Soạn bản sửa đổi (Draft the Rewrite)**:
   - Giữ lại 100% luận điểm và dữ liệu có thật.
   - Diễn đạt trực diện, dùng từ ngữ cụ thể, đời thường. Cắt bỏ các câu đệm staging không mang lại thông tin mới cho độc giả.
3. **Đối chiếu & Rà soát (Check the Draft)**:
   - Đọc thành tiếng nhẩm trong đầu. Câu văn có nhịp thở tự nhiên không? Có bị dàn hàng ngang đều chằn chặn không?
   - Kiểm tra xem có vô tình làm rơi số liệu hay bịa thêm chi tiết cảm giác nào không.
4. **Hoàn thiện văn bản (Final Version)**:
   - Xen kẽ câu ngắn (4–8 từ) với câu phức (20–30 từ). Đảm bảo mỗi câu đều mang một giá trị thông tin mới.

---

## 2. Danh Mục 6 Nhóm Dấu Hiệu AI Cốt Lõi (Core Tells)

### Nhóm A: Dàn Dựng Thay Vì Nêu Thực Tế (Staging Instead of Stating)
1. **Not X but Y**: Mẫu câu "không chỉ là X mà còn là Y", "đây không phải là X, mà là Y", "không còn là X nữa mà đã trở thành Y".
   - *Cách sửa*: Nêu thẳng khẳng định Y. Chỉ giữ tương phản khi vế X đính chính một ngộ nhận có thật của độc giả.
2. **One-line closers & Dramatic fragments**: Câu chốt đứng một mình để làm màu ("Đó chính là chìa khóa.", "Hãy đọc lại điều đó một lần nữa.", "Không thỏa hiệp. Không lùi bước.").
   - *Cách sửa*: Cắt bỏ hoàn toàn hoặc gộp vào đoạn văn mang dữ kiện mới.
3. **Mệnh đề tỏ ra sâu sắc (Pseudo-profound sayings)**: "câu hỏi thực sự ở đây là", "bản chất cốt lõi", "về cơ bản", "X không chỉ là công cụ mà là tấm gương".
   - *Cách sửa*: Cắt bỏ lời dẫn hoa mỹ, đi thẳng vào bản chất vấn đề.

### Nhóm B: Nhịp Điệu Máy Móc (Rhythm by Rule)
4. **Forced triads**: Luôn ép mọi thứ thành bộ 3 tính từ hoặc 3 mệnh đề song song.
   - *Cách sửa*: Giữ 1–2 ý quan trọng nhất hoặc diễn đạt bất đối xứng tự nhiên.
5. **Dashes everywhere (—)**: Lạm dụng dấu gạch ngang em-dash ở hầu hết các câu để tạo kịch tính gượng ép.
   - *Cách sửa*: Dùng dấu phẩy, liên từ hoặc tách câu tự nhiên.
6. **Độ dài câu đều chằn chặn**: Mọi câu đều dài 15–20 từ tạo cảm giác monotone ru ngủ.
   - *Cách sửa*: Phá vỡ cấu trúc; đặt câu cực ngắn bên cạnh câu dài giàu nhạc tính.

### Nhóm C: Phóng Đại & Ngôn Ngữ Bán Hàng (Inflation & Sales Language)
7. **Tâng bốc ý nghĩa (Inflated significance)**: "bước ngoặt mang tính cách mạng", "cột mốc lịch sử", "ngọn hải đăng hy vọng", "minh chứng sống động".
   - *Cách sửa*: Dùng từ ngữ trung thực, phản ánh đúng tầm mức sự việc.
8. **Từ vựng AI đặc trưng**: "bức tranh đa diện", "len lỏi vào từng ngóc ngách", "nuôi dưỡng", "khắc họa", "định hình bối cảnh", "không ngừng phát triển".
   - *Cách sửa*: Thay bằng từ ngữ chuẩn xác, gãy gọn, giàu tính hình ảnh đời thực.

### Nhóm D: Định Dạng Cứng Nhắc (Formatting by Rule)
9. **Bold labels**: Bôi đậm từ khóa đầu mỗi gạch đầu dòng theo thói quen máy móc.
   - *Cách sửa*: Viết thành đoạn văn văn xuôi hoàn chỉnh.
10. **Staccato line-breaks**: Tách mỗi câu thành một dòng như bài đăng mạng xã hội.
    - *Cách sửa*: Tổ chức thành các đoạn văn mạch lạc 3–5 câu.

### Nhóm E: Giải Thích Thừa Cho Sai Độc Giả (Wrong Reader)
11. **Kể lể lại những gì độc giả đã biết**: Giải thích lại bối cảnh cũ thay vì đưa ra nhận định hoặc phân tích mới.
12. **Mô tả văn bản thay vì chủ đề**: Nói về cách viết ("đoạn dưới đây so sánh...", "bảng sau sẽ cho thấy...") thay vì nói về nội dung.

---

## 3. Khi Nào Giữ Lại (When Not to Act)

- Giữ nguyên các từ ngữ riêng biệt nếu nằm trong:
  - Trích dẫn nguyên văn của nhân vật hoặc tác giả.
  - Các cụm từ phong cách đã được đăng ký trong `.agents/memory/author/voice.md` và Gold Passages.
  - Các thuật ngữ chuyên môn độc quyền trong `Books/<book_slug>/foundation/terms.md`.

---

## 4. Tài Liệu Tham Khảo Mở Rộng
- Chi tiết ví dụ Before / After cho từng lỗi: xem [ai_writing_tells.md](references/ai_writing_tells.md).
