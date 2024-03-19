# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class HospitalPatientController(http.Controller):

    @http.route('/odoo-domain/pacientes/consulta/<seq>', type='http', auth='public', csrf=False)
    def patient_info(self, seq):
        patient = request.env['hospital.patient'].search([('sequence', '=', seq)], limit=1)
        if patient:
            data = {
                'seq': patient.sequence,
                'name': patient.name + ' ' + patient.last_name,
                'dni': patient.dni,
                'state': patient.state
            }
            return json.dumps(data)
        else:
            return json.dumps({'error': 'Patient not found'})
