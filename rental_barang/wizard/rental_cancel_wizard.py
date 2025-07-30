from odoo import models, fields, api
from odoo.exceptions import UserError

class RentalCancelWizard(models.TransientModel):
    _name = 'rental.cancel.wizard'
    _description = 'Wizard Pembatalan Rental'

    cancel_reason = fields.Text(string='Alasan Pembatalan', required=True)

    def action_cancel_rental(self):
        active_id = self.env.context.get('active_id')
        rental = self.env['rental.barang'].browse(active_id)

        if rental.state not in ['draft', 'confirmed']:
            raise UserError("Hanya rental dalam status Draft atau Confirmed yang bisa dibatalkan.")

        rental.write({
            'state': 'cancelled',
            'cancel_reason': self.cancel_reason,
            'cancel_date': fields.Datetime.now(),
        })

        rental.message_post(body=f"Rental dibatalkan. Alasan: {self.cancel_reason}")
