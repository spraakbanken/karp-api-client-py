from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.history_dto import HistoryDto


T = t.TypeVar("T", bound="GetHistoryDto")


@attrs.define
class GetHistoryDto:
    """
    Attributes:
        history (list[HistoryDto]):
        total (int):
    """

    history: list[HistoryDto]
    total: int
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history": history,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.history_dto import HistoryDto  # noqa: PLC0415

        d = dict(src_dict)
        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = HistoryDto.from_dict(history_item_data)

            history.append(history_item)

        total = d.pop("total")

        get_history_dto = cls(
            history=history,
            total=total,
        )

        get_history_dto.additional_properties = d
        return get_history_dto

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
