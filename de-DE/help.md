Canonical page: https://digit-video.luopeike.com/de-DE/help

Dig It

# Dig It Hilfe und Support

Erfahre mehr über Mac-Stapelverarbeitung, Frame-Prüfung, Kontaktbögen, gespeicherte Projekte und Plattformunterschiede in Dig It sowie die CLI-Verfügbarkeit.

[App Store](https://apps.apple.com/app/id6508171056)

## Was unterscheidet Mac, iPhone und iPad?

### Mac

Mac ergänzt Stapelaufträge, Ordnerimport, Extraktionsvorlagen, automatischen PNG/JPEG-Export und Prüfung benachbarter Quellframes. Wähle vor dem automatischen Export einen Ausgabeordner.

### iPhone / iPad

Wähle auf iPhone und iPad ein Video aus Fotos oder Dateien, prüfe Bilder, exportiere ausgewählte PNGs oder einen Kontaktbogen und speichere Ergebnisse ausdrücklich im Verlauf.

## Erste Schritte

1. Wähle Ausgewogen, Cover oder Schritte.

2. Importiere ein Video aus Dateien oder Fotos.

3. Prüfe die extrahierten Frames und wähle die nützlichen aus.

4. Exportiere PNGs oder speichere das Projekt im Verlauf.

## Extraktionsmodus wählen

- Ausgewogen: ein sauberes mittelgroßes Set für die meisten Videos.

- Cover: weniger, stärkere Frames für Thumbnails und Cover.

- Schritte: mehr Änderungspunkte für Tutorials und Workflows.

## Praktische Workflows für Videobilder

[Videobilder auf dem Mac im Stapel extrahieren Füge Videodateien oder einen Ordner hinzu, wähle eine Extraktionsvorlage und prüfe die Ergebnisse oder exportiere PNG/JPEG automatisch. Die Verarbeitung bleibt auf deinem Mac. Anleitung lesen →](https://digit-video.luopeike.com/de-DE/batch-extract-video-frames-on-mac)

[Einen Kontaktbogen aus einem Video erstellen Ein Kontaktbogen vereint Videobilder in einer PNG-Übersicht. Vergleiche Titelbilder, teile Szenenzusammenfassungen oder sammle Tutorial-Schritte, ohne das Originalvideo zu versenden. Anleitung lesen →](https://digit-video.luopeike.com/de-DE/video-contact-sheet)

## Ein Standbild aus benachbarten Quellframes wählen

Wähle auf Mac ein Ergebnis, gehe durch benachbarte Quellframes und füge ein Bild hinzu oder ersetze die Auswahl. Das Quellvideo muss im aktuellen Arbeitsbereich weiterhin verfügbar sein.

[![Mac-Ergebnisse und Quellframe-Prüfung mit einem Beispielvideo. Oberfläche auf Englisch.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Mac-Ergebnisse und Quellframe-Prüfung mit einem Beispielvideo. Oberfläche auf Englisch.

Beispielvideo: Big Buck Bunny. © 2008 Blender Foundation. Bilder mit Dig It angeordnet. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Ein Bildset zum späteren Bearbeiten speichern

Speichern erhält aktuelle Ergebnisbilder und verfügbare Zeitstempel und Bewertungen im lokalen Verlauf. Öffne ein Projekt erneut, um Bilder zu prüfen, zu löschen, zu exportieren und Änderungen im selben Eintrag zu speichern. Das Quellvideo wird nicht gespeichert; alte reine Metadateneinträge können fehlende Bilder nicht wiederherstellen.

## Bis zu 40 Bilder pro Kontaktbogen der Ergebnisseite

Die Ergebnisseite erlaubt höchstens 40 Bilder in einem Kontaktbogen. Größere Sammlungen lassen sich in kleineren Gruppen mehrfach exportieren. Der Bogen ist eine Übersicht und ersetzt keine Einzelbilder. Die Mac-Stapelvorlagen bieten ebenfalls optionale Kontaktbögen.

## Häufige Fragen

### Lädt Dig It meine Videos hoch?

Nein. Analyse und Extraktion laufen auf deinem Gerät. Du entscheidest, ob exportierte Dateien geteilt werden; die lokale Extraktion braucht kein Internet.

### Brauche ich FFmpeg?

Nein. Die App aus dem App Store nutzt Apples lokale Video-Frameworks. Der grafische Workflow benötigt weder Terminalbefehle noch eine separate FFmpeg-Installation.

### Ist Dig It kostenlos?

Dig It ist derzeit im App Store kostenlos. Aktuelle Preise und Gerätekompatibilität findest du über den offiziellen Downloadlink.

### Behält der Verlauf mein Originalvideo?

Nein. Er enthält ausdrücklich gespeicherte Bilder und Metadaten, nicht das Quellvideo. Die Quellframe-Prüfung am Mac braucht ein verfügbares Video im aktuellen Arbeitsbereich.

### Bleibt bei allen Bildern die Originalauflösung erhalten?

Automatisch extrahierte Bilder passen derzeit bei gleichem Seitenverhältnis in 720 × 720 Pixel. Über die Mac-Quellframe-Prüfung hinzugefügte Bilder verwenden die Quellauflösung. PNG-Export vergrößert kleinere Frames nicht.

### Ist die CLI im App-Store-Download enthalten?

Nein. digit ist ein eigenständiges Mac-Werkzeug ohne derzeitigen öffentlichen Download. Frage den Support nach Zugang, bevor du die Beispiele nutzt. MCP-Integration wird nicht angeboten.

### Why does it ask for Photos access?

Dig It uses Photos access only so you can choose source media and save exported results when you ask it to.

## Optionale Mac-Kommandozeilenwerkzeuge

Die digit-CLI ist von der App-Store-App getrennt und wird noch nicht öffentlich verteilt. Frage den Support nach Zugang. Die Beispiele richten sich an Nutzer mit bereits installiertem eigenständigem Werkzeug.
[Support zum CLI-Zugang kontaktieren](https://digit-video.luopeike.com/de-DE/support)

```sh
digit extract video.mp4 --output ./frames --mode balanced --json frames.json
```

```sh
digit contact-sheet video.mp4 --output sheet.png --columns 4 --limit 40
```

```sh
digit sample video.mp4 --output ./samples --every 10 --max 30 --json samples.json
```

```sh
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
