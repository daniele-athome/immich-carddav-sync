from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAdminCreateDto")


@_attrs_define
class UserAdminCreateDto:
    """
    Attributes:
        email (str):
        name (str):
        password (str):
        notify (Union[Unset, bool]):
        quota_size_in_bytes (Union[None, Unset, int]):
        should_change_password (Union[Unset, bool]):
        storage_label (Union[None, Unset, str]):
    """

    email: str
    name: str
    password: str
    notify: Union[Unset, bool] = UNSET
    quota_size_in_bytes: Union[None, Unset, int] = UNSET
    should_change_password: Union[Unset, bool] = UNSET
    storage_label: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        name = self.name

        password = self.password

        notify = self.notify

        quota_size_in_bytes: Union[None, Unset, int]
        if isinstance(self.quota_size_in_bytes, Unset):
            quota_size_in_bytes = UNSET
        else:
            quota_size_in_bytes = self.quota_size_in_bytes

        should_change_password = self.should_change_password

        storage_label: Union[None, Unset, str]
        if isinstance(self.storage_label, Unset):
            storage_label = UNSET
        else:
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
        if notify is not UNSET:
            field_dict["notify"] = notify
        if quota_size_in_bytes is not UNSET:
            field_dict["quotaSizeInBytes"] = quota_size_in_bytes
        if should_change_password is not UNSET:
            field_dict["shouldChangePassword"] = should_change_password
        if storage_label is not UNSET:
            field_dict["storageLabel"] = storage_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        name = d.pop("name")

        password = d.pop("password")

        notify = d.pop("notify", UNSET)

        def _parse_quota_size_in_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quota_size_in_bytes = _parse_quota_size_in_bytes(d.pop("quotaSizeInBytes", UNSET))

        should_change_password = d.pop("shouldChangePassword", UNSET)

        def _parse_storage_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        storage_label = _parse_storage_label(d.pop("storageLabel", UNSET))

        user_admin_create_dto = cls(
            email=email,
            name=name,
            password=password,
            notify=notify,
            quota_size_in_bytes=quota_size_in_bytes,
            should_change_password=should_change_password,
            storage_label=storage_label,
        )

        user_admin_create_dto.additional_properties = d
        return user_admin_create_dto

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
