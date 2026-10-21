from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.resource_config_fields import ResourceConfigFields
    from ..models.resource_config_plugins import ResourceConfigPlugins
    from ..models.resource_config_protected_type_1 import ResourceConfigProtectedType1


T = t.TypeVar("T", bound="ResourceConfig")


@attrs.define
class ResourceConfig:
    """
    Attributes:
        resource_id (str):
        fields (ResourceConfigFields):
        config_str (str):
        resource_name (None | str | Unset):
        plugins (ResourceConfigPlugins | Unset):
        sort (list[str] | None | str | Unset):
        protected (bool | ResourceConfigProtectedType1 | Unset):  Default: False.
        protected_metadata (bool | Unset):  Default: False.
        id (None | str | Unset):
        additional_properties (bool | Unset):  Default: True.
    """

    resource_id: str
    fields: ResourceConfigFields
    config_str: str
    resource_name: None | str | Unset = UNSET
    plugins: ResourceConfigPlugins | Unset = UNSET
    sort: list[str] | None | str | Unset = UNSET
    protected: bool | ResourceConfigProtectedType1 | Unset = False
    protected_metadata: bool | Unset = False
    id: None | str | Unset = UNSET
    additional_properties: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_config_protected_type_1 import ResourceConfigProtectedType1  # noqa: PLC0415

        resource_id = self.resource_id

        fields = self.fields.to_dict()

        config_str = self.config_str

        resource_name: None | str | Unset
        if isinstance(self.resource_name, Unset):
            resource_name = UNSET
        else:
            resource_name = self.resource_name

        plugins: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins.to_dict()

        sort: list[str] | None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, list):
            sort = self.sort

        else:
            sort = self.sort

        protected: bool | dict[str, Any] | Unset
        if isinstance(self.protected, Unset):
            protected = UNSET
        elif isinstance(self.protected, ResourceConfigProtectedType1):
            protected = self.protected.to_dict()
        else:
            protected = self.protected

        protected_metadata = self.protected_metadata

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        additional_properties = self.additional_properties

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceId": resource_id,
                "fields": fields,
                "configStr": config_str,
            }
        )
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if sort is not UNSET:
            field_dict["sort"] = sort
        if protected is not UNSET:
            field_dict["protected"] = protected
        if protected_metadata is not UNSET:
            field_dict["protectedMetadata"] = protected_metadata
        if id is not UNSET:
            field_dict["id"] = id
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.resource_config_fields import ResourceConfigFields  # noqa: PLC0415
        from ..models.resource_config_plugins import ResourceConfigPlugins  # noqa: PLC0415
        from ..models.resource_config_protected_type_1 import ResourceConfigProtectedType1  # noqa: PLC0415

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        fields = ResourceConfigFields.from_dict(d.pop("fields"))

        config_str = d.pop("configStr")

        def _parse_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        resource_name = _parse_resource_name(d.pop("resourceName", UNSET))

        _plugins = d.pop("plugins", UNSET)
        plugins: ResourceConfigPlugins | Unset
        if isinstance(_plugins, Unset):
            plugins = UNSET
        else:
            plugins = ResourceConfigPlugins.from_dict(_plugins)

        def _parse_sort(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_type_1 = t.cast(list[str], data)

                return sort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(list[str] | None | str | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_protected(data: object) -> bool | ResourceConfigProtectedType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                protected_type_1 = ResourceConfigProtectedType1.from_dict(data)

                return protected_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(bool | ResourceConfigProtectedType1 | Unset, data)

        protected = _parse_protected(d.pop("protected", UNSET))

        protected_metadata = d.pop("protectedMetadata", UNSET)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        additional_properties = d.pop("additionalProperties", UNSET)

        resource_config = cls(
            resource_id=resource_id,
            fields=fields,
            config_str=config_str,
            resource_name=resource_name,
            plugins=plugins,
            sort=sort,
            protected=protected,
            protected_metadata=protected_metadata,
            id=id,
            additional_properties=additional_properties,
        )

        return resource_config
