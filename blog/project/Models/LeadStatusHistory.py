from django.db import models
from django.contrib.auth.models import User
from project.Models.LeadForm import *
from project.Models.Lead import *
# Import your Lead model

class LeadStatusHistory(models.Model):

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="history"
    )

    old_status = models.CharField(max_length=30)

    new_status = models.CharField(max_length=30)

    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead.name}: {self.old_status} → {self.new_status}"