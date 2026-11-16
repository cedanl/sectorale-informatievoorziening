# Sectorale informatievoorziening

Projectrepo van CEDA/Npuls. Bevat alleen documentatie: het verhaal, de samenhang en de verwijzingen naar de productrepo's. Geen code, behalve het script dat de infographic maakt.

## Inhoud

- `README.md`: de pagina voor beleidsmakers en stakeholders zoals DUO. Primaire interface.
- `assets/informatiestroom.svg`: de boom-infographic. Pas niet met de hand aan; wijzig `assets/genereer_informatiestroom.py` en draai `python assets/genereer_informatiestroom.py assets/informatiestroom.svg`.
- `assets/npuls-logo-*.png`: officieel Npuls-logo voor licht en donker thema.
- `docs/specs/`: beslis-samenvattingen.

## Afspraken

- Nederlands. Schrijf voor beleidsmakers zonder technische voorkennis: bondig, direct, geen verkooppraat, geen beleidsadvies.
- Huisstijl: Npuls. Alleen kleurcombinaties uit de huisstijl, General Sans met Arial als terugval, zwarte lijnen.
- Houd de tabel met producten en DUO-bestanden gelijk met de README's van de productrepo's. Verandert een product van invoer of stand, werk dan de tabel en de infographic bij.
- Presentaties staan in `cedanl/clidev-presentaties/exports/`. Link ernaartoe; zet geen PDF's in deze repo.
- Noem alleen wat aantoonbaar werkt. Wat nog niet getoetst is, krijgt die vermelding.
