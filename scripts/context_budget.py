#!/usr/bin/env python3
"""
Context Budget Estimator for Writing Agent Workflow Nodes.
Reads docs/context_budget_map.json and calculates exact token counts per node using tiktoken cl100k_base.
"""

import sys
import json
from pathlib import Path

try:
    import tiktoken
except ImportError:
    print("[ERROR] tiktoken is required. Install via: pip install tiktoken", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.resolve()
MAP_PATH = REPO_ROOT / "docs" / "context_budget_map.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def count_tokens(enc, filepath):
    p = REPO_ROOT / filepath
    if not p.exists():
        return 0, f"[MISSING: {filepath}]"
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
        return len(enc.encode(content)), None
    except Exception as e:
        return 0, f"[ERROR: {e}]"

def main():
    if not MAP_PATH.exists():
        print(f"[ERROR] Map file not found: {MAP_PATH}", file=sys.stderr)
        sys.exit(1)

    enc = tiktoken.get_encoding("cl100k_base")
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))

    # Always on tokens
    always_on_tokens = 0
    always_on_files = data.get("always_on", {}).get("loads", [])
    for f in always_on_files:
        tok, err = count_tokens(enc, f)
        always_on_tokens += tok

    print(f"=== WRITING AGENT CONTEXT BUDGET REPORT ===")
    print(f"Always-On Baseline Tokens: {always_on_tokens:,} tokens ({len(always_on_files)} files)\n")
    print(f"{'Node Name':<28} | {'Agent Tokens':<14} | {'Bundle Tokens':<15} | {'Total Tokens':<14}")
    print("-" * 80)

    for node_name, node_info in data.get("nodes", {}).items():
        agent_path = node_info.get("agent")
        if agent_path and agent_path.startswith(".agents"):
            agent_tok, _ = count_tokens(enc, agent_path)
            agent_label = f"{agent_tok:,}"
        else:
            agent_tok = 0
            agent_label = "0 (L0 Direct)"

        bundle_tok = 0
        for lf in node_info.get("loads", []):
            tok, _ = count_tokens(enc, lf)
            bundle_tok += tok

        total_node_tokens = agent_tok + bundle_tok + always_on_tokens
        print(f"{node_name:<28} | {agent_label:<14} | {bundle_tok:<15,d} | {total_node_tokens:<14,d}")

if __name__ == "__main__":
    main()
