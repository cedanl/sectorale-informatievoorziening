---
name: update-stroomschema
description: Werk het stroomschema (assets/informatiestroom.svg) van deze projectrepo bij. Gebruik bij "update het stroomschema", "update de infographic", "pas het plaatje aan", of wanneer een product andere DUO-bestanden gebruikt, een nieuw product bijkomt of de tabel in de README verandert.
---

# Stroomschema bijwerken

Het stroomschema is een boom: wortels zijn DUO-bestanden, de stam de tools die ze bruikbaar maken, de kruin de producten. Links hbo en wo, rechts mbo. Per sector staat studiesucces links en bekostiging rechts.

De SVG wordt gegenereerd door `genereer_informatiestroom.py` in deze map. Pas `assets/informatiestroom.svg` nooit met de hand aan.

## Stappen

1. **Bepaal wat er veranderd is.** Lees de tabel "Producten" in `README.md` en `docs/duo-bestanden.md`. Vraagt de gebruiker om de laatste stand, lees dan ook de README's van de productrepo's (zie de links in de tabel) op gewijzigde invoerbestanden.
2. **Pas het blok `GEGEVENS` bovenin het script aan.** Alleen daar. Per bestand geeft `naar` aan naar welk product een lijn loopt (`"vast"` of `"optioneel"`). Werk ook `VOET` bij met de maand van de stand.
3. **Genereer de SVG** vanuit de root van de repo:
   `python .claude/skills/update-stroomschema/genereer_informatiestroom.py assets/informatiestroom.svg`
4. **Controleer het resultaat met een screenshot:**
   Eerste keer op deze machine? Installeer dan eerst de browser: `uv run --with playwright playwright install chromium`
   `uv run --with playwright python .claude/skills/update-stroomschema/screenshot.py assets/informatiestroom.svg /tmp/stroomschema.png`
   Bekijk de PNG. Loopt tekst buiten een vak, kort dan de tekst in. Maak vakken niet breder.
5. **Houd README en stroomschema gelijk.** Elke lijn in de boom moet te herleiden zijn tot de tabel in de README en tot de productrepo. Geen verzonnen verbanden.

## Huisstijlregels (Npuls)

- Kleuren alleen in toegestane combinaties: zwarte tekst op groen (product), oranje (tool), roze (bestand) en geel (ontbreekt); gele tekst op blauw (sectorlabel). Zwart nooit als achtergrond.
- Witte achtergrond in de SVG zelf, zodat hij ook in het donkere thema van GitHub leesbaar is.
- Lettertype General Sans met Arial als terugval. GitHub laadt geen webfonts in plaatjes, dus in de praktijk zie je Arial.
- Zwarte lijnen, afgeronde vakken. Stippellijn of stippelrand betekent optioneel of alternatief.

## Grenzen

- Maximaal twee sectoren, twee producten per sector en vier bestanden per sector. Komt er meer bij, overleg dan eerst met de gebruiker over een andere indeling in plaats van de boom vol te proppen.
- Teksten volgen dezelfde regels als de README: Nederlands, bondig, geen "ho" maar "hbo en wo" (repo-namen blijven zoals ze zijn).
- Oranje vakken heten allemaal "Bruikbaar maken", met daaronder in één korte regel wat er gebeurt (bijv. "decoderen, controleren, samenvoegen"). Geen repo-namen; die staan in de producttabel van de README.
