---
title: Datenschutz
---

# Datenschutz

Diese Seite verarbeitet so wenig personenbezogene Daten wie technisch
möglich. Im Einzelnen:

## Keine Cookies, kein Tracking

Es werden **keine Cookies gesetzt**, kein Analytics-Tool eingebunden,
keine Tracking-Pixel geladen und keine Drittanbieter-Skripte für
Werbe- oder Statistikzwecke nachgeladen. Die Volltext-Suche läuft
vollständig im Browser; Suchanfragen werden nicht an einen Server
gesendet.

Schriften (Inter, JetBrains Mono) werden bei jedem Build über das
Material-Privacy-Plugin lokal in den Site-Bundle geholt und von
holzbau-glossar.ch direkt ausgeliefert — es gibt **keine Live-Anfrage**
mehr an `fonts.googleapis.com` oder `fonts.gstatic.com` beim Laden
einer Seite.

## Unabhängig prüfen

Die obigen Behauptungen sollst du nicht glauben müssen, sondern
nachvollziehen können. Zwei Belege:

1. **Build-Privacy-Check** (eigene, transparente Quelle):
   die Datei `https://holzbau-glossar.ch/privacy-check.json` wird bei
   jedem Site-Build automatisch erzeugt. Der Build-Hook scannt alle
   gerenderten HTML-Seiten nach 22 typischen Tracker-Mustern (Google
   Analytics, GTM, Matomo, Plausible, Hotjar, Sentry, Cloudflare
   Insights u. a.) und nach externen `<link>`/`<script>`/`<img>`-
   Quellen. Das JSON nennt den Build-Tag und die Trefferzahlen.
   Aufrufen, die Datei ist menschenlesbar.

2. **Unabhängige Live-Prüfung** über
   [Webbkoll](https://webbkoll.5july.net/en/check?url=holzbau-glossar.ch),
   die Privacy-Test-Plattform der schwedischen Datenschutz-Stiftung
   `5 juli stiftelsen`. Der Test ist Open-Source, ohne Login und ohne
   Anbieter-Interesse an einem bestimmten Ergebnis. Er prüft auf
   Third-Party-Requests, Cookies, HTTP-Header, HSTS, Referrer-Policy
   und ähnliches. Der Link öffnet eine vorausgefüllte Maske; ein Klick
   auf den Test-Button startet die Analyse.

Build-Stand des angezeigten Privacy-Checks: **{{BUILD_DATE}}**.

## Server-seitige Zugriffsprotokolle

Die Seite wird über **GitHub Pages** ausgeliefert. GitHub erstellt
serverseitig technische Zugriffsprotokolle, die u.a. IP-Adressen,
Zeitstempel und die abgerufene URL enthalten können. Diese Protokolle
liegen ausschließlich in der Verantwortung von GitHub. Details siehe
[GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement)
und [GitHub Pages Data Collection](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement).

## Externe Verweise

Die Glossar-Einträge verweisen auf externe Quellen (Normen-Verlage,
Wikipedia, Online-Wörterbücher). Beim Anklicken solcher Links verlassen
Sie diese Seite; für die Datenverarbeitung der Zielseiten sind deren
Betreiber verantwortlich.

## Hosting der Quellen

Quellcode und Glossar-Inhalte werden öffentlich auf GitHub gehostet
([github.com/steinerschueler/holzbau-glossar](https://github.com/steinerschueler/holzbau-glossar)).
Das DOI-System wird über Zenodo (CERN) bereitgestellt
([zenodo.org](https://zenodo.org)).

## Kontakt

Für Fragen zum Datenschutz siehe die Kontaktangaben im
[Impressum](impressum.md).
