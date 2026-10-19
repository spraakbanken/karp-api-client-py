from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.query_stats_response_distribution import QueryStatsResponseDistribution


T = t.TypeVar("T", bound="QueryStatsResponse")


@attrs.define
class QueryStatsResponse:
    """
    Attributes:
        total (int):
        distribution (QueryStatsResponseDistribution):
    """

    total: int
    distribution: QueryStatsResponseDistribution
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        distribution = self.distribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "distribution": distribution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.query_stats_response_distribution import QueryStatsResponseDistribution  # noqa: PLC0415

        d = dict(src_dict)
        total = d.pop("total")

        distribution = QueryStatsResponseDistribution.from_dict(d.pop("distribution"))

        query_stats_response = cls(
            total=total,
            distribution=distribution,
        )

        query_stats_response.additional_properties = d
        return query_stats_response

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
