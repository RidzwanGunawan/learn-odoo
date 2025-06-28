# Elearning Subscription

**Elearning Subscription** adalah modul Odoo kustom yang menyediakan fitur sistem pembelajaran daring (e-learning) berbasis langganan. Modul ini dirancang untuk mengelola kursus, materi pelajaran, dan memungkinkan pengguna untuk mengakses konten sesuai dengan langganan yang dimiliki.

## 📦 Fitur Utama

- **Manajemen Kursus**
  - Menambahkan dan mengelola kursus pembelajaran.
  - Kategori kursus yang terstruktur.
  
- **Materi Pembelajaran**
  - Mendukung upload materi berupa PDF, video, atau tautan eksternal.
  - Materi dapat dikaitkan dengan kursus tertentu.

- **Langganan Kursus**
  - Pengguna dapat mengakses kursus berdasarkan status langganan.
  - Cocok untuk platform pembelajaran berbayar.

- **Hak Akses Terkelola**
  - Kontrol akses terhadap data kursus dan materi.
  - Grup pengguna dapat diatur untuk akses admin atau pengguna biasa.

## 🛠 Instalasi

1. Salin folder `elearning_subscription` ke dalam direktori `addons` Anda.
2. Aktifkan mode developer di Odoo.
3. Masuk ke menu **Aplikasi**, klik **Perbarui Daftar Aplikasi**.
4. Cari `Elearning Subscription`, lalu klik **Install**.

## 🔐 Hak Akses

Pastikan Anda telah mengatur akses pada file:
``security/ir.model.access.csv``  
File ini menentukan siapa yang bisa membuat, membaca, menulis, dan menghapus data di model yang tersedia.

## 🗂 Struktur Modul
elearning_subscription/
├── manifest.py
├── models/
│ ├── init.py
│ ├── course.py
│ ├── material.py
├── views/
│ ├── course_views.xml
│ ├── material_views.xml
│ ├── menu.xml
├── security/
│ ├── ir.model.access.csv
├── README.md


## ✅ Ketergantungan

Modul ini bergantung pada:
- `base`
- (Opsional) `website`, `portal` jika akan dikembangkan ke arah portal pengguna

## 👨‍💻 Pengembangan

Jika Anda ingin mengembangkan modul ini lebih lanjut:
- Tambahkan relasi ke `res.users` atau `res.partner` untuk sistem user.
- Gunakan controller untuk membuat frontend (jika dibutuhkan).
- Tambahkan fitur sertifikat atau evaluasi untuk siswa.

## 📄 Lisensi

Modul ini berada di bawah lisensi Odoo Community Edition (LGPL v3).

