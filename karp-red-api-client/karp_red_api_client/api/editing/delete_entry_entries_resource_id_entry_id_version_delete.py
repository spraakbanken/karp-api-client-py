import typing as t
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    resource_id: str,
    entry_id: Any,
    version: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/entries/{resource_id}/{entry_id}/{version}".format(
            resource_id=quote(str(resource_id), safe=""),
            entry_id=quote(str(entry_id), safe=""),
            version=quote(str(version), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 204:
        response_204 = t.cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = t.cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = t.cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = t.cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    entry_id: Any,
    version: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Delete Entry

     Delete a entry from a resource.

    Args:
        resource_id (str):
        entry_id (Any):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        entry_id=entry_id,
        version=version,
    )

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    entry_id: Any,
    version: int,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Delete Entry

     Delete a entry from a resource.

    Args:
        resource_id (str):
        entry_id (Any):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        resource_id=resource_id,
        entry_id=entry_id,
        version=version,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    entry_id: Any,
    version: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Delete Entry

     Delete a entry from a resource.

    Args:
        resource_id (str):
        entry_id (Any):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        entry_id=entry_id,
        version=version,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    entry_id: Any,
    version: int,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Delete Entry

     Delete a entry from a resource.

    Args:
        resource_id (str):
        entry_id (Any):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            entry_id=entry_id,
            version=version,
            client=client,
        )
    ).parsed
