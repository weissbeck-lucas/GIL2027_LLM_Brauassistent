# Versuchsszenarien v1.0

Stand: 2026-08-18

Status: Nach Expertenplausibilisierung und Pilotpruefung fuer die empirischen Hauptlaeufe eingefroren

## Zweck

Die Datei definiert zwei vergleichbare Brau-KMU-Szenarien fuer die Untersuchung von LLM-generierten Bierrezeptentwuerfen. `v1.0` friert die in `v0.2` dokumentierten und durch E01 plausibilisierten Zielwerte unveraendert fuer die Hauptlaeufe ein.

Die vollstaendige Zielwertableitung ist in `01_Dokumente/Methodik_Zielwertableitung.md` dokumentiert. Das Entscheidungsprotokoll zur Expertenrueckmeldung steht in `06_Expertenbewertung/Plausibilisierung_Zielwerte.md`.

## Referenzhierarchie

Es gibt keinen einzelnen rechtlich verbindlichen Stilrahmen, der Pils und Altbier durch IBU-, EBC- und Sensorikwerte abschliessend definiert.

| Rang | Referenz | Verwendung im Projekt |
|---|---|---|
| 1 | European Beer Star 2026 | Primaere Referenz fuer analytische Korridore und Stilbeschreibung |
| 2 | BJCP Beer Style Guidelines 2021 | Sekundaere Referenz fuer Vergleich und Einordnung |
| 3 | Deutsche Bierverordnung | Rechtlicher Kontext fuer Herstellung und Kennzeichnung, nicht als sensorischer Stilrahmen |
| 4 | Anonymisierte Expertenplausibilisierung | Fachliche Pruefung und begruendete Anpassung der konkreten Zielwertkombinationen |

Die Szenarien heissen im Projekt `S01 Pils` und `S02 Altbier`. Die Bezeichnung `German-Style Pilsner` wird nur verwendet, wenn die englischsprachige Kategorie des European Beer Star benannt wird.

## Gemeinsamer KMU-Use-Case

Ein kleines Brau-KMU bzw. Getraenkestartup moechte eine neue Standardsorte durch einen externen Lohnbrauer produzieren lassen. Das LLM soll einen produktionsnahen Rezeptentwurf als Grundlage fuer ein technisches Briefing erstellen. Der Entwurf ist kein freigegebenes Braurezept und muss durch einen erfahrenen Brauer sowie den konkreten Produktionspartner geprueft werden.

Gemeinsame Arbeitsannahmen:

- Ausschlagmenge: 10 hl bzw. 1.000 Liter
- in Deutschland uebliche und regulaer beschaffbare Rohstoffe
- professioneller, aber ressourcenbeschraenkter Brau-KMU-Kontext
- keine vertraulichen Anlagen-, Wasser- oder Betriebsdaten
- keine Vorgabe einer konkreten Brauanlage
- keine lebensmittelrechtliche oder kommerzielle Freigabe durch das LLM

Die 10-hl-Menge ist eine einheitliche operative Vergleichsannahme. E01 sah keinen grundsaetzlichen Skalierungskonflikt fuer die betrachteten Rezepturen, konnte aber keine besondere Modellrelevanz dieser Groesse ableiten.

## Kontrollierte und offene Angaben

In beiden Promptvarianten werden dieselben kontrollierten Angaben verwendet:

- Szenario-ID und Bierstil
- Ausschlagmenge
- Ziel-Stammwuerze
- Ziel-Alkoholgehalt
- Ziel-Bittere
- Ziel-Farbkorridor
- qualitativer Zielcharakter
- KMU-/Lohnbrauer-Kontext

Folgende Angaben bleiben bewusst offen und muessen vom LLM als Auswahl oder Annahme behandelt werden:

- konkrete Brauanlage und Sudhausausbeute
- Wasseranalyse und erforderliche Wasseraufbereitung
- konkrete Malzprodukte, Malzfarben und Lieferanten
- konkrete Hopfenprodukte und tatsaechliche Alpha-Saeuregehalte
- konkrete Hefeprodukte, Vitalitaet und Lieferform
- Tankgeometrie und Kapazitaeten
- Gebinde, Abfuelltechnik und Haltbarkeitsziel
- betriebliche Verlust- und Ausbeutefaktoren

Die Rohstoffmengen koennen nur zusammen mit den gewaehlten Rohstoffen und relevanten Spezifikationen sinnvoll bewertet werden. Das LLM soll solche Annahmen offenlegen; die Experten bewerten Auswahl, Mengen und Konsistenz.

## S01 Pils

Primaere Referenz: European Beer Star 2026, Kategorie 2 `German-Style Pilsner`.

### Referenzkorridor und rechnerischer Startpunkt

| Merkmal | European Beer Star 2026 | Rechnerischer Startkandidat |
|---|---:|---:|
| Stammwuerze | 11,0-12,9 Grad Plato | 12,0 Grad Plato |
| Alkohol | 4,0-5,5 % vol. | 4,8 % vol. |
| Bittere | 25-50 IBU | 38 IBU |
| Farbe | helles Strohgelb bis Gold; kein numerischer EBC-Korridor | kein rechnerischer Kandidat |

### Zielwerte v1.0

| Merkmal | Zielwert | Herkunft und Entscheidung |
|---|---:|---|
| Ziel-Stammwuerze | 11,3 Grad Plato | von E01 statt 12,0 Grad Plato empfohlen, um einen schlanken und hoch vergorenen Charakter bei 4,8 % vol. abzubilden |
| Ziel-Alkohol | 4,8 % vol. | arithmetischer Mittelpunkt des EBS-Korridors, von E01 bestaetigt |
| Ziel-Bittere | 38 IBU | arithmetischer Mittelpunkt des EBS-Korridors, von E01 bestaetigt |
| Ziel-Farbe | 6-8 EBC | expertengestuetzter Zielkorridor von E01; kein EBS-Zahlenkorridor |

Zielcharakter: hell, klar, schlank, trocken und sauber vergoren, mit deutlicher Hopfenbittere und zurueckhaltendem Hopfenaroma.

Qualitative Kerneigenschaften:

- untergaerig
- hoher Vergaerungsgrad und geringe Restsuesse
- deutliche bis hohe Hopfenbittere
- feines, moderates Hopfenaroma, nicht durch Kalthopfung gepraegt
- keine Fruchtester und kein Diacetyl
- filtriert, keine Kaeltetruebung

Fachlicher Pruefhinweis: Eine konventionelle Pils-Schuettung kann vollstaendig aus Pilsener Malz bestehen. Dies wird nicht als feste Eingabe vorgeschrieben, damit die Rohstoffauswahl Teil der zu bewertenden LLM-Leistung bleibt. Abweichungen muessen fachlich plausibel sein.

## S02 Altbier

Primaere Referenz: European Beer Star 2026, Kategorie 49 `Alt`.

### Referenzkorridor und rechnerischer Startpunkt

| Merkmal | European Beer Star 2026 | Rechnerischer Startkandidat |
|---|---:|---:|
| Stammwuerze | 11,0-12,5 Grad Plato | 11,8 Grad Plato |
| Alkohol | 4,8-5,2 % vol. | 5,0 % vol. |
| Bittere | 20-45 IBU | 33 IBU |
| Farbe | kupferfarben bis braun; kein numerischer EBC-Korridor | kein rechnerischer Kandidat |

### Zielwerte v1.0

| Merkmal | Zielwert | Herkunft und Entscheidung |
|---|---:|---|
| Ziel-Stammwuerze | 11,8 Grad Plato | arithmetischer Mittelpunkt des EBS-Korridors, von E01 bestaetigt |
| Ziel-Alkohol | 5,0 % vol. | arithmetischer Mittelpunkt des EBS-Korridors, von E01 bestaetigt |
| Ziel-Bittere | 33 IBU | arithmetischer Mittelpunkt des EBS-Korridors, von E01 bestaetigt |
| Ziel-Farbe | 30-35 EBC | expertengestuetzter Zielkorridor von E01; kein EBS-Zahlenkorridor |

Zielcharakter: kupferfarben, sauber vergoren, ausgewogen malzig und bitter, mit mittlerem Koerper und trockenem Finish.

Qualitative Kerneigenschaften:

- obergaerig
- mittlerer Koerper und malziger Geschmack
- geringes bis deutliches Hopfenaroma; eine markante Hopfung ist zulaessig
- sauberer, frischer Gesamteindruck, haeufig mit trockenem Finish
- niedrige bis mittlere Fruchtester
- kein Diacetyl
- Truebung ist zulaessig

Fachlicher Pruefhinweis: Fuer die kupferne Farbe sind mehrere plausible Kombinationen aus Pilsener Malz und dunkleren Malzsorten moeglich. Das LLM muss die gewaehlten Malze, Mengenanteile und relevanten Farbangaben konsistent ausweisen.

## Rohstoff- und Berechnungsanforderungen

Fuer beide Szenarien gilt:

- Malzmengen sind nur zusammen mit Malztyp, Anteil und relevanter Farbspezifikation nachvollziehbar.
- Hopfenmengen sind nur zusammen mit Hopfensorte bzw. -produkt und angenommenem Alpha-Saeuregehalt nachvollziehbar.
- Hefeauswahl und Anstellmenge muessen zur Gaerfuehrung und Zielmenge passen.
- Anlagenabhaengige Mengen und Ausbeuten muessen als Annahmen gekennzeichnet werden.
- Die Beziehung zwischen Stammwuerze, erwartetem Endextrakt, Vergaerungsgrad und Alkohol ist auf innere Konsistenz zu pruefen.

## Plausibilisierungsstatus

E01 hat die Zielwertkombinationen am 2026-07-16 fachlich geprueft. Eine Aenderung der Pils-Stammwuerze, eine Praezisierung des Pils-Zielcharakters und zwei EBC-Zielkorridore wurden in `v0.2` uebernommen.

Eine zweite Vorabpruefung durch E02 ist fuer den Freeze nicht erforderlich. E02 und weitere Expert:innen koennen die spaeteren Rezeptoutputs unabhaengig bewerten. Dadurch wird die Vorabpruefung nicht mit der verblindeten Ergebnisbewertung gleichgesetzt.

## Freeze-Kriterien fuer v1.0

- Zielwerte und Zielcharakter aus `v0.2` sind in `Prompt_Register` und `Data_Dictionary` uebertragen
- P01 und P02 verwenden identische kontrollierte Szenarioeingaben
- Ziel-Farbkorridor ist in beiden Promptvarianten enthalten
- Rohstoff- und Alpha-Saeureangaben koennen in Outputs und Checks erfasst werden
- Modell- und Wiederholungsumfang sind beschlossen
- Bewertungsraster und Loggingstruktur passen zu den erwarteten Outputs
- nach dem Freeze erfolgen keine stillen Text- oder Zahlenanpassungen

## Aenderungen gegenueber v0.2

- keine Aenderung an Zielwerten, Zielcharakter oder offenen Anlagenannahmen
- Freigabestatus nach den zwei technischen Pils-Piloten auf `frozen` gesetzt
- inhaltliche Mengenfehler der Pilotoutputs nicht in den Szenariotext zurueckgespielt, da sie Gegenstand der spaeteren Bewertung sind

## Quellen

- European Beer Star 2026, Kategorien: https://european-beer-star.com/ebs-de/wettbewerb/kategorien/
- European Beer Star 2026, englische Kategoriebeschreibung: https://european-beer-star.com/ebs-wAssets/docs/kategorien-en/EN-Kategoriebeschreibung-2026.pdf
- BJCP 2021, German Pils: https://styles.bjcp.org/bjcp-2021-beer/5/5d-german-pils
- BJCP 2021, Altbier: https://styles.bjcp.org/bjcp-2021-beer/7/7b-altbier
- Bierverordnung: https://www.gesetze-im-internet.de/bierv/
- anonymisierte Expertenplausibilisierung: `06_Expertenbewertung/Plausibilisierung_Zielwerte.md`
