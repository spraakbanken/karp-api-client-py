from __future__ import annotations

import typing as t
from collections.abc import Mapping
from typing import Any

import attrs

if t.TYPE_CHECKING:
    from ..models.hit_response import HitResponse
    from ..models.search_result_resourcehits import SearchResultResourcehits


T = t.TypeVar("T", bound="SearchResult")


@attrs.define
class SearchResult:
    """
    Attributes:
        hits (list[HitResponse]):
        resource_hits (SearchResultResourcehits):
        resource_order (list[str]):
        total (int):
    """

    hits: list[HitResponse]
    resource_hits: SearchResultResourcehits
    resource_order: list[str]
    total: int
    additional_properties: dict[str, Any] = attrs.field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        resource_hits = self.resource_hits.to_dict()

        resource_order = self.resource_order

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hits": hits,
                "resourceHits": resource_hits,
                "resourceOrder": resource_order,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> t.Self:
        from ..models.hit_response import HitResponse  # noqa: PLC0415
        from ..models.search_result_resourcehits import SearchResultResourcehits  # noqa: PLC0415

        d = dict(src_dict)
        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = HitResponse.from_dict(hits_item_data)

            hits.append(hits_item)

        resource_hits = SearchResultResourcehits.from_dict(d.pop("resourceHits"))

        resource_order = t.cast(list[str], d.pop("resourceOrder"))

        total = d.pop("total")

        search_result = cls(
            hits=hits,
            resource_hits=resource_hits,
            resource_order=resource_order,
            total=total,
        )

        search_result.additional_properties = d
        return search_result

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
