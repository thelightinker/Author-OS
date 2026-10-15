# Book Writing Agent Kit (Nonfiction)

> **Agent Kit chuyên dụng để kiến tạo và chấp bút các bản thảo sách phi hư cấu (nonfiction) từ 30,000–60,000 từ chuẩn mực xuất bản cao.**  
> Kết hợp sức mạnh cơ học của kiến trúc module hóa từng section, kiểm định đối nghịch logic và tự động hóa sàng lọc chuẩn Python stdlib với sự thanh lịch của mô hình điều phối 4 vai trò (1 L0 Controller + 2 L1 Specialists + 1 L1 Critic = 4 Agents | 9 Unique Skills | 12 Bindings).


## 🎯 1. Triết Lý & Điểm Đột Phá Cốt Lõi

1. **Module Hóa Section Tuyệt Đối (Anti-Brevity Trap)**:
   - Các mô hình AI truyền thống thường mắc "bẫy tóm tắt" khi được yêu cầu viết cả một chương dài 4,000 từ: chúng tạo ra các bài liệt kê gạch đầu dòng nông cạn.
   - Kit này cưỡng chế nguyên tắc **"No Premature Draft Assembly"**: Văn xuôi chỉ được viết độc lập trong các module nhỏ `chapters/<chapter_id>/sections/*.md` (800–1,500 từ/section). File toàn chương `draft.md` chỉ là một góc nhìn tổng hợp được tạo tự động bằng script.
2. **Sợi Chỉ Nhân Quả `Leads-To` (Cognitive Domino)**:
   - Mục lục không phải một danh sách chủ đề rời rạc. Mỗi chương kết thúc bằng một nút thắt mở ra câu hỏi nhức nhối mà chỉ có chương tiếp theo mới giải quyết được.
3. **Bộ Nhớ Sống Chống Lặp Lại (`story_bank.md` & `terms.md`)**:
   - Mọi giai thoại đời thực của tác giả được quản lý tập trung và truy vết qua trường `Used In: []`, đảm bảo không bao giờ có chuyện một câu chuyện bị kể lặp lại trong sách.
4. **Hệ Thống Kiểm Định Chất Lượng 3 Lớp với Critic Độc Lập (Quality Engine)**:
   - **Layer 1**: Sàng lọc cơ học tự động siêu tốc bằng Python stdlib (`scripts/repair_invariants.py --lint`).
   - **Layer 2 (Informed Review)**: Thẩm định chương kép (Dual-Lens: Truth & Reader Prose) do `quality-auditor` trong Chế độ Chapter Review Mode thực hiện dưới quy tắc che chắn ngữ cảnh ("Blind to author intent, NOT blind to manuscript context").
   - **Layer 3 (Cold Read)**: Đọc mù toàn sách do `quality-auditor` trong Chế độ Whole-Book Review Mode thực hiện trên file `outputs/manuscript.md` duy nhất dưới hàng rào mù tuyệt đối (Absolute Blind Barrier).
5. **Liêm Chính Tự Sự & Thang Nhận Thức 5 Cấp Độ (Epistemic Provenance & Story Integrity)**:
   - Tuân thủ nguyên tắc **"Hiểu người trước, viết sau" (`COLLAB-011`)**: Khi thiếu ngữ cảnh cốt lõi về tác giả, Agent dừng lại phỏng vấn, không tự lấp khoảng trống.
   - Quản trị qua **Thang nhận thức 5 cấp độ (`COLLAB-012`)**: `VERIFIED_FACT`, `USER_STATED`, `AGENT_INFERENCE`, `HYPOTHESIS`, `UNKNOWN`. Cấm tự ý biến suy luận hoặc điều chưa biết thành sự thật.
   - Thẻ câu chuyện trong `story_bank.md` bắt buộc có **5-Part Epistemic Breakdown** và vượt qua kiểm tra Timeline Sanity tự động qua `scripts/repair_invariants.py --lint`.


## 🏛️ 2. Bốn Vai Trò Điều Phối & 10 Kỹ Năng Chuyên Sâu

```
                  ┌─────────────────────────────────────────┐
                  │    L0 Controller: master-orchestrator   │
                  │  (State Machine, Cold Read, Human Gates)│
                  └────────────┬──────────────────┬──────────┘
                               │                  │
            ┌──────────────────▼──┐            ┌──▼──────────────────┐
            │   book-architect    │            │   chapter-crafter   │
            │  (Strategy & Spine) │            │ (Socratic & Craft)  │
            └──────────┬──────────┘            └──┬──────────────────┘
                       │                          │
        ┌──────────────┴──────────────┐   ┌───────┴─────────────────────┐
        │ 1. genesis-interview        │   │ 5. chapter-blueprinting     │
        │ 2. spine-architecture       │   │ 6. story-enrichment         │
        │ 3. evidence-excavation      │   │ 7. chapter-drafting         │
        │ 4. falsification-steelmanning*  │ 8. editorial-revision       │
        └─────────────────────────────┘   │ 4. falsification-steelmanning*
                                          │ 9. humanizer                │
                                          │ 10. manuscript-formatting   │
                                          └─────────────────────────────┘
                             * Shared Skill (Context-Isolated)
```

- **`master-orchestrator`**: L0 System Controller quản trị chuyển pha và điều phối 4 Human Gates. Miễn trừ hợp đồng tạo skill giả.
- **`book-architect` (4 bindings)**: Phỏng vấn khởi tạo, cấu trúc Spine, khảo sát tư liệu thực nghiệm và phản biện luận đề vĩ mô.
- **`chapter-crafter` (7 bindings)**: Bóc tách chi tiết giác quan hiện trường, lập Card phân rã, chấp bút module section, khử dấu vết AI (humanizer), tinh chỉnh hình thức bản thảo (manuscript-formatting) và biên tập phẫu thuật 3 Pass.
- **`quality-auditor` (2 bindings)**: Thẩm định viên độc lập bảo vệ Độc giả: Chẩn đoán lực cản câu từ, lặp ý vi mô và hụt logic (Chapter Review Mode), thẩm định 10 giả thuyết đòn bẩy cao toàn sách (Whole-Book Cold Read Mode).
- **`falsification-steelmanning`**: Kỹ năng dùng chung (Shared Skill) nhưng độc lập ngữ cảnh tuyệt đối (`Shared Skill != Shared Context`).


## 🚀 3. Hướng Dẫn Sử Dụng Nhanh (Quick Start)

### Bước 1: Khai mở dự án & Thử lửa luận đề (5 Chặng tuần tự)
Chạy lệnh khởi tạo:
```bash
/book-genesis
```
1. **Chặng 1 (Tuyên ngôn & Phản biện)**: Xác định Working Title / Slug sách, phỏng vấn thích ứng 1 câu/lượt, thử tải phản biện đối nghịch $\rightarrow$ xuất `foundation/manifesto.md` $\rightarrow$ **Gate 1**.
2. **Chặng 2 (Giọng văn)**: Bóc tách đại từ xưng hô, thu thập 3–5 đoạn văn mẫu định hình nhịp thở $\rightarrow$ xuất `foundation/voice.md` $\rightarrow$ **Gate 2**.
3. **Chặng 3 (Ma trận khái niệm)**: Xác lập khái niệm giải phóng và phản đề $\rightarrow$ xuất `foundation/terms.md` $\rightarrow$ **Gate 3**.
4. **Chặng 4 (Ký ức & Story Bank)**: Khai thác biến cố giác quan đời thực $\rightarrow$ xuất `foundation/story_bank.md` $\rightarrow$ **Gate 4**.
5. **Chặng 5 (Khung xương sách & Lời hứa)**: Rẽ nhánh Path A (Top-Down) hoặc Path B (Bottom-Up 3 bước) dựng mục lục 3–4 tầng kèm `Leads-to` $\rightarrow$ xuất `foundation/book_spine.md` & `promises.md` $\rightarrow$ **Gate 5**.

### Bước 2: Sản xuất từng chương tuần tự từng Section
Chạy dây chuyền sản xuất cho chương 1:
```bash
/chapter-cycle --chapter ch_01
```
1. Lập Card phân rã 3–5 sections theo 3–4 tầng (`card.md`) $\rightarrow$ Tác giả duyệt tại **Gate 3**.
2. Bóc tách chi tiết hiện trường Socratic bổ sung cho câu chuyện của chương.
3. **Chấp bút tuần tự từng Section**: Chấp bút kết hợp `chapter-drafting` + `humanizer` co-pilot khử AI tells ngay từ đầu; mở đầu mỗi file bằng tiêu đề H2 (`## [Tiêu đề Section]`); sau mỗi section có checkpoint ngắn để tác giả xem/duyệt trước khi viết tiếp.
4. Sàng lọc cơ học tự động qua `python scripts/repair_invariants.py --lint`.
5. Biên tập phẫu thuật 3 Pass (Substance, Zinsser Clutter, Cadence).
6. Lắp ráp tự động bằng `python scripts/assemble_chapter.py --chapter ch_01 --commit`.
7. Kiểm định Layer 2 Informed Review (Auditor Mode) đánh giá Dual-Lens.
8. Cập nhật `Used In` trong `story_bank.md` và kiểm tra độ lệch Spine (`SPINE_CHECK`).

### Bước 3: Tổng hợp toàn cuốn & Đọc mù xuất bản
Khi đã hoàn thành tất cả các chương:
```bash
/book-assembly
```
1. Quét kiểm toán tính nhất quán thuật ngữ (`terms.md`) và cam kết (`promises.md`).
2. Rà soát mạch lập luận `Leads-to` xuyên suốt toàn bộ các ranh giới chương.
3. Làm mượt các câu nối chuyển tiếp (Transition Smoothing).
4. Quét chẩn đoán giọng văn toàn cục (Read-Only Voice Audit) xuất `voice_drift_report.md`.
5. Thực thi Đọc Mù Layer 3 (Cold Read) dưới hàng rào mù tuyệt đối (Absolute Blind Barrier) đọc duy nhất `manuscript.md`.
6. Tác giả thực thi quyền tối cao tại **Gate 4** và xuất bản thảo hoàn chỉnh.


## 🛠️ 4. Bộ Công Cụ Python Standard Library (Scripts Guide)

Tất cả các kịch bản đều dùng 100% Python Standard Library, không cần cài đặt bất kỳ gói pip bên ngoài nào:

### `scripts/repair_invariants.py`
Tự động làm sạch cơ học các dị tật văn bản phổ biến:
- Chuẩn hóa Unicode NFC (`unicodedata.normalize`).
- Xóa sạch ký tự tàng hình (`\u200b`, `\ufeff`).
- Sửa lỗi khoảng trắng trước dấu câu (`, . : ; ! ?`).
- Chế độ linter kiểm tra không ghi đè:
  ```bash
  python scripts/repair_invariants.py --lint Books/nhan-danh-dieu-vi-dai/chapters/ch_01/sections/
  ```

### `scripts/assemble_chapter.py`
Lắp ráp các section nhỏ thành bản thảo toàn chương:
- Xem trước số từ và thống kê phân bổ:
  ```bash
  python scripts/assemble_chapter.py --chapter ch_01 --preview
  ```
- Ghép chính thức vào `draft.md`:
  ```bash
  python scripts/assemble_chapter.py --chapter ch_01 --commit
  ```


## 🔒 5. Bảy Điều Cấm Kỵ Định Tuyến (ROUTE-001 đến ROUTE-007)

Hệ thống được khóa chặt bằng 7 ràng buộc chống hồi quy:
- **`ROUTE-001`**: Bảng điều phối trong `master-orchestrator.md` là SSOT duy nhất. Cấm script regex bên ngoài.
- **`ROUTE-002`**: Định tuyến dựa trên trạng thái tệp thực tế. Khi mơ hồ, bắt buộc dừng lại hỏi tác giả với 2 lựa chọn cụ thể thay vì đoán mò.
- **`ROUTE-003`**: Cấu trúc lưu trữ chuẩn duy nhất tại `Books/<book_slug>/` (với sổ bộ sống tại `foundation/`). Cấm các thư mục tạm rải rác (`.workspace/`, `00_control/`) và cấm tên mặc định kiểu `Mybook`/`my-book`.
- **`ROUTE-004`**: Orchestrator chỉ thực thi các workflow chính thức, cấm tự ý tạo pipeline song song tùy tiện.
- **`ROUTE-005`**: Trạng thái gắn liền với tệp thực trên đĩa. Cấm các khóa zombie như `read_by: []`.
- **`ROUTE-006`**: Giới hạn tối đa 3 vòng sửa đổi per section/chương (`revision_round: 1/3`). Phát hiện `[PLATEAU]` phải dừng khẩn cấp xin ý kiến tác giả.
- **`ROUTE-007`**: Tách bạch rạch ròi giữa Chế độ Đối thoại Sáng tạo (Interactive Mode) và Chế độ Sản Xuất Kỷ Luật (Production Mode).


## 📌 6. Phạm Vi & Giới Hạn Của Kit (Scope Boundaries)

- **Kit làm tốt nhất**: Kiến tạo kiến trúc lập luận phi hư cấu, khai thác trải nghiệm sâu, viết văn xuôi module hóa chất lượng cao và kiểm định biên tập sách chuyên sâu.
- **Kit KHÔNG làm**: Dàn trang tự động sang bản in vector phức tạp (Indesign/Typst PDF) trong bản MVP — tuy nhiên kit hỗ trợ đầy đủ các thẻ gợi ý minh họa ngữ nghĩa (`[VISUAL-SUGGESTION]`) để đội ngũ họa sĩ đồ họa triển khai sau này.
