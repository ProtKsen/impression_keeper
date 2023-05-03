import pytest
from django.urls import reverse


def test_user_profile_page_unauthorized_user_redirect(client):
    url = reverse("user_profile")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_profile_page_authorized_user_successed(client, create_user):
    url = reverse("user_profile")
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url)
    assert response.status_code == 200
