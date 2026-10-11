Canonical page: https://digit-video.luopeike.com/es-ES/help

Dig It

# Ayuda y soporte de Dig It

Aprende a procesar lotes en Mac, revisar fotogramas, exportar hojas de contacto y editar proyectos guardados con Dig It. Consulta la disponibilidad de la CLI.

[App Store](https://apps.apple.com/app/id6508171056)

## ¿Qué cambia entre Mac, iPhone y iPad?

### Mac

Mac añade una cola por lotes, importación de carpetas, ajustes de extracción, exportación automática PNG/JPEG y revisión de fotogramas cercanos del vídeo original. Elige una carpeta de salida antes de exportar automáticamente.

### iPhone / iPad

En iPhone y iPad, selecciona un vídeo de Fotos o Archivos, revisa las imágenes, exporta los PNG seleccionados o una hoja de contacto y guarda los resultados en el historial.

## Primeros pasos

1. Elige Equilibrado, Portada o Pasos.

2. Importa un video desde Archivos o Fotos.

3. Revisa los fotogramas extraídos y selecciona los que quieras conservar.

4. Exporta PNG seleccionados o guarda el proyecto en el historial.

## Elegir un modo de extracción

- Equilibrado: un conjunto limpio y mediano para la mayoría de videos.

- Portada: menos fotogramas, más fuertes, para miniaturas y portadas.

- Pasos: más puntos de cambio para tutoriales y flujos de trabajo.

## Flujos prácticos con fotogramas de vídeo

[Extraer fotogramas de vídeo por lotes en Mac Añade archivos o una carpeta, elige un ajuste de extracción y revisa cada resultado o exporta imágenes PNG/JPEG automáticamente. El procesamiento se realiza en tu Mac. Leer la guía →](https://digit-video.luopeike.com/es-ES/batch-extract-video-frames-on-mac)

[Crear una hoja de contacto de vídeo Una hoja de contacto combina imágenes del vídeo en un único PNG. Sirve para comparar portadas, compartir un resumen de escenas o reunir pasos de un tutorial sin enviar el vídeo original. Leer la guía →](https://digit-video.luopeike.com/es-ES/video-contact-sheet)

## Elige una imagen entre los fotogramas cercanos

En Mac, selecciona un resultado, revisa los fotogramas cercanos del vídeo original y añade una imagen o sustituye la seleccionada. El vídeo de origen debe seguir disponible en el espacio de trabajo actual.

[![Resultados de Mac y revisión del vídeo de origen con un clip de ejemplo. Interfaz en inglés.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Resultados de Mac y revisión del vídeo de origen con un clip de ejemplo. Interfaz en inglés.

Vídeo de ejemplo: Big Buck Bunny. © 2008 Blender Foundation. Imágenes organizadas con Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Guarda un conjunto que puedas seguir editando

Guardar conserva las imágenes actuales, sus marcas de tiempo y puntuaciones disponibles en el historial local. Reabre un proyecto para revisar, eliminar, exportar y guardar cambios en el mismo registro. No se guarda el vídeo original; los registros antiguos que solo contienen metadatos no pueden reconstruir imágenes ausentes.

## Hasta 40 fotogramas por hoja desde los resultados

La página de resultados admite un máximo de 40 fotogramas por hoja. Para colecciones mayores, selecciona grupos más pequeños y realiza varias exportaciones. La hoja es una vista general, no sustituye las imágenes individuales. Los ajustes por lotes de Mac también ofrecen hojas de contacto opcionales.

## Preguntas frecuentes

### ¿Dig It sube mis vídeos?

No. El análisis y la extracción se realizan en el dispositivo. Tú decides si compartes los archivos exportados; la extracción local no requiere conexión a internet.

### ¿Necesito FFmpeg?

No. La app de App Store usa los marcos de procesamiento de vídeo de Apple. Su interfaz gráfica no requiere comandos de Terminal ni instalar FFmpeg.

### ¿Dig It es gratis?

Dig It es actualmente gratuito en App Store. Consulta el enlace oficial para conocer el precio y la compatibilidad vigentes.

### ¿El historial conserva mi vídeo original?

No. Conserva las imágenes guardadas explícitamente y sus metadatos, no el vídeo de origen. La revisión de fotogramas en Mac requiere un vídeo disponible en el espacio de trabajo actual.

### ¿Todas las imágenes mantienen la resolución original?

Las imágenes extraídas automáticamente se ajustan actualmente a 720 × 720 píxeles conservando la proporción. Un fotograma añadido desde la revisión del vídeo en Mac usa la resolución de origen. Exportar PNG no amplía una imagen extraída más pequeña.

### ¿La descarga de App Store incluye la CLI?

No. digit es una herramienta independiente para Mac sin descarga pública actualmente. Consulta a soporte antes de usar los ejemplos. No se ofrece integración MCP.

### ¿Por qué pide acceso a Fotos?

Usa Fotos solo para elegir medios de origen y guardar resultados cuando lo solicitas.

## Herramientas de línea de comandos opcionales para Mac

La CLI digit es independiente de la app de App Store y aún no se distribuye públicamente. Consulta a soporte cómo obtenerla. Los ejemplos son para usuarios que ya tienen instalada la herramienta independiente.
[Consultar el acceso a la CLI](https://digit-video.luopeike.com/es-ES/support)

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
