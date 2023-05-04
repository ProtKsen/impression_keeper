from django.urls import path

from user_profile import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("place/add", views.add_place, name="add_place"),
    path("place/edit/<int:id>/", views.edit_place, name="edit_place"),
    path("place/delete/<int:id>/", views.delete_place, name="delete_place"),
]
