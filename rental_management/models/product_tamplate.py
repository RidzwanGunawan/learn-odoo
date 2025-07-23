from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    rental_ok = fields.Boolean(string='Can be Rented')
    rental_product_id = fields.Many2one('rental.product', string='Rental Configuration')
    
    def _compute_rental_price(self, duration_hours):
        self.ensure_one()
        if not self.rental_product_id:
            return 0.0
        
        # Find the best pricing based on duration
        pricing = self.env['rental.pricing'].search([
            ('rental_product_id', '=', self.rental_product_id.id)
        ], order='duration, unit', limit=1)
        
        if not pricing:
            return 0.0
        
        # Convert duration to pricing unit
        if pricing.unit == 'hour':
            multiplier = 1
        elif pricing.unit == 'day':
            multiplier = 24
        elif pricing.unit == 'week':
            multiplier = 24 * 7
        elif pricing.unit == 'month':
            multiplier = 24 * 30  # Approximation
        
        duration_in_unit = duration_hours / multiplier
        return pricing.price * duration_in_unit