from django.contrib import admin

from management.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "role",
    ]

    list_select_related = ["user"]
