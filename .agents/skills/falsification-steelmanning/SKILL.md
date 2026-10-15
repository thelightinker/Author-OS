---
name: falsification-steelmanning
description: "Phản biện đối nghịch & Thử sức chịu tải luận điểm (SHARED SKILL): Áp dụng ma trận 4 bước Steelman để công kích luận điểm cốt lõi, xây dựng phản đề mạnh nhất của đối thủ, truy quét lỗi ngụy biện logic (thiên kiến kẻ sống sót, đánh tráo tương quan thành nhân quả) và xác lập điều kiện biên chính xác (\"Đúng khi nào, Sai khi nào?\"). Dùng chung cho Architect (Genesis Stress-Test, Layer 2 Auditor) và Crafter (Pass 1 Self-Check)."
when_to_use: "Khi kiểm định sức chịu tải luận đề ở pha Genesis, khi Chapter Crafter tự kiểm định ở Pass 1, hoặc khi Book Architect tiến hành thẩm định Layer 2 Informed Review."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Falsification Steelmanning: Phản Biện Đối Nghịch & Thử Lửa Luận Đề

> "Một ý tưởng chỉ thực sự mạnh mẽ khi nó sống sót qua đòn tấn công của đối thủ thông minh nhất, không phải khi nó đắc thắng trước một bù nhìn rơm ngớ ngẩn do ta tự dựng lên."

---

## 1. Bản Chất Kỹ Năng Dùng Chung (Shared Skill Isolation Invariant)

- Kỹ năng này được **dùng chung** bởi 2 vai trò với 2 mục đích độc lập:
  - **`book-architect` (Genesis Thesis Stress-Test & Layer 2 Auditor)**: Đóng vai trò giám khảo đối nghịch, công kích toàn diện để bảo đảm luận đề và cấu trúc không có lỗ hổng chết người trước khi duyệt gate.
  - **`chapter-crafter` (Pass 1 Self-Steelmanning)**: Đóng vai trò tự vấn nội tâm khi vừa viết xong một section, kiểm tra xem luận điểm của mình có quá cực đoan hay dễ bị bắt bẻ không.
- **Nguyên tắc bất biến**: `Shared Skill != Shared Context`. Khi một Agent nạp kỹ năng này, họ vận hành độc lập hoàn toàn với ngữ cảnh của Agent kia.

---

## 2. Ma Trận Tấn Công Steelman 4 Bước (4-Step Steelman Attack Matrix)

Khi đối diện với bất kỳ khẳng định hoặc luận đề nào, thực thi tuần tự 4 bước:

1. **Bước 1 — Bóc tách Khẳng định Cốt lõi (Extract Core Claim)**:
   - Tóm gọn khẳng định thành 1 câu rõ ràng. Tước bỏ mọi từ ngữ khoa trương cảm xúc.

2. **Bước 2 — Xây dựng Phản đề Mạnh nhất (Steelman Counter-Thesis)**:
   - Đặt câu hỏi: *"Nếu một giáo sư đầu ngành hoặc một chuyên gia phản đối kịch liệt quan điểm này, họ sẽ đưa ra lập luận chặt chẽ nhất nào?"*.
   - Tuyệt đối không dùng "bù nhìn rơm" (strawman) — phải làm cho luận điểm đối nghịch trở nên thuyết phục nhất có thể.

3. **Bước 3 — Săn tìm Lỗ hổng Tư duy (Hunt Fallacy Modes)**:
   - *Survivor Bias (Thiên kiến kẻ sống sót)*: Tác giả có đang chỉ nhìn vào những người thành công mà quên mất 99% người làm đúng như vậy nhưng thất bại không?
   - *Correlation vs. Causation (Đánh tráo Tương quan)*: Hai hiện tượng xảy ra cùng lúc có thực sự là nguyên nhân của nhau?
   - *Sample Size & Context Blindness*: Nghiên cứu được trích dẫn có áp dụng được cho bối cảnh độc giả mục tiêu không?

4. **Bước 4 — Thiết lập Điều kiện Biên (Formulate Boundary Conditions)**:
   - Trả lời rành mạch 2 câu hỏi cứu mạng của một cuốn sách phi hư cấu:
     - **"ĐÚNG KHI NÀO?"** (Phạm vi áp dụng thành công rực rỡ).
     - **"SAI KHI NÀO?"** (Khi nào thì phương pháp này hoàn toàn vô tác dụng hoặc gây hại?).
   - Đưa điều kiện biên trực tiếp vào văn bản để biến một phát ngôn võ đoán thành một chân lý sâu sắc, có trách nhiệm.

---

## 3. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (Luận đề sơ bộ trong Manifesto):
```
"Mọi người nên từ bỏ công việc văn phòng 9-to-5 để khởi nghiệp làm chuyên gia độc lập (Solopreneur). Làm công ăn lương là con đường nghèo khó và bị tước đoạt tự do."
```

### Xử lý Steelman Attack:
- **Steelman Phản đề**: 95% solopreneur kiếm được ít tiền hơn lương văn phòng, chịu thuế tự doanh cao hơn, không có bảo hiểm, không có ngày nghỉ phép có lương và cô đơn cùng cực. Công việc văn phòng mang lại bệ phóng vốn, mạng lưới quan hệ và sự ổn định để quản trị rủi ro gia đình.
- **Fallacy Check**: Thiên kiến kẻ sống sót nặng nề từ các influencer mạng xã hội.

### Output (Điều kiện biên tích hợp vào `manifesto.md` & đoạn văn):
```markdown
### Điều Kiện Biên (Boundary Conditions):
- **Đúng khi nào**: Khi một cá nhân đã tích lũy tối thiểu 5 năm kinh nghiệm chuyên môn sâu trong một thị trường ngách, đã có sẵn mạng lưới 10 khách hàng tiềm năng đầu tiên, và có quỹ dự phòng sống tối thiểu 12 tháng không doanh thu.
- **Sai khi nào**: Khi bạn chỉ đang kiệt sức với người sếp hiện tại, chưa có kỹ năng bán hàng, hoặc đang gánh nợ tiêu dùng nặng. Trong trường hợp này, nhảy ra làm solopreneur là một hành động tự sát tài chính.
```

---

## 4. Tiêu Chuẩn Nghiệm Thu

- [ ] Phản đề được xây dựng đủ mạnh, không phải bù nhìn rơm.
- [ ] Chỉ ra tối thiểu 1 nguy cơ ngụy biện logic tiềm tàng.
- [ ] Luôn kết thúc bằng việc xác lập rõ ràng hai câu hỏi "Đúng khi nào? Sai khi nào?".

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `genesis-interview` | Công kích luận đề sơ khởi từ cuộc phỏng vấn để hình thành điều kiện biên trước khi ký duyệt Gate 1. |
| `editorial-revision` | Cung cấp phương pháp phản biện đối nghịch ở Pass 1 khi tự rà soát độ vững của lập luận trong từng đoạn văn. |
