"""
This check verifies that the search bar is always visible in the site header.
The search bar is a critical global UI element required for most user flows.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.components.header import Header


@pytest.mark.checks
def test_header_search_bar_is_visible(page):
    home_page = HomePage(page)
    header = Header(page)

    home_page.load(config.base_url)
    header.expect_search_bar_visible()
