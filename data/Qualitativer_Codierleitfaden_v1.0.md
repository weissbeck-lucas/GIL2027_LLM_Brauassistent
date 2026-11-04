# Qualitativer Codierleitfaden v1.0

Stand: 2026-09-23

Status: vor der systematischen qualitativen Codierung festgelegt

## Zweck und methodische Einordnung

Der Leitfaden regelt die qualitative Auswertung der bereits im professionellen
Bewertungsinstrument erhobenen Freitextantworten. Die Kategorien sind
ueberwiegend deduktiv aus Forschungsfrage, Bewertungsraster und den vorab
festgelegten Freitextfragen abgeleitet. Der Leitfaden wurde nach Eingang der
ersten drei Ruecklaeufe, aber vor einer systematischen Vollcodierung erstellt.
Er ist daher keine Praeregistrierung.

Die qualitative Auswertung ergaenzt die kriterienspezifischen Ratings. Sie
dient vor allem dazu, wiederkehrende fachliche Staerken, Fehler,
Informationsluecken, notwendige Anpassungen und Risiken nachvollziehbar zu
beschreiben. Sie wird nicht verwendet, um fehlende strukturierte Angaben aus
Freitexten zu rekonstruieren.

## Material und Einschluss

Primaer codiert werden professionell erstellte Freitexte, wenn

- der gesamte Ruecklauf formal eingeschlossen ist,
- die fachliche Bewertung einzeln erfolgte,
- die Formulierungen nicht mit generativer KI erstellt wurden und
- die jeweilige Aussage eindeutig einem Feld oder Entwurf zugeordnet ist.

Nach dem derzeitigen Pruefstand bilden `E03` und `E06` das primaere qualitative
Material. `E02` gab an, eigene fachliche Stichpunkte mit generativer KI
sprachlich ausformuliert zu haben. Diese Texte werden nur getrennt als
Sensitivitaetsmaterial codiert, nicht woertlich zitiert und nicht mit der
primaeren KI-frei formulierten Textbasis zusammengezaehlt.

Weitere professionelle Ruecklaeufe werden nach denselben Regeln einbezogen.
Hobbyruecklaeufe bleiben eine getrennte explorative Datenquelle und werden
nicht mit professionellen Aussagen aggregiert.

## Auswertungseinheit

Codiert wird die kleinste inhaltlich eigenstaendige Sinneinheit. Eine Antwort
kann mehrere Sinneinheiten und eine Sinneinheit mehrere inhaltliche Codes
enthalten. Pro Sinneinheit wird ein Hauptcode vergeben; klar mitgemeinte
weitere Aspekte koennen als Nebencodes erfasst werden.

Die Codiereinheit wird zusammen mit folgenden Merkmalen dokumentiert:

| Feld | Inhalt |
|---|---|
| `reviewer_alias` | anonymisierter Alias |
| `blind_output_id` | `B01` bis `B08` oder `GLOBAL` fuer Abschlussfragen |
| `source_field` | Ausgangsfrage beziehungsweise Kommentarfeld |
| `paraphrase` | knappe anonymisierte Inhaltswiedergabe |
| `main_code` | primaerer Inhaltscode |
| `secondary_codes` | optionale weitere Inhaltscodes |
| `function` | `STAERKE`, `PROBLEM`, `FEHLT`, `KORREKTUR`, `RISIKO`, `BEDINGUNG` oder `NEUTRAL` |
| `provenance` | `human_unassisted` oder getrennt `human_notes_ai_worded` |
| `memo` | kurze Codierentscheidung bei Grenzfaellen |

Qualitative Rohtexte verbleiben in der privaten Ablage. In versionierten
Auswertungsdateien werden nur anonymisierte Paraphrasen, Codes und Aggregate
gefuehrt.

## Inhaltliche Codes

| Code | Kategorie | Einschliessen | Abgrenzung |
|---|---|---|---|
| `ZK` | Zielwerte, Mengen und Konsistenz | Mengenrelationen, Summen, Einheiten, Ausbeute, Stammwuerze, Alkohol, IBU, EBC und rechnerische Widersprueche | Prozesswahl nur dann mitcodieren, wenn sie fuer den Zielwertbezug ausdruecklich relevant ist |
| `RO` | Rohstoffe | Malz, Hopfen, Hefe, Wasser, Rohstoffspezifikation, Verfuegbarkeit und Austauschbarkeit | Prozessparameter ohne Rohstoffbezug unter `PR` |
| `PR` | Brauprozess | Maischen, Laeutern, Kochen, Hopfengaben, Kuehlung, Gaerung, Reifung, Karbonisierung und Abfuellung | konkrete Anlagenrestriktionen zusaetzlich oder vorrangig unter `AN` |
| `ST` | Stil und Sensorik | Stiltypizitaet, Farbe, Bittereindruck, Aroma, Geschmack, Koerper und erwartete sensorische Wirkung | rein numerischer Zielwertbezug unter `ZK`; beide Codes sind gemeinsam moeglich |
| `AN` | Anlage und Betrieb | Sudhausausbeute, Tank- und Anlagenparameter, Verluste, Wasseraufbereitung, Hygiene, Qualitaetssicherung, Haltbarkeit und betriebliche Randbedingungen | allgemeine Prozessangaben unter `PR` |
| `PS` | Pilotierung und Skalierung | Kleinsud, Massstabsuebertragung, nichtlineare Skalierung, Hopfenausnutzung, Waerme- und Volumenverluste sowie pruefbeduerftige Scale-up-Annahmen | allgemeine Anlagenanpassung ohne Massstabsbezug unter `AN` |
| `BK` | Briefing und Kommunikation | Klarheit, Vollstaendigkeit, Annahmen, offene Entscheidungen, missverstaendliche Formulierungen und Rueckfragen an Auftraggeber oder Produktionspartner | fachliche Inhaltsluecke zusaetzlich mit dem passenden technischen Code versehen |
| `NU` | Nutzwert und Arbeitsentlastung | hilfreiche Struktur, brauchbarer Ausgangspunkt, Zeitersparnis, Vergleichs- oder Ideengewinn | keine pauschale positive Bewertung ableiten, wenn nur ein Teilaspekt genannt ist |
| `RI` | Risiko ungepruefter Nutzung | Scheingenauigkeit, Uebernahme fachlicher Fehler, fehlende Betriebsdaten, falsche Sicherheit, Qualitaets- oder Produktionsrisiken | konkrete fachliche Ursache nach Moeglichkeit zusaetzlich technisch codieren |
| `SO` | Sonstiger relevanter Aspekt | inhaltlich relevante Aussage, die in keine Kategorie passt | nur mit Memo verwenden; wiederkehrende `SO`-Faelle koennen eine versionierte Unterkategorie begruenden |

## Codierregeln

1. Es werden nur ausdruecklich geaeusserte Inhalte codiert. Ein niedriger oder
   hoher Zahlenwert allein wird nicht in eine qualitative Aussage uebersetzt.
2. `Nicht beurteilbar`, Unsicherheit oder der Wunsch nach einem Probesud ist
   keine negative Bewertung. Solche Aussagen erhalten die Funktion
   `BEDINGUNG` und den passenden Inhaltscode, haeufig `PS`, `ST` oder `AN`.
3. Derselbe Wortlaut, der fuer mehrere Entwuerfe wiederholt wurde, wird auf
   Outputebene dokumentiert, aber bei Aussagen zu wiederkehrenden Themen nicht
   als acht unabhaengige Expertenstimmen dargestellt.
4. Eine Aussage kann Haupt- und Nebencodes erhalten. Doppelcodierungen dienen
   der inhaltlichen Abbildung und werden nicht zu einem Gesamtscore addiert.
5. Fehlende Antworten werden als fehlend dokumentiert und nicht als
   Abwesenheit eines Problems interpretiert.
6. `E02` wird wegen der KI-gestuetzten Ausformulierung nur in einer getrennten
   Sensitivitaetsdarstellung verwendet. Inhaltliche Uebereinstimmungen mit der
   Primaerbasis koennen benannt, aber nicht als unabhaengige KI-freie
   Formulierung ausgegeben werden.
7. Woertliche Zitate werden nur genutzt, wenn eine entsprechende Freigabe
   vorliegt. Fuer `E03` liegt keine Zitierfreigabe vor; dort sind ausschliesslich
   Paraphrasen zulaessig.
8. Neue Unterkategorien duerfen nach dem Datenschluss induktiv ergaenzt werden,
   wenn mehrere Sinneinheiten sonst nur unter `SO` fallen. Anlass, Definition
   und betroffene bereits codierte Einheiten werden in einem Aenderungsmemo
   dokumentiert; die neun deduktiven Hauptkategorien bleiben bestehen.

## Zusammenfassung und Bericht

Die Ergebnisdarstellung bleibt deskriptiv. Fuer jeden Hauptcode werden
mindestens ausgewiesen:

- Zahl der professionell Bewertenden, die das Thema nennen,
- Zahl und Blind-IDs der betroffenen Entwuerfe,
- Funktion beziehungsweise Richtung der Aussagen,
- voneinander abweichende oder widersprechende Einschaetzungen und
- ein Hinweis, wenn ein Muster nur auf einer Person beruht.

Rezeptnennungen, Sinneinheiten oder Kommentare werden nicht als unabhaengige
Expertenfaelle behandelt. Vergleiche zwischen Promptvarianten oder Bierstilen
bleiben explorativ und werden nur berichtet, wenn das Muster innerhalb von
Personen nachvollziehbar ist. Bei sehr kleinen Fallzahlen stehen inhaltliche
Kontraste und Fallbeispiele vor Haeufigkeitsranglisten.

## Qualitaetssicherung

1. Nach dem Datenschluss werden zunaechst alle eingeschlossenen Texte in
   Sinneinheiten segmentiert.
2. Anschliessend wird ein gemischtes Teilmaterial aus beiden Bierstilen und
   Promptbedingungen codiert und auf Unklarheiten im Leitfaden geprueft.
3. Unklare Entscheidungen werden in Memos festgehalten. Aenderungen am
   Leitfaden erhalten eine neue Version und werden auf das gesamte Material
   rueckwirkend angewendet.
4. Mindestens eine zweite Person prueft eine Auswahl der Codierungen oder,
   falls das organisatorisch nicht moeglich ist, die Codezusammenfassungen und
   abweichenden Faelle. Das tatsaechliche Vorgehen wird im Paper berichtet.
5. Primaeranalyse und E02-Sensitivitaetsanalyse bleiben in allen Tabellen und
   Texten sichtbar getrennt.
