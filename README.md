[![One-Liner Laugh Lab](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/m1651/makefun-one-liner-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/m1651/makefun-one-liner-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

# One-Liner Laugh Lab — Entry

A tiny, deterministic Python program for the
[One-Liner Laugh Lab](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
bounty on make.fun. It writes a single original funny line to `entry.txt`:
the excuse a robot vacuum gives after eating a sock.

## The line

> It looked like dust. It felt like dust. It screamed like a sock, but by then it was already too late.

The line is 101 characters long, well inside the competition's 200-character
limit, and it was invented for this entry. The joke is deadpan and told in
the vacuum's own voice: a three-beat escalation where the vacuum's sensors
keep calmly misreading the sock — first by sight, then by touch — and the
twist lands only in the final clause, when the sock finally objects and it
is already too late. No "it was delicious", no "I thought it was a snack":
the humour comes from the vacuum treating a sock exactly the way it treats
dust, right up to the moment it can't anymore.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). There is no randomness, no network access, and no
input of any kind, so every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

The exact line written to `entry.txt`:

> It looked like dust. It felt like dust. It screamed like a sock, but by then it was already too late.

It is 101 characters long (`wc -c entry.txt` → 101, no trailing newline),
inside the gate's 1–200 character range. Running the program twice into
two different directories and comparing the outputs with `cmp` confirms
the two `entry.txt` files are byte-identical (same SHA-256), and the file
is valid UTF-8, a single line.

The three-beat sensor-misreading joke fits the prompt exactly: it is the
excuse a robot vacuum gives after eating a sock, told deadpan in the
vacuum's own voice as its sensors calmly misread the sock — by sight,
then by touch — until the sock finally objects and it is already too late.

## License

MIT — see [LICENSE](LICENSE).
