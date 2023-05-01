import pytest
from django.urls import reverse


def test_login_unauthorized_user_successed(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_authorized_user_redirect(client, create_user):
    url = reverse("login")
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url)
    assert response.status_code == 302
