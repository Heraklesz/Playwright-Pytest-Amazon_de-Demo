"""
This check verifies that the cart icon is visible in the site header.
It ensures that users can always access their cart from the global navigation.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.components.header import Header


@pytest.mark.checks
def test_header_cart_icon_is_visible(page):
    home_page = HomePage(page)
    header = Header(page)

    home_page.load(config.base_url)
    header.expect_cart_icon_visible()
