from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta

class RentalBarang(models.Model):
    _name = 'rental.barang'
    _inherit = ['mail.thread']
    _description = 'Rental Barang'
    
    name = fields.Char(string='Kode Rental', required=True, copy=False, default='New')
    
    partner_id = fields.Many2one('res.partner', string='Penyewa', required=True, ondelete='restrict')
    product_id = fields.Many2one('product.product', string='Barang yang Disewa', required=True, ondelete='restrict')
    
    no_ktp = fields.Char(string="No.KTP", required=True, size=16)
    no_sim = fields.Char(string="No.SIM", required=True, size=16) 
    contact = fields.Char(string="No.HP", required=True, size=12)
    adresss = fields.Text(string="Alamat", required=True)
    
    tanggal_mulai = fields.Date(string='Tanggal Mulai', default=fields.Date.today(), required=True)
    tanggal_selesai = fields.Date(string='Tanggal Selesai', required=True)
    durasi_hari = fields.Integer(string='Durasi Hari', compute='_compute_total_biaya', store=True, readonly=True)
    
    cancel_reason = fields.Text(string='Alasan Pembatalan')
    cancel_date = fields.Datetime(string='Tanggal Pembatalan')
    
    harga_per_hari = fields.Float(string='Harga per Hari', required=True)
    total_biaya = fields.Float(string='Total Biaya', compute='_compute_total_biaya', store=True, readonly=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True, group_expand="_read_group_stage_ids")
    
    @api.model
    def _read_group_stage_ids(self, stages=None, domain=None, order=None):
        return ['draft', 'confirmed', 'returned', 'cancelled']
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.barang') or 'New'
        return super(RentalBarang, self).create(vals)
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.harga_per_hari = self.product_id.list_price
    
    @api.depends('tanggal_mulai', 'tanggal_selesai', 'harga_per_hari')
    def _compute_total_biaya(self):
        for rec in self:
            if rec.tanggal_mulai and rec.tanggal_selesai:
                durasi = (rec.tanggal_selesai - rec.tanggal_mulai).days + 1
                rec.durasi_hari = durasi
                ppn = 0.11
                harga_dengan_ppn = rec.harga_per_hari * (1 + ppn)
                rec.total_biaya = durasi * harga_dengan_ppn
            else:
                rec.durasi_hari = 0
                rec.total_biaya = 0.0

    @api.constrains('tanggal_mulai', 'tanggal_selesai')
    def _check_tanggal(self):
        for rec in self:
            if rec.tanggal_mulai and rec.tanggal_selesai:
                if rec.tanggal_selesai < rec.tanggal_mulai:
                    raise ValidationError("Tanggal Selesai tidak boleh lebih awal dari Tanggal Mulai.")
    
    @api.constrains('product_id', 'tanggal_mulai', 'tanggal_selesai')
    def _check_double_booking(self):
        for rec in self:
            if not rec.tanggal_mulai or not rec.tanggal_selesai:
                continue

            domain = [
                ('id', '!=', rec.id),
                ('product_id', '=', rec.product_id.id),
                ('state', '=', 'confirmed'),
                ('tanggal_mulai', '<=', rec.tanggal_selesai),
                ('tanggal_selesai', '>=', rec.tanggal_mulai),
            ]
            conflict = self.search(domain, limit=1)
            if conflict:
                raise ValidationError(
                    f"Produk '{rec.product_id.name}' sudah disewa oleh '{conflict.partner_id.name}' dari "
                    f"{conflict.tanggal_mulai} hingga {conflict.tanggal_selesai}. Silakan pilih tanggal lain."
                )
    
    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError("Hanya bisa konfirmasi dari state Draft.")
            rec.state = 'confirmed'

    def action_return(self):
        for rec in self:
            if rec.state != 'confirmed':
                raise ValidationError("Hanya bisa Return dari state Confirmed.")
            rec.state = 'returned'

    def action_reset_to_draft(self):
        for rec in self:
            if rec.state != 'returned':
                raise ValidationError("Reset hanya dari state Returned.")
            rec.state = 'draft'
    
    def print_rental_report(self):
        report = self.env.ref('rental_barang.rental_barang_report_action', raise_if_not_found=False)
        if not report:
            raise UserError('Report action rental_barang.rental_barang_report_action not found')
        return report.report_action(self)

    def action_create_invoice(self):
        for rec in self:
            if rec.state != 'confirmed':
                raise ValidationError("Invoice hanya bisa dibuat dari rental yang sudah dikonfirmasi.")
            
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.partner_id.id,
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': [(0, 0, {
                    'product_id': rec.product_id.id,
                    'name': f"Sewa {rec.product_id.name} selama {rec.durasi_hari} hari",
                    'quantity': rec.durasi_hari,
                    'price_unit': rec.harga_per_hari,
                    'tax_ids': [(6, 0, rec.product_id.taxes_id.ids)],
                })],
                'invoice_origin': f"Rental {rec.name or rec.id}"
            })

            rec.message_post(body=f"Invoice dibuat: <a href='#id={invoice.id}&model=account.move'>{invoice.name}</a>")

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': invoice.id,
            }