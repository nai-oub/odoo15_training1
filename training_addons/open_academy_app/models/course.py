# -*- coding: utf-8 -*-


from odoo import fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Course(models.Model):
    _name = 'course'
    _description = "Course Model"
    title = fields.Char(string='title', required=True)
    description = fields.Text(string='description')
    # ondelete what to do when the referred record is deleted
    # a course has a respo
    responsible_id = fields.Many2one('res.users', string="Responsible", ondelete='set null', index=True)
    # inverse many2one reflect the relation between courses and sessions
    # course_id make the relationship
    session_id = fields.One2many('session', 'course_id', string="Sessions")

    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('title', '=like', u"Copy of {}%".format(self.title))])
        if not copied_count:
            new_title = u"Copy of {}".format(self.title)
        else:
            new_title = u"Copy of {} ({})".format(self.title, copied_count)

        default['title'] = new_title
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('title_description_check',
         'CHECK(title!=description)',
         "The title of the course should not be the description"),

        ('title_unique',
         'UNIQUE(title)',
         "The course title must be unique"),
    ]
