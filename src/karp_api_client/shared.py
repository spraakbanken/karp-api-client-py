"""Utility types."""

import typing as t
from collections.abc import MutableMapping
from http import HTTPStatus

import attrs


class Unset:
    def __bool__(self) -> t.Literal[False]:
        return False

    def __str__(self) -> str:
        return "UNSET"

    def __repr__(self) -> str:
        return "UNSET"


UNSET: Unset = Unset()
T = t.TypeVar("T")


@attrs.define
class Response(t.Generic[T]):
    """A response from an endpoint."""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T | None


__all__ = ["Response"]
