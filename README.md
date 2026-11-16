# Sectorale informatievoorziening

Mbo-, hbo- en wo-instellingen krijgen van DUO bestanden over hun studenten en hun bekostiging. Die bestanden zijn gemaakt voor de uitwisseling met DUO, niet voor analyse. Wie wil weten hoe het met de studenten gaat, of waarom een inschrijving niet bekostigd wordt, moet ze eerst leren lezen. Nu doet elke instelling dat apart, met eigen definities.

CEDA, een team binnen [Npuls](https://npuls.nl), maakt deze bestanden bruikbaar met open source tools.

## Doel

Elke mbo-, hbo- en wo-instelling maakt met de eigen DUO-bestanden betrouwbare cijfers over **studiesucces** en **bekostiging**: met vaste, gedocumenteerde definities, op dezelfde manier in mbo, hbo en wo en zonder dat de gegevens de instelling verlaten.

## De informatiestroom

<p align="center">
  <img src="assets/informatiestroom.svg" alt="Boom van DUO-bestand naar inzicht. Hbo en wo: 1cijferHO via 1cijferho naar Staat van de Onderwijsinstelling; VLPBEK en DEFBEK via ho-bekostiging-bestanden naar een bekostigingsdashboard. Mbo: geen studentenbestand; RO en TBG-i naar Staat van de Onderwijsinstelling MBO; RO, TBG-i en GRONDSLAG IP via mbo-bekostiging-bestanden naar een bekostigingsdashboard." width="100%">
</p>

Het verschil tussen de sectoren zit in de wortels, de DUO-bestanden. Hbo en wo hebben met 1cijferHO een studentenbestand dat voor studiesucces bedoeld is. Het mbo heeft dat niet; daar leiden we studiesucces af uit de bekostigingsbestanden RO en TBG-i.

## Producten

### Studiesucces

| Product | Voor | DUO-bestanden | Levert |
|---|---|---|---|
| [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) | hbo en wo | 1cijferHO (omgezet met 1cijferho), optioneel VAKHAVW | Analysebestand per student, dashboard met instroom, rendement, uitval en studiewissel, benchmarkrapport om te delen |
| [1cijferho](https://github.com/cedanl/1cijferho) | hbo en wo | 1cijferHO, VAKHAVW | Leesbare tabellen als invoer voor Staat van de Onderwijsinstelling |
| [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo) | mbo | RO (meerdere, tot 10 jaar), optioneel TBG-i | Dashboard met de indicatoren uit de Regeling studiesucces mbo, cohorten en loopbanen |

### Bekostiging

| Product | Voor | DUO-bestanden | Levert |
|---|---|---|---|
| [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden) | hbo en wo | VLPBEK, DEFBEK, optioneel HISBEK | Schone tabellen, datamodel en dashboard: bekostigingstrechter, redenen van niet-bekostiging, voorlopig tegenover definitief, historie |
| [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) | mbo | RO, TBG-i, GRONDSLAG IP | Schone tabellen, datamodel en dashboard met aantallen |

Verwant: [wisselstroom](https://github.com/cedanl/wisselstroom) (R-pakket) laat met VLPBEK en DEFBEK zien welke studenten in hbo en wo blijven, wisselen, stapelen of stoppen.

### Hoe de tools met gegevens omgaan

- De tools draaien op een computer van de instelling. Er gaan geen gegevens naar CEDA of naar een server.
- Ze lezen de bestanden zoals DUO ze levert. Ze rekenen de bekostiging niet opnieuw uit.
- Cijfers zijn indicatief. Het zijn geen officiële cijfers van DUO of de Inspectie.
- Elke tool heeft demodata, zodat je hem kunt bekijken zonder echte gegevens.

Welke DUO-bestanden dit zijn, wat erin staat en waar een instelling ze ophaalt: zie [DUO-bestanden](docs/duo-bestanden.md).

## Waar we heen willen

Drie richtingen, uitgewerkt in [Waar we heen willen](docs/richting.md):

1. Eén open beschrijving van de DUO-bestanden, zodat tools ze automatisch inlezen.
2. Eén overzicht van wie wordt bekostigd en waarom niet, voor mbo en hbo/wo.
3. Studiesucces in het mbo op dezelfde manier volgen als in hbo en wo.

## Presentaties

| Datum | Titel | Over |
|---|---|---|
| 21 september 2026 | [MBO en HO: wat is er mogelijk met de bekostigingsbestanden?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/260921_MBO_HO_bekostigingsbestanden.pdf) (concept) | De bestanden van mbo en hbo/wo naast elkaar, wat tools er nu mee kunnen en welke aanpassingen in vorm mogelijk zijn |
| 1 oktober 2026 | [Een 1CHO voor het mbo?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261001_mbo_1cho_haalbaarheid.pdf) | Haalbaarheid van een mbo-versie van 1cijferHO: wat werkt, wat ontbreekt en waarom |
| 4 november 2026 | [Staat van de Onderwijsinstelling: impactsessie](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261104_staat1cho_impactsessie/261104_staat1cho_impactsessie.pdf) | Het product voor hbo en wo in de praktijk |
| 5 november 2026 | [Inlezen van TBG-i en registratieoverzicht](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261105_werkgroep2_tbgi_ro.pdf) | Datacoalitie werkgroep 2: demo van mbo-bekostiging-bestanden en wat instellingen met deze bestanden willen |

## Documentatie

- [DUO-bestanden](docs/duo-bestanden.md): wat erin staat en waar je ze ophaalt
- [Waar we heen willen](docs/richting.md): wat we zagen bij het bouwen, drie richtingen en kansen
- [1cijferho](https://cedanl.github.io/1cijferho/): 1cijferHO-bestanden omzetten
- [ho-bekostiging-bestanden](https://cedanl.github.io/ho-bekostiging-bestanden/): bestanden, datamodel en kwaliteitscontroles
- [mbo-bekostiging-bestanden](https://cedanl.github.io/mbo-bekostiging-bestanden/): bestanden, datamodel en ontwerpkeuzes
- [wisselstroom](https://cedanl.github.io/wisselstroom/): studentstromen in hbo en wo
- [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling#readme) en [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo#readme): installeren, gebruiken en definities
- [Haalbaarheidsonderzoek 1CHO voor het mbo](https://github.com/cedanl/mbo-bekostiging-bestanden/issues/389)

## Contact

Vragen of zin om mee te bouwen?

- E-mail: [ceda@surf.nl](mailto:ceda@surf.nl)
- Community: [community.npuls.nl/groups/data-ai](https://community.npuls.nl/groups/data-ai)
- GitHub: [github.com/cedanl](https://github.com/cedanl)
