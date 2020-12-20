# -*- coding: utf-8 -*-
from odoo import http

# class AvanceFisico(http.Controller):
#     @http.route('/avance_fisico/avance_fisico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/avance_fisico/avance_fisico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('avance_fisico.listing', {
#             'root': '/avance_fisico/avance_fisico',
#             'objects': http.request.env['avance_fisico.avance_fisico'].search([]),
#         })

#     @http.route('/avance_fisico/avance_fisico/objects/<model("avance_fisico.avance_fisico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('avance_fisico.object', {
#             'object': obj
#         })