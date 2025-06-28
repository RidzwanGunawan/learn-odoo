from odoo import models, fields, api
from datetime import timedelta
from datetime import date

class ElearningSubscription(models.Model):
    _name = 'elearning.subscription'
    _description = 'Course Subscription'
    _order = 'state, start_date desc'
    _rec_name = 'course_id'
    _state_field = 'state'

    user_id = fields.Many2one('res.users', string='User')
    course_id = fields.Many2one('elearning.course', string='Course')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date', compute='_compute_end_date', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string='Status', default='draft', tracking=True)

    progress = fields.Integer(string="Progress (%)", compute="_compute_progress", store=True)

    @api.depends('start_date')
    def _compute_end_date(self):
        for rec in self:
            if rec.start_date:
                rec.end_date = rec.start_date + timedelta(days=30)
            else:
                rec.end_date = False

    @api.depends('start_date', 'end_date')
    def _compute_progress(self):
        today = date.today()
        for rec in self:
            if rec.start_date and rec.end_date and rec.start_date <= today <= rec.end_date:
                total_days = (rec.end_date - rec.start_date).days
                passed_days = (today - rec.start_date).days
                rec.progress = int((passed_days / total_days) * 100) if total_days else 0
            elif rec.end_date and today > rec.end_date:
                rec.progress = 100
            else:
                rec.progress = 0

    def action_activate(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'active'

    def action_expire(self):
        for rec in self:
            if rec.state == 'active':
                rec.state = 'expired'

    # optional: cron task yang jalan otomatis, tapi tidak mengganggu drag-drop
    @api.model
    def _cron_update_state(self):
        today = fields.Date.today()
        subs = self.search([])
        for rec in subs:
            if rec.start_date and rec.end_date:
                if rec.start_date <= today <= rec.end_date:
                    rec.state = 'active'
                elif today > rec.end_date:
                    rec.state = 'expired'
                else:
                    rec.state = 'draft'