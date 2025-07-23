# -*- coding: utf-8 -*-
# from odoo import http


# class RentalCommunity(http.Controller):
#     @http.route('/rental_community/rental_community', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rental_community/rental_community/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rental_community.listing', {
#             'root': '/rental_community/rental_community',
#             'objects': http.request.env['rental_community.rental_community'].search([]),
#         })

#     @http.route('/rental_community/rental_community/objects/<model("rental_community.rental_community"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rental_community.object', {
#             'object': obj
#         })

