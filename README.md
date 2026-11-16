# Sectorale informatievoorziening

Mbo-, hbo- en wo-instellingen krijgen van DUO bestanden over hun studenten en hun bekostiging. Die bestanden zijn gemaakt voor de uitwisseling met DUO, niet voor analyse. Wie wil weten hoe het met de studenten gaat, of waarom een inschrijving niet bekostigd wordt, moet ze eerst leren lezen. Nu doet elke instelling dat apart, met eigen definities.

CEDA, een team binnen [Npuls](https://npuls.nl), maakt deze bestanden bruikbaar met open source tools. De tools draaien binnen de instelling en werken voor mbo en voor hbo en wo.

## Doel

Elke mbo-, hbo- en wo-instelling maakt met de eigen DUO-bestanden betrouwbare cijfers over **studiesucces** en **bekostiging**: met vaste, gedocumenteerde definities, op dezelfde manier in beide sectoren en zonder dat de gegevens de instelling verlaten.

## De informatiestroom

<p align="center">
  <img src="assets/informatiestroom.svg" alt="Boom van DUO-bestand naar inzicht. Hbo en wo: 1cijferHO via 1cijferho naar Staat van de Onderwijsinstelling; VLPBEK en DEFBEK via ho-bekostiging-bestanden naar een bekostigingsdashboard. Mbo: geen studentenbestand; RO en TBG-i naar Staat van de Onderwijsinstelling MBO; RO, TBG-i en GRONDSLAG IP via mbo-bekostiging-bestanden naar een bekostigingsdashboard." width="100%">
</p>

Lees de boom van onder naar boven. De wortels zijn de bestanden die DUO aan een instelling levert. De stam zijn de tools die ze bruikbaar maken. De kruin zijn de producten waarmee een instelling haar vragen beantwoordt.

Het verschil tussen de sectoren zit in de wortels. Hbo en wo hebben met 1cijferHO een studentenbestand dat voor studiesucces bedoeld is. Het mbo heeft dat niet; daar leiden we studiesucces af uit de bekostigingsbestanden RO en TBG-i.

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

Bij het bouwen zagen we dat beide sectoren dezelfde vragen stellen aan bijna dezelfde bestanden. Bijna elk bestand heeft een tegenhanger in de andere sector, van registratieoverzicht tot accountantsrapport. De verschillen zitten vooral in de vorm: datums (`2025-01-30` tegenover `20250130`), bestandsnamen, XML tegenover CSV, en beschrijvingen in PDF's die vaak veranderen (hbo en wo 23 versies sinds 2020, mbo 19 sinds 2019). Elk verschil betekent bij het bouwen handwerk.

Eén verschil is wezenlijk. Een hbo- of wo-instelling ziet ook inschrijvingen en graden van eigen studenten bij andere instellingen. Een mbo-instelling ziet alleen de eigen inschrijvingen, waardoor een student die overstapt lijkt op een student die stopt.

Daaruit volgen drie richtingen. Geen ervan raakt de bekostigingsregels; het gaat om de vorm en uitleg van bestanden en om wat tools ermee doen.

**1. Eén open beschrijving van de bestanden.** Elk veld en elke code als tabel, naast de PDF. Tools lezen de bestanden dan automatisch in en een nieuwe versie laat zien wat er veranderde.
*Nu:* beschrijvingen voor vijf bestandssoorten, met de hand overgenomen uit de PDF's. *Volgende stap:* de TBG-i (mbo) en het analysebestand (hbo en wo) in één vorm naast elkaar zetten. Die twee beantwoorden dezelfde vraag: wie wordt bekostigd en waarom niet.

**2. Eén overzicht: wie wordt bekostigd en waarom niet.** Met de voorlopige bestanden ziet een instelling tijdens het jaar de verwachte uitkomst, met de redenen, en wat ze in de eigen registratie kan nakijken.
*Nu:* de tool voor hbo en wo toont de redenen en zet voorlopig naast definitief; de mbo-tool toont de aantallen. *Volgende stap:* mbo-signalen en statuscodes uit hbo en wo in dezelfde groepen redenen onderbrengen en de mbo-kant bouwen. Het nut is nog niet getoetst bij instellingen.

**3. Studiesucces in het mbo op dezelfde manier volgen als in hbo en wo.** Uit RO en TBG-i per instelling een bestand maken in de vorm van 1cijferHO.
*Nu:* 47 van de 115 velden van 1cijferHO zijn per instelling te vullen. Dat is genoeg voor rendement en uitval per opleiding, en te weinig voor kansengelijkheid, omdat vooropleiding, herkomst en regio ontbreken. Staat van de Onderwijsinstelling MBO draait met een eigen mbo-dashboard op demodata. *Volgende stap:* de cijfers toetsen op echte data van één instelling.

### Kansen

Omdat beide sectoren dezelfde vragen stellen, kan één tool beide bedienen als de bestanden dezelfde vorm hebben. Daarvoor zijn kleine stappen genoeg, zonder de regels te veranderen: een schema per bestandssoort, codelijsten als tabel, een wijzigingslog per versie en dezelfde begrippen en groepen redenen in alle sectoren. Wat echt bij een sector hoort, zoals stage in het mbo en joint degrees in hbo en wo, blijft verschillen. Zie de presentatie van 21 september hieronder.

## Presentaties

| Datum | Titel | Over |
|---|---|---|
| 21 september 2026 | [MBO en HO: wat is er mogelijk met de bekostigingsbestanden?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/260921_MBO_HO_bekostigingsbestanden.pdf) (concept) | De bestanden van beide sectoren naast elkaar, wat tools er nu mee kunnen en welke kleine aanpassingen veel opleveren |
| 1 oktober 2026 | [Een 1CHO voor het mbo?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261001_mbo_1cho_haalbaarheid.pdf) | Haalbaarheid van een mbo-versie van 1cijferHO: wat werkt, wat ontbreekt en waarom |
| 4 november 2026 | [Staat van de Onderwijsinstelling: impactsessie](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261104_staat1cho_impactsessie/261104_staat1cho_impactsessie.pdf) | Het product voor hbo en wo in de praktijk |
| 5 november 2026 | [Inlezen van TBG-i en registratieoverzicht](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261105_werkgroep2_tbgi_ro.pdf) | Datacoalitie werkgroep 2: demo van mbo-bekostiging-bestanden en wat instellingen met deze bestanden willen |

## Documentatie

- [DUO-bestanden](docs/duo-bestanden.md): wat erin staat en waar je ze ophaalt
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
