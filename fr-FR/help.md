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

## Choisissez une image parmi les images sources voisines

Sur Mac, sélectionnez un résultat, parcourez les images sources voisines et ajoutez une image ou remplacez la sélection. La vidéo source doit rester disponible dans l'espace de travail actuel.

[![Résultats Mac et révision de la source avec une vidéo d'exemple. Interface en anglais.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Résultats Mac et révision de la source avec une vidéo d'exemple. Interface en anglais.

Vidéo d'exemple : Big Buck Bunny. © 2008 Blender Foundation. Images organisées avec Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Enregistrez un ensemble d'images à rééditer

Enregistrer conserve les images actuelles ainsi que les horodatages et scores disponibles dans l'historique local. Rouvrez un projet pour examiner, supprimer, exporter et enregistrer les changements dans la même entrée. La vidéo source n'est pas conservée ; les anciennes entrées contenant uniquement des métadonnées ne peuvent pas recréer les images manquantes.

## Jusqu'à 40 images par planche depuis les résultats

La page des résultats accepte au maximum 40 images dans une planche. Pour une collection plus grande, sélectionnez des groupes plus petits et effectuez plusieurs exports. La planche est un aperçu et ne remplace pas les images individuelles. Les préréglages par lots sur Mac proposent également des planches-contact facultatives.

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

Les images extraites automatiquement tiennent actuellement dans 720 × 720 pixels en conservant leurs proportions. Une image ajoutée par la révision source sur Mac utilise la résolution source. L'export PNG n'agrandit pas une petite image extraite.

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
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
