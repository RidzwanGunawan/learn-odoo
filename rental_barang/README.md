# Rental Barang – Odoo Community Module

Modul **Rental Barang** adalah solusi manajemen penyewaan barang untuk Odoo Community Edition. Modul ini dirancang agar mudah digunakan oleh admin dan staf internal untuk mencatat, memantau, dan mengelola transaksi sewa barang secara efisien.

## 📦 Fitur Utama

### 🎯 Manajemen Rental
- Pencatatan transaksi sewa barang.
- Penentuan durasi, harga per hari, dan total biaya otomatis.
- Status dokumen: `Draft`, `Confirmed`, `Cancelled`, `Returned`.

### 🧾 Faktur Otomatis
- Pembuatan invoice otomatis saat rental dikonfirmasi.
- Integrasi dengan modul `account`.

### 🛑 Validasi Otomatis
- Cek **double booking** (barang tidak bisa disewa jika masih disewa di tanggal yang sama).
- Validasi tanggal agar tidak terjadi konflik atau input tidak logis.

### 🔁 Status Rental
- Tombol aksi: `Konfirmasi`, `Return`, `Reset`, dan `Cancel`.
- Wizard pembatalan (`rental.cancel.wizard`) dengan alasan pembatalan yang tersimpan.

### 📊 Dashboard (terintegrasi dengan Invoice)
- Ringkasan transaksi muncul otomatis di dashboard (melalui modul invoice).

### 📥 Export Laporan ke Excel
- Wizard `Export Laporan Rental` untuk mengunduh laporan transaksi rental ke format **.xlsx** berdasarkan rentang tanggal.

### 🔍 Fitur Pencarian & Filter
- **Search Bar**:
  - Filter berdasarkan status (`Draft`, `Confirmed`, `Cancelled`).
  - Group By berdasarkan nama penyewam, produk dan status
- **Search Panel**:
  - Filter berdasarkan:
    - Status
    - Produk (barang yang disewa)
    - Penyewa

## 📁 Struktur Folder

rental_barang/
│
├── models/
│ ├── rental_barang.py
│ ├── rental_order.py
│ ├── rental_product.py
│ ├── rental_pricing.py
│ └── rental_schedule.py
│
├── wizard/
│ ├── export_rental_report_wizard.py
│ └── rental_cancel_wizard.py
│
├── views/
│ ├── rental_barang_views.xml
│ ├── rental_product_views.xml
│ ├── rental_cancel_wizard_views.xml
│ ├── rental_report_wizard_views.xml
│ └── rental_barang_menu.xml
│
├── report/
│ ├── rental_barang_report.xml
│ └── rental_barang_templates.xml
│
├── security/
│ └── ir.model.access.csv
│
└── manifest.py


## 🛠 Dependencies

Modul ini bergantung pada:
- `base`
- `product`
- `account`

## 🔧 Instalasi

1. Salin folder `rental_barang/` ke dalam direktori `addons` Odoo Anda.
2. Aktifkan virtual environment Anda jika belum.
3. Jalankan Odoo dan aktifkan modul melalui menu Aplikasi.
4. Pastikan dependensi sudah terinstal.
5. Login sebagai admin dan install modul `Rental Barang`.

## 📌 Catatan

- Modul ini **tidak** menggunakan fitur email notifikasi otomatis.
- Dikembangkan khusus untuk versi **Community**, tanpa fitur Enterprise seperti kalender OWL.

## 👨‍💻 Author

- **Nama**: Ridzwan Gunawan

---


