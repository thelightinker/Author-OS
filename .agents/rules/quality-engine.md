---
name: quality-engine
version: 2.2.0
priority: P0
trigger: model_decision
description: "Hệ thống kiểm định chất lượng bản thảo cho Critic độc lập: L1 Sàng lọc cơ học, L2 Thẩm định chương kép (Dual-Lens Chapter Review với 15 bệnh học lâm sàng), liên kết L3 Đọc mù toàn sách (manuscript-cold-read.md) và cơ chế ngắt lặp."
---

# Rule: Quality Engine (Hệ Thống Kiểm Định Chất Lượng Bản Thảo)

> "Một cuốn sách vĩ đại không bao giờ được xuất bản dựa trên niềm tin mơ hồ. Nó phải vượt qua sàng lọc cơ học không khoan nhượng, phản biện bối cảnh hai mắt và trải nghiệm đọc thực tế của một độc giả độc lập."

---

## 📌 Phân loại Trigger
- **`stage_loaded`**: Được nạp có định hướng bởi `quality-auditor` và các workflow trong các giai đoạn kiểm định chất lượng ([chapter-cycle.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/workflows/chapter-cycle.md)).

---

## 1. Kiến Trúc Kiểm Định 3 Lớp (3-Layer Quality Architecture)

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: Mechanical Screen (Deterministic Stdlib Script)   │
│  - python scripts/repair_invariants.py --lint               │
│  - NFC Unicode, zero-width chars, punctuation, gap tokens   │
└──────────────────────────────┬──────────────────────────────┘
                               │ PASS
┌──────────────────────────────▼──────────────────────────────┐
│  Layer 2: Chapter Review (Chapter Mode: quality-auditor)    │
│  - Blind to author intent, NOT blind to manuscript context  │
│  - Dual-Lens: Lens A (Truth/Logic) + Lens B (Reader/Prose)  │
│  - Materiality Filter: Chỉ báo lỗi khi đủ material, else PASS│
│  - Output: audit_verdict.md (Diagnostic Rubric 15 bệnh học) │
└──────────────────────────────┬──────────────────────────────┘
                               │ PASS (Ghép toàn bộ chapters)
┌──────────────────────────────▼──────────────────────────────┐
│  Layer 3: Cold Read (Xem manuscript-cold-read.md)           │
│  - Absolute Blind Barrier: manuscript.md ONLY               │
│  - 10 High-Leverage Hypotheses (Transformation, Rent, Pacing)│
│  - Qualitative Risk Tiers: LOW / MEDIUM / HIGH RISK         │
│  - 4 Editorial Verdicts: Ship / Conditional / Revise / Kill │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Đặc Tả Chi Tiết Từng Lớp Kiểm Định

### 🔍 Layer 1 — Sàng Lọc Cơ Học (Mechanical Screen)
- **Công cụ thực thi**: `python scripts/repair_invariants.py --lint chapters/{ch_id}/sections/`.
- **Tiêu chí nhị phân (Binary Pass/Fail)**:
  1. *0 Unresolved Gap Tokens*: Tuyệt đối không còn `[PENDING:]`, `[QUERY:]`, `[VERIFY]`, `[AUTHOR]`, `[EVIDENCE-REQUEST:]`.
  2. *0 Raw Diagram Blocks*: Không chứa khối mã thô ` ```mermaid ` hoặc ` ```ascii ` trong văn xuôi bản thảo.
  3. *Unicode & Spacing*: Chuẩn hóa 100% Unicode NFC, 0 ký tự tàng hình (`\u200b`, `\ufeff`), không có khoảng trắng trước dấu câu.
  4. *CONV-001 Formatting Standard*: Mỗi khối nội dung là 1 đoạn văn liên tục, không ngắt dòng lắt nhắt hoặc lạm dụng bullet list thay văn xuôi.
  5. *Văn phong dịch thuật (Translationese Ban)*: Quét sạch các từ đệm sáo rỗng ("Điều đáng chú ý là", "Trong bối cảnh ngày nay", "Hơn nữa", "Rõ ràng rằng").

---

### 🔬 Layer 2 — Thẩm Định Chương Kép (Chapter Review - quality-auditor)
- **Chủ thể thực thi**: **`quality-auditor` trong Chapter Review Mode** (Critic độc lập — nguyên tắc $\text{Auditor} \ne \text{Author}$).
- **Hàng rào ngữ cảnh cân bằng ("Blind to author intent, NOT blind to manuscript context")**:
  - Auditor **ĐƯỢC NẠP**: `chapters/<id>/draft.md`, `chapters/<id>/card.md`, `summaries.md` (chứa Cognitive Payload Registry của các chương trước), `terms.md`, và `voice.md`.
  - Auditor **TUYỆT ĐỐI CẤM NẠP**: `manifesto.md`, `sources/`, `evidence_ledger.md`, hay nhật ký trò chuyện lúc chấp bút. Auditor không được biết tác giả *định nói gì*, mà chỉ đánh giá những gì thực sự có trên trang giấy.
- **Hai Trụ Cột Thẩm Định Độc Lập Song Song (Two Independent Parallel Pillars)**:
  - *Trụ cột 1: Liêm chính & Logic (Integrity & Logic Pillar)*:
    - Provenance check: Kiểm tra nguồn gốc và tính trung thực của dữ kiện, đối soát với `terms.md` và `summaries.md`, cấm bịa đặt trải nghiệm đời thực hoặc gán ghép giả tạo.
    - Khảo sát bằng chứng & Falsification: Luận điểm phải vững chắc, không ngụy biện logic (thiên kiến kẻ sống sót, đánh tráo tương quan thành nhân quả), xác lập điều kiện biên chính xác ("Đúng khi nào, Sai khi nào?"), hóa giải phản nghiệm hiển nhiên và khớp nối mạch dẫn `Leads-to`.
  - *Trụ cột 2: Trải nghiệm Độc giả Thực tế (Real Reader Lens Pillar)*:
    - Đóng vai độc giả tiếp nhận lần đầu: Đánh giá chức năng nhận thức của từng đoạn văn; chỉ ra những đoạn diễn giải thừa thãi điều độc giả đã hiển nhiên biết.
    - Độ cô đọng & Mật độ giá trị: Cắt bỏ các đoạn dẫn dắt dài dòng (Verbosity), loại bỏ lặp ý liên section (Semantic Repetition / Recognition Redundancy).
    - Điểm tựa chạm đất: Đoạn văn có cơ chế vận hành cụ thể, giác quan hiện trường và tình huống đời thực hay chỉ toàn khái niệm trừu tượng bay bổng.
    - Bản sắc giọng văn chân thực: Đối chiếu `voice.md`, phát hiện khẩu hiệu self-help sáo rỗng, câu chữ máy móc AI và nhịp điệu đều chằn chặn thiếu nhịp thở.
- **Hệ Thống Biên Tập 5 Tầng (5-Tier Editorial Hierarchy — Thứ Tự Ưu Tiên Từ Sâu Đến Nông)**:
  1. *Tầng 1: Tư Duy & Bằng Chứng*: Luận điểm có giá trị mới hay chỉ đổi tên nhận xét hiển nhiên? Cấm giải thích cơ chế khoa học/thần kinh học chưa được chứng minh (`UNGROUNDED_MECHANISM`).
  2. *Tầng 2: Cấu Trúc Lập Luận*: Xác lập điều kiện biên (đúng khi nào, sai khi nào, ngoại lệ chiến lược). Nếu 1 ý kéo dài qua nhiều đoạn: phát triển lập luận hoặc dừng viết, không chỉ gọt từ.
  3. *Tầng 3: Trải Nghiệm Độc Giả*: Đoạn sau phải mở rộng hiểu biết của đoạn trước. Hình ảnh và ví dụ phải có chức năng giải thích cơ chế, không trang trí văn vẻ.
  4. *Tầng 4: Câu Chữ & Nhịp Điệu*: Động từ chính xác, câu chủ động. Giữ từ rào đón nếu thể hiện sự bất định thực tế của dữ liệu. Thử phương án XÓA trước khi viết lại (The Quickest Fix).
  5. *Tầng 5: Đóng Đoạn Tự Nhiên*: Xong việc thì dừng (Stop when done). Không tóm tắt lặp lại; chỉ tổng hợp nếu mở ra hệ quả mới hoặc làm nhịp chuyển tiếp.
- **Bộ lọc nghiêm trọng (Materiality Threshold — Quyền Không Bắt Lỗi)**:
  - Auditor chỉ được ghi nhận lỗi khi vấn đề đủ nghiêm trọng (material) làm thay đổi trải nghiệm đọc, làm giảm niềm tin, gây đứt mạch hiểu hoặc làm suy giảm giá trị cuốn sách.
  - Phân tầng rủi ro định tính: đánh giá các phát hiện theo mức độ `LOW / MEDIUM / HIGH RISK`. Nếu một đoạn văn chỉ là "có thể viết hay hơn chút xíu" mà không gây cản trở trải nghiệm đọc $\rightarrow$ **BẮT BUỘC ĐÁNH `PASS`**.
  - **Chẩn đoán phẫu thuật chi tiết (Surgical Diagnostic Requirement)**: Khi đưa ra phán quyết `REVISE`, Auditor phải chỉ rõ vị trí đoạn văn yếu, lý do cụ thể theo góc nhìn độc giả (*Why Reader Notices*), và chỉ định hành động sửa đổi phẫu thuật tương ứng để Node 6 (`SECTION_REVISION`) can thiệp đúng điểm mà không làm biến dạng các phần đang hoạt động tốt.
  - **Quan sát ma sát hình thức (Formatting Friction)**: Nếu gặp ma sát trình bày (dấu câu giật cục, tiêu đề quá dày, lạm dụng bold, prose bị chatify thành list) làm đứt mạch đọc, Auditor ghi nhận trực tiếp vào nhận xét biên tập để Crafter tra cứu `manuscript-formatting` xử lý.
  - **Ranh giới bất biến (Anti-Self-Repair)**: `quality-auditor` chỉ chẩn đoán và chỉ định mã hành động, tuyệt đối CẤM tự ý viết lại câu chữ bản thảo.
- **Đầu ra bắt buộc**: `chapters/<chapter_id>/audit_verdict.md` chứa bảng **Diagnostic Rubric** tuân thủ nguyên tắc: *"An audit finding must justify Why Reader Notices, not merely why a rule was violated"*. Mọi phát hiện phải chỉ rõ trải nghiệm độc giả bị nghẽn (Why Reader Notices) và hành động đặc trị tương ứng.

#### 🔬 Bộ Tiêu Chuẩn 15 Bệnh Học Lâm Sàng (15 Clinical Pathologies Rubric across 3 Lenses):

##### 🔭 Lens A: Truth & Macro Logic (Chân Lý & Mạch Lập Luận Vĩ Mô)
1. `THESIS_EXPOSITION`: Mở đoạn giải thích cơ chế trừu tượng quá sớm thay vì kéo người đọc qua một trải nghiệm nhận thức đời sống. (Action: `EXPERIENCE_REWRITE`: Kéo mở đoạn về tình huống hiện trường cụ thể hoặc câu hỏi gợi mở).
2. `PREMISE_LEAP`: Nhảy cóc tiền đề lập luận ($A \rightarrow C$ thiếu $B$), khiến người đọc hụt chân không hiểu vì sao có kết luận. (Action: `INSERT_BRIDGE`: Thêm 1–2 câu làm rõ nỗ lực cơ cấu hoặc tiền đề trung gian).
3. `LOGICAL_NON_SEQUITUR`: Kết luận rút ra không bắt nguồn hợp lý từ tiền đề và bằng chứng đã nêu. (Action: `INSERT_BRIDGE` / `REASONING_REPAIR`: Viết lại logic suy luận nối kết chặt chẽ với dữ kiện).
4. `OVER_GENERALIZATION`: Khái quát hóa quá mức, quy chụp phổ quát cho mọi trường hợp mà thiếu điều kiện biên. (Action: `BOUNDARY_TRIM`: Bổ sung điều kiện biên đúng khi nào, sai khi nào).
5. `FALSIFICATION_BLINDSPOT`: Bỏ qua các trường hợp phản nghiệm hiển nhiên trong tâm trí độc giả khó tính. Bao gồm `THE_SKEPTIC_CHALLENGE` (Văn bản chỉ khẳng định một chiều, không giải quyết câu hỏi phản biện tự nhiên, thiếu điều kiện biên "Đúng khi nào, Sai khi nào?") và `UNGROUNDED_MECHANISM` (Tùy tiện gán ghép các cơ chế sinh học, thần kinh học, hóa học như "phần thưởng hóa học", "dopamine" khi chưa có nguồn dẫn hoặc nghiên cứu chứng minh). (Action: `GROUND_TO_REALITY`: Kéo về quan sát tâm lý thực tế, bổ sung điều kiện biên hoặc dẫn chứng kiểm chứng).

##### 🗣️ Lens B: Voice & Friction (Bản Sắc Giọng Văn & Lực Cản Câu Chữ)
6. `SELF_HELP_VOICE`: Văn phong mang màu sắc self-help phổ thông: mệnh đề chung chung, từ vựng sách vở, phán xét trừu tượng. (Action: `VOICE_ANCHOR_REWRITE`: Đối chiếu `voice.md`, thay bằng tiếng nói nội tâm và chi tiết chân thực của tác giả).
7. `MEGAPHONE_SLOGAN`: Khẩu hiệu đao to búa lớn từ Banned Clichés ("hãy nhớ rằng", "hành trình chuyển hóa"). (Action: `EAR_TEST_REWRITE`: Gọt bỏ khẩu hiệu, kéo về quan sát điềm tĩnh).
8. `TRANSLATIONESE`: Câu chữ dịch thuật sượng cứng ("được xem như là", "đóng vai trò như là"). (Action: `EAR_TEST_REWRITE`: Diễn đạt thẳng bằng tiếng Việt tự nhiên).
9. `AWKWARD_AI_PROSE`: Cụm từ máy móc AI (staging, not-X-but-Y, triads sáo rỗng, liên từ lặp). (Action: `EAR_TEST_REWRITE`: Đọc to thành tiếng, đảo về câu chủ động tự nhiên).
10. `CADENCE_MONOTONY`: Nhịp điệu phẳng lặng đơn điệu vô thức, độ dài các câu đều nhau chằn chặn. (Action: `EAR_TEST_REWRITE`: Xen kẽ câu ngắn 1–5 từ sau câu dài phân tích để tạo nhịp thở).

##### 🧩 Lens C: Reader Experience & Structure (Trải Nghiệm Độc Giả & Cấu Trúc Khối)
11. `BOUNDARY_BLEED`: Section lấn ranh giới: tóm tắt lại section trước hoặc trailer section sau. (Action: `BOUNDARY_TRIM`: Cắt tỉa phần lấn ranh giới, đóng mở section bằng nhịp tự nhiên của chính nó).
12. `FUNCTION_MISMATCH`: Nội dung đúng nhưng đặt sai vị trí kiến trúc của module (giải thích ở mở đầu, kết luận chương ở thân bài). (Action: `RELOCATE_CONTENT`: Điều chuyển khối nội dung về đúng vị trí module chức năng phù hợp).
13. `METAPHOR_INFLATION`: Ẩn dụ dày đặc, rải biến thể từ vựng làm nhãn dán, thay thế cho trải nghiệm thật. (Action: `GROUND_TO_REALITY`: Thay thế ẩn dụ hoa mỹ bằng miêu tả tình huống đời sống cụ thể).
14. `RECOGNITION_REDUNDANCY`: Lặp lại nhận thức mà các section trước đã giải quyết xong (lặp ý, Semantic Repetition). Bao gồm `REDUNDANT_PARAPHRASING` (1 ý tưởng duy nhất bị kéo dài thành nhiều đoạn văn bằng cách xếp chồng ẩn dụ hoặc diễn đạt lại mà lượng hiểu biết mới không tăng tương xứng) và `LABORIOUS_CRANKING` (Đoạn kết tóm tắt lặp lại nguyên văn những điều thân bài đã chứng minh; lưu ý: không gắn cờ nếu đoạn kết mở ra hệ quả mới hoặc làm nhịp chuyển tiếp). (Action: `DEDUP_CUT`: Bỏ đoạn dẫn nhập/tóm tắt thừa, kết thúc tự nhiên theo nguyên tắc Zinsser Exit; hoặc `COMPRESSION_PRUNING` kết hợp phát triển mô hình chiều sâu).
15. `CLIMAX_INFLATION`: Kịch tính hóa giả tạo, tạo cao trào gượng ép không tương xứng chất liệu. (Action: `GROUND_TO_REALITY`: Hạ giọng về mức chân thật, đúng với Confirmed Facts).

##### 🎯 Lens D: Author Fidelity & Epistemic Grounding (Tính Trung Thành Tác Giả & Neo Nhận Thức — Lượt 2)
16. `THESIS_DRIFT`: Bản thảo trôi dạt khỏi Core Governing Thesis hoặc mục tiêu chuyển hóa nhận thức trong `manifesto.md` và `book_spine.md` (ví dụ: biến bài toán tự do nội tâm thành bài toán quản lý năng lượng cơ học). (Action: `ALIGN_TO_MANIFESTO`: Viết lại logic định hướng theo đúng tuyên ngôn cốt lõi; hoặc `RESTRUCTURE` nếu lỗi bắt nguồn từ Card).
17. `UNGROUNDED_HYPOTHESIS`: Khẳng định một giả thuyết tâm lý, cơ chế xã hội hoặc suy luận chủ quan của AI như một chân lý hiển nhiên / quy luật phổ quát mà không có mỏ neo đời thực hoặc dữ liệu kiểm chứng. (Action: `QUALIFY_BOUNDS`: Giới hạn phạm vi, chuyển thể thành lăng kính gợi mở; hoặc `PROBE_AUTHOR`: Đưa câu hỏi vào intent ledger).
18. `RED_LINE_BREACH`: Bản thảo xuất hiện nội dung vi phạm lằn ranh đạo đức trong `manifesto.md` hoặc điều tác giả cấm kỵ trong `intent_ledger.md` (khẩu hiệu self-help, checklist cơ học, thuật ngữ thần kinh giả tạo). (Action: `DEDUP_CUT`: Cắt bỏ đoạn vi phạm; hoặc `EAR_TEST_REWRITE`).

#### 3 Phán Quyết Rẽ Nhánh (Verdicts):
1. `PASS`: Đạt chuẩn cả Lượt 1 (Trải nghiệm đọc) và Lượt 2 (Tính trung thành) $\rightarrow$ Chuyển sang `MEMORY_UPDATE`.
2. `REVISE`: Có lỗi cục bộ $\rightarrow$ Giữ nguyên `card.md`, chỉ định đích danh file section cần Crafter mở phẫu thuật kèm hành động đặc trị (`INSERT_BRIDGE`, `DEDUP_CUT`, `EAR_TEST_REWRITE`, `COMPRESSION_PRUNING`, `EXPERIENCE_REWRITE`, `VOICE_ANCHOR_REWRITE`, `BOUNDARY_TRIM`, `RELOCATE_CONTENT`, `GROUND_TO_REALITY`, `ALIGN_TO_MANIFESTO`, `QUALIFY_BOUNDS`). *Gợi ý phẫu thuật The Quickest Fix*: Khi gặp câu/đoạn rườm rà, Crafter ưu tiên thử nghiệm xóa bỏ hoàn toàn trước khi viết lại.
3. `RESTRUCTURE`: Gãy đổ luận đề vĩ mô hoặc `THESIS_DRIFT` nghiêm trọng bắt nguồn từ Card $\rightarrow$ Quay lui về `BLUEPRINT` để lập lại `card.md`.

---

### 🧊 Layer 3 — Đọc Mù Toàn Sách (Whole-Book Cold Read)
- **Tài liệu tham chiếu SSOT**: Toàn bộ quy chuẩn Layer 3 (Hàng rào đọc mù tuyệt đối `SEQ-006`, 10 Giả thuyết thẩm định đòn bẩy cao, Phân tầng rủi ro định tính `LOW / MEDIUM / HIGH RISK`, 4 Phán quyết ấn hành `Ship / Conditional / Major Revise / Kill`) và Quy trình Voice Audit Scan được quy định chuyên biệt tại **[manuscript-cold-read.md](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/manuscript-cold-read.md)**.
- **Kích hoạt tại**: `book-assembly.md` $\rightarrow$ `COLD_READ` & `VOICE_AUDIT`.

---

## 3. Cơ Chế Ngắt Vòng Lặp & Dừng Khẩn Cấp (`ROUTE-006`)
- **Bộ đếm sửa đổi trên đĩa**: Số vòng sửa đổi được lưu vết bền vững trong frontmatter của `chapters/<chapter_id>/card.md` (`revision_round: 1/3`).
- **Hạn ngạch**: Tối đa 3 vòng sửa đổi cho mỗi section/chương.
- **Dấu hiệu Plateau (`[PLATEAU]`)**: Khi các chỉnh sửa qua lại không làm tăng chất lượng hoặc sinh lỗi vòng quanh.
- **Quy tắc cứng**: Khi đạt 3 vòng (`revision_round >= 3`) hoặc phát hiện `[PLATEAU]` mà vẫn chưa đạt `PASS`, Agent **BẮT BUỘC DỪNG NGAY LẬP TỨC** và chuyển về Node 2 (`GATE_3_BLUEPRINT`) xin chỉ đạo trực tiếp từ tác giả (`[ESCALATE_HUMAN]`), báo cáo kèm các phương án lựa chọn:
  - Tác giả chấp thuận bản hiện tại (`Author Override` $\rightarrow$ ghi nhận `DISSENT`).
  - Tác giả cung cấp chỉ đạo bổ sung để phá vỡ thế bế tắc.
  - Tái cấu trúc lại mục tiêu của section/chương.

