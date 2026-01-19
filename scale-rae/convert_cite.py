#!/usr/bin/env python3
import re
import sys
from pathlib import Path

CITEP = re.compile(r"~\\citep\{([^}]+)\}")
CITEP_wosimple = re.compile(r"\\citep\{([^}]+)\}")
def replace_citep(text: str, pattern: re.Pattern = CITEP) -> str:
    def repl(m: re.Match) -> str:
        keys = m.group(1)
        parts = [k.strip() for k in keys.split(",")]
        parts = [p for p in parts if p]
        return "".join([f'<d-cite key="{p}"></d-cite>' for p in parts])
    return pattern.sub(repl, text)
def main():
    if len(sys.argv) != 3:
        print("Usage: replace_citep.py input.html output.html", file=sys.stderr)
        sys.exit(2)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    text = in_path.read_text(encoding="utf-8")
    out = replace_citep(text, CITEP)
    out = replace_citep(out, CITEP_wosimple)
    out_path.write_text(out, encoding="utf-8")

if __name__ == "__main__":
    main()
