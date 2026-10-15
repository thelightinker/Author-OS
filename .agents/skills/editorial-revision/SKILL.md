---
name: editorial-revision
description: "Biên tập phẫu thuật 3 lớp theo chuẩn thủ công cao cấp: Tiêu thụ trực tiếp Diagnostic Rubric từ quality-auditor, thực thi 5 hành động đặc trị (INSERT_BRIDGE, DEDUP_CUT, EAR_TEST_REWRITE, COMPRESSION_PRUNING, RESTRUCTURE), áp dụng kỷ luật bắt buộc WHAT TO KEEP và chỉ can thiệp phẫu thuật duy nhất trên section file bị báo lỗi."
when_to_use: "Khi thực hiện chu trình sửa chữa bản thảo (Node SECTION_REVISION) sau khi có kết quả kiểm tra linter hoặc phán quyết REVISE từ Layer 2 Informed Review."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 2.0.0
---

# Editorial Revision: Biên Tập Phẫu Thuật 3 Lớp & Kỷ Luật "What To Keep"

> "Viết là quá trình đổ cát vào xô; biên tập là quá trình gạn đục khơi trong để tìm thấy những hạt kim cương. Bác sĩ phẫu thuật giỏi không cắt nát cơ thể bệnh nhân, mà rạch đúng một đường dao chính xác để giải quyết đúng khối u."

---

## 1. Kỷ Luật Bất Biến "WHAT TO KEEP" (Trước Khi Cắt Gọt)

Trước khi chạm vào bất kỳ câu chữ nào trong một đoạn văn cần sửa:
- **Nguyên tắc**: Biên tập viên thường có xu hướng biến văn bản thành văn của chính mình, làm mất đi sự thô mộc, góc cạnh chân thật của tác giả.
- **Hành động bắt buộc**: Trích dẫn chính xác **1–2 câu văn đắt giá nhất** trong section mà bạn cam kết **GIỮ NGUYÊN 100%**. Mọi sự cắt gọt và tái cấu trúc xung quanh phải phục vụ cho việc tôn vinh 2 câu văn này tỏa sáng.
- **Kỷ Luật Tôn Trọng Bản Thảo Đã Khóa ("Đủ Tốt Là Tốt Nhất" — #B)**: Khi tác giả đã chấp thuận hoặc yêu cầu dừng sửa ("đoạn này ổn rồi, đừng sửa thêm"), Agent tôn trọng tuyệt đối. Không cố nâng cấp hay "làm hay hơn" những gì tác giả đã khóa, tránh nguy cơ over-processing làm mất đi giọng điệu tự nhiên.

---

## 2. Tiêu Thụ Diagnostic Rubric & 10 Hành Động Đặc Trị

Bác sĩ phẫu thuật (`chapter-crafter`) **CẤM sửa bài chung chung**. Bạn phải đọc trực tiếp cột `Targeted Action` trong Diagnostic Rubric của `audit_verdict.md` và thực thi chính xác 1 trong các hành động đặc trị sau:

1. **`INSERT_BRIDGE` (Thêm Nhịp Đệm Logic)**:
   - Dùng khi phát hiện lỗi `REASONING_GAP` (nhảy cóc $A \rightarrow C$ thiếu $B$).
   - Viết bổ sung 1–3 câu giải thích tiền đề trung gian còn thiếu. Tuyệt đối không xóa bỏ hay viết lại toàn bộ đoạn văn xung quanh.

2. **`DEDUP_CUT` (Cắt Bỏ Trùng Lặp & Nối Mạch)**:
   - Dùng khi phát hiện lỗi `SEMANTIC_REPETITION` (nhai lại insight mà không tạo giá trị gia tăng).
   - Cắt bỏ khối câu văn nhắc lại ý cũ; dùng kỹ thuật Refocus để nối thẳng mạch văn vào ca nghiên cứu thực tế hoặc chi tiết hiện trường.

3. **`EAR_TEST_REWRITE` (Viết Lại Theo Ear-Test Tự Nhiên & Conditional Humanizer Pass)**:
   - Dùng khi phát hiện lỗi `AWKWARD_AI_PROSE` hoặc `CADENCE_MONOTONY`.
   - **Kích hoạt Conditional Humanizer Pass**: Trong hành động này hoặc khi có chẩn đoán bệnh học AI tells rõ rệt trong `audit_verdict.md`, `chapter-crafter` nạp kỹ năng `humanizer` để khử các cấu trúc máy móc (not-X-but-Y, cấu trúc 3 vế cân đối gượng gạo, dramatic fragments, inflated claims).
   - **Nguyên tắc Conditional Guard**: Bước khử AI này là xử lý có điều kiện (conditional pass), TUYỆT ĐỐI KHÔNG biến thành trạm kiểm soát bắt buộc ở mọi lần revise. Nếu đoạn văn đã có giọng điệu tự nhiên, cấm chạy humanizer máy móc để chống nguy cơ over-processing làm phẳng nhịp văn.
   - Đọc to thành tiếng (Ear Test) để kiểm tra nhịp thở của câu:
     - Chuyển thể bị động thành chủ động.
     - Đa dạng hóa nhịp điệu hữu cơ: xen kẽ câu ngắn đanh thép với câu dài suy tưởng. CẤM ép buộc câu văn vào công thức số từ cứng nhắc.

4. **`COMPRESSION_PRUNING` (Cắt Tỉa Cô Đọng)**:
   - Dùng khi phát hiện lỗi `VERBOSITY` (nói nhiều hơn lượng ý truyền tải).
   - Áp dụng nguyên lý William Zinsser và bài test Compression Probe: Cắt bỏ các mệnh đề giải thích lại ("nói cách khác", "điều này có nghĩa là"), giữ lại hạt nhân luận điểm.

5. **`RESTRUCTURE` (Hồi Quy Đề Cương)**:
   - Khi phán quyết là `RESTRUCTURE`: Dừng ngay việc sửa chữ cục bộ, thực hiện Context Reset và quay lui về `BLUEPRINT` để tái thiết kế `card.md`.

6. **`EXPERIENCE_REWRITE` (Viết Lại Khơi Gợi Trải Nghiệm — #01)**:
   - Dùng khi phát hiện lỗi `THESIS_EXPOSITION` (giải thích thesis quá sớm và quá sạch thay vì dẫn dắt trải nghiệm).
   - Viết lại đoạn mở đầu bằng tình huống hiện trường cụ thể, chi tiết đời sống hoặc câu hỏi khơi gợi tò mò. Kéo câu văn từ thế đứng trên phân tích lý thuyết xuống trải nghiệm nhận thức.

7. **`VOICE_ANCHOR_REWRITE` (Neo Lại Bản Sắc Văn Phong — #02)**:
   - Dùng khi phát hiện lỗi `SELF_HELP_VOICE` (văn phong mang màu sắc self-help phổ thông).
   - Đối chiếu `voice.md` và `story_bank.md` (`Interview Content`), thay thế các mệnh đề chung chung hoặc từ vựng sách vở bằng tiếng nói nội tâm chân thực và tình huống đời thường.

8. **`BOUNDARY_TRIM` (Cắt Tỉa Lấn Ranh Giới — #03)**:
   - Dùng khi phát hiện lỗi `BOUNDARY_BLEED` (tóm tắt ý section trước hoặc kết bằng trailer cho section sau).
   - Cắt bỏ phần mở đầu tóm tắt thừa thãi; cắt tỉa câu kết nhảy cóc sang section sau, để section đóng lại bằng nhịp tự nhiên của chính luận điểm đó.

9. **`RELOCATE_CONTENT` (Điều Chuyển Đúng Vị Trí Kiến Trúc — #07)**:
   - Dùng khi phát hiện lỗi `FUNCTION_MISMATCH` (đúng nội dung nhưng sai vị trí module).
   - Cắt khối nội dung bị đặt sai vị trí (ví dụ: giải thích trong opening, kết luận chương trong section thân bài) và điều chuyển sang đúng module chức năng tương ứng.

10. **`GROUND_TO_REALITY` (Kéo Ẩn Dụ Về Mặt Đất — #06)**:
    - Dùng khi phát hiện lỗi `METAPHOR_INFLATION` (lạm dụng ẩn dụ dày đặc hoặc biến thể nhãn dán).
    - Lược bỏ các biến thể ẩn dụ rườm rà; thay thế bằng miêu tả trực diện tình huống đời sống cụ thể để người đọc cảm nhận được sự việc chân thực thay vì nhớ nhãn dán văn hoa.

11. **`ALIGN_TO_MANIFESTO` (Tái Căn Chỉnh Theo Luận Đề Gốc)**:
    - Dùng khi phát hiện lỗi `THESIS_DRIFT` (trôi dạt khỏi Core Governing Thesis của Manifesto).
    - Cắt bỏ các phân nhánh lạc đề, viết lại logic định hướng bám sát tôn chỉ cốt lõi trong `manifesto.md` và các quyết định `[CONFIRMED]` trong `intent_ledger.md`.

12. **`QUALIFY_BOUNDS` (Giới Hạn Phạm Vi & Hạ Giọng Nhận Thức)**:
    - Dùng khi phát hiện lỗi `UNGROUNDED_HYPOTHESIS` (khẳng định giả thuyết tâm lý/cơ chế như sự thật phổ quát).
    - Bổ sung điều kiện biên ("chỉ đúng trong bối cảnh...", "đây là một hướng tiếp cận cần kiểm chứng"), hạ giọng khẳng định tuyệt đối về dạng giả thuyết gợi mở hoặc gắn mỏ neo đời thực.

---

## 3. Quy Tắc Biên Tập Phẫu Thuật (Surgical Scope Rule)

- **CHỈ SỬA ĐÚNG FILE ĐƯỢC CHỈ ĐỊNH**: Nếu `audit_verdict.md` chỉ ra lỗi ở Section 2, bạn **CHỈ ĐƯỢC PHÉP** mở và sửa `02_sec2.md`.
- Tuyệt đối không mở các file `00_open.md` hay `01_sec1.md` để "sửa tiện tay". Điều này giúp bảo toàn ngữ cảnh và không làm phát sinh lỗi mới ở những phần đã ổn định.
- Chạy `python scripts/repair_invariants.py chapters/{id}/sections/{target_file}` sau khi sửa để làm sạch khoảng trắng cơ học.

---

## 4. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (`audit_verdict.md` chỉ trích `01_sec1.md`):
```markdown
| Vị trí | Pathology | Why Reader Notices | Targeted Action |
| `01_sec1.md` (P.3) | REASONING_GAP | Người đọc bị hụt chân vì tác giả nhảy từ áp lực doanh số sang quyết định sa thải mà thiếu bước đàm phán nợ. | INSERT_BRIDGE |
```

### Xử lý Phẫu Thuật:
- **WHAT TO KEEP**: *"Khi kỳ hạn ngân hàng gõ cửa vào ngày mùng năm, bạn buộc phải cúi đầu trước những điều mình khinh bỉ."*
- **Hành động `INSERT_BRIDGE`**: Bổ sung 2 câu làm rõ nỗ lực tái cơ cấu nợ với ngân hàng đã thất bại vào chiều hôm trước, tạo cầu nối hợp lý dẫn tới quyết định sa thải.
- **Ear-Test**: Đọc to thành tiếng để bảo đảm giọng văn trầm tĩnh, tự nhiên.

---

## 5. Tiêu Chuẩn Nghiệm Thu

- [ ] Cung cấp danh mục `WHAT TO KEEP` rõ ràng trước khi sửa.
- [ ] Khắc phục 100% mã hành động chỉ định trong `audit_verdict.md` (`INSERT_BRIDGE`, `DEDUP_CUT`, `EAR_TEST_REWRITE`, `COMPRESSION_PRUNING`).
- [ ] Chỉ sửa duy nhất file section mục tiêu.
- [ ] Vượt qua linter cơ học `repair_invariants.py --lint`.

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `falsification-steelmanning` | Khung phản biện đối nghịch chuyên sâu khi gặp luận điểm phức tạp cần đào sâu điều kiện biên ở Pass 1. |
| `humanizer` | Tham chiếu các mẫu nhận diện câu văn AI để gọt sạch dấu vết máy móc ở Pass 2. |
| `chapter-drafting` | Đối chiếu beat gốc và hạn ngạch từ của section trước khi phẫu thuật văn bản. |
