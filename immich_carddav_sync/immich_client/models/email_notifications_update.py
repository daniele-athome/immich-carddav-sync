from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailNotificationsUpdate")


@_attrs_define
class EmailNotificationsUpdate:
    """
    Attributes:
        album_invite (Union[Unset, bool]):
        album_update (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
    """

    album_invite: Union[Unset, bool] = UNSET
    album_update: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_invite = self.album_invite

        album_update = self.album_update

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if album_invite is not UNSET:
            field_dict["albumInvite"] = album_invite
        if album_update is not UNSET:
            field_dict["albumUpdate"] = album_update
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_invite = d.pop("albumInvite", UNSET)

        album_update = d.pop("albumUpdate", UNSET)

        enabled = d.pop("enabled", UNSET)

        email_notifications_update = cls(
            album_invite=album_invite,
            album_update=album_update,
            enabled=enabled,
        )

        email_notifications_update.additional_properties = d
        return email_notifications_update

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
