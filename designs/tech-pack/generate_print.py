"""Build print-ready Tee Box dial artwork at true size (28.5 mm).

Run from the repo root:  python3 designs/tech-pack/generate_print.py

Writes to designs/tech-pack/tee-box/:
  tee-box-<variant>-sandwich.svg / .pdf   Layered file for a dial factory. One layer per
                                          print color, plus the cut layer and guides.
  tee-box-<variant>-flat.svg / .pdf       Single flattened image for a one-off "mule"
                                          print on a blank dial (no cutouts).
  proof.svg                               Enlarged proof of both variants with the layer legend.

All text is converted to outlines, so the files do not need the fonts installed.
Geometry comes from the concept in designs/dials/generate.py (dial radius 117 units).
"""
import math
import subprocess
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = Path(__file__).parent
OUT = HERE / "tee-box"
FONTS = HERE / "fonts"

DIAL_MM = 28.5
R = 117.0                      # dial radius in concept units
MM = DIAL_MM / (2 * R)         # millimetres per concept unit
CANVAS = 150                   # half-width of the canvas, in concept units

# Print colors. Hex values are screen references; match to physical swatches before printing.
INK = {
    "base":  ("#f3efe4", "Dial base (top plate lacquer)", "Cream, match to sample"),
    "lower": ("#1f4d36", "Lower plate, seen through the tee cutouts", "Green lacquer"),
    "green": ("#1f4d36", "Pad print 1: minute track, wordmark, model name, cup rim", "Green, approx. Pantone 3435 C"),
    "brass": ("#b98a3f", "Pad print 2: ampersand", "Metallic gold, approx. Pantone 871 C"),
    "ink":   ("#0f1612", "Pad print 3: inside of the cup", "Near-black, approx. Pantone Black 7 C"),
    "white": ("#ffffff", "Pad print 4: golf ball on the 12 tee", "Opaque white"),
    "gray":  ("#a39a86", "Pad print 5: AUTOMATIC, ball outline and dimples", "Warm gray, approx. Pantone Warm Gray 7 C"),
}
CUT = "#e4007c"    # conventional magenta for cut lines
GUIDE = "#00a0e0"  # cyan for non-printing guides

TEE_BIG = "M-7.5,-104 Q0,-99.5 7.5,-104 L6.4,-101 Q2.6,-99.6 2.3,-96 L1.5,-83 L0,-77 L-1.5,-83 L-2.3,-96 Q-2.6,-99.6 -6.4,-101 Z"
TEE_SM = "M-5.5,-104 Q0,-100.8 5.5,-104 L4.7,-101.9 Q2,-100.9 1.7,-98.4 L1.1,-90 L0,-86 L-1.1,-90 L-1.7,-98.4 Q-2,-100.9 -4.7,-101.9 Z"
DATE_APERTURE = (73, -13, 32, 24)   # x, y, w, h in concept units (window at 3)


class Font:
    def __init__(self, path):
        self.f = TTFont(path)
        self.cmap = self.f.getBestCmap()
        self.gs = self.f.getGlyphSet()
        self.upm = self.f["head"].unitsPerEm

    def layout(self, text, size, x, y, spacing=0.0):
        """Return [(char, svg_path)] for text centred on x with its baseline at y."""
        s = size / self.upm
        names = [self.cmap[ord(c)] for c in text]
        widths = [self.gs[n].width * s for n in names]
        total = sum(widths) + spacing * (len(text) - 1)
        cx = x - total / 2
        out = []
        for c, n, w in zip(text, names, widths):
            pen = SVGPathPen(self.gs)
            self.gs[n].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
            out.append((c, pen.getCommands()))
            cx += w + spacing
        return out


def paths(glyphs, fill):
    return "".join(f'<path d="{d}" fill="{fill}"/>' for _, d in glyphs if d)


def tee_uses(date):
    """(path, rotation, y-offset) for each hour marker; no marker at 6 (the cup) or at 3 on the date dial."""
    marks = [(TEE_BIG, 0, 6)]
    for h in range(1, 12):
        if h == 6 or (date and h == 3):
            continue
        marks.append((TEE_BIG if h in (3, 9) else TEE_SM, h * 30, 0))
    return marks


def tee_shapes(date, fill, dx=0.0, dy=0.0, stroke=None):
    attr = f'fill="{fill}"' if stroke is None else f'fill="none" stroke="{stroke}" stroke-width="0.25"'
    return "".join(f'<path d="{d}" {attr} transform="translate({dx} {dy}) rotate({a}) translate(0 {oy})"/>'
                   for d, a, oy in tee_uses(date))


def minute_track(fill):
    """60 ticks, 1 x 5 units, centred on radius 110."""
    return "".join(f'<rect x="-0.5" y="-112.5" width="1" height="5" fill="{fill}" transform="rotate({m * 6})"/>' for m in range(60))


def layer(lid, label, body, hidden=False):
    style = ' style="display:none"' if hidden else ''
    return f'<g id="{lid}" inkscape:groupmode="layer" inkscape:label="{label}"{style}>{body}</g>'


def build(date, flat):
    fr = Font(FONTS / "fraunces-latin-500-normal.woff")
    jo = Font(FONTS / "jost-latin-500-normal.woff")
    word = fr.layout("Fairway & Dials", 14, 0, -50)
    model = fr.layout("Tee Box", 17, 0, -30)
    auto = jo.layout("AUTOMATIC", 8.5, 0, 66, spacing=1.6)
    c = {k: v[0] for k, v in INK.items()}

    ball = (f'<circle cx="0" cy="-103.2" r="5.2" fill="{c["white"]}"/>'
            f'<circle cx="0" cy="-103.2" r="5.2" fill="none" stroke="{c["gray"]}" stroke-width="0.85"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="0.7" fill="{c["gray"]}"/>' for x, y in ((-1.6, -104.6), (1.6, -104.6), (0, -102))))
    cup_rim = f'<ellipse cx="0" cy="92" rx="11" ry="4.5" fill="{c["green"]}"/>'
    cup_in = f'<ellipse cx="0" cy="92.6" rx="8.5" ry="3" fill="{c["ink"]}"/>'
    ax, ay, aw, ah = DATE_APERTURE

    if flat:
        # Everything printed on one blank cream dial; the tee recess is faked with a printed shadow.
        body = (f'<circle r="{R}" fill="{c["base"]}"/>' + minute_track(c["green"])
                + tee_shapes(date, "#8a8170", -1.2, -1.2) + tee_shapes(date, c["green"])
                + ball + cup_rim + cup_in
                + paths([g for g in word if g[0] != "&"], c["green"]) + paths([g for g in word if g[0] == "&"], c["brass"])
                + paths(model, c["green"]) + paths(auto, c["gray"]))
        if date:
            body += (f'<rect x="{ax - 2}" y="{ay - 2}" width="{aw + 4}" height="{ah + 4}" rx="2" fill="{c["ink"]}"/>'
                     f'<rect x="{ax}" y="{ay}" width="{aw}" height="{ah}" rx="1" fill="#ffffff"/>')
        layers = layer("artwork", "Artwork (flattened)", body)
    else:
        layers = (
            layer("lower", "0 Lower plate (seen through cutouts)", f'<circle r="{R}" fill="{c["lower"]}"/>', hidden=True)
            + layer("base", "1 Top plate base color", f'<circle r="{R}" fill="{c["base"]}"/>')
            + layer("cut", "2 CUT through top plate (tees)" + (" + date aperture" if date else ""),
                    tee_shapes(date, CUT) + (f'<rect x="{ax}" y="{ay}" width="{aw}" height="{ah}" rx="1" fill="none" stroke="{CUT}" stroke-width="0.4"/>' if date else ""))
            + layer("print-green", "3 PRINT green", minute_track(c["green"]) + cup_rim + paths([g for g in word if g[0] != "&"], c["green"]) + paths(model, c["green"]))
            + layer("print-brass", "4 PRINT brass", paths([g for g in word if g[0] == "&"], c["brass"]))
            + layer("print-ink", "5 PRINT ink", cup_in)
            + layer("print-white", "6 PRINT white", f'<circle cx="0" cy="-103.2" r="5.2" fill="{c["white"]}"/>')
            + layer("print-gray", "7 PRINT warm gray", paths(auto, c["gray"])
                    + f'<circle cx="0" cy="-103.2" r="5.2" fill="none" stroke="{c["gray"]}" stroke-width="0.85"/>'
                    + "".join(f'<circle cx="{x}" cy="{y}" r="0.7" fill="{c["gray"]}"/>' for x, y in ((-1.6, -104.6), (1.6, -104.6), (0, -102)))))

    mm = lambda v: v / MM
    guides = (f'<circle r="{R}" fill="none" stroke="{GUIDE}" stroke-width="0.3"/>'
              f'<circle r="{mm(1.25)}" fill="none" stroke="{GUIDE}" stroke-width="0.3" stroke-dasharray="1 1"/>'
              f'<line x1="-{R}" y1="0" x2="{R}" y2="0" stroke="{GUIDE}" stroke-width="0.15" stroke-dasharray="2 2"/>'
              f'<line x1="0" y1="-{R}" x2="0" y2="{R}" stroke="{GUIDE}" stroke-width="0.15" stroke-dasharray="2 2"/>'
              f'<line x1="-{R}" y1="128" x2="{R}" y2="128" stroke="{GUIDE}" stroke-width="0.3"/>'
              f'<line x1="-{R}" y1="124" x2="-{R}" y2="132" stroke="{GUIDE}" stroke-width="0.3"/><line x1="{R}" y1="124" x2="{R}" y2="132" stroke="{GUIDE}" stroke-width="0.3"/>'
              f'<text x="0" y="141" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="{GUIDE}">Ø 28.50 mm dial · crown at 3 · centre hole TBC</text>')
    variant = "date (NH35)" if date else "no date (NH38)"
    kind = "flat print for a blank dial" if flat else "sandwich, layered"
    head = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
    title = f'<title>Fairway &amp; Dials Tee Box dial, {variant}, {kind}, true size</title>'
    if flat:
        # The flat file is exactly the dial: 28.5 mm wide, nothing outside it, nothing non-printing.
        return f'{head}width="{DIAL_MM}mm" height="{DIAL_MM}mm" viewBox="{-R} {-R} {2 * R} {2 * R}">{title}{layers}</svg>\n'
    size = 2 * CANVAS * MM
    return (f'{head}width="{size:.3f}mm" height="{size:.3f}mm" viewBox="{-CANVAS} {-CANVAS} {2 * CANVAS} {2 * CANVAS}">'
            f'{title}{layers}{layer("guides", "9 GUIDES (do not print)", guides)}</svg>\n')


def proof():
    """Both sandwich variants enlarged, with layer legend and production notes."""
    parts = ['<rect width="1600" height="1000" fill="#faf8f2"/>',
             '<text x="60" y="80" font-family="Georgia, serif" font-size="40" fill="#1f4d36">Tee Box dial · print proof</text>',
             '<text x="60" y="122" font-family="Helvetica, Arial, sans-serif" font-size="20" fill="#4a564f">Fairway &amp; Dials · 28.5 mm · sandwich construction · shown 10× true size</text>']
    for k, date in enumerate((False, True)):
        svg = build(date, flat=False)
        inner = svg[svg.index(">", svg.index("<svg")) + 1: svg.rindex("</svg>")].replace('style="display:none"', "")
        inner = inner.replace(f'id="lower"', 'id="lower-p"')
        cx = 330 + k * 560
        parts.append(f'<g transform="translate({cx} 470) scale(1.82)">{inner}</g>')
        parts.append(f'<text x="{cx}" y="770" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="24" fill="#1b2620">{"Date · NH35" if date else "No date · NH38"}</text>')
    y = 200
    parts.append('<text x="1190" y="180" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#1b2620">Layers</text>')
    legend = [(INK["base"][0], "Top plate base"), (CUT, "Cut through top plate"), (INK["lower"][0], "Lower plate (through cuts)"),
              (INK["green"][0], "Print: green"), (INK["brass"][0], "Print: brass"), (INK["ink"][0], "Print: ink"),
              (INK["white"][0], "Print: white"), (INK["gray"][0], "Print: warm gray"), (GUIDE, "Guides, not printed")]
    for col, lab in legend:
        y += 38
        parts.append(f'<rect x="1190" y="{y - 22}" width="28" height="28" rx="4" fill="{col}" stroke="#b5ad98" stroke-width="1"/>'
                     f'<text x="1232" y="{y - 1}" font-family="Helvetica, Arial, sans-serif" font-size="19" fill="#1b2620">{lab}</text>')
    notes = ["Proof shows the cut layer in magenta; on the dial the", "green lower plate shows through each tee.",
             "Text is outlined. Colors are screen references:", "match to physical swatches before printing.",
             "Date window position to be confirmed against", "the NH35 date wheel."]
    for i, n in enumerate(notes):
        parts.append(f'<text x="1190" y="{620 + i * 30}" font-family="Helvetica, Arial, sans-serif" font-size="17" fill="#4a564f">{n}</text>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'viewBox="0 0 1600 1000" width="1600" height="1000"><title>Tee Box dial print proof</title>{"".join(parts)}</svg>\n')


SPEC_CSS = """
@font-face { font-family: Fraunces; font-weight: 500; src: url(FONTDIR/fraunces-latin-500-normal.woff); }
@font-face { font-family: Jost; font-weight: 500; src: url(FONTDIR/jost-latin-500-normal.woff); }
@page { size: Letter; margin: 14mm 15mm; }
body { font-family: Jost, Helvetica, Arial, sans-serif; font-size: 9pt; line-height: 1.4; color: #1b2620; }
h1 { font-family: Fraunces, Georgia, serif; font-weight: 500; font-size: 19pt; color: #1f4d36; margin: 0 0 2pt; }
h1 + p { color: #4a564f; margin: 0 0 8pt; border-bottom: 1.5pt solid #b98a3f; padding-bottom: 6pt; }
h2 { font-family: Fraunces, Georgia, serif; font-weight: 500; font-size: 11.5pt; color: #1f4d36; margin: 10pt 0 3pt; break-after: avoid; }
p, ul, ol { margin: 0 0 5pt; } li { margin: 0 0 1.5pt; }
table { border-collapse: collapse; width: 100%; margin: 0 0 4pt; break-inside: avoid; }
th { text-align: left; font-weight: 500; color: #4a564f; border-bottom: 1pt solid #b5ad98; padding: 2.5pt 6pt 2.5pt 0; }
td { border-bottom: 0.5pt solid #e3dccb; padding: 2.5pt 6pt 2.5pt 0; vertical-align: top; }
code { font-size: 8pt; background: #f3efe4; padding: 0 2pt; border-radius: 2pt; }
strong { font-weight: 500; color: #1f4d36; }
.proof { break-before: page; } .proof img { width: 100%; }
"""


def spec_pdf():
    """Render SPEC.md, followed by the proof, to SPEC.pdf (needs Python Playwright with Chromium)."""
    try:
        import markdown
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("skipped SPEC.pdf (needs the markdown and playwright packages)")
        return
    body = markdown.markdown((OUT / "SPEC.md").read_text(), extensions=["tables"])
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{SPEC_CSS.replace("FONTDIR", FONTS.resolve().as_uri())}</style></head>'
            f'<body>{body}<div class="proof"><h2>Print proof</h2><img src="{(OUT / "proof.svg").resolve().as_uri()}"></div></body></html>')
    page_file = OUT / ".spec.html"
    page_file.write_text(html)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(page_file.resolve().as_uri())
            page.wait_for_load_state("networkidle")
            page.pdf(path=str(OUT / "SPEC.pdf"), format="Letter", print_background=True, prefer_css_page_size=True)
            browser.close()
    finally:
        page_file.unlink()
    print((OUT / "SPEC.pdf").relative_to(HERE.parent.parent))


def main():
    OUT.mkdir(exist_ok=True)
    for date in (False, True):
        for flat in (False, True):
            name = f'tee-box-{"date" if date else "no-date"}-{"flat" if flat else "sandwich"}'
            svg = OUT / f"{name}.svg"
            svg.write_text(build(date, flat))
            subprocess.run(["rsvg-convert", "-f", "pdf", "-o", str(OUT / f"{name}.pdf"), str(svg)], check=True)
            print(svg.relative_to(HERE.parent.parent), "+ .pdf")
    (OUT / "proof.svg").write_text(proof())
    print((OUT / "proof.svg").relative_to(HERE.parent.parent))
    spec_pdf()


if __name__ == "__main__":
    main()
