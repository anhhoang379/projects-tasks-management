from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

import constants


class ProjectPermissions(permissions.BasePermission):
    message = _("Staff Permission not allowed.")

    def has_permission(self, request, view):
        if (
            request.user.staff.role == constants.Role.EMPLOYEE
            and request.method == "POST"
        ):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if (
            request.user.staff.role == constants.Role.EMPLOYEE
            and request.method not in permissions.SAFE_METHODS
        ):
            return False

        return True
