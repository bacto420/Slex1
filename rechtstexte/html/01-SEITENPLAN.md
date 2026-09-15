# Seitenplan — was ersetzen, was ausblenden, was bleibt

Stand eurer Seitenliste vom 15.09.2026.

## 1. Vier Seiten überschreiben statt neu anlegen

Weniger Arbeit, und bestehende Links bleiben erhalten. Bei jeder Seite:
Inhalt komplett löschen → `<>` anklicken → HTML einfügen → Titel und URL
anpassen → speichern.

| Bestehende Seite | Wird zu | Neuer Titel | URL ändern auf | HTML-Datei |
| --- | --- | --- | --- | --- |
| Imprint | Impressum | Impressum | `impressum` | `impressum.html` |
| Data protection | Datenschutzerklärung | Datenschutzerklärung | `datenschutz` | `datenschutz.html` |
| General Terms and Conditions | AGB | Allgemeine Geschäftsbedingungen | `agb` | `agb.html` |
| Cancellation policy | Widerrufsbelehrung | Widerrufsbelehrung | `widerrufsbelehrung` | `widerrufsbelehrung.html` |

Die URL steht rechts unter *Suchmaschineneintrag → bearbeiten*. Shopify
fragt beim Ändern, ob eine Weiterleitung von der alten Adresse angelegt
werden soll — **ja** anklicken, dann laufen alte Links nicht ins Leere.

## 2. Eine Seite neu anlegen

| Titel | URL | HTML-Datei |
| --- | --- | --- |
| Cookie-Richtlinie | `cookies` | `cookies.html` |

Achtung: Shopify macht aus dem Titel automatisch `cookie-richtlinie`. Das
muss auf `cookies` korrigiert werden, sonst finden Footer und Cookie-Banner
die Seite nicht.

## 3. Sechs Seiten ausblenden

Sichtbarkeit auf **Versteckt** setzen — nicht löschen. Alte Rechtstexte
sollte man aufheben können: Bei einer Beschwerde zu einer Bestellung aus 2024
zählt, was damals galt.

| Seite | Warum weg |
| --- | --- |
| CCPA Privacy Policy | Kalifornien |
| PIPEDA Privacy Policy | Kanada |
| APPI Privacy Policy | Japan |
| LGPD Privacy Policy | Brasilien |
| GDPR Privacy Policy | Doppelt zur neuen Datenschutzerklärung |
| Do not sell or share my personal information | Kalifornien (CCPA) |

Diese sechs sind Shopify-Vorlagen für andere Rechtsräume. Sie gelten für euch
nicht, widersprechen der neuen Datenschutzerklärung teilweise und machen im
Streitfall unklar, welche Aussage bindend ist.

## 4. Diese Seiten bleiben, wie sie sind

| Seite | Warum |
| --- | --- |
| Blog, Media | eure Galerieseiten |
| CONTACT | Kontaktseite |
| ABOUT | Markengeschichte |
| RETURN | ist bereits versteckt, kann so bleiben |

**Terms of payment and dispatch** ist eine Ermessensfrage. Der Inhalt steckt
jetzt in den AGB (Punkte 3 bis 5). Entweder ausblenden — oder sichtbar lassen
als kundenfreundliche Übersicht. Wenn sichtbar: **Inhalt an die AGB
angleichen.** Zwei Seiten, die unterschiedliche Lieferzeiten oder
Versandkosten nennen, sind schlimmer als eine Seite zu wenig.

## 5. Nicht vergessen: die Shopify-Richtlinien

Getrennt von den Seiten führt Shopify unter **Einstellungen → Richtlinien**
eigene Texte: Rückerstattungen, Datenschutz, AGB, Versand und
Kontaktinformationen. Die erscheinen **im Checkout** und unter Adressen wie
`/policies/refund-policy`.

Das ist ein eigener Satz Texte, den viele übersehen. Sind die leer oder
enthalten sie noch Shopify-Vorlagen, steht im Checkout etwas anderes als auf
euren Seiten — und der Checkout ist der Ort, an dem der Vertrag zustande
kommt.

Empfehlung: dort dieselben Inhalte einsetzen.

| Shopify-Richtlinie | Inhalt aus |
| --- | --- |
| Rückerstattungsrichtlinie | `widerrufsbelehrung.html` |
| Datenschutzrichtlinie | `datenschutz.html` |
| AGB | `agb.html` |
| Versandrichtlinie | AGB Punkt 5, plus Rücksendekosten |
| Kontaktinformationen | Anbieter und Kontakt aus `impressum.html` |

## 6. Zum Schluss prüfen

- Footer: erscheinen Impressum, AGB, Datenschutz, Widerrufsbelehrung?
  Sie tauchen automatisch auf, sobald die Seiten unter den richtigen
  Adressen liegen.
- Cookie-Banner: funktionieren die zwei Links darunter?
- Einen Testkauf bis zum Checkout durchklicken: stehen dort die richtigen
  Richtlinien?
