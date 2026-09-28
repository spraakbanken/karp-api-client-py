"""Query Response."""

import typing as t

import attrs

from karp_red_api_client.models.entry_dto import EntryDto


@attrs.define
class QueryResponse:
    """Response returned from query."""

    total: int
    hits: list["EntryDto"]
    distribution: dict[str, int] | None
    additional_properties: dict[str, t.Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, t.Any]:
        """Serialize to dict."""
        hits = [entry.to_dict() for entry in self.hits]

        field_dict: dict[str, t.Any] = {
            "total": self.total,
            "distibution": self.distribution,
        }
        field_dict.update(self.additional_properties)

        field_dict.update(
            {
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: dict[str, t.Any]) -> t.Self:
        """Deserialize from dict."""
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
