from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError, ValidationError

class UKM(models.Model):
    _name = 'data.ukm'
    _description = 'data UKM Universitas'
    _rec_name = 'nama' 


    nama = fields.Char(
        string='Nama UKM',
    )
    kategori = fields.Selection(
        selection='_get_kategori_ukm',
        string='Kategori',
    )
    mahasiswa_ids = fields.Many2many(
        'data.mahasiswa',
        'rel_ukm_mahasiwa',
        'ukm_id',
        'mahasiswa_id',
        string= 'Anggota Mahasiswa'
    )
    reference_field = fields.Reference(
        selection=[
            ('data.dosen', 'Dosen Wali'),
            ('data.mahasiswa', 'Mahasiswa'),
        ],
        string='Referensi Dosen atau Mahasiswa'
    )
    foto_ukm = fields.Binary(
        string='Foto UKM',
        attachment=True,
        help='Unggah Logo UKM' 
    )
    logo_foto_ukm = fields.Char(
        string='Nama file Gambar'
    )

    @api.model
    def _get_kategori_ukm(self):
        return [
            ('olahraga', 'Olahraga'),
            ('seni', 'Seni'),
            ('agama', 'Agama'),
            ('ilmiah', 'Ilmiah'),
        ]
    
    @api.onchange('foto_ukm')
    def _onchange_foto_ukm(self):
        if self.foto_ukm:
            # Otomatis isi nama file dengan waktu + nama ukm (opsional)
            self.logo_foto_ukm = f"{self.nama or 'gambar'}_foto.jpg"

    # * Create Method
    @api.model_create_multi
    def create_new_ukm(self, vals):
        vals_list = [
            {'nama': 'UKM Seni', 'kategori': 'Seni'},
            {'nama': 'UKM Olahraga', 'kategori': 'Olahraga'},
            {'nama': 'UKM Agama', 'kategori': 'Agama'}
        ]

        rtn = super(UKM, self).create(vals_list)
        print(rtn)
        return rtn
    
    # * Read Method
    @api.model
    def get_ukm_by_kategori(self, kategori):
        ukm_records = self.env['data.ukm'].search_read([('kategori', '=', kategori)])

        for ukm in ukm_records:
            print(ukm.nama)
        
        return ukm_records
    
    @api.model
    def get_ukm_by_kategori_read(self, kategori):
        ukm_records = self.env['data.ukm'].search([('kategori', '=', kategori)])
        ukm_data = ukm_records.read(['nama', 'kategori'])

        print('Read Method:')
        for data in ukm_data:
            print(data)

        return ukm_data
    
    @api.model
    def get_ukm_by_id(self, ukm_id):
        ukm_record = self.env['data.ukm'].browse(ukm_id)

        if ukm_record.exists():
            print(f"Browse Method: {ukm_record.nama}")
        else:
            print(f"UKM dengan ID {ukm_id} tidak ditemukan")
        
        return ukm_record
    
    @api.model
    def get_ukm_filtered(self, kategori):
        ukm_records = self.env['data.ukm'].search([])
        filtered_ukm = ukm_records.filtered(lambda r: r.kategori == kategori)

        print(f"Filtered Method ({kategori})")
        for ukm in filtered_ukm:
            print(ukm.nama)

        return filtered_ukm
    
    @api.model
    def get_ukm_count(self, kategori):
        count = self.env['data.ukm'].search_count([('kategori', '=', kategori)])
        
        print(f"Jumlah UKM dengan kategori {kategori}: {count}")
        return count
    
    @api.model
    def get_ukm_names_by_kategori(self, kategori):
        ukm_records = self.env['data.ukm'].search([('kategori', '=', kategori)])
        nama_ukm_list = ukm_records.mapped('nama')
        
        print(f"Nama UKM dalam kategori '{kategori}': {nama_ukm_list}")
        return nama_ukm_list

    # @api.model
    # def get_ukm_get(self, ukm_id):
    #     ukm_record = self.env['data.ukm'].browse(ukm_id)
    #     ukm_get = ukm_record.get()

    #     if ukm_get:
    #         print(f"Get Method: {ukm_get.nama}")
    #     else:
    #         print(f"Get Method: UKM dengan ID {ukm_id} tidak ditemukan")
        
    #     return ukm_get

    # * Update Method

    def write_data_ukm(self, vals=None):
        if vals is None:
            vals = {
                'nama': 'UKM Sains dan Technology',
                'kategori': 'ilmiah'
            }
        update_data = super(UKM, self).write(vals)
        return update_data
    
    # * Delete Method
    def unlink(self):
        for record in self:
            if record.kategori == 'ilmiah':
                raise UserError("UKM dengan kategori 'Ilmiah' tidak boleh di hapus")
            if not record.exists():
                raise ValidationError("Record sudah dihapus sebelumnya.")
        delete_data = super(UKM, self).unlink()
        return delete_data
 
 
    
        

