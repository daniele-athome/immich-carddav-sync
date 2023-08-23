from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMediaTypesResponseDto")


@_attrs_define
class ServerMediaTypesResponseDto:
    """
    Attributes:
        image (List[str]):
        sidecar (List[str]):
        video (List[str]):
    """

    image: List[str]
    sidecar: List[str]
    video: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image

        sidecar = self.sidecar

        video = self.video

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "sidecar": sidecar,
                "video": video,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image = cast(List[str], d.pop("image"))

        sidecar = cast(List[str], d.pop("sidecar"))

        video = cast(List[str], d.pop("video"))

        server_media_types_response_dto = cls(
            image=image,
            sidecar=sidecar,
            video=video,
        )

        server_media_types_response_dto.additional_properties = d
        return server_media_types_response_dto

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
