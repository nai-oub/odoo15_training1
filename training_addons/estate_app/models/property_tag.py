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


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = "Estate property Tag Model"

    name = fields.Char(string='Name', required=True)

    active = fields.Boolean()
    description = fields.Text(string='Description')