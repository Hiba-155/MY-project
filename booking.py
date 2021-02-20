from odoo import fields, models


class Booking(models.Model):
    _name = "flight.booking"

    time = fields.Datetime()
    customer = fields.Many2one("flight.customer")
    employee = fields.Many2one("hr.employee")

    customers = fields.Many2many("flight.customer")
