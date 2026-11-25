"""Notes From a Passive-Aggressive Fridge - entry program.

Writes a single funny passive-aggressive note, left by a smart fridge
for its owner, to /output/entry.txt.
The note: Your diet starts Monday, says the note on my door. It is
Thursday. I have stopped believing in Mondays.
"""

import os

LINE = ("Your diet starts Monday, says the note on my door. It is "
        "Thursday. I have stopped believing in Mondays.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
