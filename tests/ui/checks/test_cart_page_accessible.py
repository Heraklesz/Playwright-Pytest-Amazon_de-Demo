"""
This check verifies that the cart page is accessible
and properly renders its main container.
It serves as a basic cart domain health check.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage


@pytest.mark.checks
def test_cart_page_is_accessible(page):
    cart_page = CartPage(page)

    page.goto(f"{config.base_url}/gp/cart/view.html")
    cart_page.wait_until_loaded()
