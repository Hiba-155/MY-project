from odoo import fields, models


class EmployeeInheritance(models.Model):
    _inherit = "hr.employee"

    code = fields.Integer()

    bookings = fields.One2many("flight.booking", "employee")
