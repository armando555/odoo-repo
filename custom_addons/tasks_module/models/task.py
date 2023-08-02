from oddo import models,fields

class Task(models.Model):
    _name = "task.tarea"

    name = fields.Many2one("res.partner", string="Student")
    task_type = fields.Integer(string="TaskType")
    description = fields.Char(string="Description")