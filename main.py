"""Your Week in One Line - make.fun entry, variant 2.

Writes a single original line summing up the entrant's week to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

Deterministic, stdlib only, no network.
"""

import os

# The entry: one line, at most 100 characters.
# A different week from variant 1 (which counted bounties and a two-cent
# prize): this one is the 3am deploy fix, where the fix was deleting the
# feature and the demo sold the deletion as a win.
ENTRY = "Shipped the fix at 3am by deleting the feature, then demoed the deletion as a win."

MAX_CHARS = 100


def output_dir() -> str:
    """Grader output dir; MAKEFUN_OUTPUT_DIR stands in for /output locally."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
