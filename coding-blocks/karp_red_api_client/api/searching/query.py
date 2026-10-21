"""Query endpoint."""

import typing as t
from http import HTTPStatus

import httpx2 as httpx
from karp_red_api_client import AuthenticatedClient, Client, dsl, errors
from karp_red_api_client.models import HTTPValidationError
from karp_red_api_client.models.query_response import QueryResponse
from karp_red_api_client.responses import Response
from karp_red_api_client.types import UNSET, Unset


def _get_kwargs(
    *,
    resources: str | list[str],
    q: dsl.Query | str | Unset | None = UNSET,
    size: int | Unset = 25,
    from_: int | Unset = 0,
    sort: str | Unset | None = UNSET,
    lexicon_stats: bool | Unset = UNSET,
    path: str | Unset | None = UNSET,
) -> dict[str, t.Any]:

    params: dict[str, t.Any] = {}

    json_q: str | Unset | None
    if isinstance(q, Unset):
        json_q = UNSET
    elif isinstance(q, dsl.Query):
        json_q = str(q)
    else:
        json_q = q
    params["q"] = json_q

    params["size"] = size

    params["from"] = from_

    params["sort"] = sort

    json_lexicon_stats: str | Unset
    if isinstance(lexicon_stats, Unset):
        json_lexicon_stats = UNSET
    elif lexicon_stats:
        json_lexicon_stats = "true"
    else:
        json_lexicon_stats = "false"
    params["lexicon_stats"] = json_lexicon_stats

    json_path: str | Unset | None
    json_path = UNSET if isinstance(path, Unset) else path
    params["path"] = json_path

    path_resources: str
    path_resources = ",".join(resources) if isinstance(resources, list) else resources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, t.Any] = {
        "method": "get",
        "url": f"/query/{path_resources}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | QueryResponse | None:
    if response.status_code == 200:  # noqa: PLR2004
        response_200 = QueryResponse.from_dict(response.json())

        return response_200  # noqa: RET504

    if response.status_code == 422:  # noqa: PLR2004
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422  # noqa: RET504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | QueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client | AuthenticatedClient,
    resources: str | list[str],
    q: dsl.Query | str | Unset | None = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    sort: str | Unset | None = None,
    lexicon_stats: bool = True,
    path: str | None = None,
) -> Response[HTTPValidationError | QueryResponse]:
    """Search.

    Returns a list of entries matching the given query in the given resources. The results are mixed from the given resources.

    Args:
        client: a client
        resources: A list of resource identifiers, or a comma-separated str.
        q: The query. If missing, all entries in chosen resource(s) will be returned.
            See [Searching](#section/Searching).
        from_: Default: 0
        size: Default: 10.
        sort: The `field` to sort by.
        lexicon_stats: Show the hit count by lexicon.
        path: A dot-separated path to for returning a specific field in JSON. Only
            supports one path down into the tree with no indexing. For example, to fetch
            only the field `baseform` in the entry, use `?path=entry.baseform`.
            If the selected field is an array, the result will also be wrapped in an array.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QueryResult
    """  # noqa: E501
    kwargs = _get_kwargs(
        resources=resources,
        q=q,
        from_=from_,
        size=size,
        sort=sort,
        lexicon_stats=lexicon_stats,
        path=path,
    )

    response = client.get_sync_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client | AuthenticatedClient,
    resources: str | list[str],
    q: dsl.Query | str | Unset | None = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    sort: str | Unset | None = None,
    lexicon_stats: bool = True,
    path: str | None = None,
) -> HTTPValidationError | QueryResponse | None:
    """Search.

    Returns a list of entries matching the given query in the given resources. The results are mixed from the given resources.

    Args:
        client: a client
        resources: A list of resource identifiers, or a comma-separated str.
        q: The query. If missing, all entries in chosen resource(s) will be returned.
            See [Searching](#section/Searching).
        from_: Default: 0
        size: Default: 10.
        sort: The `field` to sort by.
        lexicon_stats: Show the hit count by lexicon.
        path: A dot-separated path to for returning a specific field in JSON. Only
            supports one path down into the tree with no indexing. For example, to fetch
            only the field `baseform` in the entry, use `?path=entry.baseform`.
            If the selected field is an array, the result will also be wrapped in an array.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QueryResult
    """  # noqa: E501
    return (
        sync_detailed(
            client=client,
            resources=resources,
            q=q,
            from_=from_,
            size=size,
            sort=sort,
            lexicon_stats=lexicon_stats,
            path=path,
        )
    ).parsed


async def asyncio_detailed(
    *,
    client: Client | AuthenticatedClient,
    resources: str | list[str],
    q: dsl.Query | str | Unset | None = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    sort: str | Unset | None = None,
    lexicon_stats: bool = True,
    path: str | None = None,
) -> Response[HTTPValidationError | QueryResponse]:
    """Search.

    Returns a list of entries matching the given query in the given resources. The results are mixed from the given resources.

    Args:
        client: a client
        resources: A list of resource identifiers, or a comma-separated str.
        q: The query. If missing, all entries in chosen resource(s) will be returned.
            See [Searching](#section/Searching).
        from_: Default: 0
        size: Default: 10.
        sort: The `field` to sort by.
        lexicon_stats: Show the hit count by lexicon.
        path: A dot-separated path to for returning a specific field in JSON. Only
            supports one path down into the tree with no indexing. For example, to fetch
            only the field `baseform` in the entry, use `?path=entry.baseform`.
            If the selected field is an array, the result will also be wrapped in an array.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QueryResult
    """  # noqa: E501
    kwargs = _get_kwargs(
        resources=resources,
        q=q,
        from_=from_,
        size=size,
        sort=sort,
        lexicon_stats=lexicon_stats,
        path=path,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client | AuthenticatedClient,
    resources: str | list[str],
    q: dsl.Query | str | Unset | None = UNSET,
    size: int | Unset = 10,
    from_: int | Unset = 0,
    sort: str | Unset | None = None,
    lexicon_stats: bool = True,
    path: str | None = None,
) -> HTTPValidationError | QueryResponse | None:
    """Search.

    Returns a list of entries matching the given query in the given resources. The results are mixed from the given resources.

    Args:
        client: a client
        resources: A list of resource identifiers, or a comma-separated str.
        q: The query. If missing, all entries in chosen resource(s) will be returned.
            See [Searching](#section/Searching).
        from_: Default: 0
        size: Default: 10.
        sort: The `field` to sort by.
        lexicon_stats: Show the hit count by lexicon.
        path: A dot-separated path to for returning a specific field in JSON. Only
            supports one path down into the tree with no indexing. For example, to fetch
            only the field `baseform` in the entry, use `?path=entry.baseform`.
            If the selected field is an array, the result will also be wrapped in an array.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | QueryResult
    """  # noqa: E501
    return (
        await asyncio_detailed(
            client=client,
            resources=resources,
            q=q,
            from_=from_,
            size=size,
            sort=sort,
            lexicon_stats=lexicon_stats,
            path=path,
        )
    ).parsed
