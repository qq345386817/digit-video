Canonical page: https://digit-video.luopeike.com/zh-Hans/help

Dig It

# Dig It 帮助与支持

了解 Dig It 的 Mac 批量工作区、精确选帧、联系表导出、可编辑历史记录和平台差异，并查看 CLI 获取状态与命令示例。

[App Store](https://apps.apple.com/app/id6508171056)

## Mac、iPhone 和 iPad 有什么区别？

### Mac

Mac 提供批量队列、文件夹导入、提取预设、自动 PNG/JPEG 导出和源视频附近的逐帧查看。开启自动导出前需要选择输出文件夹。

### iPhone / iPad

在 iPhone 和 iPad 上，从照片或文件中选择一个视频，查看提取出的图片，导出所选 PNG 或联系表，并主动保存结果到历史记录。

## 快速开始

1. 选择均衡、封面或步骤模式。

2. 从文件或照片导入视频。

3. 查看提取出的画面，并选择值得保留的关键帧。

4. 导出选中的 PNG 图片，或把项目保存到历史记录。

## 如何选择提取模式

- 均衡：适合多数视频的中等数量干净结果。

- 封面：更少但更强的封面、缩略图和主视觉候选。

- 步骤：保留更多变化点，适合教程、流程和操作内容。

## 实用的视频抽帧工作流

[在 Mac 上批量提取视频图片 添加多个视频或整个文件夹，选好提取预设，然后逐个查看结果或自动导出 PNG/JPEG 图片。处理过程在 Mac 本地完成。 查看指南 →](https://digit-video.luopeike.com/zh-Hans/batch-extract-video-frames-on-mac)

[从视频制作拼接联系表 联系表把多张视频静帧拼接为一张 PNG 总览图，适合比较封面、分享场景摘要或整理教程步骤，无需发送原视频。 查看指南 →](https://digit-video.luopeike.com/zh-Hans/video-contact-sheet)

## 在 Mac 上按间隔或时间点提取视频图片

这些新工作流需要 1.4.3 或更高版本。如果所在 App Store 尚未提供更新，仍可使用之前的导出功能。

在 Mac 工作区添加视频前，先选择“画面选择”：自动关键帧、固定间隔、指定时间点或均匀采样，并设置 1–120 帧的上限。固定间隔达到上限后停止；均匀采样覆盖完整时间线。时间点支持秒数或 HH:MM:SS，例如 5, 00:12.5, 01:30。自动导出时可开启“源视频分辨率”，或在结果页选中图片，使用“导出 → 导出原画 → PNG/JPEG”。原画逐帧解码并保存，不会放大图片；4K 输出需要 4K 源视频。原画导出要求当前工作区中的源视频仍然可用。

## 导出封面图片与可打印的 PDF 联系表

在 Mac、iPhone 或 iPad 上，选中一张结果，使用“导出 → 导出封面”。支持原始比例、16:9、9:16、1:1、4:3，可调整裁切位置和最大边长，并保存为 PNG 或 JPEG。JPEG 可限制为 2 MB，无法满足限制时需要选择更小的尺寸。图片不会被放大。需要打印总览时，使用“导出 → PDF 联系表”，选择 A4 或 Letter 和 2–4 列。最多 120 张所选图片按时间排列，自动分页，并附有视频名和时间戳。未选择图片时使用全部剩余结果；PNG 联系表仍最多包含 40 帧。

## 从源视频附近画面中精确选帧

在 Mac 上选中一张结果，逐帧查看附近的源画面，再添加新图片或替换所选图片。这项查看功能需要当前工作区中的源视频仍然可用。

[![使用示例视频的 Mac 结果页与源画面查看。截图为英文界面。](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

使用示例视频的 Mac 结果页与源画面查看。截图为英文界面。

示例视频：Big Buck Bunny。© 2008 Blender Foundation。画面由 Dig It 排列。 [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## 保存以后还能继续编辑的结果集

“保存”会把当前结果图片及可用的时间戳、评分保存在本机历史记录中。重新打开后可查看、删除、导出，再覆盖保存到同一记录。历史记录不保存源视频；较旧的仅元数据记录无法重建缺失图片。

## PNG 联系表：最多 40 帧

每张 PNG 联系表最多包含 40 帧。更多画面可以选择“PDF 联系表”，最多支持 120 帧并自动分页。Mac 批量工作区也可自动导出 PNG 联系表和 PDF。

## 常见问题

### Dig It 会上传我的视频吗？

不会。视频分析和抽帧在设备上完成。是否分享导出的文件由你决定，本地提取不需要联网。

### 需要安装 FFmpeg 吗？

不需要。App Store 版使用 Apple 的本地视频处理框架，图形界面工作流不要求终端命令或另装 FFmpeg。

### Dig It 是免费的吗？

Dig It 目前在 App Store 免费提供。最新价格和设备兼容性请以官方下载页面为准。

### 历史记录会保留原视频吗？

不会。历史记录保留主动保存的结果图片和元数据，不包含源视频。Mac 的源画面查看需要当前工作区里仍有可用的源视频。

### 导出的每张图片都保持原视频分辨率吗？

预览图片保持在 720 × 720 像素内。Mac 的“源视频分辨率”导出会按需解码原视频并保留源画面尺寸。Mac 封面优先使用可用的源视频，否则使用已保存图片的分辨率。不会把预览图片或低分辨率源视频放大为原画。

### 从 App Store 下载后就能使用 CLI 吗？

不能。digit CLI 是独立的 Mac 工具，目前没有公开下载入口。请先向支持咨询获取方式，再使用命令示例。目前未提供 MCP 集成。

### 为什么需要照片权限？

只用于选择源视频/图片，以及在你要求时保存导出结果。

## 可选的 Mac 命令行工具

digit CLI 独立于 App Store 版 App，目前尚未公开分发。请向支持咨询获取方式。下面的命令适用于已经安装独立工具的用户。
[咨询 CLI 获取方式](https://digit-video.luopeike.com/zh-Hans/support)

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
