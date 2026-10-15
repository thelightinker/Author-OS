#!/usr/bin/env python3
"""
Writing Agent Memory CLI (memory_cli.py).
Pure Python stdlib CLI for JIT memory querying, safe atomic state updates,
multi-book story usage tracking, and deterministic continuity auditing.

Architecture Invariant:
Memory is Source of Truth | CLI is Query & Validation | Agent is Reasoning.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "2.0.0"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def find_memory_dir() -> Path:
    """Locate .agents/memory directory from current script or working directory."""
    candidates = [
        Path(__file__).parent.parent / "memory",
        Path.cwd() / ".agents" / "memory",
        Path.cwd() / "memory",
    ]
    for c in candidates:
        if (c / "author").exists() and (c / "experience").exists():
            return c.resolve()
    # Fallback default
    return (Path(__file__).parent.parent / "memory").resolve()


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Lightweight fallback YAML parser for author voice configuration without external dependencies."""
    result: dict[str, Any] = {}
    lines = text.splitlines()
    current_key = None
    in_avoid = False
    in_preferred = False
    avoid_list = []
    preferred_list = []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("preferred:"):
            in_preferred = True
            in_avoid = False
            continue
        elif stripped.startswith("avoid:"):
            in_avoid = True
            in_preferred = False
            continue
        elif not line.startswith(" ") and not line.startswith("\t") and ":" in stripped:
            in_preferred = False
            in_avoid = False
            key, val = stripped.split(":", 1)
            result[key.strip()] = val.strip().strip('"').strip("'")
            current_key = key.strip()
            continue

        if in_preferred and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"').strip("'")
            preferred_list.append(item)
        elif in_avoid and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"').strip("'")
            avoid_list.append(item)

    if preferred_list:
        result["vocabulary_preferred"] = preferred_list
    if avoid_list:
        result["vocabulary_avoid"] = avoid_list
    return result


def cmd_get_voice(memory_dir: Path, args: argparse.Namespace) -> int:
    voice_file = memory_dir / "author" / "voice.yaml"
    id_file = memory_dir / "author" / "identity.md"

    if not voice_file.exists():
        sys.stderr.write(f"Error: Voice file not found at {voice_file}\n")
        return 1

    content = voice_file.read_text(encoding="utf-8")
    parsed = parse_simple_yaml(content)

    print("### AUTHOR VOICE CADENCE & STANCE CONTRACT")
    print(f"- **Author Persona**: Hải Đăng · The Lightinker")
    print(f"- **Cadence Hierarchy**:")
    print(f"  * short_punchy (1-7 words): Cognitive breakpoint, punchline.")
    print(f"  * medium_causal (8-18 words): Analytical backbone, clear logic.")
    print(f"  * long_sensory (19-38 words): Scene immersion, grey-zone nuance.")
    print(f"  * Monotone Penalty: HIGH (prohibit uniform sentence lengths).")

    if "vocabulary_avoid" in parsed:
        print(f"\n- **Banned Clichés (Avoid at all costs)**:")
        for w in parsed["vocabulary_avoid"]:
            print(f"  * \"{w}\"")

    if "vocabulary_preferred" in parsed:
        print(f"\n- **Preferred Core Vocabulary**:")
        print("  " + ", ".join(f'"{w}"' for w in parsed["vocabulary_preferred"]))

    print("\n- **Tone & Stance**: Intimate comrade sitting beside reader; quiet confidence; ZERO preachy guru lectures.")
    return 0


def parse_markdown_stories(content: str) -> list[dict[str, Any]]:
    """Parse canonical story_bank.md into structured story entries with Epistemic Breakdown support."""
    stories = []
    blocks = re.split(r'\n(?=##\s+S-\d+)', content)
    for block in blocks:
        m = re.search(r'##\s+(S-\d+):\s*(.+)', block)
        if not m:
            continue
        sid, title = m.group(1).strip(), m.group(2).strip()
        tags_match = re.search(r'-\s+\*\*Tags:\*\*\s*(.+)', block, re.IGNORECASE)
        tags = [t.strip() for t in tags_match.group(1).split(',')] if tags_match else []
        insight_match = re.search(r'-\s+\*\*(?:Bài học cốt lõi|Reframe Note).*:\*\*\s*(.+)', block)
        context_match = re.search(r'-\s+\*\*(?:Thời điểm & Bối cảnh|Confirmed Facts|Context):\*\*\s*(.+)', block)
        hook_match = re.search(r'-\s+\*\*(?:Điểm chạm cảm xúc|Emotional Hook).*:\*\*\s*(.+)', block)
        trans_match = re.search(r'-\s+\*\*(?:Cảnh chuyển hóa|Transformation Scene).*:\*\*\s*(.+)', block)
        details_match = re.search(r'-\s+\*\*(?:Chi tiết hiện trường|Concrete Details).*:\*\*\s*(.+)', block)

        provenance_match = re.search(r'-\s+\*\*Provenance Tier:\*\*\s*(.+)', block)
        facts_match = re.search(r'-\s+\*\*Confirmed Facts:\*\*\s*(.+)', block)
        interview_match = re.search(r'-\s+\*\*Interview Content:\*\*\s*(.+)', block)
        author_interp_match = re.search(r'-\s+\*\*Author Interpretation:\*\*\s*(.+)', block)
        agent_infer_match = re.search(r'-\s+\*\*Agent Inferences:\*\*\s*(.+)', block)
        unknown_match = re.search(r'-\s+\*\*Unknown Details:\*\*\s*(.+)', block)
        timeline_match = re.search(r'-\s+\*\*Timeline Sanity:\*\*\s*(.+)', block)

        stories.append({
            "id": sid,
            "title": title,
            "tags": tags,
            "provenance_tier": provenance_match.group(1).strip() if provenance_match else "Tier A",
            "confirmed_facts": facts_match.group(1).strip() if facts_match else "",
            "interview_content": interview_match.group(1).strip() if interview_match else "",
            "author_interpretation": author_interp_match.group(1).strip() if author_interp_match else "",
            "agent_inferences": agent_infer_match.group(1).strip() if agent_infer_match else "",
            "unknown_details": unknown_match.group(1).strip() if unknown_match else "",
            "timeline_sanity": timeline_match.group(1).strip() if timeline_match else "PASS",
            "core_insight": insight_match.group(1).strip() if insight_match else "",
            "context": context_match.group(1).strip() if context_match else "",
            "emotional_hook": hook_match.group(1).strip() if hook_match else "",
            "transformation": trans_match.group(1).strip() if trans_match else "",
            "concrete_details": [d.strip() for d in details_match.group(1).split(';')] if details_match else [],
            "raw_block": block.strip()
        })
    return stories


def cmd_get_story(memory_dir: Path, args: argparse.Namespace) -> int:
    md_file = memory_dir / "experience" / "story_bank.md"
    usage_file = memory_dir / "experience" / "usage.json"

    if not md_file.exists():
        sys.stderr.write(f"Error: Canonical story_bank.md not found in {memory_dir / 'experience'}\n")
        return 1

    raw_stories = parse_markdown_stories(md_file.read_text(encoding="utf-8"))
    usage_data = json.loads(usage_file.read_text(encoding="utf-8")) if usage_file.exists() else {"story_usage": {}}

    filtered = []
    book_id = args.book_id or "the_lightinker_first_step"

    for s in raw_stories:
        if args.id and s.get("id") != args.id:
            continue
        if args.tag and args.tag not in s.get("tags", []):
            continue

        story_copy = dict(s)
        history = [u for u in usage_data.get("story_usage", {}).get(s["id"], []) if u.get("book_id") == book_id]
        story_copy["history_in_book"] = history
        story_copy["available_for_new_angle"] = True
        filtered.append(story_copy)

    print(json.dumps(filtered, ensure_ascii=False, indent=2))
    return 0


def cmd_record_story_usage(memory_dir: Path, args: argparse.Namespace) -> int:
    usage_file = memory_dir / "experience" / "usage.json"

    if not usage_file.exists():
        usage_data = {"schema_version": SCHEMA_VERSION, "story_usage": {}, "evidence_usage": {}}
    else:
        usage_data = json.loads(usage_file.read_text(encoding="utf-8"))

    story_id = args.id
    book_id = args.book_id or "the_lightinker_first_step"
    chapter = args.chapter
    section = args.section
    angle = args.angle
    function = args.function or "hook_and_paradox"
    details = [d.strip() for d in args.key_details.split(",")] if args.key_details else []

    history = usage_data.setdefault("story_usage", {}).setdefault(story_id, [])

    # Check for same book usage
    same_book_entries = [e for e in history if e.get("book_id") == book_id]

    status = "USED"
    if same_book_entries:
        # Check angle and function duplicate risk
        is_duplicate = False
        for entry in same_book_entries:
            if entry.get("angle", "").strip().lower() == angle.strip().lower() and entry.get("function") == function:
                is_duplicate = True
                break
        status = "DUPLICATE-RISK" if is_duplicate else "REUSED-DIFFERENT-ANGLE"

    record_entry = {
        "book_id": book_id,
        "chapter": chapter,
        "section": section,
        "angle": angle,
        "function": function,
        "key_details_used": details,
        "status": status,
        "recorded_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    history.append(record_entry)

    # Atomic write with backup
    bak = usage_file.with_suffix(".json.bak")
    if usage_file.exists():
        shutil.copyfile(usage_file, bak)

    tmp = usage_file.with_suffix(".tmp")
    tmp.write_text(json.dumps(usage_data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(usage_file)

    print(json.dumps(record_entry, ensure_ascii=False, indent=2))
    return 0


def cmd_get_evidence(memory_dir: Path, args: argparse.Namespace) -> int:
    evidence_file = memory_dir / "experience" / "evidence.json"
    if not evidence_file.exists():
        sys.stderr.write(f"Error: evidence.json not found at {evidence_file}\n")
        return 1

    ev_data = json.loads(evidence_file.read_text(encoding="utf-8"))
    items = ev_data.get("evidence_items", [])

    filtered = []
    for item in items:
        if args.id and item.get("id") != args.id:
            continue
        if args.tag and args.tag not in item.get("tags", []):
            continue
        filtered.append(item)

    print(json.dumps(filtered, ensure_ascii=False, indent=2))
    return 0


def cmd_get_continuity(memory_dir: Path, args: argparse.Namespace) -> int:
    cont_file = memory_dir / "project" / "continuity.json"
    if not cont_file.exists():
        sys.stderr.write(f"Error: continuity.json not found at {cont_file}\n")
        return 1

    cont_data = json.loads(cont_file.read_text(encoding="utf-8"))

    if args.all:
        print(json.dumps(cont_data, ensure_ascii=False, indent=2))
        return 0

    target_chapter = args.chapter or "current"

    # Filtered subset tailored for LLM prompt context
    filtered_payload = {
        "book_id": cont_data.get("book_id"),
        "target_chapter": target_chapter,
        "active_concepts": [c for c in cont_data.get("core_concepts", []) if c.get("status") == "ACTIVE"],
        "callback_ready_metaphors": [m for m in cont_data.get("active_metaphors", []) if m.get("callback_ready") is True],
        "open_loops_for_chapter": [
            l for l in cont_data.get("open_loops", [])
            if l.get("status") == "OPEN" and (l.get("target_chapter") == target_chapter or target_chapter == "current")
        ],
        "established_facts_summary": [f["fact"] for f in cont_data.get("established_facts", [])[:10]],
        "central_claims_summary": [c["claim"] for c in cont_data.get("central_claims", [])[:10]]
    }

    print(json.dumps(filtered_payload, ensure_ascii=False, indent=2))
    return 0


def cmd_update_continuity(memory_dir: Path, args: argparse.Namespace) -> int:
    state_file = Path(args.state_file)
    if not state_file.exists():
        sys.stderr.write(f"Error: State file not found: {state_file}\n")
        return 1

    try:
        payload = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception as exc:
        sys.stderr.write(f"Validation error: State file contains invalid JSON: {exc}\n")
        return 1

    # Strict Schema Validation
    required_keys = ["schema_version", "book_id", "chapter"]
    for k in required_keys:
        if k not in payload:
            sys.stderr.write(f"Validation error: Missing required field '{k}' in state payload\n")
            return 1

    if payload["schema_version"] != SCHEMA_VERSION:
        sys.stderr.write(f"Validation error: Incompatible schema_version '{payload['schema_version']}' (expected '{SCHEMA_VERSION}')\n")
        return 1

    cont_file = memory_dir / "project" / "continuity.json"
    if not cont_file.exists():
        sys.stderr.write(f"Error: continuity.json not found at {cont_file}\n")
        return 1

    cont_data = json.loads(cont_file.read_text(encoding="utf-8"))

    # Create atomic backup
    bak_file = cont_file.with_suffix(".json.bak")
    shutil.copyfile(cont_file, bak_file)

    # Perform Merge
    merged_counts = {"facts": 0, "concepts": 0, "metaphors": 0, "claims": 0, "loops_closed": 0}

    for fact in payload.get("new_facts", []):
        if not any(f["id"] == fact.get("id") for f in cont_data.setdefault("established_facts", [])):
            cont_data["established_facts"].append(fact)
            merged_counts["facts"] += 1

    for concept in payload.get("new_concepts", []):
        if not any(c["id"] == concept.get("id") for c in cont_data.setdefault("core_concepts", [])):
            cont_data["core_concepts"].append(concept)
            merged_counts["concepts"] += 1

    for metaphor in payload.get("new_metaphors", []):
        if not any(m["id"] == metaphor.get("id") for m in cont_data.setdefault("active_metaphors", [])):
            cont_data["active_metaphors"].append(metaphor)
            merged_counts["metaphors"] += 1

    for claim in payload.get("new_claims", []):
        if not any(c["id"] == claim.get("id") for c in cont_data.setdefault("central_claims", [])):
            cont_data["central_claims"].append(claim)
            merged_counts["claims"] += 1

    closed_ids = payload.get("closed_loops", [])
    for loop in cont_data.get("open_loops", []):
        if loop["loop_id"] in closed_ids:
            loop["status"] = "CLOSED"
            loop["resolution_chapter"] = payload.get("chapter")
            merged_counts["loops_closed"] += 1

    cont_data["last_updated"] = datetime.date.today().isoformat()

    # Write atomically
    tmp_file = cont_file.with_suffix(".tmp")
    tmp_file.write_text(json.dumps(cont_data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp_file.replace(cont_file)

    print(f"Merged state for chapter '{payload['chapter']}': {merged_counts}")
    return 0


def cmd_audit_continuity(memory_dir: Path, args: argparse.Namespace) -> int:
    cont_file = memory_dir / "project" / "continuity.json"
    usage_file = memory_dir / "experience" / "usage.json"
    stories_file = memory_dir / "experience" / "stories.json"

    errors = []

    if not cont_file.exists():
        errors.append(f"Missing {cont_file}")
    else:
        try:
            cont_data = json.loads(cont_file.read_text(encoding="utf-8"))
            # 1. Duplicate IDs in arrays
            for section in ["established_facts", "core_concepts", "active_metaphors", "central_claims"]:
                seen = set()
                for item in cont_data.get(section, []):
                    item_id = item.get("id")
                    if not item_id:
                        errors.append(f"{section}: item missing id: {item}")
                    elif item_id in seen:
                        errors.append(f"{section}: duplicate id '{item_id}'")
                    seen.add(item_id)

            # 2. Open loops integrity
            seen_loops = set()
            for loop in cont_data.get("open_loops", []):
                lid = loop.get("loop_id")
                if not lid:
                    errors.append(f"open_loops: loop missing loop_id: {loop}")
                elif lid in seen_loops:
                    errors.append(f"open_loops: duplicate loop_id '{lid}'")
                seen_loops.add(lid)
                if loop.get("status") not in ("OPEN", "CLOSED"):
                    errors.append(f"open_loops: invalid status '{loop.get('status')}' for {lid}")
        except Exception as e:
            errors.append(f"Invalid JSON in {cont_file}: {e}")

    # 3. Usage file audit
    if usage_file.exists():
        try:
            usage_data = json.loads(usage_file.read_text(encoding="utf-8"))
            known_stories = set()
            md_file = memory_dir / "experience" / "story_bank.md"
            if md_file.exists():
                known_stories = {s["id"] for s in parse_markdown_stories(md_file.read_text(encoding="utf-8"))}

            for sid, uses in usage_data.get("story_usage", {}).items():
                if known_stories and sid not in known_stories:
                    errors.append(f"usage.json: referenced story '{sid}' does not exist in story_bank.md")
                for u in uses:
                    if u.get("status") == "DUPLICATE-RISK":
                        errors.append(f"usage.json: WARNING - Duplicate story risk detected for {sid} in chapter {u.get('chapter')}")
        except Exception as e:
            errors.append(f"Invalid JSON in {usage_file}: {e}")

    if errors:
        sys.stderr.write(f"Structural audit failed with {len(errors)} error(s):\n")
        for err in errors:
            sys.stderr.write(f"  [ERROR] {err}\n")
        return 1

    print("Audit passed: 0 structural errors, 0 duplicate IDs, all references valid.")
    return 0


def cmd_capture(memory_dir: Path, args: argparse.Namespace) -> int:
    text = args.text.strip()
    tag_str = args.tag or ""
    tags = [t.strip() for t in tag_str.split(",") if t.strip()]
    now = datetime.datetime.now(datetime.timezone.utc)
    date_str = now.date().isoformat()

    target_name = args.target or "story_bank.md"
    target_file = memory_dir / "experience" / target_name

    content = target_file.read_text(encoding="utf-8") if target_file.exists() else ""

    existing_ids = [int(m) for m in re.findall(r'##\s+S-(\d+)', content)]
    next_num = max(existing_ids, default=0) + 1
    new_id = f"S-{next_num:03d}"

    title = args.title or (text[:50] + ("..." if len(text) > 50 else ""))

    new_entry = f"""

## {new_id}: {title}
- **Status:** draft_insight
- **Captured At:** {date_str}
- **Tags:** {', '.join(tags) if tags else 'insight, raw'}
- **Provenance Tier:** Tier A (Ký ức tác giả)
- **Confirmed Facts:** {text}
- **Interview Content:** Đã ghi nhận nhanh từ tác giả qua lệnh capture. Cần phỏng vấn thêm nếu dùng làm cảnh chính.
- **Author Interpretation:** {text}
- **Agent Inferences:** None
- **Unknown Details:** Bối cảnh cụ thể, thời gian chính xác, số liệu chi tiết (cần đào sâu khi đưa vào card).
- **Timeline Sanity:** PASS
- **Used In:** None
"""
    new_content = content.rstrip() + new_entry + "\n"
    tmp_file = target_file.with_suffix(".tmp")
    tmp_file.write_text(new_content, encoding="utf-8")
    tmp_file.replace(target_file)

    res = {
        "status": "draft_insight",
        "id": new_id,
        "title": title,
        "tags": tags,
        "text": text,
        "date": date_str,
        "target": str(target_file.name)
    }
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


def cmd_find(memory_dir: Path, args: argparse.Namespace) -> int:
    query = (args.query or "").strip().lower()
    tag = (args.tag or "").strip().lower()

    md_file = memory_dir / "experience" / "story_bank.md"
    if not md_file.exists():
        sys.stderr.write(f"Error: {md_file} not found\n")
        return 1

    stories = parse_markdown_stories(md_file.read_text(encoding="utf-8"))
    results = []

    for s in stories:
        if tag:
            tags_lower = [t.lower() for t in s.get("tags", [])]
            if not any(tag in t for t in tags_lower):
                continue

        if query:
            searchable_text = f"{s.get('id', '')} {s.get('title', '')} {s.get('confirmed_facts', '')} {s.get('interview_content', '')} {s.get('core_insight', '')} {s.get('author_interpretation', '')} {' '.join(s.get('tags', []))}".lower()
            if query not in searchable_text:
                continue

        results.append({
            "id": s.get("id"),
            "title": s.get("title"),
            "tags": s.get("tags"),
            "provenance_tier": s.get("provenance_tier"),
            "confirmed_facts": s.get("confirmed_facts"),
            "interview_content": s.get("interview_content"),
            "author_interpretation": s.get("author_interpretation"),
            "unknown_details": s.get("unknown_details"),
            "timeline_sanity": s.get("timeline_sanity")
        })

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


def cmd_check(memory_dir: Path, args: argparse.Namespace) -> int:
    errors = []
    warnings = []

    md_file = memory_dir / "experience" / "story_bank.md"
    usage_file = memory_dir / "experience" / "usage.json"

    if not md_file.exists():
        errors.append(f"Missing canonical story bank: {md_file}")
        sys.stderr.write("\n".join(errors) + "\n")
        return 1

    content = md_file.read_text(encoding="utf-8")
    stories = parse_markdown_stories(content)

    if not stories:
        errors.append("No stories parsed from story_bank.md")

    seen_ids = set()
    for s in stories:
        sid = s.get("id")
        if not sid:
            errors.append(f"Story missing ID in title: {s.get('title')}")
            continue
        if sid in seen_ids:
            errors.append(f"Duplicate story ID: {sid}")
        seen_ids.add(sid)

        if not s.get("confirmed_facts"):
            errors.append(f"{sid}: Missing Confirmed Facts")
        if not s.get("timeline_sanity", "").startswith(("PASS", "TENTATIVE")):
            errors.append(f"{sid}: Invalid Timeline Sanity '{s.get('timeline_sanity')}'")

    if usage_file.exists():
        try:
            usage_data = json.loads(usage_file.read_text(encoding="utf-8"))
            for sid, uses in usage_data.get("story_usage", {}).items():
                if sid not in seen_ids:
                    errors.append(f"usage.json references non-existent story: {sid}")
                for u in uses:
                    if u.get("status") == "DUPLICATE-RISK":
                        warnings.append(f"Duplicate risk for {sid} in chapter {u.get('chapter')}")
        except Exception as e:
            errors.append(f"Invalid JSON in usage.json: {e}")

    if errors:
        sys.stderr.write(f"Check failed with {len(errors)} error(s):\n")
        for err in errors:
            sys.stderr.write(f"  [ERROR] {err}\n")
        return 1

    print(f"Check passed: {len(stories)} stories verified, 0 broken bindings, epistemic fields valid.")
    if warnings:
        for w in warnings:
            print(f"  [WARN] {w}")
    return 0


def natural_sort_key(s: str) -> list[int | str]:
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)]


def find_book_for_chapter(chapter_id: str, book_slug: str | None = None) -> tuple[Path | None, Path | None]:
    repo_root = Path(__file__).resolve().parent.parent.parent
    books_dir = repo_root / "Books"
    if not books_dir.exists():
        return None, None
    if book_slug:
        target = books_dir / book_slug
        if target.exists():
            return target, target / "foundation"
    for b in sorted(books_dir.iterdir()):
        if b.is_dir() and (b / "chapters" / chapter_id).exists():
            return b, b / "foundation"
    return None, None


def get_previous_chapter(chapters_dir: Path, current_chapter_id: str) -> str | None:
    if not chapters_dir.exists():
        return None
    all_chapters = [d.name for d in chapters_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]
    all_chapters.sort(key=natural_sort_key)
    if current_chapter_id not in all_chapters:
        return None
    idx = all_chapters.index(current_chapter_id)
    if idx <= 0:
        return None
    return all_chapters[idx - 1]


def extract_last_200_words(draft_file: Path) -> str:
    if not draft_file.exists():
        return "(không có)"
    text = draft_file.read_text(encoding="utf-8").strip()
    if not text:
        return "(không có)"
    words = text.split()
    if len(words) <= 200:
        return " ".join(words)
    tail_words = words[-200:]
    tail_text = " ".join(tail_words)
    for m in re.finditer(r"[.?!]\s+", tail_text):
        after_text = tail_text[m.end():].strip()
        if len(after_text.split()) >= 100:
            return after_text
    return tail_text


def extract_chapter_summary(summaries_file: Path, prev_chapter_id: str) -> str:
    if not summaries_file.exists():
        return "(không có)"
    content = summaries_file.read_text(encoding="utf-8")
    num_match = re.search(r"\d+", prev_chapter_id)
    if not num_match:
        return "(không có)"
    num_int = int(num_match.group())
    patterns = [
        rf"###\s*Chapter\s*0*{num_int}\s*:[^\n]*\n(.*?)(?=\n###|\Z)",
        rf"###\s*ch_0*{num_int}\b[^\n]*\n(.*?)(?=\n###|\Z)",
    ]
    block = None
    for p in patterns:
        m = re.search(p, content, re.DOTALL | re.IGNORECASE)
        if m:
            block = m.group(1)
            break
    if not block:
        return "(không có)"
    m_payload = re.search(r"-\s*\*\*Tải trọng nhận thức chốt hạ\*\*:\s*([^\n]+)", block)
    if m_payload:
        raw_payload = m_payload.group(1).strip()
        words = raw_payload.split()
        if len(words) > 80:
            payload = " ".join(words[:80]) + "..."
        else:
            payload = raw_payload
        return f"- **Tải trọng nhận thức chốt hạ**: {payload}"
    return "(không có)"


def extract_recent_feedback(feedback_file: Path, limit: int = 5) -> str:
    if not feedback_file.exists():
        return "(không có)"
    content = feedback_file.read_text(encoding="utf-8").strip()
    if not content:
        return "(không có)"
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    if not lines:
        return "(không có)"
    return "\n".join(lines[-limit:])


def extract_ideas_used(ideas_file: Path, target_chapter: str) -> str:
    if not ideas_file.exists():
        return "(không có)"
    content = ideas_file.read_text(encoding="utf-8").strip()
    if not content:
        return "(không có)"

    num_match = re.search(r"\d+", target_chapter)
    target_num = int(num_match.group()) if num_match else 0

    matching_lines = []
    for line in content.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith("#"):
            continue
        prefix = line_str.split("|")[0].strip()
        ch_num_match = re.search(r"\d+", prefix)
        ch_num = int(ch_num_match.group()) if ch_num_match else 0
        if ch_num < target_num:
            matching_lines.append(line_str)

    if not matching_lines:
        return "(không có)"
    if len(matching_lines) > 40:
        matching_lines = matching_lines[-40:]
    return "\n".join(matching_lines)


def cmd_get_writing_context(memory_dir: Path, args: argparse.Namespace) -> int:
    book_dir, foundation_dir = find_book_for_chapter(args.chapter, getattr(args, "book", None))
    if not book_dir:
        print("=== CUOI_CHUONG_TRUOC ===\n(không có)\n=== TOM_TAT_CHUONG_TRUOC ===\n(không có)\n=== PHAN_HOI_TAC_GIA ===\n(không có)\n=== Y_DA_DUNG ===\n(không có)")
        return 0
    chapters_dir = book_dir / "chapters"
    prev_ch = get_previous_chapter(chapters_dir, args.chapter)
    if not prev_ch:
        cuoi_chuong = "(không có)"
        tom_tat = "(không có)"
    else:
        draft_file = chapters_dir / prev_ch / "draft.md"
        cuoi_chuong = extract_last_200_words(draft_file)
        summaries_file = (foundation_dir / "summaries.md") if foundation_dir else Path("non_existent")
        tom_tat = extract_chapter_summary(summaries_file, prev_ch)
    feedback_file = memory_dir / "evolution" / "feedback.jsonl"
    phan_hoi = extract_recent_feedback(feedback_file, limit=5)

    ideas_file = (foundation_dir / "ideas_used.md") if foundation_dir else Path("non_existent")
    ideas_used = extract_ideas_used(ideas_file, args.chapter)

    print(f"=== CUOI_CHUONG_TRUOC ===\n{cuoi_chuong}\n=== TOM_TAT_CHUONG_TRUOC ===\n{tom_tat}\n=== PHAN_HOI_TAC_GIA ===\n{phan_hoi}\n=== Y_DA_DUNG ===\n{ideas_used}")
    return 0


def sanitize_and_format_idea_line(chapter_id: str, ideas: str, images: str) -> str:
    clean_ideas = ideas.replace("|", "/").strip()
    clean_images = images.replace("|", "/").strip()
    line = f"{chapter_id} | ý: {clean_ideas} | hình ảnh: {clean_images}"
    if len(line) > 400:
        line = line[:400].rsplit(" ", 1)[0]
    return line


def record_ideas_used_to_file(ideas_file: Path, chapter_id: str, ideas: str, images: str) -> int:
    new_line = sanitize_and_format_idea_line(chapter_id, ideas, images)
    lines = []
    if ideas_file.exists():
        content = ideas_file.read_text(encoding="utf-8")
        lines = [l for l in content.splitlines() if l.strip()]

    replaced = False
    prefix = f"{chapter_id} |"
    new_lines = []
    for l in lines:
        if l.strip().startswith(prefix):
            new_lines.append(new_line)
            replaced = True
        else:
            new_lines.append(l)

    if not replaced:
        new_lines.append(new_line)

    ideas_file.parent.mkdir(parents=True, exist_ok=True)
    ideas_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return 0


def cmd_record_ideas_used(memory_dir: Path, args: argparse.Namespace) -> int:
    book_dir, foundation_dir = find_book_for_chapter(args.chapter, getattr(args, "book", None))
    if not book_dir or not foundation_dir:
        repo_root = Path(__file__).resolve().parent.parent.parent
        books = [b for b in (repo_root / "Books").iterdir() if b.is_dir()]
        if books:
            book_dir = books[0]
            foundation_dir = book_dir / "foundation"
        else:
            sys.stderr.write("Error: Could not locate book directory.\n")
            return 1

    ideas_file = foundation_dir / "ideas_used.md"
    record_ideas_used_to_file(ideas_file, args.chapter, args.ideas, args.images)
    print(f"Ghi nhận ý đã dùng cho {args.chapter} vào {ideas_file.name}")
    return 0



def normalize_digits(text: str) -> set[str]:
    raw_nums = re.findall(r"\d+(?:[.,]\d+)*", text)
    digits_set = set()
    for rn in raw_nums:
        clean = re.sub(r"[.,]", "", rn)
        if clean:
            digits_set.add(clean)
    return digits_set


def normalize_text_words(text: str) -> list[str]:
    clean = re.sub(r"[^\w\s]", " ", text.lower(), flags=re.UNICODE)
    return [w for w in clean.split() if w]


def build_ground_truth_corpus(book_dir: Path, foundation_dir: Path | None, chapter_id: str) -> str:
    corpus_parts = []
    card_file = book_dir / "chapters" / chapter_id / "card.md"
    if card_file.exists():
        corpus_parts.append(card_file.read_text(encoding="utf-8"))
    if foundation_dir and foundation_dir.exists():
        for fname in ["story_bank.md", "terms.md", "evidence_ledger.md", "summaries.md", "story_bindings.md"]:
            fpath = foundation_dir / fname
            if fpath.exists():
                corpus_parts.append(fpath.read_text(encoding="utf-8"))
    return "\n\n".join(corpus_parts)


def check_provenance_in_sections(sec_dir: Path, ground_truth_corpus: str) -> list[str]:
    if not sec_dir.exists():
        return []
    known_digits = normalize_digits(ground_truth_corpus)
    corpus_norm = " ".join(normalize_text_words(ground_truth_corpus))
    corpus_words = set(corpus_norm.split())

    exempt_prefix_re = re.compile(r"(?:chương|phần|mục|bước|section|ch)\s*$", re.IGNORECASE)
    quote_re = re.compile(r'["“]([^"”\n]+)["”]')

    findings = []
    sec_files = sorted([f for f in sec_dir.iterdir() if f.is_file() and f.suffix == ".md"])
    for sfile in sec_files:
        lines = sfile.read_text(encoding="utf-8").splitlines()
        for line_idx, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            # 1. Check numbers
            for m in re.finditer(r"(\d+(?:[.,]\d+)*)", line):
                num_raw = m.group(1)
                clean_num = re.sub(r"[.,]", "", num_raw)
                start_pos = m.start()
                end_pos = m.end()

                followed_by_pct = (end_pos < len(line) and line[end_pos] == "%")
                prefix_text = line[:start_pos]
                is_exempt_prefix = bool(exempt_prefix_re.search(prefix_text))

                if is_exempt_prefix:
                    continue
                if len(clean_num) == 1 and not followed_by_pct:
                    continue

                if clean_num not in known_digits:
                    token_display = f"{num_raw}%" if followed_by_pct else num_raw
                    findings.append(f"{sfile.as_posix()}:{line_idx}: [SO] {token_display}")

            # 2. Check quotes (5+ words)
            for qm in quote_re.finditer(line):
                quote_text = qm.group(1).strip()
                q_words = normalize_text_words(quote_text)
                if len(q_words) < 5:
                    continue
                q_norm = " ".join(q_words)
                if q_norm in corpus_norm:
                    continue
                matched_count = sum(1 for w in q_words if w in corpus_words)
                ratio = matched_count / len(q_words)
                if ratio < 0.85:
                    findings.append(f'{sfile.as_posix()}:{line_idx}: [TRICH_DAN] "{quote_text}"')

    return findings


def cmd_check_provenance(memory_dir: Path, args: argparse.Namespace) -> int:
    book_dir, foundation_dir = find_book_for_chapter(args.chapter, getattr(args, "book", None))
    if not book_dir:
        sys.stderr.write(f"Error: Chapter {args.chapter} not found in any book.\n")
        return 1
    sec_dir = book_dir / "chapters" / args.chapter / "sections"
    corpus = build_ground_truth_corpus(book_dir, foundation_dir, args.chapter)
    findings = check_provenance_in_sections(sec_dir, corpus)

    if not findings:
        print("PROVENANCE: 0 muc chua co nguon")
        return 0

    print(f"PROVENANCE: {len(findings)} muc chua co nguon")
    for f in findings:
        print(f)
    return 3


def record_baseline_for_chapter(chapter_dir: Path) -> int:
    baseline_dir = chapter_dir / ".baseline"
    if baseline_dir.exists():
        shutil.rmtree(baseline_dir)
    baseline_dir.mkdir(parents=True, exist_ok=True)
    draft_file = chapter_dir / "draft.md"
    if draft_file.exists():
        shutil.copy2(draft_file, baseline_dir / "draft.md")
    sec_dir = chapter_dir / "sections"
    if sec_dir.exists():
        shutil.copytree(sec_dir, baseline_dir / "sections", dirs_exist_ok=True)
    return 0


def compute_chapter_diff(chapter_dir: Path) -> str:
    baseline_dir = chapter_dir / ".baseline"
    if not baseline_dir.exists():
        return ""
    import difflib

    diff_lines = []

    # Check draft.md
    cur_draft = chapter_dir / "draft.md"
    base_draft = baseline_dir / "draft.md"
    if cur_draft.exists() and base_draft.exists():
        c_lines = cur_draft.read_text(encoding="utf-8").splitlines(keepends=True)
        b_lines = base_draft.read_text(encoding="utf-8").splitlines(keepends=True)
        d = list(
            difflib.unified_diff(
                b_lines,
                c_lines,
                fromfile=f"{chapter_dir.name}/.baseline/draft.md",
                tofile=f"{chapter_dir.name}/draft.md",
                n=3,
            )
        )
        if d:
            diff_lines.extend(d)

    # Check sections/*.md
    cur_sec = chapter_dir / "sections"
    base_sec = baseline_dir / "sections"
    if cur_sec.exists() and base_sec.exists():
        for cf in sorted(cur_sec.glob("*.md")):
            bf = base_sec / cf.name
            if bf.exists():
                c_lines = cf.read_text(encoding="utf-8").splitlines(keepends=True)
                b_lines = bf.read_text(encoding="utf-8").splitlines(keepends=True)
                d = list(
                    difflib.unified_diff(
                        b_lines,
                        c_lines,
                        fromfile=f"{chapter_dir.name}/.baseline/sections/{cf.name}",
                        tofile=f"{chapter_dir.name}/sections/{cf.name}",
                        n=3,
                    )
                )
                if d:
                    diff_lines.extend(d)

    if not diff_lines:
        return ""

    if len(diff_lines) > 120:
        truncated = diff_lines[:120]
        truncated.append("... (đã cắt)\n")
        return "".join(truncated)
    return "".join(diff_lines)


def check_diff_with_auto_init(chapter_dir: Path) -> str:
    baseline_dir = chapter_dir / ".baseline"
    if not baseline_dir.exists():
        record_baseline_for_chapter(chapter_dir)
        return "(chưa có mốc)"
    diff_text = compute_chapter_diff(chapter_dir)
    if diff_text:
        record_baseline_for_chapter(chapter_dir)
        return diff_text
    return ""


def check_all_chapters_diff(chapters_dir: Path) -> str:
    if not chapters_dir.exists():
        return ""
    results = []
    all_chapters = sorted(
        [d for d in chapters_dir.iterdir() if d.is_dir() and not d.name.startswith(".")],
        key=lambda d: natural_sort_key(d.name),
    )
    for ch in all_chapters:
        diff_res = check_diff_with_auto_init(ch)
        if diff_res and diff_res != "(chưa có mốc)":
            results.append(f"=== {ch.name} ===\n{diff_res}")
    return "\n".join(results)


def cmd_record_draft_baseline(memory_dir: Path, args: argparse.Namespace) -> int:
    book_dir, _ = find_book_for_chapter(args.chapter, getattr(args, "book", None))
    if not book_dir:
        sys.stderr.write(f"Error: Chapter {args.chapter} not found.\n")
        return 1
    ch_dir = book_dir / "chapters" / args.chapter
    record_baseline_for_chapter(ch_dir)
    print(f"BASELINE: Đã ghi mốc cho {args.chapter}")
    return 0


def cmd_check_draft_diff(memory_dir: Path, args: argparse.Namespace) -> int:
    if getattr(args, "all", False):
        repo_root = Path(__file__).resolve().parent.parent.parent
        books_dir = repo_root / "Books"
        all_output = []
        if books_dir.exists():
            for b in sorted(books_dir.iterdir()):
                if b.is_dir() and (b / "chapters").exists():
                    out = check_all_chapters_diff(b / "chapters")
                    if out:
                        all_output.append(out)
        if not all_output:
            print("DIFF: 0 thay đổi")
        else:
            print("\n".join(all_output))
        return 0

    if not getattr(args, "chapter", None):
        sys.stderr.write("Error: Phải cung cấp --chapter hoặc --all.\n")
        return 1

    book_dir, _ = find_book_for_chapter(args.chapter, getattr(args, "book", None))
    if not book_dir:
        sys.stderr.write(f"Error: Chapter {args.chapter} not found.\n")
        return 1
    ch_dir = book_dir / "chapters" / args.chapter
    diff_res = check_diff_with_auto_init(ch_dir)
    if not diff_res:
        print("DIFF: 0 thay đổi")
    else:
        print(diff_res)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Writing Agent Memory CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # get-voice
    subparsers.add_parser("get-voice", help="Get concise author voice cadence and vocabulary rules")

    # get-story
    p_story = subparsers.add_parser("get-story", help="Get stories filtered by tag or ID with usage history")
    p_story.add_argument("--id", help="Story ID (e.g. S-001)")
    p_story.add_argument("--tag", help="Filter by tag")
    p_story.add_argument("--book-id", help="Book scope ID")

    # record-story-usage
    p_rec = subparsers.add_parser("record-story-usage", help="Record story usage with angle and anti-duplicate check")
    p_rec.add_argument("--id", required=True, help="Story ID")
    p_rec.add_argument("--book-id", help="Book scope ID")
    p_rec.add_argument("--chapter", required=True, help="Chapter ID (e.g. ch_01)")
    p_rec.add_argument("--section", required=True, help="Section ID (e.g. 00_open)")
    p_rec.add_argument("--angle", required=True, help="Narrative angle used")
    p_rec.add_argument("--function", help="Rhetorical function")
    p_rec.add_argument("--key-details", help="Comma-separated details used")

    # get-evidence
    p_ev = subparsers.add_parser("get-evidence", help="Get research evidence items")
    p_ev.add_argument("--id", help="Evidence ID")
    p_ev.add_argument("--tag", help="Filter by tag")

    # get-continuity
    p_cont = subparsers.add_parser("get-continuity", help="Get continuity state")
    p_cont.add_argument("--chapter", help="Target chapter ID for JIT context")
    p_cont.add_argument("--all", action="store_true", help="Dump all raw continuity state")

    # update-continuity
    p_upd = subparsers.add_parser("update-continuity", help="Atomically merge validated chapter_state.json")
    p_upd.add_argument("--state-file", required=True, help="Path to validated chapter_state.json")

    # audit-continuity
    p_aud = subparsers.add_parser("audit-continuity", help="Perform deterministic structural audit")
    p_aud.add_argument("--book-id", help="Book scope ID")

    # capture
    p_cap = subparsers.add_parser("capture", help="Capture quick author insight or story note into memory")
    p_cap.add_argument("--text", required=True, help="Insight or story content")
    p_cap.add_argument("--title", help="Optional title")
    p_cap.add_argument("--tag", help="Comma-separated tags")
    p_cap.add_argument("--target", help="Target filename in memory/experience")

    # find
    p_find = subparsers.add_parser("find", help="Query story bank by keyword or tag")
    p_find.add_argument("--query", help="Keyword search query")
    p_find.add_argument("--tag", help="Tag filter")

    # check
    p_check = subparsers.add_parser("check", help="Verify story vault and binding invariants")
    p_check.add_argument("--book-id", help="Book scope ID")

    # get-writing-context
    p_gwc = subparsers.add_parser("get-writing-context", help="Get preceding chapter context and recent author feedback")
    p_gwc.add_argument("--chapter", required=True, help="Target chapter ID (e.g. ch_02)")
    p_gwc.add_argument("--book", help="Book slug (e.g. nhan-danh-dieu-vi-dai)")

    # check-provenance
    p_prov = subparsers.add_parser("check-provenance", help="Check unsourced numbers and quotes in chapter sections")
    p_prov.add_argument("--chapter", required=True, help="Target chapter ID (e.g. ch_01)")
    p_prov.add_argument("--book", help="Book slug (e.g. nhan-danh-dieu-vi-dai)")

    # record-draft-baseline
    p_rec_base = subparsers.add_parser("record-draft-baseline", help="Record chapter baseline snapshot into .baseline/")
    p_rec_base.add_argument("--chapter", required=True, help="Chapter ID (e.g. ch_01)")
    p_rec_base.add_argument("--book", help="Book slug")

    # record-ideas-used
    p_rec_ideas = subparsers.add_parser("record-ideas-used", help="Record used ideas and images for chapter")
    p_rec_ideas.add_argument("--chapter", required=True, help="Target chapter ID (e.g. ch_01)")
    p_rec_ideas.add_argument("--ideas", required=True, help="Ideas list (semicolon-separated)")
    p_rec_ideas.add_argument("--images", required=True, help="Images or examples list (semicolon-separated)")
    p_rec_ideas.add_argument("--book", help="Book slug")

    # check-draft-diff
    p_chk_diff = subparsers.add_parser("check-draft-diff", help="Check diff against recorded baseline")
    p_chk_diff.add_argument("--chapter", help="Chapter ID (e.g. ch_01)")
    p_chk_diff.add_argument("--all", action="store_true", help="Check diff across all chapters")
    p_chk_diff.add_argument("--book", help="Book slug")

    args = parser.parse_args()
    memory_dir = find_memory_dir()

    dispatch = {
        "get-voice": cmd_get_voice,
        "get-story": cmd_get_story,
        "record-story-usage": cmd_record_story_usage,
        "get-evidence": cmd_get_evidence,
        "get-continuity": cmd_get_continuity,
        "update-continuity": cmd_update_continuity,
        "audit-continuity": cmd_audit_continuity,
        "capture": cmd_capture,
        "find": cmd_find,
        "check": cmd_check,
        "get-writing-context": cmd_get_writing_context,
        "record-ideas-used": cmd_record_ideas_used,
        "check-provenance": cmd_check_provenance,
        "record-draft-baseline": cmd_record_draft_baseline,
        "check-draft-diff": cmd_check_draft_diff,
    }

    handler = dispatch.get(args.command)
    if not handler:
        sys.stderr.write(f"Unknown command: {args.command}\n")
        return 1

    return handler(memory_dir, args)


if __name__ == "__main__":
    sys.exit(main())
