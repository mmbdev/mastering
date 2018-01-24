# VL notes

Notizen zu den einzelnen Kapiteln von Advanced Inofrmation Retrival.

## K1 Einfuehrung und Ueberblick

Information Retrival ist die Schnittmenge von:
  - Informationswissenschaft
  - Intormaitk
  - Computerlinguistik

Anwendungsgebiete:

  - Informationsbeschaffung der Unternehmung (Patente, Kreditwürdigkeit, Fachinfos, Literatur)
  - Fachinformationen (Genome, Kernresnanzspektren)
  - Bibliotheken und andere Infodienstleister - Bestandsinformationen (Recherche in Beständen)

Abgrenzung zu benachbarten Gebieten:

  - Strukturen erkennen (Exploration): Data- / Text-Mining
  - Benuterfragenorientierte Sicht / kogitive Prozesse / organ. Randbedingungen
  - Information -> Representation, Speichern, Organisieren und Auffinden


Herausforderung:
  Das Wissensvolumen wächst immer mehr.
  Traditionelle Signatursysteme aus Biblothekswesen sind unscharf, dieses Problem trifft Klassifikationssysteme generell.
  Expandierende/neue Wissensgebiete sind für Signatursysteme durch ihre Interdisziplinarität problematisch

Typologie: 
  Info-Retrival System -> Frage/Antwort-System
  Database-Mgmt -> Mgmt-Info-System

Grundfunktion:
  Suchanfragen -> Inforsprache -> Dokumente (Infoeinheit)

gängige Indexsprachen:
  - Abstracts
  - Freie Schlagwörter
  - Schlagwörter auto extrahiert
  - Dokument-Attribute (TI, AU, DT, ...)
  - Kontrollierte Schlagwörter
  - Klassikfikation-Codes
  - Relecanzurteile eines Endnutzers

  Artefakte dieser Indexierungssprachen lassen sich beliebig kombinieren (Hybriderschließung).

Retrival auf einfachen Strukturen:

  - Linerae Liste: 					        Avarage Case (n+1)/2 Elementen ist ein Treffer
  - Binäre Suche:					          log2(n+1) - Vergleiche für Treffer notwendig
  - Squentielle geordnete Suche:  	"key"-Attribut, log2(n+1)
  - Indizierte Daten:				        log2(n+1), + kleinerer Index, - neue Datei schaffen

Relationales Datenbankmodell: Name-Person*-----0..1Artikel-SI*
  Vorteil: sehr komplexe Strukturen möglich. Strukturen sind eine Art Inhaltserschließung und fast ontologie-like lesbar.
  Gängige Abfragesprache: Sequential Query Language (SQL)

Übung:
  Stellen Sie die Rechenaufwände beim Suchen in Abhängigkeit von in einem Koordinatensystem dar.
  X-Achse: n
  Y-Achse: Rechenaufwand (notwendige Schirtte zum Suchen)

Datenbankanalyse als technische Grundlage von Rechneranwendungen:

User	---> App
 !					DataBase
Admin	---> OS

Information Retrival in kommerziellen Datenbanken:
  - Bibliograische DB 	(Fach, Nationalbibliotheken)
  - Faktendatenbanken 	(Adressen und Firmen)
  - Volltext-DB			    (Zeitungen)
  - Ton,Multimedia,Links,Zitats, Nummerische-DB
  - Biografische DB

Adaption der Invertierung auf Basis des ER-Modelles, s. Zeichnung Folie 33.

Informatin Retrival Prozess:
  
  ! Idee 				
  ! Autor
  ! Dokument
  ! Eingaben
  ! Datenbasis
  
  ! Probelm, Idee, Suchanfrage
  ! Benutzer
  ! Suchergebnisse
  ! Informationsvermittler
  ! Suchanfrage / Anzeige
  ! Datenbank

Modell zum IR-Prozess, s. Folie 34/35.

### Ausblick Themengebiete 

Inhaltserschließung:
  - Abstracting . Indexierung mit Termen (Manuell, Auto, Grund und Stammformenreduktion, Termgewichtung, Auto Abstracting)
  - Kontrollierte Vokabulairen mit Thesauri
  - Klassifikationsschema
  - Implizierte Erschließung per Dokumentenstruktur - Bsp. XML

Retrival:
  - Retrivalqualität (Recall und Precission)
  - Relevance Feedback-Verfahren
  - Retrivalmodelle (Boolsches, Vektor, Probalisitisches, Fuzzy-Modell)

### Epolig des Prologs der Vorlesung

Auf Metaebene des Information Retrivals betreiben wir Wissensmanagement.

### Inhaltserschließung

das richtige Wissen definieren, identifizieren und strukturieren.

### Retrival

  Prozess: Installation eines kontinuierlichen Wissensmanagementes
  Kultur: Wissensaustausch muss belohnt werden
  Infrastruktur: Abbilden der Inhalte auf Meiden

Abbildung aller Retrivalmodelle und Eigenschaften mit mathematischem Fundament, s. Folie 38.

Die Unterscheidung zwischen Dateneben und Metaebne ist nicht trivial:

  Beschreibung der Beschreibungssprache					    Meta
  Beschreibungsprachensyntax					       Meta Data - Beschreibung Language
  Schemabescheibungssprache				 		  Meta Data - Schema - Definition
  Datenbankschema des OPAC					 Meta Data - Data Base Schema
  Daten auf der Datenbank des OPAC		Meta Data - Info Sys
  In der Bib vorhandene Literatur		Data - Bib

## K2 Abstracting

DIN1426 - ein Abstract gibt kurz und klar den Inhalt eines Dokumentes wieder.

Inhaltsverzeichnis / Auszug / Zusammenfassung / Kurzreferat / Sammelreferat / Rezession / Bericht

							(Sig. Worte)^2    (2)^2
							--------------	  -----
Signalwörter eines Satzes =  Anzahl Wörter	    2   = 2 

Satz mit höchstes Sig. ausgeben. 
Zerlegung von Sätzen in Phasenstrukturbäume (AP: Adjektivphrasen, NP: Nominativpphrasen, PP: Präpositionalphrasen, Rels: Relativsatz)

## K3 Indexierungstechniken

  Indexieren-Verschlagwortung einer Dokumenten-Einheit durch Deskriptoren (Index-Terms)
  ST-Supplementary Terms CT-kontrollierten Vokabular
  Stoppworte: keine Betrachtung {ich, du, er, sie, es, der, die, das, ein, eine, einer}
  einfache Reduktionsverfahren: 
   - Ersetzen der Wortendungen durch Stammendungen - Grund und Stammformenreduktion
   - Verfahren mit Wortform-Wörterbuch
  advanced = vollautomatisch

Grundsätzliche Arten der Post/Prä-Koordination:
  Post:
   - erst bei Suchanfrage Term-Kombis
   - structured indexing

  Prä:
   - Zusammenbau bereits bei Indexierung
   - coordinate indexing

Terme bekommen Attribute:
  - Gewichtung von Deskriptoren: Indexierung, linguistische Verfahren, Evaluierung
  - Qualifiers (Rollenindikatoren) Italien (E), am gängisten und häufigsten in der Chemie

  		Häufigkeit in der t im Dok vorkommt
  g+= 	------------------------------------- 
  		Anzahl der Doks, in denen t vorkommt

Bsp.: "Information AND Retrival" 
  - Dok1: Info 0,01, Retrival 0,012 = 0,012
  - Dok2: Info 0,03, Retrival 0,01 = 0,04

Relevanz-Ranking: Dok2, Dok1

## K4 Spracherkennung und Rechtschreibungserkennung N-Gramme

N-Gramme: Zerlgung von Wörtern, Sätzen, Texten bestehen aus Buchstaben, Graphemen oder Phoemen

HALLO WELT = M = {'HAL', 'ALL', 'LLO','LO_','O_W','_WE','WEL','ELT'} N = 3 (Trigramm)

Für jede Sprache sind bestimmte Häufigkeiten von N-Grammen bestimmt.

Anwendungsfelder:
 - Spracherkennung, Maschinelles Übersetzen, Themenerkennung, Rechtschreibkorrektur, Forensik, OCR-Prozesse, Kontextbestimmung

Übung: Berechnen Sie
  A = P(EN,"Garten")
  B = P(DE."Garten")

### Dice-Koeffizient
d(wirk, word) = ... -> s,Uebungsblatt! 
Uebung: Passt work oder word besser auf wirk?

Wahl von N 
  -> großes N = wenige Beispiele für jedes N-Gramm
  -> kleines N = viele Beispiele, aber Vorhersage dafür ungenau

guter Kompromiss - Empirische Bewertung wird N=2 oder N=3 gesetzt.

## K5 Boole'sche Retrivalmodell

Mengen Operationen: Begriff1 AND/OR/NOT Begriff2

  Nachteile:
   - Disjunkte Unterteilung in relevant / unrelevant
   - alle Doks sind gleichberechtigt, kein Ranking
   - Erwünschter Umfang schwer kontrollierbar

-> Verbesserung durch Advanced im Auto-Abstracting!
funktioniert aktuell nur in engen Kontexten.

## K6 Retrival - Effektivität - Recall and Precision

Situative Relevanz, Pertinenz (Subjektive empfundene Nützlichkeit), Objektive Relevanz (Neutrale Beobachtung), System Retrival (berechnet vom System)
  
  Typisches Szenario:
  10000 Suchdokumente, 70 Treffer bei einer Suchanfrage (tp+fp)
  30 Dok der gefundenen sind relevant, 40 unrelevant
  In Wirklichkeit 20 Doks sind noch mehr relevant, bewegen sich aber in der Grauzone und wuden nicht gefunden.

  - true positives (tp)   -> relevant gefundene Doks
  - false positives (fp)  -> nicht relevant gefundene Doks
  - flase negatives (fn)  -> nicht gefundenen Doks
  - ture negatives (tn)   -> nicht nachgewiesenen / ungefundene Doks

                  ! relevant  ! unrelevant !
  ----------------------------------------------
  gefunden        ! (tp)      ! (fp)
  nicht gefunden  ! (fn)      ! (tn)

  Beurteilung des Verteilungsergebnisses:

  Precision:      (Genauigkeit der Relevanz)            = tp / (tp + fp)
  Recall:         (Vollständigkeit oder Nachweisquote)  = tp / (tp + fn) 
  Fallout Ratio:  (Ausfallqoute)                        = fp / (fp + tn) 

Recall-Problem: Vorraussetzung für die Recall-Beurteilung ist die Kentniss über die volle Datenmenge (Antwortmenge).
  Recall drückt aus; was nicht gefunden wurde, aber vorhanden gewesen ist.

  Precision: Relevanz oder nicht Relevanz der Dokumente zeigen; wichtig Benutermodell - an was wird die Relevanz gemessen.

  Einflussfaktoren:
   - Qualität der Indexierung
   - Retrivalstrategie / Anfrageformulierung

  Praktischer Nutzen:
   - vergleichenden Betrachtung von Retrival-Systemen, Komponenten oder Recherche von Personen

  Ein solches Suchmusteranfragendiagramm ensteht nach mehreren Recherchevorgängen:

  Precisio
   !
   !      ^(1x1) wäre Optimum
   !    °DB2
   ! °DB1
   ! 
   ---------> Recal 

   Gängige mathematische Berechnungsverfahren:
    - Accuraacy Ac = (tp + tn) / (tp + fp + fn +tn) (Alle richtig zugeordneten Doks / alle Doks)
    - F-Measure 
              2*P*R
              ------
      Fß=1 =  P + R

    Maßnahmen bei zu wenigen Treffern im Ergebnis:
     - AND verrignern, mehr OR-Verküpfungen
     - Mutlidatabase, Tippfehler, Synoyme / Abkürzungen
     - Trunkierung, Klassifikationscodes

    Maßnamen bei zu vielen Treffern im Ergebnis:
     - OR verringern, mehr AND-Verknüpfungen
     - Terminologie
     - Datenbank, Anzahl der Suchfelder einschränken (nur CT)

## K7 Kontrolliertes Vokabular mit Thesauri

Thesaurus: Alle für die Indexierung bereitstehenden Begriffe sind festgeschrieben.

 - termologische Kontrolle durch Erfassung von Syn., Homonymen, Festlegung von Verzugsbenennungen
 - Darstellung der Beziehungen zwischen Begriffen
 - Polyhierarchien sind möglich 

  Gängige Abkürzungen:     Modebegriff
                        Term
                      Unterbegriff
                    Unter-Unter-Begriff

  Bsp.: Folie 28

  Thesaurusrelationen:
    BT - Boader Term
    NT - Narror Term
    RT - Related Term
    UF - Used For
    USE - Use
    TT - Top Term

  Postkoordination -> z.B. kein Thesaurus (structured indexing)
  Präkoordination -> z.B. Thesaurus (coordinate indexing)
    alle für die Indexierung bereitstehenden Begriffe sind festgeschrieben

  Vor/Nachteile:
  + geringerer Formulierungsaufwand gegenüber Freitextsuche
  + weniger linguistische Probleme, eindeutiger
  - altes Vokabular, teuerer in der Erstellung der DB
  - Indexierungsfehler, fehlende Treffer

  Prototypisches IR-System mit Thesaurus, s. Folie 32.

Übung: Erstellen Sie einen Thesaurus zum Thema Hochschule. (sollte 5-10 Begriffe enthalten)


## K8 Kalssifikation

Unterscheidung zwischen:
 - Prozess der Klassifikationserarbeitung
 - Klassifikationssystem als Ergebnis des Klassenbildungsprozesses
 - Prozess der Klassifizierung

                Schiff
                  !
          !-------!---------!--------------------------!
          !                 !                          ! 
      Fahrgastschiff    Frachtschiff              Fischerboot
                            !
                    !-------!------!-------------------!
                    !              !                   !
                Tankschiff     Kühlschiff       Massengutschiff

  Monohierarchie: nur eindimensionale Suche möglich
  Gattungsbegriff: Schiff; Artbegriff: Frachtschiff (Frachtschiff kann auch Gattungsbegriff sein, z.B. Von Tankschiff)

     Personentransport           Schiff               Fischerei
       !                           !                      !  
       !   !-------!---------!--------------------------! !
       !   !                 !                          ! !
      Fahrgastschiff    Frachtschiff                Fischerboot
                            !
                    !-------!------!-------------------!
                    !              !                   !
                Tankschiff     Kühlschiff       Massengutschiff

  Polyhierarchie: Gleichzeitige Recherche unter mehreren Aspekten (mehrdimensionale Suche)

Ketten: von oben nach unten (Schiff, Frachtschiff, Tankschiff)
Ebenen: von rechts nach links (Tankschiff, Kühlschiff, Massengutschiff)

Prototypisches IR-System mit Klassifikation, s. Folie 41.

Klassifikationssystem-Typen:
  Analytische Klassifikationen: vom Allg. zum Speziellen immer feiner werdent (Drichter)
  Facettenklassifikation (Analytisch-synthesische Klassifikaiton)
   - Merkmalsbegriffe eines Wissensgebietes (Facetten) - (Eigenschaften, Personen, Zeit, etc. ) zusammenführen

   Bsp.: Facettenklassifikation
   Sachverhalt: Verhütung von Hautkrankheiten von Chemiearbeitern
   Notation: CgHeMbi

  Eigenschaften:
   - Universalität (gesamte Wissenschaft geeignet)
   - Kontinuität (langer Zeitraum verwendbar)
   - Aktualität (Flexiel erweiterbar)

Klassifikationen basieren auf dem Prinzip der Präkoordination, das bedeutet Begriffe und Begriffskombinationen werden im Zuge der der Erarbeitung der Klassifkation festgelegt.

Vergleich von Klassifikationen und Thesauri:
  Klassifikation  - sind sys. geordnet; haben viele Wortkombis; präkoordiniert; star; weniger ausdruksfähig - Presicion = hoch!
  Thesauri        - sind alphabetisch geordnet, wenige Wortkombis; postkoordiniert; flexibel; ausdrucksmächtig - Recall = hoch!

Oft wird zur Klassifizierung mit Klassifikationen und Thesauris gearbeitet -> Hybriderschließung

Beispielklassifizierungen:
  Dewey-Dezimalklassifkation (DDC)
  Internationale Patentklassifikation (IPC)

Übung: 
  Realisieren Sie eine Facettenklassifikation zum Thema Hochschule.
  Folgende Facetten sollen berücksichtigt werden: Ort, Hochschultyp, Fach, Betätigung

## K9 Ranking in Retrivalsystemen (Relevance Feedback)

Ranking mit booleschem Retrival; 
  Vorraussetzung: Gewichtung der Terme bei der Anfrage oder Indexierung
  Vorteile: 
   - Rangordnung -> relevanteste Dok steht an Platz 1
   - Benutzer bestimmt den Abbruch, keine Mengenprobleme
  Verfahren:

  Dokumente                                   Frage
      !                                       !   !
  Dokumentrepräsentation    Fragerepräsentation   !
      !                       !   !               !
  Retrivalfunktion<-----------!   !               !
         !                        !               !
     Antworten>------------------------------------
  
  Moduse:
   - positiver (alle relevanten Dosk werden berücksichtigt)
   - negativer (alle nicht relevanten Doks werden berücksichtigt)
   - gemischter (relevante und irrelevante Doks werden berücksichtigt)

## K10 Retrievalmodelle nach Salton (Vektorraum-Modell)

  Idee:
    Jedem Dokument und jeder Frage ist eine Koordinate im mehrdimensionalen Raum zugeordnet.
    Jeder Term belegt eine Dimension in {0,1}. 
    Ein Match ist ein Skalarprodukt von 1 zwischen einem Fragevektor und einem Dokumentvektor.

  Skalarprodukt:
    a*b = |a|*|b|*cos(a,b)

  Schaubild, s. Folie 17.
  Matrixdarstellung  als Term-Dok-Matrix, s. Folie 18.

  Ähnlichkeitsbestimmung: 
   - Ähnlichkeit von Dokument- und Anfragevektor repräsentiert die mutmasliche Relevanz eines Doks gegenüber der Suchanfrage
   - Suchanfrage ist auch als Vektor dargestellt
   - Skalarpodukt ist mathematisches Vorbild, jedoch gibt es Vereinfachungen

   Fazit:
   - einfaches Modell, Ähnlichkeit von Doks leicht zu vergleichen
   - theorie Problem: Annahme der Unabhängigkeit der Terme unteinander

Übung: 
  Gegeben ist eine Term-Dok-Matrix und eine Anfrage Q. Bilden Sie ein Ranking mit dem Dice-Ähnlichkeitsmass.

## K11 Termgewichtungsverfahren

Worum es geht? -> Wie entstehen die Einträge der Dokumentvektoren?

Opterionalisierung der Gewichtung von Termen
  Bestimmung der Terme zur Inhaltsmodellierung der Doks

Inverse Dok-Frequenz, s. Folie 30, 31.

Übung:
  Gegeben sind 1000 Doks, jedes Dok hat 100 Worte.

  Term1: "Gott" kommt in  10 % der Doks vor, in Dok Di sogar 10 mal
  Term2: "Chur" kommt nur 1 mal in Dok Di vor.

  Berechnen Sie die Termgewichte T1 und T2 in Dokument Di

## K12 Clusterverfahren

Klassische Ordnungsinstrumente:
  - Thesauri
  - Klassifikaition

sind in der Erstellung aufwendig

Cluster bilden Sich durch:
 - nebeneinanderliegende Doks/Einheiten
 - Dokument/Einheitsfolgen
 - Sternstrukturen

Clusterhypothese: Eng verwandte Doks sind für die selbe Suchanfrage auch in vergleichbarer Weise relevant.
Clusteranalyse:   ähnliche doer relationale Doks erkennen und verbinden

Über Schwellwert T in Ähnlichkeitsmatirx -> Clusterzugehörigkeit definieren
 T-groß:  weniger und größere Klassen
 T-klein: mehrere und kleinere Klassen

Darstellungsmöglichkeiten:
 - Clusterdia: s. Folie 44
 - Baum-Klassifikationsschema, s. Folie 45
 - Cluster-Zenteroide

Algo zum Einfügen eines Doks D in eine Clusterstruktur, s. Folie 50
Suchen in der hierarchischen Clusterstruktur am Beispiel der Top-Down-Suche, s. Folie 51

## K13 Retrivalmodell mit Fuzzy-Mengen

Werte auf Begriffe abbilden mit "traditioneller Mengenlehre"

Element x kann mit einer bestimmten Menge unscharf zugehörig sein.

Einsatz: 
  - Abbildung der Wichtigkeit von Deskriptoren
  - Abbildung gradueller Relevanz von Doks bei Suchanfragen
  - Darstellung semantischer Beziehungen von Doks

Übung:
  Gegeben sind folgende Personen der Menge 
  U: {Peter, 14; Andi, 23; Ralf, 30; Jule,10; Opa,99}
  Gegeben sind folgende Zugehörigkeiten
  0-30 jung
  20-60 mitte
  60-max alt

  Bestimmen Sie die Menge der Personen für die jung, mittel, alt zutrifft.
  Ebenso die Menge der Personen, die jung und mittel zugleich sind.
  Machen sie jeweils ein Ranking.

## K14 Graph-Basierte Modelle

Graphentheorie:
 - Graphen sind mathematische Konstrukte
 - Elemente sind Knoten und Kanten
 - Kanten können gerichtet sein

Ein Baum ist eine spezielle Form eines Graphen.
Um Knoten zu finden -> Auswertung der Beziehungen der Kanten
Knoten sind html-Seiten, Kanten sind Links <a href>

Indexierung in Goolge: Crawler analysiert HTML-Quelltext auf Links

Nachteil:
 - es kann Backlinks zur Seite geben (erkauft werden)
 - keine Aussage über Qualität der Beiträge von Websites

Page-Rank-Übung:
  Berechnung des Page-Ranks von verschiedenen Topologien von Linkanordnungen.

## K15 Probabilistisches Retrivalmodell (BIR)

Anwendungsfeld: SPAM-Erkennung bei Mails


Retrivalvorgang aus Benutzersicht:

1) Dokument-Retriavl mit Ranking
2) Nutzer betreibt Relevance Feedback
3) Relevanzurteil: relevant oder nicht relevant (binär betrachtbar {0,1})

+ solides theoretisches Modell, alle Ausnahmen können auf Konkretes abgebildet werden
+ gute Retrivalqualität
- bestimmte Anwendungen (z.B. SPAM) benötigen Trainingsdaten

Übung: Folie 40

## K16 Social Search

Motivaiton und Vorläufer:
 - traditionelle Suchmaschinen verursachen/liefern häufig schlechte Preciscion.

Frage: Wie sucht der Teilnehmer (Social-User)?

Neue Suchmöglichkeiten durch Social-Tagging:

1.) Anfragen wie bei Suchmaschinen
2.) Geteilte Bestände (Profile) bilden
3.) Tag Clouds: Größe der Wörter per Termgewichtung
4.) Kollaborative Filterung
5.) Community basierte Systeme (Daten und Trophäen -> Motivation für User schaffen)

## K17 Vergleich der Retrivalmodelle und Diskussion

Modelle:
  - boolesches Modell
  - Vektor-Modell
  - Fuzzy-Modell
  - Page-Rank-Modell
  - Probabilistisches-Modell
  - Social-Search

Fragen hierzu:
  - Welche Anwendungszenarien fallen Ihnen zu jedem Modell ein?
  - Wie skaliert jedes Modell bei großen Datenmengen?
  - Wie verhalten sich Recall und Precision bei den Modellen?
  - Inwiweit ist Ranking möglich?
  - Gibt es weitere Kriterien?

## K18 Kommerziell einsetzbare Retrivalsysteme

Dokumentenmanagement für Bürokontexte:
- Lösungen: Datev, Docuware, Keytech, Paperless, ...

Retrival: Zugriff aus dem Internet oft nicht möglich
Keine Taxonomie oder Verschlagworterung
Fazit: IR-Techniken - Modelle sind noch nicht richtig bei den Herstellern angekommen - keine formalen Standards.

Artefakte sind aber meist nur Texte, welche nicht Gegenstand der Inhaltserschließung und des Retrivals sind.

OpenSource: Apache Lucene (Volltextindexierung und Retrival für Server)

Moderne Erweiterung von Lucene: ELK (Elasticsearch-Logstash-Kibana-Stack)

 Elasticsearch (ES): Spezielle URL Steuerung für Indexaufbau
 Kibana: Analyse- und Visualiserungsplattform in Form eines browserbasierten Interfaces (Dashboards für ES)
 Logstash: Datenansamlungsengine zur Zusammenführung von Datn aus heterogenen Quellen.

## K19 Text und Webmining

Textmining ist die systematische Auswertung von DataMining.

Typische Anwendungen: SPAM-Filtering, Executive-Info-Systems, Sentiment-Analysen

technische Herausfoderungen der Big Data Epoche:
 - Skalierbarkeit (Nutzandbinung, Performance)
 - Datenmenge (Zwischenablage der Daten)
 - Alogrithmus (Zerlegung in Teilaufgaben) -> Map-Reduce

Unsupervised Learning: (User hat kein Vorwissen)
 - Clusteranalysen
 - Sentimentanalysen
 - Kollaborative Filterung

Supervised Learning: (User hat Wissen)
 - Gnerierung von Entscheidungsbäumen
 - Probalisitisches Retrival
 - Support-Vector
 - Evolutionäre Algos

-----------

## Rapid Miner

## Next Steps:
 - Übungsaufgaben
 - Skizzen
 - Übungsklausur
 - K17 Fragenstellungen beantworten

