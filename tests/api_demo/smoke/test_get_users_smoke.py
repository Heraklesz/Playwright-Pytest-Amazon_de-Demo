"""
This API smoke test verifies that the users endpoint
returns a successful response.
It serves as a basic health check for the demo API.
"""

import pytest

from src.api_demo.client import DemoApiClient
from src.api_demo.endpoints import USERS


@pytest.mark.api_demo
@pytest.mark.api_smoke
def test_get_users_returns_200():
    client = DemoApiClient("https://reqres.in")

    response = client.get(USERS)

    assert response.status_code == 200
