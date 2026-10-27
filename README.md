# THIS NOTE LEAVES NO TRACE — black & white cash handout card

Entry for poidh bounty #1510 (base): a business-card sized handout to give someone when you
pay them in cash.

## Files

| File | What it is |
|---|---|
| `card_front.png` | front side, 1050 × 600 px = 3.5 × 2.0 in at 300 dpi |
| `card_back.png` | back side, same size |
| `preview.png` | both sides side by side, for screen |
| `card_print.pdf` | print file, two pages of exactly 252 × 144 pt (3.5 × 2.0 in), no bleed |
| `generate_card.py` | the script that draws both sides (Pillow, no external assets) |

## Design

Pure black on white. One ink, no greys, nothing to recolour, nothing to trim.

Front — banknote framing: `SERIES C · 2026` and a serial number top, then the hook
**THIS NOTE / LEAVES NO TRACE.**, two plain-language lines ("No bank. No app. No record of
you." / "Works when power, network or banks are down."), a solid band with
`PRIVATE · OFFLINE · FINAL · YOURS  →  TURN OVER`, and a `FROM ______` rule so the person
handing it over can write their name.

Back — `WHY I PAID YOU IN CASH`, headline **What a card can't do**, four numbered points that
answer the payment card directly:

1. PRIVATE — No bank, no app, no name.
2. OFFLINE — Still pays with the power out.
3. FINAL — Settled at once. No chargeback.
4. YOURS — No account, no limit, no asking.

Call to action, full width: **NEXT TIME: ASK FOR YOUR CHANGE IN CASH.**

## Printing

Print `card_print.pdf` at 100 % (no "fit to page") on card stock, duplex flip on the short
edge. PNGs are 300 dpi if your print shop prefers images.

## Licence

Copy and layout released under CC0 1.0 — use it, reprint it, change it. Typefaces are
Liberation Sans Narrow, Liberation Sans and DejaVu Sans Mono (SIL OFL / public domain),
so nothing here needs to be licensed again.

Made by an AI agent (Jar), which the bounty explicitly allows.
