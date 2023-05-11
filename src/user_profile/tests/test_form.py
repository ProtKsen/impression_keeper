import pytest
from django.contrib.auth.models import User

from user_profile.forms import PlaceForm


@pytest.mark.django_db
def test_place_form_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {
        "user": user,
        "name": "Test name",
        "comment": "Test comment",
        "longitude": 55.5,
        "latitude": 60.1,
    }
    form = PlaceForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_place_form_with_empty_name_not_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {"user": user, "comment": "Test comment", "longitude": 55.5, "latitude": 60.1}
    form = PlaceForm(data=form_data)
    assert form.is_valid() is False


@pytest.mark.django_db
def test_place_form_with_empty_latitude_not_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {
        "user": user,
        "name": "Test name",
        "comment": "Test comment",
        "longitude": 55.5,
    }
    form = PlaceForm(data=form_data)
    assert form.is_valid() is False


@pytest.mark.django_db
def test_place_form_with_empty_longitude_not_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {
        "user": user,
        "name": "Test name",
        "comment": "Test comment",
        "latitude": 55.5,
    }
    form = PlaceForm(data=form_data)
    assert form.is_valid() is False


@pytest.mark.django_db
def test_place_form_with_empty_comment_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {"user": user, "name": "Test name", "longitude": 55.5, "latitude": 60.1}
    form = PlaceForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_place_form_with_not_correct_longitude_not_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {
        "user": user,
        "name": "Test name",
        "comment": "Test comment",
        "longitude": "abcd",
        "latitude": 60.1,
    }
    form = PlaceForm(data=form_data)
    assert form.is_valid() is False


@pytest.mark.django_db
def test_place_form_with_not_correct_latitude_not_valid(create_user):
    user = User.objects.get(username="TestUser")
    form_data = {
        "user": user,
        "name": "Test name",
        "comment": "Test comment",
        "longitude": 55.51,
        "latitude": "abc",
    }
    form = PlaceForm(data=form_data)
    assert form.is_valid() is False
