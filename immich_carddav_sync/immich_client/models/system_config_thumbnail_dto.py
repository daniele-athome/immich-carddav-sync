from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemConfigThumbnailDto")


@_attrs_define
class SystemConfigThumbnailDto:
    """
    Attributes:
        jpeg_size (int):
        webp_size (int):
    """

    jpeg_size: int
    webp_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jpeg_size = self.jpeg_size
        webp_size = self.webp_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jpegSize": jpeg_size,
                "webpSize": webp_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        jpeg_size = d.pop("jpegSize")

        webp_size = d.pop("webpSize")

        system_config_thumbnail_dto = cls(
            jpeg_size=jpeg_size,
            webp_size=webp_size,
        )

        system_config_thumbnail_dto.additional_properties = d
        return system_config_thumbnail_dto

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
