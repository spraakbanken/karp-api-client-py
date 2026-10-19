from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

T = t.TypeVar("T", bound="StatisticsDto")


@attrs.define
class StatisticsDto:
    """
    Attributes:
        value (Any | str):
        count (int):
    """

    value: Any | str
    count: int
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Any | str
        value = self.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)

        def _parse_value(data: object) -> Any | str:
            return t.cast(Any | str, data)

        value = _parse_value(d.pop("value"))

        count = d.pop("count")

        statistics_dto = cls(
            value=value,
            count=count,
        )

        statistics_dto.additional_properties = d
        return statistics_dto

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
