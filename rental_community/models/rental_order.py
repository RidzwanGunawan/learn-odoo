from odoo import models, fields, api
from datetime import datetime, timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    is_rental_order = fields.Boolean(string='Is Rental Order')
    rental_start_date = fields.Datetime(string='Rental Start Date')
    rental_return_date = fields.Datetime(string='Rental Return Date')
    rental_duration = fields.Float(string='Rental Duration', compute='_compute_rental_duration')
    
    @api.depends('rental_start_date', 'rental_return_date')
    def _compute_rental_duration(self):
        for order in self:
            if order.rental_start_date and order.rental_return_date:
                start = fields.Datetime.from_string(order.rental_start_date)
                return_ = fields.Datetime.from_string(order.rental_return_date)
                delta = return_ - start
                order.rental_duration = delta.total_seconds() / 3600  # in hours
            else:
                order.rental_duration = 0

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    is_rental = fields.Boolean(related='product_id.is_rental', string='Is Rental')
    rental_start_date = fields.Datetime(string='Rental Start Date')
    rental_return_date = fields.Datetime(string='Rental Return Date')
    rental_duration = fields.Float(string='Rental Duration', compute='_compute_rental_duration')
    
    @api.depends('rental_start_date', 'rental_return_date')
    def _compute_rental_duration(self):
        for line in self:
            if line.rental_start_date and line.rental_return_date:
                start = fields.Datetime.from_string(line.rental_start_date)
                return_ = fields.Datetime.from_string(line.rental_return_date)
                delta = return_ - start
                line.rental_duration = delta.total_seconds() / 3600  # in hours
            else:
                line.rental_duration = 0