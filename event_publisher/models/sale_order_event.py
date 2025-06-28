from odoo import models, api
import requests
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for order in self:
            order.send_event()
        
        return res
    
    def send_event(self):
        try:
            payload = {
               "order_id": self.id,
                "customer": self.partner_id.name,
                "total": self.amount_total,
                "status": self.state,
            }
            response = requests.post("https://webhook.site/", json=payload) 
            _logger.info("event sent: %s - status: %s", payload, response.status_code)
        except Exception as e:
            _logger.info("failed to send event: %s", str(e))