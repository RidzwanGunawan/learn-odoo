from odoo import models, fields, api

class HrPayslipCustom(models.Model):
    _name = 'hr.payslip.custom'
    _description = 'Custom Payslip dengan PPh 21'
    _order = 'date_from desc'
    
    name = fields.Char(
        string='Reference', 
        required=True, 
        readonly=True, 
        default='New',
        help='Nomor referensi payslip yang dibuat otomatis oleh sistem'
    )
    employee_id = fields.Many2one(
        'hr.employee', 
        string='Employee', 
        required=True,
        help='Pilih karyawan yang akan dibuatkan payslip'
    )
    date_from = fields.Date(
        string='From Date', 
        required=True, 
        default=fields.Date.context_today,
        help='Tanggal mulai periode gaji (contoh: 1 Oktober 2025)'
    )
    date_to = fields.Date(
        string='To Date', 
        required=True, 
        default=fields.Date.context_today,
        help='Tanggal akhir periode gaji (contoh: 31 Oktober 2025)'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft',
        help='Status payslip: Draft (bisa edit), Confirmed (menunggu validasi), Done (selesai)'
    )
    
    # Basic Salary Components
    basic_salary = fields.Float(
        string='Basic Salary', 
        required=True, 
        default=0,
        help='Gaji pokok bulanan karyawan (wajib diisi)'
    )
    transport_allowance = fields.Float(
        string='Transport Allowance', 
        default=0,
        help='Tunjangan transportasi bulanan'
    )
    meal_allowance = fields.Float(
        string='Meal Allowance', 
        default=0,
        help='Tunjangan makan bulanan'
    )
    position_allowance = fields.Float(
        string='Position Allowance', 
        default=0,
        help='Tunjangan jabatan bulanan'
    )
    other_allowance = fields.Float(
        string='Other Allowance', 
        default=0,
        help='Tunjangan lainnya yang tidak termasuk di atas'
    )
    bonus = fields.Float(
        string='Bonus', 
        default=0,
        help='Bonus atau insentif bulanan'
    )
    
    # Deductions
    bpjs_kes = fields.Float(
        string='BPJS Kesehatan', 
        default=0,
        help='Premi BPJS Kesehatan yang dipotong dari gaji'
    )
    bpjs_tk = fields.Float(
        string='BPJS Ketenagakerjaan', 
        default=0,
        help='Premi BPJS Ketenagakerjaan (JHT, JKK, JKM) yang dipotong dari gaji'
    )
    other_deductions = fields.Float(
        string='Other Deductions', 
        default=0,
        help='Potongan lainnya seperti pinjaman, dll'
    )
    
    # PPh 21 Fields
    pph21_deducted = fields.Float(
        string='PPh 21 Dipotong', 
        compute='_compute_pph21', 
        store=True,
        help='Jumlah PPh 21 yang dipotong untuk bulan ini (otomatis)'
    )
    pph21_accumulated = fields.Float(
        string='PPh 21 Terakumulasi', 
        compute='_compute_pph21', 
        store=True,
        help='Total PPh 21 yang sudah dipotong hingga bulan ini (otomatis)'
    )
    pph21_taxable_income = fields.Float(
        string='Penghasilan Kena Pajak', 
        compute='_compute_pph21', 
        store=True,
        help='Penghasilan yang dikenakan pajak setelah dikurangi BPJS (otomatis)'
    )
    
    # Totals
    gross_salary = fields.Float(
        string='Gross Salary', 
        compute='_compute_totals', 
        store=True,
        help='Total penghasilan kotor sebelum potongan (otomatis)'
    )
    total_deductions = fields.Float(
        string='Total Deductions', 
        compute='_compute_totals', 
        store=True,
        help='Total semua potongan termasuk BPJS dan PPh 21 (otomatis)'
    )
    net_salary = fields.Float(
        string='Net Salary', 
        compute='_compute_totals', 
        store=True,
        help='Take home pay setelah semua potongan (otomatis)'
    )
    
    @api.depends('basic_salary', 'transport_allowance', 'meal_allowance', 
                 'position_allowance', 'other_allowance', 'bonus',
                 'bpjs_kes', 'bpjs_tk', 'other_deductions', 'pph21_deducted')
    def _compute_totals(self):
        for slip in self:
            # Calculate gross salary
            slip.gross_salary = (slip.basic_salary + slip.transport_allowance + 
                               slip.meal_allowance + slip.position_allowance + 
                               slip.other_allowance + slip.bonus)
            
            # Calculate total deductions (INCLUDE PPh 21)
            slip.total_deductions = slip.bpjs_kes + slip.bpjs_tk + slip.other_deductions + slip.pph21_deducted
            
            # Calculate net salary (SETELAH semua potongan termasuk PPh 21)
            slip.net_salary = slip.gross_salary - slip.total_deductions
    
    @api.depends('gross_salary', 'employee_id', 'bpjs_kes', 'bpjs_tk')
    def _compute_pph21(self):
        for slip in self:
            employee = slip.employee_id
            
            # Get PTKP based on marital status and dependents
            ptkp_monthly = employee._get_ptkp_monthly()
            
            # Calculate taxable income (Gross - BPJS)
            taxable_income = slip.gross_salary - (slip.bpjs_kes + slip.bpjs_tk)
            
            # Calculate taxable income after PTKP
            taxable_after_ptkp = max(0, taxable_income - ptkp_monthly)
            
            # Calculate PPh 21 based on tax brackets
            pph21 = self._calculate_pph21(taxable_after_ptkp)
            
            slip.pph21_taxable_income = taxable_income
            slip.pph21_deducted = pph21
            # For accumulated, you might want to query previous months
            slip.pph21_accumulated = pph21
    
    def _calculate_pph21(self, taxable_income):
        """Calculate PPh 21 based on Indonesian tax brackets"""
        if taxable_income <= 0:
            return 0
        
        # Annualize the income
        annual_income = taxable_income * 12
        
        # Tax brackets 2024
        bracket1 = 60000000  # 5%
        bracket2 = 250000000 # 15%
        bracket3 = 500000000 # 25%
        
        tax = 0
        if annual_income <= bracket1:
            tax = annual_income * 0.05
        elif annual_income <= bracket2:
            tax = (bracket1 * 0.05) + ((annual_income - bracket1) * 0.15)
        elif annual_income <= bracket3:
            tax = (bracket1 * 0.05) + ((bracket2 - bracket1) * 0.15) + ((annual_income - bracket2) * 0.25)
        else:
            tax = (bracket1 * 0.05) + ((bracket2 - bracket1) * 0.15) + ((bracket3 - bracket2) * 0.25) + ((annual_income - bracket3) * 0.30)
        
        # Return monthly tax
        return tax / 12
    
    def action_confirm(self):
        """Confirm payslip - move from Draft to Confirmed"""
        self.write({'state': 'confirmed'})
    
    def action_done(self):
        """Validate payslip - move from Confirmed to Done"""
        self.write({'state': 'done'})
    
    def action_cancel(self):
        """Cancel payslip"""
        self.write({'state': 'cancel'})
    
    def action_draft(self):
        """Set payslip back to Draft"""
        self.write({'state': 'draft'})
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hr.payslip.custom') or 'New'
        return super().create(vals)