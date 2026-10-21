from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..models.entry_op import EntryOp

if t.TYPE_CHECKING:
    from ..models.history_dto_diff_item import HistoryDtoDiffItem
    from ..models.history_dto_entry import HistoryDtoEntry


T = t.TypeVar("T", bound="HistoryDto")


@attrs.define
class HistoryDto:
    """
    Attributes:
        id (str):
        timestamp (float):
        message (str):
        version (int):
        op (EntryOp):
        user_id (str):
        diff (list[HistoryDtoDiffItem]):
        entry (HistoryDtoEntry):
    """

    id: str
    timestamp: float
    message: str
    version: int
    op: EntryOp
    user_id: str
    diff: list[HistoryDtoDiffItem]
    entry: HistoryDtoEntry
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        timestamp = self.timestamp

        message = self.message

        version = self.version

        op = self.op.value

        user_id = self.user_id

        diff = []
        for diff_item_data in self.diff:
            diff_item = diff_item_data.to_dict()
            diff.append(diff_item)

        entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "timestamp": timestamp,
                "message": message,
                "version": version,
                "op": op,
                "userId": user_id,
                "diff": diff,
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.history_dto_diff_item import HistoryDtoDiffItem  # noqa: PLC0415
        from ..models.history_dto_entry import HistoryDtoEntry  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        timestamp = d.pop("timestamp")

        message = d.pop("message")

        version = d.pop("version")

        op = EntryOp(d.pop("op"))

        user_id = d.pop("userId")

        diff = []
        _diff = d.pop("diff")
        for diff_item_data in _diff:
            diff_item = HistoryDtoDiffItem.from_dict(diff_item_data)

            diff.append(diff_item)

        entry = HistoryDtoEntry.from_dict(d.pop("entry"))

        history_dto = cls(
            id=id,
            timestamp=timestamp,
            message=message,
            version=version,
            op=op,
            user_id=user_id,
            diff=diff,
            entry=entry,
        )

        history_dto.additional_properties = d
        return history_dto

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
