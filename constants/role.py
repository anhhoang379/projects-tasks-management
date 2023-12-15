from django.utils.translation import gettext_lazy as _


class Role:
    MANAGER = "Manage"
    EMPLOYEE = "Employee"

    CHOICES = (
        (MANAGER, _(MANAGER)),
        (EMPLOYEE, _(EMPLOYEE)),
    )
