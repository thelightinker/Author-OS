# Node 10: SPINE_CHECK

- **Vai trò thực thi**: `book-architect` nạp skill `spine-architecture`.
- **Mục tiêu**:
  - Kiểm tra xem nội dung thực tế vừa viết có làm lệch hướng hoặc phát sinh nhu cầu điều chỉnh cho các chương tiếp theo không.
  - Nếu phát hiện lệch (`SPINE-FLAG`): Kích hoạt `spine-architecture` tính toán Blast Radius, tạo snapshot dự phòng và đề xuất cập nhật tối thiểu lên `book_spine.md`.
- **DoD**: Hoàn tất chu kỳ sản xuất chương, xác nhận mạch Leads-to sẵn sàng cho chương kế tiếp.
- **Transition Path**: `SPINE_CHECK` $\rightarrow$ `DONE`.
