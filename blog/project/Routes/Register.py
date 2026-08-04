from django.urls import path
from project.Controller import Register

app_name = "Register"
urlpatterns = [
    path('signup/', Register.SignupPage, name='Signup'),
    path('login/', Register.LoginPage, name='Login'),
    path('logout/', Register.LogoutPage, name='Logout'),
    path('', Register.LoginPage, name='root'),
]