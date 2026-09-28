"""Responses."""

import typing as t
from collections.abc import MutableMapping
from http import HTTPStatus

import attrs

T = t.TypeVar("T")


@attrs.define
class Response(t.Generic[T]):
    """A response from an endpoint."""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T | None


__all__ = ["Response"]
