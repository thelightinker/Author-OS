# Node 8: INFORMED_REVIEW

- **Chủ thể điều phối**: `master-orchestrator` nạp file này để thiết lập Worker Briefing và quản trị rẽ nhánh/ngắt lặp.
- **Vai trò thực thi kiểm định**: `quality-auditor` trong **Chapter Review Mode** (Critic độc lập).
- **Quy trình Kiểm định 2 Lượt Độc Lập (Two-Pass Independent Audit)**:
  - **LƯỢT 1 — Cold Read (Thẩm Định Trải Nghiệm Độc Giả)**:
    - Auditor đóng vai trò độc giả ngoài đời thực; **ĐƯỢC NẠP**: `chapters/<id>/draft.md`, `chapters/<id>/card.md`, `summaries.md` (Payload Registry để chống lặp ý), `terms.md`, `voice.md`, và rule [quality-engine.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/quality-engine.md).
    - **TUYỆT ĐỐI CẤM NẠP**: `foundation/manifesto.md`, `foundation/book_spine.md`, `chapters/<id>/intent_ledger.md`, `sources/`, `evidence_ledger.md`, hay nhật ký trò chuyện lúc chấp bút.
    - Tiêu chuẩn: 15 bệnh học lâm sàng (Awkward Prose, Verbosity, Megaphone Cliche, Metaphor Inflation...).
    - **Kiểm tra bổ sung theo card (Reader Progression Check)**: Khi card có `new_for_reader` và `anchor`. Với mỗi section: (a) section có đem lại điều ghi ở `new_for_reader` không; (b) phép thử đoán trước: chỉ đọc câu đầu của section, đoán nội dung, rồi đọc hết; nếu phần lớn nội dung đã đoán được hoặc đã nằm ở section trước thì báo LẶP Ý (`RECOGNITION_REDUNDANCY`) (trừ khi đó là mỏ neo hợp lệ theo quy tắc ở Node 4); (c) có câu khẳng định tổng quát (mọi người, luôn luôn, không bao giờ, ai cũng, chắc chắn) ở beat có ít hơn 2 `anchor` thì báo NÓI QUÁ (`OVER_GENERALIZATION`); (d) đoạn nào có thể đặt nguyên xi vào bất kỳ cuốn sách nào cùng chủ đề thì báo CHUNG CHUNG (`SELF_HELP_VOICE`). Mỗi lỗi ghi: tên section, loại lỗi, trích đúng câu hoặc đoạn bị báo (dưới 20 từ). Có lỗi thì verdict là REVISE kèm danh sách đó; cách sửa là cắt, nén hoặc viết lại theo chi tiết cụ thể của `anchor`, theo nguyên tắc sửa tối thiểu.
  - **LƯỢT 2 — Author Fidelity (Kiểm Toán Tính Trung Thành Với Tác Giả)**:
    - Sau khi Lượt 1 hoàn tất, Auditor **NẠP THÊM**: `foundation/manifesto.md`, `foundation/book_spine.md`, và `chapters/<id>/intent_ledger.md` (hoặc `foundation/decisions.md`).
    - Tiêu chuẩn kiểm tra 3 bệnh học trung thành:
      * `THESIS_DRIFT`: Bản thảo trôi dạt khỏi Core Governing Thesis của Manifesto.
      * `UNGROUNDED_HYPOTHESIS`: Khẳng định giả thuyết tâm lý/cơ chế như sự thật phổ quát khi chưa có mỏ neo kiểm chứng.
      * `RED_LINE_BREACH`: Vi phạm lằn ranh đạo đức hoặc điều tác giả cấm kỵ trong Intent Ledger.
- **Output Artifact**: `chapters/<chapter_id>/audit_verdict.md` chứa bảng **Diagnostic Rubric** tổng hợp cả 2 lượt, tuân thủ nguyên tắc: *"An audit finding must justify Why Reader Notices, not merely why a rule was violated"*.
- **Phán quyết & Rẽ nhánh**:
  - `PASS`: Đạt chuẩn cả Lượt 1 (Trải nghiệm đọc) và Lượt 2 (Tính trung thành) $\rightarrow$ Chuyển sang `MEMORY_UPDATE`.
  - `REVISE` (Sửa cục bộ section): Chỉ định file section kèm hành động đặc trị (`ALIGN_TO_MANIFESTO`, `QUALIFY_BOUNDS`, `DEDUP_CUT`, `INSERT_BRIDGE`). Giữ nguyên `card.md`. Context Reset $\rightarrow$ kích hoạt `SECTION_REVISION`.
  - `RESTRUCTURE` (Tái thiết kế đề cương): Lỗi kiến trúc vĩ mô (`THESIS_DRIFT` nghiêm trọng bắt nguồn từ Card). Context Reset $\rightarrow$ Quay lui về `BLUEPRINT` để lập lại `card.md` mới.
- **Hard Stop Protocol (`ROUTE-006`)**:
  - Nếu `revision_round >= 3` hoặc phát hiện `[PLATEAU]`: DỪNG TOÀN BỘ WORKFLOW, xuất báo cáo dừng khẩn cấp xin ý kiến tác giả.
- **Transition Path**:
  - `PASS` $\rightarrow$ `MEMORY_UPDATE`.
  - `REVISE` (vòng < 3) $\rightarrow$ `SECTION_REVISION`.
  - `RESTRUCTURE` $\rightarrow$ `BLUEPRINT`.
