from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DownloadResponse")


@_attrs_define
class DownloadResponse:
    """
    Attributes:
        archive_size (int):
        include_embedded_videos (bool):  Default: False.
    """

    archive_size: int
    include_embedded_videos: bool = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archive_size = self.archive_size

        include_embedded_videos = self.include_embedded_videos

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archiveSize": archive_size,
                "includeEmbeddedVideos": include_embedded_videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        archive_size = d.pop("archiveSize")

        include_embedded_videos = d.pop("includeEmbeddedVideos")

        download_response = cls(
            archive_size=archive_size,
            include_embedded_videos=include_embedded_videos,
        )

        download_response.additional_properties = d
        return download_response

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
