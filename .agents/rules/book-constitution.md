---
name: book-constitution
version: 2.0.0
priority: P0
trigger: always_on
description: "Hiến pháp kiến trúc workspace và bản đồ SSOT: chuẩn Books/<book_slug>/, cô lập ngữ cảnh đơn tác tử, module hóa sections và quy ước token."
---

# Rule: Book Writing Constitution (Hiến Pháp Cấu Trúc & Bản Đồ SSOT)

> "Bản thảo xuất sắc được xây dựng trên sự trung thực của dữ liệu, sự rành mạch của từng module và sự tôn trọng đối với cấu trúc hệ thống."

---

## 📌 Phân loại Trigger
- **`always_on`**: Luôn luôn tự động nạp để quản trị cấu trúc thư mục, nguồn sự thật (SSOT) và an toàn kiến trúc.

---

## 1. Cấu Trúc Workspace Chuẩn (`Books/<book_slug>/`)

Toàn bộ dữ liệu dự án tuân thủ cấu trúc lưu trữ 100% Pure Markdown SSOT:

```text
Books/<book_slug>/
├── foundation/               # Sổ bộ dự án tập trung (SSOT nền tảng)
│   ├── manifesto.md          # Tôn chỉ, luận đề và độc giả mục tiêu
│   ├── voice.md              # Kim chỉ nam giọng văn & Gold Passages
│   ├── book_spine.md         # Xương sống sách, mục lục & Reader Journey
│   ├── promises.md           # Lời hứa & biến đổi nhận thức của độc giả
│   ├── terms.md              # Thuật ngữ & khái niệm độc quyền
│   ├── story_bindings.md     # Ánh xạ Story ID (S-XXX) vào các chương
│   ├── evidence_ledger.md    # Sổ cái chứng cứ & kiểm chứng luận điểm
│   ├── decisions.md          # Nhật ký quyết định & DISSENT override
│   └── summaries.md          # Tóm tắt lũy tiến các chương đã duyệt
├── chapters/<ch_id>/         # Bản thảo từng chương
│   ├── card.md               # Card v3 Blueprint & Beat Map
│   ├── sections/*.md         # NGUỒN SỰ THẬT DUY NHẤT (SSOT) của văn xuôi
│   └── draft.md              # Bản xem tổng hợp (assembled view, sinh tự động)
├── outputs/                  # Thành phẩm hoàn chỉnh
│   ├── manuscript.md         # Toàn bộ bản thảo sách đã compile
│   └── cold_read_assessment.md # Đánh giá độc giả độc lập
└── sources/                  # Tài liệu đầu vào (raw/, notes/)
```

---

## 2. Bản Đồ Nguồn Sự Thật (SSOT Map & Invariants)

1. **Modular Section Invariant ("No Premature Draft Assembly")**:
   - Mọi hoạt động chấp bút và biên tập văn bản diễn ra 100% trong `sections/*.md`.
   - File `draft.md` chỉ là bản phái sinh được sinh ra bởi `scripts/assemble_chapter.py`. Cấm tuyệt đối chỉnh sửa trực tiếp trên `draft.md`.

2. **Single Active Agent & Context Reset Boundary (`SEQ-001`, `SEQ-006`, `SEQ-007`)**:
   - Tại bất kỳ thời điểm nào, duy nhất 1 Agent hoạt động. Cấm bundle nhiều Agent chạy song song.
   - Khi chuyển vai giữa các Agent (`master-orchestrator` → `book-architect` → `chapter-crafter` → `quality-auditor`), bắt buộc thực hiện **Context Reset**. Agent mới khởi động với ngữ cảnh sạch, chỉ nạp prompt của mình và file trên đĩa.

3. **Shared Skill Isolation (`Shared Skill != Shared Context`)**:
   - Skill dùng chung (`falsification-steelmanning`) chỉ có 1 bản duy nhất trên đĩa, nhưng ngữ cảnh thực thi hoàn toàn độc lập theo vai trò.

4. **Story Vault & Bindings Contract**:
   - Kho giai thoại đời thực lưu tại `.agents/memory/experience/story_bank.md` (SSOT).
   - Mỗi sách chỉ lưu ánh xạ tại `foundation/story_bindings.md`, trỏ tới mã `S-XXX` hợp lệ.

---

## 3. Bộ Token Chuẩn Cho Chỗ Trống (Gap Token Standard)

Trong quá trình chấp bút, nếu có khoảng trống cần xử lý, sử dụng các token chuẩn minh bạch:
- `[PENDING: ...]`: Hạng mục tác giả hoặc biên tập cần hoàn thiện sau.
- `[QUERY: ...]`: Câu hỏi cần tác giả phản hồi trong buổi phỏng vấn tiếp theo.
- `[VERIFY: ...]`: Thông tin cần đối soát trước khi hoàn tất bản thảo.
- `[AUTHOR: ...]`: Vị trí dành riêng cho ý kiến chỉ đạo hoặc chi tiết của tác giả.
- `[EVIDENCE-REQUEST: req_XX]`: Yêu cầu khảo sát chứng cứ bàn giao cho `book-architect`.
- Semantic Visual Placeholders: `[VISUAL-SUGGESTION: ...]`, `[FIGURE-PLACEHOLDER: ...]`. Cấm đưa Mermaid raw vào bản thảo.
