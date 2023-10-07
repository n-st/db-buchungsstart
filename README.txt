DB-Buchungsstart-Rechner/Schätzer
=================================

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

Annahmen:
- Der Buchungsbeginn "Mitte Oktober" ist exakt 60 Tage vor dem Fahrplanwechsel
  (und fällt somit immer auf einen Mittwoch).
  Das ist nirgends offiziell garantiert, war aber zumindest 2021, 2022 und
  2023 so.
- "180 Tage vorher" ist offenbar einschließlich des betroffenen Tages
  gerechnet, d.h. an Tag x kann man tatsächlich nur Ticket bis Tag (x+179)
  buchen.

WICHTIGER HINWEIS:
Alle Angaben ohne Gewähr.
(Insbesondere, aber nicht ausschließlich, ist der Verkaufsbeginn im Oktober
eine Vermutung, und die Rechnung 179/180-Tage-vorher ist eventuell off-by-1.)
