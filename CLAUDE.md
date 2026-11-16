# Sectorale informatievoorziening

Projectrepo van CEDA/Npuls. Bevat alleen documentatie: het verhaal, de samenhang en de verwijzingen naar de productrepo's. Geen code, behalve het script dat de infographic maakt.

## Inhoud

- `README.md`: de pagina voor beleidsmakers en stakeholders zoals DUO. Primaire interface.
- `docs/duo-bestanden.md`: de DUO-bestanden, waar je ze ophaalt en welke tool ze leest.
- `docs/richting.md`: wat we zagen bij het bouwen, drie richtingen en kansen. In de README alleen een samenvatting van drie regels.
- `assets/informatiestroom.svg`: de boom-infographic. Nooit met de hand aanpassen; gebruik de skill `update-infographic` (`.claude/skills/update-infographic/`).
- `docs/specs/`: beslis-samenvattingen.

## Afspraken

- Nederlands. Schrijf voor beleidsmakers zonder technische voorkennis: bondig, direct, geen verkooppraat, geen beleidsadvies, geen zinnen over hoe iets bijdraagt aan een ambitie.
- Schrijf "hbo en wo" (of "hbo/wo" in labels), niet "ho". Repo-namen en titels van presentaties blijven zoals ze zijn.
- Ordening op vraag (studiesucces, bekostiging), niet op sector.
- Huisstijl: Npuls. Alleen kleurcombinaties uit de huisstijl, General Sans met Arial als terugval, zwarte lijnen. Geen Npuls-logo op de pagina.
- Houd de producttabellen, `docs/duo-bestanden.md` en de infographic gelijk met de README's van de productrepo's.
- Presentaties staan in `cedanl/clidev-presentaties/exports/`. Link ernaartoe; zet geen PDF's in deze repo.
- Noem alleen wat aantoonbaar werkt. Wat nog niet getoetst is, krijgt die vermelding.
