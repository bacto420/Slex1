# BACTO — Dark Theme

Shopify-Theme für www.bactoclothing.com.

## Blog und Media

Blog und Media haben **je ein eigenes Template mit eigenen Blöcken**. Vorher
liefen beide Seiten auf `templates/page.json`. Shopify speichert Blöcke am
Template und nicht an der einzelnen Seite — dadurch teilten sich Blog und
Media einen einzigen Satz Blöcke, und ein Bild, das auf der einen Seite
eingesetzt wurde, tauchte auch auf der anderen auf. Genau diese Verbindung ist
jetzt aufgehoben.

| Bereich | Template | Section | Blocktyp | Darstellung |
| --- | --- | --- | --- | --- |
| Blog | `templates/page.blog.json` | `main-blog-gallery` | `blog_image` | Raster aus 9 anklickbaren Bildern, jedes mit eigenem Link |
| Media | `templates/page.media.json` | `main-media` | `media_image` | Bilder über die volle Breite der Website, direkt untereinander |
| Blogbeiträge | `templates/blog.json` | `main-blog-posts` | — | echte Shopify-Artikel unter `/blogs/...` |
| Normale Seite | `templates/page.json` | `main-page` | — | nur Seitentext |

### Einmalig im Shopify-Adminbereich einstellen

Der Shop hat noch keine Seiten „Blog" und „Media". Beide einmal anlegen und
dabei die passende Vorlage zuweisen:

1. **Onlineshop → Seiten → Seite hinzufügen** → Titel `Blog`, Inhalt leer,
   rechts unter *Theme-Vorlage* `blog` wählen → Speichern.
2. Dasselbe noch einmal mit Titel `Media` und Vorlage `media`.

Entscheidend ist die Adresse: sie muss auf `/pages/blog` bzw. `/pages/media`
enden — daran erkennt der Header die Seiten und verlinkt das Menü von selbst
dorthin. Bei diesen Titeln passiert das automatisch.

Danach im Theme-Editor die Bilder setzen:

* **Blog** — Block *Blog image* pro Bild. Jeder Block hat *Image*, *Link*
  (dorthin führt der Klick), *Open in a new tab* und eine optionale *Caption*.
  Voreingestellt sind 9 Blöcke; *Images per row* und *Image shape* steuern das
  Raster.
* **Media** — Block *Media image* pro Bild, nur *Image* und optionale
  *Caption*. Jedes Bild läuft randlos über die volle Breite. *Image height*
  schneidet auf Wunsch alle Bilder auf dasselbe Format.

Solange eine Seite noch auf der Standardvorlage läuft, zeigt sie die
Platzhalterbilder plus einen Hinweis, der nur im Theme-Editor sichtbar ist.

Existiert gar keine Seite „Blog" bzw. „Media", greift die Navigation auf
`templates/search.blog.json` und `templates/search.media.json` zurück. Auch
diese beiden halten ihre Bilder getrennt.

Diese zwei Fallback-Templates fehlten vorher. Ohne sie liefert Shopify für
`/search?view=blog` **und** `/search?view=media` dasselbe `search.json` aus —
beide Menüpunkte zeigten also auf ein und dieselbe Seite. Das ist der zweite
Teil der „Blog und Media hängen zusammen"-Ursache.

## Aufbau

```
assets/     CSS, JS, Logo, Platzhaltergrafiken
config/     Theme-Einstellungen
layout/     theme.liquid
locales/    Übersetzungen
sections/   Sections inkl. Schema
snippets/   gallery-blog, gallery-media
templates/  Templates je Route
```
