"""Genereer de boom-infographic (informatiestroom) als SVG in Npuls-huisstijl.

Gebruik, vanuit de root van de repo:
    python .claude/skills/update-infographic/genereer_informatiestroom.py assets/informatiestroom.svg

Pas alleen het blok GEGEVENS aan. De opmaak eronder volgt vanzelf.
"""
import sys
from xml.sax.saxutils import escape

# ---------------------------------------------------------------------------
# GEGEVENS
# ---------------------------------------------------------------------------
TITEL = "Van DUO-bestand naar inzicht"
ONDERTITEL = "Mbo en hbo/wo stellen dezelfde vragen. Lees van onder naar boven."
VOET = "CEDA · Npuls · stand november 2026"
PAYOFF = "Onderwijs bewegen."

# Per sector twee producten: links studiesucces, rechts bekostiging.
# "bestanden": maximaal vier, van links naar rechts.
#   naar      = {productindex: "vast" | "optioneel"}  -> lijn naar dat product
#   stippel   = stippelrand (bestand is optioneel)
#   ontbreekt = geel vak zonder lijnen (bestand bestaat niet)
#   periode   = welke periode het bestand beslaat (blauwe regel onderin)
# "alternatief": stippellijn van tool van product A naar product B.
SECTOREN = [
    {
        "label": "Hbo en wo",
        "producten": [
            {"titel": ["Staat van de", "Onderwijsinstelling"], "uitleg": "instroom, rendement, uitval, wissel",
             "tool": ["1cijferho", "omzetten naar leesbare tabellen"]},
            {"titel": ["Bekostigingsdashboard"], "uitleg": "aantallen en redenen",
             "tool": ["ho-bekostiging-bestanden", "inlezen, decoderen, controleren"]},
        ],
        "bestanden": [
            {"naam": "1cijferHO", "uitleg": "studentenbestand", "periode": "hele historie", "naar": {0: "vast"}},
            {"naam": "VAKHAVW", "uitleg": "havo/vwo-cijfers", "periode": "meerdere jaren", "naar": {0: "optioneel"}, "stippel": True},
            {"naam": "VLPBEK", "uitleg": "DEFBEK", "uitleg_vet": True, "periode": "1 jaar", "naar": {1: "vast"}},
            {"naam": "HISBEK", "uitleg": "bekostiging", "periode": "eerdere jaren", "naar": {1: "optioneel"}, "stippel": True},
        ],
        "alternatief": None,
    },
    {
        "label": "Mbo",
        "producten": [
            {"titel": ["Staat van de", "Onderwijsinstelling MBO"], "uitleg": "indicatoren studiesucces mbo",
             "tool": ["Samenvoegen in Staat MBO", "RO's stapelen tot 10 jaar"]},
            {"titel": ["Bekostigingsdashboard"], "uitleg": "aantallen",
             "tool": ["mbo-bekostiging-bestanden", "inlezen, decoderen, controleren"]},
        ],
        "bestanden": [
            {"naam": "Geen", "uitleg": "studentenbestand", "ontbreekt": True},
            {"naam": "RO", "uitleg": "registratieoverzicht", "periode": "max. 2 jaar", "naar": {0: "vast", 1: "vast"}},
            {"naam": "TBG-i", "uitleg": "bekostiging", "periode": "1 jaar", "naar": {0: "optioneel", 1: "vast"}},
            {"naam": "GRONDSLAG IP", "uitleg": "register, zonder BSN", "periode": "1 oktober", "naar": {1: "vast"}},
        ],
        # mbo-bekostiging-bestanden kan het datamodel aan Staat MBO leveren
        "alternatief": (1, 0),
    },
]

LEGENDA = ["Product", "Bruikbaar maken", "Bestand van DUO", "Ontbreekt in het mbo"]
LEGENDA_LIJN = "Optioneel of alternatieve route"
GROND_LABEL = "BESTANDEN VAN DUO"

# ---------------------------------------------------------------------------
# HUISSTIJL (Npuls). Alleen toegestane combinaties: tekst zwart op groen,
# oranje, roze en geel; geel op blauw. Zwart nooit als achtergrond.
# ---------------------------------------------------------------------------
ORANJE, ZWART, ROZE, BLAUW, GEEL, GROEN = "#DD784B", "#000000", "#F4D9DC", "#3D68EC", "#F4D74B", "#00AF81"
LICHT_ROZE, LICHT_GROEN, LICHT_ORANJE, GRIJS = "#FAEAEA", "#CCEEE6", "#FFE4D8", "#6B7280"
SANS = "'General Sans', Arial, Helvetica, sans-serif"
SERIF = "'Cooper Light BT', Georgia, serif"

# ---------------------------------------------------------------------------
# OPMAAK
# ---------------------------------------------------------------------------
W, H = 1200, 840
SECTOR_CX = (310, 894)
KOLOM_DX = 140                      # afstand productkolom tot midden van de boom
STAM_DX = 12                        # halve afstand tussen de twee stammen
WORTEL_X0 = (40, 624)               # linkerrand van de eerste wortel per sector
LEAF_Y, LEAF_H, LEAF_W = 180, 90, 260
TOOL_Y, TOOL_H, TOOL_W = 328, 62, 250
TRUNK_TOP, TRUNK_BOT = 452, 548
ROOT_Y, ROOT_H, ROOT_W, ROOT_GAP = 606, 74, 128, 8

out = []


def text(x, y, s, size=14, weight=400, fill=ZWART, anchor="middle", family=SANS, style="normal"):
    out.append(
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def box(cx, y, w, h, fill, lines, rx=12, dashed=False, sizes=(14, 12.5)):
    """Vak met gecentreerde regels; lines = [(tekst, vet)] of [(tekst, vet, kleur)]."""
    dash = ' stroke-dasharray="6 5"' if dashed else ""
    out.append(
        f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{ZWART}" stroke-width="1.6"{dash}/>'
    )
    line_h = 17
    start = y + h / 2 - (len(lines) - 1) * line_h / 2 + 5
    for i, (s, bold, *kleur) in enumerate(lines):
        text(cx, start + i * line_h, s, size=sizes[0] if bold else sizes[1], weight=600 if bold or kleur else 400,
             fill=kleur[0] if kleur else ZWART)


def path(d, dashed=False, width=2.2):
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    out.append(f'<path d="{d}" fill="none" stroke="{ZWART}" stroke-width="{width}" stroke-linecap="round"{dash}/>')


def stam(tool_x, stam_x, wortels):
    """Lijn van tool omlaag via de stam naar elke wortel; wortels = [(x, gestippeld)]."""
    y0 = TOOL_Y + TOOL_H
    path(f"M{tool_x},{y0} C{tool_x},{y0 + 50} {stam_x},{TRUNK_TOP - 40} {stam_x},{TRUNK_TOP} L{stam_x},{TRUNK_BOT}")
    for rx, dashed in wortels:
        path(f"M{stam_x},{TRUNK_BOT} C{stam_x},{TRUNK_BOT + 36} {rx},{ROOT_Y - 36} {rx},{ROOT_Y}", dashed=dashed)


def teken_sector(sector, cx, x0):
    kolommen = (cx - KOLOM_DX, cx + KOLOM_DX)
    stammen = (cx - STAM_DX, cx + STAM_DX)
    wortel_x = [x0 + ROOT_W / 2 + i * (ROOT_W + ROOT_GAP) for i in range(len(sector["bestanden"]))]

    # Sectorlabel, kruin en stam als achtergrond
    out.append(f'<rect x="{cx - 90}" y="118" width="180" height="32" rx="16" fill="{BLAUW}"/>')
    text(cx, 139, sector["label"], size=15, weight=600, fill=GEEL)
    out.append(f'<rect x="{cx - 287}" y="{LEAF_Y - 14}" width="574" height="{LEAF_H + 28}" rx="58" fill="{LICHT_GROEN}"/>')
    out.append(f'<rect x="{cx - 40}" y="{TRUNK_TOP - 34}" width="80" height="{TRUNK_BOT - TRUNK_TOP + 48}" rx="22" fill="{LICHT_ORANJE}"/>')

    # Lijnen eerst, zodat de vakken erover liggen
    for p in range(len(sector["producten"])):
        wortels = [(wortel_x[i], b["naar"][p] == "optioneel")
                   for i, b in enumerate(sector["bestanden"]) if p in b.get("naar", {})]
        stam(kolommen[p], stammen[p], wortels)
        path(f"M{kolommen[p]},{LEAF_Y + LEAF_H} L{kolommen[p]},{TOOL_Y}")
    if sector["alternatief"]:
        van, naar = (kolommen[i] for i in sector["alternatief"])
        richting = 1 if van > naar else -1
        path(f"M{van - richting * 60},{TOOL_Y} C{van - richting * 90},{TOOL_Y - 40} "
             f"{naar + richting * 80},{LEAF_Y + LEAF_H + 30} {naar + richting * 70},{LEAF_Y + LEAF_H}",
             dashed=True, width=1.8)

    for p, prod in enumerate(sector["producten"]):
        regels = [(t, True) for t in prod["titel"]] + [(prod["uitleg"], False)]
        box(kolommen[p], LEAF_Y, LEAF_W, LEAF_H, GROEN, regels, rx=45)
        box(kolommen[p], TOOL_Y, TOOL_W, TOOL_H, ORANJE, [(prod["tool"][0], True), (prod["tool"][1], False)])

    for x, b in zip(wortel_x, sector["bestanden"]):
        fill = GEEL if b.get("ontbreekt") else ROZE
        klein = len(b["uitleg"]) > 17
        regels = [(b["naam"], True), (b["uitleg"], b.get("uitleg_vet", False))]
        if b.get("periode"):
            regels.append((b["periode"], False, BLAUW))  # blauw op roze: toegestane combinatie
        box(x, ROOT_Y, ROOT_W, ROOT_H, fill, regels,
            dashed=b.get("stippel") or b.get("ontbreekt"), sizes=(14, 11.5 if klein else 12.5))


# Achtergrond (wit, ook leesbaar in donkere modus van GitHub) en vormentaal
out.append(f'<rect width="{W}" height="{H}" rx="18" fill="#FFFFFF"/>')
out.append('<g clip-path="url(#kader)" fill="none" stroke-width="5">')
for r, c in [(120, ORANJE), (95, BLAUW), (70, GROEN), (45, GEEL)]:
    out.append(f'<circle cx="1150" cy="40" r="{r}" stroke="{c}" opacity="0.9"/>')
out.append("</g>")

text(40, 62, TITEL, size=30, weight=600, fill=ORANJE, anchor="start")
text(40, 96, ONDERTITEL, size=18, family=SERIF, style="italic", anchor="start")

# Grond onder beide bomen
out.append(f'<rect x="30" y="{TRUNK_BOT + 14}" width="{W - 60}" height="{ROOT_Y + ROOT_H + 44 - TRUNK_BOT - 14}" '
           f'rx="14" fill="{LICHT_ROZE}"/>')
text(W / 2, ROOT_Y + ROOT_H + 26, GROND_LABEL, size=11.5, weight=600, fill=GRIJS)

for sector, cx, x0 in zip(SECTOREN, SECTOR_CX, WORTEL_X0):
    teken_sector(sector, cx, x0)

# Legenda
ly, x = 770, 40
for (fill, dashed), label in zip([(GROEN, False), (ORANJE, False), (ROZE, False), (GEEL, True)], LEGENDA):
    dash = ' stroke-dasharray="4 3"' if dashed else ""
    out.append(f'<rect x="{x}" y="{ly - 13}" width="18" height="18" rx="5" fill="{fill}" stroke="{ZWART}" stroke-width="1.4"{dash}/>')
    text(x + 26, ly + 1, label, size=13.5, anchor="start")
    x += 26 + len(label) * 7.6 + 34
path(f"M{x},{ly - 4} L{x + 40},{ly - 4}", dashed=True, width=2)
text(x + 50, ly + 1, LEGENDA_LIJN, size=13.5, anchor="start")

text(40, 816, VOET, size=12, fill=GRIJS, anchor="start")
text(W - 40, 816, PAYOFF, size=13, weight=600, anchor="end")


def beschrijving():
    """Tekstalternatief voor schermlezers, afgeleid uit GEGEVENS."""
    delen = []
    for s in SECTOREN:
        for p, prod in enumerate(s["producten"]):
            bronnen = [b["naam"] for b in s["bestanden"] if p in b.get("naar", {})]
            delen.append(f'{s["label"]}: {", ".join(bronnen)} via {prod["tool"][0]} naar {" ".join(prod["titel"])}.')
    return " ".join(delen)


svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
    f'aria-labelledby="titel beschrijving">'
    f'<title id="titel">{escape(TITEL)}</title>'
    f'<desc id="beschrijving">{escape(beschrijving())}</desc>'
    f'<defs><clipPath id="kader"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>'
    + "".join(out)
    + "</svg>\n"
)
with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(svg)
print("geschreven:", sys.argv[1])
