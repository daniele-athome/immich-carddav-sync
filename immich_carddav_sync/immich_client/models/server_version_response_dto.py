from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerVersionResponseDto")


@_attrs_define
class ServerVersionResponseDto:
    """
    Attributes:
        major (int):
        minor (int):
        patch (int):
    """

    major: int
    minor: int
    patch: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        major = self.major
        minor = self.minor
        patch = self.patch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "major": major,
                "minor": minor,
                "patch": patch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        major = d.pop("major")

        minor = d.pop("minor")

        patch = d.pop("patch")

        server_version_response_dto = cls(
            major=major,
            minor=minor,
            patch=patch,
        )

        server_version_response_dto.additional_properties = d
        return server_version_response_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
