# 🎥 Menentukan Koordinat Piksel dari Video dengan OpenCV

Proyek ini memungkinkan kamu untuk **mengklik titik pada video** untuk mendapatkan koordinat piksel **(x, y)** menggunakan pustaka **OpenCV**.
Setiap titik yang diklik akan terhubung dengan garis, membentuk jalur yang diperbarui secara dinamis saat video berjalan.

---

## 🚀 Fitur

* Menampilkan frame video secara real time.
* Klik di titik mana pun untuk mendapatkan koordinat piksel.
* Secara otomatis menampilkan koordinat `(X, Y)` di samping setiap titik yang diklik.
* Menggambar garis yang menghubungkan setiap titik berturut-turut.
* Jendela video dapat diubah ukurannya.
* Tekan **‘q’** untuk keluar dari program.

---

## 🧩 Persyaratan

Pastikan kamu sudah menginstal Python 3.x, lalu pasang dependensi berikut:

```bash
pip install opencv-python
```

---

## 💻 Cara Menjalankan

1. Kloning atau unduh repositori ini.
2. Letakkan file video kamu (misalnya `pos.mp4`) di folder yang sama dengan skrip.
3. Jalankan skrip dengan perintah:

   ```bash
   python get_coordinates.py
   ```
4. Setelah dijalankan, jendela video akan muncul:

   * **Klik kiri** di area mana pun pada video → menampilkan koordinat piksel di terminal dan pada video.
   * **Tekan ‘q’** → untuk keluar dari program.

---

## 🧠 Contoh Output

```
Koordinat Pixel: X=350, Y=220
Koordinat Pixel: X=560, Y=270
Koordinat Pixel: X=780, Y=300
```

Titik yang diklik akan muncul sebagai **lingkaran hijau** yang dihubungkan dengan **garis hijau**, dengan teks koordinat di sebelahnya.

---

## 📂 Struktur Proyek

```
📦 get-pixel-coordinates-video
 ┣ 📜 get_coordinates.py
 ┣ 📜 README.md
 ┗ 🎞️ pos.mp4
```

---

## 🖼️ Pratinjau

Kamu dapat menampilkan hasil contoh di README seperti ini:

![Preview](https://github.com/danty-putri/Menentukan-Koordinat-Dalam-Video/blob/main/Picture1.png)

---

## 📋 Catatan

* Kamu dapat mengubah variabel `video_path` dalam skrip untuk menggunakan file video lain.
* Mendukung format video umum seperti `.mp4`, `.avi`, `.mov`, dan lainnya yang didukung oleh OpenCV.

---

## 🧑‍💻 Author 
* Created by Putri Danty Apriani
* Machine Learning & Data Enthusiast 🚀
