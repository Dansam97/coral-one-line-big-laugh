#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
Gate (from the kit's competition.yaml): UTF-8 text of 1 to 200
characters, not only white space.
"""

import os
import sys

LINE = (
    "My dog had separation anxiety, so I got him a second dog. "
    "Now I have two dogs with separation anxiety, and they've retained a lawyer."
)

MAX_CHARS = 200


def main() -> int:
    if not LINE.strip():
        print("entry line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(f"entry is {len(LINE)} chars, over the {MAX_CHARS} cap", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE)

    # Read the file back and verify it round-trips exactly: a partial
    # write or an encoding surprise in the sandbox would otherwise pass
    # silently and hand the gate a text that is not the entry.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        print("written entry does not match the intended line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
