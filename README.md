# Replikationspaket zum GIL-2027-Kurzpaper

Dieses Repository enthält das öffentliche Replikationsmaterial zum Beitrag
`LLM-generierte Bierrezeptentwürfe für kleinere Brauunternehmen: Einfluss der
Promptstruktur und fachliche Bewertung`.

Der veröffentlichte Stand ist mit dem Tag `replication-package-v1.0`
gekennzeichnet.

## Enthaltene Materialien

### `prompts`

- die beiden Versuchsszenarien Pils und Altbier
- der finale Promptkatalog mit Baseline- und Produktionsbriefing-Prompt
- das Hauptlaufmanifest mit den acht exakten Promptinstanzen und der
  Modellkonfiguration

### `outputs/main`

- acht unveränderte, lesbare Modelloutputs
- acht zugehörige Request-Dateien

Die rohen API-Response-JSONs sind nicht enthalten. Sie enthalten zusätzliche
verschlüsselte interne Modellfelder, die für die fachliche Nachprüfung nicht
benötigt werden. Modell-, Token- und Laufangaben sind in `RUN_METADATA.md`
dokumentiert.

### `instrument`

- das professionelle Bewertungsraster
- die den Ratern bereitgestellte Stilreferenz

### `data`

- anonymisierte numerische Bewertungsaggregate
- finaler qualitativer Codierleitfaden
- anonymisierte qualitative Codierungen
- dokumentierte menschliche Stichprobenprüfung der Codierungen

Die Kennungen `E02`, `E03` und `E06` sind ausschließlich anonyme Rater-Aliase.
Die Kennungen `B01` bis `B08` bezeichnen verblindete Rezeptentwürfe.

### `scripts`

- der für die acht Hauptläufe verwendete OpenAI-Runner, angepasst an die
  Verzeichnisstruktur dieses öffentlichen Pakets

## Bewusst nicht enthalten

Das Repository enthält insbesondere keine:

- Arbeits- und Zeitpläne
- Wochenlisten oder Projektretrospektiven
- E-Mail-, WhatsApp- oder sonstigen Kontaktvorlagen
- Klarnamen oder Kontaktdaten von Fachpersonen
- Rekrutierungs- und Kontaktstatus
- ausgefüllten Originalbewertungsmappen
- qualitativen Originalkommentare
- Paperentwürfe, Mitautorenfeedbacks oder internen Reviewstände
- API-Schlüssel, Zahlungsdaten oder Zugangsinformationen
- Quellen-PDFs und Tagungsunterlagen

## Reproduzierbarkeitsgrenzen

- Kommerzielle Sprachmodelle können sich verändern oder später nicht mehr in
  derselben Version verfügbar sein.
- Die Generierung war nicht deterministisch. Zwei unabhängige Läufe je
  Bedingung bilden diese Streuung nur begrenzt ab.
- Die privaten Originalbewertungen werden aus Datenschutzgründen nicht
  veröffentlicht. Die öffentlichen Aggregate enthalten Prüfsummen der
  unveränderten Quelldateien.
- Die menschliche Gegenprüfung der qualitativen Codierung war keine
  unabhängige Doppelcodierung.
- Die fachlichen Bewertungen beziehen sich auf schriftliche Entwürfe.
  Brauversuche, Analytik und Sensorik waren nicht Teil der Studie.

## Nutzung der Dateien

Der Runner kann ohne API-Aufruf geprüft werden:

```powershell
python scripts/openai_main_runner.py dry-run
python scripts/openai_main_runner.py status
```

Ein erneuter API-Lauf erzeugt wegen der Nichtdeterministik voraussichtlich
nicht dieselben Texte. Für die Nachprüfung der berichteten Studie sind daher
die eingefrorenen Outputs maßgeblich.
