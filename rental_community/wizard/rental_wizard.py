from odoo import models, fields, api

class RentalConfigWizard(models.TransientModel):
    _name = 'rental.config.wizard'
    _description = 'Rental Configuration Wizard'
    
    default_rental_location_id = fields.Many2one(
        'stock.location', string='Default Rental Location')
    default_return_location_id = fields.Many2one(
        'stock.location', string='Default Return Location')
    
    def set_default_locations(self):
        config = self.env['ir.config_parameter'].sudo()
        config.set_param('rental_community.default_rental_location_id', self.default_rental_location_id.id)
        config.set_param('rental_community.default_return_location_id', self.default_return_location_id.id)
        return {'type': 'ir.actions.act_window_close'}