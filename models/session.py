from odoo import fields,models, api
from datetime import date, datetime
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name='course.session'
    _description='Course Session'

    
    name=fields.Char('Name', required=True)
    planned_date = fields.Date('Planned Date', required=True, copy=False)
    actual_date = fields.Date('Actual Date', copy=False)
    course_id = fields.Many2one('training.course', string ="Course", copy = False)

    _sql_constraints=[
        ('unique_name', 'unique (name)', 'Session name already exists!'),
    ]

    @api.constrains('planned_date')
    def check_planned_date(self):
        for record in self:
            if record.planned_date and record.planned_date < datetime.now().date():
                raise ValidationError("Planned Date must be in future")
    
    @api.constrains('actual_date')
    def check_actual_date(self):
        for record in self:
            if record.actual_date and record.actual_date > datetime.now().date():
                raise ValidationError("Actual date can't be in future")
