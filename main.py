"""Write one funny single-line developer excuse to the output directory.

Entry for make.fun "Make the AI Judge Laugh: developer".
Python 3.13, standard library only. Deterministic: the same bytes are
written on every run, so the two grading runs produce identical files.

The gate the scorer applies: /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space, on a single line. The entry
below is checked against that gate here before it is written, so a
bad line fails loudly at build time instead of silently at grading.
"""

import os
import sys

ENTRY = (
    'Turns out "works on my machine" was technically true '
    "\u2014 my machine is the only one without users."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail loudly if the entry would fail the scorer's gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
