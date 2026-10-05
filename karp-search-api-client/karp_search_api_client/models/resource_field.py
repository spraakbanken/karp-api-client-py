from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

T = t.TypeVar("T", bound="ResourceField")


@attrs.define
class ResourceField:
    """
    Attributes:
        name (str): The name of the field. Corresponds to a key under the top-level `fields`.
        primary (bool): Fields with `primary: true` are more relevant than fields with `primary: false`.
    """

    name: str
    primary: bool
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "primary": primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)
        name = d.pop("name")

        primary = d.pop("primary")

        resource_field = cls(
            name=name,
            primary=primary,
        )

        resource_field.additional_properties = d
        return resource_field

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
