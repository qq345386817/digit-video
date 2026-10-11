Canonical page: https://digit-video.luopeike.com/zh-Hans/batch-extract-video-frames-on-mac

工作流指南

# 在 Mac 上批量提取视频图片

添加多个视频或整个文件夹，选好提取预设，然后逐个查看结果或自动导出 PNG/JPEG 图片。处理过程在 Mac 本地完成。

[App Store](https://apps.apple.com/app/id6508171056)

[帮助](https://digit-video.luopeike.com/zh-Hans/help)

更新日期: 2026-10-12

## 快速开始

1. 在 Mac 批量工作区添加视频或选择文件夹。子文件夹中的受支持视频也会被加入，建议先准备好只包含目标素材的文件夹。

2. 添加视频前，选择均衡查看、封面组合或教程步骤预设。每个任务保留加入队列时的预设；之后调整配置只影响新加入的任务。

3. 使用自动导出前先选择输出文件夹，再设置图片格式、命名模板和同名文件处理方式。选择重新命名可以保留旧导出；覆盖仅适合专用导出目录。

4. 任务完成后查看结果，选择有用的画面并导出。“当前完成后暂停”会在当前视频处理完后暂停队列，“继续”会处理剩余任务。

## 批量导出会生成什么？

自动导出会为每个视频创建目录。命名模板可包含视频名、帧序号和时间戳。可选的 JSON 元数据记录图片文件名、时间戳和评分，联系表提供画面总览。预设中的图片格式用于自动导出，结果页的“导出所选”则生成 PNG。

[![Mac 批量工作区，展示示例队列与提取结果。截图为英文界面。](https://digit-video.luopeike.com/images/mac-batch-workspace.webp)](https://digit-video.luopeike.com/images/mac-batch-workspace.webp)

Mac 批量工作区，展示示例队列与提取结果。截图为英文界面。

示例视频：Big Buck Bunny。© 2008 Blender Foundation。画面由 Dig It 排列。 [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## 查看更精简的关键时刻

提取模式筛选代表性画面，并非导出视频的每一帧。封面模式偏向少量封面候选，步骤模式保留更多教程变化点。用于商品页或文档前，建议先查看结果。在 Mac 上需要更精确的替换时，选中一张结果，用源视频附近的逐帧控制进行调整。

[![使用示例视频的 Mac 结果页与源画面查看。截图为英文界面。](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

使用示例视频的 Mac 结果页与源画面查看。截图为英文界面。

示例视频：Big Buck Bunny。© 2008 Blender Foundation。画面由 Dig It 排列。 [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## 在 Mac 上按间隔或时间点提取视频图片

这些新工作流需要 1.4.3 或更高版本。如果所在 App Store 尚未提供更新，仍可使用之前的导出功能。

在 Mac 工作区添加视频前，先选择“画面选择”：自动关键帧、固定间隔、指定时间点或均匀采样，并设置 1–120 帧的上限。固定间隔达到上限后停止；均匀采样覆盖完整时间线。时间点支持秒数或 HH:MM:SS，例如 5, 00:12.5, 01:30。自动导出时可开启“源视频分辨率”，或在结果页选中图片，使用“导出 → 导出原画 → PNG/JPEG”。原画逐帧解码并保存，不会放大图片；4K 输出需要 4K 源视频。原画导出要求当前工作区中的源视频仍然可用。

## 导出封面图片与可打印的 PDF 联系表

在 Mac、iPhone 或 iPad 上，选中一张结果，使用“导出 → 导出封面”。支持原始比例、16:9、9:16、1:1、4:3，可调整裁切位置和最大边长，并保存为 PNG 或 JPEG。JPEG 可限制为 2 MB，无法满足限制时需要选择更小的尺寸。图片不会被放大。需要打印总览时，使用“导出 → PDF 联系表”，选择 A4 或 Letter 和 2–4 列。最多 120 张所选图片按时间排列，自动分页，并附有视频名和时间戳。未选择图片时使用全部剩余结果；PNG 联系表仍最多包含 40 帧。

## Mac、iPhone 和 iPad 有什么区别？

### Mac

Mac 提供批量队列、文件夹导入、提取预设、自动 PNG/JPEG 导出和源视频附近的逐帧查看。开启自动导出前需要选择输出文件夹。

### iPhone / iPad

在 iPhone 和 iPad 上，从照片或文件中选择一个视频，查看提取出的图片，导出所选 PNG 或联系表，并主动保存结果到历史记录。

## 保存以后还能继续编辑的结果集

“保存”会把当前结果图片及可用的时间戳、评分保存在本机历史记录中。重新打开后可查看、删除、导出，再覆盖保存到同一记录。历史记录不保存源视频；较旧的仅元数据记录无法重建缺失图片。

## 相关指南

[从视频制作拼接联系表 联系表把多张视频静帧拼接为一张 PNG 总览图，适合比较封面、分享场景摘要或整理教程步骤，无需发送原视频。 查看指南 →](https://digit-video.luopeike.com/zh-Hans/video-contact-sheet)

[帮助 了解 Dig It 的 Mac 批量工作区、精确选帧、联系表导出、可编辑历史记录和平台差异，并查看 CLI 获取状态与命令示例。](https://digit-video.luopeike.com/zh-Hans/help)

[阅读 Markdown 版本](https://digit-video.luopeike.com/zh-Hans/batch-extract-video-frames-on-mac.md)
