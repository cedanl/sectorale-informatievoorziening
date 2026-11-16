"""Genereer assets/informatiestroom.svg (boom-infographic, Npuls-huisstijl).

Gebruik: python assets/genereer_informatiestroom.py assets/informatiestroom.svg
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]

ORANJE, ZWART, ROZE, BLAUW, GEEL, GROEN = "#DD784B", "#000000", "#F4D9DC", "#3D68EC", "#F4D74B", "#00AF81"
LICHT_ROZE, LICHT_GROEN, LICHT_ORANJE, GRIJS = "#FAEAEA", "#CCEEE6", "#FFE4D8", "#6B7280"
SANS = "'General Sans', Arial, Helvetica, sans-serif"
SERIF = "'Cooper Light BT', Georgia, serif"

W, H = 1200, 840
LEAF_Y, LEAF_H, LEAF_W = 180, 90, 260
TOOL_Y, TOOL_H, TOOL_W = 328, 62, 250
TRUNK_TOP, TRUNK_BOT = 452, 548
ROOT_Y, ROOT_H, ROOT_W = 612, 66, 128

out = []


def text(x, y, s, size=14, weight=400, fill=ZWART, anchor="middle", family=SANS, style="normal"):
    out.append(
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def box(cx, y, w, h, fill, lines, rx=12, dashed=False, sizes=(14, 12.5)):
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    out.append(
        f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{ZWART}" stroke-width="1.6"{dash}/>'
    )
    n = len(lines)
    line_h = 17
    start = y + h / 2 - (n - 1) * line_h / 2 + 5
    for i, (s, bold) in enumerate(lines):
        text(cx, start + i * line_h, s, size=sizes[0] if bold else sizes[1], weight=600 if bold else 400)


def path(d, dashed=False, width=2.2):
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    out.append(f'<path d="{d}" fill="none" stroke="{ZWART}" stroke-width="{width}" stroke-linecap="round"{dash}/>')


def stem(tool_x, stem_x, roots):
    """Lijn van tool omlaag via de stam naar elke wortel; roots = [(x, dashed)]."""
    y0 = TOOL_Y + TOOL_H
    path(f"M{tool_x},{y0} C{tool_x},{y0 + 50} {stem_x},{TRUNK_TOP - 40} {stem_x},{TRUNK_TOP} L{stem_x},{TRUNK_BOT}")
    for rx, dashed in roots:
        path(f"M{stem_x},{TRUNK_BOT} C{stem_x},{TRUNK_BOT + 36} {rx},{ROOT_Y - 36} {rx},{ROOT_Y}", dashed=dashed)


# Achtergrond (wit, ook leesbaar in donkere modus van GitHub)
out.append(f'<rect width="{W}" height="{H}" rx="18" fill="#FFFFFF"/>')
# Vormentaal: concentrische ringen rechtsboven, decoratief
out.append('<g clip-path="url(#kader)" fill="none" stroke-width="5">')
for r, c in [(120, ORANJE), (95, BLAUW), (70, GROEN), (45, GEEL)]:
    out.append(f'<circle cx="1150" cy="40" r="{r}" stroke="{c}" opacity="0.9"/>')
out.append("</g>")

# Titel
text(40, 62, "Van DUO-bestand naar inzicht", size=30, weight=600, fill=ORANJE, anchor="start")
text(40, 96, "Twee sectoren, dezelfde vragen. Lees van onder naar boven.", size=18, family=SERIF,
     style="italic", anchor="start")

# Grond onder beide bomen
out.append(f'<rect x="30" y="{TRUNK_BOT + 14}" width="{W - 60}" height="{ROOT_Y + ROOT_H + 44 - TRUNK_BOT - 14}" '
           f'rx="14" fill="{LICHT_ROZE}"/>')
text(600, ROOT_Y + ROOT_H + 26, "BESTANDEN VAN DUO", size=11.5, weight=600, fill=GRIJS)

TREES = {
    "ho": {"cx": 310, "label": "Hoger onderwijs", "cols": (170, 450)},
    "mbo": {"cx": 894, "label": "Mbo", "cols": (754, 1034)},
}

for key, t in TREES.items():
    cx = t["cx"]
    # Sectorlabel: blauw met gele tekst (toegestane combinatie)
    out.append(f'<rect x="{cx - 90}" y="118" width="180" height="32" rx="16" fill="{BLAUW}"/>')
    text(cx, 139, t["label"], size=15, weight=600, fill=GEEL)
    out.append(f'<rect x="{cx - 287}" y="{LEAF_Y - 14}" width="574" height="{LEAF_H + 28}" rx="58" fill="{LICHT_GROEN}"/>')
    out.append(f'<rect x="{cx - 40}" y="{TRUNK_TOP - 34}" width="80" height="{TRUNK_BOT - TRUNK_TOP + 48}" rx="22" fill="{LICHT_ORANJE}"/>')

ho_s, ho_b = TREES["ho"]["cols"]
mbo_s, mbo_b = TREES["mbo"]["cols"]
ho_roots = [104, 240, 376, 512]
mbo_roots = [688, 824, 960, 1096]

# Stammen en wortels (eerst tekenen, zodat vakken erover liggen)
stem(ho_s, 298, [(ho_roots[0], False), (ho_roots[1], True)])
stem(ho_b, 322, [(ho_roots[2], False), (ho_roots[3], True)])
stem(mbo_s, 882, [(mbo_roots[1], False), (mbo_roots[2], True)])
stem(mbo_b, 906, [(mbo_roots[1], False), (mbo_roots[2], False), (mbo_roots[3], False)])

# Takken: tool naar product
for x in (ho_s, ho_b, mbo_s, mbo_b):
    path(f"M{x},{LEAF_Y + LEAF_H} L{x},{TOOL_Y}")
# mbo-bekostiging-bestanden kan ook het datamodel leveren aan Staat MBO
path(f"M{mbo_b - 60},{TOOL_Y} C{mbo_b - 90},{TOOL_Y - 40} {mbo_s + 80},{LEAF_Y + LEAF_H + 30} {mbo_s + 70},{LEAF_Y + LEAF_H}",
     dashed=True, width=1.8)

# Producten (kruin): groen met zwarte tekst
box(ho_s, LEAF_Y, LEAF_W, LEAF_H, GROEN, [("Staat van de", True), ("Onderwijsinstelling", True), ("instroom, rendement, uitval, wissel", False)], rx=45)
box(ho_b, LEAF_Y, LEAF_W, LEAF_H, GROEN, [("Bekostigingsdashboard", True), ("aantallen en redenen", False)], rx=45)
box(mbo_s, LEAF_Y, LEAF_W, LEAF_H, GROEN, [("Staat van de", True), ("Onderwijsinstelling MBO", True), ("indicatoren studiesucces mbo", False)], rx=45)
box(mbo_b, LEAF_Y, LEAF_W, LEAF_H, GROEN, [("Bekostigingsdashboard", True), ("aantallen, redenen volgen", False)], rx=45)

# Bruikbaar maken: oranje met zwarte tekst
box(ho_s, TOOL_Y, TOOL_W, TOOL_H, ORANJE, [("1cijferho", True), ("omzetten naar leesbare tabellen", False)])
box(ho_b, TOOL_Y, TOOL_W, TOOL_H, ORANJE, [("ho-bekostiging-bestanden", True), ("inlezen, decoderen, controleren", False)])
box(mbo_s, TOOL_Y, TOOL_W, TOOL_H, ORANJE, [("Samenvoegen in Staat MBO", True), ("RO's stapelen tot 10 jaar", False)])
box(mbo_b, TOOL_Y, TOOL_W, TOOL_H, ORANJE, [("mbo-bekostiging-bestanden", True), ("inlezen, decoderen, controleren", False)])

# Wortels: roze met zwarte tekst
box(ho_roots[0], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("1cijferHO", True), ("studentenbestand", False)])
box(ho_roots[1], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("VAKHAVW", True), ("havo/vwo-cijfers", False)], dashed=True)
box(ho_roots[2], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("VLPBEK", True), ("DEFBEK", True)])
box(ho_roots[3], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("HISBEK", True), ("eerdere jaren", False)], dashed=True)
box(mbo_roots[0], ROOT_Y, ROOT_W, ROOT_H, GEEL, [("Geen", True), ("studentenbestand", False)], dashed=True)
box(mbo_roots[1], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("RO", True), ("registratieoverzicht", False)], sizes=(14, 11.5))
box(mbo_roots[2], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("TBG-i", True), ("bekostiging", False)])
box(mbo_roots[3], ROOT_Y, ROOT_W, ROOT_H, ROZE, [("GRONDSLAG IP", True), ("register, zonder BSN", False)], sizes=(14, 11.5))

# Legenda
ly = 770
items = [(GROEN, "Product", False), (ORANJE, "Bruikbaar maken", False), (ROZE, "Bestand van DUO", False),
         (GEEL, "Ontbreekt in het mbo", True)]
x = 40
for fill, label, dashed in items:
    dash = ' stroke-dasharray="4 3"' if dashed else ""
    out.append(f'<rect x="{x}" y="{ly - 13}" width="18" height="18" rx="5" fill="{fill}" stroke="{ZWART}" stroke-width="1.4"{dash}/>')
    text(x + 26, ly + 1, label, size=13.5, anchor="start")
    x += 26 + len(label) * 7.6 + 34
path(f"M{x},{ly - 4} L{x + 40},{ly - 4}", dashed=True, width=2)
text(x + 50, ly + 1, "Optioneel of alternatieve route", size=13.5, anchor="start")

text(40, 816, "CEDA · Npuls · stand november 2026", size=12, fill=GRIJS, anchor="start")
text(W - 40, 816, "Onderwijs bewegen.", size=13, weight=600, anchor="end")

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
    f'aria-labelledby="titel beschrijving">'
    '<title id="titel">Van DUO-bestand naar inzicht</title>'
    '<desc id="beschrijving">Twee bomen, voor hoger onderwijs en mbo. Wortels zijn de DUO-bestanden, '
    'de stam de tools die ze bruikbaar maken, de kruin de producten. Hoger onderwijs: 1cijferHO en optioneel '
    'VAKHAVW via 1cijferho naar Staat van de Onderwijsinstelling; VLPBEK, DEFBEK en optioneel HISBEK via '
    'ho-bekostiging-bestanden naar een bekostigingsdashboard. Mbo: geen studentenbestand; RO en optioneel TBG-i '
    'naar Staat van de Onderwijsinstelling MBO; RO, TBG-i en GRONDSLAG IP via mbo-bekostiging-bestanden naar '
    'een bekostigingsdashboard.</desc>'
    f'<defs><clipPath id="kader"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>'
    + "".join(out)
    + "</svg>\n"
)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("geschreven:", OUT)
