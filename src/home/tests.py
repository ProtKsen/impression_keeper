from django.urls import reverse


def test_home_page_successed(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
