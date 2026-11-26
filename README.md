# The Houseplant Out of Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/intan151/makefun-houseplant-ooo-01/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/intan151/makefun-houseplant-ooo-01/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

One deterministic Python program (standard library only) writes the
funniest out-of-office auto-reply a houseplant would send — 113
characters — to `/output/entry.txt`.

The entry:

> Out of office indefinitely — I died in March and nobody noticed, which honestly tracks with my watering schedule.

The joke is the plant's own life doing the work: it is not on holiday,
it died in March, and nobody noticed — exactly what its watering
schedule would predict. Status first, like a real auto-reply, then the
grim punchline.

Run it:

```sh
python3 main.py
```

It writes a single line of text to `/output/entry.txt` and asserts the
written file is byte-identical to the entry it defines, inside the
1–120 character gate.

Entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).
