---
name: chapter-drafting
description: "Chấp bút văn xuôi module hóa từng section độc lập: Chuyển hóa các beat từ Chapter Card thành các file văn xuôi hoàn chỉnh trong chapters/<id>/sections/*.md, tích hợp sống động các chi tiết từ story_bank.md, tuân thủ nghiêm ngặt chuẩn định dạng CONV-001 (khối văn bản liên tục), nhúng semantic visual placeholders và thực hiện yield khi gặp khoảng trống chứng cứ [EVIDENCE-REQUEST]."
when_to_use: "Khi tiến hành chấp bút văn xuôi cho một chương đã có bản vẽ card.md được duyệt [DRAFT-READY] trong quy trình Chapter Cycle (Node SECTION_DRAFTING)."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Chapter Drafting: Chấp Bút Module Section & Thổi Hồn Vào Bản Thảo

> "Đừng cố viết một chương sách vĩ đại trong một lần gõ phím. Hãy viết một đoạn văn 1,000 từ hoàn hảo đến mức độc giả không thể rời mắt, rồi lặp lại điều đó cho căn phòng tiếp theo."

---

## 1. Giao Thức Chấp Bút Module Section (P0 Invariant)

1. **Độc lập tuyệt đối giữa các Section & Tiêu chuẩn Heading H2**:
   - Mỗi section là một file riêng biệt: `00_open.md`, `01_sec1.md`, `02_sec2.md`, `04_close.md`.
   - **Quy chuẩn Heading H2**: Mỗi file section mở đầu bằng một tiêu đề H2 (`## [Tiêu đề Section]`) làm kim chỉ nam nhận thức (trừ trường hợp tác giả chủ động yêu cầu ẩn tiêu đề để tạo nhịp tự sự liền mạch). Dưới H2 có thể phân rã các nhánh nhỏ H3 nếu cần.
   - **Cấu trúc phân cấp 3–4 tầng**: Hỗ trợ linh hoạt 3 tầng (`Part` $\rightarrow$ `Chapter` $\rightarrow$ `Section`) hoặc 4 tầng (`Part` $\rightarrow$ `Chapter` $\rightarrow$ `Section` $\rightarrow$ `Subsection/Beat`).
   - **CẤM** viết thẳng vào `draft.md`. File `draft.md` chỉ được sinh ra bằng lệnh lắp ráp `assemble_chapter.py`.
   - **Hạn ngạch trần từ (`budget_words_max`)**: Chiều dài section tuân thủ trần từ `budget_words_max` của Card v3 (thường 800–1,500 từ tùy hình thái chương). Tuyệt đối **CẤM** ép sàn từ tối thiểu hoặc viết tiếp cho đủ số từ; dứt điểm ngay khi giải quyết trọn vẹn beat và chuyển hóa nhận thức.

2. **Chế Độ Tiếp Nhận Bản Nháp Tác Giả (Author Draft Intake — Cửa A)**:
   - Khi tác giả cung cấp bản nháp tự viết, thao tác chính của Crafter là **mài giũa (sculpting)** thay vì viết mới từ đầu.
   - Sắp xếp lại bố cục cho mạch lạc, làm nổi bật quan hệ nhân quả, cắt bỏ câu từ thừa thãi; **bảo toàn ý tưởng, luận điểm, trải nghiệm và đặc trưng giọng tác giả**. Mọi sửa đổi lớn về ý nghĩa bắt buộc phải được nhận diện và xin ý kiến, cấm tự ý viết đè.

3. **Thiết Kế Trải Nghiệm Đọc Có Chủ Đích (Anti-Formulaic Reader Journey)**:
   - **Đa dạng hóa cách mở đầu theo chức năng**: Không áp đặt một công thức cố định cho mọi section. Tùy theo chức năng của section trong hành trình đọc mà chọn cách triển khai tự nhiên:
     * *Mở đầu bằng tình huống / xung đột*: Cho section tự sự hoặc mở đầu chương.
     * *Mở đầu bằng câu hỏi trực diện hoặc phản ví dụ*: Cho section bẻ gãy trực giác.
     * *Mở đầu bằng cơ chế nhân quả hoặc dữ kiện*: Cho section phân tích chuyên sâu.
   - **Không ép khuôn Aha Moment**: Mỗi section đóng góp giá trị bằng sự sáng rõ, bằng chứng hoặc cảm xúc; không ép buộc mọi section phải có một cú nổ aha moment cơ học.
   - **Cơ chế Destination Pivot**: `intended_destination` là la bàn định hướng mềm. Nếu trong quá trình viết phát hiện lập luận hoặc bằng chứng sâu sắc hơn làm thay đổi kết luận ban đầu, Agent ghi nhận đề xuất cập nhật đích đến thay vì gò ép bài viết.

4. **Nạp Kỹ Năng Linh Hoạt (1–3 Skills: Co-Pilot Humanizer)**:
   - Trong quá trình chấp bút, Agent được toàn quyền nạp kết hợp 1–3 skills:
     - `chapter-drafting` (chấp bút chính từ beats của Card).
     - `humanizer` (chạy song hành để triệt tiêu ngay các cấu trúc máy móc, văn mẫu AI, staging, triads, not-X-but-Y).
     - `story-enrichment` (khi cần tích hợp chi tiết hiện trường từ `story_bank.md`).
     - `editorial-revision` (khi mài giũa bản nháp của tác giả theo Cửa A).
   - Văn bản sinh ra phải tự nhiên, mang nhịp thở của tác giả ngay từ bản nháp đầu tiên, không bắt buộc phải đợi đến vòng biên tập mới gọi `humanizer`.

5. **Tiêu Chuẩn Định Dạng CONV-001 (Continuous Paragraph)**:
   - Viết thành các khối văn xuôi tự sự liên tục, tự nhiên, nhịp nhàng.
   - **CẤM** lạm dụng gạch đầu dòng (bullet lists) để thay thế văn xuôi. Bullet lists chỉ được dùng khi liệt kê danh mục kiểm tra kỹ thuật hoặc bước thực hành cụ thể.
   - Không ngắt dòng vụn vặt kiểu thơ tự do.

4. **Tích Hợp Chi Tiết Từ `story_bank.md` & Ràng Buộc Liêm Chính Tự Sự Toàn Diện (P0 Invariant)**:
   - Khi beat trong `card.md` có trỏ đến mã thẻ `S-XXX` hoặc yêu cầu tái hiện câu chuyện đời thực/ký ức tác giả:
     - **BẮT BUỘC (MUST)** nạp và tuân thủ [`.agents/rules/story-integrity.md`](file:///d:/Downloads/AI%20Agent%20Kits/Agent%20Kits/Writing%20Agent/.agents/rules/story-integrity.md) và `COLLAB-011` / `COLLAB-012`.
     - **Bảo Vệ Liêm Chính 8 Chiều (Anti-Invention Coverage)**:
       1. *Dialogue*: Chỉ đưa lời thoại trong ngoặc kép khi có trích dẫn nguyên văn trong `Interview Content` hoặc tài liệu nguồn. CẤM tự sáng tác câu thoại cho tác giả hoặc nhân vật thật; dùng trần thuật gián tiếp hoặc giữ UNKNOWN.
       2. *Emotions*: Cảm xúc phải do tác giả tự xác nhận trong `Author Interpretation`. CẤM suy đoán hoặc kịch hóa cảm xúc nội tâm cực đoan.
       3. *Motivations*: Động cơ hành động phải dựa trên dữ kiện thật; CẤM tự ý gán ghép động cơ tâm lý hoặc ý đồ cho con người thật.
       4. *Sensory Details*: Chỉ sử dụng chi tiết giác quan (âm thanh, mùi vị, ánh sáng, thời tiết) đã được xác nhận trong `Confirmed Facts`. CẤM tự thêm thời tiết (mưa phùn, rét buốt), đồ vật (quạt cây cọt kẹt), hoặc âm thanh giả tạo.
       5. *Background & Settings*: CẤM tự bịa số lượng nhân sự, tầng nhà, địa danh, tên công ty hoặc thông số tài chính khi tác giả chưa kể.
       6. *Causal Explanation*: CẤM tự ý phát minh quan hệ nhân quả võ đoán ("vì X nên Y") nếu chưa có kiểm chứng.
       7. *Interview Details*: Trong Tier B (chuyện người khác), CẤM tự bịa cử chỉ điện ảnh, nét mặt, ánh mắt của người được phỏng vấn.
       8. *Anti-Escalation*: CẤM thăng cấp suy đoán (`Agent Inferences`) hoặc giả thuyết thành sự thật lịch sử (`Confirmed Facts`).
     - Nếu phát hiện thiếu dữ liệu trọng yếu làm sai lệch cảnh: **BẮT BUỘC (MUST)** kích hoạt phản xạ dừng viết để phỏng vấn (`YIELD TO INTERVIEW`), tuyệt đối không tự bịa thêm sự kiện.

5. **Semantic Visual Placeholders**:
   - Khi cần minh họa một mô hình tư duy, không vẽ mã ASCII hay Mermaid thô vào văn bản.
   - Hãy chèn gợi ý ngữ nghĩa: `[VISUAL-SUGGESTION: Biểu đồ trục tọa độ thể hiện 4 bình nhiên liệu, với bình Cảm xúc đang rò rỉ ở đáy]`.

6. **Xử Lý Khoảng Trống Chứng Cứ (Evidence Gap Protocol)**:
   - Nếu đang viết mà phát hiện một số liệu hoặc khẳng định chưa được chứng thực trong `evidence_ledger.md`:
     - Chèn ngay: `[EVIDENCE-REQUEST: req_01]` vào vị trí câu.
     - Ghi tóm tắt vào `chapters/<id>/evidence_request.md`.
     - Ngừng viết section đó (yield) để Orchestrator bàn giao cho Architect xử lý. Không được tự ý bịa số liệu để viết tiếp.
   - **Hồi phục sau tra cứu (Evidence Gap Recovery)**: Khi nhận lại quyền chấp bút sau khi `evidence_request.md` đã có phản hồi:
     - Áp dụng phương án xử lý tương ứng (`Resolve` trích dẫn / `Reframe` đổi góc nhìn / `Soften` làm mềm / `Cut` lược bỏ).
     - **BẮT BUỘC xóa token `[EVIDENCE-REQUEST: req_XX]`** khỏi văn bản để vượt qua linter cơ học Layer 1 (`repair_invariants.py --lint`).

7. **Ràng Buộc Chống Nhắc Lại Vòng Lặp & Lặp Ý (Anti-Restatement Constraint & Recognition Redundancy Guard)**:
   - Nghiêm cấm mô hình diễn giải vòng lặp (Recognition Redundancy): *Nêu mệnh đề A $\rightarrow$ giải thích A $\rightarrow$ nhắc lại A $\rightarrow$ "nói cách khác" A*. Tuyệt đối không lặp lại nhận thức (lặp ý) mà các section trước đã giải quyết.
   - Khẳng định 1 lần thật sắc bén, neo chắc bằng chi tiết hiện trường hoặc dẫn chứng từ Gold Passages trong `voice.md`, rồi tiến thẳng sang luận cứ tiếp theo.

8. **Thăm Dò Nén Đoạn Văn (The Compression Probe — Heuristic)**:
   - Tự chất vấn trong khi viết: *"Có thể cắt giảm đáng kể đoạn này mà không làm mất ý nghĩa, bằng chứng, điểm chạm cảm xúc (tension) hoặc sự tiến triển của lập luận không?"*. Nếu có, hãy cô đọng ngay lập tức.

9. **Đa Dạng Hóa Nhịp Điệu (Cadence Diversity — Anti-Monotony Warning)**:
   - Cảnh báo chống nhịp điệu phẳng lặng đơn điệu vô thức (Monotony Drone).
   - Cho phép các chuỗi câu ngắn dồn dập để tạo kịch tính hoặc các câu phức dài suy tưởng để lắng đọng nhận thức tùy theo ý đồ nghệ thuật. Tuyệt đối cấm cơ học hóa câu văn bằng các công thức số từ cứng nhắc.

10. **Kỷ Luật Định Dạng Tối Thiểu (Minimal Formatting Hygiene)**:
   - **Tránh chat-like line breaking**: Giữ nhịp thở tự sự liên tục của đoạn văn (3–6 câu), không ngắt dòng lắt nhắt từng câu một kiểu thơ tự do hay mạng xã hội.
   - **Tránh nhấn mạnh Markdown vô cớ**: Không bôi đậm `**bold**` rải rác trong thân văn xuôi tự sự; dồn sức nặng nhận thức vào chính câu chữ.
   - **Bảo vệ chuẩn mực CONV-001**: Tuyệt đối không biến các luận điểm văn xuôi thành danh sách gạch đầu dòng (bullet lists) khi không có lý do cấu trúc.
   - **Tuân thủ phân cấp Markdown**: Mở đầu mỗi section bằng đúng 1 tiêu đề H2 (`## [Tiêu đề Section]`) làm kim chỉ nam.

11. **Experience-First Writing (Chống Giải Thích Thesis Sớm — #01)**:
   - **Default Principle (Nguyên tắc mặc định)**:
     - Nhiệm vụ trọng tâm của section là **tạo trải nghiệm nhận thức** để người đọc tự đi qua và tự nhận ra chân lý, không phải trình bày luận đề (thesis) sớm và sạch sẽ như một bài thuyết trình.
     - Ưu tiên mở đầu bằng tình huống đời sống cụ thể, một chi tiết hiện trường sắc nét, hoặc câu hỏi khơi gợi tò mò để kéo người đọc vào vấn đề trước khi dẫn tới nhận thức.
     - Tránh mở đầu bằng mệnh đề phổ quát mang tính giải thích cơ chế trừu tượng ("Nguyên nhân sâu xa là...", "Hậu quả lớn nhất là...") hoặc tuyên bố chân lý thay cho người đọc.
     - Tránh biến đoạn mở đầu hoặc lời giới thiệu thành mục lục trá hình (liệt kê danh sách các chương/phần tiếp theo).
   - **Exception / Context-Specific (Ngoại lệ theo chức năng module)**:
     - Với các module mang tính tổng quan định hướng hoặc tóm lược kỹ thuật (ví dụ: Executive Summary, System Architecture Overview) được blueprint chỉ định rõ ràng, việc tóm lược cấu trúc và giải thích khung khái niệm trực tiếp là hoàn toàn hợp lệ.
   - **Heuristic tự kiểm trước khi nộp section**:
     - Tự hỏi: *"Đoạn mở đầu này đang cố giải thích cho người đọc hiểu cơ chế, hay đang kéo họ đi qua một lát cắt trải nghiệm đời sống?"* Nếu đang đứng trên phân tích: kéo câu văn về hiện trường cụ thể.

12. **Anti-Self-Help Voice Guard (Chống Giọng Self-Help Mặc Định — #02)**:
   - **Default Principle**: Agent là người chắp bút đồng hành với tác giả cụ thể (theo `voice.md` và `story_bank.md`), không phải biên soạn viên sách self-help phổ thông.
   - **Nhận diện biểu hiện lệch giọng**:
     - Mở đoạn bằng câu khẳng định chung chung ("Trong thời đại ngày nay...", "Nhiều người trong chúng ta thường lầm tưởng...").
     - Lập luận chuỗi công thức sách vở ("A dẫn đến B dẫn đến C").
     - Đưa ra lời khuyên hoặc kết luận mang tính phán xét trừu tượng thay vì để chi tiết tự cất tiếng.
   - **Phương pháp nắn chỉnh**:
     - Thay thế các khái niệm self-help trừu tượng bằng tiếng nói nội tâm quen thuộc hoặc tình huống đời thực cụ thể của con người bình thường.
     - Ưu tiên chất liệu từ phỏng vấn tác giả (`Interview Content` trong `story_bank.md`).
   - **Heuristic tự kiểm**:
     - *"Nếu câu văn này có thể đặt vào bất kỳ cuốn sách self-help nào khác trên thị trường mà không cần sửa từ nào, thì nó chưa phải là giọng của tác giả này."*

13. **Section Boundary Discipline (Kỷ Luật Ranh Giới Module — #03)**:
   - **Default Principle**:
     - *Đầu section*: Khởi đầu trực tiếp vào vấn đề của riêng section đó. Tránh mở đầu bằng một đoạn tóm tắt recap lại những gì section trước vừa thảo luận.
     - *Cuối section*: Đóng lại bằng nhịp tự nhiên của chính luận điểm đó. Tránh viết những câu kết mang tính quảng cáo (trailer) hoặc mở sớm nhận thức thuộc về section tiếp theo.
     - *Tính độc lập của module*: Mỗi file section đảm nhiệm đúng vai trò kiến trúc của nó. Không tự ý gộp chức năng tổng kết chương vào file section thân bài.
   - **Exception / Context-Specific**:
     - Với các tác phẩm phức hợp nhiều tuyến lập luận dài, việc điểm xuyết một nhịp đệm ngắn (1 câu) để neo mạch logic là cho phép nếu không làm nhòe trọng tâm mới.
   - **Heuristic tự kiểm**:
     - *"Câu mở đầu này có đang nói lại ý của section trước không?"*
     - *"Câu kết thúc này có đang thuộc về nhiệm vụ của section sau hay của phần kết chương không?"*

14. **Reader Spectrum Check (Mở Rộng Phổ Độc Giả — #04 & A)**:
   - **Default Principle**:
     - Phân biệt rõ ràng giữa **cơ chế tâm lý/nhận thức cốt lõi** và **một kịch bản cụ thể** dùng để minh họa cơ chế đó.
     - Tránh mặc định quy chụp độc giả vào một nhóm đối tượng duy nhất (ví dụ: chỉ có dân văn phòng bận rộn, người đi làm có sếp và deadline).
     - Khi minh họa một trạng thái tâm lý phổ quát (như kiệt sức, mất phương hướng, trì hoãn), cần bao quát được các biểu hiện đa chiều: cả người quay cuồng trong công việc lẫn người không có việc gì gấp nhưng vẫn rã rời; cả người đã có mục tiêu rõ ràng lẫn người hoang mang chưa biết mình muốn gì.
     - **Nguyên tắc phân định Khái niệm vs Công cụ (#A)**: Khái niệm định hướng xuyên suốt cuốn sách phải được giữ ở tầm vóc bao quát; tuyệt đối không đồng nhất khái niệm nền tảng với một công cụ thực thi cục bộ.
   - **Heuristic tự kiểm**:
     - *"Tình huống minh họa này có đang vô tình loại trừ những độc giả không làm việc văn phòng hoặc có hoàn cảnh sống khác không?"*

15. **Metaphor in Service of Experience (Ẩn Dụ Phục Vụ Trải Nghiệm — #06)**:
   - **Bản chất vấn đề**: Ẩn dụ không có lỗi; vấn đề là việc lạm dụng ẩn dụ như một tấm bình phong hoặc nhãn dán để thay thế cho việc miêu tả trải nghiệm đời sống thực.
   - **Default Principle**:
     - Ưu tiên để tình huống đời thực và chi tiết hiện trường tự làm công việc gợi cảm xúc.
     - Ẩn dụ chỉ có giá trị thực sự khi nó giúp người đọc **neo giữ một cảm giác hoặc nhận thức**, không phải để họ nhớ một hình ảnh văn hoa.
     - **Cấm Xếp Chồng Ẩn Dụ (Zero Metaphor Stacking)**: Trong 1 section, chỉ dùng tối đa 1 ẩn dụ trung tâm nếu thực sự cần thiết. Tuyệt đối cấm dùng nhiều ẩn dụ liên tiếp (vạch xuất phát, bức tường đá, ngọn núi, con ngựa gỗ bập bênh) để diễn giải cùng 1 ý tưởng. Khi một ẩn dụ đã làm xong nhiệm vụ mở khóa trực giác, lập tức quay về phân tích cơ chế thực tế.
     - Khi ngôn ngữ đời thường đủ rõ ràng, gần gũi và chạm tới người đọc, hãy nói thẳng bằng trải nghiệm cụ thể, không cần gượng ép tạo thêm ẩn dụ.
     - Tránh rải các biến thể từ vựng xoay quanh một ẩn dụ (biến ẩn dụ thành một chuỗi nhãn dán lặp đi lặp lại) khiến câu chuyện bị tách rời khỏi mặt đất.
   - **Exception / Context-Specific**:
     - Cho phép phát triển các mô hình ẩn dụ mang tính khung tư duy (Mental Models) có hệ thống xuyên suốt chương nếu blueprint hoặc tác giả chủ động lựa chọn để giải thích một khái niệm phức tạp.
   - **Heuristic tự kiểm**:
     - *"Nếu lược bỏ ẩn dụ này và kể thẳng bằng tình huống đời thường cụ thể, câu văn có trở nên thật hơn, chạm hơn và gần gũi hơn không?"*

16. **Tiến Triển Nhận Thức Từng Đoạn (Paragraph Cognitive Progression)**:
   - **Default Principle**: Mỗi đoạn văn phải là một bước tiến mới trên trục nhận thức của độc giả (Hiện tượng $\rightarrow$ Cơ chế tâm lý ngầm $\rightarrow$ Phản biện/Hoài nghi $\rightarrow$ Tiêu chí phân biệt trong thực tế).
   - Nghiêm cấm viết các đoạn văn chỉ là bản dịch hoặc diễn giải lại (paraphrase) của đoạn trước bằng từ ngữ khác. Đã chứng minh xong luận điểm thì chuyển ngay sang bước tiếp theo của mô hình hoặc dừng lại.
   - **Heuristic tự kiểm**: *"Đoạn văn này mang lại hiểu biết mới gì cho độc giả, hay nó chỉ đang nói lại đoạn văn trước bằng một cách dùng từ khác?"*

17. **Điềm Tĩnh Hóa Văn Phong (Prose De-dramatization & Quiet Observation)**:
   - **Default Principle**: Sức nặng của văn bản đến từ sự chính xác của quan sát và tính thuyết phục của logic nhân quả, không đến từ các tính từ mạnh hay giọng điệu phán xét.
   - Tuyệt đối tránh gán ghép các tính từ/phó từ cường điệu gây kịch tính giả tạo (*"vô cùng tàn nhẫn"*, *"tháo chạy vô thức"*, *"cái giá đắt đỏ"*).
   - Giữ sự điềm tĩnh, trung thực và chính xác của một quan sát viên thấu hiểu tâm lý con người.

18. **Tư Duy Sáng Trước Câu Chữ Sáng & Cấm Cơ Chế Khoa Học Giả (Ungrounded Science Guard)**:
   - **Cấm cơ chế khoa học/thần kinh giả**: Tuyệt đối cấm tự ý đưa các thuật ngữ cơ chế sinh học, hóa học, thần kinh học (như *"phần thưởng hóa học"*, *"dopamine kích hoạt"*, *"vùng não bộ ghi nhận"*) như một sự thật hiển nhiên nếu không có nguồn dẫn kiểm chứng trong `sources/notes/`. Khi mô tả cảm xúc đời thường, gọi thẳng tên trạng thái tâm lý chân thực (sự nhẹ nhõm, cảm giác giải phóng, sự phấn khích, nỗi bất an).
   - **Khái niệm phải là mô hình phân loại (Functional Mental Model)**: Khi đưa ra thuật ngữ hoặc khái niệm mới, văn bản phải chỉ rõ nó giúp độc giả phân biệt được hai trạng thái thực tế nào mà trước đây họ hay đánh đồng. Cấm đặt tên cho một nhận xét hiển nhiên rồi ngộ nhận rằng đó là một mô hình tư duy.

19. **The Quickest Fix (Thử Xóa Trước Khi Viết Lại)**:
   - Khi một câu văn gặp vấn đề quanh co, rườm rà hoặc làm loãng luận điểm, phương án kiểm tra đầu tiên là **xóa hẳn câu đó**. Nếu mạch logic của đoạn văn vẫn hoàn chỉnh và sắc bén hơn khi vắng mặt nó, ưu tiên xóa bỏ thay vì tốn công viết lại ba bốn lần.

20. **Tự Nhiên Hóa Đoạn Kết (The Zinsser Natural Exit)**:
   - Khi lập luận và ví dụ đã hoàn thành việc chứng minh luận điểm, tìm ngay lối thoát gần nhất và dừng lại.
   - Cấm đoạn kết tóm tắt lặp lại những gì vừa trình bày. Chỉ viết đoạn đúc kết nếu nó mở ra hệ quả thực tế hoặc làm nhịp chuyển tiếp tự nhiên sang bước tiếp theo.


---

## 2. Quy Trình Chấp Bút 1 Section

0. **Rà soát Feedback & Tự Kiểm (Feedback Carry-Forward — #05)**:
   - Trước khi chấp bút section $i+1$, rà soát lại các phản hồi của tác giả từ các section trước trong cùng chương.
   - Nạp `memory/evolution/style_drift.md` để đối chiếu các pattern đã được tác giả xác nhận từ trước.
   - Lập danh mục tự kiểm nhẩm 2–3 điểm cần lưu ý đặc biệt cho riêng section sắp viết.
   - Khi tác giả xác nhận một feedback là thói quen lặp lại: ghi nhận vào Section 3 của `style_drift.md` theo đúng cấu trúc (Pattern + Feedback tác giả + Scope áp dụng).
1. **Nạp Card & Beat**: Đọc mục tiêu cụ thể, beat và trần từ `budget_words_max` của section trong `card.md`.
2. **Nạp Voice Corpus & Gold Passages**: Đọc 2 đoạn văn mẫu (Gold Passages) trong `voice.md` để bắt nhịp tần số ngôn ngữ (tone & cadence).
3. **Chấp bút tập trung**: Triển khai trọn vẹn beat và Reader Promise của section, không vượt trần `budget_words_max`. Ngừng viết ngay khi chuyển hóa nhận thức đã hoàn tất, không kéo dài dòng hay cố viết tiếp cho đủ số từ.
4. **Kiểm tra sơ bộ**: Bảo đảm có đủ các yếu tố: Mở móc câu $\rightarrow$ Khảo sát cơ chế $\rightarrow$ Câu chuyện hiện trường $\rightarrow$ Đúc rút bài học.

---

## 3. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (Beat từ Card `00_open.md` & Thẻ Story Bank `S-003`):
```yaml
Story: S-003 (Tier A - Ký ức tác giả)
Confirmed Facts: Tác giả trải qua khủng hoảng dòng tiền cuối năm tại công ty; công nợ bị đối tác chậm giải ngân khiến không đủ ngân sách trả thưởng Tết đúng hẹn.
Interview Content: Tác giả nhớ lại cảm giác cô độc khi ngồi một mình trong phòng làm việc, và sự bất lực khi nhận ra cam kết tài chính bị vỡ.
Author Interpretation: Tự do kinh doanh là ảo tưởng nếu không làm chủ được dòng tiền.
Unknown Details: Tên đối tác, số tiền công nợ chính xác, thời tiết cụ thể ngày hôm đó, cấu trúc phòng ốc (giữ nguyên UNKNOWN, cấm bịa).
```

### Output (`chapters/ch_01/sections/00_open.md` trích đoạn):
```markdown
Cuối năm đó, công ty tôi rơi vào một cuộc khủng hoảng dòng tiền nghiêm trọng. Một đối tác lớn thông báo chậm giải ngân công nợ — khoản tiền duy nhất mà chúng tôi dự kiến dùng để chi trả thưởng Tết cho nhân viên như đã hẹn. 

Tôi ngồi một mình trong phòng làm việc, đối diện với câu hỏi làm sao nói sự thật với các cộng sự đang chờ đợi phía ngoài. Không có tiếng trách móc hay tranh cãi ồn ào; chính sự im lặng đó khiến áp lực đè nặng lên từng nhịp thở. Tôi không nhớ rõ hôm đó thời tiết thế nào hay nhiệt độ ngoài trời ra sao, nhưng cảm giác bất lực khi nhận ra mình không thể kiểm soát được cam kết tài chính thì vẫn còn nguyên vẹn. Mọi chi tiết giữ chặt theo Confirmed Facts, đối chiếu trực tiếp với Gold Passages trong `voice.md`.

Nhiều năm qua, người ta vẫn vẽ ra bức tranh lộng lẫy về việc làm chủ: tự do tài chính, tự do thời gian, tự mình làm thuyền trưởng của cuộc đời. Nhưng ngay trong buổi chiều khủng hoảng ấy, tôi nhận ra một sự thật trần trụi: tự do không tự nhiên đến từ một tấm danh thiếp có in chức danh quản lý. Khi bạn không làm chủ được dòng tiền, doanh nhân chẳng khác nào một người đang gánh trên vai sinh kế của nhiều người khác mà không có bất kỳ tấm lưới an toàn nào.

[VISUAL-SUGGESTION: Biểu đồ dòng tiền minh họa khoảng trống giữa doanh thu trên giấy tờ và tiền mặt thực tế tại thời điểm thanh toán]
```

---

## 4. Tiêu Chuẩn Nghiệm Thu

- [ ] Viết độc lập vào file `sections/<name>.md`.
- [ ] Tuân thủ trần từ `budget_words_max` của Card v3 (0 bôi chữ kéo dài).
- [ ] 0 khối mã Mermaid/ASCII art thô; có semantic visual placeholder nếu cần.
- [ ] Tuân thủ CONV-001 (khối văn bản liên tục, không lạm dụng bullet points).
- [ ] Tuân thủ Minimal Formatting Hygiene (không chatify, không bold tùy tiện trong văn xuôi).

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `story-enrichment` | Lấy chi tiết giác quan hiện trường từ thẻ `S-XXX` trong `story_bank.md` để đắp vào cảnh mở đầu hoặc biến cố. |
| `evidence-excavation` | Tra cứu hoặc tái định khung luận điểm khi phát sinh yêu cầu chứng cứ `[EVIDENCE-REQUEST]`. |
| `humanizer` | Khử các cấu trúc viết văn AI (staging, not-X-but-Y, nhịp điệu đều) sau khi hoàn thành bản nháp thô. |
| `editorial-revision` | Chuyển giao section sang chu trình biên tập phẫu thuật 3 lớp sau khi vượt qua linter. |
| `manuscript-formatting` | Tinh chỉnh hình thức bản thảo, nhịp điệu dấu câu và chuẩn hóa typography khi cần rà soát hoặc xử lý ma sát trình bày văn xuôi. |
