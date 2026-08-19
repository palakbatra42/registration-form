from django.urls import path
from project.Controller.Api import Api
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path("list/", Api.Lead_list, name="List"),
    path("list/add/", Api.Add_list, name="Add"),
    path("list/update/<int:pk>/", Api.Update_list, name="Update"),
    path("list/delete/<int:pk>/", Api.Delete_list, name="Delete"),
    path("token/", TokenObtainPairView.as_view(),name="Token"),
    path("refresh/", TokenRefreshView.as_view(),name="Refresh"),
    path("pick/", Api.Pick_action, name="Pick"),
]