---
name: manuscript-formatting
description: "Chuẩn hóa và tinh chỉnh hình thức bản thảo sách xuất bản (Manuscript Presentation & Formatting Polish): Loại bỏ ma sát trình bày, nhịp điệu dấu câu gượng gạo (lạm dụng em dash, colon kịch tính, slash), nhịp thở đoạn văn giật cục (staccato line-breaks), lạm dụng bôi đậm (bold/italic) và chuyển hóa danh sách bullet thành văn xuôi liên tục (CONV-001). BẮT BUỘC kích hoạt khi hoàn thiện section, rà soát bản thảo trước khi nộp, xử lý lỗi formatting do Auditor gắn cờ, hoặc khi cần phẫu thuật cú pháp (syntactic re-anchoring) mà tuyệt đối không thay đổi ý nghĩa, không thêm luận điểm, không đổi giọng văn và không bịa đặt tình tiết."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.2.0
---

# Manuscript Formatting: Nghệ Thuật Trình Bày Bản Thảo Sách Chuẩn Xuất Bản

> "Make the manuscript read and look like intentional human prose without flattening authorial voice."  
> *(Biến bản thảo thành văn xuôi tự nhiên, giàu chủ đích của con người mà không làm phẳng hay triệt tiêu giọng văn tác giả).*

---

## 💎 HỆ THỐNG AIRBAG ĐIỀU PHỐI FORMATTING (BẤT BIẾN)

1. **Airbag 1 (Anti-Metric Optimization)**:
   > *"The system must never optimize for formatting metrics. It only uses human-like editorial judgment in context."*  
   > *(Hệ thống tuyệt đối không bao giờ tối ưu hóa văn bản để đạt các chỉ số máy móc vô hồn. Mọi quyết định can thiệp đều dựa trên ngữ cảnh đọc thực tế).*

2. **Airbag 2 (Observation vs. Material Repair Boundary)**:
   > *"OBSERVATION ≠ VIOLATION | VIOLATION ≠ REQUIRED REPAIR | REPAIR ≠ DELETE THE SURFACE MARKER.  
   > An unusual pattern only identifies a place worth inspecting. Only material reader friction justifies editorial intervention."*  
   > *(Một dấu hiệu lạ chỉ là vị trí đáng soi lại. Có lạ chưa chắc đã là lỗi, và sửa chữa tuyệt đối không phải là xóa mù quáng dấu câu bề mặt. Chỉ can thiệp khi có ma sát thực sự làm cản trở trải nghiệm đọc).*

3. **Airbag 3 (Strict Formatting Scope & Non-Invention Gate - P0 Boundary)**:
   > *"Formatting handles visual presentation and rhythm, NEVER content, meaning, or narrative facts."*  
   > - **Phạm vi ĐƯỢC PHÉP**: Gộp/tách đoạn văn, điều chỉnh ngắt dòng (line breaks), tinh chỉnh dấu câu, chuẩn hóa mật độ heading, khoảng trắng, dọn rác markdown và chuyển hóa liên từ nối ngữ pháp.  
   > - **Ranh giới CẤM TUYỆT ĐỐI (Hard Negative Boundaries)**:  
   >   - **CẤM** thay đổi ý nghĩa (meaning) hoặc lập luận cốt lõi của tác giả.  
   >   - **CẤM** thêm luận điểm (claims), dữ kiện (facts), số liệu hoặc phán đoán mới.  
   >   - **CẤM** thay đổi giọng văn (authorial voice) hoặc cá tính riêng của tác giả trong `voice.md`.  
   >   - **CẤM** bịa thêm tình tiết tự sự, lời thoại, cử chỉ, bối cảnh hay giác quan để làm mượt câu văn.  
   >   - **CẤM** viết lại câu thành các mẫu văn triết lý AI sáo rỗng (*"Bản chất của X chưa bao giờ nằm ở..."*).

---

## 1. Triết Lý 2 Tầng: Chuẩn Hóa Cơ Học & Lăng Kính Biên Tập

Hệ thống phân định rạch ròi 2 tầng trách nhiệm độc lập:
1. **Mechanical Normalization & Guard (`scripts/repair_invariants.py`)**: Máy xử lý những gì máy chắc chắn biết là đúng/sai (khoảng trắng trước dấu câu, dọn dấu câu thừa ở tiêu đề, chuẩn hóa en-dash cho dải số năm tháng, bảo vệ code block/code span, quét gap token). Máy là chiếc đai an toàn cơ học, không bao giờ tự phong làm nhà văn hay phán xét nhịp điệu văn chương.
2. **Editorial Lens (`manuscript-formatting`)**: Crafter và Auditor sử dụng kỹ năng này như một cẩm nang tri thức chuyên sâu khi đọc bản thảo trong toàn bộ ngữ cảnh. Nhận diện ma sát thực tế (văn giật cục, dấu câu gượng gạo, nhịp thở đứt đoạn, bôi đậm từ khóa tùy tiện) và thực thi phẫu thuật cú pháp (Syntactic Re-anchoring) bảo toàn tuyệt đối `WHAT TO KEEP` và `voice.md`. Không cần telemetry trung gian hay taxonomy phức tạp.

---

## 2. 6 Cụm Chuẩn Mực P0 (Lean 80/20 Framework)

| Mã Chuẩn Mực | Tên Chuẩn Mực | Tiêu Điểm Biên Tập |
|:---|:---|:---|
| **`FORMAT-001`** | **Emphasis Control** | Khử lạm dụng Bold/Italic & Bold Labels trong thân văn xuôi |
| **`FORMAT-002`** | **Punctuation Rhythm** | Khử lạm dụng Em Dash, Colon kịch tính, Slash viết tắt |
| **`FORMAT-003`** | **Heading Density** | Mật độ tiêu đề hài hòa (≥ 250 từ), dọn sạch dấu câu thừa |
| **`FORMAT-004`** | **Paragraph Rhythm** | Nhịp thở đoạn văn tự nhiên (3–6 câu), triệt tiêu staccato chat |
| **`FORMAT-005`** | **Markdown Artifacts** | Dọn rác kỹ thuật: backticks chữ thường, HTML sót, Mermaid thô |
| **`FORMAT-006`** | **Continuous Prose** | Bảo vệ chuẩn CONV-001, ngăn chặn chatification và lạm dụng bullet |

### `FORMAT-001`: Emphasis Control (Kiểm Soát Bold & Italic)
- **Nguyên tắc**: Mức độ in đậm/in nghiêng do `voice.md` định đoạt, framework không áp đặt cấm đoán cực đoan nhưng nghiêm cấm thói quen bôi đậm máy móc của AI.
- **Dấu hiệu ma sát (AI Tells)**:
  - Bôi đậm từ khóa tùy tiện (`**từ khóa**`) rải rác giữa thân văn xuôi như đang tóm tắt slide thuyết trình hoặc phản hồi chatbot.
  - Bôi đậm nhãn đầu đoạn (Bold Labels kiểu `**Nguyên nhân:** ...`, `**Bài học:** ...`) biến văn tự sự thành tài liệu hành chính.
- **Hành động biên tập**:
  - Gỡ bỏ các thẻ `**` trong thân văn xuôi, để sức nặng nhận thức dồn vào chính cấu trúc câu và từ ngữ tự nhiên.
  - In đậm chỉ giữ lại ở Tiêu đề hoặc bài tập/checklist có chủ đích.
  - In nghiêng `*italic*`: Dành riêng cho tên tác phẩm, từ mượn tiếng nước ngoài chưa Việt hóa lần đầu xuất hiện, hoặc lời độc thoại nội tâm.

### `FORMAT-002`: Punctuation Signals & Rhythm (Nhịp Điệu Dấu Câu)
- **Nguyên tắc**: Dấu câu là nốt nhạc biểu đạt cảm xúc và nhịp thở. Không cấm dấu câu; chỉ xử lý khi dấu câu bị lạm dụng như chiếc nẹp cú pháp lười biếng thay cho cấu trúc câu tự nhiên.
- **Dấu hiệu ma sát (AI Tells)**:
  - Cụm em dash (`—`) dày đặc (nhiều lần trong cùng đoạn hoặc liên tiếp qua các đoạn), làm mạch văn bị băm nhỏ vụn vặt.
  - Dấu `:` kịch tính giữa các câu văn xuôi khi không phải dẫn lời thoại hay mở đầu danh sách.
  - Dấu gạch chéo `/` nằm giữa các từ thông thường (`vấn đề/thách thức`, `quy trình/công cụ`).  
    *(Ngoại lệ an toàn: phân số `9/10`, niên độ `2025/2026`, đơn vị `km/h`, thuật ngữ công nghệ `input/output`, `CI/CD`).*
  - Lạm dụng dấu chấm than `!` trong văn phi hư cấu nghiêm túc (ngoại trừ trích dẫn lời thoại).
- **Hành động biên tập**:
  - Dùng **Syntactic Re-anchoring**: Tái cấu trúc câu bằng liên từ phụ thuộc (`khi`, `bởi vì`, `mặc dù`, `thay vì`), mệnh đề quan hệ hoặc tách câu bằng dấu chấm đanh thép. Tuyệt đối không xóa dấu mù quáng.

### `FORMAT-003`: Heading Density & Structure (Mật Độ & Cấu Trúc Tiêu Đề)
- **Nguyên tắc**: Tiêu đề là kim chỉ nam nhận thức, không phải công cụ câu view kiểu danh sách mạng xã hội.
- **Dấu hiệu ma sát**:
  - Khoảng cách giữa 2 tiêu đề (H2, H3) quá ngắn (< 200–250 từ), làm trang sách bị băm nhỏ, thiếu dung lượng để triển khai lập luận sâu.
- **Chuẩn hóa hình thức**:
  - Mỗi section file sở hữu đúng 1 tiêu đề H2 (`## [Tiêu đề Section]`).
  - Dọn sạch dấu chấm `.`, dấu hai chấm `:` hoặc chấm phẩy `;` thừa ở cuối các dòng tiêu đề (máy đã chuẩn hóa qua `repair_invariants.py`).

### `FORMAT-004`: Paragraph & Line-break Rhythm (Nhịp Điệu Đoạn Văn)
- **Nguyên tắc**: Sách phi hư cấu thở bằng những khối tư duy hoàn chỉnh (thông thường 3–6 câu/đoạn). Không ép buộc số từ cứng nhắc, nhưng kiên quyết chặn đứng kiểu xuống dòng lắt nhắt từng câu một.
- **Dấu hiệu ma sát**:
  - Chuỗi nhiều đoạn văn liên tiếp đều chỉ có duy nhất 1 câu ngắn (kiểu thơ tự do / LinkedIn influencer / copywriting).
- **Hành động biên tập**:
  - Hợp nhất các câu có chung dòng suy nghĩ hoặc quan hệ nhân quả thành một đoạn văn lập luận liền mạch.
  - Giữ lại nhịp ngắt đặc biệt nếu tác giả chủ động khai báo trong `voice.md` cho một khoảnh khắc giáng đòn nhận thức duy nhất.

### `FORMAT-005`: Markdown & Structural Artifacts (Dọn Rác Định Dạng)
- **Nguyên tắc**: Bản thảo sách không được sót lại các vết tích định dạng code hay giao diện chat.
- **Hành động làm sạch**:
  - `INLINE_CODE_IN_PROSE`: Giữ nguyên backticks cho tên hàm, biến số, thuật ngữ công nghệ (`API`, `repair_invariants.py`). Gỡ bỏ backticks bọc quanh các từ tiếng Việt thông thường (ví dụ: `` `tư duy` `` $\rightarrow$ `tư duy`).
  - Xóa sạch các thẻ HTML sót (`<br>`, `<div>`, `<span>`).
  - Chuyển hóa các khối sơ đồ Mermaid hoặc ASCII vẽ thô thành Semantic Visual Placeholders: `[VISUAL-SUGGESTION: ...]`.

### `FORMAT-006`: Prose-to-List / Chatification Ban (Chống Biến Văn Xuôi Thành Danh Sách)
- **Nguyên tắc**: Bảo vệ nghiêm ngặt tiêu chuẩn CONV-001 (Continuous Narrative Prose). Không để AI biến cuốn sách thành tập tài liệu gạch đầu dòng tóm tắt.
- **Dấu hiệu ma sát**:
  - Mật độ bullet dày đặc, vắng bóng ngữ cảnh bài tập/checklist mà vốn dĩ nội dung là mạch lập luận văn xuôi.
- **Hành động biên tập**:
  - Tái cấu trúc các ý gạch đầu dòng thành văn xuôi tự nhiên, sử dụng các bước chuyển đoạn uyển chuyển ("Trước hết...", "Mặt khác...", "Hệ quả trực tiếp là...").

---

## 3. Nghệ Thuật Phẫu Thuật Cú Pháp (Syntactic Re-anchoring)

Biên tập viên giỏi **không bao giờ xóa mù quáng dấu câu** để đạt chỉ số linter. Mọi can thiệp đều tuân thủ nguyên tắc:

### A. Kỷ Luật "WHAT TO KEEP"
Trước khi chạm vào bất kỳ câu chữ nào: Trích dẫn 1–2 câu văn đắt giá nhất của tác giả mà bạn cam kết **GIỮ NGUYÊN 100%**.

### B. Bảng Mẫu Tái Cấu Trúc Cú Pháp Chuẩn Xuất Bản (Clean Benchmark)

| Tình huống lạm dụng | Văn bản trước khi sửa (AI Tell) | Cắt gọt thô thiển (SAI) | Phẫu thuật cú pháp tự nhiên (ĐÚNG - Giữ nguyên Fact) |
|:---|:---|:---|:---|
| **Em Dash làm nẹp nối** | Kiến trúc phần mềm phân tán — xương sống vận hành của toàn bộ nền tảng — đã gặp sự cố gián đoạn nghiêm trọng. | Kiến trúc phần mềm phân tán xương sống vận hành của toàn bộ nền tảng đã gặp sự cố gián đoạn nghiêm trọng. *(Cụt ý, sai ngữ pháp)* | Kiến trúc phần mềm phân tán, vốn là xương sống vận hành của toàn bộ nền tảng, vừa trải qua một sự cố gián đoạn nghiêm trọng. *(Dùng cặp phẩy bổ ngữ tự nhiên)* |
| **Colon kịch tính giữa câu** | Lý do thực sự đằng sau thất bại của đợt cập nhật là: sự thiếu kỷ luật trong quy trình kiểm thử. | Lý do thực sự đằng sau thất bại của đợt cập nhật là sự thiếu kỷ luật trong quy trình kiểm thử. *(Cứng nhắc)* | Thất bại của đợt cập nhật bắt nguồn trực tiếp từ sự thiếu kỷ luật trong quy trình kiểm thử trước khi phát hành. *(Tái cấu trúc vị ngữ gọn gàng)* |
| **Slash viết tắt lười** | Chúng tôi phải đối mặt với vấn đề/thách thức lớn về tính sẵn sàng của hệ thống. | Chúng tôi phải đối mặt với vấn đề tính sẵn sàng của hệ thống. *(Thiếu sắc thái)* | Chúng tôi phải đối mặt với một thách thức lớn về tính sẵn sàng của hệ thống. *(Chọn từ ngữ xác thực, dứt khoát)* |
| **Staccato chat line-breaks** | Máy chủ ngừng phản hồi.<br><br>Đội trực chiến không thể truy cập cơ sở dữ liệu.<br><br>Mọi yêu cầu từ người dùng đều bị từ chối. | Máy chủ ngừng phản hồi họ không thể truy cập dữ liệu người dùng bị từ chối. *(Nối thô thiển, mất nhịp)* | Khi máy chủ ngừng phản hồi, đội trực chiến lập tức mất quyền truy cập vào cơ sở dữ liệu, khiến mọi yêu cầu từ người dùng bắt đầu bị từ chối hàng loạt. *(Gộp câu theo quan hệ nhân quả logic có sẵn, không bịa thêm tình tiết)* |
| **Bold rải rác trong văn xuôi** | Yếu tố then chốt để duy trì sự ổn định nằm ở **tính nhất quán** và **khả năng cô lập rủi ro**. | Yếu tố then chốt để duy trì sự ổn định nằm ở tính nhất quán và khả năng cô lập rủi ro. *(Gỡ bold nhưng chưa đủ nếu câu sáo rỗng)* | Muốn duy trì sự ổn định của hệ thống trong dài hạn, kiến trúc sư phần mềm phải kiểm soát được tính nhất quán và năng lực cô lập rủi ro. *(Gỡ bold, dồn sức nặng vào chính vị ngữ tự nhiên, không triết lý AI)* |

---

## 4. Tiêu Chuẩn Nghiệm Thu Biên Tập

- [ ] **Cam kết WHAT TO KEEP**: Giữ nguyên 100% các câu văn đắt giá đã chọn của tác giả.
- [ ] **Ranh giới nội dung bất biến**: Tuyệt đối không thay đổi ý nghĩa, không thêm luận điểm, không thêm số liệu và không bịa tình tiết mới.
- [ ] **Khử sạch AI Tells**: Không còn cụm bold rải rác vô cớ, không còn staccato line-breaks, không còn bullet lists trong văn tự sự.
- [ ] **An toàn cơ học**: 100% vượt qua kiểm tra cơ học `python scripts/repair_invariants.py --lint`.
- [ ] **Bài kiểm tra đọc thành tiếng (Ear Test)**: Đọc to các đoạn văn đã phẫu thuật; nhịp thở êm ái, trôi chảy, đúng tần số `voice.md`.
