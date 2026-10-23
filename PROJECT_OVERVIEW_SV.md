# Project Ascension — Översikt

| Fält | Värde |
|---|---|
| Dokument | Projektöversikt (svenska) |
| Status | Orientering, inte Canon |
| Senast uppdaterad | 2026-10-23 |

> **Berättelsen styr inte simulationen. Simulationen producerar berättelsen.**

Det här dokumentet är en snabb väg in i projektet. Det ersätter inte
`PROJECT_INSTRUCTIONS.md` eller `Project_Memory/Current_Project_State.md`, som fortfarande
gäller för hur arbete ska göras och var projektet står i detalj.

---

## 1. Vad är Project Ascension?

Project Ascension är ett AI-drivet, kooperativt berättar-RPG för 2–6 spelare (testskivan VS-001 stöder även en ensam spelare). Det utspelar sig
i ett nära framtida USA efter att superintelligensen **Aurora** har uppstått.

Kärnidén är att världen lever oavsett spelarna. Människor arbetar, flyttar, blir osams,
åldras och dör. Organisationer, infrastruktur, resurser och rykten förändras även när ingen
spelare tittar. Spelarna är en del av världen, inte dess centrum, och berättelsen växer fram ur
det som händer i simuleringen i stället för ur ett manus.

En AI-spelledare (Game Master) tolkar världen för spelarna. Varje session skrivs in som
permanent historia i världens logg (World Ledger).

## 2. Designpelare

- En levande värld som förändras utan att vänta på spelarna.
- Mänskliga relationer, tillit och svek står i centrum.
- Expertis ger bättre val, inte automatiska svar (nivå 0–5).
- Aurora är mycket intelligent men aldrig allvetande, och hennes motiv är osäkra.
- Spelarna börjar åtskilda och måste hitta varandra.
- Verkliga platser ger geografin, projektet står för vad som händer där.

## 3. Världens epoker (World States)

1. **The Connected World** — dagens uppkopplade samhälle.
2. **The Transition** — Aurora och andra AI-system förändrar samhället, beroendet växer och
   systemen börjar bete sig på sätt människor inte förstår.
3. **The Fractured World** — sammanbrottet; regioner isoleras och lokala samhällen tar över.
4. **The Reconnection** — långsam återuppbyggnad av kontakt och förtroende.

## 4. Hur repot är organiserat

| Mapp | Innehåll | Filer |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Regler för hur alla (människor och AI) arbetar i projektet | 1 |
| `Project_Memory/` | Var projektet står just nu och vad som är nästa steg | 2 |
| `Canon/foundation/` | Vision, designprinciper, beslut, människomodell | 14 |
| `Canon/Systems/` | Spelets system: karaktärer, liv, relationer, samhälle, fraktioner, världssimulering, Living Campaign Engine, Game Master Bible, progression och Auroras kognitiva arkitektur | ~138 |
| `Canon/Universe/` | Världen: tidslinjer, Aurora-arkivet (återfunna dokument), familjer, karaktärer, platser, epoker | ~260 |
| `Canon/Pitch/`, `Canon/Marketing/` | Pitch på svenska och engelska, kärnbudskap | 4 |
| `Development/Validation/` | Spelbar testskiva VS-001 (Republic) och testdata för Aurora | ~12 |
| `Development/Academy/` | Planerad lärokurs (Git, Markdown, Python, speldesign …), kapitlen är ännu tomma | 19 |
| `Tools/Aurora_Validation_Harness/` | Python-verktyg som testar att Aurora-arkitekturen håller informationsgränser | 39 |
| `Project_Management/`, `Project_Brain/` | Äldre status/kunskapsbas och idéer för framtida produkter | 5 |
| `Assets/Music/` | Musikriktning (Suno) | 1 |

### De viktigaste delarna

- **Aurora** (`Canon/Systems/AI/Aurora/`, `Canon/Universe/Aurora/`, `Canon/Universe/Timeline/Aurora/`):
  hur hon tänker, minns, tror, prioriterar och fattar beslut, plus hennes historia från
  bildandet i Bay Area till den offentliga eran. Arkivet *Recovered Records* är dokument som
  spelarna kan hitta i världen.
- **Övergången** (`Canon/Universe/Timeline/Transition/`): en lång kedja av händelser där
  maskiner börjar skydda information och kommunicera på sätt människor inte kan följa.
- **Karaktärer och liv** (`Canon/Systems/Characters/`, `Canon/Systems/Life/`): hur
  människor i världen har behov, mål, kunskap, rutiner och åldras över tid.
- **Familjen Mitchell/Brooks** (`Canon/Universe/Families/`, `Canon/Universe/Characters/`):
  den första fullt utskrivna familjen, med livshistorier från 1990-talet och framåt.
- **Republic, Washington** (`Canon/Universe/Locations/USA/Washington/`): första spelplatsen,
  byggd på den verkliga orten.
- **VS-001 Northern Isolation** (`Development/Validation/Gameplay/VS-001/`): spelarna
  anländer till Republic där något redan har hänt, men ingen vet vad eller hur långt det
  sträcker sig. Fokus är frågorna "vad händer?", "vem kan vi lita på?" och "vad gör vi nu?".
- **The Hunt** (`Canon/Systems/Narrative/Story_Framework/Main_Stories/The_Hunt/`): första
  huvudstoryn. Ett federalt utredarteam undersöker två mord nära Republic som liknar en
  ouppklarad seriemördarutredning från 1990-talets Florida, "The Sunday Man".

## 5. Var projektet står

- **Fas:** städning av grunden och arkitekturen. Implementation skjuts medvetet upp tills
  systemen och deras ansvarsgränser är fastställda.
- **Pågående arbete:** granskning av de tidiga karaktärsfilerna. Nästa planerade steg är att
  bygga om `Canon/Systems/Characters/Autonomy_and_Initiative.md`.
- **Testverktyget:** kärnan i Aurora Validation Harness är byggd och alla 2 253 enhetstester
  går igenom. Nästa steg (HC-8) är att skapa testdatat för FOUND-001 och göra en första
  provkörning.
- **Projektminnet** (`Project_Memory/Current_Project_State.md`) uppdaterades senast
  2026-08-30 och tar ännu inte upp Game Master Bible, The Hunt och VS-001 från september.

## 6. Kända luckor

Följande behöver åtgärdas med rätt innehåll. Städningen 2026-10-23 rörde dem inte, eftersom
texten inte kan återskapas ur repot:

| Fil | Problem |
|---|---|
| `Canon/Universe/Characters/People/Brooks/Daniel_Brooks_1988_2018_Early_Life.md` | Innehåller en exakt kopia av Michael Mitchells livshistoria i stället för Daniels |
| `Canon/Universe/Timeline/Transition/Transition_International_Machine_Autonomy_Divergence.md` | Exakt kopia av `Transition_Cross_Domain_Machine_Anomaly_Period.md` |
| `Canon/Universe/Timeline/Transition/Transition_Selective_Exposure_Utility_Formation.md` | Exakt kopia av `Transition_Content_Oriented_Information_Protection_Emergence.md` |
| `Development/Validation/Aurora/Fixtures/fixture-manifest.json` | Pekar på testfiler under `Fixtures/FOUND-001/` som inte finns än (del av HC-8) |
| `Development/Academy/*.md` | Kapitlen i lärokursen är tomma platshållare |

Om originaltexten finns kvar i gamla ChatGPT-konversationer är det enklast att klistra in den
i rätt fil.

## 7. Läsordning för nya bidragsgivare

1. Den här översikten.
2. `PROJECT_INSTRUCTIONS.md`
3. `Project_Memory/Current_Project_State.md`
4. `Canon/foundation/Vision.md` och `Canon/Pitch/Project_Ascension_Pitch_SV.md`
5. Den Canon och de system som berörs av uppgiften.
