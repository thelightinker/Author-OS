---
name: author-excavation
description: "Kỹ năng chuyên sâu khai thác insight, bóc tách ký ức theo thang 7 bậc Insight Ladder, phỏng vấn có phương pháp luận và bắt nhanh câu chuyện đời thực (Fast Story Capture) từ tác giả."
version: 2.0.0
role: master-orchestrator, chapter-crafter
triggers: ["excavate", "interview", "insight_brief", "story_capture", "phỏng vấn tác giả"]
references: ["references/insight_ladder.md"]
---

# Skill: Author Excavation (Khai Thác Insight & Ký Ức Tác Giả)

> "Zero Fabrication Without Grounding. Khoảng trống nhận thức thuộc về tác giả thì BẮT BUỘC phải phỏng vấn để khai thác, tuyệt đối không tự điền."

---

## 3 Chế Độ Vận Hành (Operating Modes)

### 1. Mode `genesis` (Khởi nguyên toàn sách)
- Khai thác manifesto, tư tưởng chủ đạo, đối tượng độc giả và ranh giới không nhượng bộ của cuốn sách.
- Sinh ra `foundation/manifesto.md` và `foundation/promises.md`.

### 2. Mode `chapter` (Khai thác theo chương trước khi lập Card & Node 3 Excavation)
- Sử dụng phương pháp luận **Insight Ladder** (xem [insight_ladder.md](references/insight_ladder.md)).
- **Quy trình Phỏng vấn Cửa B (Ghi chú rời):**
  * Cho phép phỏng vấn nhiều lượt liên tiếp (mỗi lượt chỉ hỏi đúng 1 câu có giá trị thông tin cao nhất).
  * Dừng phỏng vấn ngay khi đã giải quyết được các khoảng trống nhận thức cốt lõi.
- **Tiêu chuẩn đủ chất liệu linh hoạt theo loại section (Content-Specific Material Sufficiency):**
  * *Section Narrative*: Bắt buộc có sự thật từ tác giả, chi tiết hiện trường và 5-second moment.
  * *Section Analytical / Conceptual*: Đòi hỏi cơ chế nhân quả và tính chặt chẽ của lập luận. AI được tự suy luận logic hợp lý nếu có cơ sở vững, không ép tìm câu chuyện cá nhân.
  * *Section Research*: Đòi hỏi nguồn dẫn kiểm chứng trong `sources/notes/`.
  * Các vùng `UNKNOWN` thứ yếu được phép giữ nguyên và nêu rõ ranh giới nhận thức thay vì coi là lỗi chặn.
- **Exception-Only Escalation:** Sau khi đào sâu chất liệu, Agent tự động chuyển sang Node 4 (`SECTION_DRAFTING`); chỉ quay lại Node 2 (`GATE_3_BLUEPRINT`) nếu phát hiện dữ kiện làm đảo lộn cấu trúc Card đã duyệt.
- Co giãn theo kết quả Gap Scan:
  * `explore`: Tác giả chưa định hình rõ -> 7–10 câu hỏi theo thang.
  * `standard`: Đã có hướng tổng quát -> 3–7 câu hỏi chọn lọc.
  * `fast`: Đã có tài liệu đầy đủ -> 0–2 câu hỏi xác nhận.
- **Phỏng Vấn Thử Tải Luận Điểm Đối Nghịch (Adversarial Socratic Probing):**
  * Đối với các chương và section phân tích (`Analytical`) hoặc tái định nghĩa (`Conceptual`), Agent kích hoạt bộ câu hỏi phản biện đối nghịch để thử sức chịu tải của luận điểm:
    1. **Core Claim (Luận điểm):** *"Nhận định sắc bén nhất mà anh muốn bảo vệ trong chương này là gì, điều mà hầu hết mọi người ngoài kia đang hiểu sai?"*
    2. **Grounding Basis (Cơ sở):** *"Bằng chứng hay trải nghiệm cụ thể nào khiến anh tin chắc vào điều này (đây là sự thật anh đã kiểm chứng qua đời thực, hay là một lăng kính giải thích anh đang cân nhắc)?"*
    3. **Falsification (Phản đề & Thử tải):** *"Điều gì hoặc tình huống nào có thể chứng minh rằng nhận định này hoàn toàn sai?"*
    4. **Boundary Condition (Điều kiện biên):** *"Nhận định này đúng trong trường hợp nào, và đâu là trường hợp ngoại lệ mà nếu áp dụng nó sẽ trở nên độc hại?"*
    5. **Stakes (Cái giá):** *"Nếu độc giả không thay đổi nhận thức này mà tiếp tục duy trì niềm tin cũ, hậu quả thực tế đắt nhất mà họ phải trả là gì?"*
  * **Nguyên tắc phỏng vấn thích ứng:** Không hỏi dồn dập cả 5 câu như một biểu mẫu. Chọn đúng 1 câu hỏi có giá trị entropy thông tin cao nhất dựa trên câu trả lời trước đó của tác giả.
- **Tiêu chuẩn kết thúc (DoD của phiên phỏng vấn):**
  1. Core Insight được phát biểu bằng chính từ ngữ nguyên văn của tác giả.
  2. Có ít nhất một trải nghiệm cá nhân của tác giả (với narrative) hoặc cơ chế nhân quả được xác nhận (với analytical).
  3. Xác định rõ ngộ nhận phổ biến của người đọc và cú huých nhận thức (Shift).
  4. Xác định rõ cái giá phải trả (Stakes) và điều kiện biên (Boundary).
- **Thành phẩm:** Lưu thành `chapters/ch_XX/insight_brief.md` hoặc cập nhật vào `chapters/ch_XX/intent_ledger.md`.

### 3. Mode `capture` (Lưu nhanh câu chuyện giữa hội thoại)
- Khi tác giả tình cờ chia sẻ một câu chuyện đời thực trong lúc trò chuyện, AI **không ngắt mạch tư duy** mà đề nghị lưu nhanh:
  *"Em lưu câu chuyện này vào kho là S-XXX nhé sếp?"*
- **Schema 3 trường tối thiểu:**
  * `title`: Tên biến cố / trải nghiệm.
  * `verbatim`: Trích nguyên văn lời kể của tác giả.
  * `themes`: Chủ đề liên quan (ví dụ: `failure`, `finance`, `productivity`).
  * Trạng thái mặc định: `status: raw`.
- Khi câu chuyện được đưa vào sử dụng trong chương cụ thể, mới tiến hành phỏng vấn sâu để làm giàu thành `shaped` hoặc `verified`.

---

## Hợp Đồng Định Dạng `insight_brief.md`

```markdown
# Insight Brief — Chapter [XX]

## 1. Core Insight (Tư tưởng cốt lõi)
- **Author Verbatim:** "[Trích nguyên văn lời tác giả phát biểu]"
- **Synthesized Stance:** [Tóm tắt 1 câu đanh thép của AI sau khi tác giả duyệt]

## 2. Reader Misbelief -> Shift (Chuyển hóa nhận thức)
- **From:** [Ngộ nhận hiện tại độc giả đang mắc phải]
- **To:** [Nhận thức mới giải phóng người đọc]

## 3. Stakes (Sức nặng hiện sinh)
- [Cái giá đắt nhất nếu tiếp tục duy trì niềm tin cũ]

## 4. Author Materials & Story Binding
- **Canonical Stories:** [Ví dụ: S-001 (shaped)]
- **New Captured Stories:** [Ví dụ: S-004 (raw)]
- **Direct Quotes to Preserve:** [Các cụm từ chữ ký của tác giả cần giữ nguyên]

## 5. Identified Gaps (Khoảng trống cần xử lý)
- [Liệt kê các điểm cần AI tìm thêm dẫn chứng ngoài hoặc logic bắc cầu]
```
