from django.conf import settings
from django.db import models

import constants
from management.managers import StaffManager


class Staff(models.Model):
    objects = StaffManager()

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="staff",
        on_delete=models.PROTECT,
    )
    role = models.CharField(
        max_length=100,
        choices=constants.Role.CHOICES,
        default=constants.Role.EMPLOYEE,
    )

    @property
    def username(self):
        return self.user.username
