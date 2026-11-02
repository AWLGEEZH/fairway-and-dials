# Tee Box dial: supplier specification

Fairway & Dials · dial for a 38–40 mm field watch · version 1, November 2026

## Request

Please quote:

1. **Samples:** 3 pieces of each variant below, with sample cost and lead time.
2. **Production:** unit price at 100 and 300 pieces per variant, plus any printing plate or tooling cost, MOQ and payment terms.

Artwork is supplied at true size with all text converted to outlines. Please confirm whether you can hold the minimum feature sizes listed under Critical dimensions.

## Dial

| Item | Specification |
|---|---|
| Diameter | 28.50 mm |
| Movement | Seiko NH38 (no date) or NH35 (date). Dial feet and centre hole to the movement standard. |
| Crown position | 3 o'clock |
| Construction | Sandwich: cream top plate with the hour markers cut through; green lower plate visible through the cuts |
| Top plate finish | Matte lacquer, cream (screen reference `#f3efe4`); match to our approved swatch |
| Lower plate finish | Matte lacquer, green (`#1f4d36`). Please also quote a lume-filled lower plate (C3 or BGW9) as an option. |
| Total thickness | Please recommend; tell us what the movement and case allow |

## Variants

| Variant | Movement | Difference |
|---|---|---|
| No date | NH38 | Large tee marker at 3 |
| Date | NH35 | Date aperture at 3 replaces the tee: 3.90 × 2.92 mm, centred 10.84 mm from the dial centre, with a 0.24 mm printed ink frame. Please confirm the position against the NH35 date wheel. |

## Print colors

Five pad-print colors on the top plate. Hex values are screen references only; Pantone values are suggested starting points. Please match to physical swatches and send a color proof before the run.

| # | Color | Screen | Suggested | Prints |
|---|---|---|---|---|
| 1 | Green | `#1f4d36` | Pantone 3435 C | Minute track, "Fairway", "Dials", "Tee Box", rim of the cup at 6 |
| 2 | Brass | `#b98a3f` | Pantone 871 C (metallic) | The ampersand in the wordmark |
| 3 | Ink | `#0f1612` | Pantone Black 7 C | Inside of the cup at 6; date window frame |
| 4 | White | `#ffffff` | Opaque white | Golf ball on the 12 o'clock tee |
| 5 | Warm gray | `#a39a86` | Pantone Warm Gray 7 C | "AUTOMATIC"; ball outline and dimples |

Cost option: if five colors is expensive, ink and green can merge (cup and frame printed green), leaving four.

## Critical dimensions

| Feature | Size |
|---|---|
| Minute track | 60 ticks, 0.12 × 0.61 mm, centred on a 13.40 mm radius |
| Tee markers (cut) | Large: 3.29 mm long, 1.83 mm head (at 12, 3, 9). Small: 2.19 × 1.34 mm. The pointed tips may be blunted slightly if needed. |
| Golf ball | 1.27 mm diameter, white, sitting on the 12 o'clock tee |
| Cup at 6 | 2.68 × 1.10 mm ellipse, centred 11.21 mm below the dial centre |
| "Fairway & Dials" | Fraunces, cap height 1.19 mm, baseline 6.09 mm above centre |
| "Tee Box" | Fraunces, cap height 1.45 mm, baseline 3.65 mm above centre |
| "AUTOMATIC" | Jost, cap height 0.72 mm, baseline 8.04 mm below centre |
| Thinnest printed line | 0.10 mm (ball outline). The wordmark's serif hairlines are finer; tell us if they need thickening. |

## Hands (for reference)

Hands are quoted separately, but the dial is designed around them:

- **Hour and minute:** dark ink batons with a cream lume stripe.
- **Seconds:** thin dark ink hand with a small brass pennant 5.1–6.6 mm from the centre. Its tip must reach the cup at 6: about 11.5 mm from the centre. At 30 seconds the hand reads as a flagstick standing in the cup.
- **Centre cap:** white, styled as a golf ball.

## Files

In `designs/tech-pack/tee-box/`:

| File | Use |
|---|---|
| `tee-box-no-date-sandwich.pdf` / `.svg` | Factory artwork, no date. One layer per print color, a magenta cut layer and non-printing cyan guides. |
| `tee-box-date-sandwich.pdf` / `.svg` | Factory artwork, date. |
| `tee-box-no-date-flat.pdf` / `.svg` | One flattened image, exactly 28.5 mm wide, for printing onto a blank dial (prototype "mule"). |
| `tee-box-date-flat.pdf` / `.svg` | The same for a blank dial with a date window at 3. |
| `proof.svg` | Enlarged proof of both variants with the layer legend. |

The SVG layers open as named layers in Illustrator and Inkscape. Rebuild every file with `python3 designs/tech-pack/generate_print.py`.
