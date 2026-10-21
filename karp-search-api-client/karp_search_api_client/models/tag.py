from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.multi_lang_type_1 import MultiLangType1


T = t.TypeVar("T", bound="Tag")


@attrs.define
class Tag:
    """
    Attributes:
        label (MultiLangType1 | str):
        description (MultiLangType1 | str):
    """

    label: MultiLangType1 | str
    description: MultiLangType1 | str
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        label: dict[str, Any] | str
        if isinstance(self.label, MultiLangType1):
            label = self.label.to_dict()
        else:
            label = self.label

        description: dict[str, Any] | str
        if isinstance(self.description, MultiLangType1):
            description = self.description.to_dict()
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_label(data: object) -> MultiLangType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_multi_lang_type_1 = MultiLangType1.from_dict(data)

                return componentsschemas_multi_lang_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(MultiLangType1 | str, data)

        label = _parse_label(d.pop("label"))

        def _parse_description(data: object) -> MultiLangType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_multi_lang_type_1 = MultiLangType1.from_dict(data)

                return componentsschemas_multi_lang_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(MultiLangType1 | str, data)

        description = _parse_description(d.pop("description"))

        tag = cls(
            label=label,
            description=description,
        )

        tag.additional_properties = d
        return tag

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
