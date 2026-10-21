from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.entry_add_entry import EntryAddEntry


T = t.TypeVar("T", bound="EntryAdd")


@attrs.define
class EntryAdd:
    """
    Attributes:
        entry (EntryAddEntry):
        message (str | Unset):  Default: ''.
    """

    entry: EntryAddEntry
    message: str | Unset = ""
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.entry_add_entry import EntryAddEntry  # noqa: PLC0415

        d = dict(src_dict)
        entry = EntryAddEntry.from_dict(d.pop("entry"))

        message = d.pop("message", UNSET)

        entry_add = cls(
            entry=entry,
            message=message,
        )

        entry_add.additional_properties = d
        return entry_add

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
