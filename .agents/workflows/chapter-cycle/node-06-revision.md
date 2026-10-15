# Node 6: SECTION_REVISION

- **Vai trò thực thi**: `chapter-crafter` nạp skill `editorial-revision`.
- **Input**: Lỗi từ linter hoặc `audit_verdict.md`, `chapters/<chapter_id>/intent_ledger.md`.
- **Output Artifact**: Cập nhật trực tiếp trên section file bị báo lỗi.
- **Quy tắc phẫu thuật**:
  - Chỉ mở và sửa DUY NHẤT file section bị báo lỗi (ví dụ: `01_sec1.md`).
  - Đối chiếu `intent_ledger.md`: Tuân thủ nghiêm ngặt mọi quyết định `[CONFIRMED]` và lằn ranh cấm. Với các cảnh báo `THESIS_DRIFT` hoặc `UNGROUNDED_HYPOTHESIS`, thực thi hành động đặc trị `ALIGN_TO_MANIFESTO` hoặc `QUALIFY_BOUNDS` để đưa văn bản về đúng trục tôn chỉ và thu hẹp phạm vi nhận thức.
  - Áp dụng kỷ luật `WHAT TO KEEP`: Trích dẫn 1–2 câu văn đắt giá nhất giữ nguyên 100% trước khi cắt tỉa.
  - Thực thi 3 Pass: Pass 1 (Tự phản biện luận điểm), Pass 2 (Zinsser Clutter Cut), Pass 3 (Tiết tấu Bằng - Trắc) (chi tiết trong `editorial-revision/SKILL.md`).
  - **Conditional Humanizer Pass**: Nếu `audit_verdict.md` chỉ định hành động `EAR_TEST_REWRITE` hoặc lỗi `AWKWARD_AI_PROSE` / `CADENCE_MONOTONY`, Crafter nạp `humanizer` để khử các cấu trúc máy móc. Tuyệt đối không chạy máy móc trên mọi section để chống over-processing.
  - **Hạn ngạch & Biến đếm Tất định**: Biến đếm `revision_round` được tăng tự động bằng lệnh máy móc tất định: `python scripts/repair_invariants.py --step-revision chapters/<chapter_id>/card.md` (hạn ngạch tối đa 3 vòng; Zero LLM Intervention). Nếu chạm trần 3 vòng, script trả về exit code 2 và kích hoạt ngắt mạch chuyển tiếp.
  - **Nguyên tắc sửa tối thiểu**: Chỉ sửa câu hoặc đoạn bị báo lỗi. Không viết lại cả section khi nguyên nhân chỉ là lỗi cục bộ. Giữ nguyên các câu không bị báo.
  - **Xử lý chi tiết chưa có nguồn**: Với danh sách chi tiết chưa có nguồn từ bước kiểm tra nguồn gốc: mỗi mục, bỏ chi tiết đó hoặc viết lại không dùng số hay trích dẫn cụ thể (ví dụ "khoảng một năm" thành "một thời gian"; câu thoại thành lời kể gián tiếp). Không tự thêm số liệu hay câu thoại mới. Không hỏi tác giả trong lúc sửa. Cuối chương, nói với tác giả một câu bằng lời thường: đã bỏ hoặc làm mềm những chi tiết nào vì chưa thấy trong ghi chép, và mời bổ sung nguồn nếu muốn giữ lại.
- **Transition Path**: `SECTION_REVISION` $\rightarrow$ `MECHANICAL_SCREEN`.
