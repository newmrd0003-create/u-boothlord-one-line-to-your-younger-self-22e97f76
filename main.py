"""One Line to Your Younger Self — make.fun entry program (v1).

Writes exactly one file, entry.txt, into MAKEFUN_OUTPUT_DIR
(fallback /output). Writes nothing anywhere else.
"""

import os
import sys

ENTRY = (
    "Keep the mixtape she made you \u2014 in twenty years you'll still hum "
    "the third song at red lights, and you'll finally understand why she chose it."
)


def validate(entry):
    """Return (True, []) if the entry is valid, else (False, [errors])."""
    errors = []
    if not isinstance(entry, str):
        return False, ["entry is not text"]
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8")
    if len(entry) == 0:
        errors.append("entry is empty")
    if len(entry) > 200:
        errors.append("entry is %d characters, over the 200 limit" % len(entry))
    if entry.strip() == "":
        errors.append("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    return (len(errors) == 0), errors


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        for err in errors:
            print("ERROR: %s" % err, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
