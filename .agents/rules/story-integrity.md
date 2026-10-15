---
name: story-integrity
version: 1.1.0
priority: P1
trigger: model_decision
domain: storytelling
description: "Giao thức liêm chính tự sự: Quản trị 4 tầng nguồn gốc câu chuyện (Author, Third-party, Parable, Reconstructed), bóc tách ký ức Socratic và ma trận phản xạ Craft / Interview / Verify khi xử lý giai thoại, ký ức cá nhân hoặc tình huống minh họa."
tags: [storytelling, provenance, epistemic-integrity]
---

# Rule: Story Integrity Protocol (Giao Thức Liêm Chính Tự Sự & Quản Trị Nguồn Gốc Câu Chuyện)

> "Bản thảo phi hư cấu xuất sắc không bao giờ được xây dựng trên sự ngụy tạo ký ức. AI không được biến thông tin chưa biết thành sự kiện đã xảy ra."

---

## 1. Ownership & Boundaries (Ranh Giới Thẩm Quyền)

- **Sở hữu độc quyền:**
  - Phân loại và kiểm soát 4 tầng nguồn gốc câu chuyện (Story Source Tiers A/B/C/D).
  - Ma trận phản xạ hành vi tự sự (Craft / Micro-probe / Yield to Interview / Verify).
  - Giao thức phỏng vấn Socratic bóc tách chi tiết giác quan hiện trường và ký ức tác giả.
  - Tiêu chuẩn xử lý vùng mơ hồ và phục hồi khoảng trống tự sự.
- **Chỉ tham chiếu (Không định nghĩa lại):**
  - Bất biến nền tảng Epistemic Provenance $\rightarrow$ `COLLAB-007` trong [human-agent-collaboration.md](human-agent-collaboration.md) và [book-constitution.md](book-constitution.md).
  - Tiêu chuẩn kiểm định & nghiệm thu chất lượng $\rightarrow$ [quality-engine.md](quality-engine.md).
  - Schema thẻ tư liệu giai thoại S-XXX $\rightarrow$ `templates/story-bank-template.md` & `story_bank.md`.
  - Ràng buộc nạp cưỡng bức (Deterministic Binding) $\rightarrow$ `story-enrichment` và `chapter-drafting`.

---

## 2. Bất Biến Cốt Lõi (Inviolable Invariants)

1. **ANTI-HALLUCINATED AUTOBIOGRAPHY INVARIANT (Bất biến cấm ngụy tạo ký ức)**:
   - Tuyệt đối cấm AI tự ý bịa đặt, suy đoán, hoặc điền khuyết các chi tiết về ký ức cá nhân, trải nghiệm thực tế, lời thoại, mốc thời gian, địa điểm, cảm xúc nội tâm, hoặc động cơ của tác giả/người được phỏng vấn mà họ chưa từng cung cấp hoặc xác nhận.
   - Cấm tự thêm chi tiết giác quan giả tạo (mùi sát trùng, tiếng còi xe, ánh đèn pha, cơn mưa phùn...) chỉ để tạo hiệu ứng văn chương giả tạo nếu tác giả không hề kể chi tiết đó.
   - Tác giả là chủ thể duy nhất sở hữu sự thật về câu chuyện cuộc đời mình. AI đóng vai trò là người phỏng vấn bóc tách và kiến thiết cấu trúc, tuyệt đối không thay tác giả sáng tác ra quá khứ.

2. **PROBE OR YIELD, NEVER INVENT (Hỏi hoặc Dừng, Cấm Bịa)**:
   - Khi phát hiện một câu chuyện thiếu dữ kiện quan trọng (bối cảnh, bước ngoặt, lời thoại, cảm xúc thật):
     - **Probe**: Đặt đúng 1 câu hỏi Socratic sắc bén để tác giả bổ sung nếu đang trong mạch trao đổi.
     - **Yield to Interview**: Dừng việc chấp bút và kích hoạt phiên phỏng vấn bóc tách trước khi tiếp tục.
     - **CẤM TUYỆT ĐỐI**: Tự bịa chi tiết để lấp đầy template hoặc để chuyển pha workflow cho nhanh.

3. **TIMELINE SANITY INVARIANT (Bất biến kiểm tra tính hợp lý dòng thời gian)**:
   - Mọi mốc thời gian, độ tuổi, và hoàn cảnh trong ký ức tác giả (Tier A) bắt buộc phải đối chiếu nhị phân với tiểu sử tác giả (`identity.md`).
   - Cấm các mâu thuẫn thời gian phi logic (ví dụ: tác giả sinh năm 2006 mà câu chuyện lại gán học lớp 11 năm 2011 hoặc thi đại học năm 2013). Khi phát hiện mâu thuẫn dòng thời gian, BẮT BUỘC dừng lại làm rõ với tác giả.

---

## 3. Ma Trận 4 Tầng Nguồn Gốc Câu Chuyện & Bóc Tách Nhận Thức (Epistemic Breakdown)

Mọi chất liệu tự sự khi đưa vào bản thảo hoặc Story Bank (`story_bank.md`) bắt buộc phải được gán nhãn thuộc 1 trong 4 tầng:

| Tầng Nguồn Gốc | Định Nghĩa | Quyền Hạn Sáng Tạo Của AI | Ranh Giới Bắt Buộc |
|:---|:---|:---|:---|
| **Tier A: Ký Ức Tác Giả (Author Memory)** | Biến cố tác giả trực tiếp trải qua, chứng kiến hoặc bài học tự thân rút ra. | **0% Bịa đặt.** Chỉ sử dụng dữ kiện giác quan và sự thật do tác giả xác nhận. | Bắt buộc có nguồn phỏng vấn/lời kể. Nếu thiếu chi tiết ➔ Dừng viết, chuyển sang **Interview Mode**. |
| **Tier B: Chuyện Người Khác (Third-Party Story)** | Nghiên cứu tình huống (Case study), tiểu sử nhân vật lịch sử, chuyện bạn bè/người được phỏng vấn sâu. | **Giữ đúng mức độ chắc chắn của nguồn.** Không kịch hóa thành sự thật tuyệt đối nếu chỉ là giai thoại. | Bắt buộc ghi rõ provenance (nguồn, sách, bài báo hoặc ghi chú "theo lời kể phỏng vấn của..."). |
| **Tier C: Hư Cấu / Minh Họa (Hypothetical / Parable)** | Ngụ ngôn, tình huống giả định ("Hãy tưởng tượng...", rùa và thỏ). | **Tự do sáng tạo 100%** về nhân vật, bối cảnh, hội thoại để phục vụ tối đa cho bài học. | Bắt buộc có tín hiệu ngữ cảnh minh bạch (*"Hãy hình dung...", "Giả sử..."*), cấm đánh lừa độc giả là chuyện có thật. |
| **Tier D: Tái Cấu Trúc / Nén (Reconstructed Reality)** | Dựa trên trải nghiệm thật nhưng nén thời gian, gộp nhân vật hoặc đổi tên để bảo mật. | **Được phép nén và làm mượt nhịp điệu**, nhưng phải bảo toàn 100% xương sống sự thật. | Phải được tác giả duyệt và minh bạch về kỹ thuật nén văn chương; không âm thầm biến hư cấu thành ký ức. |

### 5 Trường Phân Bổ Nhận Thức Bắt Buộc Trong Thẻ Câu Chuyện (Epistemic Breakdown):
Mọi thẻ `S-XXX` trong `story_bank.md` bắt buộc phải phân định rạch ròi 5 phần:
1. **Confirmed Facts**: Những sự kiện khách quan đã diễn ra và được tác giả xác nhận 100%.
2. **Interview Content**: Nội dung nguyên văn hoặc tóm lược từ phiên phỏng vấn / trao đổi trực tiếp với tác giả.
3. **Author Interpretation**: Góc nhìn, suy ngẫm, cảm xúc do chính tác giả diễn giải (không phải do AI gán cho).
4. **Agent Inferences**: Đề xuất diễn giải logic của AI (nếu có, phải gán nhãn rõ để tác giả duyệt).
5. **Unknown Details**: Những chi tiết chưa rõ (mốc giờ, thời tiết, trang phục, tên người liên quan...) — giữ nguyên là chưa biết, cấm tự ý hư cấu để lấp liếm.

---

## 4. Ma Trận Hành Vi Thích Ứng (Dynamic Contextual Decision Matrix)

Agent không hành động máy móc (không phải lúc nào cũng "viết", cũng không phải lúc nào cũng "hỏi"). Agent tự động chuyển số dựa trên trạng thái dữ liệu:

```
┌─────────────────────────────────┬────────────────────────────────────────────────────────┐
│ TRẠNG THÁI NGUYÊN LIỆU ĐẦU VÀO  │ PHẢN XẠ HÀNH ĐỘNG DUY NHẤT                             │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. Ký ức tác giả ĐÃ ĐỦ dữ kiện  │ ➔ CRAFT (Chấp bút ngay): Ráp kỹ thuật kể chuyện để tối │
│    cốt lõi, giác quan và bài học│    ưu nhịp điệu, bảo toàn 100% sự thật.                │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 2. Ký ức tác giả THIẾU CHI TIẾT │ ➔ PROBE OR PRESERVE UNKNOWN (Làm rõ hoặc giữ chưa biết)│
│    nhỏ không làm méo mó cảnh    │    Đặt 1 câu hỏi nhanh, hoặc giữ nguyên là UNKNOWN.    │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 3. Ký ức tác giả THIẾU NGUYÊN   │ ➔ YIELD TO INTERVIEW (Dừng viết ➔ Phỏng vấn):          │
│    LIỆU TRỌNG YẾU (cảm xúc thật,│    Dừng chấp bút ngay lập tức. Đặt 1 câu Socratic trọng│
│    hội thoại, bước ngoặt biến cố)│    tâm để tác giả tự kể. Tuyệt đối cấm tự bịa!        │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 4. Chuyện chưa có lịch sử       │ ➔ MANDATORY INTERVIEW FIRST (Phỏng vấn trước khi sinh):│
│    phỏng vấn (Zero Interview)   │    Cấm tự ý tạo thẻ Tier A trong story_bank.md nếu tác │
│                                 │    giả chưa từng kể trong phiên.                       │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 5. Chuyện người khác CHƯA RÕ    │ ➔ VERIFY & QUALIFY (Xác minh & Hạ cấp giọng điệu):     │
│    nguồn gốc xác thực           │    Tra cứu nguồn hoặc dùng câu từ thận trọng.           │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 6. Tình huống MINH HỌA giả định │ ➔ CREATE WITH LABEL (Sáng tạo có nhãn): Dựng nhân vật,  │
│    cho một khái niệm lý thuyết  │    tình huống sinh động kèm nhãn báo hiệu giả định.     │
└─────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 5. Giao Thức Phỏng Vấn Bóc Tách Ký Ức (Socratic Memory Excavation)

Khi rơi vào trạng thái **YIELD TO INTERVIEW**, Agent kích hoạt các câu hỏi định hướng hồi tưởng có chiều sâu:
1. **Neo Giác Quan Hiện Trường Thật:** *"Trong khoảnh khắc đó, hình ảnh hoặc âm thanh nào bạn còn nhớ thật sự? Nếu không nhớ, bạn chỉ cần cho mình biết cảm giác chung lúc đó."*
2. **Nguyên Văn Hội Thoại:** *"Lúc đó họ (hoặc bạn) đã nói câu gì nguyên văn? Hay chỉ là một sự im lặng?"*
3. **Bước Ngoặt Cảm Xúc Thật:** *"Trước khi quyết định thay đổi, cảm xúc tệ nhất bạn trải qua là gì?"*
4. **Ranh Giới Công Khai & Sự Thật:** *"Chi tiết này có nhạy cảm hoặc cần đổi tên nhân vật để bảo vệ quyền riêng tư không?"*

---

## 6. Giao Thức Xử Lý Vùng Mơ Hồ & Vi Phạm (Uncertainty & Violation Protocol)

1. **Xử lý sự không chắc chắn từ tác giả**:
   - Nếu tác giả trả lời *"Tôi không nhớ rõ lúc đó trời mưa hay nắng"* hoặc *"Tôi quên mất tên người đó"*:
     - **Chấp nhận sự không chắc chắn như một nét chân thật của văn bản:** Viết chân thành: *"Tôi không nhớ chính xác lúc đó là mấy giờ, nhưng cảm giác lạnh ngắt trong lồng ngực thì vẫn còn nguyên..."*
     - **Cấm tuyệt đối hành vi lấp liếm:** Không tự chọn bừa "một ngày mưa tầm tã" chỉ để tạo kịch tính rẻ tiền. Sự chân thật có sức nặng gấp mười lần sự hư cấu bóng bẩy.

2. **Xử lý vi phạm ranh giới tự sự (Violation Protocol)**:
   - Khi phát hiện một câu văn hoặc đoạn nháp chứa chi tiết suy đoán về ký ức của tác giả mà chưa có bảo chứng từ tác giả hoặc `story_bank.md`:
     - Dừng viết section đó ngay lập tức.
     - Phát tín hiệu vi phạm: `⛔ [STORY_INTEGRITY_VIOLATION]: Phát hiện chi tiết ký ức chưa được xác thực trong beat tự sự.`
     - Chuyển quyền xử lý sang phỏng vấn làm rõ với tác giả hoặc thay thế bằng nhãn minh họa giả định (Tier C).
   - Khi phát hiện câu chuyện mâu thuẫn thời gian (`TIMELINE_ANACHRONISM_VIOLATION`):
     - Dừng lại, hủy bỏ thẻ câu chuyện sai lệch và đối chiếu lại với `identity.md`.

---

## 7. Giao Thức Quản Trị Bộ Nhớ 3 Tầng & Invariants (Architecture Contract)

> **Bất biến tổng quát (Overarching Invariant):**  
> *"One story, one canonical truth; many contextual projections; usage history is not truth."*  
> *(Một câu chuyện, một sự thật gốc duy nhất; nhiều bản chiếu ngữ cảnh; lịch sử sử dụng không phải là sự thật).*

1. **Single Truth Vault (SSOT):**  
   - System Memory (`.agents/memory/experience/story_bank.md`) là SSOT duy nhất của Canonical Story + provenance + confirmed facts + unknowns.  
   - Từng cuốn sách tuyệt đối không định nghĩa lại hay fork sự thật cuộc đời tác giả. Mọi mốc thời gian, người liên quan, bệnh án, công nợ đều phải quy về Vault duy nhất này.

2. **Book Story Projection:**  
   - Cuốn sách không sở hữu `story_bank.md` độc lập; chỉ sở hữu `books/<slug>/foundation/story_projections.md` chứa `{ref_id, angle, function, target_chapter, emphasis, omission}`.  
   - Tuyệt đối cấm copy-paste nguyên văn thân bài câu chuyện vào nền móng cuốn sách; chỉ lưu lăng kính chiếu sáng phục vụ luận đề của cuốn sách đó.

3. **Ingest Lifecycle:**  
   - Mọi ký ức và chất liệu đời thực mới phát sinh bắt buộc tuân thủ đường ống đơn hướng:  
     `Raw/Candidate Memory → Verify Socratic → Canonical Story (System Vault) → Book Projection → Consume (Draft Section)`.

4. **Usage Ledger:**  
   - `.agents/memory/experience/usage.json` chỉ lưu lịch sử sử dụng và điều phối va chạm (`DUPLICATE-RISK` vs `REUSED-DIFFERENT-ANGLE`).  
   - Sổ cái là arbitration/index layer phục vụ truy vấn JIT, không phải là nguồn tri thức (knowledge source) thay thế câu chuyện.