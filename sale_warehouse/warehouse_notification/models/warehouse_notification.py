from odoo import models, fields

class WarehouseNotification(models.Model):
    _name = 'warehouse.notification'
    _description = 'Warehouse Notification'

    order_id = fields.Integer(string="Order ID")
    customer = fields.Char(string="Customer")
    total = fields.Integer(string="Total Amount")
    message = fields.Char(string="Message")
    state = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
    ], default='pending')

    def action_mark_done(self):
        for rec in self:
            rec.state = 'done'

