"""Search endpoint."""

import typing as t
from http import HTTPStatus
from urllib import parse

import attrs
import httpx2 as httpx
from karp_api_core import status_codes
from returns.result import Failure, Result, Success

from karp_search_api_client import AuthenticatedSearchClient, SearchClient, dsl, errors
from karp_search_api_client.models import HttpValidationError
from karp_search_api_client.models.search_response import SearchResponse
from karp_search_api_client.responses import Response


@attrs.define
class SearchOptions:
    """Options for adapting a Query."""

    resources: str | list[str]
    q: str | dsl.Query | None = attrs.field(default=None)
    from_: int | None = attrs.field(default=None)
    size: int | None = attrs.field(default=None)
    sort: list[str] | None = attrs.field(default=None)

    def to_search_string(self) -> str:
        """Format this object as a query string."""
        resources = ",".join(self.resources) if isinstance(self.resources, list) else self.resources
        d: dict[str, int | str] = {"resources": resources}
        if self.q:
            d["q"] = str(self.q)
        if self.from_:
            d["from"] = self.from_
        if self.size:
            d["size"] = self.size
        if self.sort and len(self.sort) > 0:
            d["sort"] = ",".join(self.sort)

        if d:
            return parse.urlencode(d, quote_via=parse.quote)
        return ""


def search_sync(
    *,
    client: SearchClient | AuthenticatedSearchClient,
    search_options: SearchOptions,
) -> Result[Response[SearchResponse], Response[HttpValidationError | None]]:
    """Query.

    Args:
        resources : sequence of resources as strings, or as a commas-separatade string.
        client : the client to use for this API call
        search_options : optional query options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code
                                and SearchClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than SearchClient.timeout.

    Returns:
        Response[Union[EntryAddResponse, HttpValidationError]]
    """
    kwargs = _get_search_kwargs(search_options=search_options)
    response = client.get_sync_client().request(**kwargs)

    return _build_search_response(client=client, response=response)


async def search_async(
    *,
    client: SearchClient | AuthenticatedSearchClient,
    search_options: SearchOptions,
) -> Result[Response[SearchResponse], Response[HttpValidationError | None]]:
    """Query.

    Args:
        resources : sequence of resources as strings, or as a commas-separatade string.
        client : the client to use for this API call
        search_options : optional query options

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code
                                and SearchClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than SearchClient.timeout.

    Returns:
        Response[Union[EntryAddResponse, HttpValidationError]]
    """
    kwargs = _get_search_kwargs(
        search_options=search_options,
    )
    response = await client.get_async_client().request(**kwargs)

    return _build_search_response(client=client, response=response)


def _get_search_kwargs(*, search_options: SearchOptions) -> dict[str, t.Any]:
    headers: dict[str, t.Any] = {}

    qs = search_options.to_search_string()
    url = f"/search?{qs}"

    kwargs: dict[str, t.Any] = {"method": "get", "url": url}
    headers["Accept"] = "application/json"
    kwargs["headers"] = headers
    return kwargs


def _build_search_response(
    *, client: SearchClient | AuthenticatedSearchClient, response: httpx.Response
) -> Result[Response[SearchResponse], Response[HttpValidationError | None]]:
    return (
        _parse_search_response(client=client, response=response)
        .map(
            lambda resp: Response(
                status_code=HTTPStatus(response.status_code),
                content=response.content,
                headers=response.headers,
                parsed=resp,
            )
        )
        .alt(
            lambda opt_resp: Response(
                status_code=HTTPStatus(response.status_code),
                content=response.content,
                headers=response.headers,
                parsed=opt_resp,
            )
        )
    )


def _parse_search_response(
    *, client: SearchClient | AuthenticatedSearchClient, response: httpx.Response
) -> Result[SearchResponse, HttpValidationError | None]:
    if response.status_code == status_codes.OK:
        response_200 = SearchResponse.from_dict(response.json())

        return Success(response_200)
    if response.status_code == status_codes.UNPROCESSABLE_ENTITY:
        response_422 = HttpValidationError.from_dict(response.json())
        return Failure(response_422)
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return Failure(None)
