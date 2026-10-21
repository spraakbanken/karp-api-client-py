"""A client library for accessing Karps sökgränssnitt - API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
