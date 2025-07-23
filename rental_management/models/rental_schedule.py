from odoo import models, fields, api

class RentalSchedule(models.Model):
    _name = 'rental.schedule'
    _description = 'Rental Schedule'
    
    rental_product_id = fields.Many2one('rental.product', string='Rental Product', required=True)
    rental_order_id = fields.Many2one('rental.order', string='Rental Order', required=True)
    rental_order_line_id = fields.Many2one('rental.order.line', string='Rental Order Line', required=True)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    state = fields.Selection(related='rental_order_id.state', string='Status', store=True)
    
    def name_get(self):
        result = []
        for record in self:
            name = "%s - %s to %s" % (record.rental_product_id.product_id.name, record.start_date, record.end_date)
            result.append((record.id, name))
        return result