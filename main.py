"""Funniest Time Machine Warning Label — make.fun entry.

Writes one line to /output/entry.txt: the funniest warning label for
a time machine, 120 characters or fewer. The warning is not about
paradoxes or the fabric of time, it is about the one person you
should never meet on a trip to the past: yourself, disappointed, and
asking for money.
"""

import os

ENTRY = (
    "Warning: do not meet your past self. He is you, he is "
    "disappointed, and he will ask to borrow money."
)

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
