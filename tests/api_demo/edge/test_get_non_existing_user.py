"""
This API edge test verifies system behavior
when requesting a non-existing user.
It validates proper handling of not-found scenarios.
"""

import pytest

from src.api_demo.client import DemoApiClient


@pytest.mark.api_demo
@pytest.mark.api_edge
def test_get_non_existing_user_returns_404():
    client = DemoApiClient("https://reqres.in")

    response = client.get("api/users/9999")

    assert response.status_code == 404
