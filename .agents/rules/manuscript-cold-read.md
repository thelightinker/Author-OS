---
name: manuscript-cold-read
version: 1.0.0
priority: P1
trigger: model_decision
domain: publishing-audit
description: "Quy chuẩn kiểm định độc lập toàn sách (Whole-Book Cold Read) và chẩn đoán giọng văn (Voice Drift Scan): Hàng rào đọc mù tuyệt đối (Absolute Blind Barrier), 10 giả thuyết thẩm định đòn bẩy cao, phân tầng rủi ro định tính và 4 phán quyết ấn hành."
tags: [cold-read, whole-book, publishing-audit, reader-advocacy]
---

# Rule: Manuscript Cold Read & Whole-Book Audit (Kiểm Định Toàn Cục Bản Thảo)

> "Đóng vai người mua sách bỏ ra 200,000 VNĐ và 6 tiếng cuộc đời. Đọc mù tuyệt đối từ trang đầu đến trang cuối — không định kiến, không khoan nhượng, chỉ bảo vệ giá trị thực sự mà độc giả nhận được."

---

## 📌 Phân loại Trigger
- **`stage_loaded`**: Được kích hoạt có định hướng bởi `quality-auditor` trong giai đoạn tổng hợp và đóng gói xuất bản bản thảo ([book-assembly.md](../workflows/book-assembly.md)).

---

## 1. Hàng Rào Đọc Mù Tuyệt Đối (Absolute Blind Barrier - `SEQ-006`)

Khi tiến hành kiểm định Layer 3 (Whole-Book Cold Read Mode):
- **ĐƯỢC NẠP**: DUY NHẤT file bản thảo hợp nhất `outputs/manuscript.md`.
- **CẤM NẠP TUYỆT ĐỐI**:
  - `book_spine.md`, `terms.md`, `summaries.md`, `manifesto.md`.
  - Toàn bộ ghi chú ý đồ, transcript genesis hay scratchpad của tác giả.
- **Tâm thế thẩm định**: Độc giả mua sách ngoài tiệm sách, không biết tác giả *định nói gì*, chỉ phán xét những gì *thực tế đã hiển hiện trên trang giấy*.

---

## 2. 10 Giả Thuyết Thẩm Định Đòn Bẩy Cao (10 High-Leverage Non-Fiction Hypotheses)

Auditor rà soát bản thảo toàn cục theo 10 câu hỏi cốt tử:

1. **Transformation Payoff (Trả nợ cam kết)**:
   - Lời hứa cốt lõi ở Lời mở đầu có được trả nợ trọn vẹn ở trang cuối cùng không? Độc giả có đạt được sự chuyển hóa nhận thức như đã hứa?
2. **Chapter Rent (Tiền thuê nhà của từng chương)**:
   - Mỗi chương có tự trả tiền thuê nhà cho chính nó không? Nếu cắt bỏ một chương bất kỳ, cấu trúc cuốn sách có bị sụp đổ không?
3. **Whole-Book Semantic De-duplication (Chống lặp nhận thức toàn sách)**:
   - Có chương nào đang loay hoay khám phá lại điều mà chương trước đã chứng minh và chốt xong không?
4. **Cognitive Escalation (Mạch leo thang nhận thức)**:
   - Tải nhận thức có tăng tiến mượt mà từ nền tảng đến chuyên sâu, hay bị đứt gãy, chững lại giữa chừng?
5. **Drop-Off Danger Zones (Vùng trũng bỏ đọc)**:
   - Độc giả có nguy cơ buông sách ở đâu nhất (đặc biệt là vùng nguy hiểm ở 40%–60% cuốn sách)?
6. **The Dinner Table Metric (Khả năng truyền miệng)**:
   - Người đọc có thể tóm tắt và say sưa kể lại luận đề cốt lõi của cuốn sách cho bạn bè trong 2 phút trên bàn ăn không?
7. **Counter-Intuitive Reframe (Góc nhìn phản trực giác)**:
   - Cuốn sách có ít nhất 2–3 góc nhìn bẻ gãy lối mòn tư duy thông thường, tạo khoảnh khắc "Aha!" đáng nhớ không?
8. **Friction & Reality Contact (Va chạm thực tế)**:
   - Tác giả có dự phóng và giải quyết những rào cản, ma sát tâm lý và trở ngại khi người đọc áp dụng giải pháp vào đời sống không?
9. **Insight Density (Mật độ đòn bẩy nhận thức)**:
   - Mật độ giá trị nhận thức trên mỗi 1,000 từ có đủ đậm đặc không? Có phần nào bị loãng, dài dòng hay kể lể thừa thãi?
10. **Ending Payoff & Autonomy (Cái kết trao quyền)**:
    - Phần kết có giải phóng độc giả và trao quyền tự chủ hành động trọn vẹn, hay biến thành bài giảng đạo đức gượng ép?

---

## 3. Phân Tầng Rủi Ro Định Tính & 4 Phán Quyết Ấn Hành

### Phân tầng Rủi ro Định tính (Qualitative Risk Tiers)
- **LOW / MEDIUM / HIGH RISK**: Mọi kết luận phải gắn liền với trích dẫn hiện trường cụ thể.
- **Nguyên tắc cấm**: Tuyệt đối cấm đưa ra các chỉ số giả định (pseudo-metrics) thiếu cơ sở thực nghiệm (như "8.5/10", "78% completion rate").

### 4 Phán Quyết Biên Tập Tư Vấn (Advisory Verdicts)
| Phán quyết | Tiêu chuẩn chất lượng | Hành động tiếp theo |
|:---|:---|:---|
| **Ship** | Bản thảo hoàn thiện xuất sắc, lập luận chặt chẽ, nhịp điệu cuốn hút, thông điệp sắc bén. | Chuyển sang đóng gói xuất bản ([Export](../workflows/book-assembly.md)). |
| **Conditional** | Ý tưởng xuất sắc, chỉ vấp phải một số ma sát cục bộ ở các đoạn chuyển tiếp liên chương. | Chỉnh sửa cục bộ các section chỉ định trước khi xuất bản. |
| **Major Revise** | Lập luận đứt gãy ở quy mô khối, một số chương chưa tự trả tiền thuê nhà, lặp nhận thức. | Tái cấu trúc lại một số chương mục trọng yếu. |
| **Kill** | Luận đề cốt lõi không đứng vững trong toàn bộ trải nghiệm đọc, thiếu tính thực tiễn và tính mới. | Khuyến nghị tác giả định hình lại luận đề nền tảng. |

---

## 4. Quét Chẩn Đoán Giọng Văn Toàn Bản Thảo (Voice Audit Scan)

- **Thời điểm**: Kích hoạt tại Node `VOICE_AUDIT` của `book-assembly.md` trước khi tiến hành Cold Read.
- **Thực thi**: `chapter-crafter` thực hiện chế độ **Read-Only Scan** toàn bộ các chương đối chiếu với `.agents/memory/author/voice.md`.
- **Ranh giới bất biến**:
  - Tuyệt đối cấm sửa đổi bản thảo trong quá trình quét giọng văn.
  - Xuất báo cáo độc lập `outputs/voice_drift_report.md` chỉ rõ các vị trí bị trôi giọng, lạm dụng sáo ngữ hoặc lệch nhịp thở của tác giả.
