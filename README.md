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

## Bundle-Deal auf der Produktseite

Unter jeder Produktseite sitzt der Abschnitt **Bundle deal**
(`sections/product-bundle.liquid`): zwei Produkte nebeneinander mit einem Plus
dazwischen, daneben der Einzelpreis-Gesamtbetrag durchgestrichen, der
Bundle-Preis, die Ersparnis und ein Button, der beide Artikel auf einmal in den
Warenkorb legt.

Einstellbar im Theme-Editor (Produkte → Bundle deal): Überschrift, Untertitel,
Rabattsatz, Wortlaut der Zeilen und pro Block ein Produkt.

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

## Aufbau

```
assets/     CSS, JS, Logo, Platzhaltergrafiken
config/     Theme-Einstellungen
layout/     theme.liquid
locales/    Übersetzungen
sections/   Sections inkl. Schema
snippets/   gallery-blog (Vollbreite), gallery-media (Raster mit Links)
templates/  Templates je Route
```
