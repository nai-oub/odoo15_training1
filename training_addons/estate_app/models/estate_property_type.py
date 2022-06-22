from dateutil.utils import today

from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property.type"
    _description = "Estate property Type Model"

    name = fields.Char(string='Name', required=True)

    active = fields.Boolean()
    description = fields.Text(string='Description')






