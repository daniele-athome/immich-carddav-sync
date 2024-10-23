from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_by_user_dto import UsageByUserDto


T = TypeVar("T", bound="ServerStatsResponseDto")


@_attrs_define
class ServerStatsResponseDto:
    """
    Attributes:
        photos (int):  Default: 0.
        usage (int):  Default: 0.
        usage_by_user (List['UsageByUserDto']):  Example: [{'photos': 1, 'videos': 1, 'diskUsageRaw': 1}].
        videos (int):  Default: 0.
    """

    usage_by_user: List["UsageByUserDto"]
    photos: int = 0
    usage: int = 0
    videos: int = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        photos = self.photos

        usage = self.usage

        usage_by_user = []
        for usage_by_user_item_data in self.usage_by_user:
            usage_by_user_item = usage_by_user_item_data.to_dict()
            usage_by_user.append(usage_by_user_item)

        videos = self.videos

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photos": photos,
                "usage": usage,
                "usageByUser": usage_by_user,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.usage_by_user_dto import UsageByUserDto

        d = src_dict.copy()
        photos = d.pop("photos")

        usage = d.pop("usage")

        usage_by_user = []
        _usage_by_user = d.pop("usageByUser")
        for usage_by_user_item_data in _usage_by_user:
            usage_by_user_item = UsageByUserDto.from_dict(usage_by_user_item_data)

            usage_by_user.append(usage_by_user_item)

        videos = d.pop("videos")

        server_stats_response_dto = cls(
            photos=photos,
            usage=usage,
            usage_by_user=usage_by_user,
            videos=videos,
        )

        server_stats_response_dto.additional_properties = d
        return server_stats_response_dto

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
