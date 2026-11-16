# DUO-bestanden

De bestanden die de tools van dit project gebruiken: wat erin staat, welke periode ze beslaan, waar een instelling ze ophaalt en welke tool ze leest. Terug naar de [projectpagina](../README.md).

## Studiesucces

| Bestand | Sector | Wat erin staat | Periode | Ophalen | Gebruikt door |
|---|---|---|---|---|---|
| 1cijferHO | hbo en wo | Door DUO bewerkt studentenbestand van de instelling: inschrijvingen, diploma's en vooropleiding | Hele historie van de studenten. Elke levering vervangt de vorige, dus alleen de nieuwste is nodig | Jaarlijkse levering van DUO aan de instelling. Meestal ontvangen door BI, informatiemanagement of de studentenadministratie. De bestandsbeschrijving zit in de levering | [1cijferho](https://github.com/cedanl/1cijferho), [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) |
| VAKHAVW | hbo en wo | Havo- en vwo-cijfers van instromers | Meerdere jaren, zelfde levering als 1cijferHO | Onderdeel van de 1cijferHO-levering | [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) (optioneel) |
| RO (registratieoverzicht) | mbo | Alle inschrijvingen en diploma's zoals ze in het register staan | Gekozen periode van maximaal 2 jaar. Voor 10 jaar zijn 5 opeenvolgende RO's nodig | [Mijn DUO, registratieoverzicht opvragen](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/studentenadministratie/rod-en-uw-administratie.jsp) | [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo), [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) |

Het mbo heeft geen studentenbestand zoals 1cijferHO. Staat van de Onderwijsinstelling MBO leidt studiesucces daarom af uit RO en, als die er is, TBG-i.

## Bekostiging

| Bestand | Sector | Wat erin staat | Periode | Ophalen | Gebruikt door |
|---|---|---|---|---|---|
| VLPBEK (voorlopig analysebestand) | hbo en wo | Voorlopige bekostigingsuitkomst per inschrijving en graad, met statuscodes | Eén bekostigingsjaar | [Mijn DUO, voorlopige bekostigingsstatus opvragen](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp) | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom) |
| DEFBEK (definitief analysebestand) | hbo en wo | Definitieve bekostigingsuitkomst per inschrijving en graad, met statuscodes | Eén bekostigingsjaar | [Automatisch in Mijn DUO na de berekening, 90 dagen beschikbaar](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp) | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom) |
| HISBEK | hbo en wo | Inschrijvingen en graden met hun bekostigingsstatus | Eerdere definitieve bekostigingsjaren | Levering van DUO, beschreven in het Programma van Eisen | [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden) (optioneel) |
| TBG-i | mbo | Per inschrijving en diploma de gegevens voor de bekostiging, met signalen | Eén bekostigingsjaar: inschrijvingen op 1 oktober en diploma's in het tweede kalenderjaar vóór het bekostigingsjaar | [Mijn DUO, voorlopig aanvragen of definitief downloaden](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/terugmelding-bekostigingsgrondslagen-individueel.jsp) | [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden), [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo) (optioneel) |
| GRONDSLAG IP | mbo | Afslag van het register met bekostigingsinformatie, zonder BSN | Eén peildatum: 1 oktober | Levering van DUO, beschreven in het Programma van Eisen | [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden) |

## Wat een instelling ziet

Het analysebestand voor hbo en wo (VLPBEK, DEFBEK) bevat ook inschrijvingen en graden van eigen studenten bij andere instellingen. De mbo-bestanden bevatten alleen de eigen inschrijvingen. Een mbo-student die naar een andere instelling gaat, is daarin niet te onderscheiden van een student die stopt.

## Bestandsbeschrijvingen

DUO beschrijft de bestanden in een Programma van Eisen per sector. De tools zijn gebouwd op deze versies:

- Hbo en wo: [Programma van Eisen hoger onderwijs](https://duo.nl/zakelijk/images/programma-van-eisen-hoger-onderwijs.pdf), versie 26.3.1
- Mbo: [Programma van Eisen mbo-instellingen](https://duo.nl/zakelijk/images/pve-mbo-instellingen.pdf), versie 4.8.3

DUO werkt deze documenten regelmatig bij. De links wijzen naar de actuele versie.
