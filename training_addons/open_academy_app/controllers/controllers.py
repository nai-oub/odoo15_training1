# -*- coding: utf-8 -*-
# from odoo import http


# class OpenAcademyApp(http.Controller):
#     @http.route('/open_academy_app/open_academy_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_academy_app/open_academy_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_academy_app.listing', {
#             'root': '/open_academy_app/open_academy_app',
#             'objects': http.request.env['open_academy_app.open_academy_app'].search([]),
#         })

#     @http.route('/open_academy_app/open_academy_app/objects/<model("open_academy_app.open_academy_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_academy_app.object', {
#             'object': obj
#         })
