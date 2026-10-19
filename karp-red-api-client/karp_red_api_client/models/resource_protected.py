from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.resource_config import ResourceConfig


T = t.TypeVar("T", bound="ResourceProtected")


@attrs.define
class ResourceProtected:
    """
    Attributes:
        id (str):
        resource_id (str):
        name (str):
        config (ResourceConfig):
        last_modified (float):
        last_modified_by (str):
        message (None | str | Unset):
        is_published (bool | None | Unset):
        version (int | None | Unset):
    """

    id: str
    resource_id: str
    name: str
    config: ResourceConfig
    last_modified: float
    last_modified_by: str
    message: None | str | Unset = UNSET
    is_published: bool | None | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_id = self.resource_id

        name = self.name

        config = self.config.to_dict()

        last_modified = self.last_modified

        last_modified_by = self.last_modified_by

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        is_published: bool | None | Unset
        if isinstance(self.is_published, Unset):
            is_published = UNSET
        else:
            is_published = self.is_published

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resourceId": resource_id,
                "name": name,
                "config": config,
                "lastModified": last_modified,
                "lastModifiedBy": last_modified_by,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.resource_config import ResourceConfig  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        resource_id = d.pop("resourceId")

        name = d.pop("name")

        config = ResourceConfig.from_dict(d.pop("config"))

        last_modified = d.pop("lastModified")

        last_modified_by = d.pop("lastModifiedBy")

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_is_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(bool | None | Unset, data)

        is_published = _parse_is_published(d.pop("isPublished", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        resource_protected = cls(
            id=id,
            resource_id=resource_id,
            name=name,
            config=config,
            last_modified=last_modified,
            last_modified_by=last_modified_by,
            message=message,
            is_published=is_published,
            version=version,
        )

        resource_protected.additional_properties = d
        return resource_protected

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
