# from odoo import http


# class Greet(http.Controller):
#     @http.route('/greet/greet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/greet/greet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('greet.listing', {
#             'root': '/greet/greet',
#             'objects': http.request.env['greet.greet'].search([]),
#         })

#     @http.route('/greet/greet/objects/<model("greet.greet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('greet.object', {
#             'object': obj
#         })
