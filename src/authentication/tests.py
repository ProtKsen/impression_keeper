import pytest
from django.contrib import auth
from django.urls import reverse


def test_login_page_unauthorized_user_successed(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_page_authorized_user_redirect(client, create_user):
    url = reverse("login")
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_authorized_user_successed(client, create_user):
    url = reverse("logout")
    client.login(username="TestUser", password="TestPassword")
    client.get(url)
    user = auth.get_user(client)
    assert user.is_anonymous is True


@pytest.mark.django_db
def test_logout_authorized_user_redirect(client, create_user):
    url = reverse("logout")
    client.login(username="TestUser", password="TestPassword")
    response = client.get(url)
    assert response.status_code == 302


def test_logout_page_unauthorized_user_redirect(client):
    url = reverse("logout")
    response = client.get(url)
    assert response.status_code == 302
