"""Search Response."""

import typing as t

import attrs

from karp_api_client.models.shared import WithAdditionalProperties

if t.TYPE_CHECKING:
    from karp_api_client.models.search.hit_entry_dto import HitEntryDto

T = t.TypeVar("T", bound="SearchResponse")


@attrs.define
class ResourceHits(WithAdditionalProperties):
    """ResourceHits."""


@attrs.define
class SearchResponse:
    """Response returned from query."""

    hits: list["HitEntryDto"]
    resource_hits: ResourceHits
    resource_order: list[str] = attrs.field(alias="resourceOrder")
    total: int
    additional_properties: dict[str, t.Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, t.Any]:
        """Serialize to dict."""
        hits = [entry.to_dict() for entry in self.hits]

        field_dict: dict[str, t.Any] = {
            "hits": hits,
            "total": self.total,
            "resourceOrder": self.resource_order,
            "resourceHits": self.resource_hits.to_dict(),
        }
        field_dict.update(self.additional_properties)

        field_dict.update(
            {
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, t.Any]) -> T:
        """Deserialize from dict."""
        from karp_api_client.models.red.entry_dto import EntryDto  # noqa: PLC0415

        d = src_dict.copy()
        hits = [EntryDto.from_dict(entry) for entry in d.pop("hits")]
        total = d.pop("total")
        distribution = d.pop("distribution")

        query_response = cls(
            total=total,
            hits=hits,
            distribution=distribution,
        )

        query_response.additional_properties = d
        return query_response

    @property
    def additional_keys(self) -> list[str]:
        """Get additional property keys."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> t.Any:
        """Get an additional property by 'key'."""
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: t.Any) -> None:
        """Set an additional property by 'key'."""
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        """Delete an additional property by 'key'."""
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        """Check if additional properties contains 'key'."""
        return key in self.additional_properties
