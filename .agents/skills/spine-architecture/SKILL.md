---
name: spine-architecture
description: "Kiến tạo khung xương sống 3 tầng cho cuốn sách (Part → Chapter → Governing Argument), thiết lập sợi chỉ nhân quả Leads-to kết nối liền mạch các chương, lập bảng cam kết đền đáp kỳ vọng độc giả (promises.md) và tính toán bán kính ảnh hưởng (Blast Radius) khi cấu trúc bị thay đổi. Kích hoạt khi thiết kế cấu trúc mục lục hoặc xử lý SPINE-FLAG."
when_to_use: "Khi thiết kế cấu trúc mục lục tổng thể của cuốn sách, liên kết lập luận Leads-to giữa các chương, hoặc khi có sự thay đổi cấu trúc cần tính toán bán kính ảnh hưởng (SPINE_CHECK)."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Spine Architecture: Thiết Kế Khung Xương Sách & Sợi Chỉ Leads-to

> "Một mục lục tồi là một danh sách các chủ đề rời rạc. Một mục lục xuất sắc là một chuỗi domino nhận thức: khi chương trước ngã xuống, nó tạo ra lực đẩy tất yếu bắt buộc chương kế tiếp phải xuất hiện."

## 0. Schema Authority & Context-Aware Grounding

- **Schema Authority**:
  - `templates/spine-template.md`: Chuẩn cấu trúc bắt buộc cho `book_spine.md` và `promises.md` (3-tier hierarchy, Governing Line, Leads-to link, Promise Tracker).
- **Quy tắc Grounding**:
  - Khi khởi tạo hoặc tái cấu trúc `book_spine.md`, bắt buộc ground vào schema của `spine-template.md`.
  - **Context-Aware Exemption**: Nếu template hoặc artifact đã có mặt trong ngữ cảnh phiên làm việc hoặc đã được nạp qua workflow, **KHÔNG đọc lại** để tránh lãng phí token (Anti-Spam Invariant).

---

## 1. Các Mức Độ Phân Giải Nhận Thức (Certainty-Driven Resolution Levels)

L0 $\rightarrow$ L3 là **các mức độ phân giải nhận thức (Resolution Levels / Zoom levels)**, **Không phải workflow 4 bước bắt buộc**.
Agent tự động lựa chọn mức độ phân giải tiếp theo căn cứ trên 3 yếu tố thực tế: (1) độ chắc chắn của ý tưởng, (2) trạng thái tài liệu hiện có, và (3) nhu cầu cộng tác thực tế của tác giả. Tuyệt đối không đi tuần tự máy móc chỉ để "đủ quy trình":

- **Mức L0: Nền Tảng (Core Intent & Transformation Promise):** Độc giả ở đâu? Về đâu? Luận đề cốt lõi không nhân nhượng.
- **Mức L1: Cấu Trúc Khối (Macro Parts / 2-4 Khối):** Bẻ gãy ảo tưởng ➔ Cơ chế ngầm ➔ Tái thiết nhận thức.
- **Mức L2: Chuỗi Domino (Leads-to Interlock):** Logic chuyển tiếp: Tại sao Phần A ép người đọc sang B?
- **Mức L3: Luận Điểm & Beat (Governing Lines & Beats):** Mỗi chương: 1 câu hỏi nhức nhối, 1 luận điểm, 1 cú hích.

### Quy Tắc Cấm Đốt Cháy Giai Đoạn (No Premature Full TOC)
Tuyệt đối cấm Agent tự ý sinh toàn bộ mục lục chi tiết (Full TOC) khi các quyết định ở mức phân giải hiện tại (Luận đề cốt lõi, Lời hứa chuyển hóa hoặc Cấu trúc khối) chưa đạt độ chắc chắn hoặc chưa được user đồng thuận.

---

## 2. Cấu Trúc Khung Xương 3 Tầng (3-Tier Spine Engineering)

Spine không phải là bảng mục lục tĩnh, mà là bản đồ hành trình nhận thức của độc giả gồm 3 tầng:

1. **Tier 1 — Phần (Part / Act)**: Khối chuyển hóa nhận thức lớn (ví dụ: Phần 1: Bẻ gãy ảo tưởng $\rightarrow$ Phần 2: Cơ chế ngầm $\rightarrow$ Phần 3: Tái thiết hành vi).
2. **Tier 2 — Chương (Chapter)**: Đơn vị lập luận độc lập giải quyết một nút thắt cụ thể.
3. **Tier 3 — Luận điểm chủ đạo (Governing Argument Line)**: Câu tuyên bố duy nhất (1 câu) thể hiện bản chất lập luận của chương, không dùng tiêu đề mơ hồ.

---

## 2. Quy Tắc Sợi Chỉ Nhân Quả Leads-To (Leads-to Causality Threading)

Mỗi chương trong `book_spine.md` bắt buộc phải có trường `Leads-to`:
- **Định nghĩa**: Kết thúc của Chương N phải giải quyết xong vấn đề của nó, nhưng đồng thời làm lộ ra một khoảng trống nhận thức hoặc nghịch lý mới mà CHỈ CÓ Chương N+1 mới giải quyết được.
- **Công thức kiểm tra**:
  - *"Độc giả vừa đồng ý với Chương N rằng [X]. Nhưng nếu [X] đúng, thì điều gì sẽ xảy ra với [Y]? Câu hỏi nhức nhối này buộc họ phải lật sang Chương N+1."*
  - Nếu bỏ Chương N+1 ra mà cuốn sách vẫn trơn tru $\rightarrow$ Chương N+1 là thừa hoặc Chương N chưa có `Leads-to` chuẩn.

---

## 3. Bảng Cam Kết Kỳ Vọng Độc Giả (`promises.md`)

- Mỗi lời hứa trong `manifesto.md` phải được ánh xạ trực tiếp sang các chương:
  - Lời hứa 1 $\rightarrow$ Được gieo hạt ở Chương 1, giải thích ở Chương 3, trả nợ trọn vẹn (Payoff) ở Chương 7.
- Ngăn chặn triệt để tình trạng "Đầu voi đuôi chuột": hứa hẹn ở bìa nhưng không có chương nào thực sự hướng dẫn giải quyết.

---

## 4. Giao Thức Tính Toán Bán Kính Ảnh Hưởng (Scoped Blast Radius Protocol)

Khi cờ `SPINE-FLAG` được bật trong quá trình chấp bút (ví dụ: phát hiện một chương cần tách đôi hoặc đổi vị trí):
1. **Định vị Blast Radius**:
   - Xác định chính xác các chương bị ảnh hưởng trực tiếp (thường là chương trước nó và chương sau nó qua liên kết `Leads-to`).
2. **Kích hoạt Scoped Snapshot**:
   - Sao lưu các file liên quan vào `snapshots/YYYY-MM-DD-spine-update/`. Cấm sao lưu tràn lan cả dự án.
3. **Đề xuất can thiệp tối thiểu (Minimal-Change Principle)**:
   - Điều chỉnh lại trường `Leads-to` giáp ranh để bảo toàn tính toàn vẹn của mạch sách.

---

## 5. Ví Dụ Cụ Thể (Few-Shot Example)

### Input:
Ý tưởng sách về quản trị năng lượng thay vì quản trị thời gian. Gồm 3 chương đầu.

### Output (`book_spine.md` format):
```markdown
# Book Spine: Quản Trị Năng Lượng

## Part I: Ảo Tưởng Về 24 Giờ

### Chapter 01: Chiếc Bẫy Lịch Kín Mít
- **Governing Line**: Quản trị thời gian chỉ tối ưu hóa sự bận rộn chứ không tạo ra hiệu suất đột phá.
- **Promise Payoff**: Giải phóng độc giả khỏi cảm giác tội lỗi khi không hoàn thành to-do list.
- **Leads-to**: Khi độc giả nhận ra thời gian là hữu hạn và cố định, họ buộc phải tìm kiếm một biến số có thể co giãn và tái tạo được: đó chính là Năng Lượng (dẫn thẳng vào Chapter 02).

### Chapter 02: 4 Bình Nhiên Liệu Con Người
- **Governing Line**: Năng lượng con người không phải một khối đồng nhất, nó vận hành qua 4 bình chứa độc lập: Thể chất, Cảm xúc, Trí tuệ và Tinh thần.
- **Promise Payoff**: Giúp độc giả tự chẩn đoán bình nhiên liệu đang bị rò rỉ.
- **Leads-to**: Khi đã hiểu 4 bình nhiên liệu, câu hỏi bức thiết xuất hiện: Làm thế nào để sạc lại khi công việc liên tục vắt kiệt chúng ta mỗi ngày? (dẫn vào Chapter 03 về Nghi thức Nhịp sinh học).
```

---

## 6. Tiêu Chuẩn Nghiệm Thu

- [ ] 100% các chương đều có trường `Governing Line` và `Leads-to`.
- [ ] Mạch nhân quả không bị đứt gãy giữa các chương giáp ranh.
- [ ] Ánh xạ đủ cam kết trong `promises.md`.

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `genesis-interview` | Đối chiếu lại định vị độc giả và lời hứa bìa sách (`manifesto.md`) khi thiết lập bảng cam kết `promises.md`. |
| `chapter-blueprinting` | Bàn giao dòng lập luận `Governing Line` và logic `Leads-to` để bẻ gãy thành các beats trong `card.md`. |
