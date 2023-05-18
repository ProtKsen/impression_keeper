import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from user_profile.models import Place
from user_profile.tests.factories import PlaceFactory

"""
Tests for user_profile
"""


def test_profile_get_request_from_unauthorized_user_redirect(client):
    url = reverse("user_profile")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")


@pytest.mark.django_db
def test_profile_get_request_from_authorized_user_successed(client, create_user, login_user):
    url = reverse("user_profile")
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "user_profile.html")


"""
Tests for add_place
"""


def test_add_place_get_request_from_unauthorized_user_redirect(client):
    url = reverse("add_place")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")


@pytest.mark.django_db
def test_add_place_get_request_from_authorized_user_successed(client, create_user, login_user):
    url = reverse("add_place")
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "edit_place.html")


@pytest.mark.django_db
def test_add_place_get_request_send_empty_place_form(client, create_user, login_user):
    url = reverse("add_place")
    response = client.get(url)
    assert response.context["form"]["name"].value() is None
    assert response.context["form"]["comment"].value() is None
    assert response.context["form"]["latitude"].value() is None
    assert response.context["form"]["longitude"].value() is None


@pytest.mark.parametrize("n", [0, 5])
@pytest.mark.django_db
def test_add_place_post_request_adds_new_place_successed(client, create_user, login_user, n):
    url = reverse("add_place")
    user = User.objects.get(username="TestUser")
    for _ in range(n):
        place = PlaceFactory(user=user)
        place.save()
    form_data = {
        "name": "Test name",
        "comment": "Test comment",
        "latitude": 55.5,
        "longitude": 60.0,
    }
    response = client.post(url, data=form_data, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "user_profile.html")
    assert len(Place.objects.all()) == n + 1


@pytest.mark.django_db
def test_add_place_post_request_not_valid_form_redirect(client, create_user, login_user):
    url = reverse("add_place")
    form_data = {"comment": "Test comment", "latitude": 55.5, "longitude": 60.0}
    response = client.post(url, data=form_data, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "edit_place.html")


"""
Tests for edit_place
"""


@pytest.mark.django_db
def test_edit_place_page_request_from_unauthorized_user_redirect(client, create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    url = reverse("edit_place", args=[place.id])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")


@pytest.mark.django_db
def test_edit_place_get_request_from_authorized_user_successed(client, create_user, login_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    url = reverse("edit_place", args=[place.id])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "edit_place.html")


@pytest.mark.django_db
def test_edit_place_get_request_from_authorized_user_permission_denied_redirect(
    client, create_user, login_user
):
    user2 = User.objects.create_user(username="TestUser2", password="TestPassword")
    place = PlaceFactory(user=user2)
    place.save()
    url = reverse("edit_place", args=[place.id])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_edit_place_get_request_from_authorized_user_not_existed_place_redirect(
    client, create_user, login_user
):
    url = reverse("edit_place", args=[100])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_edit_place_post_request_edits_place_successed(client, create_user, login_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    form_data = {"name": "new_name", "comment": "new_comment", "latitude": 10.0, "longitude": 10.0}
    url = reverse("edit_place", args=[place.id])
    response = client.post(url, data=form_data, follow=True)
    place = Place.objects.get(id=place.id)
    assert response.status_code == 200
    assert place.name == "new_name"
    assert place.comment == "new_comment"
    assert place.latitude == 10.0
    assert place.longitude == 10.0


@pytest.mark.django_db
def test_edit_place_get_request_send_form_with_initial_data(client, create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    url = reverse("edit_place", args=[place.id])
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url)
    assert response.context["form"]["name"].value() == place.name
    assert response.context["form"]["comment"].value() == place.comment
    assert response.context["form"]["latitude"].value() == place.latitude
    assert response.context["form"]["longitude"].value() == place.longitude


"""
Tests for delete_place
"""


@pytest.mark.django_db
def test_delete_place_get_request_from_unauthorized_user_redirect(client, create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    url = reverse("delete_place", args=[place.id])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")


@pytest.mark.django_db
def test_delete_place_get_request_from_authorized_user_successed(client, create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    url = reverse("delete_place", args=[place.id])
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "user_profile.html")
    assertTemplateUsed(response, "layouts.html")


@pytest.mark.django_db
def test_delete_place_get_request_from_authorized_user_permission_denied_redirect(
    client, create_user, login_user
):
    user2 = User.objects.create_user(username="TestUser2", password="TestPassword")
    place = PlaceFactory(user=user2)
    place.save()
    url = reverse("delete_place", args=[place.id])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_delete_place_get_request_from_authorized_user_not_existed_place_redirect(
    client, create_user, login_user
):
    url = reverse("delete_place", args=[100])
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


@pytest.mark.parametrize("n", [5])
@pytest.mark.django_db
def test_delete_place_successed(client, create_user, login_user, n):
    user = User.objects.get(username="TestUser")
    for _ in range(n):
        place = PlaceFactory(user=user)
        place.save()
    url = reverse("delete_place", args=[place.id])
    client.get(url)
    assert len(Place.objects.all()) == n - 1
