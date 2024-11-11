from odoo import fields,models

class Material(models.Model):
    _name='training.material'
    _description='Training Material'

    name = fields.Char('Name', required=True)