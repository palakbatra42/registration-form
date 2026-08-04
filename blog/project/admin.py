

# Register your models here.
print("PROJECT ADMIN LOADED")

from django.contrib import admin
from project.Models.Lead import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "source",
        "status",
        "assigned_user",
        "created_at",
    )