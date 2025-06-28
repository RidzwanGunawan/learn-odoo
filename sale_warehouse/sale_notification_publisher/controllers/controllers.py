# -*- coding: utf-8 -*-
# from odoo import http


# class SaleNotificationPublisher(http.Controller):
#     @http.route('/sale_notification_publisher/sale_notification_publisher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_notification_publisher/sale_notification_publisher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_notification_publisher.listing', {
#             'root': '/sale_notification_publisher/sale_notification_publisher',
#             'objects': http.request.env['sale_notification_publisher.sale_notification_publisher'].search([]),
#         })

#     @http.route('/sale_notification_publisher/sale_notification_publisher/objects/<model("sale_notification_publisher.sale_notification_publisher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_notification_publisher.object', {
#             'object': obj
#         })

