from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CuratedObjectsResponseDto")


@_attrs_define
class CuratedObjectsResponseDto:
    """
    Attributes:
        device_asset_id (str):
        device_id (str):
        id (str):
        object_ (str):
        resize_path (str):
    """

    device_asset_id: str
    device_id: str
    id: str
    object_: str
    resize_path: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_asset_id = self.device_asset_id
        device_id = self.device_id
        id = self.id
        object_ = self.object_
        resize_path = self.resize_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceAssetId": device_asset_id,
                "deviceId": device_id,
                "id": id,
                "object": object_,
                "resizePath": resize_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_asset_id = d.pop("deviceAssetId")

        device_id = d.pop("deviceId")

        id = d.pop("id")

        object_ = d.pop("object")

        resize_path = d.pop("resizePath")

        curated_objects_response_dto = cls(
            device_asset_id=device_asset_id,
            device_id=device_id,
            id=id,
            object_=object_,
            resize_path=resize_path,
        )

        curated_objects_response_dto.additional_properties = d
        return curated_objects_response_dto

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
