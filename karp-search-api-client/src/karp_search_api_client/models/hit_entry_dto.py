"""SearchEntryDto model."""

import typing as t

import attrs:w
from attrs import define as _attrs_define
from attrs import field as _attrs_field

from karp_api_client.shared import UNSET, Unset

if t.TYPE_CHECKING:
    from karp_api_client.models.red.entry_dto_entry import EntryDtoEntry


T = t.TypeVar("T", bound="EntryDto")

@attrs.define
class HitEntryDto:
    """Entry for HitDto.entry."""

    additional_properties: dict[str, t.Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, t.Any]:
        """Serialize as dict."""
        field_dict: dict[str, t.Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, t.Any]) -> T:
        """Deserialize from dict."""
        d = src_dict.copy()
        hit_entry_dto = cls()

        hit_entry_dto.additional_properties = d
        return hit_entry_dto

    @property
    def additional_keys(self) -> list[str]:
        """Get keys of additional properties."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> t.Any:
        """Get additional property by 'key'."""
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: t.Any) -> None:
        """Set additional property by 'key'."""
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        """Delete additional property by 'key'."""
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        """Check if additional properties contains 'key'."""
        return key in self.additional_properties

    def get(self, key: str, default=None) -> t.Any | None:  # noqa: ANN001
        """Look up additional property by 'key' and fall back to default if not present."""
        try:
            return self.additional_properties[key]
        except KeyError:
            return default

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
    def from_dict(cls: type[T], src_dict: dict[str, t.Any]) -> T:
        """Deserialize from dict."""

        d = src_dict.copy()

        resource_id = d.pop("resourceId", None)

        if resource_id is None:
            resource_id = d.pop("resource_id")

        entry = HitEntryDto.from_dict(d.pop("entry"))



        entry_dto = cls(
            resource_id=resource_id,
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
