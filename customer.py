from odoo import fields, models


class Customer(models.Model):
    _name = "flight.customer"

    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])

    bookings = fields.Many2many("flight.booking")
