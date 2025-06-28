from odoo import models, fields, api

class ElearningMaterial(models.Model):
    _name = 'elearning.course.material'
    _description = 'Course Material'

    course_id = fields.Many2one('elearning.course', string="Course", required=True)
    title = fields.Char(string="Title", required=True)
    content_type = fields.Selection([
        ('pdf', 'PDF'),
        ('video', 'Video'),
        ('link', 'External Link')
    ], string="Content Type", required=True)
    file = fields.Binary(string="Upload File")
    url = fields.Char(string="External URL")

    @api.depends('course_id.type')
    def _compute_show_category(self):
        for record in self:
            record.show_category = record.course_id.type != 'online' if record.course_id else False

    show_category = fields.Boolean(compute='_compute_show_category')
