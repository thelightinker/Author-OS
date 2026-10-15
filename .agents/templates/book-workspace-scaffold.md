<!-- Schema Authority for Books/<book_slug>/ project scaffold (Context-Aware Grounding: master-orchestrator grounds project structure against this spec) -->
# Book Workspace Scaffold: Cấu Trúc Dự Án Sách Chuẩn (SSOT)

> Bản đặc tả cấu trúc thư mục làm việc tiêu chuẩn duy nhất của một dự án viết sách phi hư cấu (`Books/<book_slug>/`). Tuân thủ nghiêm ngặt Hợp đồng Lưu trữ Chuẩn (`ROUTE-003`) và nguyên tắc 100% Pure Markdown SSOT.

---

## 1. Cấu Trúc Cây Thư Mục Toàn Diện

```
Books/<book_slug>/
├── foundation/                        # SỔ BỘ NỀN TẢNG (9 living registers)
│   ├── manifesto.md                   # Dự án luật: Luận đề, Độc giả 2h sáng, Lời hứa, Điều kiện biên
│   ├── voice.md                       # Bộ gen giọng văn: Đại từ, 5-10 đoạn mẫu, anti-patterns, từ vựng cấm
│   ├── book_spine.md                  # Khung xương 3 tầng, Governing Lines và chuỗi nhân quả Leads-to
│   ├── promises.md                    # Bảng theo dõi và trả nợ kỳ vọng độc giả (Promise Payoff Tracker)
│   ├── terms.md                       # Ma trận khái niệm sống: Khái niệm giải phóng vs Phản đề
│   ├── story_bank.md                  # Sổ bộ giai thoại đời thực kèm truy vết chống trùng lặp (Used In)
│   ├── evidence_ledger.md             # Sổ bộ chứng cứ thực nghiệm (EV-XXX) từ Tier 1-3
│   ├── decisions.md                   # Nhật ký quyết định chiến lược & Ghi nhận bất đồng (DISSENT)
│   └── summaries.md                   # Tóm tắt nhận thức cuốn chiếu của từng chương
├── chapters/
│   └── ch_01/                         # Thư mục riêng cho từng chương
│       ├── card.md                    # Bản vẽ kiến trúc chương (chứa revision_round: 0/3)
│       ├── evidence_request.md        # Phiếu yêu cầu chứng cứ khi gặp khoảng trống (nếu có)
│       ├── audit_verdict.md           # Phán quyết kiểm định Layer 2 Informed Review (nếu có)
│       ├── sections/                  # KHU VỰC CHẤP BÚT MODULE ĐỘC LẬP
│       │   ├── 00_open.md             # Mở đầu, bẻ gãy trực giác, móc câu cảm xúc (800-1,000 từ)
│       │   ├── 01_sec1.md             # Triển khai luận điểm 1 & Dữ liệu thực nghiệm (1,000-1,200 từ)
│       │   ├── 02_sec2.md             # Triển khai luận điểm 2 & Ca thực tế (1,000-1,200 từ)
│       │   └── 04_close.md            # Khoảnh khắc 5 giây, bài tập & mở nút Leads-to (600-800 từ)
│       └── draft.md                   # GÓC NHÌN TỔNG HỢP (Sinh bởi scripts/assemble_chapter.py)
├── sources/
│   ├── raw/                           # Nơi tác giả thả tài liệu thô (PDF, docx, ghi chép nhanh)
│   └── notes/                         # Ghi chú đã qua triage và kiểm chứng nguồn (Tier 1-3)
├── snapshots/                         # Khu vực lưu bản sao lưu phạm vi ảnh hưởng khi sửa Spine
└── outputs/
    ├── voice_drift_report.md          # Báo cáo quét chẩn đoán giọng văn toàn cục (Read-only)
    ├── cold_read_assessment.md        # Báo cáo thẩm định Đọc Mù Layer 3 (Advisory Verdict)
    ├── manuscript.md                  # BẢN THẢO TOÀN CUỐN HOÀN CHỈNH SẴN SÀNG XUẤT BẢN
    └── <book_slug>.pdf                # File PDF bản thảo định dạng xuất bản trang in hoàn chỉnh
```

---

## 2. Hợp Đồng Lưu Trữ Chuẩn (`ROUTE-003` Canonical Storage Contract)

1. **Quy tắc định danh và thư mục gốc**:
   - Thư mục gốc chuẩn duy nhất của mỗi cuốn sách là: `Books/<book_slug>/`.
   - Phân định rạch ròi giữa:
     - `book_title`: Tên tiếng Việt hiển thị của tác phẩm (ví dụ: *Nhân Danh Điều Vĩ Đại*).
     - `book_slug`: Tên thư mục filesystem chuẩn hóa viết thường, nối bằng gạch ngang (ví dụ: `nhan-danh-dieu-vi-dai`).
   - CẤM TUYỆT ĐỐI các tên mặc định vô nghĩa kiểu `Mybook`, `my-book`.
2. **Khu vực Sổ bộ Nền tảng (`foundation/`)**:
   - 9 file sổ bộ sống (`manifesto.md`, `voice.md`, `book_spine.md`, `promises.md`, `terms.md`, `story_bank.md`, `evidence_ledger.md`, `decisions.md`, `summaries.md`) bắt buộc cư trú trong `Books/<book_slug>/foundation/`.
   - Giữ root của cuốn sách gọn gàng, trực quan và dễ điều hướng.
3. **Tuyệt đối cấm tạo thư mục trung gian tùy tiện**:
   - CẤM tạo `.workspace/`, `00_control/`, `shared_state/`.
   - Toàn bộ dữ liệu nằm rành mạch trong `Books/<book_slug>/` với các file định danh rõ ràng.
4. **100% Pure Markdown SSOT**:
   - Không lưu trạng thái trong cơ sở dữ liệu ngầm hay JSON bí mật. Mọi quyết định, số vòng sửa đổi, và trạng thái đều được đọc trực tiếp từ frontmatter Markdown trên đĩa.
5. **Quy định bất biến về Section Files**:
   - Chấp bút và sửa đổi 100% diễn ra trong `sections/*.md`.
   - File `draft.md` chỉ là artifact phái sinh (derived view).
