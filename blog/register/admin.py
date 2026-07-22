

from django.contrib import admin
from leads.models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'source', 'status', 'notes')

admin.site.register(Lead, LeadAdmin)