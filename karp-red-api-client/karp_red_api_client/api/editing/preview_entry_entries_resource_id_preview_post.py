import typing as t
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entry_preview import EntryPreview
from ...models.entry_preview_response import EntryPreviewResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    resource_id: str,
    *,
    body: EntryPreview,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/entries/{resource_id}/preview".format(
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EntryPreviewResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EntryPreviewResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | EntryPreviewResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EntryPreview,
) -> Response[Any | EntryPreviewResponse | HTTPValidationError]:
    """Preview Entry

    Args:
        resource_id (str):
        body (EntryPreview):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntryPreviewResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        body=body,
    )

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EntryPreview,
) -> Any | EntryPreviewResponse | HTTPValidationError | None:
    """Preview Entry

    Args:
        resource_id (str):
        body (EntryPreview):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntryPreviewResponse | HTTPValidationError
    """

    return sync_detailed(
        resource_id=resource_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EntryPreview,
) -> Response[Any | EntryPreviewResponse | HTTPValidationError]:
    """Preview Entry

    Args:
        resource_id (str):
        body (EntryPreview):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntryPreviewResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        body=body,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EntryPreview,
) -> Any | EntryPreviewResponse | HTTPValidationError | None:
    """Preview Entry

    Args:
        resource_id (str):
        body (EntryPreview):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntryPreviewResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            client=client,
            body=body,
        )
    ).parsed
