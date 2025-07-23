from odoo import models, fields, api
from datetime import datetime, timedelta

class RentalOrderLine(models.Model):
    _name = 'rental.order.line'
    _description = 'Rental Order Line'
    
    rental_order_id = fields.Many2one('rental.order', string='Rental Order', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    rental_product_id = fields.Many2one('rental.product', string='Rental Product', related='product_id.rental_product_id')
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(string='Unit Price', compute='_compute_price_unit', store=True)
    price_subtotal = fields.Float(string='Subtotal', compute='_compute_price_subtotal', store=True)
    
    @api.depends('start_date', 'end_date', 'product_id')
    def _compute_price_unit(self):
        for line in self:
            if line.start_date and line.end_date and line.product_id:
                duration = (line.end_date - line.start_date).total_seconds() / 3600  # in hours
                line.price_unit = line.product_id._compute_rental_price(duration)
            else:
                line.price_unit = 0.0
    
    @api.depends('price_unit', 'quantity')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.price_unit * line.quantity
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.rental_product_id = self.product_id.rental_product_id