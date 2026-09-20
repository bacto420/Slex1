# Größentabellen als Grafik

Vier Bilder, gerendert aus HTML mit der Michroma-Schrift des Shops:

| Kleidungsstück | Format | Datei |
| --- | --- | --- |
| Longsleeve | 2400 × 3000 | `bacto-size-chart-longsleeve-portrait.png` |
| Longsleeve | 3200 × 1800 | `bacto-size-chart-longsleeve-wide.png` |
| Jacke | 2400 × 3000 | `bacto-size-chart-jacket-portrait.png` |
| Jacke | 3200 × 1800 | `bacto-size-chart-jacket-wide.png` |

Hochformat passt ins Produktbild-Raster (dasselbe 4:5 wie die Produktfotos),
Querformat in Beschreibung, Banner oder Instagram.

## Ändern

Alles steht in `build.py`: die Zeichnungen als SVG, die Maße in `GARMENTS`.
Danach:

```
tools/sizechart/render.sh
```

Das Skript baut die HTML-Dateien neu und rendert sie. **Die HTML-Dateien
nicht direkt bearbeiten** — sie werden bei jedem Lauf überschrieben.

Ein weiteres Kleidungsstück braucht einen Eintrag in `GARMENTS` und seinen
Namen in der Schleife in `render.sh`.

## Auf den Rand achten

Was über die Fläche hinausragt, wird beim Rendern kommentarlos
abgeschnitten. Nach jeder Änderung die untere Zeile des Bildes prüfen: Steht
der Hinweis zur Toleranz noch da, ist alles drin.

## Verhältnis zum Theme

`sections/size-chart.liquid` enthält dieselben zwei Zeichnungen und zeigt
über die Einstellung *Drawing*, welche. Wird hier eine Zeichnung geändert,
gehört sie auch dort ersetzt, sonst zeigen Bild und Shop verschiedene
Silhouetten.

Die Schrift liegt als base64 in den erzeugten HTML-Dateien. Wird
`assets/michroma-latin.woff2` getauscht, erledigt `build.py` das Einbetten
beim nächsten Lauf von selbst.
