---
# Card v3: Reader Journey Architecture Schema
chapter_id: "{{CHAPTER_ID}}"
card_version: 1
status: draft # [draft | approved]
shape: story-unpack-apply # [story-unpack-apply | myth-bust | problem-turn-practice | question-journey | contrast-pair]
budget_words_max: 3500
revision_round: 0
story_bank_ids: [{{STORY_BANK_IDS}}]
---

# Chapter Card: {{CHAPTER_TITLE}}

## 1. Reader Promise (Lời hứa với độc giả — 1 câu duy nhất)
{{ONE_SENTENCE_READER_PROMISE}}

## 2. Entry State -> Exit State (Biên độ chuyển dịch nhận thức)
- **Vào chương:** Độc giả đang tin, cảm thấy hoặc bế tắc ở điều gì: {{ENTRY_STATE}}
- **Ra khỏi chương:** Độc giả thấu suốt, sở hữu được góc nhìn hoặc công cụ gì mới: {{EXIT_STATE}}

## 3. Core Insight (Tư tưởng cốt lõi từ insight_brief.md)
- {{CORE_INSIGHT_STATEMENT}}

## 4. Argument Arc (Trục lập luận xuyên suốt)
Claim cốt lõi ➔ Vì sao điều này không hiển nhiên ➔ Dữ liệu / Trải nghiệm chứng minh ➔ Phản biện mạnh nhất (Steelman) ➔ Giải quyết & Chuyển hóa hành động.

## 5. Beat Map (Bản đồ nhịp đọc — Tối đa 1 beat PEAK duy nhất)
| beat | role | new_for_reader (giá trị mới cho người đọc) | anchor (chỗ dựa) | ~words |
|:---|:---|:---|:---|:---|
| b1 | hook | Nhận ra vấn đề hiện tại không như mình tưởng | {{STORY_ID_OR_QUOTE}} | 300 |
| b2 | tension | Bế tắc sâu hơn khi giải pháp thông thường phá sản | none | 500 |
| b3 | turn (PEAK) | Cú huých nhận thức giải phóng tư duy | insight_brief §Core | 700 |
| b4 | unpack | Bóc tách cơ chế và công thức đòn bẩy | none | 600 |
| b5 | close | Neo bài học và mở vết nứt nhân quả sang chương sau | domino_leads_to | 400 |

## 6. Section Breakdown & Soft Destination Locks (Đích Đến Mềm & Loại Trừ Có Lý Do)
- **00_open.md** [type: Narrative | Analytical | Conceptual | Research]:
  - `intended_destination`: {{SECTION_00_INTENDED_DESTINATION}}
  - `out_of_scope`: {{SECTION_00_OUT_OF_SCOPE}}
- **01_sec1.md** [type: Narrative | Analytical | Conceptual | Research]:
  - `intended_destination`: {{SECTION_01_INTENDED_DESTINATION}}
  - `out_of_scope`: {{SECTION_01_OUT_OF_SCOPE}}
- **02_sec2.md** [type: Narrative | Analytical | Conceptual | Research]:
  - `intended_destination`: {{SECTION_02_INTENDED_DESTINATION}}
  - `out_of_scope`: {{SECTION_02_OUT_OF_SCOPE}}
- **04_close.md** [type: Narrative | Analytical | Conceptual | Research]:
  - `intended_destination`: {{SECTION_04_INTENDED_DESTINATION}}
  - `out_of_scope`: {{SECTION_04_OUT_OF_SCOPE}}

## 7. Knowledge References (Tối đa 3 units)
- {{KNOWLEDGE_REF_1}}
- {{KNOWLEDGE_REF_2}}

## 8. Open Gaps (Khoảng trống cần xử lý)
- [ ] {{GAP_1}}
