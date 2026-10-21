"""Client for accessing Karp API."""

import os
import typing as t

import attrs
import httpx2 as httpx
from karp_api_core.client_base import ClientBase


@attrs.define
class Client(ClientBase):
    """Client to use for unauthenticated API calls.

    A class for keeping track of data related to the API

    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
    """

    # raise_on_unexpected_status: bool = attrs.field(default=False, kw_only=True)
    _base_url: str = attrs.field(default="https://spraakbanken4.it.gu.se/karp/v7", alias="base_url")


@attrs.define
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints

    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.


    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
        token: The token to use for authentication
        prefix: The prefix to use for the Authorization header
        auth_header_name: The name of the Authorization header
    """

    token: str = attrs.field(repr=False)
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"
    # raise_on_unexpected_status: bool = attrs.field(default=False, kw_only=True)
    _base_url: str = attrs.field(default="https://spraakbanken4.it.gu.se/karp/v7", alias="base_url")

    def _create_sync_client(self) -> httpx.Client:
        self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
        client = super()._create_sync_client()
        return client

    def _create_async_client(self) -> httpx.AsyncClient:
        self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
        client = super()._create_async_client()
        return client

    @classmethod
    def from_env(cls) -> t.Self:
        """Create an AuthenticatedClient from env."""
        token = None
        if (
            (token_from_env := os.environ.get("KARP_XYZ_API_CLIENT_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_XYZ_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_API_CLIENT_API_TOKEN"))
            or (token_from_env := os.environ.get("KARP_API_TOKEN"))
        ):
            token = token_from_env

        if token is None:
            raise RuntimeError(
                "you must set KARP_XYZ_API_CLIENT_API_TOKEN, KARP_XYZ_API_TOKEN, KARP_API_CLIENT_API_TOKEN or KARP_API_TOKEN"  # noqa: E501
            )
        return cls(token=token)
