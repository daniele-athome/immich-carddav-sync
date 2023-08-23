from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageByUserDto")


@_attrs_define
class UsageByUserDto:
    """
    Attributes:
        photos (int):
        usage (int):
        user_first_name (str):
        user_id (str):
        user_last_name (str):
        videos (int):
    """

    photos: int
    usage: int
    user_first_name: str
    user_id: str
    user_last_name: str
    videos: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        photos = self.photos
        usage = self.usage
        user_first_name = self.user_first_name
        user_id = self.user_id
        user_last_name = self.user_last_name
        videos = self.videos

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photos": photos,
                "usage": usage,
                "userFirstName": user_first_name,
                "userId": user_id,
                "userLastName": user_last_name,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        photos = d.pop("photos")

        usage = d.pop("usage")

        user_first_name = d.pop("userFirstName")

        user_id = d.pop("userId")

        user_last_name = d.pop("userLastName")

        videos = d.pop("videos")

        usage_by_user_dto = cls(
            photos=photos,
            usage=usage,
            user_first_name=user_first_name,
            user_id=user_id,
            user_last_name=user_last_name,
            videos=videos,
        )

        usage_by_user_dto.additional_properties = d
        return usage_by_user_dto

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
