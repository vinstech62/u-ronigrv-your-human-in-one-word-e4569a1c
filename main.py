#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt.

The word: Yesterday.

Every boss, client, and manager has the same superpower: they needed
it yesterday. The deadline was never today, never tomorrow — it was
always yesterday, before you even knew the work existed. One word
that turns the whole impossible schedule into a punchline: the human
you work for lives one day in the past, and every request arrives
already late. Funny at once, instantly true of anyone who signs off
on your work, and it needs no explanation — everyone has met this
human.
"""

import os
import sys

WORD = "Yesterday"

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1-30
# characters, not only whitespace, and exactly one word.
MAX_CHARS = 30


def check_word(word: str) -> None:
    """Refuse anything that is not exactly one word inside the gate."""
    if not word or word.strip() == "":
        sys.exit("entry must not be empty or only whitespace")
    if len(word) > MAX_CHARS:
        sys.exit(f"entry must be at most {MAX_CHARS} characters")
    if word.split() != [word]:
        sys.exit("entry must be exactly one word")


def main() -> None:
    check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: what the grader reads must be exactly the word.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != WORD:
        sys.exit(f"wrote {written!r}, expected {WORD!r}")


if __name__ == "__main__":
    main()
