from odoo import models, fields

class ElearningCourse(models.Model):
    _name = 'elearning.course'
    _description = 'E-Learning Course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")
    category_id = fields.Many2one('elearning.course.category', string="Category")
    price = fields.Float(string="Price")
    duration_days = fields.Integer(string="Subscription Duration (days)")
    type = fields.Selection([
    ('online', 'Online'),
    ('offline', 'Offline')
    ], string="Course Type")
