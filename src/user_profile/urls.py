from django.urls import path

from user_profile import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("place/add", views.add_place, name="add_place"),
]
