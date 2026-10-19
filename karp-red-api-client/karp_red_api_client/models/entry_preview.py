from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.entry_preview_entry import EntryPreviewEntry


T = t.TypeVar("T", bound="EntryPreview")


@attrs.define
class EntryPreview:
    """
    Attributes:
        entry (EntryPreviewEntry):
    """

    entry: EntryPreviewEntry
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.entry_preview_entry import EntryPreviewEntry  # noqa: PLC0415

        d = dict(src_dict)
        entry = EntryPreviewEntry.from_dict(d.pop("entry"))

        entry_preview = cls(
            entry=entry,
        )

        entry_preview.additional_properties = d
        return entry_preview

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
