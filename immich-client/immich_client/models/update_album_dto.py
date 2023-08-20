from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlbumDto")


@_attrs_define
class UpdateAlbumDto:
    """
    Attributes:
        album_name (Union[Unset, str]):
        album_thumbnail_asset_id (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    album_name: Union[Unset, str] = UNSET
    album_thumbnail_asset_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_name = self.album_name
        album_thumbnail_asset_id = self.album_thumbnail_asset_id
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if album_name is not UNSET:
            field_dict["albumName"] = album_name
        if album_thumbnail_asset_id is not UNSET:
            field_dict["albumThumbnailAssetId"] = album_thumbnail_asset_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_name = d.pop("albumName", UNSET)

        album_thumbnail_asset_id = d.pop("albumThumbnailAssetId", UNSET)

        description = d.pop("description", UNSET)

        update_album_dto = cls(
            album_name=album_name,
            album_thumbnail_asset_id=album_thumbnail_asset_id,
            description=description,
        )

        update_album_dto.additional_properties = d
        return update_album_dto

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
