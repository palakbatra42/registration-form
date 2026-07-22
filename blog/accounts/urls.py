from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('add/', views.add_lead, name='add_lead'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage ,name='logout'),
    path('', views.loginPage, name='root'),

    ]