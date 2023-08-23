from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateProfileImageResponseDto")


@_attrs_define
class CreateProfileImageResponseDto:
    """
    Attributes:
        profile_image_path (str):
        user_id (str):
    """

    profile_image_path: str
    user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_image_path = self.profile_image_path
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileImagePath": profile_image_path,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_image_path = d.pop("profileImagePath")

        user_id = d.pop("userId")

        create_profile_image_response_dto = cls(
            profile_image_path=profile_image_path,
            user_id=user_id,
        )

        create_profile_image_response_dto.additional_properties = d
        return create_profile_image_response_dto

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
