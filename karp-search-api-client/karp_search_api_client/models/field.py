from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.field_category_labels_type_0 import FieldCategoryLabelsType0
    from ..models.field_fields import FieldFields
    from ..models.multi_lang_type_1 import MultiLangType1


T = t.TypeVar("T", bound="Field")


@attrs.define
class Field:
    """
    Attributes:
        name (str): (Machine) name of the field. This name is used by resources to list the available fields.
        type_ (str): Type of the field, can be text, integer or float or table.
        collection (bool | Unset): If `true`, the field is a list of `type`. Default: False.
        label (MultiLangType1 | None | str | Unset): Label for the field, can be in mulitple languages.
        fields (FieldFields | Unset): If type is table, then there can be sub-fields (that cannot be table).
        categories (list[str] | None | Unset): If set, a list of possible values for this field.
        category_labels (FieldCategoryLabelsType0 | None | Unset): For fields with categories, labels for each value
            (optional, even if categories is given).
        protected_metadata (bool | Unset): The field is only available for users with access Default: False.
        resource_id (list[str] | Unset): The resources that this field is available in.
    """

    name: str
    type_: str
    collection: bool | Unset = False
    label: MultiLangType1 | None | str | Unset = UNSET
    fields: FieldFields | Unset = UNSET
    categories: list[str] | None | Unset = UNSET
    category_labels: FieldCategoryLabelsType0 | None | Unset = UNSET
    protected_metadata: bool | Unset = False
    resource_id: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_category_labels_type_0 import FieldCategoryLabelsType0  # noqa: PLC0415
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        name = self.name

        type_ = self.type_

        collection = self.collection

        label: dict[str, Any] | None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, MultiLangType1):
            label = self.label.to_dict()
        else:
            label = self.label

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        category_labels: dict[str, Any] | None | Unset
        if isinstance(self.category_labels, Unset):
            category_labels = UNSET
        elif isinstance(self.category_labels, FieldCategoryLabelsType0):
            category_labels = self.category_labels.to_dict()
        else:
            category_labels = self.category_labels

        protected_metadata = self.protected_metadata

        resource_id: list[str] | Unset = UNSET
        if not isinstance(self.resource_id, Unset):
            resource_id = self.resource_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if collection is not UNSET:
            field_dict["collection"] = collection
        if label is not UNSET:
            field_dict["label"] = label
        if fields is not UNSET:
            field_dict["fields"] = fields
        if categories is not UNSET:
            field_dict["categories"] = categories
        if category_labels is not UNSET:
            field_dict["categoryLabels"] = category_labels
        if protected_metadata is not UNSET:
            field_dict["protectedMetadata"] = protected_metadata
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.field_category_labels_type_0 import FieldCategoryLabelsType0  # noqa: PLC0415
        from ..models.field_fields import FieldFields  # noqa: PLC0415
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        collection = d.pop("collection", UNSET)

        def _parse_label(data: object) -> MultiLangType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_multi_lang_type_1 = MultiLangType1.from_dict(data)

                return componentsschemas_multi_lang_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(MultiLangType1 | None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: FieldFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = FieldFields.from_dict(_fields)

        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = t.cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_category_labels(data: object) -> FieldCategoryLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_labels_type_0 = FieldCategoryLabelsType0.from_dict(data)

                return category_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(FieldCategoryLabelsType0 | None | Unset, data)

        category_labels = _parse_category_labels(d.pop("categoryLabels", UNSET))

        protected_metadata = d.pop("protectedMetadata", UNSET)

        resource_id = t.cast(list[str], d.pop("resourceId", UNSET))

        field = cls(
            name=name,
            type_=type_,
            collection=collection,
            label=label,
            fields=fields,
            categories=categories,
            category_labels=category_labels,
            protected_metadata=protected_metadata,
            resource_id=resource_id,
        )

        return field
