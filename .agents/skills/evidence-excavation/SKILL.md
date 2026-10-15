---
name: evidence-excavation
description: "Khảo sát và xử lý tư liệu thực nghiệm: Quét tài liệu thô trong sources/raw/, phân loại 5 cấp bậc nguồn, trích xuất ghi chú đã kiểm chứng sang sources/notes/, cập nhật sổ bộ chứng cứ evidence_ledger.md và thực thi quy trình leo thang luận điểm 4 bước khi giải quyết yêu cầu evidence_request.md. Kích hoạt khi triage nguồn tư liệu hoặc xử lý lỗ hổng dữ liệu."
when_to_use: "Khi xử lý tài liệu nguồn trong pha Genesis, lập sổ bộ evidence_ledger.md hoặc khi nhận bàn giao khoảng trống chứng cứ [EVIDENCE-REQUEST] từ Chapter Crafter."
allowed-tools: [Read, Write, Edit, Glob, Grep]
version: 1.0.0
---

# Evidence Excavation: Khảo Sát Chứng Cứ & Liêm Chính Dữ Liệu Thực Nghiệm

> "Một luận điểm dù sắc sảo đến đâu cũng sẽ sụp đổ nếu dựa trên một con số bịa đặt. Uy tín của một cuốn sách phi hư cấu nghiêm túc nằm ở tính minh bạch và độ tin cậy của kho dữ liệu đằng sau nó."

---

## 1. Quy Trình Khảo Sát Nguồn (Source Triage Workflow)

1. **Tiếp nhận tài liệu thô (`sources/raw/`)**:
   - Quét tài liệu định dạng PDF, Markdown, bài nghiên cứu hoặc bài phỏng vấn.
2. **Phân loại 5 cấp bậc nguồn (5-Tier Source Hierarchy)**:
   - **Tier 1**: Bài báo khoa học có bình duyệt (PubMed, IEEE, Nature), báo cáo thống kê chính phủ (Tổng cục Thống kê, World Bank).
   - **Tier 2**: Sách nghiên cứu chuyên khảo từ các nhà xuất bản uy tín (Harvard Business Review Press, MIT Press, Routledge).
   - **Tier 3**: Dữ liệu thực nghiệm hoặc nhật ký lâm sàng trực tiếp từ tác giả.
   - **Tier 4**: Báo chí điều tra kinh tế/xã hội chính thống (Financial Times, The Economist).
   - **Tier 5**: Bài viết cá nhân, blog, bài PR — **CẤM DÙNG** làm nguồn chứng minh luận đề cốt lõi.
3. **Chiết xuất ghi chú có kiểm chứng (`sources/notes/<slug>.md`)**:
   - Ghi lại: Tên nghiên cứu, tác giả, năm công bố, cỡ mẫu ($N$), phương pháp, trích dẫn nguyên văn và kết luận chính xác.

---

## 2. Ghi Chép Vào Sổ Bộ Chứng Cứ (`evidence_ledger.md`)

Mỗi bằng chứng được mã hóa định danh `EV-XXX` trong `evidence_ledger.md` với schema:
- **ID**: `EV-001`
- **Claim**: Luận điểm cuốn sách đang khẳng định.
- **Source**: Tên tác giả, năm, tên nghiên cứu, DOI / URL.
- **Tier**: Tier 1 đến Tier 3.
- **Confidence**: High / Medium / Low.
- **Scope Limit**: Giới hạn của nghiên cứu (ví dụ: "chỉ thử nghiệm trên nhóm tuổi 20-30 tại Mỹ, không suy diễn cho toàn nhân loại").
- **Mapped Sections**: `["ch_02/01_sec1.md"]`.

---

## 3. Quy Trình Leo Thang Luận Điểm 4 Bước (Claim Escalation Protocol)

Khi nhận file `chapters/<id>/evidence_request.md` từ Crafter:
1. `Resolve (Giải quyết)`: Tìm thấy nghiên cứu Tier 1–2 $\rightarrow$ Bổ sung vào `evidence_ledger.md`, phản hồi cho Crafter trích dẫn chuẩn xác.
2. `Reframe (Tái định khung)`: Không có nghiên cứu vĩ mô, nhưng tác giả có kinh nghiệm thực tế $\rightarrow$ Đổi câu từ: *"Các nghiên cứu chứng minh..."* thành *"Qua hơn 10 năm tư vấn cho 200 doanh nghiệp, tôi nhận thấy..."*.
3. `Soften (Làm mềm)`: Dữ liệu chưa đủ mạnh $\rightarrow$ Dùng ngôn từ thận trọng: *"Dữ liệu ban đầu gợi ý rằng..."*, *"Một số trường hợp điển hình cho thấy..."*.
4. `Cut (Cắt bỏ)`: Luận điểm sai lệch, ngụy biện hoặc hoàn toàn không có cơ sở $\rightarrow$ Chỉ đạo Crafter cắt bỏ hoàn toàn để bảo vệ uy tín cuốn sách.

---

## 4. Ví Dụ Cụ Thể (Few-Shot Example)

### Input (`evidence_request.md` từ Crafter):
```
Yêu cầu: Crafter đang viết đoạn: "90% người khởi nghiệp thất bại trong 3 năm đầu vì thiếu vốn lưu động." Cần tìm nguồn xác thực số liệu này.
```

### Xử lý & Output:
```markdown
# Phản hồi Evidence Request: req_01

## 1. Kết Quả Khảo Sát
- Nghiên cứu từ Cục Quản lý Doanh nghiệp Nhỏ (SBA) và CB Insights cho thấy: Khoảng 20% doanh nghiệp thất bại trong năm đầu, 50% sau 5 năm. Nguyên nhân hàng đầu là "Không có nhu cầu thị trường" (42%), thiếu vốn chỉ đứng thứ hai (29%).
- Con số "90% thất bại trong 3 năm vì thiếu vốn" là một huyền thoại truyền miệng vô căn cứ.

## 2. Quyết Định Leo Thang Luận Điểm (Escalation Action: Reframe & Resolve)
- **Mã nguồn mới**: `EV-014` (CB Insights Startup Failure Report).
- **Chỉ thị sửa đổi cho Crafter**:
  - Không dùng câu khẳng định 90%.
  - Sửa thành: *"Dữ liệu từ CB Insights chỉ ra rằng gần một nửa số startup đóng cửa không phải vì cạn tiền trước tiên, mà vì họ tạo ra thứ thị trường không hề cần. Thiếu vốn chỉ là triệu chứng bề mặt của một căn bệnh sâu hơn: xây dựng sản phẩm trong ảo tưởng."*
```

---

## 5. Tiêu Chuẩn Nghiệm Thu

- [ ] Mọi luận điểm mang tính khẳng định khoa học phải có mã `EV-XXX` trong `evidence_ledger.md`.
- [ ] 0 nguồn trích dẫn thuộc Tier 5 làm trụ cột cho luận điểm chính.
- [ ] Phản hồi `evidence_request.md` minh bạch, có chỉ thị rõ ràng (Resolve/Reframe/Soften/Cut).

---

## Related Skills

| Skill | Khi nào dùng |
|---|---|
| `chapter-drafting` | Tiếp nhận yêu cầu khảo sát chứng cứ từ file `evidence_request.md` và trả về phương án xử lý (Resolve/Reframe/Soften/Cut). |
| `falsification-steelmanning` | Cung cấp dữ liệu thực nghiệm và giới hạn phạm vi nghiên cứu để kiểm tra sức chịu tải của luận đề. |
