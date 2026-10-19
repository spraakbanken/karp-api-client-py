from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.resource_config_plugins_additional_property import ResourceConfigPluginsAdditionalProperty


T = t.TypeVar("T", bound="ResourceConfigPlugins")


@attrs.define
class ResourceConfigPlugins:
    additional_properties: dict[str, ResourceConfigPluginsAdditionalProperty] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.resource_config_plugins_additional_property import (
            ResourceConfigPluginsAdditionalProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        resource_config_plugins = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ResourceConfigPluginsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        resource_config_plugins.additional_properties = additional_properties
        return resource_config_plugins

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ResourceConfigPluginsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ResourceConfigPluginsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
