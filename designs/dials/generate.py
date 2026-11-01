"""Generate the Fairway & Dials dial concepts as SVG files.

Run from the repo root:  python3 designs/dials/generate.py
Writes one SVG per model and date option into designs/dials/links/ and
designs/dials/tool/, plus a contact sheet at designs/dials/collection-sheet.svg.
Every dial is drawn around (0, 0) with a 117-unit dial radius, so all files share
the same scale.
"""
from pathlib import Path

OUT = Path(__file__).parent

GREEN, BRASS, CREAM, INK, MUTED = "#1f4d36", "#b98a3f", "#f3efe4", "#1b2620", "#4a564f"
LUME, RECESS = "#e6dcb8", "#0e1611"

def hands(hid, color, sec_angle):
    """Hour and minute hands are plain with lume; the seconds hand carries the brass flag near the center."""
    return (f'<g id="{hid}"><g transform="rotate(305)"><rect x="-5" y="-56" width="10" height="60" rx="2" fill="{color}"/><rect x="-2" y="-50" width="4" height="40" fill="{LUME}"/></g>'
            f'<g transform="rotate(63)"><rect x="-3" y="-90" width="6" height="94" rx="2" fill="{color}"/><rect x="-1.2" y="-82" width="2.4" height="66" fill="{LUME}"/></g>'
            f'<g transform="rotate({sec_angle})"><rect x="-0.9" y="-94.5" width="1.8" height="116" fill="{color}"/><circle cx="0" cy="20" r="3" fill="{color}"/>'
            f'<polygon points="0.9,-54 17,-48 0.9,-42" fill="{BRASS}"/></g><use href="#ball" transform="scale(0.86)"/></g>')


DEFS = f"""<style>@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@500&amp;family=Jost:wght@300;500&amp;display=swap');.fr{{font-family:Fraunces,Georgia,serif}}.jo{{font-family:Jost,Helvetica,sans-serif}}.jl{{font-family:Jost,Helvetica,sans-serif;font-weight:300}}</style>
<defs>
<clipPath id="fwclip"><circle r="117"/></clipPath>
<g id="ball"><circle r="7" fill="#ffffff" stroke="#9a9a9a" stroke-width="0.5"/><circle cx="-2" cy="-2" r="0.9" fill="#c8c8c8"/><circle cx="2" cy="-2" r="0.9" fill="#c8c8c8"/><circle cx="0" cy="2" r="0.9" fill="#c8c8c8"/></g>
{hands("handsL", CREAM, 200)}
{hands("handsD", INK, 200)}
<g id="sticks">{''.join(f'<rect x="-4" y="-107" width="8" height="21" rx="1" transform="rotate({a})"/>' for a in (30, 60, 120, 150, 210, 240, 300, 330))}</g>
<g id="n4" class="fr" text-anchor="middle" style="font-size:28px"><text x="0" y="-70">12</text><text x="88" y="9">3</text><text x="0" y="96">6</text><text x="-88" y="9">9</text></g>
<g id="n39" class="fr" text-anchor="middle" style="font-size:28px"><text x="88" y="9">3</text><text x="-88" y="9">9</text></g>
<g id="n19" class="fr" text-anchor="middle" style="font-size:22px"><text x="41" y="-63">1</text><text x="71" y="-33">2</text><text x="88" y="9" style="font-size:28px">3</text><text x="71" y="49">4</text><text x="41" y="79">5</text><text x="0" y="96" style="font-size:28px">6</text><text x="-41" y="79">7</text><text x="-71" y="49">8</text><text x="-88" y="9" style="font-size:28px">9</text></g>
<g id="n12"><use href="#n19"/><g class="fr" text-anchor="middle" style="font-size:22px"><text x="-71" y="-33">10</text><text x="-41" y="-63">11</text><text x="0" y="-70" style="font-size:28px">12</text></g></g>
<path id="tee-big" d="M-7.5,-104 Q0,-99.5 7.5,-104 L6.4,-101 Q2.6,-99.6 2.3,-96 L1.5,-83 L0,-77 L-1.5,-83 L-2.3,-96 Q-2.6,-99.6 -6.4,-101 Z"/>
<path id="tee-sm" d="M-5.5,-104 Q0,-100.8 5.5,-104 L4.7,-101.9 Q2,-100.9 1.7,-98.4 L1.1,-90 L0,-86 L-1.1,-90 L-1.7,-98.4 Q-2,-100.9 -4.7,-101.9 Z"/>
<g id="tees"><use href="#tee-big" transform="translate(0 6)"/>{''.join(f'<use href="#tee-{"big" if a in (90, 270) else "sm"}" transform="rotate({a})"/>' for a in (30, 60, 90, 120, 150, 210, 240, 270, 300, 330))}</g>
{hands("handsT", INK, 180)}
<g id="handsC"><g transform="rotate(305)"><polygon points="0,-60 5,-10 0,4 -5,-10" fill="{BRASS}"/><polygon points="0,-60 0,4 -5,-10" fill="#d6b06a"/></g><g transform="rotate(63)"><polygon points="0,-98 4,-12 0,4 -4,-12" fill="{BRASS}"/><polygon points="0,-98 0,4 -4,-12" fill="#d6b06a"/></g><g transform="rotate(200)"><rect x="-0.8" y="-96" width="1.6" height="116" fill="{CREAM}"/><circle cx="0" cy="20" r="3" fill="{CREAM}"/><polygon points="0.8,-54 17,-48 0.8,-42" fill="{BRASS}"/></g><use href="#ball" transform="scale(0.86)"/></g>
<g id="datewin"><rect x="71" y="-15" width="36" height="28" rx="2" fill="{RECESS}"/><rect x="73" y="-13" width="32" height="24" rx="1" fill="{CREAM}"/><text class="jo" x="89" y="6" text-anchor="middle" style="fill:{INK};font-size:18px">31</text></g>
<g id="idx"><circle cx="36" cy="-62.35" r="5.5"/><circle cx="62.35" cy="-36" r="5.5"/><circle cx="62.35" cy="36" r="5.5"/><circle cx="36" cy="62.35" r="5.5"/><circle cx="-36" cy="62.35" r="5.5"/><circle cx="-62.35" cy="36" r="5.5"/><circle cx="-62.35" cy="-36" r="5.5"/><circle cx="-36" cy="-62.35" r="5.5"/><rect x="58" y="-4" width="20" height="8" rx="1"/><rect x="-78" y="-4" width="20" height="8" rx="1"/><rect x="-4" y="58" width="8" height="20" rx="1"/><polygon points="-10,-82 10,-82 0,-66"/></g>
<g id="divehands"><g transform="rotate(305)"><rect x="-5.5" y="-46" width="11" height="50" rx="2" fill="{CREAM}"/><rect x="-2.5" y="-40" width="5" height="32" fill="{LUME}"/></g><g transform="rotate(60)"><rect x="-2.5" y="-80" width="5" height="84" rx="2" fill="{CREAM}"/><rect x="-1" y="-72" width="2" height="58" fill="{LUME}"/></g><g transform="rotate(200)"><rect x="-0.9" y="-86" width="1.8" height="106" fill="{CREAM}"/><circle cx="0" cy="20" r="3" fill="{CREAM}"/><polygon points="0.9,-50 15,-44.5 0.9,-39" fill="{BRASS}"/></g><use href="#ball" transform="scale(0.86)"/></g>
</defs>"""


def case(dial_fill):
    return f'<rect x="123" y="-9" width="13" height="18" rx="2" fill="#8a8a8a"/><circle r="126" fill="#a8a8a8"/><circle r="117" fill="{dial_fill}"/>'


def track(color, r=110):
    gap = 2 * 3.14159265 * r / 60 - 1
    return f'<circle r="{r}" fill="none" stroke="{color}" stroke-width="5" stroke-dasharray="1 {gap:.2f}" stroke-dashoffset="0.5" transform="rotate(-90)"/>'


def cut(ref, lume, recess=RECESS):
    """A sandwich cutout: the recess wall, then the lume layer seen through it."""
    return f'<use href="#{ref}" fill="{recess}" transform="translate(-1.5 -1.5)"/><use href="#{ref}" fill="{lume}"/>'


def text_block(name, word_c, name_c, auto_c, top=-50, y1=-30, y2=66, wsize=14, nsize=17, asize=8.5):
    """Wordmark under 12, model name beneath it, and a faint light-weight Automatic above 6."""
    return (f'<text class="fr" x="0" y="{top}" text-anchor="middle" style="fill:{word_c};font-size:{wsize}px">Fairway <tspan style="fill:{BRASS}">&amp;</tspan> Dials</text>'
            f'<text class="fr" x="0" y="{y1}" text-anchor="middle" style="fill:{name_c};font-size:{nsize}px">{name}</text>'
            f'<text class="jl" x="0" y="{y2}" text-anchor="middle" style="fill:{auto_c};font-size:{asize}px;letter-spacing:1.6px">AUTOMATIC</text>')


# Links collection (field). Each returns (dial body, hands id).
def bunker():
    grooves = ''.join(f'<circle r="{r}"/>' for r in (22, 38, 54, 70, 86, 102))
    return (case("#d8c296") + f'<g fill="none" stroke="#c4ab78" stroke-width="2">{grooves}</g>'
            + cut("sticks", "#2f6b4a", "#6b5a3a") + cut("n4", "#2f6b4a", "#6b5a3a")
            + text_block("Bunker", INK, INK, "#8f7b55")), "handsD"


def fairway_stripe():
    stripes = ''.join(f'<rect x="{x}" y="-117" width="26" height="234" fill="{GREEN if i % 2 == 0 else "#2a6146"}"/>'
                      for i, x in enumerate(range(-117, 117, 26)))
    return ('<rect x="123" y="-9" width="13" height="18" rx="2" fill="#8a8a8a"/><circle r="126" fill="#a8a8a8"/>' + f'<g clip-path="url(#fwclip)">{stripes}</g>'
            + cut("sticks", LUME) + cut("n4", LUME) + text_block("Fairway Stripe", CREAM, CREAM, "#9fb5a6")), "handsL"


def pin_high():
    flag_recess = f'<g fill="{RECESS}" transform="translate(-1.5 -1.5)"><rect x="-2.5" y="-106" width="5" height="40"/><polygon points="2.5,-106 26,-98 2.5,-90"/><ellipse cx="0" cy="84" rx="20" ry="8"/></g>'
    flag = f'<g fill="{LUME}"><rect x="-1.5" y="-104.5" width="3" height="37"/><polygon points="1.5,-104.5 24,-97 1.5,-89.5" fill="{BRASS}"/><ellipse cx="0" cy="84" rx="18" ry="6.5"/></g>'
    return (case(GREEN) + track(CREAM, 108) + cut("sticks", LUME) + flag_recess + flag + cut("n39", LUME)
            + text_block("Pin High", CREAM, CREAM, "#9fb5a6")), "handsL"


def tee_box():
    """Realistic tee markers, a ball on the 12 tee, and a printed cup at 6.
    The seconds hand carries the flag; at :30 it stands in the cup."""
    ball = ('<circle cx="0" cy="-103.2" r="5.2" fill="#ffffff" stroke="#9a9a9a" stroke-width="0.6"/>'
            '<circle cx="-1.6" cy="-104.6" r="0.7" fill="#c8c8c8"/><circle cx="1.6" cy="-104.6" r="0.7" fill="#c8c8c8"/><circle cx="0" cy="-102" r="0.7" fill="#c8c8c8"/>')
    cup = f'<ellipse cx="0" cy="92" rx="11" ry="4.5" fill="{GREEN}"/><ellipse cx="0" cy="92.6" rx="8.5" ry="3" fill="#0f1612"/>'
    return (case(CREAM) + track(GREEN)
            + f'<use href="#tees" fill="#8a8170" transform="translate(-1.2 -1.2)"/><use href="#tees" fill="{GREEN}"/>'
            + ball + cup + text_block("Tee Box", GREEN, GREEN, "#a39a86")), "handsT"


def caddie():
    """A faint tone-on-tone caddie bib printed behind the numerals, with a bib number."""
    bib = ('<path d="M-40,-6 L-22,-12 Q0,10 22,-12 L40,-6 L36,22 Q30,30 34,40 L38,82 L-38,82 L-34,40 Q-30,30 -36,22 Z" '
           'fill="#ebe3cf" stroke="#ddd3bb" stroke-width="0.8"/>'
           '<text class="jo" x="0" y="42" text-anchor="middle" style="fill:#d8cdb2;font-size:34px">1</text>')
    return (case(CREAM) + bib + track(GREEN) + cut("n12", GREEN, "#8a8170")
            + text_block("Caddie", GREEN, GREEN, "#a39a86")), "handsD"


def dawn_patrol():
    rail = (f'<circle r="112" fill="none" stroke="{CREAM}" stroke-width="0.8"/><circle r="104" fill="none" stroke="{CREAM}" stroke-width="0.8"/>'
            f'<circle r="108" fill="none" stroke="{CREAM}" stroke-width="8" stroke-dasharray="0.8 10.51" stroke-dashoffset="0.4" transform="rotate(-90)"/>')
    return (case(INK) + rail + cut("n12", "#e8c48a", "#0a0f0c")
            + text_block("Dawn Patrol", CREAM, "#e8c48a", "#8a948d")), "handsL"


def front_nine():
    """Hours 1 to 9 (the front nine) are sandwich lume; 10, 11 and 12 are printed in brass."""
    back = (f'<g class="fr" text-anchor="middle" style="font-size:22px" fill="{BRASS}">'
            '<text x="-71" y="-33">10</text><text x="-41" y="-63">11</text><text x="0" y="-70" style="font-size:28px">12</text></g>')
    return (case(GREEN) + track(CREAM) + cut("n19", LUME) + back
            + text_block("Front Nine", CREAM, CREAM, "#9fb5a6")), "handsL"


def clubhouse():
    """The 19th hole: a dressier finale. Applied brass batons instead of sandwich lume,
    brass dauphine hands, and a tiny brass 19 in place of the 19th minute tick."""
    import math
    ticks = ''.join(
        f'<line x1="{math.sin(math.radians(m * 6)) * 108:.2f}" y1="{-math.cos(math.radians(m * 6)) * 108:.2f}" '
        f'x2="{math.sin(math.radians(m * 6)) * 112:.2f}" y2="{-math.cos(math.radians(m * 6)) * 112:.2f}"/>'
        for m in range(60) if m != 19)
    a = math.radians(19 * 6)
    nineteen = (f'<text class="jo" x="{math.sin(a) * 110:.1f}" y="{-math.cos(a) * 110:.1f}" text-anchor="middle" '
                f'dominant-baseline="central" style="fill:{BRASS};font-size:6.5px">19</text>')
    baton = '<rect x="-3" y="-104" width="6" height="22" rx="0.8"/>'
    batons = ''.join(f'<g transform="rotate({h * 30})">{baton}</g>' for h in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    double12 = '<rect x="-8" y="-104" width="5.5" height="24" rx="0.8"/><rect x="2.5" y="-104" width="5.5" height="24" rx="0.8"/>'
    shine = ''.join(f'<g transform="rotate({h * 30})"><rect x="-0.6" y="-102" width="1.2" height="18" fill="#e3c27e"/></g>' for h in range(1, 12))
    return (case("#16382a") + f'<g stroke="{BRASS}" stroke-width="0.9">{ticks}</g>' + nineteen
            + f'<g fill="#0b1d15" transform="translate(1.2 1.2)">{batons}{double12}</g>'
            + f'<g fill="{BRASS}">{batons}{double12}</g>' + shine
            + text_block("Clubhouse", CREAM, BRASS, "#6f8a7b")), "handsC"


# Tool collection (diver). First model: Marker, with a stroke-counter bezel and a hole-counter inner ring.
RING = [(0, -93), (33.2, -87.2), (62.4, -70.3), (84, -44.5), (95.5, -12.8), (95.5, 20.8), (84, 52.5), (62.4, 78.3), (33.2, 95.2),
        (0, 101), (-33.2, 95.2), (-62.4, 78.3), (-84, 52.5), (-95.5, 20.8), (-95.5, -12.8), (-84, -44.5), (-62.4, -70.3), (-33.2, -87.2)]


def marker(date=False):
    holes = ''.join(f'<text x="{x}" y="{y - 4}" dominant-baseline="central"{" fill=\"" + BRASS + "\"" if n == 1 else ""}>{n}</text>' for n, (x, y) in enumerate(RING, 1))
    bezel = ''.join(f'<text x="{x}" y="{y}" dominant-baseline="central">{t}</text>' for t, x, y in
                    (("20", 100.5, -58), ("40", 100.5, 58), ("60", 0, 116), ("80", -100.5, 58), ("100", -100.5, -58)))
    date_win = (f'<rect x="54" y="-12" width="30" height="24" rx="2" fill="{RECESS}"/><rect x="56" y="-10" width="26" height="20" rx="1" fill="{CREAM}"/>'
                f'<text class="jo" x="69" y="6" text-anchor="middle" style="fill:{INK};font-size:15px">31</text>') if date else ""
    return ('<g fill="#8a8a8a"><rect x="0" y="-8" width="13" height="16" rx="2" transform="translate(116 -67) rotate(-30)"/>'
            '<rect x="0" y="-8" width="13" height="16" rx="2" transform="translate(116 67) rotate(30)"/></g>'
            f'<circle r="137" fill="#a8a8a8"/><circle r="131" fill="{GREEN}"/>'
            f'<circle r="127" fill="none" stroke="{CREAM}" stroke-width="3" stroke-dasharray="1 5.65" stroke-dashoffset="0.5" transform="rotate(-90)"/>'
            f'<polygon points="-8,-129 8,-129 0,-115" fill="{BRASS}"/>'
            f'<g class="jo" text-anchor="middle" style="font-size:13px" fill="{CREAM}">{bezel}</g>'
            f'<circle r="105.5" fill="{RECESS}"/><circle r="97" fill="none" stroke="{CREAM}" stroke-width="14"/>'
            f'<g class="jo" text-anchor="middle" style="font-size:14px" fill="{INK}">{holes}</g>'
            f'<circle r="90" fill="#3b4043"/>'
            f'<circle r="86" fill="none" stroke="{CREAM}" stroke-width="4" stroke-dasharray="0.8 8.2" stroke-dashoffset="0.4" transform="rotate(-90)"/>'
            + cut("idx", LUME, "#141618") + date_win
            + text_block("Marker", CREAM, CREAM, "#8e9497", top=-44, y1=-28, y2=48, wsize=11, nsize=13, asize=7) + '<use href="#divehands"/>')


LINKS = [("bunker", "Bunker", bunker), ("fairway-stripe", "Fairway Stripe", fairway_stripe), ("pin-high", "Pin High", pin_high),
         ("tee-box", "Tee Box", tee_box), ("caddie", "Caddie", caddie), ("dawn-patrol", "Dawn Patrol", dawn_patrol),
         ("front-nine", "Front Nine", front_nine), ("clubhouse", "Clubhouse", clubhouse)]


def field_dial(fn, date):
    body, hands = fn()
    return body + ('<use href="#datewin"/>' if date else '') + f'<use href="#{hands}"/>'


def standalone(body, title, half=145):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-half} {-half} {2 * half} {2 * half}" width="{4 * half}" height="{4 * half}">'
            f'<title>{title}</title>{DEFS}{body}</svg>\n')


def main():
    files = []
    for slug, name, fn in LINKS:
        for date in (False, True):
            path = OUT / "links" / f"{slug}-{'date' if date else 'no-date'}.svg"
            path.parent.mkdir(exist_ok=True)
            path.write_text(standalone(field_dial(fn, date), f"Fairway &amp; Dials Links {name}, {'date' if date else 'no date'}"))
            files.append(path)
    for date in (False, True):
        path = OUT / "tool" / f"marker-{'date' if date else 'no-date'}.svg"
        path.parent.mkdir(exist_ok=True)
        path.write_text(standalone(marker(date), f"Fairway &amp; Dials Marker, {'date' if date else 'no date'}"))
        files.append(path)

    # Contact sheet: four columns (two models per row, no date then date).
    W, cell_w, cell_h, s = 800, 200, 210, 0.62
    parts = [f'<rect width="{W}" height="100%" fill="#faf8f2"/>',
             f'<text class="fr" x="40" y="52" style="fill:{GREEN};font-size:30px">Fairway <tspan fill="{BRASS}">&amp;</tspan> Dials · dial concepts</text>',
             f'<text class="jo" x="40" y="96" style="fill:{MUTED};font-size:13px;letter-spacing:2px">LINKS COLLECTION · FIELD</text>']
    y0 = 110
    for i, (slug, name, fn) in enumerate(LINKS):
        row, pair = divmod(i, 2)
        for date in (False, True):
            col = pair * 2 + int(date)
            cx, cy = 100 + col * cell_w, y0 + 95 + row * cell_h
            parts.append(f'<g transform="translate({cx} {cy}) scale({s})">{field_dial(fn, date)}</g>')
            parts.append(f'<text class="jo" x="{cx}" y="{cy + 100}" text-anchor="middle" style="fill:{INK};font-size:13px">{name} · {"date" if date else "no date"}</text>')
    y1 = y0 + 4 * cell_h + 20
    parts.append(f'<text class="jo" x="40" y="{y1}" style="fill:{MUTED};font-size:13px;letter-spacing:2px">TOOL COLLECTION · DIVER</text>')
    for k, date in enumerate((False, True)):
        cx, cy = 200 + k * 400, y1 + 140
        parts.append(f'<g transform="translate({cx} {cy}) scale(0.85)">{marker(date)}</g>')
        parts.append(f'<text class="jo" x="{cx}" y="{cy + 140}" text-anchor="middle" style="fill:{INK};font-size:13px">Marker · {"date" if date else "no date"}</text>')
    H = y1 + 310
    sheet = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
             f'<title>Fairway &amp; Dials dial concepts</title>{DEFS}{"".join(parts)}</svg>\n')
    (OUT / "collection-sheet.svg").write_text(sheet)
    files.append(OUT / "collection-sheet.svg")

    # Large side-by-side of the launch model, no date and date.
    parts = ['<rect width="1200" height="680" fill="#faf8f2"/>']
    for k, (date, label) in enumerate(((False, "Tee Box · no date"), (True, "Tee Box · date"))):
        cx = 300 + k * 600
        parts.append(f'<g transform="translate({cx} 315) scale(2.05)">{field_dial(tee_box, date)}</g>')
        parts.append(f'<text class="jo" x="{cx}" y="650" text-anchor="middle" style="fill:{INK};font-size:22px">{label}</text>')
    pair = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="1200" height="680">'
            f'<title>Fairway &amp; Dials Tee Box, no date and date</title>{DEFS}{"".join(parts)}</svg>\n')
    (OUT / "tee-box-side-by-side.svg").write_text(pair)
    files.append(OUT / "tee-box-side-by-side.svg")
    for f in files:
        print(f.relative_to(OUT.parent.parent))


if __name__ == "__main__":
    main()
