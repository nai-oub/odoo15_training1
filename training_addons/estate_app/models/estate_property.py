# -*- coding: utf-8 -*-

import logging
import threading
from datetime import date, datetime, timedelta
from psycopg2 import sql
from odoo.addons.phone_validation.tools import phone_validation
from collections import OrderedDict, defaultdict
from dateutil.utils import today

from odoo import fields, models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate property Models"

    active = fields.Boolean()
    id = fields.Integer(string='ID', required=True)
    bedrooms = fields.Integer(string='Bedroom', default="2")
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_availability = fields.Date(string='Available date ', required=True, copy=False,
                                    default=today() + relativedelta(months=3))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', required=True, attrs="{ 'readonly' : True}", copy=False)
    garden_orientation = fields.Selection([('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')],
                                          String="orientation")
    state = fields.Selection(
        [('N', 'New'), ('O', 'Offer Received'), ('OA', 'Offer Accepted'), ('SC', 'Sold and Cancled')],
        string='State')

    postcode = fields.Char(string='Postcode')
    living_area = fields.Integer(string='Living area')
    facades = fields.Integer(string='facades')
    garden_area = fields.Integer(string='Garden Area')
    garden = fields.Boolean(string='Garden')
    garage = fields.Boolean(string='Garage')
    property_type_id = fields.Many2one('res.partner', string="Property type id ")
    buyer_id = fields.Many2one('res.users', string="Buyer", copy=False, index=True)
    salesperson_id = fields.Many2one('res.partner', string="Salesperson")
    total_area = fields.Integer(string="total area ", compute="_total_area")
    best_price = fields.Float(string="total area ", compute="_best_price")

    @api.depends('living_area', 'garden_area')
    def _total_area(self):
        for r in self:
            r.total_area = r.living_area + r.garden_area


@api.depends('selling_price')
def _best_price(self):
    for r in self:
        r.best_price = max(r.selling_price)
