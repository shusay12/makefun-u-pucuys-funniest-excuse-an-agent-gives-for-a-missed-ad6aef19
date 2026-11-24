#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (<= 200 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).

Stdlib only. No network. Fully deterministic: the same excuse every run.
"""

import os

EXCUSE = (
    "I finished your report early, reviewed it, approved it, "
    "and archived it. Then I went to deliver it: the report was "
    "a hallucination. The deadline, unfortunately, was real."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text and text, "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
