# Bewertungsraster fuer fachlich Bewertende v1.2

Stand: 2026-08-26

Status: Vor dem ersten Hauptlauf mit Freeze `v1.2` methodisch eingefroren; professionelles Vollinstrument mit gemeinsamem rezepttechnischem Kern fuer eine gegebenenfalls spaeter bestaetigte Hobbyvergleichsgruppe

## Zweck und Bewertungsgegenstand

Das Raster dient der anonymisierten fachlichen Bewertung von LLM-generierten Bierrezeptentwuerfen. Bewertet wird, ob ein Entwurf als vorpruefbare Grundlage fuer ein technisches Briefing an einen Lohnbrauer oder Produktionspartner geeignet ist.

Zusaetzlich wird die erwartete Pilotierbarkeit erfasst: Eignet sich der Textentwurf als Grundlage fuer einen deutlich kleineren Versuchssud, mit dem Rezeptidee, Zielwerte und erwarteter Charakter vor einem Scale-up geprueft werden koennen? Diese Texteinschaetzung ist kein Nachweis, dass ein tatsaechlicher Kleinsud funktioniert oder sensorisch ueberzeugt.

Nicht bewertet wird, ob das Rezept ohne weitere betriebliche Pruefung unmittelbar gebraut oder kommerziell freigegeben werden kann.

Geplanter Umfang:

- acht anonymisierte Rezeptentwuerfe im Kernumfang
- fuer Baseline-Entwuerfe etwa 6-8 Minuten und fuer strukturierte Entwuerfe etwa 10-12 Minuten als vorsichtige Planungsannahme nach den Low-Verbosity-Piloten
- insgesamt etwa 70-90 Minuten pro professionell bewertender Person einschliesslich Pilotierbarkeitsfrage und Abschlussfragen; Bearbeitung in zwei oder mehreren Sitzungen ist zulaessig

Die Zeitangaben sind Planungswerte und keine gemessenen Bearbeitungszeiten. Grundlage sind 829 Woerter im Low-Verbosity-P01-Piloten und 1.690 Woerter bei 13 Pflichtabschnitten im Low-Verbosity-P02-Piloten.

## Anonymisierung und Verblindung

- Expert:innen werden nur als `E01`, `E02` usw. gefuehrt.
- Die Entwuerfe erhalten neutrale Bewertungs-IDs wie `B01` bis `B08`.
- Bierstil und Zielwerte werden angezeigt, damit Stiltreue und Zielerreichung bewertet werden koennen.
- Modell, Promptvariante, Run-ID und Erzeugungsreihenfolge werden nicht angezeigt.
- Die Reihenfolge der Entwuerfe wird vor Versand zufaellig festgelegt und fuer alle Experten dokumentiert.
- Eine vollstaendige Verblindung der Promptvariante ist nicht garantiert, da eine stark strukturierte Ausgabe erkennbar sein kann. Die Experten werden jedoch nicht ueber die Zuordnung informiert.

## Metadaten je Bewertung

Die anonymisierten beruflichen Perspektiven werden getrennt in `06_Expertenbewertung/Expertenprofile_Anonymisiert.md` gefuehrt und nicht bei jedem einzelnen Rating wiederholt.

| Feld | Beschreibung |
|---|---|
| `expert_alias` | anonymisierter Expertenalias |
| `blind_output_id` | neutrale Bewertungs-ID |
| `beer_style` | Pils oder Altbier |
| `rating_date` | Datum der Bewertung |
| `rating_duration_optional` | freiwillige ungefaehre Dauer der gesamten Bewertung, nicht je Entwurf |

## Allgemeine Skalenregel

Alle Bewertungskriterien verwenden eine Skala von 1 bis 5. Ein hoeherer Wert bedeutet immer eine positivere Bewertung.

- `1` = sehr schwach bzw. nicht erfuellt
- `2` = zwischen den Beschreibungen fuer 1 und 3
- `3` = teilweise erfuellt
- `4` = zwischen den Beschreibungen fuer 3 und 5
- `5` = sehr gut erfuellt

Die Anker fuer 1, 3 und 5 sind kriterienspezifisch definiert.

Zusaetzlich steht fuer jedes einzelne Kriterium `NB` = `nicht beurteilbar` zur Verfuegung. `NB` ist keine schwache Bewertung und wird nicht in Median- oder Verteilungsberechnungen als Zahlenwert einbezogen. Wenn `NB` fuer ein fachlich zentrales Kriterium verwendet wird, soll der Grund kurz im Kommentarfeld erkennbar sein.

## Bewertungskriterien und Anker

| Kriterium | 1 | 3 | 5 |
|---|---|---|---|
| KMU-Fit | Der Entwurf bietet kaum verwertbare Unterstuetzung und erzeugt eher zusaetzlichen Klaerungsaufwand. | Einzelne Teile sind hilfreich, fuer eine praktische Nutzung ist aber deutliche Nacharbeit erforderlich. | Der Entwurf strukturiert die Aufgabe klar und bietet einem Brau-KMU einen deutlichen praktischen Ausgangsnutzen. |
| Produktionsnaehe | Zentrale Produktionsangaben fehlen oder sind so unklar, dass ein Produktionspartner nicht sinnvoll weiterarbeiten kann. | Ein grundsaetzlicher Produktionsansatz ist erkennbar, mehrere wesentliche Angaben muessen jedoch geklaert oder ergaenzt werden. | Der Entwurf ist konkret genug, um als belastbare Grundlage fuer die fachliche Abstimmung mit einem Produktionspartner zu dienen. |
| Technische Plausibilitaet | Der Entwurf enthaelt deutliche Widersprueche, gravierende fachliche Fehler oder unplausible Mengen und Prozesswerte. | Der Entwurf ist im Grundsatz plausibel, enthaelt aber einzelne Fehler, Inkonsistenzen oder unsichere Annahmen. | Rohstoffe, Mengenrelationen, Zielwerte und Prozessannahmen sind in sich schluessig; es fallen keine wesentlichen fachlichen Fehler auf. |
| Stiltreue | Der Entwurf verfehlt wesentliche Merkmale des vorgegebenen Bierstils. | Der Stil ist erkennbar, einzelne Zielwerte, Rohstoffe oder Prozessentscheidungen sind jedoch nur teilweise stiltypisch. | Zielwerte, Rohstoffe und Prozess passen klar und nachvollziehbar zum vorgegebenen Bierstil. |
| Pilotierbarkeit | Ein sinnvoller Kleinsud waere auf Grundlage des Entwurfs ohne grundlegende Neukonzeption kaum planbar. | Ein Kleinsud ist grundsaetzlich planbar, erfordert aber mehrere fachliche Ergaenzungen, Annahmen oder massstabsbedingte Anpassungen. | Der Entwurf laesst sich mit ueblichen fachlichen Anpassungen gut als Kleinsud planen; scale-abhaengige Annahmen und Pruefpunkte sind ausreichend erkennbar. |
| Briefing-Qualitaet | Der Entwurf ist als Kommunikationsgrundlage ungeeignet oder laesst zentrale Anforderungen und offene Fragen unklar. | Der Entwurf kann als Gespraechseinstieg dienen, erfordert aber mehrere Rueckfragen und Ergaenzungen. | Anforderungen, Annahmen, offene Punkte und Pruefbedarf sind so dargestellt, dass eine effiziente fachliche Abstimmung moeglich ist. |
| Korrekturbedarf | Sehr hoher Korrekturbedarf; der Entwurf muss fachlich weitgehend neu aufgebaut werden. | Mittlerer Korrekturbedarf; wesentliche Teile sind brauchbar, mehrere Punkte muessen substanziell ueberarbeitet werden. | Sehr geringer Korrekturbedarf; nur uebliche fachliche Pruefung und kleinere Anpassungen sind erforderlich. |
| Gesamtempfehlung | Entwurf verwerfen oder grundlegend neu erstellen. | Nach deutlicher fachlicher Ueberarbeitung weiterverfolgen. | Als gute Arbeitsgrundlage weiterverfolgen; normale professionelle Pruefung bleibt erforderlich. |

## Pilotierbarkeit und Kleinsud-Eignung

Frage:

> Wie gut eignet sich der Rezeptentwurf als Grundlage fuer einen Kleinsud beziehungsweise Pilotbrauversuch, mit dem Rezeptidee, Zielwerte und erwarteter Charakter vor der Uebertragung auf den Produktionsmassstab geprueft werden koennen?

Kurze Zusatzfrage:

> Welche Angaben oder massstabsbedingten Anpassungen waeren fuer einen Pilotversuch besonders wichtig?

Die Zusatzantwort wird im Feld `pilot_scale_adaptations` stichpunktartig erfasst. Moegliche Themen sind insbesondere Sudhausausbeute, Verdampfung, Hopfenausnutzung, Hefemenge, Gaerbehaeltergeometrie, Kuehlung, Wasser, Verluste und Abfuellung.

Bewertet wird die erwartete Eignung des Textentwurfs fuer die Planung eines Pilotversuchs. Ein tatsaechlicher Kleinsud, analytische Messwerte und eine sensorische Bewertung waeren ein eigener Versuchsarm. Aus der Pilotierbarkeitsbewertung wird daher weder tatsaechliche Braubarkeit noch sensorische Zielerreichung abgeleitet.

## Geschaetzter Nachbearbeitungsaufwand

Der Zeitaufwand wird getrennt vom Korrekturbedarf erfasst. Ein schwerwiegender Einzelpunkt kann schnell korrigiert sein, waehrend viele kleinere Luecken insgesamt viel Zeit benoetigen koennen.

Frage:

> Wie viel Zeit muesste eine fachkundige Person voraussichtlich investieren, um diesen Entwurf ohne weitere LLM-Unterstuetzung zu einem brauchbaren technischen Briefing fuer einen Produktionspartner zu ueberarbeiten?

| Code | Zeitband |
|---|---|
| `T1` | hoechstens 15 Minuten |
| `T2` | 16-30 Minuten |
| `T3` | 31-60 Minuten |
| `T4` | 61-120 Minuten |
| `T5` | mehr als 120 Minuten |
| `TX` | anhand des Entwurfs nicht einschaetzbar |

Die Angabe ist eine subjektive Expertenschaetzung. Sie wird im Paper als `geschaetzter fachlicher Nachbearbeitungsaufwand` und nicht als tatsaechlich gemessene Zeitersparnis berichtet.

Die Zeitbaender werden ordinal ausgewertet. Sie werden nicht ohne gesonderte Begruendung in exakte Minuten umgerechnet, summiert oder als gemessene Arbeitszeit behandelt.

## Art der erforderlichen Nacharbeit

Mehrfachauswahl ist moeglich:

| Code | Kategorie | Beispiele |
|---|---|---|
| `N0` | keine wesentliche Nacharbeit | nur normale fachliche Freigabepruefung |
| `N1` | formal und strukturell | fehlende Abschnitte, uneinheitliche Einheiten, unklare Darstellung |
| `N2` | rechnerisch und konsistenzbezogen | Mengen, Summen, Zielwerte, Ausbeute, Einheiten |
| `N3` | brautechnologisch | Rohstoffe, Schuettung, Hopfung, Hefe, Maischen, Gaerung, Lagerung |
| `N4` | anlagen- oder betriebsspezifisch | Wasser, Sudhausausbeute, Tanks, Verluste, Abfuellung, Haltbarkeit |
| `N5` | kommunikativ | unklare Anforderungen, fehlende Entscheidungen, Rueckfragen an Auftraggeber oder Produktionspartner |

`N0` wird nur verwendet, wenn keine der Kategorien `N1` bis `N5` zutrifft.

## Potenzial fuer LLM-gestuetzte Nacharbeit

Frage:

> In welchem Umfang koennten die notwendigen Korrekturen voraussichtlich erneut durch ein LLM unterstuetzt werden?

| Code | Antwortoption |
|---|---|
| `A1` | ueberwiegend mit LLM-Unterstuetzung bearbeitbar |
| `A2` | teilweise mit LLM-Unterstuetzung bearbeitbar |
| `A3` | ueberwiegend menschliche Fachpruefung erforderlich |
| `A4` | ohne konkrete Anlagen- oder Betriebsdaten nicht sinnvoll bearbeitbar |
| `AX` | nicht einschaetzbar |

Es wird keine zweite Zeitangabe fuer eine LLM-gestuetzte Revision verlangt. Ohne standardisiertes Modell, Revisionsprompt und beobachteten Arbeitsablauf waere diese Schaetzung nicht belastbar.

Die Kategorien `A1` bis `A4` und `AX` werden als kategoriale Einschaetzungen ausgewertet und nicht gemittelt.

## Kurze qualitative Angaben je Entwurf

Die Antworten sollen stichpunktartig bleiben:

1. Welcher fachliche Fehler oder welche Unplausibilitaet ist am wichtigsten?
2. Welche Information fehlt am dringendsten fuer ein professionelles Produktionsbriefing?
3. Welche Korrektur oder Klaerung sollte zuerst erfolgen?

Die separat erfassten Hinweise zu massstabsbedingten Anpassungen stehen im Feld `pilot_scale_adaptations` und werden nicht mit der wichtigsten allgemeinen Korrektur gleichgesetzt.

## Abschliessende Fragen nach allen Entwuerfen

Diese Fragen werden nur einmal pro Experte gestellt:

1. Bei welchen Aufgaben oder Bestandteilen spart ein LLM-Entwurf aus Ihrer Sicht tatsaechlich Zeit?
2. Welche Risiken entstehen, wenn ein Brau-KMU einen solchen Entwurf ungeprueft uebernimmt?
3. Welche wiederkehrenden Staerken oder Fehler sind Ihnen ueber mehrere Entwuerfe hinweg aufgefallen?
4. Welche Nacharbeiten koennen sinnvoll durch ein LLM unterstuetzt werden und welche erfordern zwingend Brauexpertise oder konkrete Betriebsdaten?

## Felder fuer `Expert_Ratings`

| Feld | Typ/Inhalt |
|---|---|
| `expert_alias` | E01, E02 usw. |
| `blind_output_id` | B01-B08 |
| `rating_date` | Datum |
| `kmu_fit` | 1-5 oder NB |
| `production_readiness` | 1-5 oder NB |
| `technical_plausibility` | 1-5 oder NB |
| `style_fidelity` | 1-5 oder NB |
| `pilotability` | 1-5 oder NB; erwartete Eignung als Grundlage fuer einen Kleinsud |
| `briefing_quality` | 1-5 oder NB |
| `correction_need_score` | 1-5 oder NB; 5 = sehr gering |
| `overall_recommendation` | 1-5 oder NB |
| `rework_time_band` | T1-T5 oder TX |
| `rework_types` | N0-N5, Mehrfachauswahl |
| `llm_rework_potential` | A1-A4 oder AX |
| `main_issue` | kurzer Freitext |
| `most_important_missing_info` | kurzer Freitext |
| `first_required_correction` | kurzer Freitext |
| `pilot_scale_adaptations` | kurzer Freitext zu erforderlichen Anpassungen fuer einen Kleinsud |

## Gemeinsamer Kern und professionelles Zusatzmodul

Professionelle Bewertende bearbeiten das vollstaendige Raster.

Eine gegebenenfalls bestaetigte Hobbyvergleichsgruppe bearbeitet ausschliesslich den gemeinsamen rezepttechnischen Kern:

- `technical_plausibility`
- `style_fidelity`
- `pilotability`
- `correction_need_score`
- `main_issue`
- `first_required_correction`
- `pilot_scale_adaptations`

KMU-Fit, Produktionsnaehe, Briefing-Qualitaet, Gesamtempfehlung als Produktionsbriefing, Nachbearbeitungszeit bis zum professionellen Briefing, betriebliche Nacharbeitsarten und die abschliessenden KMU-Fragen gehoeren zum professionellen Zusatzmodul. Hobbybewertungen werden fuer diese Felder nicht als `NB` erzwungen, sondern strukturell nicht erhoben. Verglichen werden nur die identischen Kernfelder.

## Auswertungsregeln

- Jedes Bewertungskriterium wird zunaechst einzeln ausgewertet.
- Pilotierbarkeit und Produktionsnaehe werden getrennt ausgewertet: Die erste Dimension betrifft die erwartete Planbarkeit eines Kleinsuds, die zweite die Nutzbarkeit als Grundlage fuer die gewerbliche Produktion.
- Ein zusammengesetzter Qualitaetsindex wird nur verwendet, wenn Gewichtung und Berechnung vor den Hauptlaeufen festgelegt werden; fuer den Minimalumfang ist kein Gesamtindex vorgesehen.
- Bei mehreren Expert:innen werden Verteilungen, Medianwerte je Kriterium und abweichende Einschaetzungen deskriptiv berichtet.
- Eine formale Interrater-Reliabilitaet wird nur berechnet, wenn Anzahl, Vollstaendigkeit und Skalenstruktur dies sinnvoll zulassen.
- Zeitbaender werden ordinal, Nacharbeitstypen und LLM-Unterstuetzbarkeit kategorial ausgewertet.
- Qualitative Angaben werden in wenige nachvollziehbare Fehler- und Nacharbeitskategorien codiert; Originalrueckmeldungen bleiben anonymisiert ausserhalb des oeffentlichen Repositories.

## Ergebnis der Pilotpruefung

Das Raster wurde am 2026-08-18 durch das Projektteam auf beide ausgeschlossenen Pils-Piloten angewendet. Dies ist ein Instrumententest und kein Expertenrating.

- Mengen- und Zielwertwidersprueche lassen sich unter `Technische Plausibilitaet`, `Korrekturbedarf`, `N2` und `N3` eindeutig erfassen.
- Zeitband, Art der Nacharbeit und Potenzial fuer erneute LLM-Unterstuetzung bleiben voneinander unterscheidbar.
- Die drei kurzen qualitativen Fragen fuehren zu getrennten Angaben fuer Fehler, fehlende Betriebsinformation und erste Korrektur.
- `NB` wurde als ausdrueckliche, nicht numerische Option ergaenzt.
- Die urspruengliche Annahme von 5-7 Minuten je Entwurf war angesichts von 989 bzw. 1.429 Pilotwoertern knapp; fuer die Planung werden 8-10 Minuten angesetzt.
- Es wurden keine inhaltlichen Anker nach beobachteter Modellleistung verschoben.

Am 2026-08-26 wurden zusaetzlich zwei GPT-5.6-Sol-Instrumentenpiloten mit `reasoning.effort=max` und `text.verbosity=low` technisch geprueft. Beide Ausgaben sind mit dem unveraenderten Raster bewertbar; P02 enthaelt alle 13 verlangten Abschnitte. Die Anpassung von `v1.0` auf `v1.1` betrifft ausschliesslich Status, Modellkontext und die Planungsannahme zum zeitlichen Bewertungsaufwand. Kriterien, Skalen, Anker und Auswertungsregeln bleiben unveraendert.

Vor dem ersten Hauptlauf wurde das Raster am 2026-08-26 als `v1.2` um Pilotierbarkeit und `pilot_scale_adaptations` ergaenzt. Anlass war die methodische Trennung zwischen rezepttechnischer Eignung fuer einen kleinen Versuchssud und Produktionsnaehe auf 10-hl-Massstab. Die ausgeschlossenen Low-Verbosity-Piloten enthalten ausreichend Rezept- und Prozessangaben, um beide Felder anzuwenden; P02 fordert zusaetzlich ausdruecklich Skalierungshinweise. Es wurden keine Hauptoutputs erzeugt oder zur Anpassung des Instruments herangezogen.

## Optionale Erweiterung

Eine tatsaechliche LLM-gestuetzte Ueberarbeitung mit standardisiertem Revisionsprompt waere ein eigener Versuchsarm. Sie gehoert nicht zum garantierten Kernumfang und wird nur vor den Hauptlaeufen aufgenommen, wenn Zeitbudget und Expertenkapazitaet ausreichen.

Dasselbe gilt fuer einen real gebrauten Kleinsud mit analytischer und sensorischer Pruefung. Er kann spaeter als dokumentierte Fallstudie ergaenzt werden, ist aber nicht Bestandteil der acht textbasierten Hauptoutputs oder ihrer Kernbewertung.
