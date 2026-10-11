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

## Sample video frames by interval or timestamp on Mac

These new workflows require version 1.4.3 or later. If the update is not available in your App Store yet, the previous export options remain available.

Before adding videos to the Mac workspace, choose Frame Selection: Automatic Keyframes, Fixed Interval, Specific Timestamps or Evenly Spaced. Set a limit of 1–120 frames. Fixed Interval stops at that limit; Evenly Spaced covers the full timeline. Timestamps accept seconds or HH:MM:SS, for example 5, 00:12.5, 01:30. Enable Source Resolution for automatic export, or select results and use Export → Export Source Resolution → PNG/JPEG. Original-size frames are decoded and saved one at a time, without upscaling; 4K output requires a 4K source. Source export requires the original video to remain available in the workspace.

## Export cover images and printable PDF contact sheets

On Mac, iPhone or iPad, select one result and choose Export → Export Cover. Choose the original ratio, 16:9, 9:16, 1:1 or 4:3, adjust the crop position and maximum edge, then save PNG or JPEG. JPEG can be limited to 2 MB; if it cannot fit, choose smaller dimensions. Images are never upscaled. For a printable overview, choose Export → PDF Contact Sheet, A4 or Letter, and 2–4 columns. Up to 120 selected frames are ordered chronologically and paginated automatically, with the video name and timestamps. With no selection, all remaining results are used. A PNG contact sheet still accepts at most 40 frames.

## Pick a still from nearby source frames

On Mac, select one result, move through nearby source frames, and add a new still or replace the selected image. This review needs the source video to remain available in the current workspace.

[![Mac results and source-frame review using a sample video. English interface shown.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Mac results and source-frame review using a sample video. English interface shown.

Sample video: Big Buck Bunny. © 2008 Blender Foundation. Frames arranged in Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Save a frame set you can return to

Save keeps the current result images and their available timestamps and scores in local History. Reopen a saved project to review, delete, export and save changes to the same record. The source video is not stored with the history record; older metadata-only records cannot recreate missing images.

## PNG contact sheets: up to 40 frames

A PNG contact sheet accepts up to 40 frames. For a larger printable overview, use PDF Contact Sheet: up to 120 frames with automatic pagination. The Mac batch workspace can also export PNG sheets and PDFs.

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

Previews fit within 720 × 720 pixels. On Mac, Source Resolution exports decode the original video on demand and preserve its image dimensions. Mac covers use an available source; otherwise covers use the saved image resolution. Output never upscales a preview or a low-resolution source.

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
digit extract video.mp4 --output ./originals --resolution source --json originals.json
```

```sh
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
