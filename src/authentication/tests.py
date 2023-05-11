import pytest
from django.contrib import auth
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_login_get_request_from_unauthorized_user_successed(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")


@pytest.mark.django_db
def test_login_get_request_from_authorized_user_redirect(client, create_user, login_user):
    url = reverse("login")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


@pytest.mark.django_db
def test_logout_get_request_from_authorized_user_successed(client, create_user, login_user):
    url = reverse("logout")
    client.get(url)
    user = auth.get_user(client)
    assert user.is_anonymous is True


@pytest.mark.django_db
def test_logout_get_request_from_authorized_user_redirect_after_logout(
    client, create_user, login_user
):
    url = reverse("logout")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


def test_logout_get_request_from_unauthorized_user_redirect(client):
    url = reverse("logout")
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, "login.html")
