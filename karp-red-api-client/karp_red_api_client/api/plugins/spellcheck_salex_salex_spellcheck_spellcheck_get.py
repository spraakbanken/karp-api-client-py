from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.spellcheck_result import SpellcheckResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    words: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["words"] = words

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/salex/salex_spellcheck/spellcheck",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SpellcheckResult | None:
    if response.status_code == 200:
        response_200 = SpellcheckResult.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SpellcheckResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    words: str,
) -> Response[HTTPValidationError | SpellcheckResult]:
    """Spellcheck

     Check which of the given words are not found in Salex. Looks in inflection tables and fields called
    'ortografi'.

    Args:
        words (str): Words to be spellchecked. Should not contain whitespace or punctuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpellcheckResult]
    """

    kwargs = _get_kwargs(
        words=words,
    )

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    words: str,
) -> HTTPValidationError | SpellcheckResult | None:
    """Spellcheck

     Check which of the given words are not found in Salex. Looks in inflection tables and fields called
    'ortografi'.

    Args:
        words (str): Words to be spellchecked. Should not contain whitespace or punctuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpellcheckResult
    """

    return sync_detailed(
        client=client,
        words=words,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    words: str,
) -> Response[HTTPValidationError | SpellcheckResult]:
    """Spellcheck

     Check which of the given words are not found in Salex. Looks in inflection tables and fields called
    'ortografi'.

    Args:
        words (str): Words to be spellchecked. Should not contain whitespace or punctuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpellcheckResult]
    """

    kwargs = _get_kwargs(
        words=words,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    words: str,
) -> HTTPValidationError | SpellcheckResult | None:
    """Spellcheck

     Check which of the given words are not found in Salex. Looks in inflection tables and fields called
    'ortografi'.

    Args:
        words (str): Words to be spellchecked. Should not contain whitespace or punctuation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpellcheckResult
    """

    return (
        await asyncio_detailed(
            client=client,
            words=words,
        )
    ).parsed
