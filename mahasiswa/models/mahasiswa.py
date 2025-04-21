from odoo import models, fields, api
from datetime import datetime
import time

class DataMahasiswa(models.Model):
    _name = 'data.mahasiswa'
    _description = 'Data Mahasiswa'

    npm = fields.Char(
        string='NPM',
        required=True,
        index= True,
        size=10,
        help='Nomor Pokok Mahasiswa (NPM) terdiri dari 10 digit angka unik untuk setiap mahasiswa.'
    )
    nama = fields.Char(
        string='Nama',
        required=True,
        index=True,
        help='Masukkan nama lengkap mahasiswa sesuai identitas resmi.'
    )
    tanggal_lahir = fields.Date(
        default=fields.date.today()
    )
    usia = fields.Integer(
        string='Usia', 
        required=True,
        compute='_compute_usia',
        store=True,
    )
    alamat = fields.Text(
        required=True,
        help='Masukkan alamat tempat tinggal mahasiswa secara lengkap.'
    )
    gender = fields.Selection(
        [
            ('laki-laki', 'Laki-Laki'),
            ('perempuan', 'Perempuan'),
        ],
        required=True,
        default='laki-laki'
    )
    prodi = fields.Selection(
        selection='_get_prodi_list', 
        string='Program Studi',
        required=True
    )
    waktu_pendaftaran = fields.Datetime(
        string='Waktu Pendaftaran',
        default=fields.Datetime.now(),
        help='Waktu lengkap saat mahasiswa didaftarkan.',
        readonly=True,
        required=True
    )
    matakuliah = fields.Selection(
        selection='_get_matakuliah_list', 
        string='Mata Kuliah', 
        required=True,
        default='web dev'
    )
    total_sks = fields.Float(
        string='Total SKS', 
        digits=(3,2),
        required=True
    )
    is_aktif = fields.Boolean(
        string='Aktif',
        help='Centang jika mahasiswa masih aktif.'
    )
    dosen_wali_id = fields.Many2one(
        comodel_name='data.dosen',
        string='Dosen Wali',
        help='Pilih dosen wali untuk mahasiswa ini.'
    )
    dosen_wali_nama = fields.Char(
        string='Nama Dosen Wali',
        related='dosen_wali_id.nama',  # Ambil nama dosen dari relasi dosen_wali_id
        store=True,  # Agar bisa dicari dan difilter
        help='Dosen wali yang dipilih akan otomatis di tampilkan disini'
    )
    ukm_ids = fields.Many2many(
        'data.ukm',
        'rel_ukm_mahasiwa',
        'mahasiswa_id',
        'ukm_id',
        string= 'Organisasi yang diikuti'
    )
    jumlah_ukm_diikuti = fields.Integer(
        string='Jumlah UKM Diikuti',
        compute='_compute_jumlah_ukm',
        store=True
    )
    reference_field = fields.Reference(
        selection=[
            ('data.dosen', 'Dosen Wali'),
            ('data.ukm', 'UKM'),
        ],
        string='Referensi Wali atau UKM'
    )
    catatan = fields.Html(
        string='Catatan Tambahan',
        help='Isi catatan tambahan seperti prestasi, keterangan akademik, atau lainnya.'
    )
    data_tambahan = fields.Json(
        string='Data Tambahan',
        help='Data opsional dalam format JSON seperti hobi, sertifikat, atau preferensi belajar.'
    )
  

    @api.model
    def _get_prodi_list(self):
        return [
            ('infomartika', 'Informatika'),
            ('manajemen', 'Manajemen'),
            ('elektro', 'Elektro')
        ]
    
    @api.model
    def _get_matakuliah_list(self):
        return [
            ('web dev', 'Web Development'),
            ('data analys', 'Data Analys'),
            ('mobile dev', 'Mobile Development')
        ]
    
    @api.depends('tanggal_lahir')
    def _compute_usia(self):
        today = datetime.today()
        for record in self:
            if record.tanggal_lahir:
                record.usia = today.year - record.tanggal_lahir.year - (
                    (today.month, today.day) < (record.tanggal_lahir.month, record.tanggal_lahir.day)
                )
            else:
                record.usia = 0
    
    @api.depends('ukm_ids')
    def _compute_jumlah_ukm(self):
        for rec in self:
            rec.jumlah_ukm_diikuti = len(rec.ukm_ids)


