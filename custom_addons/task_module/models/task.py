from odoo import models,fields

class Task(models.Model):
    _name = "task.task"

    name = fields.Char(required=True, string="name")
    task_type = fields.Selection([("general","General"),("particular","Particular")])
    description = fields.Text(string="Description")