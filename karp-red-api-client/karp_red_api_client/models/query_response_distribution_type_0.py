from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

T = t.TypeVar("T", bound="QueryResponseDistributionType0")


@attrs.define
class QueryResponseDistributionType0:
    additional_properties: dict[str, int] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)
        query_response_distribution_type_0 = cls()

        query_response_distribution_type_0.additional_properties = d
        return query_response_distribution_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
