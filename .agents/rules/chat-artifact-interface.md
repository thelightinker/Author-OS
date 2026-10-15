---
trigger: manual
description: "Chat tối giản (Status → Evidence → Next step), khi nào persist ra file, workspace deep-work Books/<book_slug>/, vòng đời artifact, Execution Badge và minh bạch bằng chứng. Quy định cách chuyển thông tin giữa chat và file, không quy định quyền quyết định hay routing."
---

# Rule: Communication ↔ Artifact

> Chat ngắn. Deep work nằm trong file. Mọi tuyên bố đều có bằng chứng.

## Ownership

- **Sở hữu:** format & ngân sách chat · ma trận Chat vs Artifact · vòng đời artifact · cách hiển thị file · Execution Badge · minh bạch.
- **Chỉ tham chiếu, không định nghĩa lại:**
  - Cấu trúc thư mục chuẩn → `ROUTE-003`.
  - Quyền quyết định, khi nào hỏi/dừng, cách hỏi → `human-agent-collaboration`.
  - Nội dung/schema các file sổ bộ → Memory (Architecture §5).
  - Phán quyết kiểm định → Quality Engine (Architecture §7).

## COMM-001 · Hai tầng

- **Chat:** giao tiếp.
- **Workspace `Books/<book_slug>/`:** 100% deep work (`foundation/`, `chapters/`, audit, `outputs/`).

## COMM-002 · Ngân sách chat & format

Mặc định ≤ 10 dòng; tối đa 15 dòng khi trình quyết định chiến lược. Dòng đầu là badge (nếu có, COMM-005), sau đó theo thứ tự:

`Status → Evidence → Next step`

- **Status:** xong / dở / bị chặn.
- **Evidence:** file/tool/lint thực sự đã dùng, kèm link (COMM-004).
- **Next step:** 1 gợi ý hoặc 1 câu hỏi (`COLLAB-004`, `COLLAB-009`).

Ngắn, cụ thể, không lặp lại nội dung đã biết. **Cấm:** bản thảo, dàn ý chi tiết, bảng audit, nội dung artifact dạng raw.

## COMM-003 · Ma trận Chat vs Artifact

| Loại thông tin                  | Ghi file                                  | Chat chứa                                               |
| :-------------------------------- | :---------------------------------------- | :------------------------------------------------------- |
| Brainstorm / câu hỏi đào sâu | Không                                    | 1 câu hỏi Socratic                                     |
| Blueprint                         | Tạo`chapters/ch_XX/card.md`            | 3 dòng: trục nhận thức chính, 5-second moment, link |
| Prose                             | Tạo/sửa`chapters/ch_XX/sections/*.md` | 1 dòng: số từ, trạng thái lint, link                |
| Audit / Critique                  | `audit_verdict.md`, `cold_read…`     | Verdict, 2–3 rủi ro nổi cộm, link                    |
| Quyết định chiến lược       | Cả hai, lưu`decisions.md`             | Trade-off ngắn để duyệt (`COLLAB-006`)             |

Verdict: Layer 2 = `PASS / REVISE / RESTRUCTURE`; Layer 3 = `Ship / Conditional / Major Revise / Kill`.

## COMM-004 · Vòng đời artifact & hiển thị file

- **Tạo mới:** khi sang node tạo entity độc lập; đối chiếu template trong `.agents/templates/`.
- **Sửa in-place:** biên tập phẫu thuật đúng file lỗi; sổ bộ sống (`story_bank.md`, `summaries.md`).
- **Đọc lại:** chỉ khi tác giả đã sửa file hoặc bước trước vừa bàn giao qua file đó. File/template/rule đã có trong context → không đọc lại.
- **Hiển thị file:** tên ngắn dạng Markdown link, không show absolute path. Ví dụ: `🤖 [book-architect.md](file:///...)`.
- Kết quả ghi trực tiếp vào file chỉ định trong `Books/<book_slug>/`.

## COMM-005 · Execution Badge & Resource Manifest Hai Tầng

### 1. Tầng 1: Compact Execution Badge (Tác vụ thực thi thông thường)
Cú pháp 4 dòng ở đầu phản hồi chat (hỗ trợ linh hoạt 2 đến 5 skills thực sự được nạp):

```markdown
🤖 **@role**  
⚡ `skill_1` + `skill_2` + ... *(2–5 skills thực sự nạp)*  
📄 [target_file](file:///...)  
🎯 **Mục tiêu ngắn gọn**
```

Ví dụ:
🤖 **@chapter-crafter**  
⚡ `chapter-drafting` + `humanizer` + `author-excavation` (3 skills)  
📄 [01_sec1.md](file:///...)  
🎯 **Chấp bút Section 1 bóc tách cơ chế Xao nhãng vĩ mô**

### 2. Tầng 2: Full Resource Manifest (Có điều kiện khi chuyển giao node lớn)
Chỉ kích hoạt tại điểm khởi đầu các Node lớn (`Node 1 Blueprint`, `Node 4 Drafting`, `Node 8 Informed Review`) hoặc khi chuyển giao Agent chủ trì:

```markdown
### 📋 Resource Manifest: Node <X> — <Tên Node>
- 🎯 **Mục tiêu**: Kết quả cụ thể cần đạt của node.
- 🤖 **Agent chủ trì**: `@role` chịu trách nhiệm chính.
- ⚡ **Skills dự kiến (2–5)**: Tên các skill kèm vai trò và điều kiện kích hoạt.
- 🔄 **Workflow Node**: `<workflow>` → `Node <X>`.
- 🧠 **Memory tham chiếu**: Các file memory thực sự tồn tại sẽ đọc/ghi.
- 📜 **Rules chi phối**: Các rule trực tiếp ảnh hưởng.
- 🛠️ **Công cụ/Script tiếp theo**: Script hoặc công cụ kiểm tra kế tiếp.
- 🏁 **Điều kiện hoàn thành**: Tiêu chuẩn nhị phân để kết thúc node.
```

### 3. Quy tắc minh bạch tài nguyên:
1. **Phân biệt 3 trạng thái:** *Tài nguyên dự kiến* (trước thực thi), *Tài nguyên thực sự nạp/thực thi* (trong thực thi, có kiểm chứng), và *Tài nguyên thực tế đã dùng kèm sai lệch* (sau thực thi).
2. **Không khai khống:** Tuyệt đối không liệt kê tài nguyên chưa nạp hoặc file chưa tồn tại trên đĩa. Tài nguyên tùy chọn phải ghi rõ điều kiện (ví dụ: *chỉ kích hoạt nếu tác giả nạp bản nháp*).
3. **Lựa chọn từ 2 đến 5 skill:** Chọn đúng số lượng cần thiết theo thực tế nhiệm vụ, không ép đủ số lượng và không cắt xuống 2 skill chỉ vì hiển thị.
4. Chỉ xuất hiện ở Chat; không chèn vào file trong `Books/<book_slug>/`.
5. **Miễn badge/manifest:** Hỏi thăm ngắn, đàm đạo, phỏng vấn Socratic nhanh.

## COMM-006 · Minh bạch & Bằng chứng thực tế

Nói ngắn gọn những gì thực sự đã load/đọc/chạy. Chỉ claim "loaded/activated" khi có bằng chứng từ file/tool trong phiên. Khi có sai lệch so với tài nguyên dự kiến ban đầu, báo cáo trung thực sai lệch đó.

## Hard Boundaries

- Cấm xả deep work dạng raw vào chat.
- Cấm claim hoặc badge giả (chưa gọi tool/script mà vẫn khai).
- Cấm chèn badge vào artifact.
- Cấm show absolute path trong chat.

## Thứ tự áp dụng

Áp dụng sau `human-agent-collaboration`. Rule đó quyết có hỏi/dừng hay không; rule này quyết nội dung đó đi qua chat hay file, và trình bày thế nào.