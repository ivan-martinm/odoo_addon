# -*- coding: utf-8 -*-
# from odoo import http


# class Practicas(http.Controller):
#     @http.route('/practicas/practicas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practicas/practicas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('practicas.listing', {
#             'root': '/practicas/practicas',
#             'objects': http.request.env['practicas.practicas'].search([]),
#         })

#     @http.route('/practicas/practicas/objects/<model("practicas.practicas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practicas.object', {
#             'object': obj
#         })
