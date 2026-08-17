
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "",
        include(("project.Routes.Register", "Register"), namespace="Register"),
    ),

    path(
        "lead/",
        include(("project.Routes.Lead", "Lead"), namespace="Lead"),
    ),

    path(
        "api/",
        include(("project.Routes.Api", "Api"), namespace="Api"),
    ),

    path("admin/", admin.site.urls),

    path(
        "Credentials/",
        include(("project.Routes.Sync", "Credentials"), namespace="Credentials")
    ),

    path(
        "webhook/",
        include(("project.Routes.Webhook", "Webhook"), namespace="Webhook")
    ),
]