# Sectorale informatievoorziening

Mbo-, hbo- en wo-instellingen krijgen van DUO bestanden over hun studenten en hun bekostiging. Die bestanden zijn gemaakt voor de uitwisseling met DUO, niet voor analyse. Wie wil weten hoe het met de studenten gaat, of waarom een inschrijving niet bekostigd wordt, moet ze eerst leren lezen. Elke instelling doet dat nu apart, met eigen definities, en het mbo heeft andere bestanden dan hbo en wo. Cijfers over studiesucces en bekostiging zijn daardoor moeilijk te vergelijken.

## Wat we doen

CEDA, een team binnen [Npuls](https://npuls.nl), maakt open source tools die deze bestanden inlezen en er cijfers over **studiesucces** en **bekostiging** van maken. De definities liggen vast en zijn gedocumenteerd. Omdat elke instelling zo met dezelfde definities rekent, kunnen instellingen hun cijfers vergelijken (bijvoorbeeld benchmarken) en samen analyses doen. Waar de bestanden het toelaten, werken de tools in mbo, hbo en wo op dezelfde manier.

## De informatiestroom

<p align="center">
  <img src="assets/informatiestroom.svg" alt="Boom van DUO-bestand naar inzicht. Hbo en wo: 1cijferHO via leesbaar maken naar Staat van de Onderwijsinstelling; VLPBEK en DEFBEK via inlezen en controleren naar een bekostigingsdashboard. Mbo: geen studentenbestand; registratieoverzicht (RO) en TBG-i via samenvoegen naar Staat van de Onderwijsinstelling MBO; registratieoverzicht (RO), TBG-i en afslag registerlevering IP via inlezen en controleren naar een bekostigingsdashboard." width="100%">
</p>

Het verschil tussen de sectoren zit in de wortels. Hbo en wo krijgen van DUO het 1cijferHO-bestand: een door DUO samengesteld studentenbestand met de hele historie van hun studenten. Het mbo heeft dat niet. Daar voegen we registratieoverzichten van meerdere jaren samen, bestanden die bedoeld zijn voor de bekostiging. Meer in [Waar we heen willen](docs/richting.md).

## Producten

### Studiesucces

<table>
<tr><th align="left">Product</th><th align="left">Voor</th><th align="left">DUO-bestanden</th><th align="left">Levert</th></tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/staat-van-onderwijsinstelling">Staat van de Onderwijsinstelling</a></td>
<td valign="top">hbo en wo</td>
<td valign="top"><ul><li><a href="docs/duo-bestanden.md#1cijferho-bestand">1cijferHO-bestand</a> (eerst omgezet met het product 1cijferho).</li></ul>Optioneel<ul><li><a href="docs/duo-bestanden.md#vakkenbestand-vakhavw">Vakkenbestand (VAKHAVW)</a>.</li></ul></td>
<td valign="top">Analysebestand per student. Dashboard met instroom, rendement, uitval en studiewissel. Benchmarkrapport om te delen.</td>
</tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/1cijferho">1cijferho</a></td>
<td valign="top">hbo en wo</td>
<td valign="top"><ul><li><a href="docs/duo-bestanden.md#1cijferho-bestand">1cijferHO-bestand</a>, met bestandsbeschrijving en decodeertabellen.</li></ul>Optioneel<ul><li><a href="docs/duo-bestanden.md#vakkenbestand-vakhavw">Vakkenbestand (VAKHAVW)</a>.</li></ul></td>
<td valign="top">Leesbare tabellen als invoer voor Staat van de Onderwijsinstelling.</td>
</tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/wisselstroom">wisselstroom</a></td>
<td valign="top">hbo en wo</td>
<td valign="top">Eén van:<ul><li><a href="https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp">Analysebestand voorlopige bekostiging (VLPBEK)</a>.</li><li><a href="https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp">Analysebestand definitieve bekostiging (DEFBEK)</a>.</li></ul></td>
<td valign="top">Per inschrijving of een student blijft, wisselt, stapelt, stopt of begint, en naar welke instelling. Stroomdiagram.</td>
</tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/staat-van-onderwijsinstelling-mbo">Staat van de Onderwijsinstelling MBO</a></td>
<td valign="top">mbo</td>
<td valign="top"><ul><li><a href="https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/studentenadministratie/rod-en-uw-administratie.jsp">Registratieoverzicht (RO)</a>: één of meer. Eén RO beslaat maximaal 2 jaar. Diplomaresultaat en startersresultaat zijn pas volledig met minstens 6 jaar, dus 3 opeenvolgende RO's.</li></ul>Optioneel<ul><li><a href="https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/terugmelding-bekostigingsgrondslagen-individueel.jsp">Terugmelding bekostigingsgrondslagen individueel (TBG-i)</a>, alleen samen met minstens één RO.</li></ul></td>
<td valign="top">Dashboard met de indicatoren uit de Regeling studiesucces mbo, cohorten en loopbanen.</td>
</tr>
</table>

### Bekostiging

<table>
<tr><th align="left">Product</th><th align="left">Voor</th><th align="left">DUO-bestanden</th><th align="left">Levert</th></tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/ho-bekostiging-bestanden">ho-bekostiging-bestanden</a></td>
<td valign="top">hbo en wo</td>
<td valign="top">Eén of meer van:<ul><li><a href="https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp">Analysebestand voorlopige bekostiging (VLPBEK)</a>.</li><li><a href="https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp">Analysebestand definitieve bekostiging (DEFBEK)</a>.</li><li><a href="docs/duo-bestanden.md#historisch-bestand-definitieve-bekostiging-hisbek">Historisch bestand definitieve bekostiging (HISBEK)</a>.</li></ul></td>
<td valign="top">Schone tabellen en datamodel. Dashboard met bekostigingstrechter, redenen van niet-bekostiging, voorlopig tegenover definitief en historie.</td>
</tr>
<tr>
<td valign="top"><a href="https://github.com/cedanl/mbo-bekostiging-bestanden">mbo-bekostiging-bestanden</a></td>
<td valign="top">mbo</td>
<td valign="top">Eén of meer van:<ul><li><a href="https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/studentenadministratie/rod-en-uw-administratie.jsp">Registratieoverzicht (RO)</a>.</li><li><a href="https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/terugmelding-bekostigingsgrondslagen-individueel.jsp">Terugmelding bekostigingsgrondslagen individueel (TBG-i)</a>.</li><li><a href="docs/duo-bestanden.md#afslag-registerlevering-ip">Afslag registerlevering IP</a>.</li></ul></td>
<td valign="top">Schone tabellen en datamodel. Dashboard met aantallen.</td>
</tr>
</table>

### Hoe de tools met gegevens omgaan

- De tools draaien op een computer van de instelling. Er gaan geen gegevens naar CEDA of naar een server.
- Ze lezen de bestanden zoals DUO ze levert. Ze rekenen de bekostiging niet opnieuw uit.
- Cijfers zijn indicatief. Het zijn geen officiële cijfers van DUO of de Inspectie.
- Elke tool heeft demodata, zodat je hem kunt bekijken zonder echte gegevens.

Welke DUO-bestanden dit zijn, wat erin staat en waar een instelling ze ophaalt: zie [DUO-bestanden](docs/duo-bestanden.md).

## Waar we heen willen

Mbo en hbo/wo stellen dezelfde vragen. Krijgen de bestanden dezelfde vorm, dan kan één tool alle sectoren bedienen, zonder de regels te veranderen. Die kans willen we in drie richtingen benutten, uitgewerkt in [Waar we heen willen](docs/richting.md):

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

Handleidingen en technische documentatie per tool: zie [Documentatie](docs/documentatie.md).

## Contact

Vragen of zin om mee te bouwen?

- E-mail: [ceda@surf.nl](mailto:ceda@surf.nl)
- Community: [CEDA op de Data & AI-community van Npuls](https://community-data-ai.npuls.nl/groups/view/44d20066-53a8-48c2-b4e9-be348e05d273/project-center-for-educational-data-analytics-ceda)
- GitHub: [github.com/cedanl](https://github.com/cedanl)
