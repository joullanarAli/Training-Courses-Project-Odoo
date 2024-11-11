from odoo import fields,models

class Course(models.Model):
    _name='training.course'
    _description='Training Course'

    name= fields.Char('Name', required=True)
    number_of_students=fields.Integer('Number of students',required=True)
    material_id = fields.Many2one('training.material', string='Material', copy=False)
    active = fields.Boolean('Is Active', copy=False)
    start_date = fields.Date('Start Date',copy=False, required=True)
    end_date = fields.Date('End Date', copy=False,required=True)
    type = fields.Selection([('online','Online'),('onsite','Onsite')],
                            string='Type',
                            required=True,
                            default = 'onsite'
    )
    responsible=fields.Char('Responsible', required=True)
    session_ids = fields.One2many('course.session', 'course_id', string="Sessions")
