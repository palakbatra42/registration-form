from django.db import models
from django.contrib.auth.models import User

from project.Controller.Notification import Send_email, Update_email
class Lead(models.Model):

    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Qualified", "Qualified"),
        ("Proposal Sent", "Proposal Sent"),
        ("Won", "Won"),
        ("Lost", "Lost"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=True, null=True)
    phone = models.BigIntegerField(max_length=10,blank=True, null=True)
    source = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="New")
    notes = models.TextField(blank=True)
    ROLE_CHOICES = [ ("Admin", "Admin"), ("User", "User"), ] 
    created_at = models.DateField(auto_now_add=True)

    ASSIGNED_CHOICES = [
        ("Admin", "Admin"),
        ("User", "User"),
    ]

    assigned_user = models.CharField(
        max_length=20,
        choices=ASSIGNED_CHOICES,
        default="User"
    )

    
    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:
            Send_email(self)   # New lead mail
        else:
            Update_email(self)  # Update mail

    def __str__(self):
        return self.name

