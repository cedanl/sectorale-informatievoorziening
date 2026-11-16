# Brainstorm: projectrepo Sectorale informatievoorziening

## Beslissingen (locked)

- **Doel:** één plek die het verhaal van het project vertelt voor beleidsmakers en kernstakeholders zoals DUO. Een stakeholder ziet daar wat CEDA al doet, met welke DUO-bestanden, en waar we heen willen. De repo is geen beleidsadvies; ze is de basis voor een gesprek over samenwerking.
- **Projectrepo, geen coderepo:** alleen documentatie. De code staat in de productrepo's waar de README naar verwijst.
- **Overkoepelt:** staat-van-onderwijsinstelling, staat-van-onderwijsinstelling-mbo, ho-bekostiging-bestanden, mbo-bekostiging-bestanden. 1cijferho staat erbij als voorbewerking, wisselstroom als verwant. De oudere repo's 1cijfermbo en duo-mbo-datafiles worden niet genoemd.
- **Opbouw README:** waarom en doel, de informatiestroom als boom-infographic, tabel met producten en DUO-bestanden, wat we leerden, waar we heen willen, kansen, gespreksonderwerpen, presentaties, documentatie, contact.
- **Visual:** SVG in Npuls-huisstijl (geen Mermaid, dat kan de huisstijl niet volgen). Wortels zijn DUO-bestanden, stam de tools, kruin de producten. De SVG wordt gegenereerd door `assets/genereer_informatiestroom.py`.
- **Presentaties:** de PDF's staan met nette namen in `cedanl/clidev-presentaties/exports/`; deze repo linkt ernaartoe. De rapportage van 21 september heet "concept".
- **De one-pager** (`sectorale-informatievoorziening.html`) is bron voor de inhoud, niet als los bestand opgenomen.
- **Herkenbaarheid van projectrepo's:** gewone naam, GitHub-topic `project`, en een sectie "Projecten" op de cedanl-profielpagina.
- **Taal en stijl:** Nederlands. Toon volgens de Npuls-huisstijl (energiek, nuchter, samenwerkend, vooruitkijkend), bondig, zonder verkooppraat.

## Aannames (met confidence)

- Doelgroep is in de eerste plaats DUO, daarnaast beleidsmakers bij instellingen. *Zeker.*
- Er is geen aparte Npuls-schrijfwijzer; de toon uit de huisstijlgids volstaat. *Onzeker.*
- De stand per product (werkt, eerste versie, demodata) klopt met de README's van november 2026. *Waarschijnlijk.*

## Open

- Volgen er meer projectrepo's, dan komt er een template. Pas bij de tweede.

## Deferred

- Een terugverwijzing ("onderdeel van Sectorale informatievoorziening") in de vier productrepo's.
- Opname van de presentatie van Datacoalitie werkgroep 2 (TBG-i en RO, 5 november 2026).
