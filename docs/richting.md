# Waar we heen willen

Terug naar de [projectpagina](../README.md).

## Wat we zagen bij het bouwen

Mbo en hbo/wo stellen dezelfde vragen aan bijna dezelfde bestanden. Bijna elk bestand heeft een tegenhanger in de andere sector, van registratieoverzicht tot accountantsrapport. De verschillen zitten vooral in de vorm: datums (`2025-01-30` tegenover `20250130`), bestandsnamen, XML tegenover CSV, en beschrijvingen in PDF's die vaak veranderen (hbo en wo 23 versies sinds 2020, mbo 19 sinds 2019).

Twee verschillen zijn wezenlijk.

- **Een studentenbestand.** Hbo en wo krijgen het 1cijferHO-bestand, dat DUO samenstelt voor onderzoek naar studiesucces, met de hele historie van de studenten en hun vooropleiding. Het mbo heeft zo'n bestand niet. Daar voegen we registratieoverzichten samen. Elk beslaat maximaal 2 jaar; voor volledige cijfers zijn er minstens 3 nodig. Vooropleiding en herkomst staan er niet in. Richting 3 gaat hierover.
- **Wat een instelling ziet.** Een hbo- of wo-instelling ziet in de bekostigingsbestanden ook inschrijvingen en graden van eigen studenten bij andere instellingen. Een mbo-instelling ziet alleen de eigen inschrijvingen, waardoor een student die overstapt lijkt op een student die stopt.

## Kansen

Omdat mbo en hbo/wo dezelfde vragen stellen, kan één tool alle sectoren bedienen zodra de bestanden dezelfde vorm hebben. Daarvoor zijn kleine stappen genoeg, zonder de regels te veranderen. Wat echt bij een sector hoort, zoals stage in het mbo en joint degrees in hbo en wo, blijft verschillen. Dezelfde tool betekent ook dezelfde definities, dus cijfers die instellingen onderling kunnen vergelijken en samen kunnen analyseren. Meer in [MBO en HO: wat is er mogelijk met de bekostigingsbestanden?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/260921_MBO_HO_bekostigingsbestanden.pdf) (concept).

## Drie richtingen

Die kansen willen we in drie richtingen benutten.

**1. Eén open beschrijving van de bestanden.** Elk veld en elke code als tabel, naast de PDF. Tools lezen de bestanden dan automatisch in en een nieuwe versie laat zien wat er veranderde.
*Nu:* beschrijvingen voor vijf bestandssoorten, met de hand overgenomen uit de PDF's. *Volgende stap:* de TBG-i (mbo) en het analysebestand (hbo en wo) in één vorm naast elkaar zetten. Die twee beantwoorden dezelfde vraag: wie wordt bekostigd en waarom niet.

**2. Eén overzicht: wie wordt bekostigd en waarom niet.** Met de voorlopige bestanden ziet een instelling tijdens het jaar de verwachte uitkomst, met de redenen, en wat ze in de eigen registratie kan nakijken.
*Nu:* de tool voor hbo en wo toont de redenen en zet voorlopig naast definitief; de mbo-tool toont de aantallen. *Volgende stap:* mbo-signalen en statuscodes uit hbo en wo in dezelfde groepen redenen onderbrengen en de mbo-kant bouwen. Het nut is nog niet getoetst bij instellingen.

**3. Studiesucces in het mbo op dezelfde manier volgen als in hbo en wo.** Uit RO en TBG-i per instelling een bestand maken in de vorm van 1cijferHO.
*Nu:* 47 van de 115 velden van 1cijferHO zijn per instelling te vullen. Dat is genoeg voor rendement en uitval per opleiding, en te weinig voor kansengelijkheid, omdat vooropleiding, herkomst en regio ontbreken. Staat van de Onderwijsinstelling MBO draait met een eigen mbo-dashboard op demodata. *Volgende stap:* de cijfers toetsen op echte data van één instelling. Meer in [Een 1CHO voor het mbo?](https://github.com/cedanl/clidev-presentaties/blob/main/exports/261001_mbo_1cho_haalbaarheid.pdf)
