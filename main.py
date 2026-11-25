"""Entry for make.fun's "One Star, Five Stars for the Food" bounty.

Writes a single sentence to /output/entry.txt: a one-star review of Earth
from an alien tourist that still slips in a real compliment about the food.
"""

import os

ENTRY = (
    "One star: I waited forty minutes in a queue just to be allowed to eat, "
    "but the dumplings were so good I briefly considered forgiving the whole planet."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.count("\n") == 0, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing space"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
