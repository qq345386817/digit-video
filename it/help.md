Canonical page: https://digit-video.luopeike.com/it/help

Dig It

# Aiuto e supporto Dig It

Scopri batch Mac, revisione fotogrammi, esportazione di provini a contatto, progetti salvati e differenze tra piattaforme di Dig It. Consulta la disponibilità della CLI.

[App Store](https://apps.apple.com/app/id6508171056)

## Cosa cambia tra Mac, iPhone e iPad?

### Mac

Mac aggiunge una coda batch, importazione di cartelle, preset, esportazione automatica PNG/JPEG e revisione dei fotogrammi sorgente vicini. Scegli una cartella di destinazione prima di attivare l'esportazione automatica.

### iPhone / iPad

Su iPhone e iPad, scegli un video da Foto o File, rivedi le immagini, esporta PNG selezionati o un provino a contatto e salva esplicitamente i risultati nella cronologia.

## Per iniziare

1. Scegli Bilanciata, Copertina o Passaggi.

2. Importa un video da File o Foto.

3. Rivedi i fotogrammi estratti e seleziona quelli da conservare.

4. Esporta le immagini PNG selezionate o salva il progetto nella cronologia.

## Scegliere una modalità di estrazione

- Bilanciata: un set pulito di dimensione media per la maggior parte dei video.

- Copertina: meno fotogrammi ma più forti per miniature e copertine.

- Passaggi: più punti di cambiamento per tutorial e flussi di lavoro.

## Flussi pratici per i fotogrammi video

[Estrarre fotogrammi video in batch su Mac Aggiungi file video o una cartella, scegli un preset e rivedi ogni risultato o esporta immagini PNG/JPEG automaticamente. L'elaborazione rimane sul Mac. Leggi la guida →](https://digit-video.luopeike.com/it/batch-extract-video-frames-on-mac)

[Creare un provino a contatto da un video Un provino a contatto riunisce immagini video in un'unica panoramica PNG. Usalo per confrontare copertine, condividere un riepilogo delle scene o raccogliere i passaggi di un tutorial senza inviare il video originale. Leggi la guida →](https://digit-video.luopeike.com/it/video-contact-sheet)

## Scegli un'immagine tra i fotogrammi sorgente vicini

Su Mac, seleziona un risultato, scorri i fotogrammi sorgente vicini e aggiungi un'immagine o sostituisci quella selezionata. Il video sorgente deve essere ancora disponibile nello spazio di lavoro attuale.

[![Risultati Mac e revisione sorgente con un video di esempio. Interfaccia in inglese.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Risultati Mac e revisione sorgente con un video di esempio. Interfaccia in inglese.

Video di esempio: Big Buck Bunny. © 2008 Blender Foundation. Fotogrammi disposti con Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Salva un insieme di fotogrammi da modificare ancora

Salva conserva le immagini attuali e i timestamp e punteggi disponibili nella cronologia locale. Riapri un progetto per rivedere, eliminare, esportare e salvare modifiche nella stessa voce. Il video originale non viene salvato; le vecchie voci con soli metadati non possono ricreare immagini mancanti.

## Fino a 40 fotogrammi per provino dalla pagina dei risultati

La pagina dei risultati accetta al massimo 40 fotogrammi per provino. Per raccolte più grandi, seleziona gruppi più piccoli ed effettua più esportazioni. Il provino è una panoramica, non sostituisce le immagini separate. I preset batch di Mac offrono anche provini a contatto opzionali.

## Domande frequenti

### Dig It carica i miei video online?

No. Analisi ed estrazione avvengono sul dispositivo. Scegli tu se condividere i file esportati; l'estrazione locale non richiede internet.

### Serve FFmpeg?

No. L'app di App Store usa i framework locali di elaborazione video di Apple. Il flusso grafico non richiede comandi di Terminale o un'installazione separata di FFmpeg.

### Dig It è gratuito?

Dig It è attualmente gratuito su App Store. Consulta il download ufficiale per prezzo e compatibilità aggiornati.

### La cronologia conserva il video originale?

No. Conserva immagini salvate esplicitamente e metadati, non il video sorgente. La revisione sorgente su Mac richiede un video disponibile nello spazio di lavoro attuale.

### Tutte le immagini mantengono la risoluzione originale?

I fotogrammi estratti automaticamente rientrano attualmente in 720 × 720 pixel, mantenendo le proporzioni. Un fotogramma aggiunto tramite la revisione sorgente Mac usa la risoluzione sorgente. L'esportazione PNG non ingrandisce un fotogramma più piccolo.

### La CLI è inclusa nel download da App Store?

No. digit è uno strumento separato per Mac e al momento non ha un download pubblico. Chiedi all'assistenza come ottenerlo prima di usare gli esempi. Non è disponibile l'integrazione MCP.

### Perché chiede accesso a Foto?

Usa l’accesso a Foto solo per scegliere i contenuti di origine e salvare i risultati quando lo richiedi.

## Strumenti da riga di comando opzionali per Mac

La CLI digit è separata dall'app di App Store e non è ancora distribuita pubblicamente. Chiedi all'assistenza come accedervi. Gli esempi seguenti sono per chi ha già installato lo strumento indipendente.
[Chiedi come ottenere la CLI](https://digit-video.luopeike.com/it/support)

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
