

# Create your models here.
from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    source = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name