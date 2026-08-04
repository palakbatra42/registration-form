from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path(
        "",include(("project.Routes.Register", "Register"), namespace="Register"),
    ),
    
    path(
        "lead/",include(("project.Routes.Lead", "Lead"), namespace="Lead"),
    ),
    path(
        "api/",include(("project.Routes.Api", "Api"), namespace="Api"),
    ),
    path("admin/", admin.site.urls),
]