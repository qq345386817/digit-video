Canonical page: https://digit-video.luopeike.com/fr-FR/help

Dig It

# Aide et support Dig It

Découvrez les lots Mac, la révision des images, les planches-contact, les projets enregistrés et les différences entre plateformes de Dig It, ainsi que la disponibilité de la CLI.

[App Store](https://apps.apple.com/app/id6508171056)

## Quelles différences entre Mac, iPhone et iPad ?

### Mac

Mac ajoute une file de lots, l'import de dossiers, des préréglages, l'export automatique PNG/JPEG et la révision des images sources voisines. Choisissez un dossier de sortie avant d'activer l'export automatique.

### iPhone / iPad

Sur iPhone et iPad, choisissez une vidéo dans Photos ou Fichiers, examinez les images, exportez les PNG sélectionnés ou une planche-contact et enregistrez les résultats dans l'historique.

## Premiers pas

1. Choisissez Équilibré, Couverture ou Étapes.

2. Importez une vidéo depuis Fichiers ou Photos.

3. Examinez les images extraites et sélectionnez celles à garder.

4. Exportez les PNG sélectionnés ou sauvegardez le projet dans l’historique.

## Choisir un mode d’extraction

- Équilibré : un ensemble moyen et propre pour la plupart des vidéos.

- Couverture : moins d’images, plus fortes, pour miniatures et couvertures.

- Étapes : plus de points de changement pour tutoriels et workflows.

## Des flux pratiques pour vos images vidéo

[Extraire des images vidéo par lots sur Mac Ajoutez des vidéos ou un dossier, choisissez un préréglage, puis examinez chaque résultat ou exportez des PNG/JPEG automatiquement. Le traitement reste sur votre Mac. Lire le guide →](https://digit-video.luopeike.com/fr-FR/batch-extract-video-frames-on-mac)

[Créer une planche-contact à partir d'une vidéo Une planche-contact réunit des images vidéo dans un aperçu PNG. Comparez des couvertures, partagez un résumé des scènes ou rassemblez les étapes d'un tutoriel sans envoyer la vidéo originale. Lire le guide →](https://digit-video.luopeike.com/fr-FR/video-contact-sheet)

## Extraire des images par intervalle ou horodatage sur Mac

Ces nouveautés nécessitent la version 1.4.3 ou ultérieure. Si la mise à jour n’est pas encore disponible dans votre App Store, les exports précédents restent disponibles.

Avant d’ajouter les vidéos à l’espace Mac, choisissez images clés automatiques, intervalle fixe, horodatages précis ou répartition uniforme, avec une limite de 1 à 120 images. L’intervalle fixe s’arrête à la limite ; la répartition uniforme couvre toute la vidéo. Saisissez des secondes ou HH:MM:SS, par exemple 5, 00:12.5, 01:30. Activez Résolution source pour l’export automatique ou sélectionnez les résultats puis Exporter → Exporter à la résolution source → PNG/JPEG. Les images originales sont décodées et enregistrées une par une, sans agrandissement. La 4K exige une source 4K et la vidéo source doit rester disponible dans l’espace de travail.

## Exporter des couvertures et des planches contact PDF imprimables

Sur Mac, iPhone ou iPad, sélectionnez une image puis Exporter → Exporter une couverture. Choisissez le format original, 16:9, 9:16, 1:1 ou 4:3, ajustez le cadrage et la longueur maximale, puis enregistrez en PNG/JPEG. Le JPEG peut être limité à 2 Mo ; réduisez les dimensions si nécessaire. Les images ne sont jamais agrandies. Pour une planche PDF, choisissez A4/Letter et 2 à 4 colonnes. Jusqu’à 120 images sont classées chronologiquement et paginées avec le nom de la vidéo et les horodatages. Sans sélection, tous les résultats restants sont utilisés. La planche PNG reste limitée à 40 images.

## Choisissez une image parmi les images sources voisines

Sur Mac, sélectionnez un résultat, parcourez les images sources voisines et ajoutez une image ou remplacez la sélection. La vidéo source doit rester disponible dans l'espace de travail actuel.

[![Résultats Mac et révision de la source avec une vidéo d'exemple. Interface en anglais.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Résultats Mac et révision de la source avec une vidéo d'exemple. Interface en anglais.

Vidéo d'exemple : Big Buck Bunny. © 2008 Blender Foundation. Images organisées avec Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Enregistrez un ensemble d'images à rééditer

Enregistrer conserve les images actuelles ainsi que les horodatages et scores disponibles dans l'historique local. Rouvrez un projet pour examiner, supprimer, exporter et enregistrer les changements dans la même entrée. La vidéo source n'est pas conservée ; les anciennes entrées contenant uniquement des métadonnées ne peuvent pas recréer les images manquantes.

## Planches PNG : jusqu’à 40 images

Une planche PNG accepte jusqu’à 40 images. Pour une vue imprimable plus grande, choisissez PDF : jusqu’à 120 images avec pagination automatique. L’espace Mac peut aussi exporter des planches PNG et des PDF.

## Questions fréquentes

### Dig It téléverse-t-il mes vidéos ?

Non. L'analyse et l'extraction se font sur votre appareil. Vous choisissez de partager les fichiers exportés ; l'extraction locale ne nécessite pas internet.

### Ai-je besoin de FFmpeg ?

Non. L'app de l'App Store utilise les frameworks locaux de traitement vidéo d'Apple. Son interface graphique n'exige ni commandes Terminal ni installation séparée de FFmpeg.

### Dig It est-il gratuit ?

Dig It est actuellement gratuit sur l'App Store. Consultez le lien officiel pour connaître le prix et la compatibilité actuels.

### L'historique conserve-t-il la vidéo originale ?

Non. Il conserve les images explicitement enregistrées et leurs métadonnées, pas la vidéo source. La révision source sur Mac nécessite une vidéo disponible dans l'espace de travail actuel.

### Toutes les images gardent-elles la résolution originale ?

Les aperçus tiennent dans 720 × 720 pixels. Sur Mac, l’export à la résolution source décode la vidéo originale à la demande et conserve ses dimensions. Les couvertures Mac utilisent la source disponible, sinon l’image enregistrée. Aucun aperçu ni source basse résolution n’est agrandi.

### La CLI est-elle incluse dans le téléchargement App Store ?

Non. digit est un outil Mac séparé sans téléchargement public actuellement. Contactez l'assistance avant d'utiliser les exemples. L'intégration MCP n'est pas proposée.

### Why does it ask for Photos access?

Dig It uses Photos access only so you can choose source media and save exported results when you ask it to.

## Outils de ligne de commande facultatifs pour Mac

La CLI digit est distincte de l'app de l'App Store et n'est pas encore distribuée publiquement. Contactez l'assistance pour en savoir plus. Les exemples sont destinés aux personnes ayant déjà installé l'outil indépendant.
[Demander l'accès à la CLI](https://digit-video.luopeike.com/fr-FR/support)

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
digit extract video.mp4 --output ./originals --resolution source --json originals.json
```

```sh
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
