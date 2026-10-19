from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

T = t.TypeVar("T", bound="EntryDiffDto")


@attrs.define
class EntryDiffDto:
    """
    Attributes:
        diff (Any):
        from_version (int | None):
        to_version (int | None):
    """

    diff: Any
    from_version: int | None
    to_version: int | None
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diff = self.diff

        from_version: int | None
        from_version = self.from_version

        to_version: int | None
        to_version = self.to_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diff": diff,
                "fromVersion": from_version,
                "toVersion": to_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        d = dict(src_dict)
        diff = d.pop("diff")

        def _parse_from_version(data: object) -> int | None:
            if data is None:
                return data
            return t.cast(int | None, data)

        from_version = _parse_from_version(d.pop("fromVersion"))

        def _parse_to_version(data: object) -> int | None:
            if data is None:
                return data
            return t.cast(int | None, data)

        to_version = _parse_to_version(d.pop("toVersion"))

        entry_diff_dto = cls(
            diff=diff,
            from_version=from_version,
            to_version=to_version,
        )

        entry_diff_dto.additional_properties = d
        return entry_diff_dto

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
