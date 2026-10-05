from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.user_error_schema_extra_type_0 import UserErrorSchemaExtraType0


T = t.TypeVar("T", bound="UserErrorSchema")


@attrs.define
class UserErrorSchema:
    """
    Attributes:
        message (str):
        code (int | None | Unset): ### Code definitions

            1: Returned when the database was forced to truncate a value. Query parameter "columns" is the issue.

            2: Returned when an unauthenticated user or a user without the proper access tries access a restricted resource.

            3: Returned when a JWT was given, but the JWT was malformed or expired.

            4: Returned when an API key was given, but it was malformed, expired or it was not possible to verify the key.
        extra (None | Unset | UserErrorSchemaExtraType0): Some errors have data output in addition to the human readable
            message.
    """

    message: str
    code: int | None | Unset = UNSET
    extra: None | Unset | UserErrorSchemaExtraType0 = UNSET
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_error_schema_extra_type_0 import UserErrorSchemaExtraType0  # noqa: PLC0415

        message = self.message

        code: int | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        extra: dict[str, Any] | None | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, UserErrorSchemaExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.user_error_schema_extra_type_0 import UserErrorSchemaExtraType0  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message")

        def _parse_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(int | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_extra(data: object) -> None | Unset | UserErrorSchemaExtraType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = UserErrorSchemaExtraType0.from_dict(data)

                return extra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(None | Unset | UserErrorSchemaExtraType0, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        user_error_schema = cls(
            message=message,
            code=code,
            extra=extra,
        )

        user_error_schema.additional_properties = d
        return user_error_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
