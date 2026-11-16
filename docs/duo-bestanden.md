# DUO-bestanden

De bestanden die de tools van dit project gebruiken: wat erin staat, waar een instelling ze ophaalt en welke tool ze leest. Terug naar de [projectpagina](../README.md).

## Studiesucces

| Bestand | Sector | Wat erin staat | Ophalen | Gebruikt door |
|---|---|---|---|---|
| 1cijferHO | hbo en wo | Door DUO bewerkt studentenbestand van de instelling: inschrijvingen, diploma's en vooropleiding over meerdere jaren | Jaarlijkse levering van DUO aan de instelling. Meestal ontvangen door BI, informatiemanagement of de studentenadministratie. De bestandsbeschrijving zit in de levering | [1cijferho](https://github.com/cedanl/1cijferho), [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) |
| VAKHAVW | hbo en wo | Havo- en vwo-cijfers van instromers | Onderdeel van de 1cijferHO-levering | [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) (optioneel) |
| RO (registratieoverzicht) | mbo | Alle inschrijvingen en diploma's in een gekozen periode van maximaal 2 jaar | [Mijn DUO, registratieoverzicht opvragen](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/studentenadministratie/rod-en-uw-administratie.jsp) | [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo), [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) |

Het mbo heeft geen studentenbestand zoals 1cijferHO. Staat van de Onderwijsinstelling MBO leidt studiesucces daarom af uit RO en, als die er is, TBG-i.

## Bekostiging

| Bestand | Sector | Wat erin staat | Ophalen | Gebruikt door |
|---|---|---|---|---|
| VLPBEK (voorlopig analysebestand) | hbo en wo | Voorlopige bekostigingsuitkomst per inschrijving en graad, met statuscodes | [Mijn DUO, voorlopige bekostigingsstatus opvragen](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp) | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom) |
| DEFBEK (definitief analysebestand) | hbo en wo | Definitieve bekostigingsuitkomst per inschrijving en graad, met statuscodes | [Automatisch in Mijn DUO na de berekening, 90 dagen beschikbaar](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp) | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom) |
| HISBEK | hbo en wo | Inschrijvingen en graden uit eerdere definitieve bekostigingsjaren | Levering van DUO, beschreven in het Programma van Eisen | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden) (optioneel) |
| TBG-i | mbo | Per inschrijving en diploma de gegevens voor de bekostiging, met signalen | [Mijn DUO, voorlopig aanvragen of definitief downloaden](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/terugmelding-bekostigingsgrondslagen-individueel.jsp) | [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden), [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo) (optioneel) |
| GRONDSLAG IP | mbo | Afslag van het register op 1 oktober, met bekostigingsinformatie, zonder BSN | Levering van DUO, beschreven in het Programma van Eisen | [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) |

## Bestandsbeschrijvingen

DUO beschrijft de bestanden in een Programma van Eisen per sector. De tools zijn gebouwd op deze versies:

- Hbo en wo: [Programma van Eisen hoger onderwijs](https://duo.nl/zakelijk/images/programma-van-eisen-hoger-onderwijs.pdf), versie 26.3.1
- Mbo: [Programma van Eisen mbo-instellingen](https://duo.nl/zakelijk/images/pve-mbo-instellingen.pdf), versie 4.8.3

DUO werkt deze documenten regelmatig bij. De links wijzen naar de actuele versie.
