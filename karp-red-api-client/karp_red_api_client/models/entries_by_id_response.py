from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.entry_dto import EntryDto


T = t.TypeVar("T", bound="EntriesByIdResponse")


@attrs.define
class EntriesByIdResponse:
    """
    Attributes:
        total (int):
        hits (list[Any | EntryDto]):
    """

    total: int
    hits: list[Any | EntryDto]
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.entry_dto import EntryDto  # noqa: PLC0415

        total = self.total

        hits = []
        for hits_item_data in self.hits:
            hits_item: Any | dict[str, Any]
            if isinstance(hits_item_data, EntryDto):
                hits_item = hits_item_data.to_dict()
            else:
                hits_item = hits_item_data
            hits.append(hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.entry_dto import EntryDto  # noqa: PLC0415

        d = dict(src_dict)
        total = d.pop("total")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:

            def _parse_hits_item(data: object) -> Any | EntryDto:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    hits_item_type_0 = EntryDto.from_dict(data)

                    return hits_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return t.cast(Any | EntryDto, data)

            hits_item = _parse_hits_item(hits_item_data)

            hits.append(hits_item)

        entries_by_id_response = cls(
            total=total,
            hits=hits,
        )

        entries_by_id_response.additional_properties = d
        return entries_by_id_response

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
