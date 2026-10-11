Canonical page: https://digit-video.luopeike.com/help

Dig It

# Dig It Help and Support

Learn Dig It's Mac batch workflow, frame review, contact-sheet export, saved projects and platform differences. Find CLI availability and practical examples.

[App Store](https://apps.apple.com/app/id6508171056)

## What is different on Mac, iPhone and iPad?

### Mac

Mac adds a batch queue, folder import, extraction presets, automatic PNG/JPEG export and nearby source-frame review. Choose an output folder before enabling automatic export.

### iPhone / iPad

On iPhone and iPad, choose one video from Photos or Files, review the extracted images, export selected PNGs or a contact sheet, and explicitly save results to History.

## Getting started

1. Choose Balanced, Cover, or Steps.

2. Import a video from Files or Photos.

3. Review the extracted frames and select the ones worth keeping.

4. Export selected PNG images or save the project to history.

## Choosing an extraction mode

- Balanced: a clean medium-sized set for most videos.

- Cover: fewer stronger frames for thumbnails, covers, and hero images.

- Steps: more change points for tutorials, workflows, and process content.

## Practical video-frame workflows

[Batch extract video frames on Mac Queue video files or a folder, choose a reusable extraction preset, and review each result or export PNG/JPEG images automatically. Processing stays on your Mac. Read the guide →](https://digit-video.luopeike.com/batch-extract-video-frames-on-mac)

[Create a video contact sheet A contact sheet combines video stills into one PNG overview. Use it to compare covers, share a scene summary or keep tutorial steps together without sending the original video. Read the guide →](https://digit-video.luopeike.com/video-contact-sheet)

## Pick a still from nearby source frames

On Mac, select one result, move through nearby source frames, and add a new still or replace the selected image. This review needs the source video to remain available in the current workspace.

[![Mac results and source-frame review using a sample video. English interface shown.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Mac results and source-frame review using a sample video. English interface shown.

Sample video: Big Buck Bunny. © 2008 Blender Foundation. Frames arranged in Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Save a frame set you can return to

Save keeps the current result images and their available timestamps and scores in local History. Reopen a saved project to review, delete, export and save changes to the same record. The source video is not stored with the history record; older metadata-only records cannot recreate missing images.

## Up to 40 frames per result-page contact sheet

The result page accepts at most 40 frames for one contact sheet. For a larger collection, select a smaller group and make several exports. The sheet is an overview, not a replacement for separately exported images. The Mac batch preset also offers optional contact-sheet output.

## Frequently asked questions

### Does Dig It upload my videos?

No. Video analysis and frame extraction run on your device. You choose whether to share exported files; an internet connection is not required for local extraction.

### Do I need FFmpeg?

No. The App Store app uses Apple's local video-processing frameworks. Its graphical workflow does not require Terminal commands or a separate FFmpeg installation.

### Is Dig It free?

Dig It is currently free on the App Store. Follow the official download link for current pricing and device compatibility.

### Does History keep my original video?

No. History keeps explicitly saved result images and metadata, not the source video. Mac source-frame review requires an available source in the current workspace.

### Do all exported frames keep the original resolution?

Automatically extracted frames currently fit within 720 × 720 pixels while preserving aspect ratio. A frame added through Mac source-frame review uses the source image resolution. PNG export does not upscale a smaller extracted frame.

### Is the CLI included in the App Store download?

No. The digit CLI is a separate Mac tool and currently has no public download. Contact support about availability before following the command examples. MCP integration is not provided.

### Why does it ask for Photos access?

Dig It uses Photos access only so you can choose source media and save exported results when you ask it to.

## Optional command line tools for Mac

The digit CLI is separate from the App Store app and is not currently distributed publicly. Contact support about access. The examples below are for users who already have the standalone tool installed.
[Contact support about CLI access](https://digit-video.luopeike.com/support)

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
