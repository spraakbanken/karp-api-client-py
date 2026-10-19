from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

from ..types import UNSET, Unset

if t.TYPE_CHECKING:
    from ..models.field_fieldparams import FieldFieldparams
    from ..models.field_fields_type_0 import FieldFieldsType0
    from ..models.field_label_type_0 import FieldLabelType0
    from ..models.field_params import FieldParams


T = t.TypeVar("T", bound="Field")


@attrs.define
class Field:
    """
    Attributes:
        type_ (None | str | Unset):
        required (bool | Unset):  Default: False.
        collection (bool | Unset):  Default: False.
        store (bool | Unset):  Default: True.
        virtual (bool | Unset):  Default: False.
        plugin (None | str | Unset):
        params (FieldParams | Unset):
        field_params (FieldFieldparams | Unset):
        fields (FieldFieldsType0 | None | Unset):
        hidden (bool | Unset):  Default: False.
        flatten_params (bool | Unset):  Default: False.
        allow_missing_params (bool | Unset):  Default: False.
        cache_plugin_expansion (bool | Unset):  Default: True.
        searchable (bool | Unset):  Default: True.
        skip_raw (bool | None | Unset):  Default: False.
        additional_properties (bool | Unset):  Default: True.
        label (FieldLabelType0 | None | str | Unset):
    """

    type_: None | str | Unset = UNSET
    required: bool | Unset = False
    collection: bool | Unset = False
    store: bool | Unset = True
    virtual: bool | Unset = False
    plugin: None | str | Unset = UNSET
    params: FieldParams | Unset = UNSET
    field_params: FieldFieldparams | Unset = UNSET
    fields: FieldFieldsType0 | None | Unset = UNSET
    hidden: bool | Unset = False
    flatten_params: bool | Unset = False
    allow_missing_params: bool | Unset = False
    cache_plugin_expansion: bool | Unset = True
    searchable: bool | Unset = True
    skip_raw: bool | None | Unset = False
    additional_properties: bool | Unset = True
    label: FieldLabelType0 | None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_fields_type_0 import FieldFieldsType0  # noqa: PLC0415
        from ..models.field_label_type_0 import FieldLabelType0  # noqa: PLC0415

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        required = self.required

        collection = self.collection

        store = self.store

        virtual = self.virtual

        plugin: None | str | Unset
        if isinstance(self.plugin, Unset):
            plugin = UNSET
        else:
            plugin = self.plugin

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_params, Unset):
            field_params = self.field_params.to_dict()

        fields: dict[str, Any] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, FieldFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        hidden = self.hidden

        flatten_params = self.flatten_params

        allow_missing_params = self.allow_missing_params

        cache_plugin_expansion = self.cache_plugin_expansion

        searchable = self.searchable

        skip_raw: bool | None | Unset
        if isinstance(self.skip_raw, Unset):
            skip_raw = UNSET
        else:
            skip_raw = self.skip_raw

        additional_properties = self.additional_properties

        label: dict[str, Any] | None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, FieldLabelType0):
            label = self.label.to_dict()
        else:
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if collection is not UNSET:
            field_dict["collection"] = collection
        if store is not UNSET:
            field_dict["store"] = store
        if virtual is not UNSET:
            field_dict["virtual"] = virtual
        if plugin is not UNSET:
            field_dict["plugin"] = plugin
        if params is not UNSET:
            field_dict["params"] = params
        if field_params is not UNSET:
            field_dict["fieldParams"] = field_params
        if fields is not UNSET:
            field_dict["fields"] = fields
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if flatten_params is not UNSET:
            field_dict["flattenParams"] = flatten_params
        if allow_missing_params is not UNSET:
            field_dict["allowMissingParams"] = allow_missing_params
        if cache_plugin_expansion is not UNSET:
            field_dict["cachePluginExpansion"] = cache_plugin_expansion
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if skip_raw is not UNSET:
            field_dict["skipRaw"] = skip_raw
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.field_fieldparams import FieldFieldparams  # noqa: PLC0415
        from ..models.field_fields_type_0 import FieldFieldsType0  # noqa: PLC0415
        from ..models.field_label_type_0 import FieldLabelType0  # noqa: PLC0415
        from ..models.field_params import FieldParams  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        required = d.pop("required", UNSET)

        collection = d.pop("collection", UNSET)

        store = d.pop("store", UNSET)

        virtual = d.pop("virtual", UNSET)

        def _parse_plugin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(None | str | Unset, data)

        plugin = _parse_plugin(d.pop("plugin", UNSET))

        _params = d.pop("params", UNSET)
        params: FieldParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = FieldParams.from_dict(_params)

        _field_params = d.pop("fieldParams", UNSET)
        field_params: FieldFieldparams | Unset
        if isinstance(_field_params, Unset):
            field_params = UNSET
        else:
            field_params = FieldFieldparams.from_dict(_field_params)

        def _parse_fields(data: object) -> FieldFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = FieldFieldsType0.from_dict(data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(FieldFieldsType0 | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        hidden = d.pop("hidden", UNSET)

        flatten_params = d.pop("flattenParams", UNSET)

        allow_missing_params = d.pop("allowMissingParams", UNSET)

        cache_plugin_expansion = d.pop("cachePluginExpansion", UNSET)

        searchable = d.pop("searchable", UNSET)

        def _parse_skip_raw(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return t.cast(bool | None | Unset, data)

        skip_raw = _parse_skip_raw(d.pop("skipRaw", UNSET))

        additional_properties = d.pop("additionalProperties", UNSET)

        def _parse_label(data: object) -> FieldLabelType0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                label_type_0 = FieldLabelType0.from_dict(data)

                return label_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return t.cast(FieldLabelType0 | None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        field = cls(
            type_=type_,
            required=required,
            collection=collection,
            store=store,
            virtual=virtual,
            plugin=plugin,
            params=params,
            field_params=field_params,
            fields=fields,
            hidden=hidden,
            flatten_params=flatten_params,
            allow_missing_params=allow_missing_params,
            cache_plugin_expansion=cache_plugin_expansion,
            searchable=searchable,
            skip_raw=skip_raw,
            additional_properties=additional_properties,
            label=label,
        )

        return field
