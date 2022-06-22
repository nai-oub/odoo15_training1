# -*- coding: utf-8 -*-
from dateutil.utils import today

from odoo import fields, models, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta


class Session(models.Model):
    _name = 'session'
    _description = "Session Model"
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    # computed field
    end_date = fields.Date(string="End Date", store=True,
                           compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(string='Duration', digits=(6, 2), help="Duration in days")
    number_seats = fields.Integer(string='Number of seats')
    # a session has an instructor
    instructor_id = fields.Many2one('res.partner', string="Instructor",
                                    damain=[('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
    # a session is related to a course
    # ondelete=cascade allows to delete data from child tables automatically
    # when deleting data from parent
    course_id = fields.Many2one('course', string="Course", ondelete='cascade', required=True)
    # course_id is the inverse Many2one field(key in linking the relation betwen records
    # session is related to a set of attendees(participants)
    attendee_id = fields.Many2many('res.partner', string="Attendees")
    # computed field(not stored in db)
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    attendees_count = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)
    color = fields.Integer()

    # Calculate the % of taken seats
    # number_seats and attendee_id are fields used
    @api.depends('number_seats', 'attendee_id')
    def _taken_seats(self):
        for r in self:
            if not r.number_seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_id) / r.number_seats

    # Warning
    @api.onchange('number_seats', 'attendee_id')
    def _verify_valid_seats(self):
        if self.number_seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "number of seats is negative",
                },
            }

        if self.number_seats < len(self.attendee_id):
            return {
                'warning': {
                    'title': "more participants than seats",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_id')
    def _check_instructor_presence(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_id:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('attendee_id')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_id)
