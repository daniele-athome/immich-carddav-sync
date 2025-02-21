from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryStatsResponseDto")


@_attrs_define
class LibraryStatsResponseDto:
    """
    Attributes:
        photos (int):  Default: 0.
        total (int):  Default: 0.
        usage (int):  Default: 0.
        videos (int):  Default: 0.
    """

    photos: int = 0
    total: int = 0
    usage: int = 0
    videos: int = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        photos = self.photos

        total = self.total

        usage = self.usage

        videos = self.videos

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photos": photos,
                "total": total,
                "usage": usage,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        photos = d.pop("photos")

        total = d.pop("total")

        usage = d.pop("usage")

        videos = d.pop("videos")

        library_stats_response_dto = cls(
            photos=photos,
            total=total,
            usage=usage,
            videos=videos,
        )

        library_stats_response_dto.additional_properties = d
        return library_stats_response_dto

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
