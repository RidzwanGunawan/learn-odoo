# -*- coding: utf-8 -*-
# from odoo import http


# class EventPublisher(http.Controller):
#     @http.route('/event_publisher/event_publisher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_publisher/event_publisher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_publisher.listing', {
#             'root': '/event_publisher/event_publisher',
#             'objects': http.request.env['event_publisher.event_publisher'].search([]),
#         })

#     @http.route('/event_publisher/event_publisher/objects/<model("event_publisher.event_publisher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_publisher.object', {
#             'object': obj
#         })

