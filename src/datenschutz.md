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

## Security-Header — was geht, was nicht

Diese Site wird über **GitHub Pages** ausgeliefert. GitHub Pages
erlaubt keine Custom-HTTP-Header-Konfiguration (kein `_headers`,
kein `.htaccess`, kein eigener Web-Server). Manche der von Webbkoll
oder Mozilla Observatory geprüften Security-Header lassen sich
deshalb ausschließlich über HTML-`<meta>`-Tags setzen — die wirken
genauso, solange der Browser sie verarbeitet:

| Header | Auf dieser Site gesetzt | Mechanismus |
|---|---|---|
| **Content-Security-Policy** | ✓ | `<meta http-equiv>` im `<head>` |
| **Referrer-Policy** | ✓ (`strict-origin-when-cross-origin`) | `<meta name="referrer">` im `<head>` |
| **Strict-Transport-Security** (HSTS) | nicht setzbar auf GitHub Pages | nur als echter HTTP-Header möglich |
| X-Content-Type-Options | nicht setzbar | nur als HTTP-Header möglich |
| X-Frame-Options | funktional ersetzt | über CSP `frame-ancestors 'none'` |
| Permissions-Policy | nicht setzbar | nur als HTTP-Header möglich |

**Warum die fehlenden Header hier in der Praxis kaum schaden:**

- Die Site setzt **keine Cookies** und nutzt **keine Sessions**.
  Ein HSTS-Mangel macht primär Cookie-Diebstahl bei
  Downgrade-Angriffen kritisch — beides ist hier nicht relevant.
- HTTPS-Enforce ist im GitHub-Pages-Setting aktiv: jeder
  HTTP-Aufruf wird per Server-Redirect auf HTTPS umgelenkt. Eine
  erste Verbindung über HTTP wird also nicht statisch ausgeliefert.
- Die Site liefert ausschließlich statisches HTML/CSS/JS. Es gibt
  keine User-generierten Inhalte, keine Eingabe-Formulare (außer
  der browser-internen Volltextsuche), keine Datei-Uploads und
  keine Authentifizierung — die Angriffsfläche, die die fehlenden
  Header sonst schützen würden, existiert hier nicht.

Wer maximalen Schutz im Hosting-Layer braucht, müsste die Site
hinter ein CDN setzen, das Custom-Header injiziert (Netlify,
Cloudflare Pages). Das ist hier bewusst nicht gemacht — der
Plattform-Tradeoff ist transparent dokumentiert.

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
