"""Http Validation Error."""

import typing as t

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from karp_api_client.shared import UNSET, Unset

if t.TYPE_CHECKING:
    from karp_api_client.models.validation_error import ValidationError


T = t.TypeVar("T", bound="HttpValidationError")


@_attrs_define
class HttpValidationError:
    """Http Validation Error.

    Attributes:
    detail (Union[Unset, list['ValidationError']]):
    """

    detail: Unset | list["ValidationError"] = UNSET
    additional_properties: dict[str, t.Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, t.Any]:
        """Serizalize this entity to dict."""
        detail: Unset | list[dict[str, t.Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = []
            for detail_item_data in self.detail:
                detail_item = detail_item_data.to_dict()
                detail.append(detail_item)

        field_dict: dict[str, t.Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, t.Any]) -> T:
        """Deserialize from dict."""
        from karp_api_client.models.validation_error import ValidationError  # noqa: PLC0415

        d = src_dict.copy()
        detail = []
        detail_ = d.pop("detail", UNSET)
        for detail_item_data in detail_ or []:
            detail_item = ValidationError.from_dict(detail_item_data)

            detail.append(detail_item)

        http_validation_error = cls(
            detail=detail,
        )

        http_validation_error.additional_properties = d
        return http_validation_error

    @property
    def additional_keys(self) -> list[str]:
        """List of t.any additional keys."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> t.Any:
        """Get an addtional property."""
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: t.Any) -> None:
        """Set additional property by 'key'."""
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        """Delete additional property."""
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        """Check if additional property includes 'key'."""
        return key in self.additional_properties
