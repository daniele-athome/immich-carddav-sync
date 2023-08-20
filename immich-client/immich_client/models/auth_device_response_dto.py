from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthDeviceResponseDto")


@_attrs_define
class AuthDeviceResponseDto:
    """
    Attributes:
        created_at (str):
        current (bool):
        device_os (str):
        device_type (str):
        id (str):
        updated_at (str):
    """

    created_at: str
    current: bool
    device_os: str
    device_type: str
    id: str
    updated_at: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        current = self.current
        device_os = self.device_os
        device_type = self.device_type
        id = self.id
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "current": current,
                "deviceOS": device_os,
                "deviceType": device_type,
                "id": id,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt")

        current = d.pop("current")

        device_os = d.pop("deviceOS")

        device_type = d.pop("deviceType")

        id = d.pop("id")

        updated_at = d.pop("updatedAt")

        auth_device_response_dto = cls(
            created_at=created_at,
            current=current,
            device_os=device_os,
            device_type=device_type,
            id=id,
            updated_at=updated_at,
        )

        auth_device_response_dto.additional_properties = d
        return auth_device_response_dto

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
