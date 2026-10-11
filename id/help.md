Canonical page: https://digit-video.luopeike.com/id/help

Dig It

# Bantuan dan dukungan Dig It

Pelajari batch Mac, tinjauan frame, ekspor lembar kontak, proyek tersimpan, dan perbedaan platform Dig It. Lihat ketersediaan CLI serta contoh perintah.

[App Store](https://apps.apple.com/app/id6508171056)

## Apa perbedaan Mac, iPhone, dan iPad?

### Mac

Mac menambahkan antrean batch, impor folder, preset ekstraksi, ekspor otomatis PNG/JPEG, dan tinjauan frame sumber terdekat. Pilih folder keluaran sebelum mengaktifkan ekspor otomatis.

### iPhone / iPad

Di iPhone dan iPad, pilih satu video dari Foto atau File, tinjau gambar, ekspor PNG terpilih atau lembar kontak, dan simpan hasil ke Riwayat secara eksplisit.

## Mulai

1. Pilih Seimbang, Cover, atau Langkah.

2. Impor video dari File atau Foto.

3. Tinjau frame yang diekstrak dan pilih yang ingin disimpan.

4. Ekspor PNG pilihan atau simpan proyek ke riwayat.

## Memilih mode ekstraksi

- Seimbang: kumpulan bersih berukuran sedang untuk sebagian besar video.

- Cover: frame lebih sedikit namun lebih kuat untuk thumbnail dan cover.

- Langkah: lebih banyak titik perubahan untuk tutorial dan alur kerja.

## Alur kerja praktis untuk frame video

[Ekstrak frame video secara batch di Mac Tambahkan file video atau folder, pilih preset ekstraksi, lalu tinjau hasil atau ekspor gambar PNG/JPEG secara otomatis. Semua pemrosesan berlangsung di Mac Anda. Baca panduan →](https://digit-video.luopeike.com/id/batch-extract-video-frames-on-mac)

[Buat lembar kontak video Lembar kontak menggabungkan gambar video menjadi satu ikhtisar PNG. Gunakan untuk membandingkan sampul, berbagi ringkasan adegan, atau menyatukan langkah tutorial tanpa mengirim video asli. Baca panduan →](https://digit-video.luopeike.com/id/video-contact-sheet)

## Ekstrak frame berdasarkan interval atau waktu di Mac

Fitur baru ini memerlukan versi 1.4.3 atau lebih baru. Jika pembaruan belum tersedia di App Store Anda, opsi ekspor sebelumnya tetap bisa digunakan.

Sebelum menambah video ke ruang kerja Mac, pilih Keyframe Otomatis, Interval Tetap, Waktu Tertentu, atau Jarak Merata dan batas 1–120 frame. Interval Tetap berhenti pada batas; Jarak Merata mencakup seluruh video. Waktu dapat berupa detik atau HH:MM:SS, misalnya 5, 00:12.5, 01:30. Aktifkan Resolusi Sumber untuk ekspor otomatis atau pilih hasil lalu Ekspor → Ekspor Resolusi Sumber → PNG/JPEG. Frame asli didekode dan disimpan satu per satu tanpa diperbesar. Output 4K memerlukan sumber 4K dan video sumber harus tetap tersedia di ruang kerja.

## Ekspor sampul dan contact sheet PDF siap cetak

Di Mac, iPhone, atau iPad, pilih satu hasil lalu Ekspor → Ekspor Sampul. Pilih rasio asli, 16:9, 9:16, 1:1, atau 4:3, sesuaikan posisi potong dan sisi maksimum, lalu simpan PNG/JPEG. JPEG bisa dibatasi 2 MB; pilih dimensi lebih kecil jika tidak muat. Gambar tidak diperbesar. Untuk contact sheet PDF, pilih A4/Letter dan 2–4 kolom. Hingga 120 frame diurutkan menurut waktu dan dibagi otomatis ke halaman, dengan nama video dan waktu. Tanpa pilihan, semua hasil tersisa digunakan. Contact sheet PNG tetap dibatasi 40 frame.

## Pilih gambar dari frame sumber terdekat

Di Mac, pilih satu hasil, telusuri frame sumber di sekitarnya, lalu tambahkan gambar atau ganti gambar terpilih. Video sumber harus tetap tersedia di ruang kerja saat ini.

[![Hasil Mac dan tinjauan frame sumber menggunakan video contoh. Antarmuka berbahasa Inggris.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Hasil Mac dan tinjauan frame sumber menggunakan video contoh. Antarmuka berbahasa Inggris.

Video contoh: Big Buck Bunny. © 2008 Blender Foundation. Frame disusun dengan Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Simpan kumpulan frame untuk diedit kembali

Simpan mempertahankan gambar hasil saat ini beserta stempel waktu dan skor yang tersedia di Riwayat lokal. Buka kembali proyek untuk meninjau, menghapus, mengekspor, dan menyimpan perubahan pada catatan yang sama. Video sumber tidak disimpan; catatan lama yang hanya berisi metadata tidak dapat membuat ulang gambar yang hilang.

## Contact sheet PNG: maksimal 40 frame

Contact sheet PNG menerima hingga 40 frame. Untuk tampilan cetak lebih besar, pilih PDF: hingga 120 frame dengan halaman otomatis. Ruang kerja Mac juga dapat mengekspor contact sheet PNG dan PDF.

## Pertanyaan umum

### Apakah Dig It mengunggah video saya?

Tidak. Analisis dan ekstraksi dilakukan di perangkat. Anda memilih apakah akan membagikan file ekspor; ekstraksi lokal tidak memerlukan internet.

### Apakah saya perlu FFmpeg?

Tidak. App Store app menggunakan kerangka pemrosesan video lokal Apple. Alur kerja grafisnya tidak memerlukan perintah Terminal atau instalasi FFmpeg terpisah.

### Apakah Dig It gratis?

Dig It saat ini gratis di App Store. Lihat tautan unduhan resmi untuk harga dan kompatibilitas perangkat terbaru.

### Apakah Riwayat menyimpan video asli?

Tidak. Riwayat menyimpan gambar hasil yang disimpan secara eksplisit beserta metadata, bukan video sumber. Tinjauan sumber di Mac memerlukan video yang tersedia di ruang kerja saat ini.

### Apakah semua gambar mempertahankan resolusi asli?

Pratinjau muat dalam 720 × 720 piksel. Ekspor Resolusi Sumber di Mac mendekode video asli sesuai kebutuhan dan menjaga dimensinya. Sampul Mac memakai sumber yang tersedia atau resolusi gambar tersimpan. Gambar resolusi rendah tidak diperbesar.

### Apakah CLI termasuk dalam unduhan App Store?

Tidak. CLI digit adalah alat Mac terpisah yang saat ini belum memiliki unduhan publik. Hubungi dukungan tentang akses sebelum memakai contoh perintah. Integrasi MCP belum tersedia.

### Mengapa perlu akses Foto?

Akses Foto hanya digunakan untuk memilih media sumber dan menyimpan hasil saat diminta.

## Alat baris perintah opsional untuk Mac

CLI digit terpisah dari App Store app dan belum didistribusikan secara publik. Hubungi dukungan tentang akses. Contoh berikut ditujukan untuk pengguna yang sudah memasang alat mandiri tersebut.
[Tanyakan akses CLI ke dukungan](https://digit-video.luopeike.com/id/support)

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
