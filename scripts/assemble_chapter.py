#!/usr/bin/env python3
"""
scripts/assemble_chapter.py
Deterministic modular section assembler for chapters.
Assembles chapters/<chapter_id>/sections/*.md -> chapters/<chapter_id>/draft.md.
Pure Python standard library (no third-party dependencies).
"""

import sys
import re
import argparse
from pathlib import Path

def count_words(text: str) -> int:
    # Strip markdown headers, links, and code blocks for word counting
    clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    clean = re.sub(r"#+\s*", "", clean)
    clean = re.sub(r"\[.*?\]\(.*?\)", "", clean)
    words = clean.strip().split()
    return len(words)

def natural_sort_key(name: str):
    """Sort key that handles numeric substrings naturally (e.g. ch_01, ch_2, ch_10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", str(name))]

def assemble_chapter(chapter_dir: Path, commit: bool = False) -> int:
    sections_dir = chapter_dir / "sections"
    if not sections_dir.exists() or not sections_dir.is_dir():
        print(f"[ERROR] Sections directory not found: {sections_dir}", file=sys.stderr)
        return 1

    section_files = sorted(
        list(sections_dir.glob("*.md")) + list(sections_dir.glob("*.markdown")),
        key=lambda p: natural_sort_key(p.name),
    )
    if not section_files:
        print(f"[ERROR] No section files found in {sections_dir}", file=sys.stderr)
        return 1

    assembled_blocks = []
    total_words = 0
    breakdown = []

    for sfile in section_files:
        content = sfile.read_text(encoding="utf-8").strip()
        wc = count_words(content)
        total_words += wc
        breakdown.append((sfile.name, wc))
        assembled_blocks.append(content)

    banner = "<!-- GENERATED MANUSCRIPT DRAFT - SOURCE OF TRUTH IS sections/ -->\n\n"
    assembled_draft = banner + "\n\n<!-- section_break -->\n\n".join(assembled_blocks) + "\n"

    print(f"=== Chapter Assembly: {chapter_dir.name} ===")
    print(f"Total Sections: {len(section_files)}")
    print(f"Total Word Count: {total_words:,} words")
    print("Section Breakdown:")
    for name, wc in breakdown:
        print(f"  - {name}: {wc:,} words")

    draft_target = chapter_dir / "draft.md"
    if commit:
        draft_target.write_text(assembled_draft, encoding="utf-8")
        print(f"\n[COMMIT] Successfully assembled {len(section_files)} sections into: {draft_target}")
    else:
        print(f"\n[PREVIEW] Running in preview mode. To generate draft.md, pass --commit.")

    return 0

def assemble_manuscript(chapters_dir: Path, output_file: Path, commit: bool = False) -> int:
    """Deterministic whole-book compiler: concatenates chapters/*/draft.md in natural order."""
    if not chapters_dir.exists() or not chapters_dir.is_dir():
        print(f"[ERROR] Chapters directory not found: {chapters_dir}", file=sys.stderr)
        return 1

    # Find chapter directories
    chapter_dirs = [p for p in chapters_dir.iterdir() if p.is_dir() and not p.name.startswith(".")]
    if not chapter_dirs:
        print(f"[ERROR] No chapter directories found in: {chapters_dir}", file=sys.stderr)
        return 1

    chapter_dirs.sort(key=lambda p: natural_sort_key(p.name))

    chapters_drafts = []
    total_words = 0
    breakdown = []

    for cdir in chapter_dirs:
        draft_file = cdir / "draft.md"
        if not draft_file.exists():
            print(f"[ERROR] Draft file missing for chapter {cdir.name}: {draft_file}", file=sys.stderr)
            return 1
        content = draft_file.read_text(encoding="utf-8").strip()
        wc = count_words(content)
        total_words += wc
        breakdown.append((cdir.name, wc))
        chapters_drafts.append(content)

    full_manuscript = "\n\n---\n\n".join(chapters_drafts) + "\n"

    print(f"=== Whole-Book Manuscript Compilation ===")
    print(f"Total Chapters: {len(chapter_dirs)}")
    print(f"Total Word Count: {total_words:,} words")
    print("Chapter Breakdown:")
    for name, wc in breakdown:
        print(f"  - {name}: {wc:,} words")

    if commit:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(full_manuscript, encoding="utf-8")
        print(f"\n[COMMIT] Successfully compiled whole-book manuscript to: {output_file}")
    else:
        print(f"\n[PREVIEW] Running in preview mode. Pass --commit to write: {output_file}")

    return 0

def main():
    parser = argparse.ArgumentParser(description="Assemble modular chapter sections or whole-book manuscript.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--chapter", help="Chapter ID/folder name (e.g. ch_01)")
    group.add_argument("--path", help="Direct path to chapter directory")
    group.add_argument("--all", action="store_true", help="Compile all chapters into outputs/manuscript.md")

    parser.add_argument("--book", help="Book ID / slug (resolves chapters to Books/<book_id>/chapters)")
    parser.add_argument("--base-dir", default=None, help="Base directory containing chapters")
    parser.add_argument("--output-manuscript", default=None, help="Output path for whole-book manuscript")
    parser.add_argument("--commit", action="store_true", help="Commit assembled draft or manuscript (default is preview)")
    parser.add_argument("--preview", action="store_true", help="Preview assembled word counts without writing")
    args = parser.parse_args()

    if args.book:
        base_dir = Path("Books") / args.book / "chapters"
        output_manuscript = Path("Books") / args.book / "outputs" / "manuscript.md" if not args.output_manuscript else Path(args.output_manuscript)
    elif args.base_dir:
        base_dir = Path(args.base_dir)
        output_manuscript = Path(args.output_manuscript) if args.output_manuscript else base_dir.parent / "outputs" / "manuscript.md"
    else:
        # Auto-detect if Books has books
        books_dir = Path("Books")
        existing_books = [p for p in books_dir.iterdir() if p.is_dir() and not p.name.startswith(".")] if books_dir.exists() else []
        if len(existing_books) == 1:
            base_dir = existing_books[0] / "chapters"
            output_manuscript = existing_books[0] / "outputs" / "manuscript.md" if not args.output_manuscript else Path(args.output_manuscript)
        else:
            base_dir = Path("chapters")
            output_manuscript = Path("outputs") / "manuscript.md" if not args.output_manuscript else Path(args.output_manuscript)

    if args.all:
        sys.exit(assemble_manuscript(base_dir, output_manuscript, commit=args.commit))
    elif args.path:
        target_dir = Path(args.path)
        sys.exit(assemble_chapter(target_dir, commit=args.commit))
    else:
        target_dir = base_dir / args.chapter
        sys.exit(assemble_chapter(target_dir, commit=args.commit))

if __name__ == "__main__":
    main()
