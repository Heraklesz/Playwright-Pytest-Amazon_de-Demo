"""
This edge test verifies system behavior when an empty search
is submitted by the user.
It ensures the application responds gracefully without errors.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage


@pytest.mark.edge
def test_search_with_empty_input(page):
    home_page = HomePage(page)

    home_page.load(config.base_url)
    home_page.search_for("")

    page.wait_for_load_state("networkidle")
    assert "amazon" in page.url.lower()
