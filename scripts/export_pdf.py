#!/usr/bin/env python3
"""
Export Markdown chapter or manuscript to a clean, publication-grade reading PDF using Edge Headless.
"""

import os
import sys
import subprocess
import argparse
import markdown

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

def find_edge():
    for p in EDGE_PATHS:
        if os.path.exists(p):
            return p
    return None

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  @page {{
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @bottom-center {{
      content: "- " counter(page) " -";
      font-size: 10pt;
      font-family: 'Segoe UI', Arial, sans-serif;
      color: #718096;
    }}
  }}
  body {{
    font-family: 'Times New Roman', 'Cambria', serif;
    font-size: {font_size};
    line-height: {line_height};
    color: #1a202c;
    background: #fff;
    max-width: 820px;
    margin: 0 auto;
    padding: 10px;
  }}
  h1 {{
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: {h1_size};
    font-weight: 700;
    color: #0f172a;
    margin-top: 30px;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid #0f172a;
    text-align: center;
    page-break-after: avoid;
  }}
  h2 {{
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: {h2_size};
    font-weight: 600;
    color: #1e3a8a;
    margin-top: 32px;
    margin-bottom: 14px;
    page-break-after: avoid;
  }}
  h3 {{
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: {h3_size};
    font-weight: 600;
    color: #1d4ed8;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }}
  p {{
    margin-top: 0;
    margin-bottom: 18px;
    text-align: justify;
    text-justify: inter-word;
  }}
  blockquote {{
    margin: 20px 0;
    padding: 12px 20px;
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    font-style: italic;
    color: #334155;
  }}
  hr {{
    page-break-after: always;
    visibility: hidden;
    margin: 0;
    padding: 0;
    border: none;
    height: 0;
  }}
  .meta-header {{
    text-align: center;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 11pt;
    color: #64748b;
    margin-bottom: 35px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
  }}
  .badge {{
    display: inline-block;
    padding: 4px 14px;
    background: #e2e8f0;
    border-radius: 4px;
    font-size: 9pt;
    font-weight: 600;
    margin-bottom: 12px;
    color: #334155;
  }}
</style>
</head>
<body>
<div class="meta-header">
  <div class="badge">{badge}</div>
  <div>{book_title}</div>
</div>
{content}
</body>
</html>
"""

def export_to_pdf(input_md_path, output_pdf_path, book_title="LÀM ÍT ĐƯỢC NHIỀU, LÀM NHIỀU VẪN PHIÊU", badge="BẢN THẢO CHUYÊN SÂU (CHAPTER DRAFT PREVIEW)", font_size="12pt"):
    if not os.path.exists(input_md_path):
        print(f"Error: Input file {input_md_path} not found.")
        sys.exit(1)

    edge_exe = find_edge()
    if not edge_exe:
        print("Error: Microsoft Edge executable not found.")
        sys.exit(1)

    with open(input_md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text, extensions=['extra', 'smarty'])
    title = os.path.splitext(os.path.basename(input_md_path))[0]
    
    # Scale heading sizes proportionally to base font-size
    if font_size == "16pt":
        h1_size = "26pt"
        h2_size = "20pt"
        h3_size = "17pt"
        line_height = "1.85"
    elif font_size == "14pt":
        h1_size = "24pt"
        h2_size = "18pt"
        h3_size = "15pt"
        line_height = "1.8"
    else:
        h1_size = "22pt"
        h2_size = "15pt"
        h3_size = "13pt"
        line_height = "1.8"

    html_full = HTML_TEMPLATE.format(
        title=title,
        content=html_content,
        book_title=book_title,
        badge=badge,
        font_size=font_size,
        h1_size=h1_size,
        h2_size=h2_size,
        h3_size=h3_size,
        line_height=line_height
    )

    temp_html_path = output_pdf_path + ".temp.html"
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_full)

    abs_html = os.path.abspath(temp_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)

    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        abs_html
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    if os.path.exists(abs_pdf):
        print(f"[SUCCESS] Exported PDF: {abs_pdf}")
    else:
        print(f"[ERROR] Failed to export PDF. Details: {result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Markdown to PDF via Edge Headless.")
    parser.add_argument("--input", required=True, help="Path to input markdown file")
    parser.add_argument("--output", required=True, help="Path to output PDF file")
    parser.add_argument("--title", default="LÀM ÍT ĐƯỢC NHIỀU, LÀM NHIỀU VẪN PHIÊU", help="Book title header")
    parser.add_argument("--badge", default="BẢN THẢO CHUYÊN SÂU (CHAPTER DRAFT PREVIEW)", help="Badge header")
    parser.add_argument("--font-size", default="12pt", help="Base body font size (e.g. 12pt, 14pt, 16pt)")
    args = parser.parse_args()

    export_to_pdf(args.input, args.output, book_title=args.title, badge=args.badge, font_size=args.font_size)

