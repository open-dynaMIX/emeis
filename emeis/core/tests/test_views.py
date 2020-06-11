from uuid import uuid4

import pytest
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
)


def test_me_200(db, acl, client):
    client.force_authenticate(user=acl.user)
    url = reverse("me-detail")

    response = client.get(url, data={"include": "acls"})

    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["included"]) == 1
    assert (
        result["data"]["id"]
        == result["included"][0]["relationships"]["user"]["data"]["id"]
        == str(acl.user.pk)
    )
    assert result["included"][0]["id"] == str(acl.pk)


@pytest.mark.parametrize(
    "method,status_code",
    [
        ("post", HTTP_405_METHOD_NOT_ALLOWED),
        ("patch", HTTP_405_METHOD_NOT_ALLOWED),
        ("put", HTTP_405_METHOD_NOT_ALLOWED),
        ("head", HTTP_200_OK),
        ("options", HTTP_200_OK),
    ],
)
def test_me_405(db, acl, client, method, status_code):
    client.force_authenticate(user=acl.user)
    url = reverse("me-detail")

    response = getattr(client, method)(url)

    assert response.status_code == status_code


@pytest.mark.parametrize("list", [True, False])
def test_myacls_200(db, acl_factory, client, list):
    acl = acl_factory(role__slug="my-role")
    acl_factory()
    client.force_authenticate(user=acl.user)
    url = reverse("myacls-list")
    if not list:
        url = reverse("myacls-detail", args=[acl.pk])

    response = client.get(url, data={"include": "role"})

    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["included"]) == 1
    if list:
        assert result["data"][0]["id"] == str(acl.pk)
        assert len(result["data"]) == 1
    else:
        assert result["data"]["id"] == str(acl.pk)


def test_myacls_404(db, user, client):
    client.force_authenticate(user=user)
    url = reverse("myacls-detail", args=[str(uuid4())])

    response = client.get(url)

    assert response.status_code == HTTP_404_NOT_FOUND


def test_myacls_403(db, acl_factory, user, client):
    acl = acl_factory()
    client.force_authenticate(user=user)
    url = reverse("myacls-detail", args=[str(acl.pk)])

    response = client.get(url)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_user_search_filter(db, user_factory, client):
    user_factory(username="user1", city="Lucerne", zip="6000", last_name="Kafka")
    user_factory(username="user2", city="Berne", zip="5000", last_name="Smith")
    user_factory(username="user3", city="Zurich", zip="8000", last_name="Smith")

    url = reverse("user-list")

    response = client.get(url, {"filter[search]": "bern"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 1
    assert result["data"][0]["attributes"]["username"] == "user2"

    response = client.get(url, {"filter[search]": "8000"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 1
    assert result["data"][0]["attributes"]["username"] == "user3"

    response = client.get(url, {"filter[search]": "smith"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 2
    assert "user1" not in (
        result["data"][0]["attributes"]["username"],
        result["data"][1]["attributes"]["username"],
    )


def test_scope_search_filter(db, scope_factory, client):
    scope_factory(name="scope1")
    scope_factory(name={"de": "skop2", "en": "scope2"})
    scope_factory(name="scope3")

    url = reverse("scope-list")

    response = client.get(url, {"filter[search]": "skop"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 1
    assert result["data"][0]["attributes"]["name"] == {
        "de": "skop2",
        "en": "scope2",
        "fr": "",
    }

    response = client.get(url, {"filter[search]": "scope"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 3


def test_acl_search_filter(db, acl_factory, client):
    acl = acl_factory(role__name="scope1", scope__name="scope1", user__username="user1")
    acl_factory(role__name="scope1", scope__name="scope2", user=acl.user)
    acl_factory(role__name="scope1", scope=acl.scope, user__username="user2")

    url = reverse("acl-list")

    response = client.get(url, {"filter[search]": "user1"})
    assert response.status_code == HTTP_200_OK
    result = response.json()
    assert len(result["data"]) == 2
    assert (
        result["data"][0]["relationships"]["user"]["data"]["id"]
        == result["data"][1]["relationships"]["user"]["data"]["id"]
        == str(acl.user.pk)
    )
