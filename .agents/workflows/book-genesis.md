---
name: book-genesis
description: "Quy trình khai mở dự án sách phi hư cấu: Phỏng vấn Socratic thích ứng từng câu, thử lửa luận đề đối nghịch, khởi tạo từng sổ bộ nền tảng tuần tự qua 5 Human Gates: Manifesto -> Voice -> Stories -> Spine -> Terms."
version: 2.1.0
initial_state: GENESIS_MANIFESTO
terminal_states: [DONE]
nodes:
  GENESIS_MANIFESTO:
    required_outcome: "manifesto_created_and_stress_tested"
    human_gate: false
    transitions:
      - to: GATE_1_MANIFESTO
        when: "manifesto_interviewed == true && manifesto_exists == true"
  GATE_1_MANIFESTO:
    required_outcome: "manifesto_approved"
    human_gate: true
    transitions:
      - to: GENESIS_VOICE
        when: "gate_1_signed_off == true"
  GENESIS_VOICE:
    required_outcome: "voice_and_cadence_defined"
    human_gate: false
    transitions:
      - to: GATE_2_VOICE
        when: "voice_interviewed == true && voice_exists == true"
  GATE_2_VOICE:
    required_outcome: "voice_approved"
    human_gate: true
    transitions:
      - to: GENESIS_STORIES
        when: "gate_2_signed_off == true"
  GENESIS_STORIES:
    required_outcome: "story_bank_initialized"
    human_gate: false
    transitions:
      - to: GATE_3_STORIES
        when: "stories_interviewed == true && story_bank_exists == true"
  GATE_3_STORIES:
    required_outcome: "stories_approved"
    human_gate: true
    transitions:
      - to: PATH_SELECTION
        when: "gate_3_signed_off == true"
  PATH_SELECTION:
    required_outcome: "path_selected"
    human_gate: false
    transitions:
      - to: SOURCE_TRIAGE
        when: "selected_path == 'PATH_A'"
      - to: DRAFT_FIRST_SAMPLE
        when: "selected_path == 'PATH_B'"
  SOURCE_TRIAGE:
    required_outcome: "sources_triaged"
    human_gate: false
    transitions:
      - to: SPINE_DESIGN
        when: "evidence_ledger_initialized == true"
  SPINE_DESIGN:
    required_outcome: "spine_and_promises_created"
    human_gate: false
    transitions:
      - to: GATE_4_SPINE
        when: "book_spine_exists == true"
  DRAFT_FIRST_SAMPLE:
    required_outcome: "sample_draft_and_bottom_up_spine_created"
    human_gate: false
    transitions:
      - to: GATE_4_SPINE
        when: "bottom_up_spine_exists == true"
  GATE_4_SPINE:
    required_outcome: "spine_approved"
    human_gate: true
    transitions:
      - to: GENESIS_TERMS
        when: "gate_4_signed_off == true"
  GENESIS_TERMS:
    required_outcome: "terms_matrix_established"
    human_gate: false
    transitions:
      - to: GATE_5_TERMS
        when: "terms_interviewed == true && terms_exists == true"
  GATE_5_TERMS:
    required_outcome: "terms_approved"
    human_gate: true
    transitions:
      - to: DONE
        when: "gate_5_signed_off == true"
topology: sequential
trigger: manual
max_retry_per_node: 2
---

# Workflow: Book Genesis (/book-genesis)

> **Mục tiêu**: Thiết lập nền móng vững chắc cho dự án sách phi hư cấu qua dây chuyền cộng tác tuần tự 5 chặng độc lập: **Manifesto $\rightarrow$ Voice $\rightarrow$ Stories (Vault + Phỏng vấn) $\rightarrow$ Spine $\rightarrow$ Terms**. Thuật ngữ độc quyền được chốt sau cùng khi đã thấu hiểu toàn bộ nội dung và khung xương sách.

---

## ⚡ Chỉ Dẫn Chạy Node Độc Lập (Standalone Invocation)

Khi cần chạy lại hoặc tinh chỉnh một Node cụ thể:
- **Lệnh cú pháp**: `/book-genesis --node <NODE_NAME>`
- **Điều kiện tiên quyết**: Đảm bảo các artifact đầu vào của Node đó đã tồn tại trên đĩa (ví dụ: muốn chạy `GENESIS_VOICE` thì `foundation/manifesto.md` phải đã được duyệt tại Gate 1).

---

## 🔄 Chi Tiết 5 Chặng Tuần Tự & Hợp Đồng Chuyển Pha

### [CHẶNG 1: GENESIS_MANIFESTO] (Tuyên Ngôn & Luận Đề Thử Lửa)
- **Vai trò thực thi**: `book-architect` nạp kết hợp `genesis-interview` + `falsification-steelmanning`.
- **Input**: Trao đổi trực tiếp trong phiên chat, ghi chú ban đầu của tác giả.
- **Output Artifact**: `Books/<book_slug>/foundation/manifesto.md`.
- **Human Gate**: `false` (chuyển sang `GATE_1_MANIFESTO` sau khi đã phỏng vấn và sinh file hợp lệ).
- **Quy trình Phỏng vấn Thích ứng & Cổng Thiếu Ngữ Cảnh (COLLAB-011)**:
  1. *Insufficient-Context Gate*: Nếu tác giả chỉ cung cấp một ý tưởng sơ lược (1-2 câu), **CẤM TUYỆT ĐỐI** tự sinh file `manifesto.md` để "hỏi ý kiến sau". Agent BẮT BUỘC DỪNG LẠI và đặt đúng 1 câu hỏi Socratic sắc bén nhất để khai phá luận đề cốt lõi, độc giả mục tiêu và nỗi đau lúc 2h sáng.
  2. *Khởi tạo thư mục*: Xác định Working Title / Slug của cuốn sách để tạo thư mục không gian làm việc `Books/<book_slug>/foundation/`.
  3. *Phỏng vấn thích ứng từng câu (`Ask exactly one question at a time`)*: Đặt câu hỏi tiếp theo dựa trên khoảng trống thông tin, không dùng bảng câu hỏi dài dòng.
  4. *Thử tải phản biện (Adversarial Steelmanning)*: Tự dựng phản đề mạnh nhất, săn tìm thiên kiến kẻ sống sót, xác lập mục `## Điều Kiện Biên (Boundary Conditions: Đúng khi nào? Sai khi nào?)`.
- **DoD**:
  - [ ] Đã hoàn thành phỏng vấn khai phá luận đề với tác giả (`manifesto_interviewed == true`).
  - [ ] File `Books/<book_slug>/foundation/manifesto.md` tồn tại, chứa đầy đủ Core Thesis và tối thiểu 2 điều kiện biên sắc bén.
- **Transition Path**: `GENESIS_MANIFESTO` $\rightarrow$ `GATE_1_MANIFESTO`.

---

### [GATE 1: GATE_1_MANIFESTO]
- **Human Gate**: `true (Tác giả ký duyệt)`
- **Mục tiêu**: Trình duyệt `foundation/manifesto.md` cho tác giả nghiệm thu.
- **Lựa chọn**:
  - `APPROVE`: Khóa Tuyên ngôn, tự động chuyển sang `GENESIS_VOICE`.
  - `REVISE`: Góp ý tinh chỉnh luận đề hoặc điều kiện biên.
- **Transition Path**: Phê duyệt $\rightarrow$ `GENESIS_VOICE`.

---

### [CHẶNG 2: GENESIS_VOICE] (Nhịp Thở & DNA Giọng Văn)
- **Vai trò thực thi**: `book-architect` nạp skill `genesis-interview`.
- **Input**: `foundation/manifesto.md` đã duyệt.
- **Output Artifact**: `Books/<book_slug>/foundation/voice.md`.
- **Human Gate**: `false`.
- **Nguyên tắc Hiểu Người Trước, Viết Sau (COLLAB-011)**:
  - CẤM tự ý sinh file `voice.md` dựa trên giả định. Bắt buộc phỏng vấn tác giả:
    1. Đại từ xưng hô và thái độ tiếp cận độc giả (đồng hành, phản biện hay quan sát viên).
    2. Thu thập 3–5 đoạn văn bản mẫu của chính tác giả để phân tích nhịp thở, độ dài câu.
    3. Xác lập danh mục từ cấm kỵ (sáo ngữ marketing, biệt ngữ rườm rà).
- **DoD**:
  - [ ] Đã hoàn thành phỏng vấn giọng văn với tác giả (`voice_interviewed == true`).
  - [ ] File `Books/<book_slug>/foundation/voice.md` tồn tại, có đủ quy chuẩn xưng hô và văn mẫu định hình nhịp điệu.
- **Transition Path**: `GENESIS_VOICE` $\rightarrow$ `GATE_2_VOICE`.

---

### [GATE 2: GATE_2_VOICE]
- **Human Gate**: `true (Tác giả ký duyệt)`
- **Mục tiêu**: Trình duyệt `foundation/voice.md`.
- **Lựa chọn**:
  - `APPROVE`: Khóa giọng văn, tự động chuyển sang `GENESIS_STORIES`.
  - `REVISE`: Tinh chỉnh đại từ xưng hô hoặc bổ sung mẫu văn.
- **Transition Path**: Phê duyệt $\rightarrow$ `GENESIS_STORIES`.

---

### [CHẶNG 3: GENESIS_STORIES] (Khai Thác Ký Ức & Ngân Hàng Câu Chuyện)
- **Vai trò thực thi**: `book-architect` nạp kết hợp `author-excavation` (hoặc `genesis-interview` + `story-enrichment`).
- **Input**: `foundation/manifesto.md`, `foundation/voice.md`, canonical vault `.agents/memory/experience/story_bank.md` và phỏng vấn trực tiếp từ tác giả.
- **Output Artifact**: `Books/<book_slug>/foundation/story_bindings.md` (hoặc khởi tạo câu chuyện mới vào vault).
- **Human Gate**: `false` (chuyển sang `GATE_3_STORIES` khi đã phỏng vấn và sinh file hợp lệ).
- **Nguyên tắc "Hiểu người trước, viết sau" (COLLAB-011 & Story Integrity)**:
  1. *Cấm sinh thẻ hư cấu (Zero Ungrounded Story Generation)*: Tuyệt đối không tự ý bịa đặt câu chuyện, mốc thời gian, địa điểm hoặc cảm xúc của tác giả để tạo file `story_bank.md`. Không tự copy các câu chuyện chưa được tác giả xác nhận cho dự án này.
  2. *Phỏng vấn Socratic bóc tách ký ức (Interview-First)*: Nếu tác giả chưa cung cấp câu chuyện thực tế, Agent **BẮT BUỘC DỪNG LẠI VÀ PHỎNG VẤN** (Yield to Interview). Đặt 1 câu hỏi có giá trị thông tin cao nhất về biến cố thực tế hoặc ca phỏng vấn sâu của tác giả.
  3. *5 Trường Phân Bổ Nhận Thức (Epistemic Breakdown)*: Mọi thẻ câu chuyện bắt buộc phân định: `Confirmed Facts`, `Interview Content`, `Author Interpretation`, `Agent Inferences`, và `Unknown Details`.
  4. *Kiểm Tra Tính Hợp Lý Dòng Thời Gian (Timeline Sanity)*: Mọi câu chuyện cá nhân (Tier A) phải khớp với năm sinh và tiểu sử trong `identity.md`. Cấm các mốc thời gian phi lý.
- **DoD**:
  - [ ] Đã hoàn thành phỏng vấn bóc tách câu chuyện thực tế với tác giả (`stories_interviewed == true`).
  - [ ] File `Books/<book_slug>/foundation/story_bindings.md` tồn tại, 100% thẻ câu chuyện có Epistemic Breakdown, 0% chi tiết bịa đặt, và pass kiểm tra Timeline Sanity (`stories_interviewed == true && story_bank_exists == true`).
- **Transition Path**: `GENESIS_STORIES` $\rightarrow$ `GATE_3_STORIES`.

---

### [GATE 3: GATE_3_STORIES]
- **Human Gate**: `true (Tác giả ký duyệt)`
- **Mục tiêu**: Trình duyệt danh mục câu chuyện thực tế đã đối chiếu nguồn gốc xác thực.
- **Lựa chọn**:
  - `APPROVE`: Khóa Stories, chuyển sang chọn lộ trình xây dựng khung xương `PATH_SELECTION`.
  - `REVISE`: Bổ sung hoặc chỉnh sửa chi tiết câu chuyện.
- **Transition Path**: Phê duyệt $\rightarrow$ `PATH_SELECTION`.

---

### [NODE: PATH_SELECTION]
- **Mục tiêu**: Tác giả chọn 1 trong 2 lộ trình xây dựng khung xương:
  - **Path A (Top-Down / TOC-First)**: Đã có sẵn đề cương hoặc nhiều tư liệu $\rightarrow$ `SOURCE_TRIAGE` $\rightarrow$ `SPINE_DESIGN`.
  - **Path B (Bottom-Up / Draft-First)**: Viết thử ngay 1 section để tìm nhịp rồi tổng hợp ngược $\rightarrow$ `DRAFT_FIRST_SAMPLE`.

---

### [CHẶNG 4A: SOURCE_TRIAGE & SPINE_DESIGN] (Chỉ chạy trên Path A)
- **Vai trò thực thi**: `book-architect` nạp `evidence-excavation` (khi phân loại nguồn) và `spine-architecture` (khi thiết kế khung xương).
- **Nguyên Tắc Dựng TOC Thích Ứng (Certainty-Driven Progressive TOC)**:
  - Chọn mức độ phân giải (L0 $\rightarrow$ L3) dựa trên độ chắc chắn của ý tưởng và trạng thái tài liệu; không ép quy trình 4 bước bắt buộc.
  - **No Premature Full TOC**: Tuyệt đối cấm sinh full mục lục chi tiết khi luận đề cốt lõi hoặc cấu trúc khối chưa được tác giả chốt.
- **Output Artifacts**: `Books/<book_slug>/foundation/book_spine.md`, `Books/<book_slug>/foundation/promises.md`.
- **Quy chuẩn Cấu trúc Phân cấp Linh hoạt**:
  - Hỗ trợ chuẩn 3 tầng (`Part > Chapter > Section`) hoặc 4 tầng (`Part > Chapter > Section > Subsection/Beat`).
  - Thiết lập chuỗi domino nhân quả `Leads-to` giữa các chương giáp ranh.
  - Lập bảng cam kết đền đáp kỳ vọng `promises.md`.
- **DoD**: File `book_spine.md` và `promises.md` tồn tại hợp lệ.
- **Transition Path**: `SPINE_DESIGN` $\rightarrow$ `GATE_4_SPINE`.

---

### [CHẶNG 4B: DRAFT_FIRST_SAMPLE] (Chỉ chạy trên Path B)
- **Quy trình 3 bước tuần tự**:
  - Bước 4B.1: `chapter-crafter` nạp `chapter-blueprinting` tạo thẻ mẫu `chapters/ch_sample/card.md` [DRAFT-READY].
  - Bước 4B.2: `chapter-crafter` nạp `chapter-drafting` + `humanizer` chấp bút 1 section mẫu (~1,000 từ) có tiêu đề H2 ở đầu vào `chapters/ch_sample/sections/00_open.md`.
  - Bước 4B.3: `book-architect` nạp `spine-architecture` tổng hợp ngược Bottom-Up thành toàn bộ khung xương `book_spine.md` và `promises.md`.
- **DoD**: `book_spine.md` và section mẫu tồn tại hợp lệ.
- **Transition Path**: `DRAFT_FIRST_SAMPLE` $\rightarrow$ `GATE_4_SPINE`.

---

### [GATE 4: GATE_4_SPINE]
- **Human Gate**: `true (Tác giả ký duyệt toàn bộ khung xương)`
- **Mục tiêu**: Nghiệm thu toàn bộ Khung xương sách 3–4 tầng (`book_spine.md`) và Bảng cam kết (`promises.md`).
- **Lựa chọn**:
  - `APPROVE`: Khóa Spine, chuyển sang chốt thuật ngữ `GENESIS_TERMS`.
  - `REVISE`: Tinh chỉnh tên chương, các section hoặc luồng Leads-to.
- **Transition Path**: Phê duyệt $\rightarrow$ `GENESIS_TERMS`.

---

### [CHẶNG 5: GENESIS_TERMS] (Hệ Thống Khái Niệm & Ma Trận Phản Đề)
- **Vai trò thực thi**: `book-architect` nạp skill `genesis-interview`.
- **Input**: `foundation/manifesto.md`, `foundation/book_spine.md`, `foundation/story_bindings.md`.
- **Output Artifact**: `Books/<book_slug>/foundation/terms.md`.
- **Human Gate**: `false`.
- **Nguyên tắc Khai Phá Khái Niệm Thực Tế (COLLAB-011)**:
  - Khi đã rõ toàn bộ các chương và câu chuyện, chốt hệ thống thuật ngữ độc quyền:
    1. Khái niệm giải phóng: Từ khóa/định nghĩa mới mở khóa nhận thức.
    2. Phản đề: Khái niệm/thói quen độc hại cần bị triệt hạ.
    3. Đích đến tối hậu: Trạng thái giải phóng của độc giả.
- **DoD**:
  - [ ] Đã phỏng vấn xác lập ma trận khái niệm với tác giả (`terms_interviewed == true && terms_exists == true`).
  - [ ] File `Books/<book_slug>/foundation/terms.md` tồn tại trên đĩa, định nghĩa sắc bén (≤ 3 dòng/thuật ngữ).
- **Transition Path**: `GENESIS_TERMS` $\rightarrow$ `GATE_5_TERMS`.

---

### [GATE 5: GATE_5_TERMS]
- **Human Gate**: `true (Tác giả ký duyệt)`
- **Mục tiêu**: Trình duyệt `foundation/terms.md` sau khi đã đối chiếu với khung xương và giai thoại thực tế.
- **Lựa chọn**:
  - `APPROVE`: Khóa Terms. Hoàn tất Book Genesis $\rightarrow$ Chuyển sang trạng thái `DONE`. Toàn bộ dự án sẵn sàng cho `/chapter-cycle --chapter ch_01`.
  - `REVISE`: Điều chỉnh tên thuật ngữ hoặc định nghĩa.
- **Transition Path**: Phê duyệt $\rightarrow$ `DONE`.
