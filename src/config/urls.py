"""config URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("authenticate/", include("authentication.urls")),
    path("accounts/", include("allauth.urls")),
    path("userprofile/", include("user_profile.urls")),
]
