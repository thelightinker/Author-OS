---
name: chapter-blueprinting
description: "Thiết kế bản vẽ chi tiết Chapter Card v3 (card.md): Lựa chọn Chapter Shape, xây dựng Beat Map với Reader Promise và đúng 1 nhịp PEAK, ấn định trần ngân sách chữ budget_words_max, gán nguồn dữ liệu tác giả từ insight_brief và story_bank, chống Recognition Redundancy và Climax Inflation."
when_to_use: "Khi bắt đầu một chu kỳ thiết kế chương mới trong Chapter Cycle (Stage 2: Design) để chuẩn bị trình tác giả duyệt tại Gate 3 Card Approval qua Dialogue Mode."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 2.0.0
---
# Chapter Blueprinting: Thiết Kế Bản Vẽ Kiến Trúc Chương (Card.md v3)

> "Đừng bao giờ để nhà văn đối diện với trang giấy trắng của một chương dài. Hãy thiết kế một Reader Journey có mục đích rõ ràng, một Reader Promise đanh thép, và một Beat Map với đúng 1 đỉnh cao trào PEAK."

## 0. Schema Authority & Context-Aware Grounding

- **Schema Authority**:
  - `templates/chapter-card-template.md`: Chuẩn cấu trúc Card v3 bắt buộc cho `chapters/<id>/card.md` (frontmatter `card_version`, `shape`, `budget_words_max`, `Reader Promise`, `Entry/Exit State`, `Beat Map` với giá trị mới cho người đọc).
  - `knowledge/structure/chapter_shapes.md`: Tham khảo 5 hình thái cấu trúc chương (`story-unpack-apply`, `myth-bust`, `problem-turn-practice`, `question-journey`, `contrast-pair`).
- **Quy tắc Grounding**:
  - Khi khởi tạo thẻ Card mới, bắt buộc ground vào schema của `chapter-card-template.md`.
  - **Context-Aware Exemption**: Nếu template hoặc card mẫu đã có mặt trong ngữ cảnh phiên làm việc hoặc đã được nạp qua workflow, **KHÔNG đọc lại** để tránh lãng phí token (Anti-Spam Invariant).

---

## 1. Cấu Trúc Bản Vẽ Chapter Card v3 (`chapters/<id>/card.md`)

Mỗi chương trước khi viết phải có một bản vẽ được duyệt mang trạng thái `status: approved` với các thành phần:

1. **Thông tin định danh & Quản trị phiên bản**:
   - `chapter_id`: `ch_01`
   - `card_version`: 1 (tăng mỗi khi tác giả duyệt phiên bản mới; các section bắt buộc mang `card_version` khớp với card).
   - `shape`: Lựa chọn từ 5 Chapter Shapes (`story-unpack-apply`, `myth-bust`, `problem-turn-practice`, `question-journey`, `contrast-pair`).
   - `budget_words_max`: Trần ngân sách từ tối đa cho toàn chương (mặc định 3500 từ). Ngân sách chữ là TRẦN, không phải sàn.
   - `status`: `draft` -> `approved` (chỉ chuyển sang `approved` khi tác giả đồng thuận).

2. **Reader Promise & Chuyển Dịch Nhận Thức (Entry State -> Exit State)**:
   - **Reader Promise**: Lời hứa danh dự của chương — người đọc mang về được điều gì cụ thể (1 câu duy nhất).
   - **Entry State**: Người đọc bước vào chương với bế tắc, cảm xúc hoặc ngộ nhận gì.
   - **Exit State**: Người đọc rời khỏi chương với năng lực, lăng kính hoặc nhận thức mới nào.

3. **Beat Map & Đỉnh Cao Trào (Single PEAK Invariant)**:
   - Bản đồ phân rã 4–7 beats rõ ràng theo bảng:
     `| beat | role | new_for_reader (giá trị mới cho người đọc) | anchor (chỗ dựa) | ~words |`
   - Mỗi beat phải có `new_for_reader` và `anchor`. `new_for_reader` là một câu, khác hẳn các beat trước, và không được chỉ lặp lại luận điểm của chương. Nếu hai beat không thể có `new_for_reader` khác nhau thì gộp thành một beat. `anchor` là mã story hoặc mục bằng chứng cụ thể; không có thì ghi `none`, và beat đó chỉ được làm câu nối tối đa 2 câu. Khi trình tác giả duyệt, nói bằng lời thường: ở mỗi phần, độc giả sẽ hiểu thêm điều gì, và phần đó dựa vào chuyện hoặc bằng chứng nào; phần nào chưa có chỗ dựa thì nói rõ để tác giả bổ sung hoặc đồng ý để nó chỉ làm câu nối.
   - **Đúng 1 nhịp PEAK (Single PEAK Invariant)**: Mỗi chương chỉ có duy nhất 1 beat đóng vai trò đỉnh cao trào nhận thức (PEAK). Cấm tạo nhiều đỉnh giả gây mệt mỏi và lạm phát cảm xúc (Anti-Climax Inflation).
   - **Giá trị mới duy nhất (Anti-Recognition Redundancy)**: Mỗi beat phải cung cấp một giá trị mới khác biệt hoàn toàn với các beats còn lại. Không lặp lại cùng một thông điệp hay bài học dưới nhiều hình thức diễn đạt khác nhau.
   - **Minh bạch nguồn gốc**: Mọi beat sử dụng chất liệu cá nhân phải ghi rõ `nguồn` (`insight_brief §Core`, `S-XXX`, hoặc trích dẫn tác giả).
4. **Phân Rã Sections, Hợp Đồng Chức Năng & Ranh Giới (Section Breakdown, Function & Boundary Contracts)**:
   Phân bổ các nhịp nhận thức vào các file module độc lập, với hai trường bắt buộc trong từng section:
   - `intended_destination`: La bàn định hướng mềm xác định bước chuyển nhận thức hoặc cảm xúc cụ thể mà độc giả đạt được sau khi đọc xong section. Được phép cập nhật linh hoạt nếu trong quá trình viết phát hiện insight hoặc bằng chứng sâu sắc hơn.
   - `out_of_scope`: Danh mục các khía cạnh loại trừ có lý do (những ý tưởng dù hay nhưng không trực tiếp phục vụ cho đích đến của section này, hoặc đã thuộc quyền sở hữu của chương khác).
   - **Nguyên tắc Zinsser Scope (Trọng Tâm & Ranh Giới)**: Mỗi section xác định đúng **một trọng tâm nhận thức chính** cùng các ý phụ hỗ trợ cần thiết để phát triển lập luận; kiên quyết loại trừ hội chứng muốn nói hết mọi điều (definitiveness complex).
   - **Linh hoạt thể loại nội dung (Không ép khuôn con người vận động)**: Phân loại rõ loại nội dung: *Narrative* (tự sự/ký ức), *Analytical* (phân tích cơ chế tâm lý), *Conceptual* (tái định nghĩa tư duy), hoặc *Research* (dữ liệu chứng cứ). Tuyệt đối không áp đặt điều kiện cứng ép buộc mọi beat phải có con người thực hiện hành động cụ thể; cho phép các beat phân tích khái niệm trừu tượng, mô hình logic, và khảo sát dữ liệu thực nghiệm khi thể loại nội dung yêu cầu.
   - Ngân sách từ ngữ tuân theo nguyên tắc cô đọng: mỗi câu chữ đều phải đóng góp vào bước chuyển nhận thức, không áp đặt hạn ngạch từ cứng nhắc làm loãng bài viết.

   - `00_open.md`: Đặt vấn đề, bẻ gãy trực giác hoặc mở khoảng trống tò mò (`BEFORE` + `COLLISION`).
   - `01_sec1.md`: Phân tích cơ chế ngầm & dữ liệu thực nghiệm (`INSIGHT`).
   - `02_sec2.md`: Luận điểm giải phóng & ca nghiên cứu điển hình (`REFRAME`).
   - `04_close.md`: Hệ quả, bài tập tự vấn và mở nhịp chuyển tiếp `Leads-to` (`CONSEQUENCE` + `AFTER`).

   **Hợp Đồng Chức Năng Module (Module Function Contract)**:
   - Bản thiết kế chương (`card.md`) phân định rõ chức năng kiến trúc của từng vị trí:
     - `Open / Lời mở đầu` (`00_open.md`): Chức năng là **gợi mở, đặt vấn đề, tạo điểm chạm tò mò và bẻ gãy trực giác cũ**. Không ôm đồm giải thích toàn bộ cơ chế, không biến thành mục lục tóm tắt nội dung cuốn sách.
     - `Section Thân bài` (`0N_secX.md`): Chức năng là **triển khai sâu 1 beat trải nghiệm / luận điểm cụ thể**. Không mang vác trọng trách đúc kết toàn bộ chương sách.
     - `Close / Kết chương` (`0N_close.md`): Chức năng là **đúc kết nhận thức toàn chương, chuyển hóa tâm thế và mở nhịp chuyển tiếp (`Leads-to`)**. Không phân tích lại nội dung chi tiết của thân bài.
   - Mỗi beat trong Card cần được gán đúng vào module có chức năng tương ứng.

   **Ranh Giới Module & Phạm Vi Loại Trừ (Boundary Contract)**:
   - Mỗi section trong `card.md` phải được xác định rõ trọng tâm nhận thức và điều cần tránh lấn ranh giới:
     - Section thân bài (`0N_secX.md`): Tập trung giải quyết trọn vẹn 1 nhiệm vụ nhận thức. Tránh mở đầu bằng việc tóm tắt lại bài học của section trước; tránh kết thúc bằng việc nhảy sang kết luận của section sau hay kết luận của cả chương.
     - Section kết thúc chương (`0N_close.md`): Đảm nhiệm việc đúc kết nhận thức toàn chương và mở nhịp chuyển tiếp (`Leads-to`). Không viết gộp chung vào section nội dung cuối cùng.
   - Khi thiết kế Card: Bổ sung lưu ý ranh giới nhận thức (`boundary_note`) cho từng beat nếu hai beat liền kề có nguy cơ giao thoa chủ đề.
5. **Phân Bổ Tải Trọng Nhận Thức (Cognitive Payload Allocation & Incremental Value)**:
   Để diệt trừ tận gốc lỗi lặp ý (Semantic Repetition) ngay từ sàn thiết kế:

   - **`Introduces Payload`**: Khai báo rõ nhận thức hoặc cơ chế mới xuất hiện lần đầu tiên trong section này.
   - **`Incremental Value Contract`**: Nếu section có chạm vào một insight đã từng xuất hiện ở các section trước hoặc chương trước, **BẮT BUỘC** phải nêu rõ chức năng gia tăng (`Deepen` — đào sâu cơ chế, `Reframe` — đổi góc nhìn đối nghịch, `Apply` — thực thi cụ thể). Nghiêm cấm mọi hình thức lặp lại cùng một tải trọng nhận thức chỉ để diễn giải lại mà không tạo ra giá trị mới.
6. **Giàn Giáo Cầu Nối Lập Luận (Reasoning Bridge Scaffold)**:
   Để ngăn chặn triệt để bước nhảy cóc logic ($A \rightarrow C$ thiếu $B$):

   - Mỗi beat phải chỉ rõ nhịp cầu nối nhân quả với beat trước đó: *"Vì sao khi độc giả vừa thấu suốt luận điểm A thì nhu cầu tự nhiên tiếp theo là phải bước sang luận cứ B?"*.
7. **Ràng Buộc Khái Niệm & Câu Chuyện (Story & Concept Binding / Understand-Before-Draft)**:

   - `concept_roles`: Ánh xạ trực tiếp từ `terms.md`.
   - `story_bank_ids`: Các mã thẻ `S-XXX` dự kiến đưa vào, cam kết chưa có trong `Used In`.
   - **Ràng buộc Understand-Before-Draft (COLLAB-011)**: Nếu một beat yêu cầu câu chuyện cá nhân hoặc biến cố thực tế của tác giả nhưng chưa có thẻ `S-XXX` tương ứng trong `story_bank.md` (hoặc thẻ chưa có `Confirmed Facts` / `Interview Content`), Card **CẤM** chuyển trạng thái `[DRAFT-READY]`. Phải kích hoạt phỏng vấn bóc tách (`story-enrichment`) trước khi chấp bút, tuyệt đối không để Crafter tự bịa câu chuyện khi viết section.
8. **Thiết Kế Mô Hình Tư Duy & Phản Biện Hoài Nghi (Mental Model & Skeptic's Challenge)**:
   Để biến một nhận xét quen thuộc thành một mô hình nhận thức có giá trị ứng dụng cao, mỗi beat phân tích hoặc tái định nghĩa trong Blueprint bắt buộc xác định:
   - **`skeptic_question`**: Câu hỏi hoài nghi hoặc phản bác tự nhiên nhất của một độc giả khó tính (ví dụ: *"Khi nào việc dừng lại hay đổi hướng là quyết định chiến lược đúng đắn chứ không phải là sự né tránh?"*).
   - **`boundary_condition`**: Điều kiện biên của lập luận — Đúng khi nào, Sai khi nào, đâu là ngoại lệ chiến lược?
   - **`diagnostic_test`**: Tiêu chí hoặc câu hỏi tự vấn cụ thể để độc giả phân biệt được hai trạng thái đối nghịch trong đời sống thực.


---

## 2. Quy Trình 3 Bước Lập Blueprint & Hợp Đồng Pre-Card Intent Echo

1. **Pha 1: Pre-Card Intent Echo & Điểm Dừng Bắt Buộc (Echo & Yield Barrier)**:
   - Đọc ngữ cảnh thẩm quyền: `foundation/manifesto.md`, dòng `Governing Argument` và `Leads-to` trong `book_spine.md`, `terms.md`, `story_bank.md`, và `chapters/<id>/intent_ledger.md` (nếu đã có).
   - Xuất bản bản tóm tắt **Pre-Card Intent Echo** gồm 5 trường định hướng vào chat:
     * **Core Governing Thesis**: Trọng tâm nhận thức độc nhất của chương này, phân biệt rõ với các chương trước và sau.
     * **Boundary Conditions**: Điều kiện biên — lập luận đúng khi nào, sai khi nào, đâu là ngoại lệ chiến lược?
     * **Author Red Lines**: Ranh giới cấm kỵ của tác giả (ví dụ: không mẹo vặt self-help, không checklist cơ học, không thuật ngữ khoa học chưa kiểm chứng).
     * **Concrete Anchors**: Chất liệu neo giữ đời thực (mã thẻ `S-XXX`, ca nghiên cứu, ghi chú kiểm chứng).
     * **Open Ambiguities**: Những khoảng trống nhận thức còn $\ge 2$ hướng hiểu cần tác giả chốt lựa chọn.
   - 🛑 **DỪNG HẲN (Yield to Author)**: Chờ tác giả gửi phản hồi xác nhận ("ok", "duyệt", hoặc góp ý điều chỉnh). **CẤM TUYỆT ĐỐI** gọi tool tạo file `chapters/<id>/card.md` khi tác giả chưa xác nhận bản Echo trong phiên làm việc.
2. **Pha 2: Soạn thảo `chapters/<id>/card.md`**:
   - Ghi nhận các quyết định đã xác nhận vào `chapters/<id>/intent_ledger.md` với nhãn `[CONFIRMED]`.
   - Phân chia beats cụ thể theo Chapter Shape, tích hợp các mỏ neo và giá trị mới cho người đọc (`new_for_reader`), ấn định hạn ngạch từ cho từng section file để tổng từ đạt 3,500–5,000 từ/chương.
3. **Trình duyệt Gate 3 Nghiệm Thu Blueprint (100% Author Gate)**:
   - **Bắt buộc 100% duyệt Card**: Tác giả trực tiếp phê duyệt `card.md` tại Gate 3 ở 100% các chương của cuốn sách. Tuyệt đối cấm cơ chế tự động bỏ qua (`auto_proceed`) ở cấp độ duyệt Blueprint.
   - `always_ask`: Tác giả duyệt Card trực tiếp qua hội thoại.
   - `sample_first`: Tác giả duyệt Card kèm 1 section mẫu.

---

## 3. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (Dòng Spine của Chapter 02):

```
Chapter 02: 4 Bình Nhiên Liệu Con Người — Năng lượng vận hành qua 4 bình chứa độc lập: Thể chất, Cảm xúc, Trí tuệ và Tinh thần.
```

### Output (`chapters/ch_02/card.md`):

```markdown
---
chapter_id: ch_02
title: "4 Bình Nhiên Liệu Con Người"
archetype: Analytical
revision_round: 0/3
status: "[DRAFT-READY]"
target_word_count: 3800
story_bank_ids: ["S-004", "S-007"]
---

# Chapter Blueprint: 4 Bình Nhiên Liệu Con Người

## 1. Governing Argument
Năng lượng con người không phải một khối đồng nhất; nó vận hành qua 4 bình chứa độc lập (Thể chất, Cảm xúc, Trí tuệ, Tinh thần) và chỉ cần 1 bình bị rò rỉ, toàn bộ động cơ sẽ chết máy dù 3 bình kia còn đầy.

## 2. The 5-Second Transformation Moment
Vị CEO bước vào phòng họp quan trọng sau 10 tiếng ngủ ngon (bình thể chất đầy 100%) nhưng chỉ một tin nhắn phản bội từ cộng sự lúc 8:55 sáng đã làm tê liệt hoàn toàn khả năng ra quyết định trong 5 giây (bình cảm xúc rò rỉ chạm đáy).

## 3. Section Breakdown & Beats
- **`00_open.md` (900 từ) [BEFORE + COLLISION]**: 
  - *Beats*: Mở đầu bằng nghịch lý "Ngủ đủ 8 tiếng nhưng sáng thức dậy vẫn thấy kiệt quệ". Giới thiệu ẩn dụ 4 bình nhiên liệu. Gán câu chuyện `S-004`.
  - *Introduces Payload*: Khái niệm 4 bình nhiên liệu độc lập.
  - *Incremental Value*: N/A (mở đầu chương).
  - *Reasoning Bridge*: Mở màn bẻ gãy trực giác để chuẩn bị cho việc khảo sát cơ chế sinh học ở Section 1.
- **`01_sec1.md` (1100 từ) [INSIGHT]**: 
  - *Beats*: Khảo sát Bình Thể chất và Bình Cảm xúc. Bẻ gãy lầm tưởng rằng thể lực có thể bù đắp cho tổn thương tâm lý. Trích dẫn nghiên cứu nhịp tim `EV-005`.
  - *Introduces Payload*: Cơ chế rò rỉ cảm xúc qua hormone cortisol.
  - *Incremental Value*: `Deepen` (đào sâu vào 2 bình đầu tiên mà không nhai lại ẩn dụ chung).
  - *Reasoning Bridge*: Vì độc giả đã nhận ra sự kiệt quệ không do thiếu ngủ, bước tiếp theo phải chứng minh cơ chế tổn thương cảm xúc.
- **`02_sec2.md` (1100 từ) [REFRAME]**: 
  - *Beats*: Khảo sát Bình Trí tuệ và Bình Tinh thần. Khái niệm giải phóng từ `terms.md`: "Mục Đích Sống Như Van Điều Áp". Gán câu chuyện `S-007`.
  - *Introduces Payload*: Van xả áp tinh thần.
  - *Incremental Value*: `Reframe` (chuyển dịch từ quản lý năng lượng cơ thể sang neo đậu ý nghĩa cuộc sống).
  - *Reasoning Bridge*: Từ cơ chế cảm xúc ở Sec 1 dẫn sang động cơ tinh thần tối hậu ở Sec 2.
- **`04_close.md` (700 từ) [CONSEQUENCE + AFTER]**: 
  - *Beats*: Công cụ tự chẩn đoán bình rò rỉ trong 3 phút. Mở nút `Leads-to` sang Chapter 03 về các nghi thức sạc năng lượng theo chu kỳ 90 phút.
  - *Introduces Payload*: Thang đo tự chẩn đoán 3 phút.
  - *Incremental Value*: `Apply` (chuyển hóa toàn bộ lý thuyết thành hành động tự đánh giá ngay).
  - *Reasoning Bridge*: Sau khi hiểu trọn vẹn 4 bình, người đọc cần ngay công cụ hành động trước khi bước sang chương giải pháp tiếp theo.
```

---

## 4. Tiêu Chuẩn Nghiệm Thu

- [ ] Phân rã tối thiểu 3–4 section files rõ ràng với tên file chuẩn (`00_open.md`, `01_sec1.md`, ...).
- [ ] Có hạn ngạch từ cụ thể cho từng section file (500–1,500 từ).
- [ ] Định nghĩa rõ ràng Khoảnh khắc chuyển hóa 5 giây.
- [ ] Trạng thái sẵn sàng cho Gate 3.

---

## Related Skills

| Skill                  | Khi nào dùng                                                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `spine-architecture` | Khớp nối các beats với dòng lập luận`Governing Line` và logic chuyển tiếp `Leads-to` từ khung xương sách. |
| `story-enrichment`   | Bóc tách chi tiết hiện trường các câu chuyện gán vào beats trước khi bước vào viết nháp.                  |
| `chapter-drafting`   | Chuyển giao các beats từ`card.md` sang văn xuôi module hóa độc lập.                                              |
