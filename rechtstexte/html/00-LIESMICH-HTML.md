# Fertige HTML-Blöcke zum Einfügen

Diese fünf Dateien sind die Rechtstexte als fertiges HTML. Sie werden in
Shopify als Seiteninhalt eingefügt — nicht ins Theme.

## So fügst du sie ein

Für jede der fünf Dateien:

1. **Onlineshop → Seiten → Seite hinzufügen**
2. **Titel** eintragen (siehe Tabelle unten)
3. Im Inhaltsfeld oben rechts auf **`<>`** klicken („Code anzeigen")
4. Den **gesamten** Inhalt der HTML-Datei hineinkopieren
5. Rechts unter *Suchmaschineneintrag* prüfen, dass die **URL** stimmt
6. Sichtbarkeit auf **Sichtbar**, dann Speichern

| Datei | Seitentitel | URL muss enden auf |
| --- | --- | --- |
| `impressum.html` | Impressum | `/pages/impressum` |
| `datenschutz.html` | Datenschutzerklärung | `/pages/datenschutz` |
| `cookies.html` | Cookie-Richtlinie | `/pages/cookies` |
| `widerrufsbelehrung.html` | Widerrufsbelehrung | `/pages/widerrufsbelehrung` |
| `agb.html` | Allgemeine Geschäftsbedingungen | `/pages/agb` |

Die URLs sind nicht beliebig: Footer und Cookie-Banner verlinken genau
darauf. Shopify leitet den Titel automatisch in eine URL um — bei „Cookie-
Richtlinie" wird daraus `cookie-richtlinie`, nicht `cookies`. Das musst du
unter *Suchmaschineneintrag → URL bearbeiten* korrigieren, sonst laufen die
Links ins Leere.

Die Überschrift ist in den HTML-Dateien absichtlich weggelassen — Shopify
setzt den Seitentitel selbst darüber, sonst stünde sie doppelt da.

## Warum nicht ins Theme

Rechtstexte gehören zum Shop, nicht zum Design. Liegen sie im Theme, sind sie
beim nächsten Theme-Wechsel oder beim Hochladen einer neuen Version weg — und
ein fehlendes Impressum ist genau das, was abgemahnt wird. Als Seiten
überleben sie jeden Theme-Wechsel und lassen sich ohne Code-Kenntnisse
ändern.

Was sehr wohl im Theme steckt und nach dem Hochladen sofort dasteht: die
Angaben im Footer — Anbieter, Kontakt, Versand und Rücksendeadresse. Die
findest du im Theme-Editor unter *Footer*, falls du sie später ändern willst.

## Danach kontrollieren

- Footer öffnen: stehen alle fünf Links da und führen sie auf die richtigen
  Seiten?
- Cookie-Banner öffnen: funktionieren die beiden Links darunter?
- Alte Vorlagen-Seiten ausblenden (CCPA, GDPR, PIPEDA, APPI, LGPD,
  Data protection, Do not sell or share my personal information)
