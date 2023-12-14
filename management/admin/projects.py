from django.contrib import admin

from management.models import Project


@admin.register(Project)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "managers",
    ]
