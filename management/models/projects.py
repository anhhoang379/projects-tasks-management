from django.contrib.auth.models import User
from django.db import models

from management.managers import ProjectManager


class Project(models.Model):
    objects = ProjectManager()

    name = models.CharField(max_length=255)
    description = models.TextField()
    managers = models.ManyToManyField(User, related_name="managed_projects")

    def __str__(self):
        return self.name
