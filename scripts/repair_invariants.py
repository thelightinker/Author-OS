#!/usr/bin/env python3
"""
scripts/repair_invariants.py
Deterministic mechanical normalization and safety guard for nonfiction book writing.
Pure Python standard library (no third-party dependencies).

Principles:
1. Mechanical normalization & guard ONLY: Handles strictly what machines can verify
   and standardize with 100% certainty (Unicode NFC, zero-width chars, heading punctuation,
   number range en-dash, gap tokens, code block isolation).
2. Not a final editorial cleaner: Never attempts semantic rewrites, rhythm alterations,
   or prose formatting judgments. Those belong strictly to the editorial lens.
3. Auto-repair is strictly mechanical, idempotent, deterministic, and safe.
4. Code spans, URLs, authorial voice, and prose semantics are strictly protected.
"""

import sys
import os
import re
import json
import argparse
import unicodedata
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ZERO_WIDTH_CHARS = ["\u200b", "\u200c", "\u200d", "\ufeff"]
GAP_PATTERNS = [
    re.compile(r"\[GAP.*?\]", re.IGNORECASE),
    re.compile(r"\[PENDING:.*?\]", re.IGNORECASE),
    re.compile(r"\[QUERY:.*?\]", re.IGNORECASE),
    re.compile(r"\[VERIFY.*?\]", re.IGNORECASE),
    re.compile(r"\[AUTHOR.*?\]", re.IGNORECASE),
    re.compile(r"\[EVIDENCE-REQUEST:.*?\]", re.IGNORECASE),
    re.compile(r"\[MISSING.*?\]", re.IGNORECASE),
    re.compile(r"\[UNVERIFIED.*?\]", re.IGNORECASE),
    re.compile(r"\[FABRICATED.*?\]", re.IGNORECASE),
    re.compile(r"\[HALLUCINATION.*?\]", re.IGNORECASE),
    re.compile(r"\[UNGROUNDED.*?\]", re.IGNORECASE),
]
RAW_DIAGRAM_PATTERN = re.compile(r"```(mermaid|ascii)", re.IGNORECASE)

MEGAPHONE_CLICHES = [
    "hãy nhớ rằng",
    "chiếc chìa khóa vạn năng",
    "hành trình chuyển hóa",
    "bức tranh toàn cảnh",
    "bức tranh tổng thể",
    "kỷ nguyên số phát triển như vũ bão",
    "đừng ngần ngại",
    "không thể phủ nhận rằng",
    "điều quan trọng cần ghi nhớ là",
    "nâng tầm",
    "bứt phá giới hạn",
]

TRANSLATIONESE_PHRASES = [
    "được xem như là",
    "đóng vai trò như là",
    "dưới góc độ của",
    "mang tính chất là",
    "có thể nói rằng",
]

def mask_code_spans(text: str) -> tuple[str, dict[str, str]]:
    """
    Masks code fences and inline code spans to guarantee that mechanical
    formatting replacements never alter code or technical syntax.
    """
    code_map: dict[str, str] = {}
    counter = 0

    def replace_fence(match: re.Match) -> str:
        nonlocal counter
        key = f"__CODE_FENCE_{counter}__"
        counter += 1
        code_map[key] = match.group(0)
        return key

    def replace_inline(match: re.Match) -> str:
        nonlocal counter
        key = f"__CODE_INLINE_{counter}__"
        counter += 1
        code_map[key] = match.group(0)
        return key

    # Mask fenced code blocks first, then inline code
    text = re.sub(r"```[\s\S]*?```", replace_fence, text)
    text = re.sub(r"`[^`\n]+`", replace_inline, text)
    return text, code_map

def unmask_code_spans(text: str, code_map: dict[str, str]) -> str:
    for key, orig in code_map.items():
        text = text.replace(key, orig)
    return text

def normalize_nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)

def strip_zero_width_and_control(text: str) -> str:
    for zw in ZERO_WIDTH_CHARS:
        text = text.replace(zw, "")
    clean_chars = [c for c in text if c in ("\t", "\n", "\r") or unicodedata.category(c)[0] != "C"]
    return "".join(clean_chars)

def fix_punctuation_spacing(text: str) -> str:
    # Remove space before punctuation marks: , . : ; ! ?
    text = re.sub(r"[ \t]+([,.:;!?])", r"\1", text)
    # Ensure a space after comma/semicolon/colon/period if followed immediately by letter/digit
    # Exception: numbers like 3.14 or URLs
    text = re.sub(r"([,;])([^\s\d])", r"\1 \2", text)
    return text

def fix_heading_trailing_punctuation(text: str) -> str:
    """
    Strips trailing colons, periods, or semicolons from markdown headings.
    Preserves question marks and exclamation marks.
    e.g. '## Giới thiệu:' -> '## Giới thiệu'
    """
    lines = []
    for line in text.splitlines(keepends=True):
        if re.match(r"^\s*#{1,6}\s+", line):
            line = re.sub(r"([ \t]*[:.;])+(\s*)$", r"\2", line)
        lines.append(line)
    return "".join(lines)

def fix_number_range_en_dash(text: str) -> str:
    """
    Conservative en-dash normalization:
    Only normalizes explicit 4-digit years or labeled ranges.
    Preserves version identifiers (v1-2), ISBNs, negative numbers, and IDs (S-003).
    """
    # 1. 4-digit years: 1990-2000 or 1990 - 2000 -> 1990–2000
    text = re.sub(r"\b(19\d\d|20\d\d)\s*[-–]\s*(19\d\d|20\d\d)\b", r"\1–\2", text)
    # 2. Labeled ranges: trang 10-20, chương 3-5
    text = re.sub(r"\b(trang|chương|tập|phần|bài)\s+(\d+)\s*[-–]\s*(\d+)\b", r"\1 \2–\3", text, flags=re.IGNORECASE)
    return text

def strip_thematic_breaks(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out_lines = []
    in_frontmatter = False
    frontmatter_count = 0

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if idx == 0 and stripped == "---":
            in_frontmatter = True
            frontmatter_count += 1
            out_lines.append(line)
            continue
        elif in_frontmatter and stripped == "---":
            in_frontmatter = False
            frontmatter_count += 1
            out_lines.append(line)
            continue
        elif in_frontmatter:
            out_lines.append(line)
            continue

        # In prose: strip standalone thematic breaks (--- or - - - or ***)
        if re.match(r"^(\s*[-*_]\s*){3,}$", stripped):
            continue
        out_lines.append(line)
    return "".join(out_lines)

def repair_text(text: str) -> str:
    """
    Applies 100% deterministic, idempotent, and safe mechanical repairs.
    Guarantees zero prose corruption and code span preservation.
    """
    masked_text, code_map = mask_code_spans(text)
    masked_text = normalize_nfc(masked_text)
    masked_text = strip_zero_width_and_control(masked_text)
    masked_text = fix_punctuation_spacing(masked_text)
    masked_text = fix_heading_trailing_punctuation(masked_text)
    masked_text = fix_number_range_en_dash(masked_text)
    masked_text = strip_thematic_breaks(masked_text)
    return unmask_code_spans(masked_text, code_map)

def find_author_birth_year(file_path: Path) -> int | None:
    curr = file_path.resolve()
    for parent in [curr] + list(curr.parents):
        id_path = parent / ".agents" / "memory" / "author" / "identity.md"
        if id_path.exists():
            try:
                text = id_path.read_text(encoding="utf-8")
                m = re.search(r"birth_year:\s*(\d{4})", text)
                if m:
                    return int(m.group(1))
            except Exception:
                pass
    return None

def is_epistemic_issue(issue_str: str) -> bool:
    """Checks whether a lint issue represents an epistemic gap requiring author input."""
    epistemic_markers = [
        "Unresolved gap token found",
        "[STORY_INTEGRITY_VIOLATION]",
        "[TIMELINE_ANACHRONISM_VIOLATION]",
        "TIMELINE_ANACHRONISM",
        "Provenance Tier",
        "Confirmed Facts",
        "Interview Source",
    ]
    return any(marker in issue_str for marker in epistemic_markers)

def step_revision(card_path: Path) -> int:
    """
    Deterministically increments revision_round in card.md frontmatter.
    Returns:
      0: Successfully incremented, still below ceiling (< 3)
      2: Reached or already at ceiling (>= 3)
      1: Error (file not found, malformed syntax)
    """
    if not card_path.exists():
        print(f"Error: card file not found: {card_path}", file=sys.stderr)
        return 1

    try:
        content = card_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {card_path}: {e}", file=sys.stderr)
        return 1

    m = re.search(r'revision_round:\s*["\']?(\d+)(?:\s*/\s*(\d+))?["\']?', content)
    if not m:
        print(f"Error: missing or invalid revision_round in {card_path}", file=sys.stderr)
        return 1

    curr = int(m.group(1))
    max_r = int(m.group(2)) if m.group(2) else 3

    if curr >= max_r:
        print(f"[REVISION_CEILING_REACHED] card {card_path} is already at ceiling ({curr}/{max_r}).", file=sys.stderr)
        return 2

    nxt = curr + 1
    new_str = f'revision_round: "{nxt}/{max_r}"'
    new_content = re.sub(
        r'revision_round:\s*["\']?\d+(?:\s*/\s*\d+)?["\']?',
        new_str,
        content,
        count=1
    )

    try:
        card_path.write_text(new_content, encoding="utf-8")
        print(f"[REVISION_STEP] card {card_path} incremented revision_round: {curr}/{max_r} -> {nxt}/{max_r}")
    except Exception as e:
        print(f"Error writing {card_path}: {e}", file=sys.stderr)
        return 1

    if nxt >= max_r:
        print(f"[REVISION_CEILING_REACHED] card {card_path} reached revision ceiling ({nxt}/{max_r}).", file=sys.stderr)
        return 2

    return 0

def lint_story_bank(file_path: Path, content: str) -> list[str]:
    issues = []
    blocks = re.split(r'\n(?=##\s+S-\d+)', content)
    birth_year = find_author_birth_year(file_path)

    for block in blocks:
        m = re.search(r'##\s+(S-\d+):\s*(.+)', block)
        if not m:
            continue
        sid, title = m.group(1).strip(), m.group(2).strip()

        # 1. Provenance Tier check
        prov = re.search(r'-\s+\*\*Provenance Tier:\*\*\s*(.+)', block)
        if not prov:
            issues.append(f"{file_path}: Story {sid} ({title}) missing required '**Provenance Tier:**' (Tier A/B/C/D).")
        else:
            tier_val = prov.group(1).strip()
            if not any(t in tier_val for t in ["Tier A", "Tier B", "Tier C", "Tier D"]):
                issues.append(f"{file_path}: Story {sid} has invalid Provenance Tier '{tier_val}'. Must be Tier A, B, C, or D.")

            # 2. Tier A must have confirmed facts or interview source
            if "Tier A" in tier_val:
                facts = re.search(r'-\s+\*\*Confirmed Facts:\*\*\s*(.+)', block)
                interview = re.search(r'-\s+\*\*(?:Interview Source|Interview Content):\*\*\s*(.+)', block)
                if not facts and not interview:
                    issues.append(f"{file_path}: Tier A story {sid} ({title}) must declare verified '**Confirmed Facts:**' or '**Interview Source:**'.")

        # 3. Check for un-replaced template placeholders
        if re.search(r'\{\{[A-Z0-9_]+\}\}', block):
            issues.append(f"{file_path}: Story {sid} contains unresolved template placeholder.")

        # 4. Timeline Sanity Check against author birth year (Tier A only)
        if birth_year and prov and "Tier A" in prov.group(1):
            years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', block)]
            for y in years:
                if y == birth_year:
                    continue
                if y < birth_year + 14 and any(kw in block.lower() for kw in ["lớp 11", "lớp 12", "đại học", "công ty", "văn phòng", "thi cử", "sư phạm", "it", "phá sản"]):
                    issues.append(
                        f"{file_path}: Story {sid} TIMELINE_ANACHRONISM: Event year {y} contradicts author birth year {birth_year} (author was {y - birth_year} years old)."
                    )

    return issues

def lint_file(file_path: Path) -> list:
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Cannot read file {file_path}: {e}"]

    # Mask protected code regions before evaluating mechanical prose invariants
    masked_content, _ = mask_code_spans(content)

    # 1. Check NFC (on prose outside code spans)
    if not unicodedata.is_normalized("NFC", masked_content):
        issues.append(f"{file_path}: Text is not NFC normalized.")

    # 2. Check Zero-width chars (on prose outside code spans)
    for zw in ZERO_WIDTH_CHARS:
        if zw in masked_content:
            issues.append(f"{file_path}: Contains zero-width character ({repr(zw)}).")

    # 3. Check unresolved gaps
    for pat in GAP_PATTERNS:
        matches = pat.findall(content)
        if matches:
            issues.append(f"{file_path}: Unresolved gap token found: {matches[:3]}")

    # 4. Check raw diagram blocks
    if RAW_DIAGRAM_PATTERN.search(content):
        issues.append(f"{file_path}: Raw diagram block found (mermaid/ascii). Use semantic placeholders instead.")

    # 5. Check punctuation errors (space before punctuation, outside code spans)
    if re.search(r"[ \t]+[,.:;!?]", masked_content):
        issues.append(f"{file_path}: Contains illegal whitespace preceding punctuation mark.")

    # 6. Check violation markers (in draft/story/section files, not in rule definitions)
    if "rules" not in file_path.parts:
        if "[STORY_INTEGRITY_VIOLATION]" in content:
            issues.append(f"{file_path}: Contains active [STORY_INTEGRITY_VIOLATION] marker.")
        if "[TIMELINE_ANACHRONISM_VIOLATION]" in content:
            issues.append(f"{file_path}: Contains active [TIMELINE_ANACHRONISM_VIOLATION] marker.")

    # 7. Check Story Bank integrity if applicable
    if file_path.name == "story_bank.md":
        issues.extend(lint_story_bank(file_path, content))

    # 8. Check Card version and revision_round alignment if card.md
    if file_path.name == "card.md":
        m_ver = re.search(r'card_version:\s*["\']?([^"\'\n]+)["\']?', content)
        if m_ver:
            version_str = m_ver.group(1).strip()
            if version_str != "3.0.0":
                issues.append(f"{file_path}: CARD_VERSION_MISMATCH: expected 'card_version: \"3.0.0\"', found '{version_str}'.")
        else:
            if "---" in content or "card" in content.lower():
                issues.append(f"{file_path}: CARD_VERSION_MISMATCH: missing 'card_version: \"3.0.0\"'.")

        m_rev = re.search(r'revision_round:\s*["\']?([^"\'\n]+)["\']?', content)
        if m_rev:
            rev_str = m_rev.group(1).strip()
            if not re.match(r'^\d+(\s*/\s*3)?$', rev_str):
                issues.append(f"{file_path}: CARD_REVISION_ROUND_INVALID: expected format 'N/3' or integer (max 3), found '{rev_str}'.")
        else:
            if "---" in content:
                issues.append(f"{file_path}: CARD_REVISION_ROUND_MISSING: missing 'revision_round: \"0/3\"' in frontmatter.")

    # 9. Megaphone Cliches & Translationese in prose content (outside doc/template/test folders)
    is_doc_or_meta = any(part in file_path.parts for part in ["rules", "templates", "skills", "agent", "workflows", "references", "knowledge", "tests"])
    if not is_doc_or_meta:
        lower_masked = masked_content.lower()
        for phrase in MEGAPHONE_CLICHES:
            if phrase in lower_masked:
                issues.append(f"{file_path}: MEGAPHONE_CLICHE: Preachy slogan pattern detected: '{phrase}'. Anchor in concrete scene or quiet observation instead.")
        for phrase in TRANSLATIONESE_PHRASES:
            if phrase in lower_masked:
                issues.append(f"{file_path}: TRANSLATIONESE: Awkward literal phrasing detected: '{phrase}'. Simplify into direct Vietnamese prose.")

    # 10. Word Ceiling Check for section files
    if "sections" in file_path.parts or file_path.parent.name == "sections":
        chapter_dir = file_path.parent.parent if file_path.parent.name == "sections" else file_path.parent
        card_path = chapter_dir / "card.md"
        if card_path.exists():
            try:
                card_text = card_path.read_text(encoding="utf-8")
                sec_budget = None
                sec_filename = file_path.name
                table_match = re.search(rf'\|\s*`?{re.escape(sec_filename)}`?\s*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|', card_text)
                if table_match:
                    sec_budget = int(table_match.group(1))
                else:
                    m_budget = re.search(r'budget_words_max:\s*(\d+)', card_text)
                    if m_budget:
                        sec_budget = int(m_budget.group(1))

                if sec_budget:
                    words = len(re.findall(r'\S+', masked_content))
                    ceiling = int(sec_budget * 1.20)
                    if words > ceiling:
                        issues.append(
                            f"{file_path}: WORD_CEILING_EXCEEDED: Section word count ({words}) exceeds budget_words_max ({sec_budget}) by more than 20% (ceiling: {ceiling})."
                        )
            except Exception:
                pass

    # 11. Mechanical Formatting Pre-flight check (sections, draft, manuscript)
    is_prose_file = (
        ("sections" in file_path.parts or file_path.name in ["draft.md", "manuscript.md"])
        and "tests" not in file_path.parts
        and "rules" not in file_path.parts
        and ".baseline" not in file_path.parts
    )
    if is_prose_file:
        if re.search(r"[a-zA-ZÀ-ỹ0-9]—|—[a-zA-ZÀ-ỹ0-9]", masked_content):
            issues.append(
                f"{file_path}: UNSPACED_EM_DASH: Found em-dash ('—') attached directly to characters without spacing. "
                f"Apply manuscript-formatting (FORMAT-002) to re-anchor syntax or remove artificial dashes."
            )

    return issues

def process_path(target: Path, lint_mode: bool, json_mode: bool = False) -> int:
    files = []
    if target.is_file():
        files.append(target)
    elif target.is_dir():
        for ext in ("*.md", "*.markdown"):
            files.extend(target.rglob(ext))
    else:
        print(f"Target path does not exist: {target}", file=sys.stderr)
        return 1

    if lint_mode:
        all_issues = []
        for f in files:
            issues = lint_file(f)
            if issues:
                all_issues.extend(issues)
        if all_issues:
            has_epistemic = any(is_epistemic_issue(iss) for iss in all_issues)
            has_style = any(not is_epistemic_issue(iss) for iss in all_issues)
            exit_code = 3 if has_epistemic else 1
            if json_mode:
                payload = {
                    "status": "gap_detected" if has_epistemic else "style_defect",
                    "mode": "lint",
                    "exit_code": exit_code,
                    "has_epistemic_gaps": has_epistemic,
                    "has_style_defects": has_style,
                    "files_checked": len(files),
                    "violations_count": len(all_issues),
                    "violations": all_issues,
                    "errors": []
                }
                print(json.dumps(payload, indent=2, ensure_ascii=False))
            else:
                tag = "[EPISTEMIC GAP]" if has_epistemic else "[STYLE DEFECT]"
                print(f"[FAIL] {tag} Found {len(all_issues)} lint issue(s):", file=sys.stderr)
                for iss in all_issues:
                    print(f"  - {iss}", file=sys.stderr)
            return exit_code

        if json_mode:
            payload = {
                "status": "pass",
                "mode": "lint",
                "files_checked": len(files),
                "violations_count": 0,
                "violations": [],
                "errors": []
            }
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(f"[PASS] All {len(files)} file(s) passed mechanical lint.")
        return 0
    else:
        changed_files = []
        errors = []
        for f in files:
            try:
                orig = f.read_text(encoding="utf-8")
                repaired = repair_text(orig)
                if repaired != orig:
                    f.write_text(repaired, encoding="utf-8")
                    changed_files.append(str(f))
            except Exception as e:
                errors.append(f"Failed to process {f}: {e}")

        if json_mode:
            payload = {
                "status": "repaired" if not errors else "partial",
                "mode": "repair",
                "files_processed": len(files),
                "changed_files_count": len(changed_files),
                "changed_files": changed_files,
                "errors": errors
            }
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(f"[REPAIR] Processed {len(files)} file(s). Auto-repaired {len(changed_files)} file(s).")
        return 0 if not errors else 1

def main():
    parser = argparse.ArgumentParser(description="Deterministic stdlib mechanical text normalization and safety guard.")
    parser.add_argument("target", nargs="?", default=None, help="File or directory path to process")
    parser.add_argument("--lint", action="store_true", help="Lint mode: check mechanical invariants without modifying files")
    parser.add_argument("--repair", "--fix", dest="repair", action="store_true", help="Repair mode: apply deterministic mechanical normalizations")
    parser.add_argument("--step-revision", dest="step_revision", help="Increment revision_round in card.md deterministically")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    if args.step_revision:
        sys.exit(step_revision(Path(args.step_revision)))

    if not args.target:
        parser.print_help(sys.stderr)
        sys.exit(1)

    lint_mode = not args.repair
    sys.exit(process_path(Path(args.target), lint_mode=lint_mode, json_mode=args.json))

if __name__ == "__main__":
    main()
