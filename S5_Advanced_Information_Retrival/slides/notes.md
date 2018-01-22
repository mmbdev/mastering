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

## K3 Indexierungstechniken

  Indexieren-Verschlagwortung einer Dokumenten-Einheit durch Deskriptoren (Index-Terms)
  ST-Supplementary Terms CT-kontrollierten Vokabular
  Stoppworte: keine Betrachtung {ich, du, er, sie, es, der, die, das, ein, eine, einer}
  einfache Reduktionsverfahren: 
   - Ersetzen der Wortendungen durch Stammendungen
   - Verfahren mit Wortform-Wörterbuch

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



## K7
## K8
## K9
## K10
## K11
## K12
## K13
## K14
## K15
## K16
## K17
## K18
## K19