# Node 7: CHAPTER_ASSEMBLY

- **Thực thi**: L0 Direct (Script stdlib — Zero LLM Intervention).
- **Lệnh thực thi**: `python scripts/assemble_chapter.py --chapter <chapter_id> --commit`.
- **Human Gate**: `false`
- **Output Artifact**: `chapters/<chapter_id>/draft.md`.
- **Mục tiêu**: Ghép các section đã qua linter theo thứ tự alphanumeric thành bản thảo chương hoàn chỉnh kèm banner nguồn sự thật, in báo cáo thống kê số từ.
- **DoD**: File `chapters/<chapter_id>/draft.md` được sinh ra tự động.
- **Transition Path**: `CHAPTER_ASSEMBLY` $\rightarrow$ `INFORMED_REVIEW`.
