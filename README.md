# BACTO — Dark Theme

Shopify-Theme für www.bactoclothing.com.

## Blog und Media

Blog und Media sind **zwei getrennte Abschnitte mit je eigenen Bildblöcken**.
Vorher steckten beide Blocksätze in ein und demselben Abschnitt auf
`templates/page.json`. Shopify speichert Blöcke am Template und nicht an der
einzelnen Seite — dadurch teilten sich Blog und Media eine einzige Blockliste,
und ein Bild, das auf der einen Seite eingesetzt wurde, tauchte auch auf der
anderen auf. Genau diese Verbindung ist jetzt aufgehoben.

| Bereich | Abschnitt | Blocktyp | Darstellung |
| --- | --- | --- | --- |
| Blog | `main-blog-gallery` | `blog_image` | Bilder über die volle Breite der Website, direkt untereinander |
| Media | `main-media` | `media_image` | Raster aus 9 anklickbaren Bildern, jedes mit eigenem Link |
| Blogbeiträge | `main-blog-posts` | — | echte Shopify-Artikel unter `/blogs/...` |
| Normale Seite | `main-page` | — | nur Seitentext |

Beide Abschnitte sitzen auf der Standard-Seitenvorlage `templates/page.json`.
Es muss also **keiner Seite eine Theme-Vorlage zugewiesen werden**. Jeder
Abschnitt zeigt sich nur dort, wo er hingehört — entschieden am Handle der
Seite:

* Adresse enthält `blog` oder `journal` → Abschnitt **Blog**
* Adresse enthält `media` oder `presse` → Abschnitt **Media**
* alles andere → nur der normale Seitentext

Auf allen übrigen Seiten geben beide Abschnitte gar nichts aus — auch nicht
im Theme-Editor. In der Seitenleiste des Editors stehen sie zwar bei jeder
Seite, zeigen aber nur dort etwas, wo sie hingehören.

Wichtig: die beiden Abschnitte **nicht ausblenden**. Es ist jeweils ein
einziger Abschnitt auf einem gemeinsamen Template — wer ihn auf der
Media-Seite ausblendet, blendet ihn auch auf der Blog-Seite aus.

### Bilder einsetzen

Onlineshop → Themes → **Anpassen**, oben im Dropdown die Seite **Blog** bzw.
**Media** auswählen. Links in der Seitenleiste die Abschnitte aufklappen:

* **Blog** — Block *Blog image* pro Bild, nur *Image* und optionale *Caption*.
  Jedes Bild läuft randlos über die volle Breite, direkt unter dem vorherigen.
  *Image height* schneidet auf Wunsch alle Bilder auf dasselbe Format.
  Voreingestellt sind 5 Blöcke.
* **Media** — Block *Media image* pro Bild. Jeder Block hat *Image*, *Link*
  (dorthin führt der Klick), *Open in a new tab* und eine optionale *Caption*.
  Voreingestellt sind 9 Blöcke; *Images per row* und *Image shape* steuern das
  Raster.

Blöcke lassen sich über *Block hinzufügen* ergänzen (bis 24) und per Drag &
Drop umsortieren.

### Adressen der Seiten

Der Header verlinkt automatisch auf die Seiten mit den Handles `blog` und
`media`, die Adressen lauten also `/pages/blog` und `/pages/media`.

Existiert eine der beiden Seiten nicht, greift die Navigation auf
`templates/search.blog.json` bzw. `templates/search.media.json` zurück. Diese
zwei Fallback-Templates fehlten ursprünglich; ohne sie liefert Shopify für
`/search?view=blog` **und** `/search?view=media` dasselbe `search.json` aus —
beide Menüpunkte zeigten also auf ein und dieselbe Seite. Das war der zweite
Teil der „Blog und Media hängen zusammen"-Ursache.

## Größentabelle

Die Größentabelle ist **kein Abschnitt im Theme**, sondern ein Bild. Vier
fertige PNGs liegen unter `tools/sizechart/out/` — je Kleidungsstück eines im
Hoch- und eines im Querformat. Das Hochformat hat dasselbe 4:5 wie die
Produktfotos und passt damit ins Bilderraster, das Querformat in die
Beschreibung oder einen Banner.

Hochladen wie jedes andere Produktbild. Zum Ändern der Maße oder der
Zeichnung siehe `tools/sizechart/README.md`.

Ein Abschnitt im Theme hätte bedeutet, dass jede Produktvorlage ihre eigene
Tabelle pflegt — beim Bild reicht es, die Datei auszutauschen.

## Sprachen

Der Shop läuft zweisprachig: Englisch als Standardsprache des Shops, Deutsch
als veröffentlichte Übersetzung. Im Header steht rechts neben dem Warenkorb
eine Auswahl, mit der Besucher umschalten können. Sie erscheint nur, wenn
mehr als eine Sprache veröffentlicht ist — in einem einsprachigen Shop
verschwindet sie von selbst.

### Was das Theme entscheidet und was nicht

**Nicht das Theme:** in welcher Sprache jemand ankommt. Das steht in
*Einstellungen → Sprachen* (Standardsprache je Domain) und in *Einstellungen
→ Märkte*. Ist für `www.bacto-clothing.com` Deutsch als Standard gesetzt,
liefert Shopify dort Deutsch aus, Englisch liegt dann unter `/en`. Das Theme
folgt dem, was Shopify schickt — es kann und soll das nicht überschreiben.

**Das Theme:** dass es zu jeder Sprache Wörter gibt und dass man wechseln
kann.

### Woher die Wörter kommen

| Text | Quelle | Übersetzen in |
| --- | --- | --- |
| Navigation, Warenkorb, Formular-Beschriftungen, Kontoseiten | `locales/en.default.json` und `locales/de.json` | Translate & Adapt → *Theme* |
| Alles, was im Theme-Editor eingetippt ist (Footer-Spalten, Widerrufs-Texte, Überschriften) | Abschnitts-Einstellungen | Translate & Adapt → *Theme* |
| Produkte, Seiten, Blogbeiträge, Rechtstexte, Navigation | Shopify-Inhalte | Translate & Adapt → jeweilige Rubrik |

Beide Sprachdateien sind Schlüssel für Schlüssel gleich. Kommt ein Text dazu,
gehört er in **beide** — fehlt er in `de.json`, zeigt Shopify still die
englische Fassung, und das fällt erst dem Kunden auf.

Die deutschen Texte in den Dateien sind eine brauchbare Grundlage, keine
Vorgabe: was in Translate & Adapt für Deutsch eingetragen wird, hat Vorrang.
Dort geänderte Wörter überschreiben also nichts im Theme und gehen beim
nächsten Theme-Update auch nicht verloren.

### Wenn eine Sprache dazukommt

Sprache in Shopify veröffentlichen, `locales/de.json` kopieren, umbenennen
(z. B. `es.json`), übersetzen. Die Auswahl im Header nimmt sie automatisch
auf — sie liest `localization.available_languages` und zählt nicht selbst.

## Bundle-Deal auf der Produktseite
Unter jeder Produktseite sitzt der Abschnitt **Bundle deal**
(`sections/product-bundle.liquid`): zwei Produkte nebeneinander mit einem Plus
dazwischen, daneben der Einzelpreis-Gesamtbetrag durchgestrichen, der
Bundle-Preis, die Ersparnis und ein Button, der beide Artikel auf einmal in den
Warenkorb legt.

Ein Bundle besteht aus **Slots**. Ein Slot ist entweder ein festes Produkt
(Block *Bundle product*) oder eine **Auswahl** (Block *Bundle choice*) mit bis
zu vier Produkten, von denen der Kunde eines nimmt — etwa zwei Jacken.

Hat das gewählte Produkt Varianten, erscheint im Slot zusätzlich ein
**Größen-Auswahlfeld**. Ohne das könnte das Formular nur die erste verfügbare
Variante senden, und jedes Bundle landete in irgendeiner Größe im Warenkorb.

Preise, Ersparnis und Gesamtsumme rechnen beim Umschalten live mit. Liquid
rendert die Ausgangsauswahl fertig samt Formularfeldern, das Skript übernimmt
erst ab der ersten Änderung — ohne JavaScript bleibt also eine gültige,
vollständige Bestellung stehen.

Einstellbar im Theme-Editor (Produkte → Bundle deal): Überschrift, Untertitel,
Rabattsatz, Layout, Produktgröße und Wortlaut der Zeilen.

Ausgeliefert wird der Abschnitt mit zwei **leeren** Produkt-Blöcken. Solange
weniger als zwei Produkte gewählt sind, gibt er im Shop nichts aus — im
Theme-Editor dagegen schon: dort steht ein gestrichelter Rahmen mit dem
Hinweis, dass noch Produkte fehlen. Sonst wäre der Abschnitt ausgerechnet
während der Einrichtung unsichtbar.

**Der Rabatt selbst kommt nicht aus dem Theme.** Ein Theme kann einen Deal nur
zeigen, nicht gewähren — der Nachlass muss als automatischer Rabatt unter
*Rabatte* im Adminbereich existieren, sonst verlangt der Warenkorb den vollen
Preis, obwohl die Seite einen niedrigeren angezeigt hat.

Die Einstellung *Discount applies to* muss zu diesem Rabatt passen:

| Einstellung | passender Rabatt im Admin |
| --- | --- |
| *The whole bundle* | 15 % auf alle Artikel des Sets — z. B. „Betrag auf Produkte" auf eine Kollektion mit Mindestmenge 2 |
| *The cheaper item only* | „Kauf X, erhalte Y": 1 Jacke gekauft → 15 % auf 1 Longsleeve |

Shopify kann „genau eine Jacke **und** ein Longsleeve zusammen" nativ nicht
exakt abbilden; am nächsten kommt „Kauf X, erhalte Y". Für einen echten
Bundle-Rabatt auf die Gesamtsumme braucht es eine Bundle-App oder Shopify
Functions.

## Preview-Theme für die Zeit vor dem Drop

`python3 tools/build-preview.py` erzeugt aus diesem Theme eine zweite
Fassung, bei der der Shop geschlossen ist: keine Produkte, keine
Kollektionen, kein Warenkorb, kein Blog. Übrig bleiben Startseite, Media,
die Rechtstexte und der Cookie-Banner.

Jede Route, die etwas verkaufen würde, beantwortet der Abschnitt
**Coming soon**. Das ist Absicht: Ein Shop ohne Produkte antwortet trotzdem
auf `/products/...` und `/cart`, und eine nackte Shopify-Fehlerseite dort
wirkt kaputt statt „noch nicht offen". Optional zeigt der Abschnitt einen
Countdown, sobald ein Datum gesetzt ist.

Die Vorschau wird **abgeleitet statt kopiert**. Damit driften die beiden
Fassungen nicht auseinander: Eine Korrektur am Footer landet in beiden.

```
preview/sections/coming-soon.liquid   die Teaser-Section
preview/templates/*.json              welche Route worauf zeigt
preview/config/settings_data.json     Navigation, Footer
preview/preview.css                   wird an base.css angehängt
```

Welche Navigationspunkte erscheinen, steht in den **Theme-Einstellungen →
Navigation** — einmal für Header und Footer-Leiste gemeinsam, damit die
beiden nie auseinanderlaufen. Home steht immer da. Die Vorschau schaltet
Shop, Blog, Media und Warenkorb ab, zeigt also nur die Startseite.

## Aufbau
```
assets/     CSS, JS, Logo, Platzhaltergrafiken
config/     Theme-Einstellungen
layout/     theme.liquid
locales/    en.default.json und de.json — Schlüssel für Schlüssel gleich
sections/   Sections inkl. Schema
snippets/   gallery-blog (Vollbreite), gallery-media (Raster mit Links),
            language-switcher (Sprachauswahl im Header), price
templates/  Templates je Route
```
