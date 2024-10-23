from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.colorspace import Colorspace

if TYPE_CHECKING:
    from ..models.system_config_generated_image_dto import SystemConfigGeneratedImageDto


T = TypeVar("T", bound="SystemConfigImageDto")


@_attrs_define
class SystemConfigImageDto:
    """
    Attributes:
        colorspace (Colorspace):
        extract_embedded (bool):
        preview (SystemConfigGeneratedImageDto):
        thumbnail (SystemConfigGeneratedImageDto):
    """

    colorspace: Colorspace
    extract_embedded: bool
    preview: "SystemConfigGeneratedImageDto"
    thumbnail: "SystemConfigGeneratedImageDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        colorspace = self.colorspace.value

        extract_embedded = self.extract_embedded

        preview = self.preview.to_dict()

        thumbnail = self.thumbnail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "colorspace": colorspace,
                "extractEmbedded": extract_embedded,
                "preview": preview,
                "thumbnail": thumbnail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_config_generated_image_dto import SystemConfigGeneratedImageDto

        d = src_dict.copy()
        colorspace = Colorspace(d.pop("colorspace"))

        extract_embedded = d.pop("extractEmbedded")

        preview = SystemConfigGeneratedImageDto.from_dict(d.pop("preview"))

        thumbnail = SystemConfigGeneratedImageDto.from_dict(d.pop("thumbnail"))

        system_config_image_dto = cls(
            colorspace=colorspace,
            extract_embedded=extract_embedded,
            preview=preview,
            thumbnail=thumbnail,
        )

        system_config_image_dto.additional_properties = d
        return system_config_image_dto

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
