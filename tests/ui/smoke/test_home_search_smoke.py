"""
This smoke test verifies that a user can successfully search for a product
from the Amazon home page.
It validates basic page loading, cookie handling, and navigation to
the search results page.
This test represents a critical user flow and serves as a baseline UI smoke check.
"""
import pytest

from src.core.config import config
from src.pages.home_page import HomePage


@pytest.mark.smoke
def test_user_can_search_from_home_page(page):
    """
    Verifies that searching from the home page navigates to a results page.
    """
    home_page = HomePage(page)

    home_page.load(config.base_url)
    home_page.search_for("wireless headphones")

    page.wait_for_load_state("networkidle")
    assert "s?k=wireless+headphones" in page.url
