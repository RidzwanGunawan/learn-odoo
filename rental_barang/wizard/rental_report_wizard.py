from odoo import models, fields

class RentalReportWizard(models.TransientModel):
    _name = 'rental.report.wizard'
    _description = 'Wizard Export Laporan Rental ke Excel'

    date_start = fields.Date(string="Tanggal Mulai", required=True)
    date_end = fields.Date(string="Tanggal Selesai", required=True)

    def action_redirect_download(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = f"{base_url}/rental/export_excel?date_start={self.date_start}&date_end={self.date_end}"
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }
