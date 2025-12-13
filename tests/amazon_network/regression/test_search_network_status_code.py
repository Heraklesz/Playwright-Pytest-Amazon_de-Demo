"""
This regression test validates that search-related backend requests
return successful HTTP status codes.
It focuses on detecting backend regressions that may not immediately
surface as UI failures.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage


@pytest.mark.amazon_network
@pytest.mark.regression
def test_search_backend_requests_return_success(page):
    search_responses = []

    def capture_response(response):
        if "s?k=" in response.url:
            search_responses.append(response)

    page.on("response", capture_response)

    home_page = HomePage(page)
    home_page.load(config.base_url)
    home_page.search_for("mechanical keyboard")

    page.wait_for_load_state("networkidle")

    assert search_responses, "No search-related backend responses captured"

    for response in search_responses:
        assert response.status == 200, (
            f"Unexpected status code {response.status} for {response.url}"
        )
