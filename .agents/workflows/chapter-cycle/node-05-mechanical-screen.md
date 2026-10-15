# Node 5: MECHANICAL_SCREEN

- **Thực thi**: L0 Direct (Script stdlib — Zero LLM Intervention).
- **Lệnh thực thi**: `python scripts/repair_invariants.py --lint chapters/<chapter_id>/sections/`.
- **Human Gate**: `false`
- **Tiêu chuẩn kiểm định**: Tuân thủ nghiêm ngặt 5 tiêu chuẩn nhị phân Layer 1 tại [quality-engine.md](../../rules/quality-engine.md) (0 unresolved gap tokens, 0 raw diagram blocks, Unicode NFC & punctuation spacing, CONV-001 continuous prose, Translationese Ban).
- **Kiểm tra nguồn gốc (Provenance Gate)**: Sau khi bước kiểm tra cơ học đạt (mã thoát 0), chạy tiếp `python .agents/scripts/memory_cli.py check-provenance --chapter <chapter_id>`. Nếu mã thoát khác 0, coi như `lint_exit_code != 0` và chuyển sang SECTION_REVISION kèm danh sách các mục bị báo.
- **Transition Path**:
  - Exit code 0 (PASS) $\rightarrow$ `CHAPTER_ASSEMBLY`.
  - Exit code 3 (EPISTEMIC GAP DETECTED: `[GAP:]`, `[AUTHOR:]`, `[EVIDENCE-REQUEST:]`) $\rightarrow$ `GATE_3_BLUEPRINT` (Dừng yield xin dữ kiện tác giả; CẤM đẩy sang vòng sửa Section Revision để chống AI bịa đặt).
  - Exit code 1 (STYLE DEFECT && revision_round < 3) $\rightarrow$ `SECTION_REVISION` (Crafter phẫu thuật cắt tỉa sáo rỗng/độ dài).
  - Exit code 1 (STYLE DEFECT && revision_round >= 3) $\rightarrow$ `INFORMED_REVIEW` (Hết hạn ngạch sửa, chuyển lên Auditor thẩm định cưỡng bức / kích hoạt `[ESCALATE_HUMAN]`).
