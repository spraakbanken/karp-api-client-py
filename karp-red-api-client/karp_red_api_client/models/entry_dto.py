from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.entry_dto_entry import EntryDtoEntry


T = t.TypeVar("T", bound="EntryDto")


@attrs.define
class EntryDto:
    """
    Attributes:
        id (str):
        version (int):
        last_modified (float):
        last_modified_by (str):
        discarded (bool):
        resource (str):
        entry (EntryDtoEntry):
        message (None | str | Unset):
    """

    id: str
    version: int
    last_modified: float
    last_modified_by: str
    discarded: bool
    resource: str
    entry: EntryDtoEntry
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        last_modified = self.last_modified

        last_modified_by = self.last_modified_by

        discarded = self.discarded

        resource = self.resource

        entry = self.entry.to_dict()

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "lastModified": last_modified,
                "lastModifiedBy": last_modified_by,
                "discarded": discarded,
                "resource": resource,
                "entry": entry,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.entry_dto_entry import EntryDtoEntry  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        last_modified = d.pop("lastModified")

        last_modified_by = d.pop("lastModifiedBy")

        discarded = d.pop("discarded")

        resource = d.pop("resource")

        entry = EntryDtoEntry.from_dict(d.pop("entry"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        entry_dto = cls(
            id=id,
            version=version,
            last_modified=last_modified,
            last_modified_by=last_modified_by,
            discarded=discarded,
            resource=resource,
            entry=entry,
            message=message,
        )

        entry_dto.additional_properties = d
        return entry_dto

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
