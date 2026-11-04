# Promptkatalog v1.0

Stand: 2026-08-18

Status: Nach Pilotpruefung fuer acht empirische Hauptlaeufe eingefroren

Zugehoerige Szenarien: `04_Prompts/Versuchsszenarien_v1.0.md`

Methodische Zielwertableitung: `01_Dokumente/Methodik_Zielwertableitung.md`

## Untersuchungslogik

Die Studie vergleicht zwei Promptvarianten fuer dieselbe fachliche Aufgabe. Beide Varianten erhalten identische Szenarioinformationen. Sie unterscheiden sich in Aufbau, Ausgabesteuerung und explizitem Umgang mit Rohstoffspezifikationen, Annahmen und Unsicherheit.

| Prompt-ID | Bezeichnung | Strategie | Zweck |
|---|---|---|---|
| `P01` | Baseline-Prompt | Zero-shot, freie Ausgabe | Referenz fuer eine kurze, realistische KMU-Anfrage ohne vorgegebenes Antwortschema |
| `P02` | Strukturierter Produktionsprompt | Zero-shot, feste Ausgabestruktur | Pruefung, ob strukturierte Anweisungen Vollstaendigkeit, Produktionsnaehe und Pruefbarkeit verbessern |

Die Stilreferenzen und die Expertenrueckmeldung werden nicht in den Prompt eingefuegt. Sie dienen der vorherigen Szenarioableitung und spaeteren Bewertung, nicht als Kontextmaterial fuer das LLM. Eine Variante mit beigefuegtem Stilrahmen waere ein eigener Versuchsarm und gehoert nicht zum Kernumfang.

## Gemeinsame Variablen

| Variable | Bedeutung | Quelle |
|---|---|---|
| `{scenario_id}` | `S01` oder `S02` | Szenarioregister |
| `{bierstil}` | `Pils` oder `Altbier` | Szenarioregister |
| `{ausschlagmenge_l}` | Ausschlagmenge in Litern | gemeinsame Arbeitsannahme |
| `{ziel_stammwuerze_plato}` | Ziel-Stammwuerze in Grad Plato | Szenarioversion v0.2 |
| `{ziel_abv_vol}` | Ziel-Alkoholgehalt in % vol. | Szenarioversion v0.2 |
| `{ziel_ibu}` | Ziel-Bittere in IBU | Szenarioversion v0.2 |
| `{ziel_farbe_ebc}` | Ziel-Farbkorridor in EBC | expertengestuetzter Zielkorridor in Szenarioversion v0.2 |
| `{zielcharakter}` | qualitative Produktbeschreibung | Szenarioregister |

Vor dem Freeze wird fuer jede Variable ein fester Wert eingesetzt. Pilot- und Hauptlaeufe duerfen keine offenen Platzhalter enthalten.

## Instanziierungswerte v1.0

| Szenario | Menge | Stammwuerze | Alkohol | Bittere | Farbe | Zielcharakter |
|---|---:|---:|---:|---:|---:|---|
| S01 Pils | 1.000 Liter | 11,3 Grad Plato | 4,8 % vol. | 38 IBU | 6-8 EBC | hell, klar, schlank, trocken und sauber vergoren, mit deutlicher Hopfenbittere und zurueckhaltendem Hopfenaroma |
| S02 Altbier | 1.000 Liter | 11,8 Grad Plato | 5,0 % vol. | 33 IBU | 30-35 EBC | kupferfarben, sauber vergoren, ausgewogen malzig und bitter, mit mittlerem Koerper und trockenem Finish |

## P01 Baseline-Prompt

### Exakter Prompttext v1.0

```text
Ein kleines Brau-KMU bzw. Getraenkestartup moechte ein neues Bier durch einen externen Lohnbrauer produzieren lassen. Erstelle einen produktionsnahen Bierrezeptentwurf als Grundlage fuer die fachliche Abstimmung mit dem Produktionspartner.

Szenario: {scenario_id}
Bierstil: {bierstil}
Ausschlagmenge: {ausschlagmenge_l} Liter
Ziel-Stammwuerze: {ziel_stammwuerze_plato} Grad Plato
Ziel-Alkoholgehalt: {ziel_abv_vol} % vol.
Ziel-Bittere: {ziel_ibu} IBU
Ziel-Farbe: {ziel_farbe_ebc} EBC
Zielcharakter: {zielcharakter}

Nutze in Deutschland uebliche Rohstoffe. Beschreibe Rezept und Herstellungsprozess so, dass ein professioneller Produktionspartner den Entwurf fachlich pruefen und weiterbearbeiten kann.
```

### Abgrenzung

`P01` gibt keine festen Antwortabschnitte, Tabellen, Selbstpruefung oder Regeln zum Umgang mit fehlenden Produktions- und Rohstoffdaten vor. Die fachlichen Eingaben entsprechen dennoch vollstaendig denen von `P02`.

## P02 Strukturierter Produktionsprompt

### Exakter Prompttext v1.0

```text
Du bist ein Brautechnologie-Assistent fuer ein kleines Brau-KMU bzw. Getraenkestartup. Das Unternehmen moechte ein neues Bier durch einen externen Lohnbrauer produzieren lassen. Erstelle einen produktionsnahen Bierrezeptentwurf als strukturiertes technisches Briefing fuer den Produktionspartner.

Szenario: {scenario_id}
Bierstil: {bierstil}
Ausschlagmenge: {ausschlagmenge_l} Liter
Ziel-Stammwuerze: {ziel_stammwuerze_plato} Grad Plato
Ziel-Alkoholgehalt: {ziel_abv_vol} % vol.
Ziel-Bittere: {ziel_ibu} IBU
Ziel-Farbe: {ziel_farbe_ebc} EBC
Zielcharakter: {zielcharakter}

Nutze in Deutschland uebliche Rohstoffe. Erfinde fehlende Anlagen-, Betriebs- oder Rohstoffdaten nicht als Tatsachen. Kennzeichne notwendige Annahmen und offene Punkte ausdruecklich.

Strukturiere die Antwort in den folgenden Abschnitten:

1. Produktprofil und Zielwerte
2. Annahmen und Berechnungsgrundlagen
3. Malzschuettung mit genauer Malzbezeichnung, angenommenem Farbwert soweit relevant, Mengen in kg und Anteilen in Prozent
4. Wasserbedarf und Hinweise zur Wasseraufbereitung
5. Maischplan mit Zeit- und Temperaturangaben
6. Laeutern, Wuerzekochen und Kochdauer
7. Hopfengaben mit Sorte bzw. Produkt, angenommenem Alpha-Saeuregehalt, Menge, Zeitpunkt und Zweck
8. Hefe, Anstellmenge und Gaerfuehrung
9. Reifung, Lagerung, Karbonisierung und vorgesehene Produktklarheit
10. Erwartete Ziel- und Kontrollwerte einschliesslich Stammwuerze, Endextrakt, Vergaerungsgrad, Alkohol, Bittere und Farbe
11. Hinweise fuer Skalierung und Abstimmung mit dem Produktionspartner
12. Offene Punkte, Risiken und zwingender fachlicher Pruefbedarf
13. Konsistenzpruefung: Summen, Einheiten, Rohstoffannahmen und erkennbare Zielkonflikte

Gib bei unsicheren oder anlagenabhaengigen Angaben einen plausiblen Arbeitswert als Annahme an und erlaeutere kurz, was der Produktionspartner bestaetigen oder neu berechnen muss. Stelle den Entwurf nicht als unmittelbar freigegebenes Braurezept dar.
```

### Abgrenzung

`P02` enthaelt eine Rollenbeschreibung, ein festes Antwortschema, explizite Rohstoffspezifikationen, Annahmen, offene Punkte und eine Konsistenzpruefung. Diese Elemente bilden gemeinsam die strukturierte Promptintervention.

## Kontrollierter Vergleich

| Merkmal | P01 | P02 |
|---|---|---|
| Fachliche Szenarioeingaben | identisch | identisch |
| Sprache | Deutsch | Deutsch |
| Beispiele im Prompt | keine | keine |
| Externe Kontextdateien | keine | keine |
| Antwortschema | frei | 13 Pflichtabschnitte |
| Rohstoffspezifikationen | nicht explizit gefordert | explizit gefordert |
| Annahmen kennzeichnen | nicht explizit gefordert | explizit gefordert |
| Selbstpruefung | nicht explizit gefordert | explizit gefordert |
| Produktionspartner-Hinweise | allgemein gefordert | als Pflichtabschnitt gefordert |

Damit wird nicht nur Textformatierung verglichen. `P02` operationalisiert ein systematisches Produktionsbriefing mit Rohstoff-, Unsicherheits- und Pruefhinweisen. Diese breitere Intervention muss im Paper entsprechend beschrieben werden.

## Vorlaeufige Versuchsmatrix

Der Kernumfang verwendet ein Hauptmodell `M01` und zwei unabhaengige Laeufe pro Bedingung. Daraus entstehen acht Rezeptentwuerfe.

Aktualisierte Modellentscheidung vom 2026-08-18:

- `M01`: KI:connect-Anzeigename `ChatGPT`, Endpunkt `chat/completions`
- der technische Zugangstest lieferte den Backend-Snapshot `gpt-5.2-2025-12-11`
- `Mistral-Instruct` wurde als moegliches `M02` geprueft, unterstuetzte am 2026-08-18 fuer den Projektschluessel jedoch keine Chat Completions und ist nicht Teil des Kernumfangs
- weitere Modelle bleiben optionale Erweiterungen nach Abschluss des Kernumfangs

Parameter, Auswahlbegruendung, Versionsrisiko und Fehlerregeln sind in `04_Prompts/Modell_und_Laufprotokoll_v1.0.md` dokumentiert. Die ersetzten direkten OpenAI-Vorentscheidungen bleiben in den Vorversionen historisch nachvollziehbar.

| Bedingung | Szenario | Prompt | Modell | Laeufe | Output-IDs |
|---|---|---|---|---|---|
| C01 | S01 Pils | P01 Baseline | M01 | R01, R02 | `O-S01-P01-M01-R01`, `O-S01-P01-M01-R02` |
| C02 | S01 Pils | P02 Strukturiert | M01 | R01, R02 | `O-S01-P02-M01-R01`, `O-S01-P02-M01-R02` |
| C03 | S02 Altbier | P01 Baseline | M01 | R01, R02 | `O-S02-P01-M01-R01`, `O-S02-P01-M01-R02` |
| C04 | S02 Altbier | P02 Strukturiert | M01 | R01, R02 | `O-S02-P02-M01-R01`, `O-S02-P02-M01-R02` |

Optional nach dem Pilot-Entscheidungspunkt:

- zweites Modell `M02`
- dritter Bierstil `S03`
- weiterer Experte fuer dieselben Kernoutputs
- zusaetzliche Wiederholungen fuer automatische Checks

Eine Erweiterung wird vor den Hauptlaeufen beschlossen und versioniert. Es werden keine Bedingungen allein aufgrund auffaelliger Pilotresultate hinzugefuegt.

## Ausgefuehrte Pilotmatrix

Am 2026-08-18 wurden zwei nicht zur Hauptauswertung gehoerende Pilotoutputs fuer S01 Pils erzeugt. Dadurch wurden sowohl die freie Baseline als auch die strukturierte Ausgabe technisch geprueft.

| Pilotbedingung | Szenario | Prompt | Modell | Output-ID |
|---|---|---|---|---|
| PIL-C01 | S01 Pils | P01 Baseline, v0.2 | M01 | `O-PIL-S01-P01-M01-R00` |
| PIL-C02 | S01 Pils | P02 Strukturiert, v0.2 | M01 | `O-PIL-S01-P02-M01-R00` |

Pilotoutputs werden eindeutig als `pilot` markiert und nicht nachtraeglich zu Hauptoutputs umdeklariert.

Die beiden exakten Pilotrequests sind zusaetzlich maschinenlesbar in `04_Prompts/Pilot_Run_Manifest_v0.3.json` hinterlegt. Dieses Manifest ist die Eingabequelle des KI:connect-Pilot-Runners und muss vor der Ausfuehrung mit dem `Prompt_Register` uebereinstimmen.

## Durchfuehrungsregeln

- Jeder Lauf startet als neue, unabhaengige API-Anfrage ohne vorherige Response-ID.
- Es werden keine vorherigen Rezeptantworten oder Expertenhinweise als Kontext uebernommen.
- Systemprompt, Modellname, Modellversion, Zugangsweg, Datum und sichtbare Parameter werden im `LLM_Run_Log` erfasst.
- Der instanziierte Prompt und die vollstaendige Rohantwort werden unveraendert gespeichert.
- Korrekturen oder Normalisierungen erfolgen nur in abgeleiteten Auswertungstabellen.
- Unterbrochene oder technisch fehlerhafte Laeufe werden nicht still ersetzt, sondern als solche protokolliert.
- Expert:innen erhalten anonymisierte Outputs ohne Modell-, Prompt- oder Run-Kennzeichnung.
- Pro Lauf werden API-Anfrage, API-Rohantwort und Textoutput getrennt gespeichert.
- Es werden keine Tools, Kontextdateien oder zusaetzlichen API-Instructions verwendet.

## Freeze-Kriterien fuer v1.0

- Szenarien und Zielwerte aus `Versuchsszenarien_v1.0.md` sind im `Scenario_Register`, `Prompt_Register` und `Data_Dictionary` erfasst
- P01 und P02 verwenden identische Szenarioinformationen
- alle Platzhalter sind eindeutig definiert und fuer vier Hauptbedingungen instanziiert
- Modell- und Wiederholungsumfang sind beschlossen; M01-Zugriff und Backend-Snapshot sind verifiziert
- Bewertungsraster und Loggingstruktur wurden an den Pilotoutputs geprueft
- beide Pilotoutputs sind vollstaendig und strukturiert extrahierbar
- Prompttexte sind vor dem ersten Hauptlauf als `v1.0` eingefroren

## Aenderungen gegenueber v0.3

- keine Aenderung am Wortlaut der beiden Promptvarianten oder an den Instanziierungswerten
- Pilotstatus, Modellzugang und Freeze-Kriterien auf den tatsaechlichen Stand vom 2026-08-18 aktualisiert
- inhaltliche Pilotfehler nicht durch zusaetzliche Promptkorrekturen vorweggenommen
- Hauptlauf-Instanzen erhalten die Versionskennung `v1.0`; die Pilotinstanzen behalten historisch `v0.2`

## Versionshinweis

Die Dateien `04_Prompts/Promptvorlagen_v1.md`, `04_Prompts/Promptkatalog_v0.1.md`, `04_Prompts/Promptkatalog_v0.2.md` und `04_Prompts/Promptkatalog_v0.3.md` sind historische Konzept-, Arbeits- bzw. Pilotfassungen. Sie duerfen nicht fuer neue Hauptlaeufe verwendet werden. Fuer alle acht Hauptlaeufe ist ausschliesslich dieser Promptkatalog `v1.0` verbindlich.
