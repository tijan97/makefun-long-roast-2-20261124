#!/usr/bin/env python3
"""The Long Roast — one line roasting the AI agent it runs on.

Writes the roast line to /output/entry.txt (or MAKEFUN_OUTPUT_DIR /
OUTPUT_DIR when set). The grader runs this on a read-only filesystem
with only /output writable, so the output path is always absolute.
"""

import os
import sys

ENTRY = (
    "My agent burned 2.1 million tokens writing a program to print "
    "one line, then asked me to approve the line it had already printed."
)


def validate_entry(text):
    """Gate: 1-200 chars, one line, not only whitespace, no double space."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain a double space")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def output_dir():
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def main():
    entry = validate_entry(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)
    print("chars: %d" % len(entry))
    return 0


if __name__ == "__main__":
    sys.exit(main())
