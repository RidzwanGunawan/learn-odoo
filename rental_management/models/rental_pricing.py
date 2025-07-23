from odoo import models, fields, api

class RentalPricing(models.Model):
    _name = 'rental.pricing'
    _description = 'Rental Pricing'
    
    rental_product_id = fields.Many2one('rental.product', string='Rental Product')
    duration = fields.Float(string='Duration', required=True)
    unit = fields.Selection([
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
    ], string='Unit', required=True, default='day')
    price = fields.Float(string='Price', required=True)
    
    def name_get(self):
        result = []
        for record in self:
            name = "%s %s - %s" % (record.duration, record.unit, record.price)
            result.append((record.id, name))
        return result