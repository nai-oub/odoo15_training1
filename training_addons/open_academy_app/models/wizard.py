# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"


def _default_sessions(self):
    return self.env['session'].browse(self._context.get('active_ids'))


session_ids = fields.Many2many('session',
                               string="Sessions", required=True, default=_default_sessions)
attendee_id = fields.Many2many('res.partner', string="Attendees")


def subscribe(self):
    for session in self.session_ids:
        session.attendee_id |= self.attendee_id
    return {}
