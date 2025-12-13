"""
This smoke test verifies that triggering a product search
results in successful backend network calls.
It validates that core search-related API requests return
successful HTTP responses.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage


@pytest.mark.amazon_network
@pytest.mark.smoke
def test_search_triggers_successful_network_calls(page):
    network_responses = []

    def capture_response(response):
        if "amazon" in response.url and response.request.method == "GET":
            network_responses.append(response)

    page.on("response", capture_response)

    home_page = HomePage(page)
    home_page.load(config.base_url)
    home_page.search_for("external ssd")

    page.wait_for_load_state("networkidle")

    assert network_responses, "No network responses captured during search"

    for response in network_responses:
        assert response.status < 500, f"Server error detected: {response.url}"
