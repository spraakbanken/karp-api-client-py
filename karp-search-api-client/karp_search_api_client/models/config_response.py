from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.config_response_fields import ConfigResponseFields
    from ..models.config_response_tags import ConfigResponseTags
    from ..models.resource_config import ResourceConfig


T = t.TypeVar("T", bound="ConfigResponse")


@attrs.define
class ConfigResponse:
    """
    Attributes:
        resources (list[ResourceConfig]): All resources available in this instance.
        tags (ConfigResponseTags): All tags available in this instance. Will be used by some of the resources under
            "resources".
        fields (ConfigResponseFields): All fields available in this instance.
    """

    resources: list[ResourceConfig]
    tags: ConfigResponseTags
    fields: ConfigResponseFields
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        tags = self.tags.to_dict()

        fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
                "tags": tags,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.config_response_fields import ConfigResponseFields  # noqa: PLC0415
        from ..models.config_response_tags import ConfigResponseTags  # noqa: PLC0415
        from ..models.resource_config import ResourceConfig  # noqa: PLC0415

        d = dict(src_dict)
        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = ResourceConfig.from_dict(resources_item_data)

            resources.append(resources_item)

        tags = ConfigResponseTags.from_dict(d.pop("tags"))

        fields = ConfigResponseFields.from_dict(d.pop("fields"))

        config_response = cls(
            resources=resources,
            tags=tags,
            fields=fields,
        )

        config_response.additional_properties = d
        return config_response

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
