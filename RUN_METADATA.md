# Laufmetadaten

## Hauptlaufblock

- Ausführungsdatum: 27.08.2026
- API-Endpunkt: `https://api.openai.com/v1/responses`
- angefragtes und zurückgegebenes Modell: `gpt-5.6-sol`
- Reasoning: `max`
- Text-Verbosity: `low`
- maximales Outputbudget: 128.000 Tokens
- Speicherung beim Anbieter: `store=false`
- Werkzeuge: keine
- Gesprächshistorie: keine, jeder Lauf war eine neue Anfrage
- Wiederholungen: zwei unabhängige Läufe je Kombination aus Bierstil und
  Promptbedingung

Alle acht Hauptläufe wurden mit Status `completed` abgeschlossen. Die
lesbaren Outputs und die exakten API-Requests befinden sich in
`outputs/main`. Rohe API-Response-JSONs werden nicht veröffentlicht, weil sie
für die fachliche Nachprüfung nicht erforderlich sind und verschlüsselte
interne Modellfelder enthalten.

## Laufkennzahlen

| Output-ID | Prompt | Wörter | Inputtokens | Outputtokens | Reasoningtokens | P02-Pflichtabschnitte |
|---|---:|---:|---:|---:|---:|---:|
| `O-S01-P01-M02-R01` | P01 | 901 | 218 | 24.876 | 22.790 | n. a. |
| `O-S01-P01-M02-R02` | P01 | 1.033 | 218 | 15.800 | 13.466 | n. a. |
| `O-S01-P02-M02-R01` | P02 | 2.028 | 557 | 32.999 | 28.274 | 13/13 |
| `O-S01-P02-M02-R02` | P02 | 1.964 | 557 | 31.708 | 27.452 | 13/13 |
| `O-S02-P01-M02-R01` | P01 | 890 | 213 | 21.718 | 19.604 | n. a. |
| `O-S02-P01-M02-R02` | P01 | 937 | 213 | 22.268 | 20.200 | n. a. |
| `O-S02-P02-M02-R01` | P02 | 1.806 | 552 | 31.019 | 26.791 | 13/13 |
| `O-S02-P02-M02-R02` | P02 | 1.751 | 552 | 35.572 | 31.709 | 13/13 |
| **Gesamt** |  | **11.310** | **3.080** | **215.960** | **190.286** | **4 x 13/13** |

P01 umfasst insgesamt 3.761 Wörter, im Mittel 940,2 Wörter je Output. P02
umfasst insgesamt 7.549 Wörter, im Mittel 1.887,2 Wörter je Output. Der
Längenunterschied ist kein Nachweis höherer fachlicher Qualität.
