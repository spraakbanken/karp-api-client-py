"""Client for accessing Karp Red API."""

import os
import typing as t

import attrs
import httpx2 as httpx

from karp_api_client.client.base import ApiKeyAuth, ClientBase

T = t.TypeVar("T", bound="ClientBase")


@attrs.define(slots=False)
class RedClient(ClientBase):
    """Client to use for unauthenticated API calls."""

    _base_url: str = attrs.field(default="https://spraakbanken4.it.gu.se/karp/v7", alias="base_url")


@attrs.define(slots=False)
class AuthenticatedRedClient(RedClient):
    """Client to use for authenticated API calls."""

    _token: str = attrs.field(kw_only=True, alias="token")

    def _create_sync_client(self) -> httpx.Client:
        client = super()._create_sync_client()
        client.auth = ApiKeyAuth(self._token)
        return client

    def _create_async_client(self) -> httpx.AsyncClient:
        client = super()._create_async_client()
        client.auth = ApiKeyAuth(self._token)
        return client

    @classmethod
    def from_env(cls) -> "AuthenticatedRedClient":
        """Create an AuthenticatedClient from env."""
        token = None
        if (
            (token_from_env := os.environ.get("KARP_RED_API_CLIENT_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_RED_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_API_CLIENT_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_API_TOKEN"))
        ):
            token = token_from_env

        if token is None:
            raise RuntimeError(
                "you must set KARP_RED_API_CLIENT_API_TOKEN, KARP_RED_API_TOKEN, KARP_API_CLIENT_API_TOKEN or KARP_API_TOKEN"  # noqa: E501
            )
        return cls(token=token)
