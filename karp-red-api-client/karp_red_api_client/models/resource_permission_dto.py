from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..models.scope import Scope

T = t.TypeVar("T", bound="ResourcePermissionDto")


@attrs.define
class ResourcePermissionDto:
    """
    Attributes:
        resource_id (str):
        protected (None | Scope):
    """

    resource_id: str
    protected: None | Scope
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        protected: None | str
        if isinstance(self.protected, Scope):
            protected = self.protected.value
        else:
            protected = self.protected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "protected": protected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        def _parse_protected(data: object) -> None | Scope:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protected_type_0 = Scope(data)

                return protected_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(None | Scope, data)

        protected = _parse_protected(d.pop("protected"))

        resource_permission_dto = cls(
            resource_id=resource_id,
            protected=protected,
        )

        resource_permission_dto.additional_properties = d
        return resource_permission_dto

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
