# -*- coding: utf-8 -*-
# from odoo import http


# class ElearningSubscription(http.Controller):
#     @http.route('/elearning_subscription/elearning_subscription', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elearning_subscription/elearning_subscription/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('elearning_subscription.listing', {
#             'root': '/elearning_subscription/elearning_subscription',
#             'objects': http.request.env['elearning_subscription.elearning_subscription'].search([]),
#         })

#     @http.route('/elearning_subscription/elearning_subscription/objects/<model("elearning_subscription.elearning_subscription"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elearning_subscription.object', {
#             'object': obj
#         })

