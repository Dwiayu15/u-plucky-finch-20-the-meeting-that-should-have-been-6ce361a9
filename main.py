"""One-line joke entry: The Meeting That Should Have Been an Email.

Writes a single joke line to /output/entry.txt and checks it against the
sealed gate: UTF-8 text, 1-200 characters, a single line, not only
whitespace.
"""

import os

ENTRY = (
    # The joke's turn lands on the last word: a meeting that produces
    # nothing but its own sequel, a calendar invite titled "Follow-up".
    "We spent an hour deciding when to meet again, then sent an invite "
    "titled 'Follow-up' \u2014 the meeting's only deliverable was its own sequel."
)


def validate(text):
    """Return True when *text* passes the sealed gate."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


def self_test():
    print("characters:", len(ENTRY))
    assert validate(ENTRY), "entry failed the gate"
    print("gate: PASS")


if __name__ == "__main__":
    main()
    self_test()
