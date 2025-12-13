"""
This API regression test verifies the structure of the users response.
It ensures that returned user objects conform to the expected schema.
"""

import pytest

from src.api_demo.client import DemoApiClient
from src.api_demo.endpoints import USERS
from src.api_demo.models import User


@pytest.mark.api_demo
@pytest.mark.api_regression
def test_users_response_schema():
    client = DemoApiClient("https://reqres.in")

    response = client.get(USERS)
    data = response.json()["data"]

    users = [User(**user) for user in data]

    assert users, "No users returned from API"
