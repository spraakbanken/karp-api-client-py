from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_result import SearchResult
from ...models.user_error_schema import UserErrorSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    resources: None | str,
    sort: str | Unset = "asc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params["size"] = size

    params["from"] = from_

    json_resources: None | str
    json_resources = resources
    params["resources"] = json_resources

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SearchResult | UserErrorSchema | None:
    if response.status_code == 200:
        response_200 = SearchResult.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = UserErrorSchema.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SearchResult | UserErrorSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    resources: None | str,
    sort: str | Unset = "asc",
) -> Response[HTTPValidationError | SearchResult | UserErrorSchema]:
    """Search

     From each provided resource, return the entries that match the query q.

    ### Sorting
    Sorting is supported on fields that are present in all selected resources. The default field is
    `entryWord` (**ascending** order).

    The sort is done within each resource, the results from each resource are not mixed.

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        size (int | Unset):  Default: 10.
        from_ (int | Unset):  Default: 0.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchResult | UserErrorSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        size=size,
        from_=from_,
        resources=resources,
        sort=sort,
    )

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    resources: None | str,
    sort: str | Unset = "asc",
) -> HTTPValidationError | SearchResult | UserErrorSchema | None:
    """Search

     From each provided resource, return the entries that match the query q.

    ### Sorting
    Sorting is supported on fields that are present in all selected resources. The default field is
    `entryWord` (**ascending** order).

    The sort is done within each resource, the results from each resource are not mixed.

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        size (int | Unset):  Default: 10.
        from_ (int | Unset):  Default: 0.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchResult | UserErrorSchema
    """

    return sync_detailed(
        client=client,
        q=q,
        size=size,
        from_=from_,
        resources=resources,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    resources: None | str,
    sort: str | Unset = "asc",
) -> Response[HTTPValidationError | SearchResult | UserErrorSchema]:
    """Search

     From each provided resource, return the entries that match the query q.

    ### Sorting
    Sorting is supported on fields that are present in all selected resources. The default field is
    `entryWord` (**ascending** order).

    The sort is done within each resource, the results from each resource are not mixed.

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        size (int | Unset):  Default: 10.
        from_ (int | Unset):  Default: 0.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SearchResult | UserErrorSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        size=size,
        from_=from_,
        resources=resources,
        sort=sort,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    resources: None | str,
    sort: str | Unset = "asc",
) -> HTTPValidationError | SearchResult | UserErrorSchema | None:
    """Search

     From each provided resource, return the entries that match the query q.

    ### Sorting
    Sorting is supported on fields that are present in all selected resources. The default field is
    `entryWord` (**ascending** order).

    The sort is done within each resource, the results from each resource are not mixed.

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        size (int | Unset):  Default: 10.
        from_ (int | Unset):  Default: 0.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SearchResult | UserErrorSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            size=size,
            from_=from_,
            resources=resources,
            sort=sort,
        )
    ).parsed
