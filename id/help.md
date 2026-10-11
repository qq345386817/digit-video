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

## Pilih gambar dari frame sumber terdekat

Di Mac, pilih satu hasil, telusuri frame sumber di sekitarnya, lalu tambahkan gambar atau ganti gambar terpilih. Video sumber harus tetap tersedia di ruang kerja saat ini.

[![Hasil Mac dan tinjauan frame sumber menggunakan video contoh. Antarmuka berbahasa Inggris.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Hasil Mac dan tinjauan frame sumber menggunakan video contoh. Antarmuka berbahasa Inggris.

Video contoh: Big Buck Bunny. © 2008 Blender Foundation. Frame disusun dengan Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Simpan kumpulan frame untuk diedit kembali

Simpan mempertahankan gambar hasil saat ini beserta stempel waktu dan skor yang tersedia di Riwayat lokal. Buka kembali proyek untuk meninjau, menghapus, mengekspor, dan menyimpan perubahan pada catatan yang sama. Video sumber tidak disimpan; catatan lama yang hanya berisi metadata tidak dapat membuat ulang gambar yang hilang.

## Maksimal 40 frame per lembar kontak di halaman hasil

Halaman hasil menerima paling banyak 40 frame untuk satu lembar. Untuk kumpulan lebih besar, pilih kelompok kecil dan lakukan beberapa ekspor. Lembar kontak adalah ikhtisar, bukan pengganti gambar terpisah. Preset batch Mac juga menyediakan keluaran lembar kontak opsional.

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

Frame yang diekstrak otomatis saat ini disesuaikan ke dalam 720 × 720 piksel dengan rasio tetap. Frame yang ditambahkan melalui tinjauan sumber Mac memakai resolusi sumber. Ekspor PNG tidak memperbesar frame yang lebih kecil.

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
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
