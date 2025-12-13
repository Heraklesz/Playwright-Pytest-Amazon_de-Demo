"""
This module provides a lightweight API client built on top of Playwright's
request context. It is intended for network-level assertions that complement
UI-driven tests, such as validating response status codes and payload structure
of backend calls triggered by user actions.
"""

from playwright.sync_api import APIRequestContext, expect


class ApiClient:
    """
    Wrapper around Playwright's APIRequestContext for simple network assertions.
    """

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, url: str):
        """
        Executes a GET request and returns the response.
        """
        response = self.request.get(url)
        expect(response).to_be_ok()
        return response
