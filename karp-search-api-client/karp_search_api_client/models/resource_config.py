from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.entry_word import EntryWord
    from ..models.multi_lang_type_1 import MultiLangType1
    from ..models.resource_field import ResourceField


T = t.TypeVar("T", bound="ResourceConfig")


@attrs.define
class ResourceConfig:
    """
    Attributes:
        resource_id (str): The resource ID
        fields (list[ResourceField]): The fields available in this resource.
        label (MultiLangType1 | str):
        entry_word (EntryWord):
        updated (int): The timestamp for when this resource was last updated (data or configuration). UNIX timestmap in
            milliseconds.
        size (int): The number of entries in this resource.
        link (str): A link to a relevant page for the resource.
        limited_access (bool | Unset): The resource is only available for users with access Default: False.
        protected_metadata (bool | Unset): The metadata of the resource is only available for users with access Default:
            False.
        description (MultiLangType1 | None | str | Unset): Description of this resource, can be in mulitple languages.
        tags (list[str] | None | Unset): The tags for this resource, see top-level `tags`, for tag labels and
            description.
    """

    resource_id: str
    fields: list[ResourceField]
    label: MultiLangType1 | str
    entry_word: EntryWord
    updated: int
    size: int
    link: str
    limited_access: bool | Unset = False
    protected_metadata: bool | Unset = False
    description: MultiLangType1 | None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415

        resource_id = self.resource_id

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        label: dict[str, Any] | str
        if isinstance(self.label, MultiLangType1):
            label = self.label.to_dict()
        else:
            label = self.label

        entry_word = self.entry_word.to_dict()

        updated = self.updated

        size = self.size

        link = self.link

        limited_access = self.limited_access

        protected_metadata = self.protected_metadata

        description: dict[str, Any] | None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, MultiLangType1):
            description = self.description.to_dict()
        else:
            description = self.description

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceId": resource_id,
                "fields": fields,
                "label": label,
                "entryWord": entry_word,
                "updated": updated,
                "size": size,
                "link": link,
            }
        )
        if limited_access is not UNSET:
            field_dict["limitedAccess"] = limited_access
        if protected_metadata is not UNSET:
            field_dict["protectedMetadata"] = protected_metadata
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.entry_word import EntryWord  # noqa: PLC0415
        from ..models.multi_lang_type_1 import MultiLangType1  # noqa: PLC0415
        from ..models.resource_field import ResourceField  # noqa: PLC0415

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = ResourceField.from_dict(fields_item_data)

            fields.append(fields_item)

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

        entry_word = EntryWord.from_dict(d.pop("entryWord"))

        updated = d.pop("updated")

        size = d.pop("size")

        link = d.pop("link")

        limited_access = d.pop("limitedAccess", UNSET)

        protected_metadata = d.pop("protectedMetadata", UNSET)

        def _parse_description(data: object) -> MultiLangType1 | None | str | Unset:
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

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = t.cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        resource_config = cls(
            resource_id=resource_id,
            fields=fields,
            label=label,
            entry_word=entry_word,
            updated=updated,
            size=size,
            link=link,
            limited_access=limited_access,
            protected_metadata=protected_metadata,
            description=description,
            tags=tags,
        )

        return resource_config
