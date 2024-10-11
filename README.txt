DB-Buchungsstart-Rechner/Schätzer
=================================

Update 2024/25
--------------

Mit Veröffentlichung des Fahrplans für 2025 ändert sich der Vorbuchungszeitraum
und möglicherweise auch der Vorbuchungsbeginn für Fahrten nach dem Fahrplanwechsel:
https://www.tagesschau.de/wirtschaft/verbraucher/bahn-vorbuchungsfrist-100.html

!!! Die von diesem Skript berechneten Zeiten sind daher für Reisedaten
!!! >= 2024-12-08 voraussichtlich NICHT KORREKT.

Kurzfassung:
- Zugtickets können bei der Deutschen Bahn i.d.R. 180 Tage im Voraus gebucht
  werden.
- Bei Sparpreisen lohnt es sich, möglichst früh zu buchen.
- Allerdings wird jeweils zum zweiten Sonntag im Dezember der Fahrplan
  aktualisiert. Ticketbuchungen für den "neuen" Fahrplan sind erst ab Mitte
  Oktober (d.h. teilweise weniger als 180 Tage im Voraus) möglich.

Dieses Skript berechnet den frühestmöglichen Tag, an dem Tickets für ein
gegebenes Datum gebucht werden können.
Das Ergebnis kann u.a. als lange Liste aller Daten, sowie als iCalendar-Datei
exportiert werden.

=== Die iCalendar-Dateien gibt es auch fertig hier in den Github-RELEASES ===>

WICHTIGER HINWEIS:
Alle Angaben ohne Gewähr.

Annahmen:
- Der Fahrplanwechsel ist am zweiten Sonntag im Dezember.
- Der Buchungsbeginn "Mitte Oktober" ist exakt 60 Tage vor dem Fahrplanwechsel
  (und fällt somit immer auf einen Mittwoch).
  Das ist nirgends offiziell garantiert, war aber zumindest 2021, 2022 und
  2023 so.
- "180 Tage vorher" ist einschließlich des betroffenen Tages gerechnet, d.h.
  an Tag x kann man tatsächlich nur Ticket bis Tag (x+179) buchen (aktuell
  getestet für den Fahrplan 2024).
- Verkaufsbeginn ist jeweils um Mitternacht Ortszeit in Deutschland (+ ggf.
  ein paar Minuten, bis sich der Cache des DB-Verkaufssystems aktualisiert
  hat).
