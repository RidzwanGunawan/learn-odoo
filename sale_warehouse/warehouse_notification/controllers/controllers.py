# -*- coding: utf-8 -*-
# from odoo import http


# class WarehouseNotification(http.Controller):
#     @http.route('/warehouse_notification/warehouse_notification', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warehouse_notification/warehouse_notification/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('warehouse_notification.listing', {
#             'root': '/warehouse_notification/warehouse_notification',
#             'objects': http.request.env['warehouse_notification.warehouse_notification'].search([]),
#         })

#     @http.route('/warehouse_notification/warehouse_notification/objects/<model("warehouse_notification.warehouse_notification"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warehouse_notification.object', {
#             'object': obj
#         })

