from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.multi_lang_type_1 import MultiLangType1


T = t.TypeVar("T", bound="FieldCategoryLabelsType0")


@attrs.define
class FieldCategoryLabelsType0:
    additional_properties: dict[str, MultiLangType1 | str] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, MultiLangType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        d = dict(src_dict)
        field_category_labels_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> MultiLangType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_multi_lang_type_1 = MultiLangType1.from_dict(data)

                    return componentsschemas_multi_lang_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return t.cast(MultiLangType1 | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        field_category_labels_type_0.additional_properties = additional_properties
        return field_category_labels_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> MultiLangType1 | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: MultiLangType1 | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
