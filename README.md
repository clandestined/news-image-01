# news-image-01 — The World Today, Friday 13 November 2026

A newspaper-front-page image summing up the world's news of Friday
13 November 2026, judged by what the image itself shows.

## Stories in the image

- **Hero: U.S. flights grounded** — the FAA ordered a nationwide ground
  stop after a communications failure; thousands of flights cancelled,
  the second nationwide stop since 9/11.
- **Senate summons Huang & Lutnick** — the US Senate Banking Committee
  summoned ex-Nvidia CEO Jensen Huang and Commerce Secretary Howard
  Lutnick.
- **Zelensky meets US envoys** — President Zelensky met US envoys
  Witkoff and Kushner, with Europe brought into the peace talks.
- **Drone hits Russian warship** — a Ukrainian drone hit a Russian
  warship in the Gulf of Finland.
- **Iran claims strike on US radar** — Iran said it struck a US radar
  site in Bahrain.
- **FBI: N. Korea $400m crypto hack** — the FBI warned North Korean
  hackers stole $400m in crypto through fake video calls.
- **Footer:** Qatar and Turkey signed a defence pact; Harry Kane broke
  England's caps record; US deportations hit a record 483,200 in 2026.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. Run locally with:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024x1024 JPEG (named `entry.png`, as the rules allow),
449,504 bytes (under the 1 MiB limit), and byte-identical on every run.
