# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    sequence = fields.Char(string='Sequence', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('hospital.patient.seq'))
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    dni = fields.Char(string='DNI', required=True)
    treatment_ids = fields.Many2many('hospital.treatment', string='Treatments')
    date_admitted = fields.Datetime(string='Admission Date', default=fields.Datetime.now)
    date_updated = fields.Datetime(string='Last Updated', readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('admitted', 'Admitted'), ('discharged', 'Discharged')], string='State', default='draft')
    chatter = fields.Html(string='Chatter', readonly=True)

    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if not record.dni.isdigit():
                raise ValidationError("DNI must only contain digits.")

    def action_change_state(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'admitted'
            elif record.state == 'admitted':
                record.state = 'discharged'
            else:
                record.state = 'draft'

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Hospital Treatment'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    doctor = fields.Char(string='Doctor')
