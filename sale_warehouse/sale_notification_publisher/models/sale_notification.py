from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()

        for order in self:
            self.env['warehouse.notification'].create({
                'order_id': order.id,
                'customer': order.partner_id.name,
                'total': order.amount_total,
                'message': f"Sales Order #{order.name} has been confirmed. Please prepare delivery.",
                'state': 'pending'
            })

        return res
    