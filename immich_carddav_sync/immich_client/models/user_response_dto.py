import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_avatar_color import UserAvatarColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponseDto")


@_attrs_define
class UserResponseDto:
    """
    Attributes:
        avatar_color (UserAvatarColor):
        created_at (datetime.datetime):
        email (str):
        id (str):
        is_admin (bool):
        name (str):
        oauth_id (str):
        profile_image_path (str):
        should_change_password (bool):
        updated_at (datetime.datetime):
        deleted_at (Optional[datetime.datetime]):
        external_path (Optional[str]):
        memories_enabled (Union[Unset, bool]):
        storage_label (Optional[str]):
    """

    avatar_color: UserAvatarColor
    created_at: datetime.datetime
    email: str
    id: str
    is_admin: bool
    name: str
    oauth_id: str
    profile_image_path: str
    should_change_password: bool
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]
    external_path: Optional[str]
    storage_label: Optional[str]
    memories_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_color = self.avatar_color.value

        created_at = self.created_at.isoformat()

        email = self.email
        id = self.id
        is_admin = self.is_admin
        name = self.name
        oauth_id = self.oauth_id
        profile_image_path = self.profile_image_path
        should_change_password = self.should_change_password
        updated_at = self.updated_at.isoformat()

        deleted_at = self.deleted_at.isoformat() if self.deleted_at else None

        external_path = self.external_path
        memories_enabled = self.memories_enabled
        storage_label = self.storage_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatarColor": avatar_color,
                "createdAt": created_at,
                "email": email,
                "id": id,
                "isAdmin": is_admin,
                "name": name,
                "oauthId": oauth_id,
                "profileImagePath": profile_image_path,
                "shouldChangePassword": should_change_password,
                "updatedAt": updated_at,
                "deletedAt": deleted_at,
                "externalPath": external_path,
                "storageLabel": storage_label,
            }
        )
        if memories_enabled is not UNSET:
            field_dict["memoriesEnabled"] = memories_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar_color = UserAvatarColor(d.pop("avatarColor"))

        created_at = isoparse(d.pop("createdAt"))

        email = d.pop("email")

        id = d.pop("id")

        is_admin = d.pop("isAdmin")

        name = d.pop("name")

        oauth_id = d.pop("oauthId")

        profile_image_path = d.pop("profileImagePath")

        should_change_password = d.pop("shouldChangePassword")

        updated_at = isoparse(d.pop("updatedAt"))

        _deleted_at = d.pop("deletedAt")
        deleted_at: Optional[datetime.datetime]
        if _deleted_at is None:
            deleted_at = None
        else:
            deleted_at = isoparse(_deleted_at)

        external_path = d.pop("externalPath")

        memories_enabled = d.pop("memoriesEnabled", UNSET)

        storage_label = d.pop("storageLabel")

        user_response_dto = cls(
            avatar_color=avatar_color,
            created_at=created_at,
            email=email,
            id=id,
            is_admin=is_admin,
            name=name,
            oauth_id=oauth_id,
            profile_image_path=profile_image_path,
            should_change_password=should_change_password,
            updated_at=updated_at,
            deleted_at=deleted_at,
            external_path=external_path,
            memories_enabled=memories_enabled,
            storage_label=storage_label,
        )

        user_response_dto.additional_properties = d
        return user_response_dto

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
