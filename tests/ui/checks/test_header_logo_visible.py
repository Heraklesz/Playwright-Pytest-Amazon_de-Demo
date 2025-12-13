"""
This check verifies that the Amazon logo is visible in the site header.
It serves as a basic UI health indicator and branding verification.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.components.header import Header


@pytest.mark.checks
def test_header_logo_is_visible(page):
    home_page = HomePage(page)
    header = Header(page)

    home_page.load(config.base_url)
    header.expect_logo_visible()
