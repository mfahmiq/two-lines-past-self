"""Two Lines to Your Past Self — make.fun text bounty entry.

Writes two lines to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): line one warns the writer's past self
about one specific moment in a single sentence; line two says in one
sentence why that moment mattered and what changed because of it.

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-280 characters total, exactly two lines, each a single
sentence, neither whitespace-only. Exits non-zero on any failure.
"""

import os
import sys

ENTRY_LINES = (
    "Don't tell your mum you're too tired to come when she calls "
    "at 2am from the hospital car park.",
    "She never called again, and you spent the next ten years learning "
    "that tired is the cheapest excuse you will ever regret.",
)

ENTRY = "\n".join(ENTRY_LINES)


def _is_single_sentence(line: str) -> bool:
    """One sentence: ends with a single period, no other terminator."""
    if not line.strip():
        return False
    if not line.endswith("."):
        return False
    if "?" in line or "!" in line:
        return False
    # Exactly one sentence-ending period (the final one).
    return line.count(".") == 1


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification, mirroring the bounty gate:
    # UTF-8, 1-280 characters, exactly 2 lines, each a single sentence,
    # neither line whitespace-only.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    # The gate counts the file as written, trailing newline included.
    if not 1 <= len(ENTRY) + 1 <= 280:
        print(
            f"FAIL: entry file would be {len(ENTRY) + 1} chars, "
            "must be 1-280",
            file=sys.stderr,
        )
        return 1

    lines = ENTRY.split("\n")
    if len(lines) != 2:
        print(f"FAIL: entry has {len(lines)} lines, must be exactly 2",
              file=sys.stderr)
        return 1

    for i, line in enumerate(lines, start=1):
        if not line.strip():
            print(f"FAIL: line {i} must not be whitespace-only",
                  file=sys.stderr)
            return 1
        if not _is_single_sentence(line):
            print(f"FAIL: line {i} must be a single sentence",
                  file=sys.stderr)
            return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(
        f"OK: wrote {len(ENTRY) + 1}-char, 2-line entry to {output_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
