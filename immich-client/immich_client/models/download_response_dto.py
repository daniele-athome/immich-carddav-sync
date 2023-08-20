from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.download_archive_info import DownloadArchiveInfo


T = TypeVar("T", bound="DownloadResponseDto")


@_attrs_define
class DownloadResponseDto:
    """
    Attributes:
        archives (List['DownloadArchiveInfo']):
        total_size (int):
    """

    archives: List["DownloadArchiveInfo"]
    total_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archives = []
        for archives_item_data in self.archives:
            archives_item = archives_item_data.to_dict()

            archives.append(archives_item)

        total_size = self.total_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archives": archives,
                "totalSize": total_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.download_archive_info import DownloadArchiveInfo

        d = src_dict.copy()
        archives = []
        _archives = d.pop("archives")
        for archives_item_data in _archives:
            archives_item = DownloadArchiveInfo.from_dict(archives_item_data)

            archives.append(archives_item)

        total_size = d.pop("totalSize")

        download_response_dto = cls(
            archives=archives,
            total_size=total_size,
        )

        download_response_dto.additional_properties = d
        return download_response_dto

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
