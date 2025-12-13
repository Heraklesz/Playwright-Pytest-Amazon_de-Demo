"""
This end-to-end test verifies a complete user journey:
searching for a product, opening the product details page,
adding the product to the shopping cart, and validating cart contents.
It validates critical integration points across multiple domains.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage


@pytest.mark.e2e
def test_user_can_add_product_to_cart_from_search(page):
    home_page = HomePage(page)
    results_page = SearchResultsPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    home_page.load(config.base_url)
    home_page.search_for("usb c cable")

    results_page.wait_until_loaded()
    results_page.results_list.click_first_result()

    product_page.wait_until_loaded()
    product_page.add_product_to_cart()

    cart_page.wait_until_loaded()
    cart_page.expect_cart_has_items()
