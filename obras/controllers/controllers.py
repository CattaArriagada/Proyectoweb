# -*- coding: utf-8 -*-
from odoo import http

# class Obras(http.Controller):
#     @http.route('/obras/obras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/obras/obras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('obras.listing', {
#             'root': '/obras/obras',
#             'objects': http.request.env['obras.obras'].search([]),
#         })

#     @http.route('/obras/obras/objects/<model("obras.obras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('obras.object', {
#             'object': obj
#         })