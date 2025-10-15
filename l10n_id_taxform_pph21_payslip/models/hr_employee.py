from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    def _get_ptkp_monthly(self):
        """Get monthly PTKP based on marital status and dependents"""
        # PTKP values (annual)
        ptkp_single = 54000000
        ptkp_married = 58500000
        ptkp_dependent = 4500000
        
        # Get employee data
        marital = self.marital or 'single'
        dependents = self.dependents or 0
        
        # Calculate annual PTKP
        if marital in ['married', 'widower', 'widow']:
            annual_ptkp = ptkp_married + (dependents * ptkp_dependent)
        else:  # single, divorced
            annual_ptkp = ptkp_single
        
        # Return monthly PTKP
        return annual_ptkp / 12
    
    dependents = fields.Integer(
        string='Number of Dependents', 
        default=0,
        help='Jumlah tanggungan (anak/orang tua) untuk perhitungan PTKP PPh 21'
    )