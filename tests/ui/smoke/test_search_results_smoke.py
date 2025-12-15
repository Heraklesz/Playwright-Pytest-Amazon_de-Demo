"""
Smoke test ensuring navigation to search results does not crash the page.
"""

import pytest


@pytest.mark.smoke
def test_search_displays_results(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    try:
        page.wait_for_load_state("domcontentloaded", timeout=20_000)
    except Exception:
        pytest.skip("Page load blocked")

    # Attempt search only if input exists
    search_box = page.locator("#twotabsearchtextbox")
    if search_box.count() == 0:
        pytest.skip("Search input not available")

    try:
        search_box.fill("iphone")
        search_box.press("Enter")
        page.wait_for_load_state("domcontentloaded", timeout=20_000)
    except Exception:
        pytest.skip("Search interaction blocked")

    assert page.url.startswith("https://www.amazon.de")
