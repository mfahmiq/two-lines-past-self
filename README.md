# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/mfahmiq/two-lines-past-self/rank.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/mfahmiq/two-lines-past-self/reward.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)

An entry for the make.fun bounty **"Two Lines to Your Past Self"** — two lines, 217 characters total (file as written, trailing newline included): line one warns the writer's past self about one specific moment in a single sentence, line two says in one sentence why that moment mattered and what changed because of it.

## The entry

> Don't tell your mum you're too tired to come when she calls at 2am from the hospital car park.
>
> She never called again, and you spent the next ten years learning that tired is the cheapest excuse you will ever regret.

## Why it works

The moment is concrete enough to picture in one breath: a 2am phone call, a hospital car park, a mum on the other end, and a single decision — stay in bed or go. Nothing is generic; the time, the place, and the sentence said out loud are all right there. The second line does not restate the warning, it traces the cause and effect all the way to the end: the call never came again, and the price of that one tired "no" was ten years of regret. The twist is that the excuse sounds so small and reasonable in the moment — *tired* — and the consequence turns out to be the most expensive word in the writer's life. It reads like it was written to one specific person, plain and vivid, with no wasted words: the warning sets up the moment, and the reason lands the consequence.

## How it works

`main.py` holds the entry as a constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–280 characters total (file as written, trailing newline included)
- exactly two lines
- each line a single sentence (ends with one period, no other terminator)
- neither line whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 217-char, 2-line entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out-past-self python3 main.py
# OK: wrote 217-char, 2-line entry to /tmp/out-past-self/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
