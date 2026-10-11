Canonical page: https://digit-video.luopeike.com/ja/help

Dig It

# Dig It ヘルプとサポート

Dig ItのMac一括処理、フレーム確認、コンタクトシート出力、保存済みプロジェクト、端末の違いを解説。CLIの提供状況とコマンド例も確認できます。

[App Store](https://apps.apple.com/app/id6508171056)

## MacとiPhone・iPadの違いは？

### Mac

Macには一括キュー、フォルダ読み込み、抽出プリセット、自動PNG/JPEG出力、近くの元動画フレームの確認があります。自動出力を有効にする前に出力先を選択してください。

### iPhone / iPad

iPhone・iPadでは写真やファイルから動画を1本選び、結果を確認して選択PNGやコンタクトシートを出力し、必要な結果を履歴に保存します。

## はじめに

1. バランス、カバー、手順を選びます。

2. ファイルまたは写真から動画を読み込みます。

3. 抽出されたフレームを確認し、残すものを選びます。

4. 選択した PNG を書き出すか、プロジェクトを履歴に保存します。

## 抽出モードの選び方

- バランス：多くの動画向けの扱いやすい中規模セット。

- カバー：サムネイルやカバー向けの少数で強いフレーム。

- 手順：チュートリアルや作業手順向けに変化点を多めに保持。

## 動画フレームの実用ワークフロー

[Macで動画フレームを一括抽出する 動画ファイルやフォルダを追加し、抽出プリセットを選び、結果を確認するかPNG/JPEG画像を自動出力できます。処理はMac内で行われます。 ガイドを読む →](https://digit-video.luopeike.com/ja/batch-extract-video-frames-on-mac)

[動画のコンタクトシートを作る コンタクトシートは複数の静止画を1枚のPNGにまとめます。カバー比較、場面の概要共有、チュートリアル手順の整理に使え、元動画を送る必要がありません。 ガイドを読む →](https://digit-video.luopeike.com/ja/video-contact-sheet)

## Mac で間隔や時刻を指定して動画フレームを抽出

新しい機能にはバージョン 1.4.3 以降が必要です。App Store でまだ更新できない場合も、従来の書き出し機能は利用できます。

Mac のワークスペースに動画を追加する前に、フレーム選択で自動キーフレーム、一定間隔、指定した時刻、均等にサンプリングを選び、上限を 1〜120 に設定します。一定間隔は上限で停止し、均等サンプリングは動画全体をカバーします。時刻は秒数や HH:MM:SS（例：5, 00:12.5, 01:30）で指定できます。自動書き出しでは元動画の解像度を有効にするか、結果を選択して「書き出す → 元の解像度で書き出す → PNG/JPEG」を使います。元画像は 1 枚ずつデコードして保存し、拡大しません。4K 出力には 4K の元動画が必要です。元の解像度での書き出しにはワークスペース内の元動画が必要です。

## カバー画像と印刷用 PDF コンタクトシートを書き出す

Mac、iPhone、iPad で結果を 1 枚選び、「書き出す → カバーを書き出す」を使います。元の比率、16:9、9:16、1:1、4:3、切り抜き位置、最大辺を設定して PNG/JPEG を保存できます。JPEG は 2 MB 以下に制限できます。収まらない場合は画像サイズを小さくしてください。画像は拡大しません。「PDF コンタクトシート」では A4/Letter と 2〜4 列を選べます。最大 120 枚を時刻順に自動でページ分けし、動画名と時刻を付けます。選択がなければ残りの全結果を使用します。PNG シートは引き続き最大 40 枚です。

## 近くの元動画フレームから画像を選ぶ

Macで結果を1枚選択し、付近の元動画フレームを確認して、画像を追加または置き換えます。この確認には、現在のワークスペースで元動画が利用できる必要があります。

[![サンプル動画を使ったMacの結果と元フレーム確認。表示は英語版です。](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

サンプル動画を使ったMacの結果と元フレーム確認。表示は英語版です。

サンプル動画：Big Buck Bunny。© 2008 Blender Foundation。Dig Itでフレームを配置。 [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## 後から編集できるフレームセットを保存

保存は現在の結果画像と、利用できる時刻・スコアをローカル履歴に保持します。再度開いて確認、削除、出力し、同じ記録に変更を保存できます。元動画は履歴に保存されません。メタデータのみの古い記録から失われた画像は再作成できません。

## PNG シート：最大 40 フレーム

PNG シートは最大 40 フレームです。より多くの画像を印刷する場合は、最大 120 フレームを自動ページ分けする PDF コンタクトシートを使ってください。Mac のバッチ処理でも PNG シートと PDF を出力できます。

## よくある質問

### Dig Itは動画をアップロードしますか？

いいえ。分析とフレーム抽出は端末内で行われます。出力ファイルの共有は自分で選択でき、ローカル抽出にインターネットは不要です。

### FFmpegは必要ですか？

不要です。App Store版はAppleのローカル動画処理フレームワークを使います。画面操作にターミナルコマンドや別途FFmpegのインストールは必要ありません。

### Dig Itは無料ですか？

現在はApp Storeで無料です。最新の価格と端末対応は公式ダウンロードページで確認してください。

### 履歴は元動画を保存しますか？

いいえ。明示的に保存した画像とメタデータを保持し、元動画は保存しません。Macで元フレームを確認するには、現在のワークスペースに元動画が必要です。

### 出力画像は元動画の解像度を維持しますか？

プレビューは 720 × 720 ピクセル以内です。Mac の元の解像度での書き出しは必要に応じて元動画をデコードし、元画像の寸法を維持します。Mac のカバーは利用できる元動画を使い、なければ保存画像の解像度を使います。低解像度の画像を拡大しません。

### App Store版にCLIは含まれますか？

含まれません。digit CLIは独立したMacツールで、現在は公開ダウンロードがありません。例を使う前にサポートへ入手方法を確認してください。MCP連携は提供していません。

### Why does it ask for Photos access?

Dig It uses Photos access only so you can choose source media and save exported results when you ask it to.

## 任意のMacコマンドラインツール

digit CLIはApp Store版とは別のツールで、現在は一般公開されていません。入手についてサポートへお問い合わせください。以下の例は独立ツールをインストール済みの方向けです。
[CLIの入手方法を問い合わせる](https://digit-video.luopeike.com/ja/support)

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
