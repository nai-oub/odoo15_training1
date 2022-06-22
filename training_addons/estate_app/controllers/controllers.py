# -*- coding: utf-8 -*-
# from odoo import http


# class EstateApp(http.Controller):
#     @http.route('/estate_app/estate_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate_app/estate_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate_app.listing', {
#             'root': '/estate_app/estate_app',
#             'objects': http.request.env['estate_app.estate_app'].search([]),
#         })

#     @http.route('/estate_app/estate_app/objects/<model("estate_app.estate_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate_app.object', {
#             'object': obj
#         })
