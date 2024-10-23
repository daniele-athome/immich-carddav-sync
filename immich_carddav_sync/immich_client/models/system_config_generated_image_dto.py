from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_format import ImageFormat

T = TypeVar("T", bound="SystemConfigGeneratedImageDto")


@_attrs_define
class SystemConfigGeneratedImageDto:
    """
    Attributes:
        format_ (ImageFormat):
        quality (int):
        size (int):
    """

    format_: ImageFormat
    quality: int
    size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_.value

        quality = self.quality

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "quality": quality,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = ImageFormat(d.pop("format"))

        quality = d.pop("quality")

        size = d.pop("size")

        system_config_generated_image_dto = cls(
            format_=format_,
            quality=quality,
            size=size,
        )

        system_config_generated_image_dto.additional_properties = d
        return system_config_generated_image_dto

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
