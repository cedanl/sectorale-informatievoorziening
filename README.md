<p align="right">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/npuls-logo-wit.png">
    <img src="assets/npuls-logo-zwart.png" alt="Npuls" height="48">
  </picture>
</p>

# Sectorale informatievoorziening

**Mbo- en ho-instellingen stellen dezelfde vragen aan de bestanden die ze van DUO krijgen. Hoe gaat het met onze studenten? Wie wordt bekostigd, en waarom niet? CEDA maakt die bestanden bruikbaar met open source tools die binnen de eigen instelling draaien, voor beide sectoren.**

Deze repo beschrijft het project als geheel: het verhaal, welke DUO-bestanden we gebruiken, wat er al werkt en waar we heen willen. De code staat in de repo's van de afzonderlijke producten, waar deze pagina naar verwijst.

CEDA (Centre of Educational Data Analytics) is een team binnen [Npuls](https://npuls.nl) dat samen met mbo, hbo en wo open source tools maakt voor onderwijsdata.

## Waarom

Elke instelling krijgt van DUO bestanden over haar studenten en haar bekostiging. Die bestanden zijn gemaakt voor uitwisseling, niet voor analyse: vaste kolombreedtes of tekst gescheiden door `|`, meerdere soorten regels door elkaar en codes zonder uitleg. De beschrijvingen staan in PDF's en veranderen vaak (ho 23 versies sinds 2020, mbo 19 sinds 2019).

Nu bouwt elke instelling haar eigen manier om deze bestanden in te lezen, met eigen definities. Dat kost tijd, geeft fouten en maakt cijfers van instellingen moeilijk te vergelijken. Het bewerkbaar en betrouwbaar maken van data is het grootste deel van het werk in elk data-project. CEDA doet dat werk één keer, open, en zo dat elke instelling het kan gebruiken.

## Doel

Elke mbo-, hbo- en wo-instelling kan met de eigen DUO-bestanden betrouwbare cijfers maken over **studiesucces** en **bekostiging**: met vaste, gedocumenteerde definities, op dezelfde manier in beide sectoren en zonder dat de gegevens de instelling verlaten.

Dit draagt bij aan de Npuls-ambitie om AI en data waarde(n)vol in te zetten. Goede, verbonden data is de basis voor elk dashboard, elke voorspelling en elke AI-toepassing die erop volgt.

## De informatiestroom

<p align="center">
  <img src="assets/informatiestroom.svg" alt="Boom van DUO-bestand naar inzicht. Hoger onderwijs: 1cijferHO via 1cijferho naar Staat van de Onderwijsinstelling; VLPBEK en DEFBEK via ho-bekostiging-bestanden naar een bekostigingsdashboard. Mbo: geen studentenbestand; RO en TBG-i naar Staat van de Onderwijsinstelling MBO; RO, TBG-i en GRONDSLAG IP via mbo-bekostiging-bestanden naar een bekostigingsdashboard." width="100%">
</p>

Lees de boom van onder naar boven. De wortels zijn de bestanden die DUO aan een instelling levert. De stam zijn de tools die ze bruikbaar maken. De kruin zijn de producten waarmee een instelling haar vragen beantwoordt.

Het verschil tussen de sectoren zit in de wortels. Het ho heeft met 1cijferHO een studentenbestand dat voor studiesucces bedoeld is. Het mbo heeft dat niet; daar leiden we studiesucces af uit de bekostigingsbestanden RO en TBG-i.

## Producten en de DUO-bestanden die ze gebruiken

| Product | Sector | Vraag | DUO-bestanden | Levert | Stand |
|---|---|---|---|---|---|
| [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) | ho | Studiesucces | 1cijferHO (via 1cijferho), optioneel VAKHAVW | Analysebestand per student, dashboard met instroom, rendement, uitval en studiewissel, benchmarkrapport om te delen | Werkt. Oorspronkelijk ontwikkeld bij Avans Hogeschool |
| [1cijferho](https://github.com/cedanl/1cijferho) | ho | Voorbewerking | 1cijferHO met decodeertabellen, VAKHAVW | Leesbare tabellen (CSV, Parquet) als invoer voor Staat van de Onderwijsinstelling | Werkt |
| [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden) | ho | Bekostiging | VLPBEK, DEFBEK, optioneel HISBEK | Schone tabellen, datamodel en dashboard: bekostigingstrechter, redenen van niet-bekostiging, voorlopig tegenover definitief, historie | Eerste versie |
| [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo) | mbo | Studiesucces | RO (meerdere, tot 10 jaar), optioneel TBG-i | Dashboard met de indicatoren uit de Regeling studiesucces mbo, cohorten en loopbanen | Eerste versie, getest op demodata |
| [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) | mbo | Bekostiging | RO, TBG-i, GRONDSLAG IP | Schone tabellen, datamodel en dashboard met aantallen. Redenen van niet-bekostiging volgen | Eerste versie |

Verwant: [wisselstroom](https://github.com/cedanl/wisselstroom) (R-pakket) laat met VLPBEK en DEFBEK zien welke ho-studenten blijven, wisselen, stapelen of stoppen.

### De DUO-bestanden in het kort

| Bestand | Sector | Wat erin staat | Gebruikt door |
|---|---|---|---|
| 1cijferHO | ho | Door DUO bewerkt studentenbestand van de instelling: inschrijvingen, diploma's en vooropleiding over meerdere jaren | 1cijferho, Staat van de Onderwijsinstelling |
| VAKHAVW | ho | Havo- en vwo-cijfers van instromers | Staat van de Onderwijsinstelling (optioneel) |
| VLPBEK, DEFBEK | ho | Analysebestand: voorlopige en definitieve bekostigingsuitkomst per inschrijving en graad, met statuscodes | ho-bekostiging-bestanden, wisselstroom |
| HISBEK | ho | Inschrijvingen en graden uit eerdere definitieve bekostigingsjaren | ho-bekostiging-bestanden (optioneel) |
| RO | mbo | Registratieoverzicht: alle inschrijvingen en diploma's in een gekozen periode van maximaal 2 jaar | Staat van de Onderwijsinstelling MBO, mbo-bekostiging-bestanden |
| TBG-i | mbo | Per inschrijving en diploma de gegevens voor de bekostiging, met signalen | Staat van de Onderwijsinstelling MBO (optioneel), mbo-bekostiging-bestanden |
| GRONDSLAG IP | mbo | Afslag van het register op 1 oktober, met bekostigingsinformatie, zonder BSN | mbo-bekostiging-bestanden |

Bron: de bestandsbeschrijvingen (Programma van Eisen) van DUO, mbo-versie 4.8.3 en ho-versie 26.3.1.

### Hoe de tools met gegevens omgaan

- De tools draaien op een computer van de instelling. Er gaan geen gegevens naar CEDA of naar een server.
- Ze lezen de bestanden zoals DUO ze levert. Ze rekenen de bekostiging niet opnieuw uit.
- Cijfers zijn indicatief. Het zijn geen officiële cijfers van DUO of de Inspectie.
- Elke tool heeft demodata, zodat je hem kunt bekijken zonder echte gegevens.

## Wat we leerden bij het bouwen

- **Zelfde vragen, bijna dezelfde bestanden.** Bijna elk bestand heeft een tegenhanger in de andere sector, van registratieoverzicht tot accountantsrapport.
- **Kleine verschillen kosten veel werk.** Datums, bestandsnamen en bestandstypen wijken af: `2025-01-30` tegenover `20250130`, XML tegenover CSV. Wie een tool bouwt, neemt elk veld met de hand over uit de PDF.
- **De sectoren zien niet hetzelfde.** Een ho-instelling ziet ook inschrijvingen en graden van eigen studenten bij andere instellingen. Een mbo-instelling ziet alleen de eigen inschrijvingen. Een mbo-student die overstapt, lijkt daardoor op een student die stopt.

## Waar we heen willen

Drie richtingen. Geen ervan raakt de bekostigingsregels; het gaat om de vorm en uitleg van bestanden en om wat tools ermee doen.

**1. Eén open beschrijving van de bestanden.** Elk veld en elke code als tabel, naast de PDF. Tools lezen de bestanden dan automatisch in en een nieuwe versie laat zien wat er veranderde.
*Stand:* we hebben beschrijvingen voor vijf bestandssoorten, met de hand overgenomen uit de PDF's. *Volgende stap:* de TBG-i (mbo) en het analysebestand (ho) in één vorm naast elkaar zetten. Die twee beantwoorden dezelfde vraag: wie wordt bekostigd en waarom niet.

**2. Eén overzicht: wie wordt bekostigd en waarom niet.** Met de voorlopige bestanden ziet een instelling tijdens het jaar de verwachte uitkomst, met de redenen, en wat ze in de eigen registratie kan nakijken.
*Stand:* de ho-tool toont de redenen en zet voorlopig naast definitief. De mbo-tool toont de aantallen. *Volgende stap:* mbo-signalen en ho-statuscodes in dezelfde groepen redenen onderbrengen en de mbo-kant bouwen. Het nut is nog niet getoetst bij instellingen.

**3. Studiesucces in het mbo op dezelfde manier volgen als in het ho.** Uit RO en TBG-i per instelling een bestand maken in de vorm van 1cijferHO.
*Stand:* 47 van de 115 velden van 1cijferHO zijn per instelling te vullen. Dat is genoeg voor rendement en uitval per opleiding, en te weinig voor kansengelijkheid, omdat vooropleiding, herkomst en regio ontbreken. Staat van de Onderwijsinstelling MBO draait met een eigen mbo-dashboard op demodata. *Volgende stap:* de cijfers toetsen op echte data van één instelling.

### Kansen die we zien

Omdat beide sectoren dezelfde vragen stellen, kan één tool beide bedienen als de bestanden dezelfde vorm hebben. Daarvoor zijn kleine stappen genoeg, zonder de regels te veranderen: een schema per bestandssoort, codelijsten als tabel, een wijzigingslog per versie en dezelfde begrippen en groepen redenen in mbo en ho. Wat echt bij een sector hoort, zoals stage in het mbo en joint degrees in het ho, blijft verschillen. Meer hierover in de presentatie *MBO en HO: wat is er mogelijk met de bekostigingsbestanden?* hieronder.

### Waar we graag over in gesprek gaan

- Bij welke statuscodes en signalen kan een instelling zelf iets nakijken of herstellen?
- Komen opleidingscodes in mbo en ho straks uit één register (RIO)?
- Welke gegevens uit de andere sector zijn zinvol om aan te vullen, zoals een meerjarig bestand voor het mbo?
- Hoe controleren instellingen de bekostigingsuitkomst nu, en wat voegt een tool daaraan toe?

## Presentaties

| Datum | Titel | Over |
|---|---|---|
| 21 september 2026 | [MBO en HO: wat is er mogelijk met de bekostigingsbestanden?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/260921_MBO_HO_bekostigingsbestanden.pdf) (concept) | De bestanden van beide sectoren naast elkaar, wat tools er nu mee kunnen en welke kleine aanpassingen veel opleveren |
| 1 oktober 2026 | [Een 1CHO voor het mbo?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261001_mbo_1cho_haalbaarheid.pdf) | Haalbaarheid van een mbo-versie van 1cijferHO: wat werkt, wat ontbreekt en waarom |
| 4 november 2026 | [Staat van de Onderwijsinstelling: impactsessie](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261104_staat1cho_impactsessie/261104_staat1cho_impactsessie.pdf) | Het ho-product in de praktijk |

## Documentatie

- [1cijferho](https://cedanl.github.io/1cijferho/): 1cijferHO-bestanden omzetten
- [ho-bekostiging-bestanden](https://cedanl.github.io/ho-bekostiging-bestanden/): bestanden, datamodel en kwaliteitscontroles
- [mbo-bekostiging-bestanden](https://cedanl.github.io/mbo-bekostiging-bestanden/): bestanden, datamodel en ontwerpkeuzes
- [wisselstroom](https://cedanl.github.io/wisselstroom/): studentstromen in het ho
- [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling#readme) en [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo#readme): installeren, gebruiken en definities
- [Haalbaarheidsonderzoek 1CHO voor het mbo](https://github.com/cedanl/mbo-bekostiging-bestanden/issues/389)

## Contact

Vragen, feedback of zin om mee te bouwen?

- E-mail: [ceda@surf.nl](mailto:ceda@surf.nl)
- Community: [community.npuls.nl/groups/data-ai](https://community.npuls.nl/groups/data-ai)
- GitHub: [github.com/cedanl](https://github.com/cedanl)

---

CEDA · Npuls · **Onderwijs bewegen.**
