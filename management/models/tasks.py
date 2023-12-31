from django.contrib.auth.models import User
from django.db import models

import constants
from management.managers import TaskManager


class Task(models.Model):
    objects = TaskManager()

    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="tasks"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_tasks"
    )
    status = models.CharField(
        max_length=20,
        choices=constants.TaskStatus.CHOICES,
        default=constants.TaskStatus.NOT_STARTED,
    )

    def __str__(self):
        return "{} - {}".format(self.project, self.name)
