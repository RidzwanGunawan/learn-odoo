from odoo import models, fields, api

class RentalProduct(models.Model):
    _name = 'rental.product'
    _description = 'Rental Product'
    
    product_id = fields.Many2one('product.product', string='Product', required=True)
    rental_ok = fields.Boolean(string='Can be Rented', default=True)
    rental_pricing_ids = fields.One2many(
        'rental.pricing', 'rental_product_id', string='Rental Pricing')
    schedule_ids = fields.One2many(
        'rental.schedule', 'rental_product_id', string='Rental Schedules')
    
    _sql_constraints = [
        ('product_unique', 'unique(product_id)', 'Product can only have one rental configuration!'),
    ]