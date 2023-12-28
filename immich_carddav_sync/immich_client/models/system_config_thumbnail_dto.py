from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.colorspace import Colorspace

T = TypeVar("T", bound="SystemConfigThumbnailDto")


@_attrs_define
class SystemConfigThumbnailDto:
    """
    Attributes:
        colorspace (Colorspace):
        jpeg_size (int):
        quality (int):
        webp_size (int):
    """

    colorspace: Colorspace
    jpeg_size: int
    quality: int
    webp_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        colorspace = self.colorspace.value

        jpeg_size = self.jpeg_size
        quality = self.quality
        webp_size = self.webp_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "colorspace": colorspace,
                "jpegSize": jpeg_size,
                "quality": quality,
                "webpSize": webp_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        colorspace = Colorspace(d.pop("colorspace"))

        jpeg_size = d.pop("jpegSize")

        quality = d.pop("quality")

        webp_size = d.pop("webpSize")

        system_config_thumbnail_dto = cls(
            colorspace=colorspace,
            jpeg_size=jpeg_size,
            quality=quality,
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
