from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_response import ConfigResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/config",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConfigResponse | None:
    if response.status_code == 200:
        response_200 = ConfigResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConfigResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ConfigResponse]:
    """Get config

     Returns a description of the contents of each installed resource/lexicon. For example the available
    fields and their types.

    Some resources have `limitedAccess: true` - they will not be searchable without access.

    Some resources have `protectedMetadata: true` - they will not be returned by this call without
    access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ConfigResponse | None:
    """Get config

     Returns a description of the contents of each installed resource/lexicon. For example the available
    fields and their types.

    Some resources have `limitedAccess: true` - they will not be searchable without access.

    Some resources have `protectedMetadata: true` - they will not be returned by this call without
    access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ConfigResponse]:
    """Get config

     Returns a description of the contents of each installed resource/lexicon. For example the available
    fields and their types.

    Some resources have `limitedAccess: true` - they will not be searchable without access.

    Some resources have `protectedMetadata: true` - they will not be returned by this call without
    access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ConfigResponse | None:
    """Get config

     Returns a description of the contents of each installed resource/lexicon. For example the available
    fields and their types.

    Some resources have `limitedAccess: true` - they will not be searchable without access.

    Some resources have `protectedMetadata: true` - they will not be returned by this call without
    access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
