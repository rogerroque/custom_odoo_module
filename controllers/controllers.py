# -*- coding: utf-8 -*-
# from odoo import http


# class LolEsports(http.Controller):
#     @http.route('/lol_esports/lol_esports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lol_esports/lol_esports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lol_esports.listing', {
#             'root': '/lol_esports/lol_esports',
#             'objects': http.request.env['lol_esports.lol_esports'].search([]),
#         })

#     @http.route('/lol_esports/lol_esports/objects/<model("lol_esports.lol_esports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lol_esports.object', {
#             'object': obj
#         })
