"""One line that sums up a week, written out for the make.fun judge.

This is variant 2 of the entry. The program does a small, fixed job:
take the single line below, make sure it fits the competition's shape
rules, and drop it into a file called entry.txt inside the output
folder the grader provides. Nothing is fetched, nothing is random,
and nothing changes from one run to the next.
"""

import os

# The one line this entry submits. It stays exactly as written here:
# a single line of at most one hundred characters, kept verbatim.
ENTRY = "Shipped the fix at 3am by deleting the feature, then demoed the deletion as a win."

# Upper bound on how long the submitted line may be.
CHAR_LIMIT = 100


def build_entry() -> str:
    """Return the week's line, trimmed of any surrounding whitespace."""
    return ENTRY.strip()


def check_line(line: str) -> str:
    """Confirm the line obeys the shape rules, then hand it back.

    The line must be a single line, and it must be between one and
    CHAR_LIMIT characters long once trimmed.
    """
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError(f"entry is {len(line)} chars, limit is {CHAR_LIMIT}")
    return line


def resolve_output_dir() -> str:
    """Work out where entry.txt should go.

    The grader hands the program /output. When running it by hand,
    setting MAKEFUN_OUTPUT_DIR points it somewhere else instead.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Save the checked line to entry.txt in the output folder."""
    folder = resolve_output_dir()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main() -> None:
    line = check_line(build_entry())
    write_entry(line)


if __name__ == "__main__":
    main()
