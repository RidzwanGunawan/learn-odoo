from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_rental = fields.Boolean(string='Can be Rented')
    rental_pricing_ids = fields.One2many(
        'rental.pricing', 'product_id', string='Rental Pricing')
    rental_description = fields.Text(string='Rental Description')

class RentalPricing(models.Model):
    _name = 'rental.pricing'
    _description = 'Rental Pricing'
    
    product_id = fields.Many2one('product.template', string='Product')
    duration = fields.Float(string='Duration')
    unit = fields.Selection([
        ('hour', 'Hours'),
        ('day', 'Days'),
        ('week', 'Weeks'),
        ('month', 'Months')], string='Unit')
    price = fields.Float(string='Price')