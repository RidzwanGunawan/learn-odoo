from odoo import api, fields, models
from datetime import datetime

class DosenWali(models.Model):
    _name = 'data.dosen'
    _description = 'Data Wali Dosen'
    _rec_name = 'nama' 

    nidn = fields.Char(
        string='NIDN',
        size=10,
        required=True,
        index=True
    )
    nama = fields.Char( 
        string='Nama',
        required=True,
        index=True,
        help='Masukkan nama lengkap mahasiswa sesuai identitas resmi.'
    )
    mahasiswa_ids = fields.One2many(
        comodel_name='data.mahasiswa',
        inverse_name='dosen_wali_id',
        string='Wali Dosen Mahasiswa'
    )
    reference_field = fields.Reference(
        selection=[
            ('data.mahasiswa', 'Mahasiswa'),
            ('data.ukm', 'UKM'),
        ],
        string='Referensi Mahasiswa atau UKM'
    )
    salary = fields.Monetary(
        string='Salary',
        currency_field='currency_id'
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Mata Uang',
        default=lambda self: self.env.company.currency_id,
    )