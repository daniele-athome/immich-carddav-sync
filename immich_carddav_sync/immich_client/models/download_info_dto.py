from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadInfoDto")


@_attrs_define
class DownloadInfoDto:
    """
    Attributes:
        album_id (Union[Unset, UUID]):
        archive_size (Union[Unset, int]):
        asset_ids (Union[Unset, List[UUID]]):
        user_id (Union[Unset, UUID]):
    """

    album_id: Union[Unset, UUID] = UNSET
    archive_size: Union[Unset, int] = UNSET
    asset_ids: Union[Unset, List[UUID]] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_id: Union[Unset, str] = UNSET
        if not isinstance(self.album_id, Unset):
            album_id = str(self.album_id)

        archive_size = self.archive_size

        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = []
            for asset_ids_item_data in self.asset_ids:
                asset_ids_item = str(asset_ids_item_data)
                asset_ids.append(asset_ids_item)

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

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
        _album_id = d.pop("albumId", UNSET)
        album_id: Union[Unset, UUID]
        if isinstance(_album_id, Unset):
            album_id = UNSET
        else:
            album_id = UUID(_album_id)

        archive_size = d.pop("archiveSize", UNSET)

        asset_ids = []
        _asset_ids = d.pop("assetIds", UNSET)
        for asset_ids_item_data in _asset_ids or []:
            asset_ids_item = UUID(asset_ids_item_data)

            asset_ids.append(asset_ids_item)

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

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
