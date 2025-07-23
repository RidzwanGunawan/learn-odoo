from odoo import models, fields, api

class RentalSchedule(models.Model):
    _name = 'rental.schedule'
    _description = 'Rental Schedule'
    _order = 'start_date'
    
    product_id = fields.Many2one('product.product', string='Product', required=True)
    order_line_id = fields.Many2one('sale.order.line', string='Order Line')
    start_date = fields.Datetime(string='Start Date', required=True)
    return_date = fields.Datetime(string='Return Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('reserved', 'Reserved'),
        ('rented', 'Rented'),
        ('returned', 'Returned'),
        ('cancel', 'Cancelled')], string='Status', default='draft')
    company_id = fields.Many2one(
        'res.company', 
        string='Company', 
        required=True,  # Add this
        default=lambda self: self.env.company  # Ensure default value
    )