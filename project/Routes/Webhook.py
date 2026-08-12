from django.urls import path
from project.Controller import Webhook

urlpatterns = [
    path("webhook/", Webhook.Webhook, name="Webhook"),
]