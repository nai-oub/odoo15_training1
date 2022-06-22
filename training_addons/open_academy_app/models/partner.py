# -*- coding: utf-8 -*-


from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean('instructor', default=False)

    session_id = fields.Many2many('session', string="Attended sessions", readonly=True)
