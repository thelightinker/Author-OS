#!/usr/bin/env python3
"""
scripts/lint_chapter.py
Convenience wrapper running repair_invariants.py --lint on a chapter directory or section files.
"""
import sys
import subprocess
from pathlib import Path

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    target_path = Path(target)
    if (target_path / "sections").is_dir():
        lint_target = str(target_path / "sections")
    else:
        lint_target = str(target_path)
    
    script = Path(__file__).parent / "repair_invariants.py"
    cmd = [sys.executable, str(script), "--lint", lint_target]
    res = subprocess.run(cmd)
    sys.exit(res.returncode)

if __name__ == "__main__":
    main()
