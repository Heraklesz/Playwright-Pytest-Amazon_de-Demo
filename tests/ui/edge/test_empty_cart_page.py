"""
This edge test verifies that opening the cart page directly
without any items results in a proper empty cart state.
It validates graceful handling of an empty shopping cart.
"""

import pytest

from src.core.config import config
from src.pages.cart_page import CartPage


@pytest.mark.edge
def test_empty_cart_page_is_displayed(page):
    cart_page = CartPage(page)

    page.goto(f"{config.base_url}/gp/cart/view.html")
    cart_page.wait_until_loaded()
    cart_page.expect_cart_is_empty()
