from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "leads"

urlpatterns = [
    path('add/', views.add_lead, name='add_lead'),
    path("update/<int:id>/", views.update_lead, name="update_lead"),
    path("delete/<int:id>/", views.delete_lead, name="delete_lead"),
]