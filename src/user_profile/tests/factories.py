import random

import factory
from factory.django import DjangoModelFactory

from user_profile.models import Place


class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place

    name = factory.Faker("name")
    comment = factory.Faker("sentence")
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
