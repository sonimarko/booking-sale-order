from odoo import api, models, api, exceptions, fields, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	ns_is_booking_order = fields.Boolean(string='Is Booking Order?')