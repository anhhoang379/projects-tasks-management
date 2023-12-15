from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

import constants


class TaskPermissions(permissions.BasePermission):
    message = _("Deleting not allowed.")

    def has_object_permission(self, request, view, obj):
        if (
            request.method == "DELETE"
            and request.user.staff.role == constants.Role.EMPLOYEE
        ):

            return False

        return True
