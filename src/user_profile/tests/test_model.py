import pytest
from django.contrib.auth.models import User

from user_profile.models import Place
from user_profile.tests.factories import PlaceFactory


@pytest.mark.django_db
def test_place_model_types_of_fields(create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    assert isinstance(place.user, User)
    assert isinstance(place.name, str)
    assert isinstance(place.comment, str)
    assert isinstance(place.longitude, float)
    assert isinstance(place.latitude, float)


@pytest.mark.django_db
@pytest.mark.parametrize("n", [5])
def test_place_model_user_relation(create_user, n):
    user = User.objects.get(username="TestUser")
    for _ in range(n):
        place = PlaceFactory(user=user)
        place.save()
    all_places = Place.objects.filter(user=user)
    assert len(all_places) == n
    for place in Place.objects.all():
        assert place.user == user


@pytest.mark.django_db
def test_place_model_string_representation_is_name(create_user):
    user = User.objects.get(username="TestUser")
    place = PlaceFactory(user=user)
    place.save()
    assert str(place) == place.name
