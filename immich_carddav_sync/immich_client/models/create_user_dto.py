from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserDto")


@_attrs_define
class CreateUserDto:
    """
    Attributes:
        email (str):
        name (str):
        password (str):
        external_path (Union[Unset, None, str]):
        memories_enabled (Union[Unset, bool]):
        storage_label (Union[Unset, None, str]):
    """

    email: str
    name: str
    password: str
    external_path: Union[Unset, None, str] = UNSET
    memories_enabled: Union[Unset, bool] = UNSET
    storage_label: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        name = self.name
        password = self.password
        external_path = self.external_path
        memories_enabled = self.memories_enabled
        storage_label = self.storage_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "name": name,
                "password": password,
            }
        )
        if external_path is not UNSET:
            field_dict["externalPath"] = external_path
        if memories_enabled is not UNSET:
            field_dict["memoriesEnabled"] = memories_enabled
        if storage_label is not UNSET:
            field_dict["storageLabel"] = storage_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        name = d.pop("name")

        password = d.pop("password")

        external_path = d.pop("externalPath", UNSET)

        memories_enabled = d.pop("memoriesEnabled", UNSET)

        storage_label = d.pop("storageLabel", UNSET)

        create_user_dto = cls(
            email=email,
            name=name,
            password=password,
            external_path=external_path,
            memories_enabled=memories_enabled,
            storage_label=storage_label,
        )

        create_user_dto.additional_properties = d
        return create_user_dto

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
