from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
