# Größentabelle als Grafik

Zwei Bilder, gerendert aus HTML mit der Michroma-Schrift des Shops:

| Datei | Größe | wofür |
| --- | --- | --- |
| `bacto-sizechart-portrait.png` | 2400 × 3000 | Produktbild in der Galerie — dasselbe Hochformat wie die anderen Produktbilder |
| `bacto-sizechart-wide.png` | 3200 × 1800 | Produktbeschreibung, Banner, Instagram |

## Zahlen ändern

Die Werte stehen als Text in `portrait.html` und `wide.html`, jeweils in der
Tabelle am Ende der Datei. Ändern, dann:

```
tools/sizechart/render.sh
```

Beide Dateien müssen einzeln gepflegt werden — sie teilen sich bewusst keine
gemeinsame Quelle, weil sie unterschiedliche Schriftgrade und Abstände
brauchen, damit der Inhalt in die jeweilige Fläche passt.

## Auf den Rand achten

Was über die Fläche hinausragt, wird beim Rendern abgeschnitten, ohne
Warnung. Nach jeder Änderung die untere Zeile des Bildes prüfen: Steht der
Hinweis „Gemessen mit einer Toleranz…" noch da, ist alles drin.

Die Schrift liegt als base64 in der HTML-Datei. Wird `assets/michroma-latin.woff2`
im Theme getauscht, muss sie hier neu eingebettet werden.
