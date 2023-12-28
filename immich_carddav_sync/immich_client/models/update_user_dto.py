from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_avatar_color import UserAvatarColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserDto")


@_attrs_define
class UpdateUserDto:
    """
    Attributes:
        id (str):
        avatar_color (Union[Unset, UserAvatarColor]):
        email (Union[Unset, str]):
        external_path (Union[Unset, str]):
        is_admin (Union[Unset, bool]):
        memories_enabled (Union[Unset, bool]):
        name (Union[Unset, str]):
        password (Union[Unset, str]):
        should_change_password (Union[Unset, bool]):
        storage_label (Union[Unset, str]):
    """

    id: str
    avatar_color: Union[Unset, UserAvatarColor] = UNSET
    email: Union[Unset, str] = UNSET
    external_path: Union[Unset, str] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    memories_enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    should_change_password: Union[Unset, bool] = UNSET
    storage_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        avatar_color: Union[Unset, str] = UNSET
        if not isinstance(self.avatar_color, Unset):
            avatar_color = self.avatar_color.value

        email = self.email
        external_path = self.external_path
        is_admin = self.is_admin
        memories_enabled = self.memories_enabled
        name = self.name
        password = self.password
        should_change_password = self.should_change_password
        storage_label = self.storage_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if avatar_color is not UNSET:
            field_dict["avatarColor"] = avatar_color
        if email is not UNSET:
            field_dict["email"] = email
        if external_path is not UNSET:
            field_dict["externalPath"] = external_path
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if memories_enabled is not UNSET:
            field_dict["memoriesEnabled"] = memories_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if should_change_password is not UNSET:
            field_dict["shouldChangePassword"] = should_change_password
        if storage_label is not UNSET:
            field_dict["storageLabel"] = storage_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _avatar_color = d.pop("avatarColor", UNSET)
        avatar_color: Union[Unset, UserAvatarColor]
        if isinstance(_avatar_color, Unset):
            avatar_color = UNSET
        else:
            avatar_color = UserAvatarColor(_avatar_color)

        email = d.pop("email", UNSET)

        external_path = d.pop("externalPath", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        memories_enabled = d.pop("memoriesEnabled", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        should_change_password = d.pop("shouldChangePassword", UNSET)

        storage_label = d.pop("storageLabel", UNSET)

        update_user_dto = cls(
            id=id,
            avatar_color=avatar_color,
            email=email,
            external_path=external_path,
            is_admin=is_admin,
            memories_enabled=memories_enabled,
            name=name,
            password=password,
            should_change_password=should_change_password,
            storage_label=storage_label,
        )

        update_user_dto.additional_properties = d
        return update_user_dto

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
