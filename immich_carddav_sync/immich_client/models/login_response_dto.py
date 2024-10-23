from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginResponseDto")


@_attrs_define
class LoginResponseDto:
    """
    Attributes:
        access_token (str):
        is_admin (bool):
        name (str):
        profile_image_path (str):
        should_change_password (bool):
        user_email (str):
        user_id (str):
    """

    access_token: str
    is_admin: bool
    name: str
    profile_image_path: str
    should_change_password: bool
    user_email: str
    user_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        is_admin = self.is_admin

        name = self.name

        profile_image_path = self.profile_image_path

        should_change_password = self.should_change_password

        user_email = self.user_email

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessToken": access_token,
                "isAdmin": is_admin,
                "name": name,
                "profileImagePath": profile_image_path,
                "shouldChangePassword": should_change_password,
                "userEmail": user_email,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("accessToken")

        is_admin = d.pop("isAdmin")

        name = d.pop("name")

        profile_image_path = d.pop("profileImagePath")

        should_change_password = d.pop("shouldChangePassword")

        user_email = d.pop("userEmail")

        user_id = d.pop("userId")

        login_response_dto = cls(
            access_token=access_token,
            is_admin=is_admin,
            name=name,
            profile_image_path=profile_image_path,
            should_change_password=should_change_password,
            user_email=user_email,
            user_id=user_id,
        )

        login_response_dto.additional_properties = d
        return login_response_dto

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
