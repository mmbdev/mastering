#QRNM 2018 HS

Das Selbststudium besteht im Durcharbeiten des Textbuches Kronthaler, F. (2016), Statistik angewandt – Datenanalyse ist (k)eine Kunst mit dem R Commander, Berlin Heidelberg, Springer (nicht Kapitel 16, 20, 21, 22).

1.2 Warum Statistik Checkpoints
􏰌 - Wissen basiert auf Erfahrungen, Theorien und Daten, wobei der größte Teil unseres Wissens auf Daten beruht.
􏰌 - Daten werden manchmal eingesetzt, um uns zu manipulieren.
􏰌 - Fundierte Datenanalyse hilft uns, gute Entscheidungen zu treffen.

1.3. Daten Checkpoints

􏰌 - Ein Datensatz ist in Spalten und Zeilen organisiert. In den Zeilen sind die Untersuchungsobjekte enthalten, in den Spalten die Variablen.
􏰌 - Ein Datensatz ist in der Regel mit Hilfe von Zahlen aufgebaut. Es lässt sich so leichter rechnen.
􏰌 - Die Legende zum Datensatz sollte den Variablennamen, die Variablenbeschreibung, die Definition zu den Werten und Informationen zu fehlenden Werten sowie zur Skala enthalten.

1.6 Skalen:
nominal = 0,1  Mann, Frau -> dichotomen Variable oder einer Dummy-Variable

ordinal = Rangordnung 0-6, freundlich, unfreundlich, Technisch gesprochen ist in unserem Beispiel 1=1, 2=2, 3=3, 4=4 und 1>2>3>4. Die Abstände zwischen den Ausprägungen 1, 2, 3 und 4 sind nicht definiert.

metrisch ist neben der Unterscheidung und der Rangordnung zusätzlich noch der Abstand zwischen zwei Ausprägungen eindeutig definiert, z. B. Alter, X > Y > Z und X 􏰍 Y beziehungsweise Y 􏰍 Z ist klar definiert. Weitere Bsp.: Geld, Gewicht

1.6 Checkpoints
􏰌 - Nominale Variablen erlauben eine Unterscheidung der Untersuchungsobjekte.
􏰌 - Ordinale Variablen beinhalten neben einer Unterscheidung zusätzlich eine Rangordnung.
􏰌 - Metrische Variablen ermöglichen neben der Unterscheidung und der Rangordnung noch eine präzise Abstandsbestimmung.
 - Ordinale Daten können wie metrische Daten behandelt werden, wenn genügend Ausprägungen möglich und die Daten normalverteilt sind. Eleganter ist die Erzeugung einer quasi-metrischen Variable.
 - Das Skalenniveau bestimmt entscheidend darüber mit, welche statistischen Verfahren wir anwenden können.

 1.7 Software, Excel, SPSS, R

1.10 Anwendung:

1.1. Nenne drei Gründe, warum Statistik nützlich ist.
1.2. Welche Angaben sind in einem Datensatz enthalten?
1.3. Welche Skalenniveaus sind für die statistische Datenanalyse von Bedeutung und wie sind diese ausgestaltet?
1.4. Welches Skalenniveau besitzt die Variable Branche mit den Ausprägungen Industrieunternehmen und Dienstleistungsunternehmen, die Variable Selbsteinschätzung mit den Ausprägungen sehr erfahren, erfahren, wenig erfahren und nicht erfahren und die Variable Umsatz gemessen in Franken?
1.5. Welches Skalenniveau hat die Variable Bildung mit den Ausprägungen Sekundarschule, Matura, Fachhochschule, Universität, PhD bzw. die Variable Bildung gemessen in Jahren, die in einer Bildungsinstitution verbracht wurden?
1.6. Warum sind Skalenniveaus für die statistische Datenanalyse von Bedeutung?
1.7. Warum benötigen wir eine Legende für unsere Daten?
1.8. Öffne unseren Datensatz Daten_Wachstum und mache Dich mit ihm vertraut. Beantworte dabei folgende Fragen: Wie groß ist die Anzahl an Beobachtungen? Wie viele metrische, ordinale und nominale Variablen sind im Datensatz enthalten? Wie sind die metrischen, ordinalen und nominalen Daten gemessen?
1.9. Wie vertrauenswürdig ist unser Datensatz Daten_Wachstum?
1.10. Nenne jeweils eine vertrauenswürdige Datenquelle für dein Land, deinen Kontinent und die Welt?
1.11. Denke dir drei Fragestellungen aus, welche vermutlich mit Daten analysiert werden. Suche hierfür die geeigneten Datenquellen.

Im Kap. 3 befassen wir uns mit dem Durchschnitt, im Kap. 4 mit der Abweichung vom Durchschnitt und im Kap. 5 gehen wir noch einmal genauer auf unsere Beobachtungen ein und fragen uns, wie sich Gruppen von Beobachtungen verhalten. Anschließend betrachten wir in Kap. 6 den Zusammenhang zwischen Variablen und in Kap. 7 zeigen wir auf, wie aus vorhandenen Variablen neues Wissen erzeugt werden kann.

Kapitel 2 - Beschreiben (Deskriptive Statistik)

3.1 Mittelwerte
 - Ermitteln von Personen und Objekte Durschnittsverhalten

3.2 arithmetische Mittelwert 
metrische Daten voraussetzt, d. h. wir sollten ihn nur berechnen, wenn unser Skalenniveau metrisch ist.
  . Wachstumsrate in Prozent "Alle/Summe"
  . bei Klassen Kreuzprodukt "Anzahl der Objekte pro Klasse x Klassenmittelwert / 100"
  . reagiert empfindlich auf Ausreiser

3.3 Median
  . anwendbar bei ordinal, metrischen Werten
  . Werte aufsteigend sortieren, obere untere hälfte bilden -> Zwischenwert ist Median
  . robust bei Ausreiser

3.4 Modus
kann der Modus für metrische Daten, ordinale Daten und nominale Daten berechnet werden
 . interessant bei häufigeren Wertvorkommnissen (häufigster Wert ist Modus)
 . nominalen Daten ist er der einzige Mittelwert, der uns zur Verfügung steht. (ordinal und metrisch kann er ergänzend sein)
 . robust bei Ausreiser

3.5 geo Mittelwert und durchschnittliche Wachstumsrate
 . Wurzel aus Anzahl der Werte, die unter der Wurzel multipliziert werden

3.6 welchen Mittelwert?
 - entscheidend Skalenniveau der Variable
  nominal  -> Modus
  ordinal  -> Modus, Median
  metrisch -> Modus, Median, arithmetisches Mittel
  Wachstumraten -> geo Mittelwert

3.7 Checkwerte
􏰌 - Der Modus kommt bei nominalen Variablen zum Einsatz.
􏰌 - Bei ordinalen Variablen können wir sowohl den Modus als auch den Median berechnen.
􏰌 - Bei metrischen Variablen stehen uns der Modus, der Median und der arithmetische Mittelwert zur Verfügung.
􏰌 - Der arithmetische Mittelwert reagiert empfindlich auf Ausreißer, während der Modus und der Median für Extremwerte unempfindlich sind.
􏰌 - Seriös arbeitende Menschen geben an, welchen Mittelwert sie benutzt haben

3.8 R Mittelwerte
 - GUI: deskriptive Statistik -> Aktive Datenmatrix
 - arith. Mittel: 	mean(Daten_Wachstum$Wachstumsrate)
 - Median:			median(Daten_ Wachstum$Selbsteinschaetzung)
 - Modus:			table(Daten_Wachstum$Motiv)

Befehle: Funktion(Name_Datensatz$Variablenname)

attach(Name_Datensatz)
mean(Variablename)
median(Variablename)
table(Variablenamen)
detach(Name_Datensatz)

3.9 Anwendung
3.1. Welcher Mittelwert soll bei welchem Skalenniveau angewandt werden?
3.2. Berechne von Hand für die ersten sechs Unternehmen des Datensatzes Daten_ Wachstum den arithmetischen Mittelwert für die Variablen Produktverbesserung und Marketing und interpretiere die Ergebnisse.
3.3. Berechne von Hand für die ersten sechs Unternehmen des Datensatzes Daten_Wachstum den Median für die Variablen Selbsteinschätzung und Bildung und interpretiere die Ergebnisse.
3.4. Berechne von Hand für die ersten sechs Unternehmen des Datensatzes Daten_Wachstum den Modus für die Variablen Geschlecht und Erwartung und interpretiere die Ergebnisse.
3.5. Kann für die Variable Motiv der Median sinnvoll berechnet werden?
3.6. Berechne zu dem Datensatz Daten_Wachstum für alle Variablen die zugehörigen Mittelwerte mit Hilfe des R Commanders.
3.7. Unser drittes Unternehmen im Datensatz ist im ersten Jahr mit 16 %, im zweiten Jahr mit 11 %, im dritten Jahr mit 28 %, im vierten Jahr mit 13 % und im fünften Jahr mit 23 % gewachsen. Wie hoch ist durchschnittliche Wachstumsrate?
3.8. Welcher Mittelwert reagiert sensibel auf Ausreißer, welche beiden nicht und  warum?

4. Streuung: Die Abweichung vom durchschnittlichen Verhalten

4.1 Streuung – die Kehrseite des Mittelwertes
Die andere Seite der Medaille ist die Abweichung der einzelnen beobachteten Werte von ihrem Mittelwert. Wenn die einzelnen Werte näher am Mittelwert liegen, dann repräsentiert der Mittelwert die Werte besser, liegen sie weiter vom Mittelwert entfernt, ist der Mittelwert nicht mehr so aussagekräftig.

4.2 Spannweite
Die Spannweite ist der Abstand zwischen dem größtem und dem kleinsten Wert einer Variablen. (Bandbreite)
. anwendbar ordinale und metrische Werte
. reagiert extrem empfindlich auf Ausreiser, da nur kleinster und größter Wert betrachtet werden

4.3 Standardabweichung (S. 64-66)
ist die durchschnittliche Abweichung der einzelnen Beobachtungen vom Mittelwert.
. metrische Daten sind Vorraussetzung
. wir berechnen zunächst die Abweichungen der einzelnen Werte vom Mittelwert, quadrieren diese Abweichungen (damit sich negative und positive Abweichungen nicht auf null aufaddieren), teilen durch die Anzahl der Beobachtungen und ziehen anschließend die Wurzel.
. bereits in Klassen definiert:

4.4 Der Variationskoeffizient
Der Variationskoeffizient kommt zum Einsatz, wenn wir die Streuung zweier Variablen vergleichen wollen, d. h., wenn wir uns fragen, welche Variable die größere Streuung aufweist. Er misst die Abweichung relativ, in Prozent vom Mittelwert.

-> zeigt für die Variablen die Repräsentationskraft auf die Personen oder Objekte

4.5 Der Quartilsabstand (S. 69)
Der Quartilsabstand kommt sowohl bei metrischen Daten als auch bei ordinalen Daten zum Einsatz. Er gibt uns wieder, in welcher Bandbreite sich die mittleren 50 % der Werte bewegen.

 . Werte, wie beim Median aufsteigend sortieren
 . der Quartilsabstand ist derjenige Wert, der wiedergibt, in welcher Bandbreite sich die vier mittleren Unternehmen/Werte bewegen.

nominale Skaalen besitzen kein Streuungsmaß, da Sie sich nicht um andere Werte teilen oder Zwischenwerte besitzen. 

4.6 Boxplott
Der Boxplot vereinigt die Informationen zum Median, zum 1. und 3. Quartil sowie zum Minimalwert und zum Maximalwert. Der Boxplot ist daher ein beliebtes Instrument zur grafischen Analyse der Streuung von ordinalen und metrischen Variablen.

4.7 Checkpoints
􏰌 - Streuungsmaße ergänzen unsere Information zum Mittelwert, je kleiner die Streuung, desto aussagekräftiger ist der Mittelwert.
 - Die Spannweite ist die Differenz zwischen Maximum und Minimum einer Variablen, sie reagiert sehr empfindlich auf Ausreißer.
􏰌 - Die Standardabweichung ist die durchschnittliche Abweichung aller Werte vom Mittelwert. Die Varianz ist die quadrierte Standardabweichung. Bei metrischen Variablen können beide Werte sinnvoll berechnet werden.
􏰌 - Der Quartilsabstand gibt uns die Bandbreite an, in der sich die mittleren 50 % der Werte bewegen. Er kann sowohl bei metrischen als auch bei ordinalen Daten verwendet werden.
􏰌 - Der Variationskoeffizient wird bei metrischen Daten angewandt, um zu analysieren, bei welcher Variable die Streuung größer ist.
􏰌 Der Boxplot ist ein grafisches Instrument zur Analyse der Streuung.

4.8 Berechnung der Streuungsmaße mit dem R Commander
GUI -> Deskriptive Statistik -> Zusammenfassung Nummerischer Variablen -> Variablename -> Standardabweichung, Interquartilsabstand, Variationskoeffizent, Typ2, Quantile 0, .25, .5, .75, 1

attach(Datensatz)
min(Variablenname)
max(Variablenname)

sd(Variablenname)
var(Variablenname)
IQR (Variablenname)
detach(Datensatz)

4.9 Erstellen des Boxplots mit dem R Commander

GUI -> Grafiken -> Boxplott -> Variablenname
attach(Datensatz)
Boxplot(Variablenname)
detach(Datensatz)

4.10 Anwendung
4.1. Welches Streuungsmaß ist bei welchem Skalenniveau sinnvoll einsetzbar?
4.2. Kann bei nominalen Daten ein Streuungsmaß berechnet werden, warum oder warum nicht?
4.3. Berechne für die ersten acht Unternehmen unseres Datensatzes Daten_Wachstum von Hand die Spannweite, die Varianz, die Standardabweichung, den Quartilsabstand und den Variationskoeffizienten für die Variable Marketing und interpretiere das Ergebnis.
4.4. Berechne für die ersten acht Unternehmen unseres Datensatzes Daten_Wachstum von Hand die Spannweite, die Varianz, die Standardabweichung, den Quartilsabstand und den Variationskoeffizienten für die Variable Produktverbesserung und interpretiere das Ergebnis.
4.5. Welche Variable streut stärker, Marketing oder Produktverbesserung (Anwendung 4.3 & 4.4)? Welches Streuungsmaß nutzt man, um die Frage zu beantworten?
4.6. Berechne für unseren Datensatz Daten_Wachstum für alle Variablen die kleinsten Werte, die größten Werte, den Quartilsabstand und die Standardabweichung mit Hilfe des R Commanders (wenn sinnvoll). Erstelle zudem die zugehörigen Boxplots.

5. Grafiken: Die Möglichkeit Daten visuell darzustellen

5.1 Grafiken: Warum benötigen wir Grafiken?
Grafiken helfen uns, Zahlen zu vermitteln und schaffen bleibende Eindrücke.
Ein anderer Grund ist, dass uns Grafiken oft Hinweise auf das Verhalten unserer untersuchten Personen oder Objekte geben -> Häufigkeitsdarstellungen

5.2 Die Häufigkeitstabelle
- nominale und ordinale Daten können direkt in einer Tabelle angegeben werden, da normalerweise nur wenige Werte vorhanden sind
- metrisch skalierten Daten haben wir in der Regel sehr viele unterschiedliche Werte, die wir erst in Klassen einteilen müssen

5.3 Das Häufigkeitsdiagramm
drei Möglichkeiten: 
- absolute Häufigkeitsdarstellung (Anzahl y-Achse: metrisch, x-Achse: Klassen oder nominal, ordinal) (Höhe der Balken)
- relative Häufigkeitsdarstellung (Prozent y-Achse: metrisch, x-Achse: Klassen oder nominal, ordinal) (Fläche der Balken)
- Histogramm, bei unterschiedlichen Klassenbreiten, da sonst bei Häufigkeitsdarstellung das Bild verzerrt ist

Kreis: mehrere Personen und Objekte mit bestimmter Ausprägung zu etwas
Säulen: vergleich von zwei oder mehr Gruppen zu einer Ausprägung
Linien: Auskunft über einen Verlauf von Werten von mehreren Gruppen

5.6 Checkpoints

- Die grafische Darstellung von Daten hilft uns Sachverhalte zu erläutern.
􏰌-  Die grafische Darstellung von Daten gibt uns oft Hinweise auf das Verhalten von Personen oder Objekte.
􏰌- Häufigkeitsdarstellungen benutzen wir, um zu erfahren, wie oft bestimmte Werte vorkommen.
􏰌- Die Häufigkeitstabelle gibt uns Auskunft darüber, wie oft bestimmte Werte absolut und relativ vorkommen.
􏰌- Grafisch können wir die Häufigkeitsverteilung absolut, relativ oder mit dem Histogramm darstellen.
􏰌- Wenn wir gleiche Klassenbreiten haben, ist die absolute oder relative Häufigkeitsdarstellung vorzuziehen, bei unterschiedlichen Klassenbreiten das Histogramm.
􏰌- Eine gute Grafik ist möglichst einfach und stellt Informationen klar dar.

5.7 Erstellung von Häufigkeitsdiagrammen mit dem R-Commander

Grafiken -> Histogramm -> Häufigkeitsdiagramm

hist(Wachstumsrate, freq = FALSE)

5.8 Anwendung

5.1. Berechne die durchschnittliche Wachstumsrate der Unternehmen aus Abb. 5.6 und vergleiche diese mit den jeweiligen Wachstumsraten aus unserem Datensatz Daten_Wachstum.
5.2. Nenne zwei Gründe dafür, dass Grafiken hilfreich sind.
5.3. Zu welchem Zweck benötigen wir Häufigkeitsdarstellungen?
5.4. Ist bei unterschiedlichen Klassenbreiten die absolute Häufigkeitsdarstellung, die re-
lative Häufigkeitsdarstellung oder das Histogramm vorzuziehen? Warum?
5.5. Erstelle für die Variable Erwartung für die ersten sechs Unternehmen unseres Datensatzes Daten_Wachstum die Häufigkeitstabelle, die absolute und relative Häufigkeitsdarstellung von Hand und interpretiere das Ergebnis.
5.6. Erstelle für unseren Datensatz Daten_Wachstum für die Variablen Marketing und Produktverbesserung die relative Häufigkeitsdarstellung mit dem R Commander und interpretiere das Ergebnis.
5.7. Ist eher die Variable Marketing oder eher die Variable Produktverbesserung symmetrisch? Warum?
5.8. Erstelle für die Wachstumsrate die relative Häufigkeitsdarstellung und das Histogramm mit folgenden Klassenbreiten: 􏰍10 bis 􏰍5, 􏰍5 bis 0, 0 bis 5 und 5 bis 25. Zeichne die Darstellungen mit der Hand. Was fällt Dir auf? Welche Darstellung ist vorzuziehen und warum?

6 Korrelation: vom Zusammenhang

6.1 Korrelation – das gemeinsame Bewegen zweier Variablen

Die Korrelation oder die Zusammenhangsberechnung ist neben den Mittelwerten und der Streuung ein weiteres zentrales Konzept der Statistik. Hier fragen wir nach einem Zusammenhang zwischen zwei Variablen.
Die Korrelation gibt uns keine Aussage über die Richtung des Zusammenhanges, über die Kausalität.
Korrelationen können positiv oder negativ sein. 
positiv bedeutet, dass sich zwei Variablen in die gleiche Richtung bewegen. Wird der Wert einer Variable größer, dann auch der Wert der anderen Variable und umgekehrt. Negativ bedeutet, dass sich zwei Variablen in die entgegengesetzte Richtung bewegen. 	

-> Maß ist der Korrelationskoeffizienten

Zur Anwendung. Bei 

 . metrischen Daten = Bravais-Pearson (die Stärke des linearen Zusammenhanges zwischen zwei metrischen Variablen zu ermitteln)
   wir berechnen den Korrelationskoeffizienten von Bravais-Pearson aus den Abweichungen der beobachteten Werte von ihrem Mittelwert
 . ordinalen Daten = Spearman
 . nominalen Daten = Vierfelderkoeffizient oder der Kontingenzkoeffizient

6.2 Der Korrelationskoeffizient von Bravais-Pearson für metrische Variablen

 . Korrelationskoeffizient von Bravais-Pearson im Bereich von 􏰍-1 <􏰋 r <􏰋 1 definiert
 . -1 bedeutet, dass wir eine perfekte negative Korrelation haben, 1 bedeutet eine perfekte positive Korrelation.
 . Werte dawzsichen, s. Tabelle S. 76

6.3 Streudiagramm zur Darstellung

 . gerade Linie zwischen Werte einzeichnen, erkennen wir die Stärke des linearen Zusammenhangs bzw. wie stark sich die Variablen gemeinsam bewegen
 . Punkte nahe an der Geraden, dann starke Korrelation
 . Streuen die Punkte, wie im folgenden Fall konstruiert, weiträumig um die Gerade, handelt es sich um einen schwachen Zusammenhang
 . steigt die Gerade ist die Korrelation positiv, fällt sie -> negativ
 . Streudiagramm zeigt an, ob überhaupt ein linearer Zusammenhang zwischen den Variablen besteht, gerade Linie durch die Punkte gelegt werden kann

6.4 Der Korrelationskoeffizient von Spearman für ordinale Variablen

 . metrischer Daten ordinale Daten vor, benutzen wir den Rangkorrelationskoeffizienten von Spearman
 . jeweiligen Variable einen Rang geben, bei gleicher Anzahl nächster Rang und dann die Hälfte 1,5, 3.5, 5.5 vergeben
 . größte Variable erster Rang

6.5 Der Vierfelderkoeffizient für nominale Variablen mit zwei Ausprägungen

 . nominale Variablen mit nur zwei Ausprägungen, z. B. die Variable Geschlecht mit den Ausprägungen Mann oder Frau bzw. 0 und 1, so lässt sich die Korrelation mit Hilfe des Vierfelderkoeffizienten berechnen
 . ist ebenfalls zwischen 􏰍1 und 1 definiert
 . mittlerer Zusammenhang zwischen den Variablen, keine Richtung angegeben

6.6 Der Kontingenzkoeffizient für nominale Variablen (S.99)

 . für nominale Daten mit mehreren Ausprägungen
 . ist definiert von 0 < C

6.7 Korrelation, Kausalität, Drittvariablen, und weitere Korrelationskoeffizienten

 . Kausalität -> wie beeinflussen sich die Varibalen gegenseitig
 . Korrelation sagt nichts über Kausalität aus
 . Korrelationskoeffizienten und Skalenniveau der Variablen (s. Tabelle 6.8, S. 104)

6.8 Checkpoints
􏰌 
 - Korrelationen geben Auskunft darüber, ob es einen Zusammenhang zwischen zwei Variablen gibt, sie sagen nichts über Kausalität aus.
􏰌 -  Es kann sein, dass gefundene Korrelationen auf den Einfluss von Drittvariablen zurückzuführen sind. Korrelationen müssen theoretisch begründbar sein.
 􏰌-  Der Korrelationskoeffizient von Bravais-Pearson ist dazu geeignet, den linearen Zusammenhang zwischen zwei metrischen Variablen zu berechnen.
 􏰌- Vor der Berechnung des Korrelationskoeffizienten von Bravais-Pearson sollte das Streudiagramm gezeichnet werden, um zu überprüfen, ob ein linearer Zusammenhang existiert.
􏰌 - Der Korrelationskoeffizient von Spearman wird benutzt, um den Zusammenhang zwischen zwei ordinalen Variablen zu berechnen.
􏰌 - Soll die Korrelation zwischen zwei nominalen Variablen berechnet werden, so ist der Vierfelderkoeffizient oder der Kontingenzkoeffizient zu verwenden.
􏰌 - Für die Berechnung von Korrelationen zwischen Variablen mit unterschiedlichen Skalenniveaus stehen weitere spezialisierte Korrelationskoeffizienten zur Verfügung.

6.9 Berechnung der Korrelationskoeffizienten mit dem R Commander

Menüpunkt Statistik mit dem Untermenü Deskriptive Statistik und dem Befehl Korrelationsmatrix. Im sich öffnenden Fenster werden die Variablen ausgewählt, für die die Korrelation berech- net werden soll. Um mehrere Variablen auszuwählen, verwenden wir die Steuerungstaste zusammen mit der Maus. Wir können auch mehr als zwei Variablen auswählen. Zudem spezifizieren wir noch den Korrelationskoeffizienten. Anschließend bestätigen wir mit OK und im Ergebnis erscheint eine Matrix mit den Korrelationskoeffizienten.

cor(Variablenname_1, Variablenna- me_2, method=„pearson“)
cor(Variablenname_1, Variablenname_2, method=„spearman“)

Grafiken -> Streudiagramm -> Variablen ausählen

alle nominalen Varibalen anpassen, da R default-mäßig von metrisch ausgeht:
Datenmanagement -> Untermenü Variablen bearbeiten -> Konvertiere numerische Variablen in Faktoren

6.10 Anwendung
6.1. Welcher Korrelationskoeffizient ist bei welchen Skalenniveaus zu benutzen?
6.2. Warum sind theoretische Überlegungen notwendig, bevor eine Korrelation zwischen
zwei Variablen berechnet wird?
6.3. Warum sagt ein Korrelationskoeffizient nichts über Kausalität aus?
6.4. Betrachte die folgenden drei Streudiagramme (nach Anscombe 1973). In welchem
der Fälle kann der Korrelationskoeffizient von Bravais-Pearson ohne Probleme be- rechnet werden? Warum, warum nicht?
   xi xi xi
6.5. Zeichne und berechne für die ersten acht Unternehmen unseres Datensatzes Daten_Wachstum von Hand das Streudiagramm und den Korrelationskoeffizienten für die Variable Wachstumsrate und Marketing und interpretiere das Ergebnis.
6.6. Zeichne und berechne mit Hilfe des R Commanders für unseren Datensatz Daten_Wachstum für die Variablenpaare Wachstumsrate und Marketing, Wachstumsrate und Produktverbesserung, Wachstumsrate und Erfahrung sowie Wachstumsrate und Alter das Streudiagramm und den Korrelationskoeffizienten von Bravais und Pearson und interpretiere das Ergebnis.
6.7. Berechne für die ersten zehn Unternehmen unseres Datensatzes Daten_Wachstum von Hand den Rangkorrelationskoeffizienten von Spearman für die Variablen Wachstumsrate und Selbsteinschätzung und interpretiere das Ergebnis.
6.8. Berechne mit Hilfe des R Commanders den Rangkorrelationskoeffizienten von Spearman für die Variablen Wachstumsrate und Selbsteinschätzung unseres Datensatzes Daten_Wachstum und interpretiere das Ergebnis.
6.9. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Geschlecht und Branche den Vierfelderkoeffizienten und interpretiere das Ergebnis.
6.10. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Geschlecht und Gründungsmotiv den Kontingenzkoeffizienten und interpretiere das Ergebnis.


7. Verhältniszahlen: Die Chance, Neues aus altem Wissen zu erzeugen

 - Verhältniszahlen sind Quotienten aus zwei Zahlen. Mit ihnen können wir Personen und andere Untersuchungsobjekte inhaltlich, räumlich oder zeitlich vergleichen.
 - Unterscheidung von Beziehungszahlen, Gliederungszahlen und Messzahlen

7.1 Die Beziehungszahl – der Quotient aus zwei unterschiedlichen Größen

 - Eine Beziehungszahl wird gebildet, wenn wir zwei unterschiedliche Größen zueinander in Beziehung setzen
 (bekanntesten Beziehungszahlen ist vermutlich das Bruttoinlandsprodukt pro Kopf)

7.2 Die Gliederungszahl – der Quotient aus einer Teilzahl und einer Gesamtzahl

 - Eine Gliederungszahl bilden wir, wenn wir eine Teilgröße zur Gesamtgröße in Beziehung setzen
 - In der Regel multiplizieren wir die Zahl noch mit 100 und wir erhalten die Prozent, die die Teilmasse an der Gesamtmasse ausmacht
 (Exportquote eines Unternehmens, Exportumsatz zum Gesamtumsatz)

7.3 Die dynamische Messzahl

 - Verhältniszahl wollen wir noch kurz auf die dynamische Messzahl eingehen. Diese nutzen wir, um Entwicklungen im Zeitablauf anzusehen und miteinander zu vergleichen
 - multiplizieren wir in der Regel mit 100 und erhalten die Veränderung zu einem Basiszeitpunkt, den wir gewählt haben, in Prozent

 7.4 Checkpoints
􏰌 - Verhältniszahlen setzen zwei Größen zueinander in Beziehung. Wir können damit aus vorhandenen Daten neues Wissen generieren.
􏰌 - Beziehungszahlen setzen unterschiedliche Größen zueinander in Beziehung.
􏰌 - Gliederungszahlen setzen Teilgrößen in Relation zu einer Gesamtgröße.
􏰌 - Dynamische Messzahlen können wir nutzen, um die Entwicklung einer Größe über die Zeit zu analysieren.

7.5 Anwendung (S. 119)
 - Finde drei Sachverhalte, die mit Hilfe einer Beziehungszahl analysiert werden können.
 - Finde drei Sachverhalte, die mit Hilfe einer Gliederungszahl analysiert werden können.
 - Finde drei Sachverhalte, die mit Hilfe einer dynamischen Messzahl analysiert werden können.
 - Analysiere die Entwicklung des Bruttoinlandsproduktes pro Kopf für die folgenden Länder. Benutze als Basisjahr das Jahr 2003.

Von Wenigen zu Allen oder von der Stichprobe zur Grundgesamtheit

8. Von Daten und der Wahrheit

8.1 Wie kommen wir zu unseren Daten oder: Primär- oder Sekundärdaten?

Am Anfang steht daher immer ein Problem bzw. eine Fragestellung. Wir wollen etwas wissen, zum Beispiel:

􏰌 Wie hoch ist die durchschnittliche Wachstumsrate von neu gegründeten Unternehmen?
􏰌 Wie hoch ist das durchschnittliche Alter von Unternehmensgründern?
􏰌 Gründen mehr Frauen oder mehr Männer ein Unternehmen?
􏰌 Gibt es einen Zusammenhang zwischen Marketingaktivitäten und dem Wachstum neu gegründeter Unternehmen?
 Wie viel Gramm Fleisch enthält ein Cheeseburger von McBurger?

8.2 Die Zufallsstichprobe – Der beste Schätzer für unsere Grundgesamtheit

Besitzt jedes Element der Grundgesamtheit dieselbe Wahrscheinlichkeit, in die Stichprobe aufgenommen zu werden, dann ist unsere Stichprobe repräsentativ für die Grundgesamtheit und die erhaltenen Werte der Stichprobe, z. B. die Stichprobenmittelwerte, sind die besten Schätzer, die wir für die Grundgesamtheit haben.

8.3 Von der Wahrheit

 - Proxy ist der technische Ausdruck für eine Variable, welche uns näherungsweise über den Gegenstand, an dem wir interessiert sind, Auskunft gibt. 
 - International wird zum Beispiel auch der Human Development Indikator verwendet.
 - Mit Blick auf unsere Untersuchung bedeutet dass, das wir zunächst für Validität sorgen müssen und dann für Reliabilität.


8.4 Checkpoints
􏰌 - Am Anfang der Datenerhebung und Datenanalyse steht die eindeutige Definition der Problemstellung bzw. der Fragestellung.
􏰌 - Bevor eine Primärdatenerhebung durchgeführt wird, sollten wir prüfen, ob die benötigten Daten bzw. brauchbare Daten bereits vorliegen.
􏰌 - Die Grundgesamtheit sind alle Personen oder Objekte, über die wir eine Aussage machen wollen.
􏰌 - Repräsentativität der Stichprobe erreichen wir durch eine Zufallsziehung der Elemente oder Objekte aus der Grundgesamtheit.
􏰌 - Die Stichprobenwerte einer repräsentativen Stichprobe sind der beste Schätzer für die Grundgesamtheit.
􏰌 - Das Konfidenzintervall präzisiert die Punktschätzung, indem zusätzlich noch ein Intervall angegeben wird.
􏰌 - Die Stichprobengröße errechnet sich aus der Breite des Konfidenzintervalls, der Standardabweichung in der Grundgesamtheit und des definierten Vertrauensbereichs.
􏰌 - Validität einer Variable bedeutet, dass die Variable ein guter Proxy für den Gegenstand des Interesses ist.
􏰌 - Reliabilität bedeutet, dass wir die wahren Werte für die Stichprobe erhoben und zuverlässig gemessen haben.


8.5 Anwendung
8.1. Welche Schritte und welche Reihenfolge der Schritte müssen wir bei der Datenerhebung beachten?
8.2. Suche die aktuellen Daten zur Zahl der Einwohner in den Ländern der Welt im Internet. Wie viel Einwohner haben China, Indien, die Schweiz, Deutschland und die USA aktuell?
8.3. Erkläre, was die Grundgesamtheit ist, was eine Stichprobe ist und welche Eigenschaft erfüllt sein muss, damit wir von der Stichprobe auf die Grundgesamtheit schließen können.
8.4. Wie hoch ist die Wachstumsrate der Unternehmen im Durchschnitt und wie groß ist das 90-, das 95- und das 99 %-Konfidenzintervall?
8.5. Berechne die benötigte Stichprobengröße, wenn wir die durchschnittliche Wachstumsrate der Unternehmen mit einer 95 % Sicherheit schätzen wollen und die Konfidenzintervallbreite nicht größer als 2 Prozentpunkte sein soll. Aus Voruntersuchungen wissen wir, dass die Standardabweichung in der Grundgesamtheit circa 5 Prozentpunkte beträgt.
8.6. Wie viele Prozent der Unternehmensgründungen in unserem Datensatz Daten_ Wachstum sind Industrieunternehmen und wie groß ist das 90-, das 95- und das 99 %-Konfidenzintervall?
8.7. Wie groß müsste die Stichprobe sein, wenn wir den Anteil der Industriegründungen in der Grundgesamtheit mit einer 90 % Sicherheit in einer Konfidenzintervallbreite von 8 Prozentpunkten schätzen wollen. Aus Vorüberlegungen wissen wir, dass der Anteil der Industriegründungen an den Unternehmensgründungen circa bei 25 Prozent liegt.
8.8. Was bedeutet Validität und Reliabilität?
8.9. Welche der beiden Aussagen ist korrekt: 1) Reliabilität ist möglich, ohne dass Validität erreicht wird oder 2) Validität ist möglich, ohne dass Reliabilität erzeugt wird. Erkläre kurz.
8.10. Suche den Artikel von Costin, F., Greenough, W.T. & R.J. Menges (1971): Student Ratings of College Teaching: Reliability, Validity, and Usefulness, Review of Educational Research 41(5), pp. 511–535 und erörtere, wie in diesem Artikel die Konzepte Validität und Reliabilität diskutiert werden.

9. Hypothesen: Nur eine Präzisierung der Frage

9.1 Das kleine, große Ding der (Forschungs-)Hypothese

Hypothese = ist es nur eine Übersetzung der Fragestellung in eine testbare Aussage.
Eine Hypothese ist eine mit Hilfe der Theorie und Vorkenntnissen formulierte testbare Aussage. Im Forschungsprozess können wir die Hypothese auch als Forschungshypothese bezeichnen.

9.2 Die Nullhypothese H0 und die Alternativhypothese HA

Im Forschungsprozess verwendet man zwei unterschiedliche Arten von Hypothesen, die Nullhypothese und die Alternativhypothese. Die Nullhypothese ist dabei immer die testbare Aussage, die Alternativhypothese ist immer das Gegenteil der Nullhypothese.

präzises testbares Bsp.:
H0: Es gibt keinen Zusammenhang zwischen dem Anteil am Umsatz, den junge Unternehmen für Marketing aufwenden und dem Anteil am Umsatz, den junge Unternehmen für Produktverbesserung aufwenden.
HA: Es gibt einen Zusammenhang zwischen dem Anteil am Umsatz, den junge Unternehmen für Marketing aufwenden und dem Anteil am Umsatz, den junge Unternehmen für Produktverbesserung aufwenden.

9.3 Hypothesen, ungerichtet oder gerichtet?

Die Nullhypothese und die Alternativhypothese können wir ungerichtet oder gerichtet formulieren.
 -> abhängig vom Wissen über den Forschungsgegenstand
 -> gerichtet -> hinzufügen, ob die Korrelation positiv oder negativ ist

H0: Unternehmensgründerinnen sind bei Gründung jünger oder gleich alt wie Unternehmensgründer.
HA: Unternehmensgründerinnen sind bei Gründung älter als Unternehmensgründer.

H0: Es gibt keinen bzw. einen positiven Zusammenhang zwischen dem Anteil am Umsatz, den junge Unternehmen für Marketing aufwenden und dem Anteil am Umsatz, den junge Unternehmen für Produktverbesserung aufwenden.
HA: Es gibt einen negativen Zusammenhang zwischen dem Anteil am Umsatz, den junge Unternehmen für Marketing aufwenden und dem Anteil am Umsatz, den junge Unternehmen für Produktverbesserung aufwenden.

9.4 Was macht eine gute Hypothese aus?

 - Sie sollte eine direkte Erweiterung der Forschungsfrage sein
 - Hypothesen müssen immer in Bezug zur Problemstellung bzw. Fragestellung stehen
 - mit deren Hilfe wollen wir die Problemstellung lösen bzw. Antworten auf unsere Frage finden
 - Sie muss als Aussage, nicht als Fragestellung formuliert werden (Fragestellungen sind nicht überprüfbar, klare, präzise Aussagen hingegen schon)
 - eine gute Hypothese reflektiert die existierende Literatur und Theorie
 - eine Hypo muss kurz und aussagekräftig sein, ohne Aussage keine Überprüfung möglich

9.5 Checkpoints
􏰌 - Eine Hypothese ist eine Aussage über einen Gegenstand basierend auf der Theorie oder auf Erfahrung.
􏰌 - Im Forschungsprozess unterscheiden wir zwischen Nullhypothese H0 und Alternativ- hypothese HA. Die Nullhypothese ist die testbare Aussage, die Alternativhypothese ist immer das Gegenteil zur Nullhypothese.
􏰌 - Wir können unsere Hypothesen ungerichtet und gerichtet formulieren. Die Formulierung einer gerichteten Hypothese setzt einen höheren Kenntnisstand voraus als die Formulierung einer ungerichteten Hypothese.
 - Eine gute Hypothese erfüllt folgende Kriterien: Sie ist eine direkte Erweiterung der Fragestellung, ist als Aussage formuliert, reflektiert die existierende Literatur und sie ist kurz und bündig sowie testbar.

9.6 Anwendung
9.1. Formuliere für folgende Forschungsfragen die ungerichteten Null- und Alternativhypothesen.
􏰌 Gibt es einen Zusammenhang zwischen dem Umsatzwachstum eines neu gegründeten Unternehmens und dem Anteil am Umsatz der für Produktverbesserung aufgewendet wird?
􏰌 Gibt es einen Unterschied in der Branchenberufserfahrung zwischen Gründern und Gründerinnen, welchen diese bei Gründung mitbringen?
􏰌 Gibt es einen Zusammenhang zwischen Rauchen und Lebenserwartung?
9.2. Formuliere für obige Forschungsfragen jeweils eine gerichtete Null- und Alternativhypothese.
9.3. Geh in die Bibliothek und suche drei Fachartikel (welche Daten beinhalten) aus deinem Fachbereich. Beantworte für jeden Fachartikel folgende Fragen: Wie ist die vollständige Zitierweise? Was ist die Fragestellung des Artikels? Wie lautet die Forschungshypothese? Ist diese explizit formuliert? Was ist die Nullhypothese? Ist diese explizit formuliert? Formuliere zudem für diejenigen Artikel, in denen die Hypothese nicht explizit formuliert ist, die Forschungshypothese.
9.4. Evaluiere die Hypothesen, die du in Aufgabe 3 gefunden hast, mit Blick auf die fünf Kriterien, die eine gute Hypothese erfüllen sollte.
9.5. Warum nimmt die Nullhypothese in der Regel keine Beziehung zwischen den Variablen bzw. keinen Unterschied zwischen Gruppen an?
9.6. Bei Interesse lese die Erzählung „Die Waage der Baleks“ von Heinrich Böll und formuliere zur Geschichte mit Blick auf die Waage eine Hypothese. Denke darüber nach, wie der Junge seine Vermutung testet.

10. Normalverteilung und andere Testverteilungen

Wir werden sehen, dass der Zufall normal-, aber auch anders verteilt sein kann. Das bedeutet ganz konkret, wir können eine Aussage darüber treffen, wie zufällig der Zufall eintritt. Interessant, nicht? Im Folgenden setzen wir uns mit der Verteilung des Zufalls auseinander. Wir werden sehen, dass die Normalverteilung eine nicht ganz unbedeutende Testverteilung beim Hypothesentest ist.

10.1 Die Normalverteilung
Interessant weil:
 - Erstens sind in der Realität viele Variablen zumindest näherungsweise normalverteilt.
 - Zweitens ermöglicht uns die Normalverteilung einen intuitiven Zugang zur Verteilung des Zufalls

Definition Normalverteilung:
 - Die Normalverteilung ist glockenförmig, mit einem Maximum. 
 - Um das Maximum herum ist sie symmetrisch. Ihre Enden laufen asymptotisch auf die x-Achse zu
 - Das Maximum der Normalverteilung liegt in der Mitte der Kurve
 - bei Normalverteilung fallen der arithmetische Mittelwert, der Median und der Modus zusammen
 - Asymptotisch bedeutet, dass sich die Enden immer mehr der x-Achse annähern, diese aber nie erreichen
 - Die Fläche unter der Normalverteilungskurve gibt an, wie wahrscheinlich es ist, dass ein bestimmter Wert einer normalverteilten Variable innerhalb eines Intervalls auftritt.

Daraus ergibt sich, dass das Aussehen unserer Normalverteilung nur von zwei Parametern abhängt, dem Mittelwert und der Standardabweichung. Mit diesen zwei Werten können wir eine Normalverteilung eindeutig definieren.

Konkret führt eine Vergrößerung des Mittelwertes zu einer Rechtsverschiebung der Normalverteilungskurve und eine Vergrößerung der Standardabweichung zu einer Verbreiterung dieser. Da sowohl der Mittelwert als auch die Standardabweichung theoretisch jeden möglichen Wert annehmen können, gibt es nicht nur eine Normalverteilung, sondern unendlich viele.

10.2 Der z-Wert und die Standardnormalverteilung

Wir können aber jede dieser Normalverteilungen mit einer einfachen Transformation standardisieren, so dass sie einen Mittelwert von 0 und eine Standardabweichung von 1 haben.

z ist gleich der standardisierte Wert (kurz z-Wert), x ist der zu standardisierende Wert der Verteilung,

s. S. 147

N(0, 1) = Standardnormalverteilung nach der Transformation

 - Der z-Wert repräsentiert immer einen x-Wert einer beliebigen Normalverteilung
 - Mit seiner Hilfe können wir für jede beliebige Normalverteilung bestimmen, wie wahrscheinlich das Auftreten ei-
nes bestimmten x-Wertes ist.
 - Zu jeder beliebigen Fläche der Standardnormalverteilung gehört automatisch ein bestimmter z-Wert. Mit Hilfe des z-Wertes können wir also die Fläche unter der Standardnormalverteilung bestimmen.
- wie wir im folgenden Kapitel sehen werden, ist der z-Wert für den Hypothesentest außerordentlich wichtig. Mit seiner Hilfe können wir, bei Normalverteilung einer Variable, aussagen, wie wahrscheinlich oder unwahrscheinlich das Auftreten eines bestimmten x-Wertes ist und (wie wir im nächsten Kapitel sehen werden) Hypothesen ablehnen oder nicht ablehnen.

10.3 Normalverteilung, t-Verteilung, 􏰅2-Verteilung und (oder doch lieber) F-Verteilung

Variablen sind aber nicht nur normalverteilt, sondern können auch anders verteilt sein. An dieser Stelle wollen wir daher noch drei weitere wichtige Verteilungen, die wir zum Testen benötigen vorstellen: die t-Verteilung, die 􏰅2-Verteilung (gesprochen Chi-Quadrat-Verteilung) und die F-Verteilung. Auch bei diesen Tests sind die Flächen tabelliert.

t-Verteilung:
Die t-Verteilung zeigt sich wie die Standardnormalverteilung symmetrisch mit einem Maximum, einem Mittelwert von null und asymptotisch gegen die x-Achse zulaufenden Enden. Sie ist aber etwas breiter und flacher, wie breit und wie flach, hängt von der Anzahl der Freiheitsgrade (Fg) ab. Haben wir wenige Freiheitsgrade, ist die t-Verteilung flacher und breiter, haben wir mehr Freiheitsgrade, wird sie enger und spitzer. Ab circa 30 Freiheitsgraden geht die t-Verteilung in die Standardnormalverteilung über. 
t-Verteilung in der praktischen Arbeit vor allem dann benötigen, wenn wir es mit kleinen Stichproben zu tun haben.

x2-Verteilung
Neben der t-Verteilung stellt die 􏰅x2-Verteilung eine weitere wichtige Testverteilung dar. Wir benötigen sie insbesondere beim Testen von nominalen Variablen. Wie bei der t-Verteilung gibt es nicht nur eine 􏰅2-Verteilung, sondern viele 􏰅x2-Verteilungen, deren Aussehen von der Anzahl der Freiheitsgrade abhängt.

F-Vertielung
Die letzte Verteilung, die wir uns noch kurz ansehen wollen, ist die F-Verteilung. Wir benötigen diese insbesondere beim Testen von Regressionsrechnungen. Wie bereits bei der t-Verteilung und der 􏰅2-Verteilung gibt es nicht nur eine F-Verteilung, sondern viele F-Verteilungen, die von der Anzahl an Freiheitsgraden abhängen. Der Unterschied ist lediglich, dass wir für die Freiheitsgrade nicht nur einen Wert, sondern zwei Werte haben.

10.4 Checkpoints
􏰌 - Die Normalverteilung ist glockenförmig, symmetrisch mit einem Maximum und ihre Enden laufen asymptotisch auf die x-Achse zu.
􏰌 - Die Fläche unter der Normalverteilung gibt an, wie groß die Wahrscheinlichkeit ist, einen bestimmten Wert in einem bestimmten Intervall zu finden.
􏰌 - Mit Hilfe der z-Transformation können wir jede beliebige Normalverteilung in die Standardnormalverteilung mit dem Mittelwert 0 und der Standardabweichung 1 überführen.
􏰌 - Die Standardnormalverteilung ist eine wichtige Testverteilung und ihre Flächen und Werte sind tabelliert.
􏰌 - Weitere wichtige Testverteilungen, deren Werte tabelliert sind, sind die t-Verteilung, die 􏰅x2-Verteilung und die F-Verteilung.

10.5 Zeichnen der Verteilungen mit dem R Commander

Wir nutzen hierfür den Menüpunkt Verteilungen mit dem Unterpunkt Stetige Verteilungen. Im Anschluss können wir die Verteilungen auswählen.

Verteilungen -> Stetige Verteilungen -> ...

10.6 Anwendung
10.1. Zeichne mit Hilfe des R Commanders die Normalverteilungskurven N(􏰍20, 15), N(20, 15) und N(0, 25) und vergleiche diese.
10.2. Führe mit Hilfe der z-Transformation die Normalverteilung N(20, 15) in die Standardnormalverteilung N(0, 1) über. Wie hoch sind die z-Werte für folgende x-Werte: 􏰍25, 􏰍20, 􏰍10, 􏰍7, 5, 20, 35, 47, 50, 60, 65?
10.3. Wie groß ist die Fläche unter der Standardnormalverteilungskurve rechts von z = 0.5, 0.75, 1.0, 1.26?
10.4. Wie groß ist die Fläche unter der Standardnormalverteilungskurve links von z = 􏰍0.5, 􏰍0.75, 􏰍1.0, 􏰍1.26?
10.5. Vergleiche die Lösungen aus Aufgabe 3 und Aufgabe 4. Was können wir feststellen?
10.6. Nehmen wir an, dass Alter unserer Unternehmensgründer ist normalverteilt mit dem Mittelwert 35 und der Standardabweichung 7. Wie groß ist die Wahrscheinlichkeit, dass wir einen Unternehmensgründer entdecken, der älter als 42 Jahre ist? Wie groß ist die Wahrscheinlichkeit, dass wir einen Unternehmensgründer jünger als 21 Jahre entdecken? Wie groß ist die Wahrscheinlichkeit, dass wir einen Unternehmensgründer im Alter zwischen 42 und 49 Jahren entdecken?
10.7. Wir müssen in einem Auswahlverfahren zu den besten 5 % der Studenten gehören, um ein Stipendium zu erhalten. Wir wissen, dass die Punkteverteilung im Test normalverteilt ist und dass in der Regel im Durchschnitt 80 Punkte mit einer Standardabweichung von 10.0 Punkten erzielt werden. Wie viele Punkte müssen wir erzielen, um zu den besten 5 % der Studierenden zu gehören?

11. Hypothesentest: Was gilt?

Wir wissen nun, was eine Hypothese ist, wir kennen ferner wichtige Testverteilungen. Was wir noch nicht wissen ist, wie wir mit Hilfe der Testverteilungen Hypothesen testen und Aussagen über unsere Grundgesamtheit erzeugen.

-> Begriff statistische Signifikanz

11.1 Was bedeutet statistische Signifikanz?

Statistische Signifikanz ist ein zentrales Konzept zum Testen von Hypothesen. Mit Hilfe dieses Konzeptes werden Hypothesen abgelehnt oder eben nicht und es wird statistisch abgesichertes Wissen erzeugt.

H0: 􏰆D40
HA: 􏰆¤40

Was aber ist eine zu starke Abweichung bzw. ein kritischer Wert? Am besten verdeutlichen wir das mit einer Abbildung zum Konzept der statistischen Signifikanz anhand des einseitigen Hypothesentests. Diesen benutzen wir, wenn uns gerichtete Hypothesen vorliegen

Wir sehen an der Abbildung, dass Werte nahe am Erwartungswert eine hohe Wahrscheinlichkeit haben, aufzutreten, vorausgesetzt unsere Nullhypothese ist korrekt. Werte weit weg vom Erwartungswert haben eine sehr kleine Wahrscheinlichkeit. Wenn die Wahrscheinlichkeit zu klein ist, d. h. wenn unser Stichprobenmittelwert eine kritische Größe überschreitet, dann nehmen wir an, dass unsere Nullhypothese nicht korrekt sein kann und lehnen diese ab. ̨ ist dabei die Fläche der Stichprobenverteilung im Ablehnungsbereich, d. h. die Wahrscheinlichkeit, dass ein Wert gefunden wird, der größer als der kritische Wert ist.
Selbstverständlich kann es auch sein, dass der Ablehnungsbereich auf der linken Seite liegt und dass wir die Nullhypothese ablehnen, wenn ein kritischer Wert unterschritten wird.

Wir teilen unsere Fläche alphą in zwei Hälften, haben somit links und rechts jeweils  alpaha/2 und damit links einen kritischen Wert, den wir unterschreiten können und rechts einen kritischen Wert, den wir überschreiten können. An dieser Stelle ist es sinnvoll, sich noch einmal näher mit der Fläche alpha auseinanderzusetzen.	


11.2 Das Signifikanzniveau  alpha

Wir hatten bereits gesagt, dass  alpha die Fläche unter der Stichprobenverteilung im Ableh- nungsbereich ist und die Wahrscheinlichkeit repräsentiert einen Wert zu finden, der größer als der kritische Wert ist. Wie klein muss aber die Wahrscheinlichkeit sein, dass wir unsere Nullhypothese ablehnen?

In der Wissenschaft haben sich drei verschiedengroße Flächen durchgesetzt:  ̨ D 10 % bzw.  ̨ D 0:1,  ̨ D 5 % bzw.  ̨ D 0:05 sowie  ̨ D 1 % bzw.  ̨ D 0:01. Das heißt, wir lehnen die Nullhypothese ab, wenn die Wahrscheinlichkeit, einen bestimmten Wert zu finden, kleiner gleich 10, 5 oder 1 % ist. Statt 10, 5 oder 1 % können wir auch 0.1, 0.05 oder 0.01 schreiben, wir nutzen dann keine Prozentwerte sondern die Dezimalschreibweise. Wir bezeichnen diese Flächen auch als das Signifikanzniveau  ̨.

 alpha ist somit die Wahrscheinlichkeit, ab der wir unsere Nullhypothese ablehnen bzw. die Wahrscheinlichkeit des gefunden Stichprobenmittelwertes unter Gültigkeit der Nullhypothese.

 alpha ist auch die Fehlerwahrscheinlichkeit, mit der wir die Nullhypothese fälschlicherweise ablehnen.
 Das heißt, es besteht die Möglichkeit, dass wir bei unserer Testentscheidung einen Fehler machen. Dieser Fehler ist unser gewähltes Signifikanzniveau  alpha.

 Wichtig an dieser Stelle ist, dass wir uns im Vorfeld des Hypothesentests Gedanken über die Auswirkungen einer fälschlichen Ablehnung der Nullhypothese machen und unser alphą entsprechend dieser Überlegungen wählen.

 Nullhypo nicht abhlehnen obwohl sie falsch ist, dies ist dann ein beta-Fehler

 Um den ˇ-Fehler zu bestimmen, brauchen wir Kenntnis darüber, wie die Nullhypothese korrekt zu formulieren ist, so dass sie die Grundgesamtheit repräsentiert. Diese Kenntnis haben wir aber nicht, sonst hätten wir keine falsche Nullhypothese formu- liert. Aus diesem Grund begnügt man sich in der Praxis in der Regel mit dem Festlegen des  ̨-Fehlers.

 Daraus folgt, dass eine Testentscheidung immer nur ein Hinweis auf das Verhalten der Grundgesamtheit ist, nie aber ein echter Beweis.
 
11.3 Schritte beim Durchführen des Hypothesentests (S. 165)

1. Formulieren der Nullhypothese, der Alternativhypothese und des Signifikanzniveaus
2. Bestimmung der Testverteilung und der Teststatistik
3. Bestimmung des Ablehnungsbereiches und des kritischen Wertes
4. Berechnung des Testwertes
5. Entscheidung und Interpretation

11.4 Wie wähle ich mein Testverfahren aus?

Das Testverfahren hängt davon ab, was getestet werden soll und welches Skalenniveau die Daten haben.

Wichtig ist dabei zunächst, ob wir Gruppen untersuchen oder eine Beziehung zwischen Variablen. Bei ersteren gehen wir die linke Achse entlang und kommen zum Einstichprobentest, zum Test für unabhängige Stichproben und zum Test für abhängige Stichproben. Wenn wir eine Beziehung zwischen Variablen untersuchen, gehen wir die rechte Achse entlang und kommen je nach Datenniveau zu den verschiedenen Korrelationskoeffizien- ten bzw. zur Regression. Wir sind nun soweit und können starten. Im folgenden Kapitel beginnen wir mit unserer ersten Testsituation, dem Mittelwerttest.


11.5 Checkpoints
􏰌 - Das Signifikanzniveau alphą ist die Wahrscheinlichkeit einen Wert größer als einen kritischen Wert zu finden und damit die Wahrscheinlichkeit bzw. Sicherheit zu der die Nullhypothese abgelehnt wird.
􏰌 - ̨ wird üblicherweise in der Größe von 10, 5 oder 1 % gewählt. Alternativ wird auch  ̨ D 0:1,  ̨ D 0:05 und  ̨ D 0:01 geschrieben.
􏰌 - Die Wahl von  ̨ hängt davon ab, was geschieht, wenn wir die Nullhypothese fälschlicherweise ablehnen. Sind die Auswirkungen gravierend, wählen wir ein kleineres  ̨. Sind die Auswirkungen weniger gravierend, wählen wir ein größeres  ̨.
􏰌 - Beim Hypothesentest sind zwei Fehler möglich. Der  ̨-Fehler ist die Wahrscheinlich- keit, mit der die Nullhypothese abgelehnt wird, obwohl sie wahr ist. Der ˇ-Fehler ist die Wahrscheinlichkeit, mit der die Nullhypothese nicht abgelehnt wird, obwohl sie falsch ist.
􏰌 - ̨-Fehler und ˇ-Fehler sind miteinander verbunden. Verkleinert man den einen Fehler, vergrößert sich der andere und umgekehrt.
􏰌 - Beim Hypothesentest sind fünf Schritte durchzuführen: 1) das Formulieren der Nullhy- pothese, der Alternativhypothese und des Signifikanzniveaus, 2) die Bestimmung der Testverteilung und der Teststatistik, 3) die Bestimmung des kritischen Wertes und des Ablehnungsbereiches, 4) die Berechnung des Testwertes und 5) die Entscheidung und Interpretation.
􏰌 - Die Auswahl des Testverfahrens hängt von der Testsituation und dem Skalenniveau der Daten ab.	

11.6 Anwendung
11.1. WelchezweiBedeutungenhatdasSignifikanzniveau ̨? 
11.2. WelchederfolgendenAussagenistrichtig:
􏰌 Eine Überschreitung des kritischen Wertes führt zur Ablehnung der Nullhypo- these.
􏰌 Es ist möglich, den  ̨-Fehler auf null zu setzen.
􏰌 Je kleiner der  ̨-Fehler desto besser das Ergebnis.
􏰌 Die Auswahl des  ̨-Fehlers hängt von den Auswirkungen ab, die eine falsche
Verwerfung der Nullhypothese mit sich bringen.
11.3. Wannwirdbeidseitig,linksseitigoderrechtsseitiggetestet?
11.4. Formuliere zu folgender Forschungsfrage sowohl die Nullhypothese als auch die
Alternativhypothese für den beidseitigen Test, den linksseitigen Test und den rechtsseitigen Test. Wie alt sind Unternehmensgründer?
11.5. In welcher Beziehungzueinanderstehender ̨-Fehlerundderˇ-Fehler?
11.6. Gehe in die Bibliothek und suche einen Fachartikel von Interesse, welcher mittels einer Stichprobe Wissen über die Grundgesamtheit erzeugt. Erkläre, wie der Autor mittels des Konzeptes der statistischen Signifikanz Wissen über die Grundgesamt- heit erzeugt hat.

Teil 4 - Verfahren zum Testen von Hypothesen

Nun beginnen wir mit dem Hypothesentest und erzeugen Informationen über die Grundgesamtheit. Wenn unsere Angaben über die 100 neu gegründeten Unternehmen Daten aus einer echten Stichprobe wären, würden wir nun durch diese Daten Informationen über alle neu gegründeten Unternehmen erzeugen. Wir starten mit dem Mittelwerttest und den Tests auf Differenz von Mittelwerten für metrische Daten. Diese Testverfahren setzen voraus, dass die Daten metrisch und in der Grundgesamtheit normalverteilt sind. Die Vorausset- zung der Normalverteilung ist insbesondere bei kleinen Stichproben von Bedeutung. Bei großen Stichproben sind die Verfahren relativ robust gegenüber einer Verletzung dieser Annahme. Im Anschluss diskutieren wir die Testverfahren in Bezug auf Korrelation bei metrischen, ordinalen und nominalen Variablen. Zum Schluss gehen wir noch auf weitere Testverfahren für nominale Daten ein.

12 Der Mittelwerttest

12.1 Einführung zum Mittelwerttest

 Konkret gehen wir beim Mittelwerttest der Frage nach, ob die Annahme zum Mittelwert in der Grundgesamtheit mit dem vorliegenden Stichprobenbefund verträglich ist.

12.2 Die Forschungsfrage und Hypothesen beim Mittelwerttest: Sind Unternehmensgründer im Durchschnitt 40 Jahre alt?

H0: Unternehmensgründer sind im Durchschnitt 40 Jahre alt.
HA: Unternehmensgründer sind im Durchschnitt jünger oder älter als 40 Jahre.bzw.
apha = 5% bzw. alpha = 0,05

12.3 Die Testverteilung und Teststatistik beim Mittelwerttest

Jeder Test ist mit einer bestimmten Testverteilung und Teststatistik verbunden. Beim Mittelwerttest mit einer großen Stichprobe n > 30 wählt man als Testverteilung die Standardnormalverteilung. Die Teststatistik vergleicht den Stichprobenmittelwert mit dem Mittelwert, den wir unter der Nullhypothese angenommen haben

12.4 Der kritische Wert beim Mittelwerttest

Den kritischen Wert und damit den Ablehnungsbereich bestimmen wir mit Hilfe der Tabelle der Standardnormalverteilung. Dafür müssen wir wissen, ob wir einseitig oder zweiseitig testen und wie groß unser Signifikanzniveau ist. Wenn wir einseitig testen, le- gen wir das Signifikanzniveau entweder auf die linke oder auf die rechte Seite. Wenn wir zweiseitig testen, teilen wir das Signifikanzniveau auf beide Seiten auf. In unserem Beispiel testen wir beidseitig, da wir eine ungerichtete Nullhypothese, zum Signifikanzniveau von 5 % haben. Das heißt, wir haben im Ablehnungsbereich sowohl links als auch rechts eine Fläche von 2.5 % mit den kritischen Werten 􏰍-1.96 und 1.96

12.5 Der z-Wert

Nun müssen wir nur noch unseren z-Wert berechnen. Dies machen wir mit Hilfe der Teststatistik. Hierfür setzen wir den Mittelwert unserer Stichprobe, den Mittelwert aus der Nullhypothese und die Standardabweichung der Stichprobenverteilung ein. 

12.6 Die Entscheidung

Hierfür vergleichen wir unseren z-Wert mit den kritischen Werten. Wir sehen, dass unser z-Wert links vom kritischen Wert 􏰍1.96, also im Ablehnungsbereich liegt. Wir lehnen die Nullhypothese ab und kommen zur Inter- pretation. Wir können nun sagen, dass die Unternehmensgründer in der Grundgesamtheit ungleich 40 Jahre alt sind. Unser Stichprobenmittelwert deutet zudem darauf hin, dass die Unternehmensgründer im Durchschnitt jünger als 40 Jahre alt sind. Wir könnten jetzt noch das Konfidenzintervall berechnen, wie wir das schon im Kap. 8 getan haben. Wenn wir beispielsweise das 95 %-Konfidenzintervall bestimmen, zeigt sich, dass der wahre Wert mit einer Wahrscheinlichkeit von 95 % zwischen 32.68 und 35.82 Jahren liegt.

12.7 Der Mittelwerttest bei unbekannter Standardabweichung in der Grundgesamtheit oder bei kleiner Stichprobe n <= 30

Tendenziell haben wir das Problem, dass wir die Standardabweichung in der Grundgesamtheit nicht kennen.

Die Testverteilung ist dann nicht mehr die Standardnormalverteilung, sondern die t- Verteilung mit Fg = n 􏰍- 1 Freiheitsgraden. Dasselbe ist der Fall, wenn wir eine kleine Stichprobe haben. Wir sprechen beim Mittelwerttest von einer kleinen Stichprobe, wenn die Anzahl an Beobachtungen n kleiner gleich 30 ist (n 􏰋 <= 30). Die kritischen Werte werden in beiden Fällen nicht der Standardnormalverteilungstabelle, sondern der t-Verteilungstabelle (Anhang 3) entnommen. Folglich ist der Prüfwert t-verteilt.

Wir haben gerade gesehen, dass bei einer kleinen Stichprobe der Prüfwert t-verteilt und die Testverteilung die t-Verteilung ist. In Kap. 10 haben wir gesehen, dass bei einer großen Anzahl an Beobachtungen die t-Verteilung in die Standardnormalverteilung übergeht. In Statistikprogrammen wird daher in der Regel nur die t-Verteilung als Testverteilung ge- nutzt und man bezeichnet den Mittelwerttest oft auch als Einstichproben t-Test.

12.8 Checkpoints
􏰌 - Beim Mittelwerttest gehen wir der Frage nach, ob der angenommene Mittelwert der Grundgesamtheit mit unserem Stichprobenbefund verträglich ist.
􏰌 - Bei großer Stichprobe und Kenntnis über die Standardabweichung in der Grundge- samtheit ist die Testverteilung die Standardnormalverteilung und unser Prüfwert ist standardnormalverteilt. Den kritischen Wert entnehmen wir entsprechend der Stan- dardnormalverteilungstabelle.
􏰌 - Bei kleiner Stichprobe oder Unkenntnis über die Standardabweichung in der Grund- gesamtheit ist die Testverteilung die t-Verteilung und unser Prüfwert ist t-verteilt. Den kritischen Wert entnehmen wir entsprechend der t-Verteilungstabelle.
􏰌 - Der Mittelwerttest wird oft auch als Einstichproben t-Test bezeichnet.

12.9 Berechnung mit dem R Commander

Statistik -> Mittelwerte vergleichen -> t-Test für eine Stichprobe

Variable wählen -> Alternativhypo spezi ob zwei, links oder rechtsseitig getestet wird, Konfidenzintervall

R-CMD:
attach(Daten_Wachstum)
t.test(Alter, alternative=’two.sided’, mu=40.0, conf.level=.95)
detach(Daten_Wachstum


12.10 Anwendung
12.1. Wir interessieren uns für die Branchenberufserfahrung, die Unternehmensgründer im Durchschnitt mitbringen. Aufgrund von Vorüberlegungen und gelesenen Stu- dien vermuten wir, dass diese vor Gründung eines Unternehmens in der Regel zehn Jahre Branchenberufserfahrung angesammelt haben. Wir formulieren ent- sprechend folgende Nullhypothese: Die durchschnittliche Branchenberufserfah- rung beträgt 10 Jahre. Teste die Nullhypothese zum 10 % Signifikanzniveau unter Berücksichtigung aller relevanten Schritte.
12.2. Eines unserer Unternehmen ist in den letzten Jahren um durchschnittlich 5 % ge- wachsen. Uns interessiert nun, ob das Unternehmen im Vergleich zur Grundge- samtheit unterdurchschnittlich oder überdurchschnittlich gewachsen ist. Um dies zu testen, formulieren wir folgende Nullhypothese: Das durchschnittliche Wachs- tum der Jungunternehmen in der Grundgesamtheit in den letzten Jahren betrug 5 %. Teste die Nullhypothese zum 5 % Signifikanzniveau unter Berücksichtigung aller relevanten Schritte.
12.3. Nehmen wir an, dass unsere Stichprobe nur die ersten 25 Unternehmen unseres Datensatzes umfasst. Führe Aufgabe 2 für diese Problemstellung erneut durch.
12.4. Uns interessiert, ob der Anteil, den Unternehmen für Marketing aufwenden, in den letzten Jahren gesunken ist. Wir wissen, dass vor zehn Jahren der Aufwand durch- schnittlich bei 15 % lag. Um dies zu testen, formulieren wir die Nullhypothese: Der durchschnittliche Aufwand für Marketing in der Grundgesamtheit der Jungunter- nehmer ist größer gleich 15 %. Teste die Nullhypothese zum 10 % Signifikanzni- veau unter Berücksichtigung aller relevanten Schritte mit dem R Commander.
12.5. Wir wissen, dass Jungunternehmer vor zehn Jahren durchschnittlich 5 % ihres Um- satzes für Produktverbesserung aufgewandt haben. Wir vermuten, dass dieser Auf- wand gestiegen ist, da in der Literatur die steigende Bedeutung von Innovationen diskutiert wird. Das wollen wir anhand folgender Nullhypothese überprüfen: Der durchschnittliche Aufwand für Produktverbesserung ist bei der Grundgesamtheit der Jungunternehmer kleiner gleich 5 % vom Umsatz. Teste die Nullhypothese zum 5 % Signifikanzniveau unter Berücksichtigung aller relevanten Schritte mit dem R Commander.)


13. Der Test auf Differenz von Mittelwerten bei unabhängigen Stichproben

13.1 Einführung in den Test auf Differenz von Mittelwerten bei unabhängigen Stichproben

Wir vergleichen zwei Mittelwerte und testen, ob sich diese unterscheiden oder ob sie gleich sind. Immer dann, wenn wir zwei Mittelwerte aus zwei verschiedenen Gruppen vergleichen, führen wir den Test auf Differenz von Mittelwerten bei unabhängigen Stichproben durch.

13.2 Die Forschungsfrage und Hypothesen beim Test: Sind Frauen und Männer zum Zeitpunkt der Gründung gleich alt?

H0: Frauen und Männer sind bei Gründung eines Unternehmens im Durchschnitt gleich alt.
HA: Frauen und Männer sind bei Gründung eines Unternehmens im Durchschnitt nicht gleich alt.

 alpha = 10% bzw. alpha = 0,1

13.3 Die Testverteilung und die Teststatistik

Die Testverteilung ist die t-Verteilung mit (Fg = n1 + n2 -􏰍 2) Freiheitsgraden, wobei n1 die Anzahl der Beobachtungen der Gruppe eins und n2 die Anzahl der Beobachtungen der Gruppe zwei ist.

13.4 Der kritische t-Wert

Den kritischen Wert bestimmen wir mit Hilfe der t-Verteilungstabelle und der Freiheits- grade. Wie beim Mittelwerttest ist dabei wichtig, uns zu entscheiden, ob wir einseitig oder zweiseitig testen wollen und zu welchem Signifikanzniveau.
In unserem Beispiel testen wir zweiseitig und haben ein Signifikanzniveau von 10 %. D. h. wir haben sowohl links und rechts im Ablehnungsbereich eine Fläche von 5 %. Die kritischen Werte ent- nehmen wir der t-Verteilungstabelle mit Hilfe unserer Freiheitsgrade.

13.5 Der t-Wert und die Entscheidung

t-Wert berechnen, hierfür füllen wir unsere Teststatistik mit den benötigten Werten. (R-Commander)

Entscheidung: Ein Vergleich mit den kritischen Werten zeigt uns, dass wir die Nullhypothese nicht ableh- nen. Das heißt, in der Grundgesamtheit besteht kein Altersunterschied zwischen unseren Gründern und Gründerinnen, im Durchschnitt sind sie also in der Grundgesamtheit gleich alt.

13.6 Gleiche oder ungleiche Varianzen

In eben gezeigtem Beispiel sind wir einfach davon ausgegangen, dass die Streuung in der Variable Alter bei beiden Gruppen, Gründern und Gründerinnen, gleich ist. Wir können uns das natürlich ansehen, am besten mit Hilfe der Boxplots.

13.7 Berechnung mit dem R Commander

Hierfür konvertieren wir die Variable Geschlecht mit Hilfe des Menüpunktes Datenmanagement, Variablen Bearbeiten und dem Befehl Konvertiere numerische Variablen in Faktoren, in eine Faktorvariable.

Im Anschluss können wir mit Hilfe des Boxplots analysieren, ob die Varianzen für die beiden Gruppen (Gründerinnen und Gründer) in etwa gleich sind. Im Menü Grafik wählen wir den Befehl Boxplot aus. Wir spezifizieren im nächsten Fenster die Testvariable und mit Hilfe der Schaltfläche Grafik für die Gruppen definieren wir, dass wir für die Gruppen des Faktors Geschlecht die Boxplots erstellen möchten.

Grafiken -> Boxplott -> Alter -> F_Geschlecht

13.8 Checkpoints
􏰌 - Beim Test auf Differenz von Mittelwerten bei unabhängigen Stichproben gehen wir der Frage nach, ob sich zwei Gruppen in ihrer Grundgesamtheit hinsichtlich eines Mittelwertes unterscheiden.
􏰌 - Der Test auf Differenz von Mittelwerten bei unabhängigen Stichproben wird oft auch als Zweistichproben t-Test bezeichnet.
􏰌 - Je nachdem, ob die Varianzen bei beiden Gruppen gleich oder ungleich sind, führen wir den Test für gleiche Varianzen oder ungleiche Varianzen durch.
􏰌 - Bei einer kleinen Stichprobe und metrischen, aber nicht normalverteilten Daten und bei ordinalen Daten greifen wir auf den Mann-Whitney Test zurück.

13.9 Anwendung
13.1. Wir fragen uns, ob Männer und Frauen bei Gründung eines Unternehmens gleich alt sind. Theoretische Überlegungen und bisherige Studien bringen uns dazu anzunehmen, dass Männer im Durchschnitt älter als Frauen sind. Führe den Test mit Hand zum 10 % Signifikanzniveau unter Berücksichtigung aller relevanten Schritte durch.
13.2. Uns interessiert, ob Dienstleistungsunternehmen oder Industrieunternehmen in den letzten fünf Jahren ein höheres Wachstum verzeichnet haben. Studien und theoretische Überlegungen deuten darauf hin, dass es einen Unterschied geben müsste. Führe den Test unter Berücksichtigung aller relevanten Schritte mit Hilfe des R Commanders zum 5 % Signifikanzniveau durch.
13.3. Uns interessiert, ob Industrieunternehmen oder aber Dienstleistungsunternehmen relativ mehr Geld für Produktverbesserungen aufwenden. Studien und theoretische Überlegungen deuten darauf hin, dass Industrieunternehmen einen höheren Anteil vom Umsatz für Produktverbesserungen aufwenden. Führe den Test mit Hilfe des R Commanders unter Berücksichtigung aller relevanten Schritte zum 1 % Signifikanzniveau durch.
13.4. Wir fragen uns, ob Männer und Frauen bei Gründung eines Unternehmens mehr Branchenberufserfahrung mitbringen. Existierende Studien deuten darauf hin, dass es einen Unterschied gibt. Wir führen den entsprechenden Hypothesentest unter Berücksichtigung aller relevanten Schritte mit Hilfe des R Commanders durch.
13.5. Uns interessiert, ob Gründer oder Gründerinnen mehr für Marketing aufwenden. Theoretische Überlegungen führen dazu anzunehmen, dass Männer mehr Geld für Marketing aufwenden als Frauen. Wir führen den entsprechenden Hypothesentest unter Berücksichtigung aller relevanten Schritte mit Hilfe des R Commanders durch.

14 Der Test auf Differenz von Mittelwerten bei abhängigen Stichproben

14.1 Einführung in den Test auf Differenz von Mittelwerten bei abhängigen Stichproben

Beim Mittelwerttest für unabhängige Stichproben haben wir untersucht, ob sich zwei unabhängige Gruppen bezüglich eines Sachverhaltes unterscheiden. Wir haben zwei verschiedene Gruppen untersucht und diese dann verglichen. Beim Test auf Differenz von Mittelwerten bei abhängigen Stichproben untersuchen wir ein und dieselbe Gruppe zweimal und fragen uns, ob eine bestimmte Maßnahme einen Einfluss auf die Gruppe hat. Wir können uns beispielweise fragen, ob Alkohol einen Einfluss auf die Fahrtüchtigkeit von Personen hat, oder ob ein Medikament den Gesundheitszustand von Personen verbessert. Wir untersuchen die Person vor und nach der Maßnahme, vergleichen anschließend die Ergebnisse und fragen damit nach der Wirkung der Maßnahme. Im Unternehmenskontext wird das Verfahren zum Beispiel eingesetzt, um die Wirkung einer Werbemaßnahme zu evaluieren, z. B. um zu fragen, welchen Einfluss eine Werbemaßnahme auf die Einstellung von Personen zu einem bestimmten Produkt oder Unternehmen ausübt. Man könnte aber auch untersuchen, wie Energy-Drinks die Leistungsfähigkeit von Sportlern beeinflusst.

14.2 Das Beispiel: Schulung von Unternehmensgründern in der Vorgründungsphase

Tabellarische Darstellung der Kennzahlen mit Legende, ausgerechnete quadrierte Differenz des Umsatzes

14.3 Die Forschungsfrage und die Hypothesen beim Test: Hat die Schulung einen Einfluss auf die Einschätzung des Marktpotentials?

FF: Hat die Schulung einen Einfluss auf die Einschätzung der potentiellen Unternehmensgründer hinsichtlich des Marktpotentials ihrer geplanten Unternehmen?

H0: Die Schulung hat keinen Einfluss auf die Einschätzung der potentiellen Unternehmensgründer hinsichtlich des Marktpotentials ihrer geplanten Unternehmen.
HA: Die Schulung hat einen Einfluss auf die Einschätzung der potentiellen Unternehmensgründer hinsichtlich des Marktpotentials ihrer geplanten Unternehmen.

alpha = 10 %

14.4 Die Teststatistik

Wir sehen, dass der Testwert t-verteilt ist und dass wir mit Hilfe der Teststatistik die Differenz zwischen den Werten vor und nach der Maßnahme vergleichen. Sollte die Maß- nahme keinen Einfluss ausüben, so wären die Werte vor und nach der Maßnahme gleich, die Differenz also null und damit wäre auch der Zähler des Bruches in der Teststatistik null. Daraus folgt, dass auch der t-Wert bei null läge und wir unsere Nullhypothese somit nicht ablehnen würden.

14.5 Der kritische t-Wert

Die Anzahl an Freiheitsgraden beim Test auf Differenz von Mittelwerten bei abhängigen Stichproben beträgt Fg = n -􏰍 1, d. h. wir haben Fg = 25 􏰍 - 1 = 24 Freiheitsgrade. Damit sind die kritischen t-Werte gleich 􏰍1.711 und 1.711.

14.6 Der t-Wert und die Entscheidung

Vergleichen wir den berechneten t-Wert mit unseren kritischen Werten, so sehen wir, dass wir die Nullhypothese ablehnen und mit der Alternativhypothese weiterverfahren. Das heißt, die Schulung hat einen Einfluss auf die Einschätzung des Marktpotentials der potentiellen Unternehmensgründer. Um zu bestimmen, ob der Einfluss positiv oder nega- tiv wirkt, vergleichen wir am besten die Stichprobenmittelwerte vor und nach der Maß- nahme. In unserem Fall lag der Mittelwert vor der Schulung bei 183.4 bzw. CHF 183‘400, nach der Schulung lag er bei 174.6 bzw. CHF 174‘600. Das heißt, die Schulung bewirkt, dass die potentiellen Gründer das Marktpotential etwas konservativer einschätzen.

14.7 Berechnung mit dem R Commander

Die Berechnung des Tests auf Differenz von Mittelwerten bei abhängigen Stichproben mit dem R Commander erfolgt mit dem Befehl t-Test für gepaarte Stichproben. Diesen finden wir im Menü Statistik im Untermenü Mittelwerte vergleichen. Nachdem wir den Befehl aufgerufen haben, spezifizieren wir die Variablen. In der Regel nehmen wir die Variable vor der Maßnahme als erste Variable und die Variable nach der Maßnahme als zweite Variable. In der Registerkarte Optionen spezifizieren wir zudem, ob wir zwei-, links- oder rechtsseitig testen und geben das Konfidenzintervall an.

Die meisten Zahlen dürften uns bekannt sein. In der ersten Zeile steht, dass der t- Test für abhängige Stichproben durchgeführt wurde (Paired t-test). Anschließend sind die Variablen angegeben. In der dritten Zeile finden wir den t-Wert, die Anzahl an Freiheitsgraden und den p-Value. Der t-Wert beträgt 3.1734. Von Hand hatten wir 3.17 berechnet. Bis auf Rundungsfehler sind die Werte identisch. Wir haben 24 Freiheitsgrade und der p- Value zeigt uns die Wahrscheinlichkeit einer korrekten Nullhypothese. Die Wahrscheinlichkeit liegt bei 0.004096 bzw. 0.41 %. Daraus folgt, dass wir die Nullhypothese zum spezifizierten Signifikanzniveau von  ̨ D 0:1 bzw.  ̨ D 10 % ablehnen. Wir gehen also von der in der vierten Zeile angegebenen Alternativhypothese aus. Zu diesem Er- gebnis kommen wir auch, wenn wir den berechneten t-Wert mit dem kritischen t-Wert vergleichen. Ferner sehen wir in Zeile 5 bis 9 den aus der Stichprobe geschätzten durch- schnittlichen Unterschied von 8.8 (CHF 8‘800) sowie das 95 %-Konfidenzintervall. Dieses zeigt uns an, dass der wahre Wert in der Grundgesamtheit mit einer 95 % Wahrscheinlichkeit im Intervall von 3.077 (CHF 3‘077) und 14.523 (CHF 14‘523) liegt. Damit kennen wir sowohl den für die Grundgesamtheit geschätzten Unterschied als auch das Konfidenzintervall.

CMD: t.test(Pre, Post, alternative=’two.sided’, conf.level=.95, paired=TRUE)

14.8 Checkpoints
􏰌 - Beim Test auf Differenz von Mittelwerten bei abhängigen Stichproben gehen wir der Frage nach, ob eine Maßnahme einen Einfluss auf Personen oder Objekte ausübt.
􏰌 - Beim Test auf Differenz von Mittelwerten bei abhängigen Stichproben untersuchen wir dieselben Untersuchungsobjekte zweimal, einmal vor und einmal nach der Maßnahme.
􏰌 - Bei einer kleinen Stichprobe und metrischen, aber nicht normalverteilten Daten und bei
ordinalen Daten greifen wir auf den Wilcoxon Test für abhängige Stichproben zurück.


14.9 Anwendung
14.1. Uns interessiert, ob eine Schulungsmaßnahme im Bereich Buchhaltung entspre- chend der Angaben des Organisators der Schulungsmaßnahme dazu führt, dass we- niger Zeit pro Monat für die Buchhaltung aufgewendet wird (Daten_Buchhaltung). Führe den Test von Hand zum 10 % Signifikanzniveau durch und interpretiere das Ergebnis.

14.2.
Uns interessiert, ob das Trinken von Energy-Drinks die Leistungsfähigkeit von Sportlern beeinflusst (Daten_Energy). Das Untersuchungsdesign sieht vor, dass dieselben Sportler zweimal in jeweils einer Stunde so weit wie möglich laufen. Einmal haben sie die Möglichkeit während des Laufens nur Wasser zu konsumie- ren, das andere Mal dürfen sie nur Energy-Drinks zu sich nehmen. Führe den Test mit dem R Commander zum 1 % Signifikanzniveau durch und interpretiere das Ergebnis.

15. Der Test auf Korrelation bei metrischen, ordinalen und nominalen Daten

In Kap. 6 sind wir der Frage nach dem Zusammenhang zwischen zwei Variablen nach- gegangen, also wie und ob sich zwei Variablen gemeinsam bewegen. Wir haben dies sowohl für metrische und ordinale als auch für nominale Variablen untersucht. Beispiels- weise untersuchten wir einen Zusammenhang zwischen den Variablen Marketing und Produktverbesserung oder zwischen den Variablen Erwartung und Selbsteinschätzung. Berechnet haben wir die Korrelationskoeffizienten anhand der Stichprobe. Mit dem Test auf Korrelation testen wir nun, ob der in der Stichprobe entdeckte Zusammenhang auch für die Grundgesamtheit gilt. Nur dann ist unser Stichprobenergebnis wirklich für Hand- lungsempfehlungen und Schlussfolgerungen von Bedeutung. Wenn der in der Stichprobe entdeckte Zusammenhang nicht signifikant ist, dann gilt der entdeckte Zusammenhang in der Grundgesamtheit nicht. Im Folgenden diskutieren wir den Test auf Korrelation für die Korrelationskoeffizienten von Bravais-Pearson und Spearman sowie für nominale Daten. Die Vorgehensweise ist dabei die gleiche wie bei den bereits kennengelernten Hypothe- sentests. Wir formulieren zunächst die Nullhypothese sowie die Alternativhypothese und spezifizieren das Signifikanzniveau. Dann legen wir die Testverteilung und die Teststatistik fest. Anschließend bestimmen wir den Ablehnungsbereich und die kritischen Werte. Als letzte Schritte berechnen wir den Testwert und führen die Entscheidung durch.

15.1 Der Test auf Korrelation bei metrischen Daten

Die Testsituationen bei Korrelation zwischen metrischen Daten

H0: Es gibt keinen Zusammenhang zwischen der Variable X und der Variable Y 
HA: Es gibt einen Zusammenhang zwischen der Variable X und der Variable Y

Kein Zusammenhang bedeutet, dass der Korrelationskoeffizient gleich null ist. Ein Zusammenhang bedeutet entsprechend, dass der Korrelationskoeffizient ungleich null ist.

Im zweiten Fall gehen wir davon aus, dass die Korrelation positiver Natur ist. Die Null- und Alternativhypothese sehen dann wie folgt aus:

H0: Zwischen Variable X und Variable Y gibt es einen negativen bzw. keinen Zusammenhang
HA: Zwischen Variable X und Variable Y gibt es einen positiven Zusammenhang

Wenn wir die Nullhypothese ablehnen, gehen wir davon aus, dass zwischen den beiden Variablen ein positiver Zusammenhang besteht, der Korrelationskoeffizient ist grösser null.
Im dritten Fall lauten aufgrund der Annahme einer negativen Korrelation die Null- und Alternativhypothese wie folgt:

H0: Zwischen Variable X und Variable Y gibt es einen positiven bzw. keinen Zusammenhang
HA: Zwischen Variable X und Variable Y gibt es einen negativen Zusammenhang

Wenn wir die Nullhypothese ablehnen, gehen wir davon aus, dass der Korrelationsko- effizient kleiner als null ist und es besteht ein negativer Zusammenhang.

Die Teststatistik und die Testverteilung beim Test

Wir berechnen den Korrelationskoeffizienten von Bravais-Pearson aus der Stichprobe und setzen den Wert von r anschließend in folgende Teststatistik ein.

Beispiel: Gibt es einen Zusammenhang zwischen Aufwand für Marketing und Produktverbesserung bei jungen Unternehmen?

Um zu testen, ob es in der Grundgesamtheit tatsächlich einen Zusammenhang gibt, setzen wir den Wert für den Korrelationskoeffizienten in unsere Teststatistik ein und berechnen den t-Wert.

Die Testverteilung ist wie gesagt die t-Verteilung mit n 􏰍 2 Freiheitsgraden, d. h. wir haben bei 6 Beobachtungen 4 Freiheitsgrade. Ablehnen werden wir, wenn unser Korrelationskoeffizient aus der Stichprobe den kritischen Wert, d. h. 􏰍-2.132, unterschreitet.
Unser berechneter Testwert unterschreitet den kritischen Wert, d.h. wir lehnen die Nullhypothese in diesem Fall ab und arbeiten mit der Alternativhypothese weiter. In der Grundgesamtheit gibt es also einen negativen Zusammenhang zwischen dem Aufwand für Produktverbesserung und Marketing. Unternehmer, die viel für Marketing aufwenden, wenden weniger für Produktverbesserung auf und umgekehrt. Wenn wir so wollen, haben wir eine Spezialisierungsstrategie von Unternehmen entdeckt. Die einen versuchen, über Marketing erfolgreich zu sein, die anderen, sich durch Produktverbesserungen zu positionieren.

15.2 Der Test auf Korrelation bei ordinalen Daten

Die Testsituationen beim Test auf Korrelation bei ordinalen Daten sind die gleichen wie zwischen metrischen Daten. Der Unterschied ist lediglich, dass wir nicht den Korrela- tionskoeffizienten von Bravais-Pearson benutzen, sondern den Korrelationskoeffizienten von Spearman.

Die Teststatistik und die Testverteilung beim Test
Beispiel: Gibt es eine Korrelation zwischen Selbsteinschätzung und Erwartung bezüglich der wirtschaftlichen Entwicklung eines Unternehmens?

In Kap. 6 hatten wir für die ersten sechs Unternehmen eine positive Korrelation in Höhe von rSp = 0,58 berechnet. Nun wollen wir noch testen, ob diese Korrelationsbeziehung auch für die Grundgesamtheit gilt.
Signifikanzniveau alpha = 10 Prozent

Um herauszufinden, ob der Zusammenhang aufgrund unseres Stichprobenbefundes gilt, setzen wir den Wert für den Korrelationskoeffizienten in unsere Teststatistik ein und berechnen den t-Wert.

Diesen Wert müssen wir nun noch mit unserem kritischen Wert vergleichen, den wir aus der t-Tabelle ablesen. Wir lehnen die Nullhypothese ab, wenn wir einen Wert von 1.533 überschreiten.

15.3 Der Test auf Korrelation bei nominalen Daten

Wenn wir auf Korrelation zwischen zwei nominalen Variablen testen, haben wir zwei Situationen. Entweder liegen uns nominale Variablen mit jeweils zwei Ausprägungen vor, oder wir haben nominale Variablen mit mehr als zwei Ausprägungen. In beiden Fällen sagt der Korrelationskoeffizient nichts über die Richtung des Zusammenhanges aus, d. h. wir können nicht auf positive oder negative Korrelation testen. Wir können nur darauf testen, ob wir einen Zusammenhang haben oder nicht. Aus diesem Grund werden beide Testverfahren auch häufig Tests auf Unabhängigkeit genannt. Wenn die Variablen nicht korreliert sind, dann sind sie voneinander unabhängig.

Kontigenkoeffizent:
H0: C = 0 
HA: C > 0

Bei nominalen Variablen mit jeweils zwei Ausprägungen hatten wir den Vierfelderkoeffizienten berechnet.


Damit kennen wir unsere Testverteilung, es ist die 􏰅2-Verteilung, und wir kennen un- seren Testwert. Wir können den Test auf Unabhängigkeit durchführen.
In Kap. 6 sind wir der Frage nachgegangen, ob es einen Zusammenhang zwischen dem Geschlecht der Gründer und der Branche, in der sie gründen gibt. Wir hatten dabei die ersten zehn Gründungen beobachtet und errechneten anhand der folgenden 2 × 2 Matrix einer in Höhe von 􏰍-0.50.

Also haben wir einen mittleren Zusammenhang zwischen dem Geschlecht und der Branche, in der gegründet wird, entdeckt. Sehen wir uns die Matrix an, so sehen wir, dass Frauen häufiger Dienstleistungsunternehmen gründen, Männer häufiger Industrieunternehmen. Gilt der Zusammenhang aber auch für unsere Grundgesamtheit?

Hierfür führen wir den Test durch, wobei die Null- und die Alternativhypothese wie folgt lauten:
H0: Es gibt keinen Zusammenhang zwischen dem Geschlecht und der Branche, in der gegründet wird
HA: Es gibt einen Zusammenhang zwischen dem Geschlecht und der Branche, in der gegründet wird bzw.


Aus r ̊ = 􏰍-0,50 errechnen wir unseren Testwert. Dieser ist der 􏰅2-Wert: 

Den Wert vergleichen wir nun mit dem kritischen Wert der 􏰅2-Verteilungstabelle (siehe Anhang 4). Aus dieser können wir ablesen, dass wir die Nullhypothese ablehnen, wenn wir einen Wert von 3.841 überschreiten.

Der Test auf Unabhängigkeit bei nominalen Variablen mit mehr als zwei Ausprägungen

Vergleichen wir unseren Testwert in Höhe von 2.42 mit dem kritischen Wert, so stellen wir fest, dass wir die Nullhypothese nicht ablehnen. Aufgrund des Stichprobenbefundes können wir die Aussage treffen, dass zwischen Gründungsmotiv und Branche, in der ge- gründet wird, kein Zusammenhang besteht.
Auch hier ist darauf zu achten, dass jede Zelle mindestens mit 5 Untersuchungsobjek- ten besetzt ist. Ansonsten kann der Test zu falschen Ergebnissen führen.


15.4 Checkpoints

 - Beim Test auf Korrelation nutzen wir die für die Variablen relevanten Korrelationskoeffizienten, z. B. bei metrischen Daten den Korrelationskoeffizienten von Bravais-Pearson.
􏰌 - Bei metrischen und ordinalen Variablen können wir ungerichtet oder gerichtet testen.
􏰌 - Bei metrischen und ordinalen Variablen ist die Testvariable t-verteilt.
􏰌 - Bei nominalen Variablen testen wir, ob ein Zusammenhang besteht. Diese Testverfahren werden oft Test auf Unabhängigkeit genannt.
􏰌 - Bei nominalen Variablen ist die Testvariable 􏰅2-verteilt, die Testverfahren werden oft auch als 􏰅2-Unabhängigkeitstest bezeichnet.

15.5 Berechnung mit dem R-Commander

Zur Berechnung der Tests auf Korrelation bei metrischen Variablen zeichnen wir zunächst das Streudiagramm zwischen den Variablen und prüfen, ob es eine lineare Beziehung zwischen diesen gibt (siehe Abschn. 6.9). Anschließend können wir den Test durchführen. Im R Commander steht uns hierfür der Befehl Test auf Signifikanz der Korrelation zur Verfügung. Diesen Befehl können wir sowohl für den Test auf Korrelation bei metrischen Daten als auch bei ordinalen Daten nutzen. Wir finden den Befehl im Menü Statistik bei Deskriptive Statistik. Wir wählen die Variablen aus, definieren den benötigten Korrelationskoeffizienten und spezifizieren die Alternativhypothese.

-> Statistik -> Deskriptive Statistik -> Testen auf Signifikanz der Korrelation -> Variablen auswählen -> Typ (Pearson, Spearman, Kenndals Tau), 0 > Korrelation < 0

Die Interpretation des Ergebnisses geschieht wie folgt. In der ersten Zeile sehen wir den berechneten Korrelationskoeffizienten, als nächstes die verwendeten Variablen und in der dritten Zeile unseren t-Wert, die Anzahl an Freiheitsgraden und die Wahrscheinlich- keit, dass die Nullhypothese zutrifft (p-Value). Wir haben 98 Freiheitsgrade, einen t-Wert in Höhe von 􏰍0.31 und eine Wahrscheinlichkeit, dass die Nullhypothese aufgrund des Stichprobenbefundes zutrifft, von 0.3787 bzw. 38.87 %. Daraus folgt, dass wir die Null- hypothese nicht verwerfen. Es gibt also keinen negativen Zusammenhang zwischen den beiden Variablen, wie es in der Alternativhypothese formuliert ist (Zeile 4). In den Zei- len 5 bis 9 finden wir den aus der Stichprobe geschätzten Korrelationskoeffizienten sowie das Konfidenzintervall. Das 95 %-Konfidenzintervall für den Korrelationskoeffizienten in der Grundgesamtheit reicht von 􏰍1 bis 0.13. Der berechnete Korrelationskoeffizient be- trägt 􏰍0.03. Ein Hinweis: das Ergebnis weicht vom Beispiel in diesem Kapitel ab. Der Grund ist, dass im Beispiel lediglich mit den ersten sechs Beobachtungen gerechnet wur- de (n = 6), während wir hier auf den kompletten Datensatz zurückgreifen (n = 100).


CMD: cor.test(Marketing, Produktverbesserung, alternative="less", method="pearson")

Die Vorgehensweise und die Interpretation beim Test auf Korrelation bei ordinalen Daten sind weitgehend identisch. Der Unterschied besteht lediglich darin, dass wir den Rangkorrelationskoeffizienten von Spearman nutzen und interpretieren. Wir verzichten hier daher auf die ausführliche Darstellung. Der Befehl ändert sich dahingehend, dass wir bei Methode spearman definieren.

CMD: cor.test(Erwartung, Selbsteinschaetzung, alternative="greater", method="spearman")

Nun wollen wir uns noch den Test auf Unabhängigkeit bei nominalen Variablen an- sehen. Dieser ist sowohl für nominale Variablen mit zwei Ausprägungen als auch für nominale Variablen mit mehr als zwei Ausprägungen identisch. Um den Test durchzuführen,
müssen wir R zunächst wieder mitteilen, dass wir nominale Variablen haben. Wir machen dies mit dem Befehl Konvertiere numerische Variablen in Faktoren im Menü Datenmanagement und dem Untermenü Variablen bearbeiten (vgl. z. B. Abschn. 6.9). Nachdem wir R mitgeteilt haben, welches die nominalen Variablen sind, für die wir den Test durchführen möchten, finden wir den entsprechenden Befehl im Untermenü Kontingenztabellen im Menü Statistik. Der Befehl wird aufgerufen, indem Kreuztabelle angeklickt wird. Im sich öffnenden Fenster markieren wir die Zeilen- und die Spalten- variable und in der Registerkarte Statistik die entsprechenden Optionen. Uns interessiert insbesondere der Chi-Quadrat-Test auf Unabhängigkeit und die erwarteten Häufigkeiten.

Statistik -> Kontigenteztabelle -> Kreuztabelle -> Datenmangement (Zeilen, Spaltenwerte), Anweisung für die Teilmenge, Statistik -> keine Prozente, Chi-Quadrat-Test auf Unabhänigigkeit -> Zeige erwartete Häufigkeiten

Die Zahlen sind uns fast alle wieder bekannt, wir haben diese im Buch bereits mehrfach gesehen. Der erste Ausgabebereich enthält die beobachteten Häufigkeiten für das Gründungsmotiv in der jeweiligen Branche (Frequency Table). Im unteren Ausgabebereich erhalten wir die erwarteten Häufigkeiten (Expected Counts). Dazwischen finden wir unseren Test auf Unabhängigkeit. Dieser beginnt mit seinem Namen (Pearson’s Chi-squa- red test). Darunter sind die Daten spezifiziert. Diese sind die Häufigkeiten in der Tabelle. Im Anschluss daran erhalten wir unsere Abweichungssumme U bzw. 􏰅2-Quadrat Wert in Höhe von 2.42, die Anzahl an Freiheitsgraden und die Wahrscheinlichkeit, dass die Variablen voneinander unabhängig sind (p-Value). Diese ist hier 0.298 bzw. 29.8 %. Das ist die Wahrscheinlichkeit, einen Testwert in Höhe von 2.42 zu erhalten (siehe Beispiel oben), unter der Voraussetzung, dass die Nullhypothese die Grundgesamtheit richtig wiedergibt. Wie oben lehnen wir also aufgrund des Befundes die Nullhypothese nicht ab. Wir würden erst ablehnen, wenn dieser Wert unser spezifiziertes Signifikanzniveau unterschreiten würde.

15.6 Anwendung
15.1. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Wachstums- rate und Marketing den Korrelationskoeffizienten von Bravais-Pearson mit dem R Commander und teste das Ergebnis ungerichtet zum Signifikanzniveau von 5 %.
15.2. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Wachstums- rate und Erfahrung den Korrelationskoeffizienten von Bravais-Pearson mit dem R Commander und teste auf eine positive Korrelation zum Signifikanzniveau von 1%.
15.3. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Wachstums- rate und Selbsteinschätzung den Rangkorrelationskoeffizienten von Spearman mit dem R Commander und teste auf eine positive Korrelation zum Signifikanzniveau von 10 %.
15.4. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Geschlecht und Branche den Vierfelderkoeffizienten mit dem R Commander und teste das Ergebnis zum Signifikanzniveau von 5 %.
15.5. Berechne für unseren Datensatz Daten_Wachstum für die Variablen Geschlecht und Gründungsmotiv den Kontingenzkoeffizienten mit dem R Commander und teste das Ergebnis zum Signifikanzniveau von 10 %.

16 Weitere Testverfahren für nominale Variablen (Kapitel nicht lernen)

Mittlerweile haben wir eine ganze Reihe von Testverfahren kennengelernt. Es fehlt uns noch ein wichtiger Strang, die Testverfahren für nominale Daten. Diese wollen wir uns jetzt ansehen. Die Testverfahren für nominale Daten werden oft kurz 􏰅2-Tests genannt, da die Testverteilung in der Regel die 􏰅2-Verteilung ist. Mit dem 􏰅2-Test auf Unabhängigkeit haben wir bereits eines der Verfahren für nominale Daten kennengelernt. Wir werden uns jetzt zudem ansehen, wie die Tests bei nominalen Daten und einer Stichprobe, bei zwei unabhängigen Stichproben und bei zwei abhängigen Stichproben durchgeführt werden.

16.1 Der 􏰅2-Test bei einer Stichprobe: Entspricht der Anteil der Gründerinnen dem Geschlechteranteil in der Gesellschaft?

Beim 􏰅2-Test mit einer Stichprobe untersuchen wir, ob die beobachteten Häufigkeiten in einer Stichprobe mit den Häufigkeiten, die wir aufgrund unserer Vorkenntnisse haben, übereinstimmen. Mit Blick auf unseren Datensatz können wir uns z. B. fragen, ob der An- teil der Gründerinnen mit dem Geschlechterverhältnis in der Gesellschaft übereinstimmt oder nicht, d. h. ob signifikant weniger oder signifikant mehr Frauen ein Unternehmen gründen. Wir könnten uns aber auch fragen, ob der Anteil der Gründerinnen in der Stich- probe mit dem Anteil der Gründerinnen in der Grundgesamtheit übereinstimmt. In letzte- ren Fall würden wir unsere Stichprobe auf Repräsentativität testen.

0: Die Häufigkeit der von Männern und Frauen gegründeten Unternehmen entspricht dem Geschlechteranteil in der Gesellschaft
HA: Die Häufigkeit der von Männern und Frauen gegründeten Unternehmen entspricht nicht dem Geschlechteranteil in der Gesellschaft

Die Teststatistik ist 􏰅2-verteilt mit Fg = c 􏰍- 1 Freiheitsgraden. c ist dabei die Anzahl an Kategorien, die bei der Variablen vorkommen können.
Nun benötigen wir noch die beobachteten Werte und die theoretisch erwartete Werte. Beobachtet haben wir in unserer Stichprobe der 100 Unternehmen insgesamt 35 Gründe- rinnen und 65 Gründer. Erwarten würden wir aufgrund unseres Geschlechteranteils in der Gesellschaft jeweils 100 × 0.5 = 50 Gründerinnen und 50 Gründer.

wobei wir Fg D c 􏰍 1 D 2 􏰍 1 D 1 Freiheitsgrade haben. Es sind zwei Ausprägungen möglich, Mann und Frau, d. h. wir haben zwei mögliche Antwortkategorien.
Wir brauchen jetzt nur noch unseren kritischen 􏰅2-Wert zu bestimmen und können anschließend die Testentscheidung durchführen. Der kritische 􏰅2-Wert liegt bei einem Freiheitsgrad und einem Signifikanzniveau von 10 % laut 􏰅2-Verteilungstabelle bei 2.706 (vergleiche Anhang 4).

Vergleichen wir unseren berechneten Wert für die Abweichungssumme U in Höhe von 9.0 mit unserem kritischen Wert von 2.706, so lehnen wir die Nullhypothese ab. Daraus folgt, die Häufigkeit der von Männern und Frauen gegründeten Unternehmen entspricht nicht dem Geschlechteranteil in der Grundgesamtheit. Männer gründen häufiger ein Un- ternehmen als Frauen.


16.2 Der 􏰅2-Test bei zwei voneinander unabhängigen Stichproben: Sind die Gründungsmotive bei Dienstleistungs-
und Industrieunternehmen gleich?

Mit dem 􏰅2-Test bei zwei voneinander unabhängigen Stichproben untersuchen wir, ob sich zwei Gruppen hinsichtlich der Häufigkeitsanteile einer nominalen Variable unter- scheiden. Wir vergleichen, ob die jeweiligen Häufigkeiten in den jeweiligen Gruppen von den theoretisch erwarteten Häufigkeiten abweichen.
Am besten erläutern wir das anhand des in Kap. 15 beim Test auf Unabhängigkeit verwendeten Beispiels. Hier hatten wir untersucht, ob es einen Zusammenhang zwischen Gründungsmotiv und Branche gibt.

Die Zellenbesetzung kann folgendermaßen gelesen werden: Im Industriesektor wer- den 8 von 34 Unternehmen (23.5 %) aus der Arbeitslosigkeit heraus gegründet, 15 von 34 (44.1 %) der Gründer wollen eine Idee umsetzen und 11 von 34 (32.4 %) wollen ein höheres Einkommen erzielen. Bei den Dienstleistungsgründungen sind die Verhältnisse 9 zu 66 (13.6%), 39 zu 66 (59.1%) und 18 zu 66 (27.3%).
Der Test soll uns helfen zu bestimmen, ob sich die zwei Gruppen hinsichtlich der Anteile der Gründungsmotive unterscheiden. 

Wir testen folgende Null- und Alternativhypothese:
H0: Industriegründungen unterscheiden sich hinsichtlich der Anteile der Gründungs- motive nicht von Dienstleistungsgründungen
HA: Industriegründungen unterscheiden sich hinsichtlich Anteile der Gründungsmotive von Dienstleistungsgründungen


wobei U wiederum 􏰅2-verteilt mit Fg D .k 􏰍 1/ 􏰎 .j 􏰍 1/ Freiheitsgraden ist.
Damit wird beim Test so vorgegangen, wie wir es in Kap. 15 diskutiert haben (ver- gleiche Kap. 15). Der Unterschied liegt lediglich in der unterschiedlichen Formulierung der Hypothesen, das eine Mal testen wir auf Unabhängigkeit, das andere Mal auf Diffe- renz zwischen zwei Gruppen. Die Berechnung der Abweichungssumme entnehmen wir Kap. 15, sie hat eine Höhe von 2.42 bei 2 Freiheitsgraden. Damit ist die Testentscheidung dieselbe wie oben. Wir lehnen unsere Nullhypothese nicht ab.

16.3 Der 􏰅2-Test bei zwei voneinander abhängigen Stichproben: Wirkt meine Werbekampagne?

Manchmal müssen wir uns fragen, ob eine Maßnahme das Verhalten von Personen oder Objekten verändert, beispielsweise, ob eine von unserem Unternehmen durchgeführte Werbemaßnahme einen Einfluss darauf hat, ob Personen unser Produkt kaufen oder nicht.

H0: Die Werbekampagne hat keinen Einfluss darauf, ob Personen unser Produkt kaufen
HA: Die Werbekampagne hat einen Einfluss darauf, ob Personen unser Produkt kaufen

Lesen können wir die Matrix wie folgt: Vor der Kampagne hatten wir 80 + 50 = 130 Käu- fer und 100 + 70 = 170 Nicht-Käufer in der Stichprobe. Nach der Kampagne haben wir 80 + 100 = 180 Käufer und 50 + 70 = 120 Nicht-Käufer. Betrachten wir die Matrix näher, so stellen wir fest, dass von unseren ursprünglich 130 Käufern 50 zu den Nicht-Käu- fern und von unseren ursprünglichen 170 Nicht-Käufern 100 zu den Käufern gewechselt haben. Insgesamt haben wir 150 Wechsler in der Stichprobe.
Das Testverfahren, welches nun vergleicht, ob dieser Wechsel zufällig zustande kommt, ober ob unsere Werbemaßnahme darauf einen Einfluss hat, ist der McNemar 􏰅2-Test. Die- ser betrachtet nur die Wechsler, also die Zellen rechts oben (b) und links unten (c) in der Matrix und geht davon aus, dass die Hälfte der Wechsler von Käufern zu Nicht-Käufern wird und die andere Hälfte von Nicht-Käufern zu Käufern. Um das etwas zu verallgemei- nern, können wir auch sagen, dass die eine Hälfte der Wechsler von 0 auf 1 wechselt und die andere Hälfte von 1 auf 0.

16.4 Checkpoints
􏰌 - Die Testverfahren für nominale Daten beruhen auf der Analyse von Häufigkeiten.
􏰌 - Die Testverfahren für nominale Daten werden häufig kurz nur 􏰅2-Tests genannt.
􏰌 - Die Zellenbesetzung sollte bei 􏰅2-Testverfahren mindestens fünf Beobachtungen pro Zelle umfassen.

16.5 Berechnung mit dem R Commander

Den Befehl zur Berechnung der 􏰅2-Tests bei einer Stichprobe finden wir im Menü Statistik im Untermenü Anteile. Um den Befehle aktivieren zu können, müssen wir erst die für das Testverfahren benötigte Variable mit Hilfe des Menüs Datenmanagement und dem Untermenü Variablen bearbeiten in einen Faktor konvertieren. Nachdem wir den Befehl aufgerufen haben, öffnet sich ein Fenster, in welchem wir die Variable auswählen. In der Registerkarte Optionen geben wir zudem die Informationen für das Testverfahren ein. Wir spezifizieren die Alternativhypothese und den in der Alternativhypothese angenommen Anteilswert, ggf. das Konfidenzintervall sowie die Art des Testes. In der Regel nehmen wir die standardmäßig vorgegebene Version.

Statistik -> Anteile -> Datenmanagement (nominale Variablen) -> 

Das Ergebnis können wir wie folgt interpretieren. Im ersten Ausgabebereich sehen wir die beobachten Häufigkeiten, wir haben 65 Gründer und 35 Gründerinnen. Zudem sehen wir, dass wir den Test für unsere erste Ausprägung, die Null, d. h. für die Grün- der gemacht haben (test is for first level). Wir beantworten also die Frage, entspricht der Anteil der Gründer dem Geschlechteranteil in der Gesellschaft. Da wir nur zwei Ausprä- gungen haben, Gründer und Gründerinnen, ist das selbstverständlich äquivalent zu der Frage, ob der Anteil der Gründerinnen dem Geschlechteranteil in der Gesellschaft ent- spricht. Im zweiten Ausgabebereich ist das Testverfahren angegeben, der Anteilswerttest für eine Stichprobe (1-sample proportions test . . . ). In der zweiten Zeile sind die Daten angegeben und der Anteilswert in der Gesellschaft. Als nächstes sehen wir den 􏰅2-Wert in Höhe von 9.0. Diesen haben wir bereits oben in unserem Beispiel berechnet. Dahinter stehen die Freiheitsgrade und die Wahrscheinlichkeit, dass der Anteil an Gründern dem Geschlechteranteil in der Gesellschaft entspricht (p-Value). Die Wahrscheinlichkeit liegt bei 0.0027 bzw. 0.27 %. Daraus folgt, dass wir die Nullhypothese ablehnen und mit der in der vierten Zeile angegebenen Alternativhypothese weiterarbeiten. Der Anteil an Grün- dern entspricht nicht dem Geschlechteranteil in der Gesellschaft. In den Zeilen 5 bis 9

finden wir das 95 %-Konfidenzintervall und den für die Grundgesamtheit aus der Stich- probe geschätzten Anteilswert. Letzterer beträgt 65 %, das Konfidenzintervall reicht von 55.2 bis 73.6 %.
Der 􏰅2-Test bei zwei voneinander unabhängigen Stichproben kann, wie oben beschrie- ben, ebenso durchgeführt werden, wie der Test auf Unabhängigkeit. Beschrieben ist die Vorgehensweise bereits in Abschn. 15.5.
Für den 􏰅2-Test bei zwei voneinander abhängigen Stichproben steht uns kein Befehl über die Menüführung zur Verfügung. In diesem Fall müssen wir den Befehl kennen. An dieser Stelle möchte ich ermutigen, einmal zu versuchen, die Befehlsstruktur im Inter- net, entweder mit der Hilfefunktion des R Commanders oder mit einer Suchmaschine, zu suchen. 

Der Befehl, den wir finden, hat vermutlich folgende Struktur:
mcnemar.test(x, y, correct = FALSE)
Angewandt auf unser Beispiel lautet der Befehl entsprechend 
mcnemar.test(F_Vor, F_Nach, correct = FALSE)

Im Ergebnis sehen wir, dass wir den McNemar 􏰅2-Test durchgeführt haben. Der 􏰅2- Wert in Höhe von 16.7 entspricht unserer oben berechneten Abweichungssumme. Wir ha- ben 1 Freiheitsgrad und die Wahrscheinlichkeit, dass unsere Werbekampagne keinen Ein- fluss darauf hat, ob Personen unser Produkt kaufen ist sehr klein, 0.000045 bzw. 0.0045 %. Das heißt, wir lehnen unsere Nullhypothese ab, die Werbekampagne ist wirksam. Noch ein kleiner Hinweis, es könnte ja sein, dass unsere Werbekampagne wirkt, aber in die falsche Richtung, d. h. dass sie Personen abschreckt unser Produkt zu kaufen. Es ist daher immer sinnvoll, die oben im Beispiel angegebene Häufigkeitstabelle genau anzusehen.


16.6 Anwendung
16.1. Wir wollen wissen, ob es Unterschiede hinsichtlich der Anzahl an Dienstleistungsgründungen und Industriegründungen gibt. Wir betrachten dabei folgende Null- hypothese: Dienstleistungsgründungen und Industriegründungen kommen gleich häufig vor. Berechne das entsprechende Testverfahren mit dem R Commander zum Signifikanzniveau von 5 % und interpretiere das Ergebnis.
16.2. Uns interessiert, ob es zwischen Männern und Frauen Unterschiede bezüglich der Bedeutung der Gründungsmotive gibt. Berechne das entsprechende Testverfahren mit dem R Commander zum Signifikanzniveau von 5 % und interpretiere das Er- gebnis.
16.3. Wir führen in unserem Unternehmen eine Aufklärungskampagne bezüglich der Ernährung am Arbeitsplatz durch. Unser Ziel ist es, eine gesundheitsbewusste Er- nährung am Arbeitsplatz zu fördern. Wir beobachten dabei zufällig 200 Angestellte und fragen diese vor und nach der Kampagne nach ihrer Ernährung am Arbeits- platz. Mit Hilfe dieser Ergebnisse können wir folgende 2 × 2 Matrix erstellen:

S. 231

Berechne das entsprechende Testverfahren mit dem R Commander zum Signifikanzniveau von 10 % und interpretiere das Ergebnis.

16.7 Zusammenfassung und Überblick über die Testverfahren

-> Sehr wichtig !!! -> S. 232

Teil 4 - Regessionsanalyse

Die Regressionsanalyse: Die Möglichkeit vorherzusagen, was geschehen wird
Die Regressionsanalyse ist ein äußerst beliebtes Instrument, welches bei sehr vielen Frage- stellungen Anwendung findet. Wir könnten uns beispielsweise fragen, ob Aufwendungen für Marketing einen Einfluss auf das Unternehmenswachstum haben und was passiert, wenn wir die Aufwendungen erhöhen oder reduzieren. Wir könnten aber auch versuchen zu klären, welche Faktoren einen Einfluss auf die Leistung von Fußballmannschaften haben oder welcher europäische Fußballverein die Champions League voraussichtlich gewinnen wird: Barcelona, Bayern, Real Madrid oder doch Dortmund? Die Beispiele zeigen, dass die Einsatzmöglichkeiten vielfältig sind. Ganz allgemein nutzen wir die Re- gressionsanalyse zur Erklärung und zur Prognose von Sachverhalten. Um das nochmals zu verdeutlichen hier ein paar Fragestellungen:

- Welche Faktoren beeinflussen die Leistung einer Fußballmannschaft? Ist der Gesamt- wert des Fußballkaders oder das Vorhandensein eines Superstars zentral?
􏰌- Welchen Einfluss haben meine Marketingaufwendungen auf meine Verkaufszahlen? Was passiert, wenn ich Marketingaufwendungen erhöhe?
􏰌-  Welchen Einfluss haben Forschungs- und Entwicklungsausgaben auf die Innovationsra- te eines Landes? Was passiert, wenn ein Land seine Ausgaben für Grundlagenforschung erhöht?
􏰌- Welche Wirkung hat Entwicklungshilfe auf das Wachstum von Entwicklungsländern? Was passiert, wenn die Zahlungen erhöht werden?
􏰌- Welchen Einfluss hat Gewalt im Fernsehen auf die Gewaltbereitschaft von Jugendlichen? Was passiert, wenn die Fernsehsendungen gewaltreicher werden?

17 Die lineare Einfachregression

17.1 Ziel der lineraren Einfachregression

Das Ziel der linearen Einfachregression ist zu erklären, welchen Einfluss eine Variable X auf eine Variable Y ausübt und was mit der Variable Y passiert, wenn sich die Variable X verändert oder verändert wird. Y ist entsprechend die abhängige Variable und X die unabhängige Variable:

Y (abhänige Variable - metrisch) <------ X (unabhängige Varibale - metrisch)

Die Variable Y, die ab- hängige Variable, wird beeinflusst von der Variable X, der unabhängigen Variable. Beide Variablen weisen metrisches Skalenniveau auf.

17.2 Die lineare Regressionsgerade und die Methode der Kleinsten Quadrate

Mit Hilfe der Methode der kleinsten Quadrate wird der Abstand zwischen unseren Beobachtungen und der Geraden, die wir suchen, minimiert (Abb. 17.3). Wenn dieser Abstand minimal ist, haben wir die optimale Gerade gefunden.

Jetzt können wir uns noch der Minimierungsregel zuwenden. Ziel des Kleinsten-Qua- drate-Verfahrens ist es, die Summe des Abstandes zwischen beobachteten yi Werten und geschätzten yOi Werten zu minimieren. Den Abstand können wir auch wie folgt schreiben.

Die Veränderung beträgt 18.35 􏰍 16.27 = 2.08, was genau der Steigung entspricht. Wir sehen, wir können aus unseren beobachteten Werten die Regressionsgerade relativ einfach bestimmen und mit ihr den Sachverhalt erklären sowie Prognosen aufstellen. Ganz so einfach ist es dann aber doch wieder nicht. Zunächst müssen wir uns die Frage stellen, wie gut unsere berechnete Regressionsgerade den Zusammenhang erklärt.

17.3 Wie gut und wie viel können wir erklären, das R2

Bewegung (Varianz) von Y erklärt. Entsprechend bedeutet z. B. ein R2 von 0.3, dass die Regressionsgerade 30 % der Bewegung von Y erklärt, die weiteren 70 % können nicht durch die Regressionsgerade erklärt werden.

Zur Berechnung des R2s müssen wir zunächst den Mittelwert yN und die durch die Regressionsgerade geschätzten yOi ausrechnen. Anschließend bestimmen wir die Summe der Abweichungen der yi und setzen diese in die Formel ein. Das Ergebnis zeigt uns an, wie viel Prozent der Varianz von Y durch die Regressionsgerade erklärt werden. Wir wollen das Beispiel von oben weiterführen. 

Zusammenfassend können wir sagen, je höher das R2 ist, desto besser passt die Re- gressionsgerade zu den Daten und desto genauer können wir prognostizieren, was mit Y passiert, wenn wir X verändern. Ein hohes R2 ist somit ein Indiz für die Güte der Re- gressionsanalyse. In den Sozialwissenschaften sind wir dennoch oft bereits mit einem scheinbar kleinen R2, z.B. in Höhe von 0.2 oder 0.3, zufrieden. Der Grund hierfür ist, dass wir hier oft mit Konzepten arbeiten, die schwierig messbar und bei der Erhebung fehleranfällig sind. Die Daten sind daher relativ häufig nicht präzise und wir haben ein so- genanntes Rauschen in den Daten. Das R2 ist dann zwangsläufig oft relativ klein. Wie wir im Kap. 18 sehen werden, ist aber nicht nur das R2 für die Güte der Regressionsgerade ausschlaggebend, sondern wir können auch testen, ob die Regressionsgerade insgesamt einen Erklärungsgehalt besitzt.

17.4 Berechnung mit dem R Commander

Die Berechnung der linearen Einfachregression ist mit dem R Commander denkbar ein- fach. Zunächst prüfen wir mit Hilfe des Streudiagramms, ob zwischen abhängiger und unabhängiger Variable eine lineare Beziehung existiert. Wir geben im Menüpunkt Grafi- ken den Befehl Streudiagramm ein. Im sich öffnenden Fenster wählen wir die Variablen aus. Für die X-Variable wählen wir die unabhängige Variable und für die Y-Variable die abhängige Variable. In der Registerkarte Optionen entfernen wir alle Häkchen. Der visu- elle Eindruck soll nicht durch zusätzliche Informationen und Linien gestört werden.

Grafiken -> Streudiagramm -> (X,Y Variable)

Statistik -> Fitte Modelle -> Lineare Regression -> (X, Y Variable)

Bei der Interpretation der Ergebnisse konzentrieren wir uns auf die Werte, die wir be- reits kennen, die Steigung, den Achsenabschnitt, und das Bestimmtheitsmaß. Die Steigung befindet sich hinter der unabhängigen Variable Erfahrung mit der Überschrift Estimate. Estimate steht für Schätzwert, es handelt sich ja um einen aus der Stichprobe geschätzten Wert. Den Achsenabschnitt finden wir hinter dem Ausdruck Intercept. Auch hier handelt es sich selbstverständlich um einen geschätzten Wert. Das Bestimmtheitsmaß steht hin- ter dem Ausdruck Multiple R-squared (R2). Unsere Regressionsgerade ist entsprechend YO D 􏰍1:041 C 0:9709X bei einem Erklärungsgehalt von in etwa 38 %.

17.5 Ist eine unabhängige Variable genug, Out-of-Sample Vorhersagen und noch mehr Warnungen

Entsprechend müssen wir auch alle relevanten Variablen in das Re- gressionsmodell aufnehmen. Tun wir das nicht, so wird möglicherweise der Einfluss der aufgenommenen unabhängigen Variable überschätzt und unsere Prognosen sind ungenau.
Ein weiteres Problem bei Prognosen ist, dass wir solche normalerweise nur in dem Be- reich anstellen sollten, in welchem auch unsere Beobachtungen angesiedelt sind. Erstellen wir Prognosen außerhalb unseres Beobachtungsbereiches, sprechen wir von Out-of-Sam- ple Vorhersagen bzw. Vorhersagen außerhalb unserer Stichprobe. Problematisch bei Out- of-Sample Vorhersagen ist vor allem, dass wir annehmen müssen, dass die Beziehung, die wir in unseren Daten gefunden haben, auch über den beobachteten Wertebereich hinaus gilt. Dies kann, muss aber nicht so sein. Gilt das nicht, dann erstellen wir eine falsche Prognose. Vergleichen wir hierzu die entsprechende Abb. 17.6.

Noch eine letzte Bemerkung. Die lineare Regression berechnet eine Gerade. Das heißt aber auch, dass in den Daten eine lineare Beziehung bestehen muss. Ist diese nicht vor- handen, so ist die lineare Regression ungeeignet, die Beziehung darzustellen.

17.6 Checkpoints
􏰌
 - Mit Hilfe der linearen Einfachregression wird eine lineare Beziehung zwischen zwei metrischen Variablen abgebildet.
 -􏰌 Das Anwenden der Regressionsanalyse erfordert ein theoriegeleitetes Vorgehen. Wir benötigen eine saubere theoretische Fundierung, die uns zeigt, dass die unabhängige Variable einen Einfluss auf die abhängige Variable ausübt.
􏰌 - Die Berechnung der Regressionsgerade erfolgt mit Hilfe der Methode der kleinsten Quadrate.
􏰌 - Das Bestimmtheitsmaß R2 ist ein Mass für die Stärke des Zusammenhanges. Es erklärt, wie viel von der Veränderung von der abhängigen Variable durch die unabhängige Variable erklärt wird.
􏰌 - In der Regel reicht eine unabhängige Variable nicht aus, um die abhängige Variable ausreichend zu erklären, d. h. wir benötigen mehrere unabhängige Variablen.
􏰌 - Out-of-Sample Vorhersagen beruhen auf der Annahme, dass der entdeckte Zusammenhang auch über den Beobachtungsbereich hinaus gilt, und sind entsprechend vorsichtig anzuwenden.

17.7 Anwendung
17.1. Warum sind theoretische Überlegungen notwendig, bevor eine Regressionsanalyse durchgeführt werden soll?
17.2. Zeichne und berechne für die ersten acht Unternehmen unseres Datensatzes Da- ten_Wachstum von Hand das Streudiagramm, die Regressionsgerade und das Be- stimmtheitsmaß für die Variable Wachstumsrate und Marketing. Nutze als abhän- gige Variable die Wachstumsrate und als unabhängige Variable die Aufwendungen für Marketing. Interpretiere das Ergebnis.
17.3. Nutze das Ergebnis aus Aufgabe 2 und prognostiziere die Wachstumsrate für Mar- ketingaufwendungen in Höhe von 20 %. Gibt es ein Problem mit der Prognose?
17.4. Zeichne und berechne für die ersten acht Unternehmen unseres Datensatzes Da- ten_Wachstum von Hand das Streudiagramm, die Regressionsgerade und das Be- stimmtheitsmaß für die Variable Wachstumsrate und Produktverbesserung. Nutze als abhängige Variable die Wachstumsrate und als unabhängige Variable die Auf- wendungen für Produktverbesserungen. Interpretiere das Ergebnis.
17.5. Nutze das Ergebnis aus Aufgabe 4 und prognostiziere die Wachstumsrate für Auf- wendungen für Produktverbesserungen in Höhe von 20 %. Gibt es ein Problem mit der Prognose?
17.6. Zeichne und berechne für unseren Datensatz Daten_Wachstum mit Hilfe von R das Streudiagramm, die Regressionsgerade und das Bestimmtheitsmaß für folgende Variablenpaare: Wachstumsrate und Marketing, Wachstumsrate und Produktver- besserung und Wachstumsrate und Alter. Nutze als abhängige Variable die Wachs- tumsrate. Interpretiere die Ergebnisse.
17.7. Beschreibe mit Blick auf Aufgabe 6, warum eine unabhängige Variable nicht aus- reicht, um die Wachstumsrate zu erklären.

18. Die multiple Regressionsanalyse

Im vorangegangen Kapitel haben wir gesehen, dass in der Regel eine unabhängige Varia- ble nicht genügt, um die abhängige Variable ausreichend zu beschreiben. Normalerweise haben mehrere Faktoren einen Einfluss. Wir benötigen typischerweise die multiple Re- gressionsanalyse, auch multivariate Regressionsanalyse genannt, um einen Sachverhalt zu beschreiben. Mit dieser analysieren wir gleichzeitig den Einfluss mehrerer unabhängiger Variablen auf eine abhängige Variable.

Die abhängige Variable ist dabei metrisch, die unabhängigen Variablen sind eben- falls metrisch oder sogenannte Dummy-Variablen. Dummy-Variable ist der technische Ausdruck für nominale Variablen mit den Ausprägungen 0 und 1, z. B. Mann und Frau, Industrieunternehmen und Dienstleistungsunternehmen, katholisch und nicht-katholisch.

Das Ziel der multiplen Regressionsanalyse ist es zu beschreiben, welchen Einfluss ein Set von unabhängigen Variablen Xj auf eine abhängige Variable Y ausübt, und zu bestimmen, was mit Y passiert, wenn sich eine Variable Xj verändert oder verändert wird. Der Unterschied zur linearen Einfachregression ist, dass wir nicht mehr nur eine unabhängige Variable, sondern gleichzeitig mehrere unabhängige Variablen simultan untersuchen.
Obwohl wir gleichzeitig mehrere unabhängige Variablen simultan untersuchen, sind wir in der Regel trotzdem nur an einer dieser Variablen interessiert. Die anderen unabhän- gigen Variablen nehmen wir in die Regressionsanalyse auf, da auch sie einen Einfluss auf die abhängige Variable ausüben. Um den echten Einfluss der Variable, die von Interesse ist, zu ermitteln, müssen wir für den Einfluss der anderen Variablen kontrollieren. Tech- nisch sprechen wir daher auch von Kontrollvariablen. Wir ermitteln den Einfluss einer unabhängigen Variable auf Y unter Kontrolle aller anderen für den Sachverhalt relevanten Variablen.
Wir wollen dies noch einmal an einem Beispiel verdeutlichen. Uns interessiert der Ein- fluss der Branchenberufserfahrung auf das Unternehmenswachstum. Die Theorie zeigt an, dass die Branchenberufserfahrung einen Einfluss ausübt. Gleichzeitig entnehmen wir der Theorie aber auch, dass nicht nur die Branchenberufserfahrung wichtig für das Unter- nehmenswachstum ist, sondern ebenso Marketing, Forschung und Entwicklung, Branche, etc. eine Rolle spielen könnten. Um den echten Einfluss der Branchenberufserfahrung zu ermitteln, müssen wir daher für diese Faktoren kontrollieren.
Die Vorgehensweise der Schätzung der Regressionsfunktion ist mit dem Vorgehen bei der linearen Einfachregression identisch. Wir minimieren mit Hilfe der Methode der kleinsten Quadrate die quadrierten Abweichungen der Regressionsfunktion von den be- obachteten yi -Werten.

Bevor wir nun dieses Modell mit Hilfe von R schätzen (die Berechnung von Hand wird langsam aufwändig), müssen wir noch kurz auf die verschiedenen Masse zur Bestimmung der Güte der Regressionsfunktion eingehen.

18.2 F-Test, t-Test und Adjusted-R2

Zunächst sollte klar sein, dass wir die Regressionsfunktion aus einer Stichprobe schätzen. Damit erhalten wir die Regressionsfunktion für die Stichprobe. Da wir aber eine Aussa- ge über die Grundgesamtheit machen wollen, müssen wir die Regressionsfunktion testen. Testen können wir sowohl die gesamte Regressionsfunktion als auch die einzelnen Regres- sionskoeffizienten für die unabhängigen Variablen. Für die Regressionsfunktion lauten die Null- und die Alternativhypothese wie folgt:

H0: Die Regressionsfunktion trägt nicht zur Erklärung der abhängigen Variable bei HA: Die Regressionsfunktion trägt zur Erklärung der abhängigen Variable bei
Das Signifikanzniveau ist in der Regel  ̨ D 1 % bzw.  ̨ D 0:01.
Lehnen wir die Nullhypothese ab, gehen wir davon aus, dass die Regressionsfunktion die abhängige Variable in der Grundgesamtheit erklärt.

Mit den t-Tests überprüfen wir, welche der Variablen einen Erklärungsgehalt hat. Die- sen Tests können wir uns widmen, bevor oder nachdem wir das Bestimmtheitsmaß begut- achtet haben.
Das Bestimmtheitsmaß R2 kennen wir bereits. Es vergleicht die erklärte Varianz mit der Gesamtvarianz und sagt aus, wie viel Bewegung der Y Variable durch die Regressionsfunktion erklärt wird.

Bei der Analyse der Regressionsfunktion wird, insbesondere beim Vergleich verschie- dener Regressionsmodelle, oft nicht das einfache R2 verwendet, sondern ein sogenanntes „angepasstes- bzw. adjusted-R2“. Es ist genauso zu interpretieren wie das einfache R2. Der Hintergrund ist folgender: Es ist möglich, das R2 zu erhöhen, indem man mehr un- abhängige Variablen aufnimmt. Aus Gründen, die wir hier nicht diskutieren, führt die Hinzunahme einer weiteren unabhängige Variable nie zu einer Verkleinerung des R2. Damit können wir durch Hinzunahme von unabhängigen Variablen das R2 theoretisch beliebig erhöhen und eine erhöhte Erklärungskraft des Modells vortäuschen. Aus diesem Grund hat man sich ein Maß überlegt, dass für die Anzahl an aufgenommenen Variablen kontrolliert. 

18.3 Berechnung der multiplen Regression mit dem R Commander

Fitte  Modelle -> Lineare Regression -> (mehrere unab. Variablen auswählen)

Interpretation: 
 Wir können uns nun der Ergebnisinterpretation zuwenden. In der letzten Zeile finden wir den F-Wert und die Wahrscheinlichkeit, einen solch großen F-Wert zu erhalten, wenn die Nullhypothese korrekt ist (p-value). In unserem Fall ist die Wahrscheinlichkeit deut- lich kleiner als 1 %, d. h. wir lehnen die Nullhypothese ab. Entsprechend gehen wir von der Alternativhypothese, dass die Regressionsfunktion die abhängige Variable erklärt, aus. Das R2 in der Zeile darüber zeigt uns, dass unsere Regressionsfunktion circa 48 % der Bewegung der abhängigen Variable erklärt, was in der sozialwissenschaftlichen Forschung schon ein relativ hoher Wert ist.
Nun können wir die einzelnen unabhängigen Variablen betrachten. Diese finden wir im Koeffizientenblock der Ausgabe. Für jede Variable, einschließlich des Achsenabschnitts (Intercept), sind der Schätzwert (Estimate), der Standardfehler (Std. Error), der t-Wert (t value) und die Wahrscheinlichkeit angegeben, ob die Nullhypothese für die entsprechende Variable korrekt ist (Pr(>|t|)). Wir konzentrieren uns zunächst auf die Wahrscheinlich- keit. Für die Variable Alter ist die Wahrscheinlichkeit 71.52 %, für Branche 69.86 %, für Erfahrung 0.00 %, für Geschlecht 71.81 % für Marketing 0.15 % und für Produktverbes- serung 31.18 %. Das heißt, wir lehnen sowohl für die Variable Marketing als auch für die Variable Erfahrung unsere Nullhypothese ab. Diese Variablen tragen zur Erklärung der Wachstumsrate bei. Für die anderen Variablen können wir die Nullhypothese nicht ablehnen. In der ersten Spalte nach dem Variablennamen finden wir zudem noch unsere Schätzwerte für die Koeffizienten. Mit diesen können wir die Regressionsfunktion auf- stellen. 

Sehen wir uns nun die Regressionsfunktion näher an. Zuerst ist festzustellen, dass wir die Regressionsfunktion für alle geschätzten Parameter aufgestellt haben, unabhängig da- von, ob diese einen Erklärungsgehalt haben oder nicht. Dies ist hier immer der Fall, wir haben die Regressionsfunktion ja mit Hilfe eben dieser Variablen geschätzt. b0 ist der Wert der unabhängigen Variable, wenn alle unabhängigen Variablen die Ausprägung null be- sitzen. In unserem Fall ist die Wachstumsrate 􏰍2.55 %, wenn wir für alle unabhängigen Variablen den Wert null einsetzen, z. B. wenn null Prozent vom Umsatz für Marketing aufgewendet wird, etc. Die Koeffizienten b1 bis b6 geben an, um wie viel sich die Wachs- tumsrate verändert, wenn wir die jeweilige Variable um eins erhöhen. Voraussetzung ist, dass alle anderen Variablen unverändert bleiben. Der Koeffizient lässt sich nur auf je- ne Variablen anwenden, die einen Erklärungsgehalt haben. In unserem Fall sind das die Variablen Marketing und Erfahrung. Z. B. können wir sagen was passiert, wenn wir die Variable Marketing um eins erhöhen, die Wachstumsrate steigt dann um 0.15 Prozent- punkte. Wenn sich die Variable Erfahrung um eins erhöht, steigt die Wachstumsrate um 0.93 Prozentpunkte.

18.4 Wann ist die Kleinste-Quadrate-Schätzung BLUE?

Die Schätzung der Regressionsfunktion haben wir mit Hilfe der Methode der kleinsten Quadrate durchgeführt. Diese Methode führt zu den bestmöglichen Ergebnissen, wenn bestimmte Voraussetzungen erfüllt sind. Diese Voraussetzungen müssen wir uns noch an- sehen und diskutieren. Im Folgenden sind die Voraussetzungen aufgelistet:
1. Die Regressionsfunktion ist richtig spezifiziert und enthält alle relevanten unabhängi- gen Variablen. Die Beziehung zwischen den unabhängigen Variablen und der abhän- gigen Variable ist linear.
2. Die Abweichungen der beobachteten Y -Werte von den geschätzten YO -Werten haben einen Erwartungswert von null.
3. Die Abweichung korreliert nicht mit den unabhängigen Variablen.
4. Die Varianz der Abweichungen ist konstant.
5. Zwei oder mehrere unabhängige Variablen sind nicht miteinander korreliert.
6. Die Abweichungen sind zueinander unkorreliert.
7. Die Abweichungen sind normalverteilt.
Unter diesen Voraussetzungen ist der Kleinste-Quadrate-Schätzer BLUE, er ist der bes-
te, lineare, unverzerrte und effizienteste Schätzer, den wir kennen.

Die meisten dieser Annahmen analysieren wir mit Hilfe der Abweichung der beobachteten Y -Werte von den geschätzten YO-Werten, den Residuen. Wir können den R Commander leicht anweisen, uns die Residuen zu unserem Datensatz hinzuzufügen. Hierfür wählen wir im Anschluss an das Schätzen des Regressionsmodells im Menü Modelle den Befehl Füge Regressionsstatistiken zu den Daten hinzu und wählen die standardisierten Residu- en aus (studentisierte Residuen), indem wir hier einen Haken setzen. Ferner wählen wir noch die Fallbeschriftung und die vorhergesagten Werte aus. Diese benötigen wir, um die Annahmen vier und sechs zu testen. Zwei kleine Hinweise: Erstens, bei den studentisier- ten Residuen handelt es sich um die standardisierten Residuen (vgl. zur Standardisierung einer Variable Kap. 10), der zu standardisierende Wert geht bei der Standardisierung aber nicht in die Berechnung mit ein. Zweitens, wir nutzen die studentisierten Residuen bei der Analyse, da Verletzungen von Annahmen mit Hilfe der studentisierten Residuen leichter zu erkennen sind als dies mit den nicht standardisierten Werten der Fall wäre.

GUI: Modelle -> Fuege Regressionsstatistik zu den Datensätzen hinzu
 - vorhergesagte Werte
 - studentisierbare Residuen 
 - Fallbeschriftung

18.5 Checkpoints

􏰌 - Mit Hilfe der multiplen Regression analysieren wir den Einfluss mehrerer unabhängi- ger Variablen auf eine abhängige Variable.
􏰌 - Die abhängige Variable ist metrisch, die unabhängigen Variablen sind metrisch oder Dummy-Variablen.
 - Mit Hilfe des F-Tests testen wir, ob die gesamte Regressionsfunktion in der Lage ist, die abhängige Variable zu erklären.
 - Mit Hilfe des t-Tests testen wir, ob einzelne unabhängige Variablen einen Erklärungsbeitrag leisten.
 - Die Methode der kleinsten Quadrate zur Schätzung der Regressionsfunktion ist BLUE, wenn bestimmte Voraussetzungen erfüllt sind.
 - Wenn eine oder mehrere Voraussetzungen nicht erfüllt sind, dann gibt es Schätzverfah- ren, die bessere Ergebnisse liefern als die Kleinste-Quadrate-Methode.

18.6 Anwendung

18.1. Berechne die Regressionsfunktion aus diesem Kapitel ohne die unabhängige Variable Alter.
18.2. Teste, ob die Voraussetzungen dafür erfüllt sind, dass die Schätzung der Regressionsfunktion mit Hilfe der Methode der kleinsten Quadrate das beste unverzerrte und effizienteste Ergebnis liefert.
18.3. Haben wir durch das Weglassen der Variable Alter das Problem der Multikollinearität gelöst?

19 Kurzbericht zu einer Forschungsfrage

19.1 Inhalte einer empirischen Arbeit

Nach der Datenauswertung müssen wir die Ergebnisse in der Regel noch schriftlich, in Form einer Studienarbeit, einer Bachelor- oder Masterarbeit oder in Form eines Journals festhalten. Dabei sind immer folgende Punkte zu diskutieren:

1. die Problemstellung,
2. die Fragestellung,
3. die Literatur,
4. die Daten und die Methode,
5. die empirischen Ergebnisse,
6. die Zusammenfassung und die Schlussfolgerungen.


Beim Punkt Problemstellung wird angesprochen, warum man sich mit dem Thema
beschäftigt. Wenn möglich gibt es einen Aufhänger in Form einer aktuellen politischen Diskussion, etc. Aus der Problemstellung wird die Fragestellung direkt abgeleitet. Der Le- ser des Berichts erkennt so, warum diese Fragestellung ausgewählt wurde. Im Anschluss daran wird in einem Literaturteil der Stand des Wissens dargestellt und es werden ggfs. Hypothesen mit Bezug zur Fragestellung und zur Literatur formuliert. Anschließend sind die Methode und die Daten zu besprechen, die gewählt wurden, um die Fragestellung zu beantworten bzw. die Hypothesen zu testen. Der nächste Schritt beinhaltet die Präsentation der empirischen Ergebnisse. Zum Schluss sind die Ergebnisse noch zusammenzufassen, zur Literatur in Beziehung zu setzen und es ist zu diskutieren, welche Schlussfolgerungen daraus gezogen werden können. Um dies zu verdeutlichen, wollen wir im Folgenden zwei Beispiele für unterschiedliche Fragestellungen heranziehen. Hierbei darf nicht vergessen werden, dass es sich nicht um vollständige Forschungsberichte, sondern nur um „fiktive“ Skizzen/Kurzberichte handelt. Es wurde keine echte Literaturanalyse durchgeführt und die Ergebnisse basieren auf simulierten Daten. 

-> Das heißt, sowohl die Ergebnisse als auch die Kurzberichte haben nichts, rein gar nichts, mit der Realität zu tun.



Anhang 1: Lösungen zu den Anwendungen
Kapitel 1
1.1 Erstens wird mit Statistik Wissen erzeugt und wir können selbst Wissen generieren. Zweitens ermöglicht uns die Statistik fundierte Entscheidungen zu treffen. Drittens können wir mit Wissen über die Statistik Analysen, Studien und Aussagen basierend auf Daten besser einzuschätzen und Manipulationsversuche erkennen.
1.2 Im Datensatz sind folgende drei Hauptinformationen enthalten: über welche Objekte haben wir Informationen; worüber haben wir zu den Objekten Informationen; die Information selbst.
1.3 Nominal, ordinal und metrisch: Ein nominales Skalenniveau ermöglicht die Unter- scheidung der Untersuchungsobjekte. Ein ordinales Skalenniveau gibt uns neben der Unterscheidung auch eine Information über die Rangordnung. Ein metrisches Skalenniveau erlaubt eine Unterscheidung, gibt eine Rangordnung wieder und er- möglicht eine präzise Abstandsbestimmung.
1.4 Die Variable Branche ist nominal, die Variable Selbsteinschätzung ist ordinal und die Variable Umsatz ist metrisch.
1.5 Die Variable Bildung mit den Ausprägungen Sekundarschule, Matura . . . ist ordinal, die Ausprägungen ermöglichen eine Rangordnung. Die Variable Bildung gemessen in Jahren ist metrisch, neben der Rangordnung ermöglicht das Messniveau zudem eine genaue Abstandsbestimmung. Interessant ist hier, dass derselbe Sachverhalt unterschiedlich gemessen werden kann.
1.6 Das Skalenniveau einer Variablen bestimmt neben der Fragestellung, welches sta- tistische Verfahren wir einsetzen können.
1.7 Eine Legende ist notwendig, da die Daten in der Regel kodiert sind. Mit Hilfe der Legende entschlüsseln wir die Kodierung und können so die Bedeutung der Daten immer, auch zu einem späteren Zeitpunkt, nachvollziehen.
1.8 Der Datensatz umfasst 100 Beobachtungen. Er enthält drei nominale, zwei ordinale und fünf metrische Variablen (der Laufindex wurde dabei nicht mitgezählt).
1.9 Über die Vertrauenswürdigkeit der Quelle entscheiden die Seriosität der Quelle und unser Kenntnisstand über sie. Hier handelt es sich nicht um einen echten, sondern um einen für Lehrzwecke simulierten Datensatz.
1.10 EineLösungfindetsichinKap.8.

Kapitel 3
3.1 Der Modus kommt bei nominalen, ordinalen und metrischen Daten zum Einsatz. Die Berechnung des Medians ist bei ordinalen und metrischen Daten sinnvoll. Die Berechnung des arithmetischen Mittelwertes erfordert metrische Daten. Der geome- trische Mittelwert verlangt metrisch-verhältnisskalierte Daten.
3.2 xNProduktverbesserung D 6 %; xNMarketing D 20 %. Der Mittelwert ist bei der Variable Mar- keting höher, d. h. die Unternehmen wenden im Durchschnitt einen höheren Anteil vom Umsatz für Marketing auf.
3.3 MeSelbsteinschätzung D 4; MeBildung D 1,5. Der Median hat bei der Variable Selbst- einschätzung einen Wert von 4. 50 % der Unternehmen haben einen höheren Wert, 50 % einen niedrigeren Wert. Der Median bei der Variable Bildung liegt beim Wert 1.5. 50 % der Unternehmen haben einen höheren Wert, 50 % einen niedrigeren Wert.
3.4 MoGeschlecht D 0 & 1; MoErwartung D 2. Die häufigsten Werte bei der Variable Geschlecht sind 0 & 1. Wir haben gleich viele Gründer und Gründerinnen in der Stichprobe. Der häufigste Wert bei der Variable Erwartung ist 2. Die meisten Unternehmen erwarten keine Veränderung in der zukünftigen Entwicklung.
3.5 Nein, die Variable ist nominal skaliert.
3.6 Die Ergebnisse werden im Folgenden schematisch nur für die Wachstumsrate dargestellt. Zu beachten ist, dass bei metrischen Variablen der arithmetische Mittelwert, der Median und der Modus zu berechnen sind, bei ordinalen Variablen der Median und der Modus und bei nominalen Variablen nur der Modus.
3.7 Der durchschnittliche Wachstumsfaktor beträgt 1.18, die durchschnittliche Wachstumsrate 18 %.
3.8 Der arithmetische Mittelwert reagiert sensibel auf Ausreißer, da alle Werte in die Berechnung eingehen. Beim Median und beim Modus werden Extremwerte nicht berücksichtigt, daher reagieren diese nicht sensibel auf Ausreißer.

Kapitel 4
4.1 Die Spannweite und der Quartilsabstand können bei ordinalen und metrischen Daten eingesetzt werden. Die Standardabweichung und die Varianz benötigen metrische Daten.
4.2 Bei nominalen Daten wird kein Streuungsmaß benötigt, da die Daten nicht um einen Wert streuen.
4.3 SWMarketing D 21:0; varMarketing D 58:86; sMarketing D 7:67; QAMarketing D 12:5; vkMarketing D 35:68:
4.4 SWProduktverbesserung D 9:0; varProduktverbesserung D 8:00; sProduktverbesserung D 2:83; QAProduktverbesserung D 3:5; vkProduktverbesserung D 56:57:
4.5 Der Variationskoeffizient ist das benötigte Streuungsmaß. Die Abweichung der ein- zelnen Unternehmen vom Mittelwert ist bei der Variable Produktverbesserung größer.
4.6 Die Ergebnisse werden im Folgenden schematisch nur für die Variable Marketing dargestellt. Zu beachten ist, dass bei metrischen Variablen der kleinste Wert, der größte Wert, der Quartilsabstand und die Standardabweichung zu berechnen sind, bei ordinalen Variablen der kleinste Wert, der größte Wert und der Quartilsabstand und bei nominalen Variablen nichts.

