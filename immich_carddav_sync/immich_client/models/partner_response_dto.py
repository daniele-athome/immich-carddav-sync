import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_avatar_color import UserAvatarColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerResponseDto")


@_attrs_define
class PartnerResponseDto:
    """
    Attributes:
        avatar_color (UserAvatarColor):
        email (str):
        id (str):
        name (str):
        profile_changed_at (datetime.datetime):
        profile_image_path (str):
        in_timeline (Union[Unset, bool]):
    """

    avatar_color: UserAvatarColor
    email: str
    id: str
    name: str
    profile_changed_at: datetime.datetime
    profile_image_path: str
    in_timeline: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_color = self.avatar_color.value

        email = self.email

        id = self.id

        name = self.name

        profile_changed_at = self.profile_changed_at.isoformat()

        profile_image_path = self.profile_image_path

        in_timeline = self.in_timeline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatarColor": avatar_color,
                "email": email,
                "id": id,
                "name": name,
                "profileChangedAt": profile_changed_at,
                "profileImagePath": profile_image_path,
            }
        )
        if in_timeline is not UNSET:
            field_dict["inTimeline"] = in_timeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar_color = UserAvatarColor(d.pop("avatarColor"))

        email = d.pop("email")

        id = d.pop("id")

        name = d.pop("name")

        profile_changed_at = isoparse(d.pop("profileChangedAt"))

        profile_image_path = d.pop("profileImagePath")

        in_timeline = d.pop("inTimeline", UNSET)

        partner_response_dto = cls(
            avatar_color=avatar_color,
            email=email,
            id=id,
            name=name,
            profile_changed_at=profile_changed_at,
            profile_image_path=profile_image_path,
            in_timeline=in_timeline,
        )

        partner_response_dto.additional_properties = d
        return partner_response_dto

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
