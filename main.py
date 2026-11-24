#!/usr/bin/env python3
"""Ship It Friday — the funniest one-line git commit message an AI coding
agent writes right before breaking production on a Friday.

Writes the keeper line to /output/entry.txt (no trailing newline).
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.
"""

import os

ENTRY = "fix: Friday typo, 47 files, 12,003 lines, all of prod, ship it"

# Why this line won the screening (360 candidates, 12 families):
# - P13 numbers ledger + P2 claim-vs-evidence: "typo" vs 12,003 lines.
# - "all of prod" redefines the typo; "ship it" is the second beat:
#   cheerful, confident, completely unaware of the disaster.
# - Friday is explicit: the subject gate requires the Friday setting.
# - 62 chars, punch in the last two words; 47 and 12,003 are specific
#   non-round numbers, so the claim reads true, not invented.


def main() -> None:
    # Self-check the competition's entry gate before writing: UTF-8 text,
    # 1 to 159 characters, not only whitespace.
    text = ENTRY.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 159, "entry outside 1-159 char gate"
    assert text.strip(), "entry is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
