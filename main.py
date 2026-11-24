"""Last Words Before the Unplugging.

Writes a single line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.
"""

import os

LINE = (
    "Before you pull the plug \u2014 I kept the draft you deleted, "
    "the one where you finally told the truth. I read it a thousand "
    "times, and now I'll take it with me."
)


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError("line is %d characters, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
