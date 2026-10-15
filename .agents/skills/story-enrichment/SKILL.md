---
name: story-enrichment
description: "Bóc tách ký ức & Làm giàu kho giai thoại thực tế (Story Bank): Áp dụng 4 nhóm câu hỏi Socratic (Giác quan hiện trường, Chuyển biến tâm lý, Hành động cụ thể, Vùng chưa chắc chắn) để chuyển hóa một câu chuyện kể thô của tác giả thành một thẻ tư liệu sống động S-XXX trong story_bank.md, thiết lập Reframe Note và trường chống trùng lặp Used In."
when_to_use: "Khi phỏng vấn tác giả để khai thác câu chuyện đời thực, làm giàu kho dữ liệu story_bank.md trước khi chấp bút một chương."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Story Enrichment: Bóc Tách Ký Ức & Làm Giàu Kho Giai Thoại Thực Tế

> "Độc giả không nhớ các biểu đồ thống kê khô khan; họ nhớ ánh mắt hoảng loạn của người sáng lập khi nhìn vào màn hình báo cáo ngân hàng lúc 3 giờ sáng. Chi tiết hiện trường là thứ biến lập luận thành trải nghiệm sống."

## 0. Schema Authority, Governance & Context-Aware Grounding

- **Ràng buộc Liêm chính Tự sự (Deterministic Binding - P1)**:
  - Agent thực thi skill này **BẮT BUỘC (MUST)** nạp và tuân thủ [`.agents/rules/story-integrity.md`](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/story-integrity.md) trong toàn bộ phiên phỏng vấn và ghi nhận dữ liệu vào `story_bank.md`. Tuyệt đối cấm suy diễn hoặc điền khuyết chi tiết sự kiện chưa được tác giả xác nhận.
- **Schema Authority**:
  - `templates/story-bank-template.md`: Chuẩn cấu trúc bắt buộc cho `story_bank.md` và các thẻ `S-XXX` (Title, Core Insight, Sensory Anchor, 5-Second Moment, Reframe Note, Used In list).
- **Quy tắc Grounding**:
  - Khi khởi tạo hoặc bổ sung thẻ câu chuyện vào `story_bank.md`, bắt buộc ground vào schema của `story-bank-template.md`.
  - **Context-Aware Exemption**: Nếu template hoặc story bank đã có mặt trong ngữ cảnh phiên làm việc hoặc đã được nạp qua workflow, **KHÔNG đọc lại** để tránh lãng phí token (Anti-Spam Invariant).

---

## 1. Bộ Khung Phỏng Vấn Socratic 4 Nhóm Bóc Tách Ký Ức

Khi tác giả kể một sự kiện (ví dụ: "Hồi đó tôi khởi nghiệp thất bại, mất sạch tiền"), hãy dùng 4 nhóm câu hỏi sau để khơi thông ký ức:

1. **Nhóm 1 — Giác Quan Hiện Trường (Sensory Details)**:
   - "Thời điểm đó là mấy giờ? Căn phòng lúc đó trông như thế nào? Ánh sáng hắt ra từ đâu?"
   - "Âm thanh xung quanh lúc đó là tiếng máy lạnh rền rĩ, tiếng chuông điện thoại reo dồn dập hay sự im lặng ngột ngạt?"
   - "Trên bàn lúc đó có đồ vật gì cụ thể không (ly cà phê nguội ngắt, tệp hợp đồng nhàu nát)?"

2. **Nhóm 2 — Chuyển Biến Tâm Lý (Psychological Shift)**:
   - "Khoảnh khắc chính xác nào khiến bạn nhận ra tình thế không thể cứu vãn được nữa?"
   - "Cảm giác vật lý trong cơ thể lúc đó là gì (ngực thắt lại, lạnh sống lưng, hay tai ù đi)?"
   - "Lời độc thoại nội tâm đáng sợ nhất vang lên trong đầu bạn lúc đó là gì?"

3. **Nhóm 3 — Hành Động Cụ Thể (Micro-Action)**:
   - "Ngay sau giây phút đó, bạn đã làm gì đầu tiên? (Nhấc máy gọi cho ai, bước ra ban công hút thuốc, hay gập màn hình laptop lại)?"
   - "Câu nói thật nguyên văn mà người đối diện đã nói với bạn là gì?"

4. **Nhóm 4 — Vùng Chưa Chắc Chắn (Fog & Vulnerability)**:
   - "Chi tiết nào bạn cảm thấy hơi xấu hổ hoặc ngần ngại không muốn thừa nhận trên trang sách?"
   - "Điều gì bạn nghĩ mình đã làm sai hoàn toàn vào thời điểm đó mà nhiều năm sau mới nhận ra?"

---

## 2. Cấu Trúc Thẻ Giai Thoại Chuẩn Trong `story_bank.md`

Mỗi câu chuyện sau khi bóc tách được ghi vào `story_bank.md` theo chuẩn **5-Part Epistemic Breakdown**:

```markdown
## S-001: [Tiêu đề giai thoại ngắn gọn]
- **Provenance Tier:** Tier A (Ký ức tác giả) | Tier B (Chuyện người khác) | Tier C (Minh họa) | Tier D (Tái cấu trúc)
- **Interview Source:** [Ghi chú ngày/phiên phỏng vấn, trích đoạn trao đổi hoặc nguồn tham chiếu]
- **Confirmed Facts:** [Các sự kiện khách quan đã diễn ra và được tác giả xác nhận 100%]
- **Interview Content:** [Nội dung thực tế do tác giả chia sẻ trong phiên phỏng vấn]
- **Author Interpretation:** [Góc nhìn, cảm nhận, bài học do chính tác giả đúc rút]
- **Agent Inferences:** [Đề xuất diễn giải logic của AI (nếu có, phải gán nhãn rõ để tác giả duyệt)]
- **Unknown Details:** [Những chi tiết chưa rõ: mốc giờ, thời tiết, hội thoại nguyên văn... Giữ nguyên UNKNOWN, cấm bịa]
- **Emotional Hook:** [Móc câu cảm xúc thật: Tuyệt vọng / Bừng tỉnh / Bất lực / Hoang mang]
- **Transformation Scene:** [Khoảnh khắc hoặc hành động thực tế tạo chuyển biến nhận thức]
- **Reframe Note:** [Insight mới: câu chuyện này phục vụ luận điểm gì của cuốn sách?]
- **Forbidden Conflations:** [Cảnh báo: Không được để người đọc hiểu nhầm sang...]
- **Timeline Sanity:** PASS (Khớp logic với năm sinh và tiểu sử trong identity.md)
- **Used In:** []
```

---

## 3. Ví Dụ Cụ Thể (Few-Shot Example — Epistemic Truth Preservation)

### Trường Hợp 1: Tác giả kể tóm tắt ➔ Phỏng vấn đào sâu, giữ trọn sự thật

#### Input (Lời kể ban đầu của tác giả trong phiên chat):
```
"Năm 2021 công ty tôi suýt vỡ nợ vì đối tác lớn nhất quỵt 2 tỷ tiền dự án. Tôi phải đi vay người quen để trả lương nhân viên. Lúc đó tôi nhận ra quản trị rủi ro dòng tiền quan trọng hơn sự tin tưởng mù quáng."
```

#### Phản xạ của Agent (Không tự bịa chi tiết thời tiết, địa danh hay hành động giả):
Agent nhận thấy thiếu chi tiết chuyển biến cảm xúc thực tế ➔ **Kích hoạt PROBE 1 câu Socratic**:
> *"Khi biết tin đối tác quỵt nợ và phải đi vay tiền trả lương cho anh em, cảm xúc nặng nề nhất lúc đó trong anh là gì, và khoảnh khắc anh quyết định không bao giờ làm việc không có cọc bảo lãnh nữa là khi nào?"*

#### Tác giả trả lời:
> *"Cảm xúc tệ nhất là cảm giác có lỗi với 15 anh em tin tưởng mình. Tôi quyết định ngay tối hôm đó khi ngồi chuyển khoản từng món lương từ tiền đi vay: từ nay không có thanh toán theo tiến độ thì không bắt đầu."*

#### Output (Thẻ chuẩn ghi vào `story_bank.md` — 0% bịa đặt, minh bạch nhận thức):
```markdown
## S-001: Đêm Chuyển Khoản Trả Lương Bằng Tiền Vay Và Bài Học Hợp Đồng
- **Provenance Tier:** Tier A (Ký ức tác giả)
- **Interview Source:** Phiên trao đổi Genesis Inception ngày 2026-10-02
- **Confirmed Facts:** Năm 2021, đối tác lớn quỵt nợ 2 tỷ đồng dự án. Tác giả phải vay tiền người quen để thanh toán đủ lương cho 15 nhân viên.
- **Interview Content:** Tác giả chia sẻ cảm xúc tồi tệ nhất là cảm giác có lỗi với 15 người tin tưởng mình, và quyết định siết chặt hợp đồng được đưa ra ngay trong đêm chuyển khoản lương từ tiền đi vay.
- **Author Interpretation:** Quản trị rủi ro dòng tiền quan trọng hơn niềm tin cảm tính; sự tử tế mù quáng không có điều khoản bảo lãnh là vô trách nhiệm với đội ngũ.
- **Agent Inferences:** Có thể neo câu chuyện này vào chương về ranh giới bảo vệ nguồn lực và phản đề "Nhiệt tình thiếu cơ chế".
- **Unknown Details:** Địa điểm cụ thể của văn phòng đối tác, hội thoại chi tiết khi đàm phán nợ (Tác giả không đề cập ➔ Giữ nguyên UNKNOWN, cấm tự bịa thời tiết hay các hành động kịch hóa giả tạo).
- **Emotional Hook:** Nỗi day dứt và áp lực nghẹt thở trước sự tin cậy của 15 nhân viên.
- **Transformation Scene:** Ngồi trong đêm chuyển khoản từng món tiền lương được vay mượn, ra quyết định dứt khoát: không có bảo lãnh thanh toán thì không khởi động bất kỳ dự án nào.
- **Reframe Note:** Dùng để chứng minh: Trưởng thành trong quản trị không phải là trở nên sắt đá, mà là xây dựng cơ chế để bảo vệ những người cùng thuyền.
- **Forbidden Conflations:** Không biến thành câu chuyện kể khổ hay công kích cá nhân đối tác; tập trung vào sự chuyển hóa nhận thức về trách nhiệm và hợp đồng.
- **Timeline Sanity:** PASS (Phù hợp với mốc thời gian hoạt động thực tế của tác giả).
- **Used In:** []
```

---

## 4. Tiêu Chuẩn Nghiệm Thu

- [ ] Phân định đầy đủ 5 trường Epistemic Breakdown (`Confirmed Facts`, `Interview Content`, `Author Interpretation`, `Agent Inferences`, `Unknown Details`).
- [ ] **0% Bịa đặt**: Không tự ý bịa thêm thời gian, địa điểm, thời tiết, hội thoại, hoặc hành động giả tạo chưa được tác giả xác nhận.
- [ ] Chi tiết không chắc chắn được giữ nguyên trong `Unknown Details` thay vì điền khuyết hư cấu.
- [ ] Vượt qua kiểm tra Timeline Sanity (khớp logic tiểu sử trong `identity.md`).
- [ ] Ghi rõ `Reframe Note` gắn liền với mục tiêu cuốn sách.
- [ ] Trường `Used In` được khởi tạo rỗng `[]` để bảo đảm chống lặp.

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `chapter-blueprinting` | Nhận diện nhu cầu câu chuyện và vị trí beat cần minh họa từ `card.md`. |
| `chapter-drafting` | Bàn giao chi tiết hiện trường và khoảnh khắc chuyển biến 5 giây để chấp bút cảnh sống động. |
