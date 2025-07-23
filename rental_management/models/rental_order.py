from odoo import models, fields, api
from datetime import datetime, timedelta

class RentalOrder(models.Model):
    _name = 'rental.order'
    _description = 'Rental Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('rental.order'))
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    date_order = fields.Datetime(string='Order Date', required=True, default=fields.Datetime.now)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    rental_order_line_ids = fields.One2many('rental.order.line', 'rental_order_id', string='Rental Lines')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft', tracking=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    
    @api.depends('rental_order_line_ids.price_subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_subtotal for line in order.rental_order_line_ids)
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_done(self):
        self.write({'state': 'done'})
    
    def action_cancel(self):
        self.write({'state': 'canceled'})
    
    def action_draft(self):
        self.write({'state': 'draft'})