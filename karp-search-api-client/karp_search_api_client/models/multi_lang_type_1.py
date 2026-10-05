from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

T = t.TypeVar("T", bound="MultiLangType1")


@attrs.define
class MultiLangType1:
    additional_properties: dict[str, str] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)
        multi_lang_type_1 = cls()

        multi_lang_type_1.additional_properties = d
        return multi_lang_type_1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
