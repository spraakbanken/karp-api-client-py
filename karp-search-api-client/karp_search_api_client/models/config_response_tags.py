from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.tag import Tag


T = t.TypeVar("T", bound="ConfigResponseTags")


@attrs.define
class ConfigResponseTags:
    """All tags available in this instance. Will be used by some of the resources under "resources"."""

    additional_properties: dict[str, Tag] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.tag import Tag  # noqa: PLC0415

        d = dict(src_dict)
        config_response_tags = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Tag.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        config_response_tags.additional_properties = additional_properties
        return config_response_tags

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Tag:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Tag) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
