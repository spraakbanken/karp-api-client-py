"""SearchEntryDto model."""

import typing as t

import attrs
from karp_api_core.models import mixins


@attrs.define
class HitEntryDto(mixins.WithAdditionalProperties):
    """Entry for HitDto.entry."""


@attrs.define
class HitDto:
    """HitDto.

    Attributes:
    resourceId (str):
    entry (HitEntryDto):
    """

    resource_id: str = attrs.field(alias="resourceId")
    entry: HitEntryDto
    additional_properties: dict[str, t.Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, t.Any]:
        """Serialize this object to dict."""
        resource_id = self.resource_id

        entry = self.entry.to_dict()

        field_dict: dict[str, t.Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: dict[str, t.Any]) -> t.Self:
        """Deserialize from dict."""
        d = src_dict.copy()

        resource_id = d.pop("resourceId", None)

        if resource_id is None:
            resource_id = d.pop("resource_id")

        entry = HitEntryDto.from_dict(d.pop("entry"))

        entry_dto = cls(
            resourceId=resource_id,
            entry=entry,
        )

        entry_dto.additional_properties = d
        return entry_dto

    @property
    def additional_keys(self) -> list[str]:
        """Return any additional keys."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> t.Any:
        """Get an additional property by key."""
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: t.Any) -> None:
        """Set an additional property."""
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        """Delete an additional property."""
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        """Check if this object contains an additional propery 'key'."""
        return key in self.additional_properties
