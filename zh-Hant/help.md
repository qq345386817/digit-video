Canonical page: https://digit-video.luopeike.com/zh-Hant/help

Dig It

# Dig It 幫助與支援

了解 Dig It 的 Mac 批次工作區、精確選取影格、聯絡表匯出、可編輯歷史紀錄與平台差異，並查看 CLI 取得狀態與指令範例。

[App Store](https://apps.apple.com/app/id6508171056)

## Mac、iPhone 和 iPad 有什麼不同？

### Mac

Mac 提供批次佇列、資料夾匯入、擷取預設、自動 PNG/JPEG 匯出和來源影片附近的逐格檢視。啟用自動匯出前須選擇輸出資料夾。

### iPhone / iPad

在 iPhone 和 iPad，從照片或檔案選擇一個影片，查看擷取的圖片，匯出所選 PNG 或聯絡表，並主動儲存結果至歷史紀錄。

## 快速開始

1. 選擇均衡、封面或步驟模式。

2. 從檔案或照片匯入影片。

3. 查看擷取出的畫面，並選擇值得保留的關鍵影格。

4. 匯出選中的 PNG 圖片，或把專案儲存到歷史記錄。

## 如何選擇擷取模式

- 均衡：適合多數影片的中等數量乾淨結果。

- 封面：更少但更強的封面、縮圖和主視覺候選。

- 步驟：保留更多變化點，適合教學、流程和操作內容。

## 實用的影片影格工作流程

[在 Mac 上批次擷取影片圖片 加入多個影片或整個資料夾，選好擷取預設，再逐一查看結果或自動匯出 PNG/JPEG 圖片。處理在 Mac 本機完成。 查看指南 →](https://digit-video.luopeike.com/zh-Hant/batch-extract-video-frames-on-mac)

[從影片製作拼接聯絡表 聯絡表將多張影片靜態影格拼成一張 PNG 總覽圖，適合比較封面、分享場景摘要或整理教學步驟，不必傳送原影片。 查看指南 →](https://digit-video.luopeike.com/zh-Hant/video-contact-sheet)

## 在 Mac 上按間隔或時間點擷取影片圖片

這些新工作流程需要 1.4.3 或更新版本。若所在地的 App Store 尚未提供更新，仍可使用原有的匯出功能。

在 Mac 工作區加入影片前，先選擇「影格選擇」：自動關鍵影格、固定間隔、指定時間點或均勻取樣，並設定 1–120 個影格的上限。固定間隔達到上限後停止；均勻取樣涵蓋完整時間軸。時間點支援秒數或 HH:MM:SS，例如 5, 00:12.5, 01:30。自動匯出時可開啟「來源影片解析度」，或在結果頁選取圖片，使用「匯出 → 匯出原畫 → PNG/JPEG」。原畫逐格解碼並儲存，不會放大圖片；4K 輸出需要 4K 來源影片。原畫匯出需要目前工作區中的來源影片仍可使用。

## 匯出封面圖片與可列印的 PDF 聯絡表

在 Mac、iPhone 或 iPad 上，選取一張結果，使用「匯出 → 匯出封面」。支援原始比例、16:9、9:16、1:1、4:3，可調整裁切位置和最大邊長，並儲存為 PNG 或 JPEG。JPEG 可限制為 2 MB，無法符合限制時請選擇較小的尺寸。圖片不會被放大。需要列印總覽時，使用「匯出 → PDF 聯絡表」，選擇 A4 或 Letter 和 2–4 欄。最多 120 張所選圖片按時間排列，自動分頁，並附有影片名稱和時間戳記。未選取圖片時使用全部剩餘結果；PNG 聯絡表仍最多包含 40 個影格。

## 從來源影片附近畫面精確選取影格

在 Mac 選取一張結果，逐格查看附近的來源畫面，再加入新圖片或替換所選圖片。此功能需要目前工作區的來源影片仍然可用。

[![使用範例影片的 Mac 結果頁與來源畫面檢視。截圖為英文介面。](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

使用範例影片的 Mac 結果頁與來源畫面檢視。截圖為英文介面。

範例影片：Big Buck Bunny。© 2008 Blender Foundation。畫面由 Dig It 排列。 [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## 儲存之後還能繼續編輯的結果集

「儲存」會將目前結果圖片及可用的時間戳記、評分存入本機歷史紀錄。重新開啟後可查看、刪除、匯出，再覆寫儲存至同一筆紀錄。歷史紀錄不儲存來源影片；較舊的僅中繼資料紀錄無法重建遺失的圖片。

## PNG 聯絡表：最多 40 個影格

每張 PNG 聯絡表最多包含 40 個影格。更多畫面可選擇「PDF 聯絡表」，最多支援 120 個影格並自動分頁。Mac 批量工作區也可自動匯出 PNG 聯絡表及 PDF。

## 常見問題

### Dig It 會上傳我的影片嗎？

不會。影片分析與影格擷取在裝置上完成。是否分享匯出檔案由你決定，本機擷取不需要網路。

### 需要安裝 FFmpeg 嗎？

不需要。App Store 版本使用 Apple 的本機影片處理框架，圖形介面流程不需要終端機指令或另外安裝 FFmpeg。

### Dig It 是免費的嗎？

Dig It 目前在 App Store 免費提供。最新價格與裝置相容性請以官方下載頁面為準。

### 歷史紀錄會保留原影片嗎？

不會。歷史紀錄保留主動儲存的結果圖片與中繼資料，不包含來源影片。Mac 的來源畫面檢視需要目前工作區仍有可用來源影片。

### 匯出圖片都保留原影片解析度嗎？

預覽圖片維持在 720 × 720 像素內。Mac 的「來源影片解析度」匯出會按需解碼原影片並保留來源畫面尺寸。Mac 封面優先使用可用的來源影片，否則使用已儲存圖片的解析度。不會把預覽圖片或低解析度來源影片放大為原畫。

### 從 App Store 下載後就能使用 CLI 嗎？

不能。digit CLI 是獨立 Mac 工具，目前沒有公開下載。請先向支援詢問取得方式，再使用指令範例。目前未提供 MCP 整合。

### 為什麼需要照片權限？

只用於選擇來源影片/圖片，以及在你要求時儲存匯出結果。

## 可選的 Mac 命令列工具

digit CLI 獨立於 App Store 版 App，目前尚未公開發行。請向支援詢問取得方式。以下指令適用於已安裝獨立工具的使用者。
[詢問 CLI 取得方式](https://digit-video.luopeike.com/zh-Hant/support)

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
