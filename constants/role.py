from django.utils.translation import gettext_lazy as _


class Role:
    MANAGER = "Manager"
    EMPLOYEE = "Employee"

    CHOICES = (
        (MANAGER, _(MANAGER)),
        (EMPLOYEE, _(EMPLOYEE)),
    )
