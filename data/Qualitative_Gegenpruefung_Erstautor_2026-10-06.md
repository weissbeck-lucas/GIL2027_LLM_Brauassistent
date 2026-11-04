# Menschliche Gegenpruefung der qualitativen Codierung

Stand: 2026-10-06

Pruefende Person: Erstautor

Status: abgeschlossen

## Vorgehen

Geprueft werden die anonymisierten Paraphrasen, Inhaltscodes und Funktionen
gegen die privaten Originalfelder von E03 und E06. Die Originalmappen werden
nicht veraendert. Das Pruefpaket v0.1 und die source-auditierte Codierung v0.2
bleiben als historische Ausgangsstaende erhalten. Die Entscheidungen wurden
nach Abschluss der gesamten Auswahl in die finale Codierungsfassung v1.0
uebernommen.

## Entscheidungen

| ID | Original eingesehen | Paraphrase | Codes | Funktion | Gesamtergebnis | Begruendung oder Aenderung |
|---|---|---|---|---|---|---|
| Q-E03-001 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E03-004 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E03-010 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E03-013 | ja | OK | OK | OK | OK | Die erste durch Semikolon getrennte Sinneinheit beantwortet den Teil der Doppelfrage zur sinnvollen LLM-Unterstuetzung. |
| Q-E03-014 | ja | AENDERN | AENDERN | AENDERN | AENDERN | Die zweite durch Semikolon getrennte Sinneinheit beantwortet den Teil der Doppelfrage zu zwingend erforderlicher Brauexpertise oder konkreten Betriebsdaten. Neue Paraphrase: `Zeitangaben werden als Bereich eingeordnet, der Brauexpertise oder konkrete Betriebsdaten erfordert.` Neuer Hauptcode `PR`, Nebencode `AN`, Funktion `BEDINGUNG`. |
| Q-E06-002 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E06-006 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E06-010 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E06-012 | ja | OK | OK | OK | OK | keine Aenderung; weitere Sinneinheit desselben Originalfelds separat als Q-E06-013 erfasst |
| Q-E06-021 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E06-027 | ja | OK | OK | OK | OK | keine Aenderung |
| Q-E06-029 | ja | OK | OK | OK | OK | keine Aenderung; weitere Sinneinheiten desselben Originalfelds separat als Q-E06-028 und Q-E06-030 bis Q-E06-032 erfasst |
| Q-E06-039 | ja | OK | OK | OK | OK | keine Aenderung; weitere Sinneinheit desselben Originalfelds separat als Q-E06-040 erfasst |
| Q-E06-044 | ja | OK | OK | OK | OK | keine Aenderung; weitere Sinneinheiten desselben Originalfelds separat als Q-E06-043 und Q-E06-045 erfasst |
| Q-E06-047 | ja | OK | OK | OK | OK | keine Aenderung |

## Zusaetzliche Vollstaendigkeitspruefung von Mehrfachfeldern

| Originalfeld | Getrennt erfasste Sinneinheiten | Ergebnis |
|---|---|---|
| E06, `Kommentare!C7` | Q-E06-012 und Q-E06-013 | Anlagenanforderung sowie Kritik an Karamellmalz und Stiltypizitaet separat erfasst |
| E06, `Kommentare!F11` | Q-E06-028 bis Q-E06-032 | Hopfung und Karamellmalz, unklare Carafa-Zugabe, positive Gesamtbewertung, Stammwuerze-Konsistenz sowie Temperaturanstieg und Diacetylrast separat erfasst |
| E06, `Abschluss!C5` | Q-E06-039 und Q-E06-040 | Anlagenumsetzbarkeit und Stiltypizitaet als getrennte Risiken erfasst |
| E06, `Abschluss!C7` | Q-E06-043 bis Q-E06-045 | theoretische LLM-Unterstuetzung, sensorische Grenze und fehlende Kenntnis der Anlagengrenzen separat erfasst |

## Ergebnis

- regulaer ausgewaehlte Zeilen geprueft: 14 von 14
- zusaetzlich gepruefte angrenzende Sinneinheiten: 1
- regulaere Zeilen ohne Aenderungsbedarf: 14
- zusaetzliche Zeilen mit Aenderungsbedarf: 1

- Originalfelder eingesehen: ja
- Gesamtzahl gepruefter regulaerer Zeilen: 14
- davon ohne Aenderungsbedarf: 14
- zusaetzlich gepruefte Sinneinheit: Q-E03-014
- Aenderung erforderlich: ja, nur bei Q-E03-014
- Datum des Abschlusses: 2026-10-06

Paraphrasen und Codierungen waren insgesamt sinnvoll und nachvollziehbar.
Einzig Q-E03-014 war zu korrigieren, da dort eine Doppelfrage in einem
Antwortfeld gestellt wurde und das Semikolon bei der urspruenglichen
Codierung nicht als Trennung der Antworten auf beide Teilfragen aufgefasst
worden war.

Die Gegenpruefung ist eine menschliche Qualitaetssicherung der
KI-unterstuetzt vorbereiteten Codierung. Sie ist keine unabhaengige
Doppelcodierung zweier menschlicher Codierender; ein Uebereinstimmungsmass
wird deshalb nicht berechnet.
