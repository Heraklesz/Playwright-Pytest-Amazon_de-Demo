"""
This module defines a simple REST API client for demo API testing.
It centralizes HTTP request handling and response validation logic
to keep API tests clean and focused on behavior rather than transport details.
"""

import requests


class DemoApiClient:
    """
    Lightweight REST client for interacting with the demo API.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str):
        return requests.get(f"{self.base_url}/{endpoint}")

    def post(self, endpoint: str, payload: dict):
        return requests.post(f"{self.base_url}/{endpoint}", json=payload)
