#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty
u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.

Writes one out-of-office auto-reply (113 characters, <= 120) as if a
houseplant had written it, to /output/entry.txt. Stdlib only,
deterministic: the same text on every run.

The joke: the plant is not on holiday — it died in March and nobody
noticed, which is exactly what its watering schedule would predict.
The plant's own life (watering, neglect, death unnoticed) drives the
joke instead of decorating it, and it reads as a real out-of-office
reply: status first, then the grim punchline.
"""

ENTRY = (
    "Out of office indefinitely \u2014 I died in March and nobody "
    "noticed, which honestly tracks with my watering schedule."
)


def main():
    # Self-check gate: the written file must be byte-identical to the
    # entry this program defines, and inside the 1-120 char gate.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 120, f"written entry is {len(written)} chars"


if __name__ == "__main__":
    main()
