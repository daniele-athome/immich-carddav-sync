from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmailNotificationsResponse")


@_attrs_define
class EmailNotificationsResponse:
    """
    Attributes:
        album_invite (bool):
        album_update (bool):
        enabled (bool):
    """

    album_invite: bool
    album_update: bool
    enabled: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_invite = self.album_invite

        album_update = self.album_update

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumInvite": album_invite,
                "albumUpdate": album_update,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_invite = d.pop("albumInvite")

        album_update = d.pop("albumUpdate")

        enabled = d.pop("enabled")

        email_notifications_response = cls(
            album_invite=album_invite,
            album_update=album_update,
            enabled=enabled,
        )

        email_notifications_response.additional_properties = d
        return email_notifications_response

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
