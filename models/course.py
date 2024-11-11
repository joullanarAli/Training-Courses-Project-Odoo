from odoo import fields,models

class Course(models.Model):
    _name='training.course'
    _description='Training Course'

    name= fields.Char('Name', required=True)
    number_of_students=fields.Integer('Number of students',required=True)
    material_id = fields.Many2one('training.material', string='Material', copy=False)
