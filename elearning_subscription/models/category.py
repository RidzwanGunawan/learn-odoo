from odoo import models, fields

class ElearningCategory(models.Model):
    _name = 'elearning.course.category'
    _description = 'Course Category'

    name = fields.Char(string="Category Name", required=True)
