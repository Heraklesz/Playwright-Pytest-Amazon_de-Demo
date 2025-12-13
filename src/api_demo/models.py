"""
This module defines data models used in API demo tests.
It provides a typed representation of API responses to
support structural validation and readable assertions.
"""

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
