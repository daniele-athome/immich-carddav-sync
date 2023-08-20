from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserDto")


@_attrs_define
class UpdateUserDto:
    """
    Attributes:
        id (str):
        email (Union[Unset, str]):
        external_path (Union[Unset, str]):
        first_name (Union[Unset, str]):
        is_admin (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        memories_enabled (Union[Unset, bool]):
        password (Union[Unset, str]):
        should_change_password (Union[Unset, bool]):
        storage_label (Union[Unset, str]):
    """

    id: str
    email: Union[Unset, str] = UNSET
    external_path: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    memories_enabled: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    should_change_password: Union[Unset, bool] = UNSET
    storage_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        external_path = self.external_path
        first_name = self.first_name
        is_admin = self.is_admin
        last_name = self.last_name
        memories_enabled = self.memories_enabled
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
        if email is not UNSET:
            field_dict["email"] = email
        if external_path is not UNSET:
            field_dict["externalPath"] = external_path
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if memories_enabled is not UNSET:
            field_dict["memoriesEnabled"] = memories_enabled
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

        email = d.pop("email", UNSET)

        external_path = d.pop("externalPath", UNSET)

        first_name = d.pop("firstName", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        last_name = d.pop("lastName", UNSET)

        memories_enabled = d.pop("memoriesEnabled", UNSET)

        password = d.pop("password", UNSET)

        should_change_password = d.pop("shouldChangePassword", UNSET)

        storage_label = d.pop("storageLabel", UNSET)

        update_user_dto = cls(
            id=id,
            email=email,
            external_path=external_path,
            first_name=first_name,
            is_admin=is_admin,
            last_name=last_name,
            memories_enabled=memories_enabled,
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
