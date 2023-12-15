from django.contrib import admin

from management.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "project",
        "name",
        "description",
        "assigned_to",
        "status",
    ]

    list_select_related = ["project"]
