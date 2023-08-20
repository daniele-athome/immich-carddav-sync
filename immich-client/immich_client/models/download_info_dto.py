from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadInfoDto")


@_attrs_define
class DownloadInfoDto:
    """
    Attributes:
        album_id (Union[Unset, str]):
        archive_size (Union[Unset, int]):
        asset_ids (Union[Unset, List[str]]):
        user_id (Union[Unset, str]):
    """

    album_id: Union[Unset, str] = UNSET
    archive_size: Union[Unset, int] = UNSET
    asset_ids: Union[Unset, List[str]] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_id = self.album_id
        archive_size = self.archive_size
        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if archive_size is not UNSET:
            field_dict["archiveSize"] = archive_size
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_id = d.pop("albumId", UNSET)

        archive_size = d.pop("archiveSize", UNSET)

        asset_ids = cast(List[str], d.pop("assetIds", UNSET))

        user_id = d.pop("userId", UNSET)

        download_info_dto = cls(
            album_id=album_id,
            archive_size=archive_size,
            asset_ids=asset_ids,
            user_id=user_id,
        )

        download_info_dto.additional_properties = d
        return download_info_dto

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
