# DUO-bestanden

De bestanden die de tools van dit project gebruiken, met de namen die DUO gebruikt. Per bestand: wat erin staat, welke periode het beslaat, waar een instelling het ophaalt en waar DUO het beschrijft. Terug naar de [projectpagina](../README.md).

DUO beschrijft de bestanden in een Programma van Eisen (PvE) per sector:

- Hbo en wo: [Programma van Eisen hoger onderwijs](https://duo.nl/zakelijk/images/programma-van-eisen-hoger-onderwijs.pdf). De tools zijn gebouwd op versie 26.3.1.
- Mbo: [Programma van Eisen mbo-instellingen](https://duo.nl/zakelijk/images/pve-mbo-instellingen.pdf). De tools zijn gebouwd op versie 4.8.3; de verwijzingen hieronder volgen versie 4.9.1.

## Overzicht

| DUO-naam | Sector | Bestandsnaam begint met | Gebruikt voor |
|---|---|---|---|
| [1cijferHO-bestand](#1cijferho-bestand) | hbo en wo | `EV` | Studiesucces |
| [Vakkenbestand (VAKHAVW)](#vakkenbestand-vakhavw) | hbo en wo | `VAKHAVW` | Studiesucces |
| [Analysebestand voorlopige bekostiging](#analysebestand-voorlopige-bekostiging-vlpbek) | hbo en wo | `VLPBEK` | Bekostiging, studentstromen |
| [Analysebestand definitieve bekostiging](#analysebestand-definitieve-bekostiging-defbek) | hbo en wo | `DEFBEK` | Bekostiging, studentstromen |
| [Historisch bestand definitieve bekostiging](#historisch-bestand-definitieve-bekostiging-hisbek) | hbo en wo | `HISBEK` | Bekostiging |
| [Registratieoverzicht](#registratieoverzicht-ro) | mbo | `RO` | Studiesucces, bekostiging |
| [Terugmelding bekostigingsgrondslagen individueel](#terugmelding-bekostigingsgrondslagen-individueel-tbg-i) | mbo | `TBGI` | Studiesucces, bekostiging |
| [Afslag registerlevering IP](#afslag-registerlevering-ip) | mbo | `GRONDSLAG_IP_MBO` | Bekostiging |

Het mbo heeft geen bestand zoals het 1cijferHO-bestand. Staat van de Onderwijsinstelling MBO leidt studiesucces daarom af uit het registratieoverzicht en, als die er is, de TBG-i.

## Hbo en wo

### 1cijferHO-bestand

- **Wat erin staat:** door DUO samengesteld studentenbestand met inschrijvingen, diploma's en vooropleiding. Een instelling ontvangt het deel met de eigen inschrijvingen en diploma's.
- **Periode:** de hele historie van de studenten. Elke levering vervangt de vorige, dus alleen de nieuwste is nodig.
- **Ophalen:** DUO (afdeling Informatieproducten) stelt het bestand samen en levert de instelling het deel met de eigen gegevens. Er is geen openbare DUO-pagina voor. Meestal ontvangt BI, informatiemanagement of de studentenadministratie het.
- **Beschrijving:** zit in de levering (`Bestandsbeschrijving_1cyferho_…`, met decodeertabellen `Dec_…`).
- **Gebruikt door:** [1cijferho](https://github.com/cedanl/1cijferho), daarna [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling).

### Vakkenbestand (VAKHAVW)

- **Wat erin staat:** cijfers voor havo- en vwo-vakken van instromers.
- **Periode:** meerdere jaren, zelfde levering als het 1cijferHO-bestand.
- **Ophalen:** onderdeel van de levering van het 1cijferHO-bestand.
- **Beschrijving:** zit in de levering (`Bestandsbeschrijving_Vakkenbestanden.txt`).
- **Gebruikt door:** [Staat van de Onderwijsinstelling](https://github.com/cedanl/staat-van-onderwijsinstelling) (optioneel).

### Analysebestand voorlopige bekostiging (VLPBEK)

- **Wat erin staat:** van alle inschrijvingen (deelnames) en graden (resultaten) voor het lopende bekostigingsjaar de voorlopige bekostigingsstatus, met statuscodes en grondslag.
- **Periode:** één bekostigingsjaar.
- **Bestandsnaam:** `VLPBEK_<bekostigingsjaar>_<aanmaakdatum>_<instellingscode>.CSV`
- **Ophalen:** [Mijn DUO, voorlopige bekostigingsstatus opvragen](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp). Klaar binnen 2 werkdagen.
- **Beschrijving:** PvE hoger onderwijs, hoofdstuk 17 (Bestandsbeschrijving analysebestand); aanvragen in paragraaf 4.5.2.
- **Gebruikt door:** [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom).

### Analysebestand definitieve bekostiging (DEFBEK)

- **Wat erin staat:** hetzelfde als het voorlopige analysebestand, met de definitieve bekostigingsstatus.
- **Periode:** één bekostigingsjaar.
- **Bestandsnaam:** `DEFBEK_<bekostigingsjaar>_<aanmaakdatum>_<instellingscode>.CSV`
- **Ophalen:** [automatisch in Mijn DUO nadat de bekostiging is berekend](https://duo.nl/zakelijk/hoger-onderwijs/studentenadministratie/rod-controleren/bekostigingsstatus-studenten.jsp), 90 dagen beschikbaar.
- **Beschrijving:** PvE hoger onderwijs, hoofdstuk 17; levering in paragraaf 4.7.1.
- **Gebruikt door:** [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden), [wisselstroom](https://github.com/cedanl/wisselstroom).

### Historisch bestand definitieve bekostiging (HISBEK)

- **Wat erin staat:** alle inschrijvingen en graden die van belang waren voor de definitieve bekostiging in eerdere jaren, met hun status.
- **Periode:** alle eerdere definitieve bekostigingsjaren.
- **Bestandsnaam:** `HISBEK_<laatste bekostigingsjaar>_<aanmaakdatum>_<instellingscode>.CSV`
- **Ophalen:** in Mijn DUO, op hetzelfde aanvraagscherm als het analysebestand voorlopige bekostiging (PvE hoger onderwijs, paragraaf 4.5.2).
- **Beschrijving:** PvE hoger onderwijs, hoofdstuk 19 (Bestandsbeschrijving historische bekostiging).
- **Gebruikt door:** [ho-bekostiging-bestanden](https://github.com/cedanl/ho-bekostiging-bestanden) (optioneel).

## Mbo

### Registratieoverzicht (RO)

- **Wat erin staat:** alle inschrijvingen en diploma's van de instelling zoals ze in het Register Onderwijsdeelnemers (ROD) staan.
- **Periode:** een selectieperiode die de instelling kiest, van maximaal 2 jaar. Staat van de Onderwijsinstelling MBO heeft minstens 6 jaar nodig voor een volledig diplomaresultaat en startersresultaat, dus 3 opeenvolgende registratieoverzichten.
- **Bestandsnaam:** `RO_<instellingscode>_<begindatum>_<einddatum>.CSV`
- **Ophalen:** [Mijn DUO, registratieoverzicht opvragen](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/studentenadministratie/rod-en-uw-administratie.jsp). Klaar de volgende werkdag.
- **Beschrijving:** PvE mbo-instellingen, bijlage 7 (Bestandsbeschrijving registratieoverzicht); aanvragen in paragraaf 7.2.
- **Gebruikt door:** [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo), [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden).

### Terugmelding bekostigingsgrondslagen individueel (TBG-i)

- **Wat erin staat:** de bekostigingsgrondslagen per inschrijving en diploma, met signalen.
- **Periode:** één bekostigingsjaar (t): inschrijvingen op de teldata 1 oktober (t-2) en 1 februari (t-1), en diploma's behaald in kalenderjaar t-2.
- **Bestandsnaam:** `TBGI_<instellingscode>_<bekostigingsjaar>_<aanmaakdatum>.XML`
- **Ophalen:** [Mijn DUO, voorlopig aanvragen of definitief downloaden](https://duo.nl/zakelijk/middelbaar-beroepsonderwijs/bekostiging-en-subsidies/bekostiging-mbo/terugmelding-bekostigingsgrondslagen-individueel.jsp). Drie weken beschikbaar.
- **Beschrijving:** PvE mbo-instellingen, bijlage 8 (Bestandsbeschrijving TBG-i).
- **Gebruikt door:** [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden), [Staat van de Onderwijsinstelling MBO](https://github.com/cedanl/staat-van-onderwijsinstelling-mbo) (optioneel).

### Afslag registerlevering IP

- **Wat erin staat:** de gegevens van de eigen instelling uit de registerlevering waarmee de afdeling Informatieproducten (IP) van DUO haar informatieproducten maakt. Zonder persoonsgebonden nummer (wel een omgenummerd nummer) en zonder geboortedatum.
- **Periode:** peildatum 1 oktober van het lopende studiejaar.
- **Bestandsnaam:** `GRONDSLAG_IP_MBO_<instellingscode>_<einddatum selectieperiode>_<studiejaar>.csv`, gezipt geplaatst.
- **Ophalen:** DUO plaatst het bestand op de beveiligde site nadat IP akkoord heeft gegeven. Er is geen openbare DUO-pagina voor.
- **Beschrijving:** PvE mbo-instellingen, hoofdstuk 17 (Bestandbeschrijving afslag register-levering IP); proces in paragraaf 7.3.
- **Gebruikt door:** [mbo-bekostiging-bestanden](https://github.com/cedanl/mbo-bekostiging-bestanden).

## Wat een instelling ziet

De analysebestanden voor hbo en wo bevatten ook inschrijvingen en graden van eigen studenten bij andere instellingen. De mbo-bestanden bevatten alleen de eigen inschrijvingen. Een mbo-student die naar een andere instelling gaat, is daarin niet te onderscheiden van een student die stopt.
