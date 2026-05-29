---
title: Recherche-Standard
description: Quellen-Tier-System, Methodik-Sektion, Einsehungs-Status.
---

# Recherche-Standard

Jede Recherche zu einem Begriff folgt einem schriftlich
festgehaltenen Standard (`docs/recherche/README.md` im Quellrepo).
Die wichtigsten Regeln in Kurzform:

## 1. Quellen-Tier-System

Jede zentrale Aussage im Recherche-Bericht nennt die Quelle mit
ihrer Qualitäts-Stufe:

| Tier | Quellentyp | Beispiele |
|---|---|---|
| **Hoch** | Normen, Gesetze, anerkannte Lehrbücher | DIN, EN, SIA, ÖNORM, „Mönck/Rug: Holzbau-Bemessung" |
| **Mittel-Hoch** | Offizielle Doku, akademische Quellen | Lignum HBT, Lignatec, Google Scholar |
| **Mittel** | CAD-Hersteller-Doku, Berufsschul-Material | cadwork-Knowledge-Base, Wikipedia |
| **Mittel-Niedrig** | Fach-Foren, Praxis-Blogs mit Autor | Zimmerer-Treff, Holzwurm-Page |
| **Niedrig** | Massenmedien, anonyme Quellen | allgemeine Hausbau-Portale |

Bei Kollision zwischen Tiers gilt die höher eingestufte Quelle.

## 2. Falsifizier-Bereitschaft

Wenn eine Recherche die Auftrags-Hypothese widerlegt, wird das
**klar gesagt**, nicht umschifft. Bei Teil-Bestätigung trennen die
Sektionen „Was passt" und „Wo es hakt".

## 3. Schweizer vs. deutsche Praxis

Wenn die Recherche länderspezifische Konventionen berührt
(DACH-Holzbau, Norm-Anwendung, regionale Benennungen), werden CH
und DE getrennt ausgewiesen, wenn sie abweichen. Bei Identität
explizite Bestätigung.

## 4. Methodik-Sektion

Jeder Bericht trägt eine eigene Methodik-Sektion: welche Tools
eingesetzt (WebFetch, WebSearch, PDF-Direktblick), welche Quellen
**nicht zugänglich** waren (Paywall, Cache-Issues), welche Aussagen
**Vermutung** sind statt bestätigte Fakten.

## 5. Ehrliche Markierung von Unrecherchierbarem

Punkte aus dem Auftrag, die nicht abschließend recherchierbar
waren, werden explizit markiert — nicht weggelassen.

## 6. Bericht ist Beleg

Nach Status `final` ist der Bericht-Inhalt unveränderlich. Wird er
später überholt, kommt ein neuer Bericht hinzu; der alte bleibt
mit Status „abgelöst durch …" stehen. Recherche-Geschichte wird
nicht überschrieben.

## Quellen-Hierarchie und Einsehungs-Status

Norm- und Lehrbuch-Verweise tragen einen **Einsehungs-Status**, der
sichtbar macht, ob die Quelle direkt im Volltext eingesehen wurde,
nur in Vorschau-Form vorlag oder über eine Sekundärquelle
rekonstruiert ist.

| Marker | Bedeutung |
|---|---|
| (kein Marker) | via Sekundärquelle rekonstruiert (Default) |
| `[direkt]` | Volltext direkt eingesehen |
| `[einsicht: vorschau-pdf]` | nur kostenlose Vorschau eingesehen (Inhaltsverzeichnis, Auszug) |
| `[einsicht: snippet]` | nur Snippet direkt eingesehen (Google-Books, Suchergebnis-Snippet mit zitiertem Wortlaut) |
| `[via: <Quelle>]` | konkrete Sekundärquelle benannt |

Hintergrund: Norm-Volltexte sind häufig paywalled. Recherche
rekonstruiert ihre Aussagen oft aus Sekundärquellen — das ist
fachlich tragfähig, muss aber transparent sein. Der Default
„via Sekundärquelle" reflektiert die ehrliche Voreinstellung:
solange Direkteinsicht nicht ausgewiesen ist, gilt die Quelle als
nicht direkt verifiziert.

Wikipedia und vergleichbare Korpus-Quellen sind grundsätzlich
Sekundärlit, nicht Primärquelle.
