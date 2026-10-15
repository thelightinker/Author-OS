# BẢN ĐẶC TẢ VÀ REVERSE-ENGINEERING TOÀN BỘ PIPELINE VIẾT SÁCH (BOOK WRITING AGENT KIT)

> **Mục đích tài liệu:** Báo cáo kỹ thuật chi tiết phục vụ việc reverse-engineer toàn bộ quy trình vận hành thực tế của Writing Agent Kit trong repository. Tài liệu này được thiết kế để một agent độc lập, chưa từng tiếp xúc với codebase, có thể nắm bắt 100% cơ chế vận hành, luồng dữ liệu, các chốt chặn chất lượng, bằng chứng triển khai và các điểm bất thường/rủi ro tiềm ẩn mà không cần audit lại từ đầu.
>
> **Cam kết:** Báo cáo phản ánh **hành vi triển khai thực tế trên đĩa và trong mã nguồn**, phân định rõ ràng giữa hành vi đã xác minh qua code/test và các giả định/suy luận lý thuyết. Không đề xuất giải pháp, không thay đổi hiện trạng codebase.

---

## MỤC LỤC
1. [Tổng Quan Hệ Thống & Triết Lý Vận Hành](#1-tổng-quan-hệ-thống--triết-lý-vận-hành)
2. [Bản Đồ Thành Phần Hệ Thống (Component Architecture Map)](#2-bản-đồ-thành-phần-hệ-thống-component-architecture-map)
3. [Luồng Thực Thi End-to-End & Máy Trạng Thái Toàn Cục](#3-luồng-thực-thi-end-to-end--máy-trạng-thái-toàn-cục)
   - [3.1. Giai đoạn 1: Khai Mở Dự Án (Book Genesis)](#31-giai-đoạn-1-khai-mở-dự-án-book-genesis)
   - [3.2. Giai đoạn 2: Chu Kỳ Sản Xuất Từng Chương (Chapter Cycle - 10 Nodes)](#32-giai-đoạn-2-chu-kỳ-sản-xuất-từng-chương-chapter-cycle---10-nodes)
   - [3.3. Giai đoạn 3: Hợp Nhất, Đọc Mù & Xuất Bản (Book Assembly - 8 Nodes)](#33-giai-đoạn-3-hợp-nhất-đọc-mù--xuất-bản-book-assembly---8-nodes)
4. [Cơ Chế Vận Hành & Quản Trị Ngữ Cảnh (Context & Execution Mechanics)](#4-cơ-chế-vận-hành--quản-trị-ngữ-cảnh-context--execution-mechanics)
5. [Hệ Thống Kiểm Soát Chất Lượng 3 Lớp (Quality Control Engine)](#5-hệ-thống-kiểm-soát-chất-lượng-3-lớp-quality-control-engine)
6. [Bằng Chứng Triển Khai Thực Tế (Code & Contract Evidence)](#6-bằng-chứng-triển-khai-thực-tế-code--contract-evidence)
7. [Các Điểm Bất Thường, Đứt Gãy & Rủi Ro Đã Xác Minh](#7-các-điểm-bất-thường-đứt-gãy--rủi-ro-đã-xác-minh)

---

## 1. TỔNG QUAN HỆ THỐNG & TRIẾT LÝ VẬN HÀNH

Writing Agent Kit là một hệ thống đa tác tử (multi-agent system) chuyên dụng cho việc sản xuất sách phi hư cấu (non-fiction) chất lượng cao. Khác với các hệ thống sinh văn bản thông thường dựa vào một prompt duy nhất để xả toàn bộ cuốn sách, hệ thống này mô phỏng quy trình của một nhà xuất bản chuyên nghiệp với sự phân chia nhiệm vụ nghiêm ngặt.

### 1.1. Các Nguyên Tắc Bất Biến (Core Architectural Invariants)
1. **Pure Markdown SSOT (Single Source of Truth):**
   - 100% dữ liệu sách, quy chuẩn giọng văn, kiến trúc mục lục, ghi chú bằng chứng và bản thảo được lưu trữ dưới dạng các tệp Markdown thuần túy trên đĩa (`Books/<book_slug>/`).
   - Tuyệt đối không dùng cơ sở dữ liệu ngoài, không dùng vector database phụ thuộc, không dùng state ẩn trong bộ nhớ RAM hay process background.
2. **Modular Section Invariant ("No Premature Draft Assembly"):**
   - Mọi hoạt động sáng tác, drafting và phẫu thuật biên tập diễn ra 100% tại các tệp section nguyên tử: `chapters/<chapter_id>/sections/*.md` (định dạng `00_open.md`, `01_sec1.md`, ...).
   - Tệp `draft.md` chỉ là một góc nhìn phái sinh (assembled view) được sinh ra bằng compiler tất định (`scripts/assemble_chapter.py`). Cấm chỉnh sửa trực tiếp vào `draft.md`.
3. **Strict Sequential Execution & Context Reset (`SEQ-001` - `SEQ-006`):**
   - Tại một thời điểm, **duy nhất 1 Agent** được quyền hoạt động. Cấm chạy song song nhiều agent sinh văn xuôi.
   - Khi chuyển giao quyền điều khiển giữa các vai trò (`master-orchestrator` $\rightarrow$ `book-architect` $\rightarrow$ `chapter-crafter` $\rightarrow$ `quality-auditor`), hệ thống cưỡng chế **Context Reset**: giải phóng toàn bộ bộ nhớ đệm suy luận cũ, chỉ nạp đúng prompt của role mới, các skill trực thuộc và các tệp đầu vào chỉ định trên đĩa.
4. **Anti-Self-Approval & Separation of Concerns (`SEQ-008`):**
   - Agent chấp bút (`chapter-crafter`) tuyệt đối không được tự duyệt bản thảo của mình là `PASS`.
   - Agent thẩm định (`quality-auditor`) tuyệt đối không được tự sửa câu chữ trên bản thảo; chỉ được chẩn đoán bệnh học lâm sàng và chỉ định hành động đặc trị.
5. **Epistemic Hierarchy (Thang Nhận Thức 5 Cấp - `COLLAB-012`):**
   - Dữ liệu được phân tầng nghiêm ngặt: `VERIFIED_FACT` (Sự thật có chứng cứ SSOT) $\rightarrow$ `USER_STATED` (Tác giả trực tiếp kể) $\rightarrow$ `AGENT_INFERENCE` (AI suy luận, phải gắn nhãn) $\rightarrow$ `HYPOTHESIS` (Giả thuyết) $\rightarrow$ `UNKNOWN` (Chưa biết, giữ nguyên, cấm bịa).
   - **Insufficient-Context Gate (`COLLAB-011`):** Khi chạm đến quan điểm, nhân sinh quan, trải nghiệm mà tác giả chưa từng chia sẻ: **DỪNG VÀ PHỎNG VẤN (PROBE OR YIELD, NEVER INVENT)**.

---

## 2. BẢN ĐỒ THÀNH PHẦN HỆ THỐNG (COMPONENT ARCHITECTURE MAP)

Hệ thống được tổ chức theo cấu trúc liên kết chặt chẽ giữa 4 tầng: **Agents $\leftrightarrow$ Workflows $\leftrightarrow$ Skills $\leftrightarrow$ Tools/Scripts**.

```
                           ┌───────────────────────────┐
                           │    MASTER ORCHESTRATOR    │ (L0 Controller)
                           │ (.agents/agent/master-    │
                           │      orchestrator.md)     │
                           └─────────────┬─────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        │                                │                                │
┌───────▼────────────────┐   ┌───────────▼────────────┐   ┌───────────────▼───────────┐
│     BOOK ARCHITECT     │   │     CHAPTER CRAFTER    │   │      QUALITY AUDITOR      │
│ (L1 Macro Strategist)  │   │  (L1 Micro Craftsman)  │   │   (L1 Independent Critic) │
│ (.agents/agent/book-   │   │ (.agents/agent/chapter-│   │ (.agents/agent/quality-   │
│      architect.md)     │   │       crafter.md)      │   │        auditor.md)        │
└───────┬────────────────┘   └───────────┬────────────┘   └───────────────┬───────────┘
        │ 4 Skills                       │ 7 Skills                       │ 2 Skills
        ├─ genesis-interview             ├─ chapter-blueprinting          ├─ editorial-revision
        ├─ spine-architecture            ├─ story-enrichment              └─ falsification-steelmanning
        ├─ evidence-excavation           ├─ chapter-drafting                 (SHARED)
        └─ falsification-steelmanning    ├─ editorial-revision
           (SHARED)                      ├─ humanizer
                                         ├─ manuscript-formatting
                                         └─ falsification-steelmanning
```

### 2.1. Ma Trận Vai Trò Tác Tử (Agent Roster)

| Tên Agent | Tệp Định Nghĩa | Vai Trò & Thẩm Quyền | Công Cụ Cho Phép | Kỹ Năng Nạp (Owned Skills) |
| :--- | :--- | :--- | :--- | :--- |
| **`master-orchestrator`** | `.agents/agent/master-orchestrator.md` | **L0 System Controller**: Quản trị FSM, điều phối workflow, cưỡng chế Context Reset, kiểm soát Human Gates. Miễn trừ quy tắc nạp skill. | `Read`, `Grep`, `Glob`, `Agent`, `Bash` | Không nạp skill (Zero fake routing skills) |
| **`book-architect`** | `.agents/agent/book-architect.md` | **L1 Macro Strategist**: Tầm cao 10,000m. Phỏng vấn Genesis, thử lửa luận đề, kiến trúc Book Spine 3 tầng, mạch Leads-to, xử lý bằng chứng. | `Read`, `Grep`, `Glob`, `Edit`, `Write` | `genesis-interview`, `spine-architecture`, `evidence-excavation`, `falsification-steelmanning` (4 bindings) |
| **`chapter-crafter`** | `.agents/agent/chapter-crafter.md` | **L1 Micro Craftsman**: Tầm cao 1m. Bóc tách ký ức Socratic, lập Chapter Card v3, viết văn xuôi module từng section, phẫu thuật 3-pass editorial. | `Read`, `Grep`, `Glob`, `Edit`, `Write` | `chapter-blueprinting`, `story-enrichment`, `chapter-drafting`, `editorial-revision`, `humanizer`, `manuscript-formatting`, `falsification-steelmanning` (7 bindings) |
| **`quality-auditor`** | `.agents/agent/quality-auditor.md` | **L1 Independent Critic**: Độc giả độc lập bảo vệ người mua sách. Thẩm định Chapter (Layer 2) và Đọc mù toàn sách (Layer 3 Cold Read). Cấm sửa văn bản. | `Read`, `Grep`, `Glob` (Chỉ đọc) | `editorial-revision` (tiêu thụ rubric), `falsification-steelmanning` (2 bindings) |

### 2.2. Danh Mục Kỹ Năng Chuyên Biệt (Skill Inventory - 11 Skills)

Tọa lạc tại `.agents/skills/<skill_name>/SKILL.md`:
1. **`genesis-interview`**: Điều phối phỏng vấn Socratic 4 nhóm câu hỏi khai mở dự án: Manifesto, Chân dung tác giả, Lời hứa bìa, Voice corpus, khởi tạo `terms.md` và `story_bank.md`.
2. **`spine-architecture`**: Thiết kế khung xương 3–4 tầng (`Part > Chapter > Section`), chuỗi domino nhân quả `Leads-to`, bảng cam kết đền đáp `promises.md`, tính toán Blast Radius khi đổi cấu trúc.
3. **`evidence-excavation`**: Khảo sát tài liệu thô trong `sources/raw/`, phân loại 5 cấp bậc nguồn, cập nhật `evidence_ledger.md`, quy trình leo thang 4 bước khi thiếu dữ liệu (`Reframe → Soften → Cut`).
4. **`falsification-steelmanning` (SHARED)**: Thử sức chịu tải luận điểm đối nghịch. Dựng phản đề mạnh nhất của đối thủ (Steelman), truy quét ngụy biện, xác lập điều kiện biên ("Đúng khi nào, Sai khi nào?"). Dùng chung cho Architect (Genesis/Spine) và Crafter (Pass 1 Self-Check).
5. **`chapter-blueprinting`**: Thiết kế bản vẽ Chapter Card v3 (`card.md`): chọn Chapter Shape (5 shapes), lập Beat Map với đúng 1 nhịp PEAK, ấn định `new_for_reader`, `anchor`, và trần từ `budget_words_max`.
6. **`story-enrichment`**: Bóc tách ký ức Socratic 4 nhóm câu hỏi (Giác quan hiện trường, Chuyển biến tâm lý, Hành động cụ thể, Vùng chưa chắc chắn) để hoàn thiện thẻ `S-XXX` trong `story_bank.md`.
7. **`author-excavation`**: Khai quật insight theo thang 7 bậc (Insight Ladder), bắt nhanh câu chuyện thô (Fast Story Capture), phục vụ phỏng vấn đào sâu nhận thức gốc rễ.
8. **`chapter-drafting`**: Chấp bút văn xuôi từng section độc lập (`sections/*.md`), tuân thủ chuẩn CONV-001 (khối văn liên tục), nhúng semantic visual placeholders, yield khi gặp `[EVIDENCE-REQUEST]`.
9. **`humanizer`**: Biên tập khử sạch 7 dấu hiệu AI writing (staging, not-X-but-Y, triads, dramatic fragments, inflated claims, bold labels, false cadences), neo giọng văn vào `voice.md`, giữ nguyên 100% sự thật.
10. **`editorial-revision`**: Phẫu thuật biên tập 3 lớp (Substance, Zinsser Clutter Cut, Tiết tấu âm hưởng Việt), áp dụng kỷ luật bắt buộc `WHAT TO KEEP`, chỉ can thiệp trên đúng section bị báo lỗi.
11. **`manuscript-formatting`**: Chuẩn hóa hình thức xuất bản, loại bỏ ma sát trình bày, dấu câu gượng gạo (lạm dụng em dash, colon, bullet points) bằng kỹ thuật tái cấu trúc cú pháp (Syntactic Re-anchoring).

### 2.3. Hệ Thống Luật Lệ (Rules - `.agents/rules/`)

1. **`authorship-contract.md`** (`always_on`): Hợp đồng chủ quyền tác giả. Ma trận phân quyền quyết định, ranh giới Ask-vs-Decide, Goal Lock Protocol, 3 Chat Modes (Dialogue, Status, Review), Thang nhận thức 5 cấp, Badge hiển thị chat.
2. **`book-constitution.md`** (`always_on`): Hiến pháp cấu trúc và nguồn sự thật (SSOT). Cấu trúc thư mục `Books/<book_slug>/`, Modular Section Invariant, Single Active Agent, Gap Token Standard (`[PENDING:]`, `[QUERY:]`, `[VERIFY]`, `[AUTHOR]`, `[EVIDENCE-REQUEST:]`).
3. **`quality-engine.md`** (`stage_loaded`): Hệ thống kiểm định chất lượng 3 lớp: L1 Mechanical Screen, L2 Chapter Review (15 bệnh học lâm sàng, Materiality Threshold), liên kết L3 Cold Read.
4. **`story-integrity.md`** (`stage_loaded`): Giao thức liêm chính tự sự: Quản trị 4 tầng nguồn gốc câu chuyện, 5 thành phần Epistemic Breakdown, ma trận phản xạ Craft/Interview/Verify, cấm bịa đặt số liệu/chi tiết điện ảnh.
5. **`manuscript-cold-read.md`** (`stage_loaded`): Quy chuẩn kiểm định độc lập toàn sách (Whole-Book Cold Read): Hàng rào đọc mù tuyệt đối (Absolute Blind Barrier), 10 giả thuyết thẩm định đòn bẩy cao, 3 phân tầng rủi ro định tính, 4 phán quyết ấn hành (`Ship`, `Conditional`, `Major Revise`, `Kill`).
6. **`chat-artifact-interface.md`** (`stage_loaded`): Quy chuẩn giao tiếp giữa chat và đĩa: cấm xả raw manuscript ra chat, ngân sách chat $\le 10$ dòng.
7. **`human-agent-collaboration.md`** (`stage_loaded`): Giao thức phối hợp người - máy, quản trị nhịp làm việc và checkpoint.

### 2.4. Công Cụ & Scripts Bổ Trợ (Executable Tools & CLI)

Toàn bộ công cụ kỹ thuật được viết bằng **Python Standard Library (100% stdlib)**, không phụ thuộc thư viện bên ngoài:

| Đường Dẫn Script | Chức Năng Chính | Lệnh Gọi & Mã Trả Về (Exit Codes) |
| :--- | :--- | :--- |
| `scripts/repair_invariants.py` | Sàng lọc cơ học Layer 1: Unicode NFC, khoảng trắng dấu câu, gap tokens, cấm diagram thô, lọc từ sáo rỗng translationese; tăng biến đếm `revision_round` tất định. | - `--lint <path>`: 0 = PASS; 1 = Lỗi hình thức/sáo rỗng; 3 = Phát hiện Epistemic Gap (`[GAP:]`, `[AUTHOR:]`).<br>- `--step-revision <card.md>`: 0 = Tăng vòng thành công; 2 = Đạt trần 3/3 vòng (Plateau). |
| `scripts/assemble_chapter.py` | Ghép các file `sections/*.md` thành `draft.md` (cấp chương) hoặc ghép toàn bộ các chương thành `outputs/manuscript.md` (cấp sách) theo thứ tự tự nhiên (natural sort). | - `--chapter <id> [--commit]`: Ghép chương.<br>- `--all [--commit]`: Ghép toàn bộ bản thảo sách. |
| `scripts/context_budget.py` | Đo lường ngân sách token tĩnh cho từng Node trong workflow dựa trên `docs/context_budget_map.json`. | Đọc cấu hình token, tính toán tổng tải trọng context. |
| `scripts/export_pdf.py` | Hỗ trợ xuất bản thảo Markdown sang định dạng PDF/HTML. | Đóng gói xuất bản cuối kỳ. |
| `.agents/scripts/memory_cli.py` | Bộ CLI quản trị bộ nhớ sống (Living Memory): tra cứu giọng văn, kiểm tra chống trùng lặp câu chuyện (`usage.json`), kiểm tra tính nhất quán (`audit-continuity`), trích xuất bối cảnh viết 4 khối (`get-writing-context`), kiểm tra số liệu/trích dẫn chưa có nguồn (`check-provenance`), ghi nhận bài học từ sửa tay (`record-draft-baseline`, `check-draft-diff`). | Cung cấp 15 lệnh chuyên biệt: `get-voice`, `get-story`, `record-story-usage`, `get-evidence`, `get-continuity`, `update-continuity`, `audit-continuity`, `capture`, `find`, `check`, `get-writing-context`, `check-provenance`, `record-draft-baseline`, `record-ideas-used`, `check-draft-diff`. |

---

## 3. LUỒNG THỰC THI END-TO-END & MÁY TRẠNG THÁI TOÀN CỤC

Toàn bộ vòng đời sản xuất một cuốn sách vận hành qua **3 Workflow kế tiếp nhau**, được điều phối độc quyền bởi `master-orchestrator`:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      GIAI ĐOẠN 1: BOOK GENESIS WORKFLOW                         │
│  Khởi tạo nền tảng dự án qua 5 Human Gates:                                      │
│  Manifesto (G1) ➔ Voice (G2) ➔ Stories (G3) ➔ Spine/Promises (G4) ➔ Terms (G5)  │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ Hoàn thành Genesis (Spine [APPROVED])
┌────────────────────────────────────────▼────────────────────────────────────────┐
│               GIAI ĐOẠN 2: CHAPTER CYCLE WORKFLOW (Lặp từng chương)              │
│  Vòng lặp sản xuất 10 nodes:                                                    │
│  Blueprint ➔ Goal Lock ➔ Excavation ➔ Drafting ➔ Mechanical Screen              │
│  ➔ (Revision Loop ≤3) ➔ Assembly ➔ Layer 2 Review ➔ Memory Update ➔ Spine Check │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │ Hoàn thành 100% các chương theo Spine
┌────────────────────────────────────────▼────────────────────────────────────────┐
│                     GIAI ĐOẠN 3: BOOK ASSEMBLY WORKFLOW                         │
│  Tổng hợp & Thẩm định toàn cục:                                                 │
│  Consistency ➔ Leads-to Thread ➔ Smoothing ➔ Compile Manuscript                 │
│  ➔ Voice Audit (Read-only) ➔ Cold Read L3 (Blind) ➔ Gate 4 Final ➔ Export       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.1. Giai Đoạn 1: Khai Mở Dự Án (Book Genesis)
*Quy chuẩn:* `.agents/workflows/book-genesis.md` (Version 2.1.0)  
*Mục tiêu:* Thiết lập Sổ bộ nền tảng (Foundation SSOT) vững chắc tại `Books/<book_slug>/foundation/`.

```
GENESIS_MANIFESTO ──(manifesto_ok)──► GATE_1_MANIFESTO ──(approved)──► GENESIS_VOICE
                                                                            │
GATE_3_STORIES ◄──(stories_ok)── GENESIS_STORIES ◄──(approved)── GATE_2_VOICE
      │
      ▼
PATH_SELECTION ──(Path A: Top-Down)──► SOURCE_TRIAGE ──► SPINE_DESIGN ──► GATE_4_SPINE
      │                                                                         ▲
      └──(Path B: Draft-First)───────► DRAFT_FIRST_SAMPLE ─────────────────────┘
                                                                                │
                                                                            (approved)
                                                                                │
                                                                                ▼
             DONE ◄──(approved)── GATE_5_TERMS ◄──(terms_ok)── GENESIS_TERMS
```

#### Chi Tiết Từng Bước Trong Genesis:
1. **`GENESIS_MANIFESTO`**:
   - *Worker:* `book-architect` nạp `genesis-interview` + `falsification-steelmanning`.
   - *Hành động:* Phỏng vấn Socratic bóc tách Luận đề cốt lõi, Chân dung độc giả, Cơn đau lúc 2h sáng, Lời hứa trang bìa. Sau đó đóng vai phản biện đối nghịch công kích luận đề, lập bảng Điều kiện biên (`Boundary Conditions`: Đúng khi nào, Sai khi nào).
   - *Output:* `foundation/manifesto.md`.
2. **`GATE_1_MANIFESTO` (Human Gate 1):** Tác giả duyệt tôn chỉ tối cao.
3. **`GENESIS_VOICE`**:
   - *Worker:* `book-architect` nạp `genesis-interview`.
   - *Hành động:* Định hình tư thế người viết (ngồi cạnh bạn đọc), đại từ xưng hô (`Tôi`, `Chúng ta`, `Bạn`), nhịp thở câu văn và trích xuất 2–3 đoạn văn mẫu (Gold Passages).
   - *Output:* `foundation/voice.md`.
4. **`GATE_2_VOICE` (Human Gate 2):** Tác giả thẩm định âm hưởng giọng văn.
5. **`GENESIS_STORIES`**:
   - *Worker:* `book-architect` nạp `genesis-interview` + `story-enrichment`.
   - *Hành động:* Khai quật kho giai thoại đời thực của tác giả, khởi tạo thẻ `S-XXX` theo chuẩn Epistemic Breakdown (sự thật xác thực, lời kể, suy luận, vùng chưa biết).
   - *Output:* `foundation/story_bank.md` (và liên kết System Vault `.agents/memory/experience/story_bank.md`).
6. **`GATE_3_STORIES` (Human Gate 3):** Tác giả xác thực tính liêm chính của các câu chuyện.
7. **`PATH_SELECTION` (Phân Nhánh Phương Pháp Luận):**
   - **Path A (Top-Down Outline):** Phù hợp với tác giả đã có cấu trúc rõ ràng $\rightarrow$ Đi qua `SOURCE_TRIAGE` (phân loại nguồn tài liệu `sources/raw/` vào `evidence_ledger.md`) $\rightarrow$ `SPINE_DESIGN` (thiết kế mục lục 3 tầng và cam kết `promises.md`).
   - **Path B (Draft-First / Bottom-Up Synthesis):** Phù hợp khi tác giả cần "viết thử để tìm giọng": `chapter-crafter` viết thử 1 chương mẫu $\rightarrow$ `book-architect` tổng hợp ngược từ dưới lên để kiến tạo Book Spine.
8. **`GATE_4_SPINE` (Human Gate 4):** Tác giả phê duyệt Khung xương sống cuốn sách (`book_spine.md` và `promises.md`).
9. **`GENESIS_TERMS`**:
   - *Worker:* `book-architect` nạp `genesis-interview`.
   - *Hành động:* Khởi tạo Ma trận khái niệm độc quyền: gán vai trò chiến lược cho từng thuật ngữ (Khái niệm giải phóng, Luận đề dẫn dắt, Phản đề bề mặt).
   - *Output:* `foundation/terms.md`.
10. **`GATE_5_TERMS` (Human Gate 5):** Tác giả chốt thuật ngữ $\rightarrow$ Hoàn thành Genesis (`DONE`).

---

### 3.2. Giai Đoạn 2: Chu Kỳ Sản Xuất Từng Chương (Chapter Cycle - 10 Nodes)
*Quy chuẩn:* `.agents/workflows/chapter-cycle.md` và 10 tệp đặc tả tại `.agents/workflows/chapter-cycle/node-*.md`.  
*Vận hành:* Lặp lại tuần tự cho từng chương $ch_1, ch_2, \dots, ch_n$ đã chốt trong `book_spine.md`.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    CHAPTER CYCLE FSM ENGINE                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

 [Node 1: BLUEPRINT] ──► [Node 2: GATE_3_BLUEPRINT & GOAL_LOCK] (Human Gate)
                                   │ (approved)
                                   ▼
                       [Node 3: KNOWLEDGE_EXCAVATION] ◄──── Yield to interview if missing facts
                                   │ (stories ready)
                                   ▼
                       [Node 4: SECTION_DRAFTING] (Sequential section cadence)
                                   │   ▲
                                   │   │ Evidence Gap Sub-Loop ([EVIDENCE-REQUEST])
                                   │   ▼
                                   │ Book Architect / Evidence Excavation
                                   │
                                   ▼
                       [Node 5: MECHANICAL_SCREEN] (repair_invariants.py + check-provenance)
                                   │
                 ┌─────────────────┼───────────────────────────┐
                 │ exit == 0       │ exit == 3 (Gap)           │ exit == 1 (Style defect)
                 ▼                 ▼                           ▼
        [Node 7: ASSEMBLY]    [Node 2: GATE_3]       [Node 6: SECTION_REVISION]
        (assemble_chapter.py) (Dừng hỏi tác giả)               │
                 │                                             │ (repair_invariants.py
                 ▼                                             │  --step-revision)
        [Node 8: REVIEW]                                       ▼
        (quality-auditor)                            [Node 5: MECHANICAL_SCREEN]
                 │                                             ▲
                 ├─────────────────────────┬───────────────────┘ (revision_round < 3)
                 │ PASS                    │ REVISE
                 ▼                         ▼
        [Node 9: MEMORY_UPDATE]    (Nếu round >= 3 ➔ Plateau Hard Stop)
                 │
                 ▼
        [Node 10: SPINE_CHECK] ──► DONE (Sẵn sàng sang chương kế tiếp)
```

#### Đặc Tả Chi Tiết 10 Node Thực Thi:

#### **Node 1: BLUEPRINT (`node-01-blueprint.md`)**
- **Thực thi:** `chapter-crafter` nạp `chapter-blueprinting`.
- **Đầu vào (Input):** `book_spine.md`, `terms.md`, `story_bank.md`, `knowledge/structure/chapter_shapes.md`.
- **Cơ chế Feedback Loop Tự Động:** Chạy `python .agents/scripts/memory_cli.py check-draft-diff --all`. Nếu tác giả từng sửa tay bản thảo ở các chương trước, CLI phát hiện diff, Crafter rút ra tối đa 3 quy tắc viết thực tế và ghi vào `.agents/memory/evolution/feedback.jsonl`.
- **Hành động:** 
  1. Chọn 1 trong 5 Chapter Shapes (`story-unpack-apply`, `myth-bust`, `problem-turn-practice`, `question-journey`, `contrast-pair`).
  2. Bẻ gãy chương thành 3–5 beats/sections (`00_open.md`, `01_sec1.md`, ...).
  3. Lập bảng Beat Map với các trường bắt buộc: `beat`, `role`, `new_for_reader` (giá trị mới cho người đọc, 1 câu duy nhất), `anchor` (mã story hoặc mục bằng chứng cụ thể; nếu không có ghi `none`), và ngân sách từ `budget_words_max` (tổng 3,500–5,000 từ).
  4. Đảm bảo quy tắc **Single PEAK Invariant**: toàn bộ Beat Map chỉ có duy nhất 1 beat mang vai trò `turn (PEAK)`.
- **Đầu ra (Output):** `chapters/<chapter_id>/card.md` ở trạng thái `[DRAFT-READY]`.

#### **Node 2: GATE_3_BLUEPRINT & GOAL_LOCK (`node-02-goal-lock.md`)**
- **Thực thi:** `master-orchestrator` phối hợp tác giả.
- **Human Gate:** `true`. Kiểm soát theo Bậc thang Tin cậy (`Trust Escalation Enum`):
  - `always_ask`: Bắt buộc tác giả duyệt đối với Chapter 1, 2, 3.
  - `sample_first`: Tác giả duyệt Card kèm 1 section mẫu.
  - `auto_proceed`: Từ Chapter 4 trở đi nếu tác giả bật tự động.
- **Goal Lock Protocol:** Khi tác giả phê duyệt, hai trường `Core Thesis` và `Reader Promise` bị **KHÓA BẤT BIẾN**. Không agent nào được tự ý bẻ lái luận điểm trong lúc viết nếu không có lệnh `GOAL_UNLOCK` tường minh từ tác giả.

#### **Node 3: KNOWLEDGE_EXCAVATION (`node-03-excavation.md`)**
- **Thực thi:** `chapter-crafter` nạp `story-enrichment` + `author-excavation`.
- **Đầu vào:** Thẻ câu chuyện gán trong `card.md`, rule `story-integrity.md`.
- **Chốt chặn Insufficient-Context (`COLLAB-011`):** Phỏng vấn Socratic 4 nhóm câu hỏi (Giác quan hiện trường, Chuyển biến tâm lý, Hành động cụ thể, Vùng chưa chắc chắn). Nếu thiếu dữ kiện đời thực trọng yếu: **BẮT BUỘC DỪNG LẠI PHỎNG VẤN TÁC GIẢ (Yield to Interview)**. Tuyệt đối cấm nhảy sang Drafting khi chưa phỏng vấn.
- **Đầu ra:** Cập nhật chi tiết hiện trường đã kiểm chứng vào `story_bank.md`.

#### **Node 4: SECTION_DRAFTING (`node-04-drafting.md`)**
- **Thực thi:** `chapter-crafter` co-pilot linh hoạt: `chapter-drafting` + `humanizer` + `story-enrichment`.
- **Đầu vào:** `card.md`, `story_bank.md`, 2 đoạn văn mẫu từ `voice.md`.
- **Quy trình Chấp bút Khép kín:**
  1. *Bước 0 (Bắt buộc):* Chạy `python .agents/scripts/memory_cli.py get-writing-context --chapter <chapter_id>` nạp 4 khối bối cảnh: `=== CUOI_CHUONG_TRUOC ===`, `=== TOM_TAT_CHUONG_TRUOC ===`, `=== PHAN_HOI_TAC_GIA ===`, `=== Y_DA_DUNG ===`.
  2. *Chỉ thị chống lặp & Neo chất liệu:* 
     - Không mở lại ý hay hình ảnh trong `Y_DA_DUNG`. Ngoại lệ mỏ neo: cho phép tối đa 2 câu tham chiếu ngắn để nối mạch, với điều kiện câu ngay sau phải đưa ra góc nhìn mới, cấm giải thích lại cơ chế cũ.
     - Lấy `new_for_reader` của các beat trước làm danh sách điều đã nói, không diễn giải lại.
     - Mỗi đoạn phải có ít nhất 1 chi tiết cụ thể từ `anchor`. Beat có anchor `none` chỉ được viết tối đa 2 câu làm câu nối.
     - Khẳng định tổng quát ("mọi người", "luôn luôn", "ai cũng", "chắc chắn") chỉ được viết khi có $\ge 2$ anchors.
  3. *Chấp bút tuần tự (Sequential Section Cadence):* Viết xong Section $i$ $\rightarrow$ Xuất thông báo ngắn $\rightarrow$ Checkpoint tác giả $\rightarrow$ Viết Section $i+1$. Cấm viết toàn bộ chương cùng lúc.
  4. *Chuẩn Heading H2:* Mỗi section mở đầu bằng tiêu đề `## [Tiêu đề Section]`.
  5. *Định dạng CONV-001:* Khối văn xuôi tự sự liên tục, không lạm dụng gạch đầu dòng bullet.
  6. *Cơ chế Evidence Gap Yield Sub-Loop:* Khi gặp số liệu chưa rõ nguồn, chèn `[EVIDENCE-REQUEST: req_XX]`, lập `evidence_request.md` và ngừng viết (yield) $\rightarrow$ Context Reset $\rightarrow$ `book-architect` giải quyết $\rightarrow$ Context Reset $\rightarrow$ Crafter viết tiếp.
- **Đầu ra:** Các tệp `chapters/<chapter_id>/sections/*.md`.

#### **Node 5: MECHANICAL_SCREEN (`node-05-mechanical-screen.md`)**
- **Thực thi:** L0 Direct (Script stdlib — Zero LLM).
- **Lệnh thực thi:**
  1. `python scripts/repair_invariants.py --lint chapters/<chapter_id>/sections/`
  2. `python .agents/scripts/memory_cli.py check-provenance --chapter <chapter_id>`
- **Điều kiện phân nhánh (Transitions):**
  - **Exit code 0 (PASS):** Cả linter và provenance đều sạch $\rightarrow$ Chuyển sang `CHAPTER_ASSEMBLY` (Node 7).
  - **Exit code 3 (Epistemic Gap):** Phát hiện `[GAP:]`, `[AUTHOR:]`, `[EVIDENCE-REQUEST:]` $\rightarrow$ Chuyển về `GATE_3_BLUEPRINT` để hỏi tác giả; **CẤM** chuyển sang Section Revision để ngăn AI tự bịa đặt.
  - **Exit code 1 (Lỗi phong cách/sáo rỗng hoặc Provenance lỗi) && `revision_round < 3`:** Chuyển sang `SECTION_REVISION` (Node 6).
  - **Exit code 1 && `revision_round >= 3`:** Hết hạn ngạch sửa $\rightarrow$ Đẩy cưỡng bức lên `INFORMED_REVIEW` (Node 8) để Auditor xử lý hoặc kích hoạt dừng khẩn cấp.

#### **Node 6: SECTION_REVISION (`node-06-revision.md`)**
- **Thực thi:** `chapter-crafter` nạp `editorial-revision` (kèm `humanizer` khi cần).
- **Đầu vào:** Lỗi từ linter hoặc bảng Diagnostic Rubric từ `audit_verdict.md`.
- **Kỷ luật phẫu thuật:**
  - Chỉ mở và sửa **DUY NHẤT** tệp section bị báo lỗi.
  - Bắt buộc áp dụng `WHAT TO KEEP`: Trích 1–2 câu đắt giá nhất giữ nguyên 100%.
  - Áp dụng nguyên tắc sửa tối thiểu: Chỉ sửa đúng câu/đoạn bị báo, giữ nguyên các phần còn lại, không viết lại toàn bộ section.
  - Tăng biến đếm vòng sửa tất định: `python scripts/repair_invariants.py --step-revision chapters/<chapter_id>/card.md`.
- **Đầu ra:** Cập nhật tệp section bị lỗi $\rightarrow$ Quay lại `MECHANICAL_SCREEN` (Node 5).

#### **Node 7: CHAPTER_ASSEMBLY (`node-07-assembly.md`)**
- **Thực thi:** L0 Direct (Script stdlib — Zero LLM).
- **Lệnh thực thi:** `python scripts/assemble_chapter.py --chapter <chapter_id> --commit`.
- **Hành động:** Đọc toàn bộ các tệp trong `sections/`, sắp xếp theo thứ tự tự nhiên (`00_open.md`, `01_sec1.md`, ...), ghép lại thành bản xem tổng hợp kèm banner nguồn sự thật.
- **Đầu ra:** `chapters/<chapter_id>/draft.md` $\rightarrow$ Chuyển sang `INFORMED_REVIEW` (Node 8).

#### **Node 8: INFORMED_REVIEW (`node-08-review.md`)**
- **Thực thi:** `quality-auditor` trong Chapter Review Mode (Critic độc lập).
- **Hàng rào ngữ cảnh (Context Isolation Barrier):**
  - **ĐƯỢC NẠP:** `draft.md`, `card.md`, `summaries.md` (Payload Registry chống lặp ý), `terms.md`, `voice.md`, và rule `quality-engine.md`.
  - **TUYỆT ĐỐI CẤM NẠP:** `manifesto.md`, `sources/`, `evidence_ledger.md`, nhật ký chat.
- **Tiêu chuẩn kiểm định kép (Dual-Lens Audit):**
  - *Lens A (Truth & Logic):* Mâu thuẫn sự thật, ngụy biện, hụt cầu nối.
  - *Lens B (Reader Experience):* Lực cản câu chữ, nhịp điệu phẳng lặng, lặp ý liên section.
  - *Reader Progression Check:* Phép thử đoán trước (đọc câu đầu đoán nội dung; nếu đoán được $\rightarrow$ báo `LẶP Ý`), kiểm tra câu khẳng định tổng quát thiếu anchor ($\rightarrow$ báo `NÓI QUÁ`), kiểm tra câu sáo rỗng đặt vào sách nào cũng được ($\rightarrow$ báo `CHUNG CHUNG`).
  - *Materiality Threshold (Quyền không bắt lỗi):* Chỉ báo lỗi khi đủ nghiêm trọng làm đứt mạch đọc; nếu chỉ là "có thể viết hay hơn chút xíu" $\rightarrow$ BẮT BUỘC ĐÁNH `PASS`.
- **Đầu ra:** `chapters/<chapter_id>/audit_verdict.md`.
- **Phân nhánh (Transitions):**
  - `PASS`: Đạt chuẩn $\rightarrow$ Chuyển sang `MEMORY_UPDATE` (Node 9).
  - `REVISE` (vòng sửa $< 3$): Chỉ định section và hành động đặc trị $\rightarrow$ Chuyển sang `SECTION_REVISION` (Node 6).
  - `REVISE` (vòng sửa $\ge 3$ hoặc `[PLATEAU]`): **Hard Stop Protocol (`ROUTE-006`)** $\rightarrow$ Dừng toàn bộ workflow, báo cáo khẩn cấp xin chỉ đạo tác giả.
  - `RESTRUCTURE`: Lỗi kiến trúc vĩ mô (từ 2 beat trở lên không có `new_for_reader` khác nhau, luận đề đứt gãy) $\rightarrow$ Quay lui về `BLUEPRINT` (Node 1) lập lại Card mới.

#### **Node 9: MEMORY_UPDATE (`node-09-memory-update.md`)**
- **Thực thi:** L0 Direct kết hợp CLI deterministic.
- **Lệnh thực thi cơ học:**
  1. Ghi nhận chống trùng lặp câu chuyện: `python .agents/scripts/memory_cli.py record-story-usage --id S-XXX --chapter <id> --section <sec> --angle "..." --function "..."`.
  2. Hợp nhất trạng thái chương: `python .agents/scripts/memory_cli.py update-continuity --state-file chapters/<id>/chapter_state.json`.
  3. Ghi nhận ý và hình ảnh đã dùng: `python .agents/scripts/memory_cli.py record-ideas-used --chapter <id> --ideas "..." --images "..."` (cập nhật `foundation/ideas_used.md`).
  4. Ghi mốc bản thảo phục vụ học hỏi: `python .agents/scripts/memory_cli.py record-draft-baseline --chapter <id>` (lưu bản sao vào `chapters/<id>/.baseline/`).
- **Cập nhật Markdown SSOT:** Ghi tóm tắt nhận thức vào `summaries.md`, bổ sung thuật ngữ vào `terms.md`, ghi nhật ký quyết định vào `decisions.md`.
- **Đầu ra:** Bộ nhớ sống đồng bộ $\rightarrow$ Chuyển sang `SPINE_CHECK` (Node 10).

#### **Node 10: SPINE_CHECK (`node-10-spine-check.md`)**
- **Thực thi:** `book-architect` nạp `spine-architecture`.
- **Hành động:** Rà soát xem chương vừa viết có làm lệch hướng mục lục tổng thể không. Nếu phát hiện lệch (`SPINE-FLAG`): tính toán bán kính ảnh hưởng (Blast Radius), tạo snapshot sao lưu và đề xuất cập nhật tối thiểu lên `book_spine.md`.
- **Kết quả:** Kết thúc chu kỳ sản xuất chương $\rightarrow$ Trạng thái `DONE`.

---

### 3.3. Giai Đoạn 3: Hợp Nhất, Đọc Mù & Xuất Bản (Book Assembly - 8 Nodes)
*Quy chuẩn:* `.agents/workflows/book-assembly.md`  
*Mục tiêu:* Hợp nhất toàn bộ các chương riêng lẻ thành bản thảo toàn cuốn, kiểm tra tính nhất quán vĩ mô, đọc mù độc lập và đóng gói xuất bản.

```
[Node 1: CONSISTENCY_PASS] (Terms, Promises, Summaries, Story usage audit)
       │
       ▼
[Node 2: ARGUMENT_THREAD_CHECK] (Dominos Leads-to thread verification)
       │
       ▼
[Node 3: TRANSITION_SMOOTHING] (Smooth chapter bridges: 00_open vs 04_close)
       │
       ▼
[Node 4: MANUSCRIPT_COMPILATION] (Deterministic compiler -> outputs/manuscript.md)
       │
       ▼
[Node 5: VOICE_AUDIT] (Read-only scan against voice.md -> voice_drift_report.md)
       │
       ▼
[Node 6: COLD_READ] (Absolute Blind Barrier -> outputs/cold_read_assessment.md)
       │
       ▼
[Node 7: GATE_4_FINAL] (Human Sovereign Gate: Option A Publish / Option B 1-Round Fix Queue)
       │
       ▼
[Node 8: EXPORT] (Packaging to PDF/EPUB -> DONE)
```

#### Các Chốt Chặn Trọng Yếu Trong Book Assembly:
1. **`MANUSCRIPT_COMPILATION` (Node 4):**
   - Chạy `python scripts/assemble_chapter.py --all --commit`.
   - Compiler tự động quét tất cả thư mục `chapters/*/draft.md`, kiểm tra tính đầy đủ, nối lại theo thứ tự số tự nhiên và sinh ra file duy nhất: `outputs/manuscript.md`.
2. **`VOICE_AUDIT` (Node 5):**
   - Quét chẩn đoán giọng văn toàn cục đối chiếu với `voice.md`.
   - **Quy tắc bất biến:** TUYỆT ĐỐI CẤM SỬA VĂN BẢN (Read-Only Scan). Chỉ sinh báo cáo `outputs/voice_drift_report.md`.
3. **`COLD_READ` (Node 6 - Layer 3 Quality Engine):**
   - **Hàng rào mù tuyệt đối (Absolute Blind Barrier):** `quality-auditor` ĐỌC DUY NHẤT file `outputs/manuscript.md`. CẤM ĐỌC `manifesto.md`, `book_spine.md`, `terms.md`, `summaries.md` hay bất kỳ ghi chú ý đồ nào.
   - Thẩm định qua **10 Giả thuyết đòn bẩy cao** (Transformation Payoff, Chapter Rent, Semantic De-duplication, Cognitive Escalation, Drop-off Danger Zones, Dinner Table Metric, Counter-Intuitive Reframe, Friction Contact, Insight Density, Ending Autonomy).
   - Đưa ra 4 phán quyết tư vấn: `Ship`, `Conditional`, `Major Revise`, `Kill`.
   - Sinh **Hàng đợi sửa chữa (Actionable Fix Queue)**: Tối đa 8 dòng ở cuối báo cáo theo cú pháp: `- Tên chương | Tiêu đề H2 | <mã_bệnh_học> | <targeted_action> | mô tả lỗi`.
4. **`GATE_4_FINAL` (Node 7 - Human Gate):**
   - Tác giả giữ quyền quyết định tối cao qua 2 lựa chọn:
     - **Lựa chọn A:** Xuất bản ngay.
     - **Lựa chọn B:** Sửa theo hàng đợi sửa chữa đúng 1 vòng duy nhất (sửa tuần tự từng file section, chạy lại linter, assemble lại chương, compile lại toàn sách) rồi quay lại Gate 4.
5. **`EXPORT` (Node 8):** Đóng gói bản thảo hoàn chỉnh, tạo ghi chú dàn trang PDF/EPUB.

---

## 4. CƠ CHẾ VẬN HÀNH & QUẢN TRỊ NGỮ CẢNH (CONTEXT & EXECUTION MECHANICS)

### 4.1. Ngân Sách Ngữ Cảnh Tĩnh (Context Budget Map)
Theo kiểm chứng thực tế tại `docs/context_budget_map.json` và script `scripts/context_budget.py`:
- **Always-On Baseline Tokens:** Khoảng **3,478 tokens** (gồm 2 rules: `authorship-contract.md` và `book-constitution.md`).
- **Phân bổ ngân sách theo từng Node (Tokens):**
  - Node 1 (`BLUEPRINT`): ~7,500 tokens (Agent Crafter + blueprinting skill + chapter_shapes).
  - Node 2 (`GOAL_LOCK`): ~4,200 tokens (Orchestrator + contract).
  - Node 3 (`EXCAVATION`): ~8,900 tokens (Crafter + story-enrichment + author-excavation + story-integrity).
  - Node 4 (`DRAFTING`): ~9,800 tokens (Crafter + drafting + humanizer + story-integrity + 4 blocks context).
  - Node 5 (`MECHANICAL_SCREEN`): **0 LLM Tokens** (Chạy script Python stdlib trực tiếp).
  - Node 6 (`REVISION`): ~7,800 tokens (Crafter + editorial-revision + rubric lỗi).
  - Node 7 (`ASSEMBLY`): **0 LLM Tokens** (Chạy script Python stdlib trực tiếp).
  - Node 8 (`REVIEW`): ~6,800 tokens (Auditor + quality-engine + draft + card + summaries).
  - Node 9 (`MEMORY_UPDATE`): **0 LLM Tokens** (Chạy script CLI và ghi file).
  - Node 10 (`SPINE_CHECK`): ~6,200 tokens (Architect + spine-architecture).

### 4.2. Hàng Rào Cách Ly Ngữ Cảnh (Context Isolation Barriers)

| Đối Tượng | Hàng Rào Được Thiết Lập | Mục Đích Kỹ Thuật |
| :--- | :--- | :--- |
| **`quality-auditor` (Layer 2 Chapter Review)** | **Blind to Intent, Informed on Manuscript:**<br>- ĐƯỢC ĐỌC: `draft.md`, `card.md`, `summaries.md`, `terms.md`, `voice.md`.<br>- CẤM ĐỌC: `manifesto.md`, `sources/`, `evidence_ledger.md`, chat logs. | Ngăn Auditor bị "thao túng tâm lý" bởi ý đồ của tác giả; chỉ đánh giá những gì thực sự hiển hiện trên trang giấy, nhưng vẫn phát hiện được lặp ý nhờ `summaries.md`. |
| **`quality-auditor` (Layer 3 Cold Read)** | **Absolute Blind Barrier:**<br>- ĐƯỢC ĐỌC: Duy nhất `outputs/manuscript.md`.<br>- CẤM ĐỌC: 100% tài liệu foundation, đề cương, card, chat logs. | Mô phỏng chính xác trải nghiệm của một độc giả bỏ tiền mua sách ngoài tiệm: không có cẩm nang giải thích đi kèm. |
| **`chapter-crafter` (Drafting & Revision)** | **Section-Local Isolation:**<br>- Chỉ tải section file đang viết/sửa.<br>- Cấm tải các section khác hoặc các chương ngoài phạm vi. | Chống hiện tượng trôi ngữ cảnh (Context Dilution), ngăn LLM tóm tắt vội vã làm hụt dung lượng từ. |

---

## 5. HỆ THỐNG KIỂM SOÁT CHẤT LƯỢNG 3 LỚP (QUALITY CONTROL ENGINE)

Đặc tả chi tiết từ `rules/quality-engine.md`:

```
┌────────────────────────────────────────────────────────────────────────┐
│              LAYER 1: MECHANICAL SCREEN (Binary Pass/Fail)             │
│  - 0 Gap Tokens ([PENDING:], [QUERY:], [AUTHOR:], [EVIDENCE-REQUEST:])  │
│  - 0 Raw Diagram Blocks (```mermaid, ```ascii)                         │
│  - 100% Unicode NFC & chuẩn khoảng trắng dấu câu                       │
│  - Chuẩn định dạng văn xuôi liên tục CONV-001 (0 lạm dụng bullet list) │
│  - Lọc sạch từ sáo rỗng translationese ("Hơn nữa", "Rõ ràng là")       │
│  - Provenance Check: 0 số liệu hoặc trích dẫn chưa có nguồn gốc        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ PASS (Exit code 0)
┌───────────────────────────────────▼────────────────────────────────────┐
│              LAYER 2: CHAPTER REVIEW (Dual-Lens Meso Audit)             │
│  - Lens A: Truth & Logic (Không ngụy biện, rõ điều kiện biên, Leads-to) │
│  - Lens B: Reader Experience (Nhịp điệu câu, chống lặp ý vi mô)        │
│  - Reader Progression Check: Phép thử đoán trước, LẶP Ý, NÓI QUÁ,     │
│    CHUNG CHUNG                                                         │
│  - Materiality Threshold (Quyền không bắt lỗi khi chưa đủ material)    │
│  - Bảng Diagnostic Rubric 15 bệnh học lâm sàng                         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ PASS (Toàn bộ các chương)
┌───────────────────────────────────▼────────────────────────────────────┐
│              LAYER 3: COLD READ (Absolute Blind Macro Audit)           │
│  - Đọc mù tuyệt đối manuscript.md (0 intent context)                   │
│  - 10 High-Leverage Hypotheses                                         │
│  - Phân tầng rủi ro định tính: LOW / MEDIUM / HIGH RISK                │
│  - 4 Editorial Verdicts: Ship / Conditional / Major Revise / Kill      │
│  - Actionable Fix Queue: Hàng đợi sửa tối đa 8 dòng                    │
└────────────────────────────────────────────────────────────────────────┘
```

### Bảng Tra Cứu 15 Bệnh Học Lâm Sàng (Diagnostic Pathologies Rubric)

| Mã Bệnh Học | Ống Kính (Lens) | Bản Chất Lỗi Nhìn Từ Độc Giả | Hành Động Đặc Trị Chỉ Định |
| :--- | :---: | :--- | :--- |
| `THESIS_EXPOSITION` | Lens A | Giải thích lý thuyết trừu tượng quá sớm thay vì kéo người đọc qua trải nghiệm. | `EXPERIENCE_REWRITE`: Kéo mở đoạn về tình huống hiện trường cụ thể. |
| `PREMISE_LEAP` | Lens A | Nhảy cóc tiền đề lập luận ($A \rightarrow C$ thiếu $B$), hụt chân logic. | `INSERT_BRIDGE`: Thêm 1–2 câu làm rõ tiền đề trung gian. |
| `UNCHECKED_ABSOLUTE` | Lens A | Khẳng định tuyệt đối thiếu điều kiện biên ("luôn luôn", "chắc chắn"). | `QUALIFY_BOUNDS`: Thêm ngữ cảnh áp dụng thực tế ("trong trường hợp này"). |
| `STRAWMAN_ATTACK` | Lens A | Phê phán quan điểm đối thủ một cách hời hợt, hạ thấp độc giả. | `STEELMAN_REVISE`: Dựng lại phản đề mạnh nhất của đối thủ trước khi phản biện. |
| `UNGROUNDED_EVIDENCE` | Lens A | Đưa ra số liệu hoặc trích dẫn thiếu căn cứ thực nghiệm. | `FLAG_EVIDENCE_GAP`: Gắn cờ yield hoặc cắt bỏ. |
| `RECOGNITION_REDUNDANCY` | Lens B | Lặp ý: Giải thích lại điều người đọc đã hiểu ở section/chương trước. | `DEDUP_CUT`: Cắt bỏ đoạn lặp, nén thành 1 mỏ neo ngắn $\le 2$ câu. |
| `CADENCE_MONOTONY` | Lens B | Nhịp điệu phẳng lặng: Các câu có độ dài đều đều ru ngủ người đọc. | `EAR_TEST_REWRITE`: Xen kẽ câu cực ngắn đanh thép với câu dài trầm lắng. |
| `VERBOSITY_DILUTION` | Lens B | Dài dòng, lạm dụng tính từ làm loãng tư tưởng cốt lõi. | `COMPRESSION_PRUNING`: Áp dụng Zinsser cut $\ge 20\%$ số từ thừa. |
| `SELF_HELP_VOICE` | Lens B | Giọng điệu sáo rỗng, hô khẩu hiệu dạy đời ("Hãy nhớ rằng", "Bứt phá"). | `VOICE_RECALIBRATION`: Đổi sang giọng điềm đạm, ngồi cạnh người đọc. |
| `SUDDEN_PIVOT` | Lens B | Chuyển ý đột ngột giữa hai đoạn văn không có liên kết tâm lý. | `INSERT_TRANSITION`: Thêm câu chuyển mạch tự nhiên. |
| `CLIMAX_INFLATION` | Lens B | Nhiều đoạn gồng mình làm cao trào, làm mất sức nặng của nhịp PEAK thật. | `DE_ESCALATE`: Hạ giọng các đoạn phụ, giữ độc quyền cho beat PEAK. |
| `ANECDOTE_DISCONNECT` | Lens B | Kể chuyện đời thực xong không rút ra được đòn bẩy nhận thức nào. | `ANCHOR_INSIGHT`: Rút ra bài học và liên kết trực tiếp vào luận điểm. |
| `OVER_GENERALIZATION` | Progression | Khẳng định tổng quát về con người ở beat có ít hơn 2 anchors. | `QUALIFY_BOUNDS`: Giới hạn trong phạm vi trường hợp cụ thể. |
| `AWKWARD_AI_PROSE` | Formatting | Mắc các mẫu câu công thức AI (staging, triads, not-X-but-Y). | `HUMANIZER_POLISH`: Khử cấu trúc máy móc, tái cấu trúc câu tự nhiên. |
| `FORMATTING_FRICTION` | Formatting | Lạm dụng bôi đậm, dấu gạch ngang em-dash, chia nhỏ đoạn giật cục. | `SYNTACTIC_REANCHOR`: Phẫu thuật dấu câu, đưa về khối văn xuôi CONV-001. |

---

## 6. BẰNG CHỨNG TRIỂN KHAI THỰC TẾ (CODE & CONTRACT EVIDENCE)

### 6.1. Bằng Chứng Mã Lệnh (Script & CLI Implementations)

1. **Khử Lỗi Cơ Học & Tăng Biến Đếm Revision (`scripts/repair_invariants.py`):**
   - *Dòng 34–46:* Bộ Regex chuẩn quét 11 mẫu gap tokens (`GAP_PATTERNS`).
   - *Dòng 49–61:* Danh sách 11 cụm từ Megaphone Clichés bị cấm triệt để (`MEGAPHONE_CLICHES`).
   - *Dòng 320–350:* Hàm `--step-revision` đọc trường `revision_round: N/3` từ frontmatter của `card.md`. Nếu $N < 3$, tăng thành $(N+1)/3$ (exit code 0); nếu $N \ge 3$, trả về exit code 2 (ngắt mạch lặp).
2. **Kiểm Tra Nguồn Gốc Số Liệu & Trích Dẫn (`.agents/scripts/memory_cli.py`):**
   - *Hàm `cmd_check_provenance` (dòng 865–975):* Quét toàn bộ các số có $\ge 2$ chữ số (ngoại trừ số thứ tự chương/section) và các đoạn trích dẫn trong ngoặc kép $\ge 5$ từ. Đối chiếu tự động với `story_bank.md`, `card.md`, `terms.md`, `evidence_ledger.md`. Nếu phát hiện chi tiết chưa có nguồn, in danh sách và thoát mã 3.
3. **Cơ Chế Trích Xuất Bối Cảnh Viết 4 Khối (`.agents/scripts/memory_cli.py`):**
   - *Hàm `cmd_get_writing_context` (dòng 720–850):* Trích xuất chính xác 4 khối bối cảnh sạch:
     - `=== CUOI_CHUONG_TRUOC ===`: 1–2 đoạn cuối của chương liền trước.
     - `=== TOM_TAT_CHUONG_TRUOC ===`: Tóm tắt nhận thức từ `summaries.md`.
     - `=== PHAN_HOI_TAC_GIA ===`: Bài học từ `feedback.jsonl` hoặc `style_drift.md`.
     - `=== Y_DA_DUNG ===`: Danh sách ý và hình ảnh từ `foundation/ideas_used.md` (loại trừ chương hiện tại).
4. **Trọng Trọng Token Của Always-On Rules (`tests/test_rule_consolidation.py`):**
   - *Dòng 31–49:* Test `test_always_on_rules_footprint_budget` kiểm chứng rằng **duy nhất 2 file** (`authorship-contract.md` và `book-constitution.md`) mang `trigger: always_on`, và tổng dung lượng của chúng bắt buộc **$\le 12,288$ bytes (12KB)**.

### 6.2. Hiện Trạng Kiểm Thử (Test Suite Status)
Hệ thống hiện sở hữu **153 unit tests** tự động, bao phủ toàn bộ các mặt:
- `test_fsm_integrity_and_bounds.py`: Đảm bảo FSM không có trạng thái mồ côi và vòng lặp có chặn trên.
- `test_card_v3_schema.py`: Kiểm chứng schema Card v3, 5 chapter shapes, Beat Map có `new_for_reader` và `anchor`.
- `test_quality_auditor_suite.py`: Kiểm chứng toàn bộ các chốt chặn Node 4, 8, 9 và hàng đợi Cold Read.
- `test_memory_cli_extensions.py`: Kiểm chứng 15 lệnh của CLI bộ nhớ.
- Toàn bộ 153 tests đều đang vượt qua (`PASS`) với 0 lỗi.

---

## 7. CÁC ĐIỂM BẤT THƯỜNG, ĐỨT GÃY & RỦI RO ĐÃ XÁC MINH

Dưới đây là các phát hiện quan trọng sau quá trình reverse-engineering thực tế, phân định rạch ròi giữa **Hiện Tượng Đã Xác Minh** và **Rủi Ro Hệ Thống**:

### 7.1. Bất Thường 1: Xung Đột Vị Trí Script (Path Inconsistency)
- **Hiện tượng xác minh:** 
  - Trong `ARCHITECTURE.md` và một số workflow cũ, các lệnh thực thi được viết là `python scripts/assemble_chapter.py` và `python scripts/repair_invariants.py`. Thư mục này nằm tại thư mục gốc (`./scripts/`).
  - Trong khi đó, CLI bộ nhớ lại nằm tại `./.agents/scripts/memory_cli.py`.
  - Trong tài liệu trước đây từng có chỗ ghi nhầm thành `python .agents/scripts/assemble_chapter.py`, gây ra lỗi `FileNotFoundError` khi agent chạy lệnh từ bash.
- **Mức độ rủi ro:** Trung bình (Gây gãy lệnh tự động nếu agent mới suy đoán sai đường dẫn).

### 7.2. Bất Thường 2: Xung Đột Kiến Trúc Story Vault (SSOT vs Book Local Desync)
- **Hiện tượng xác minh:**
  - `ARCHITECTURE.md` §5.1 quy định: Hệ thống áp dụng mô hình 3 tầng: Single Canonical Vault duy nhất tại `.agents/memory/experience/story_bank.md`. Từng cuốn sách KHÔNG ĐƯỢC CÓ `story_bank.md` riêng, mà chỉ duy trì `story_projections.md` trỏ mã `ref_id`.
  - **Thực tế trên đĩa:** Cả hai dự án sách thật (`Books/lam-it-duoc-nhieu/foundation/` và `Books/nhan-danh-dieu-vi-dai/foundation/`) đều sở hữu một tệp `story_bank.md` đồ sộ độc lập, đồng thời có thêm `story_bindings.md`.
  - Khi cập nhật câu chuyện (Node 3 hoặc Genesis), dữ liệu được ghi vào `Books/<slug>/foundation/story_bank.md`, trong khi System Vault `.agents/memory/experience/story_bank.md` có nguy cơ bị bỏ quên hoặc lệch pha nội dung (Desynchronization).
- **Mức độ rủi ro:** Cao (Lệch pha nguồn sự thật lịch sử của tác giả giữa các cuốn sách).

### 7.3. Bất Thường 3: Trần Cứng Dung Lượng Rules (Budget Bottleneck)
- **Hiện tượng xác minh:**
  - Test suite `test_rule_consolidation.py` cưỡng chế cứng: `authorship-contract.md` + `book-constitution.md` $\le 12,288$ bytes.
  - Hiện tại, hai file này đã chiếm xấp xỉ 11.5KB. 
  - Bất kỳ ai muốn bổ sung thêm quy tắc hợp tác, ràng buộc an toàn hay hướng dẫn mới vào 2 file này đều sẽ lập tức kích hoạt lỗi CI và làm gãy test suite.
- **Mức độ rủi ro:** Cao (Ngăn cản việc mở rộng quy chuẩn lõi nếu không tái cấu trúc bài test).

### 7.4. Bất Thường 4: Giả Định "Context Reset" vs Thực Tế Môi Trường IDE Assistant
- **Hiện tượng xác minh:**
  - Kiến trúc quy định nguyên tắc `SEQ-006`: Mỗi lần chuyển vai (`orchestrator` $\rightarrow$ `crafter` $\rightarrow$ `auditor`), agent phải thực hiện **Clean Activation & Context Reset** (xóa sạch bộ nhớ đệm suy luận cũ để tránh rò rỉ ý đồ).
  - **Thực tế:** Khi hệ thống chạy inline trong một phiên làm việc duy nhất của AI coding assistant (như session hiện tại), toàn bộ lịch sử trò chuyện, các bản nháp trước đó và các tranh luận đều nằm nguyên trong context window. Không có cơ chế native nào của IDE tự động xóa trắng context giữa các node ngoại trừ việc khởi tạo subagent mới hoặc chờ context window bị nén (compaction).
  - Điều này dẫn đến nguy cơ Auditor bị "nhiễm bối cảnh" (Context Contamination), không còn giữ được tính độc lập khách quan tuyệt đối như thiết kế.
- **Mức độ rủi ro:** Rất cao (Làm suy giảm tính độc lập của Layer 2 và Layer 3).

### 7.5. Bất Thường 5: Khoảng Cách Giữa "Đạt Tiêu Chuẩn Linter" Và "Trải Nghiệm Đọc 10/10"
- **Hiện tượng xác minh (Case Study Chương 2 `lam-it-duoc-nhieu`):**
  - Section `00_open.md` ban đầu vượt qua 100% kiểm tra cơ học của Layer 1 (0 gap tokens, đúng heading H2, đúng CONV-001, provenance sạch), và thậm chí vượt qua cả kiểm định Layer 2.
  - Tuy nhiên, khi tác giả trực tiếp đọc, phản hồi nhận được là: *"quá tệ =))"* và *"ông chỉ biết màu mè câu chữ?"*.
  - **Nguyên nhân cốt lõi:** Linter và Auditor hiện tại bắt rất tốt các lỗi hình thức (format, chính tả, gap tokens, ngụy biện logic sơ đẳng), nhưng **chưa đo lường được tỷ lệ $\frac{\text{Value}}{\text{Total Cost}}$** của trải nghiệm đọc:
    - *Total Cost cao:* Văn phong tiểu luận học thuật (AI-essay), xưng "Ta" giáo điều, phân tích tâm lý lý thuyết, dạo đầu dông dài làm tiêu tốn năng lượng nhận thức của độc giả.
    - *Value thấp:* Thiếu các mô hình tư duy đắt giá (Mental Models như của Dan Koe), thiếu các cú bẻ gãy trực giác (Aha moments), và thiếu sự chân thành, cụ thể, tự trào kéo người đọc ngồi cạnh (như của FuSuSu hay Hormozi).
  - Hệ thống dễ tạo ra văn bản "đúng quy chuẩn kỹ thuật nhưng vô hồn và nhàm chán", nhầm lẫn giữa việc trau chuốt tính từ với việc kiến tạo chiều sâu nhận thức.
- **Mức độ rủi ro:** Chí mạng (Ảnh hưởng trực tiếp đến giá trị thương mại và sự đón nhận của độc giả thực tế).

### 7.6. Bất Thường 6: Rủi Ro Lệch Pha Baseline Khi Tác Giả Sửa Tay Trực Tiếp Trong Sections
- **Hiện tượng xác minh:**
  - Cơ chế học hỏi từ sửa tay (`check-draft-diff` tại Node 1) so sánh bản sao lưu `.baseline/draft.md` với `draft.md` hiện tại.
  - Nếu tác giả sửa tay trực tiếp trong các tệp `chapters/<id>/sections/*.md` (đúng theo nguyên tắc Modular Section SSOT) nhưng chưa chạy lệnh `assemble_chapter.py`, tệp `draft.md` vẫn giữ nguyên nội dung cũ.
  - Khi đó, lệnh `check-draft-diff` sẽ báo: "không có thay đổi" (False Negative), và toàn bộ các bài học/phản hồi quý giá từ tác giả sẽ bị bỏ sót, không được ghi vào `feedback.jsonl`.
- **Mức độ rủi ro:** Trung bình (Làm đứt gãy vòng lặp tự học hỏi của hệ thống).

---

## KẾT LUẬN & HƯỚNG DẪN CHO AGENT KẾ TIẾP

Tài liệu này xác nhận rằng Writing Agent Kit là một hệ thống có kiến trúc FSM và quản trị SSOT cực kỳ chặt chẽ, kỷ luật kiểm định 3 lớp rõ ràng và khả năng vận hành deterministic đáng tin cậy. 

Tuy nhiên, điểm nghẽn lớn nhất của hệ thống hiện tại không nằm ở tầng cơ học (Mechanical/Pipeline), mà nằm ở **tầng triết lý sáng tác và thiết kế trải nghiệm đọc**: làm thế nào để bản thảo không chỉ vượt qua các bài test linter, mà phải đạt chuẩn **10/10 Unputdownable** — nơi chi phí nhận thức của độc giả được đè bẹp xuống 0 và giá trị tư duy được đẩy lên cực đại.

Bất kỳ đề xuất nâng cấp nào trong tương lai cần tập trung giải quyết 6 điểm bất thường nêu trên mà không làm phá vỡ các hợp đồng kiến trúc bất biến của hệ thống.
