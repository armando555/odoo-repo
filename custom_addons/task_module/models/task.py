from oddo import models,fields

class Task(models.Model):
    _name = "task.Task"

    name = fields.Many2one("res.partner", string="Task")
    task_type = fields.Integer(string="TaskType")
    description = fields.Char(string="Description")