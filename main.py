"""One-Liner Laugh Lab entry.

Writes one original funny line to entry.txt in the output directory.
The line is a fixed string: the program is fully deterministic, so two
runs produce byte-identical output.
"""

import os

LINE = (
    "It looked like dust. It felt like dust. "
    "It screamed like a sock, but by then it was already too late."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
