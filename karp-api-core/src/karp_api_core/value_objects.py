"""Value objects."""

import typing as t
from collections.abc import Mapping, MutableMapping
from http import HTTPStatus

import attrs


class Unset:
    """Model for unset values."""

    def __bool__(self) -> t.Literal[False]:
        """Return is always false."""
        return False

    def __str__(self) -> str:
        """Return the string version of this class."""
        return "UNSET"

    def __repr__(self) -> str:
        """Return the repr version of this class."""
        return "UNSET"


UNSET: Unset = Unset()

# The types that `httpx.Client(files=)` can accept, copied from that library.
FileContent = t.IO[bytes] | bytes | str
FileTypes = (
    # (filename, file (or bytes), content_type)
    tuple[str | None, FileContent, str | None]
    # (filename, file (or bytes), content_type, headers)
    | tuple[str | None, FileContent, str | None, Mapping[str, str]]
)
RequestFiles = list[tuple[str, FileTypes]]


@attrs.define
class File:
    """Contains information for file uploads."""

    payload: t.BinaryIO
    file_name: str | None = None
    mime_type: str | None = None

    def to_tuple(self) -> FileTypes:
        """Return a tuple representation that httpx will accept for multipart/form-data."""
        return self.file_name, self.payload, self.mime_type


T = t.TypeVar("T")


@attrs.define
class Response(t.Generic[T]):
    """A response from an endpoint."""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: T | None


__all__ = ["UNSET", "File", "FileTypes", "RequestFiles", "Response", "Unset"]
