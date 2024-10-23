from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_order import AssetOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlbumDto")


@_attrs_define
class UpdateAlbumDto:
    """
    Attributes:
        album_name (Union[Unset, str]):
        album_thumbnail_asset_id (Union[Unset, UUID]):
        description (Union[Unset, str]):
        is_activity_enabled (Union[Unset, bool]):
        order (Union[Unset, AssetOrder]):
    """

    album_name: Union[Unset, str] = UNSET
    album_thumbnail_asset_id: Union[Unset, UUID] = UNSET
    description: Union[Unset, str] = UNSET
    is_activity_enabled: Union[Unset, bool] = UNSET
    order: Union[Unset, AssetOrder] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_name = self.album_name

        album_thumbnail_asset_id: Union[Unset, str] = UNSET
        if not isinstance(self.album_thumbnail_asset_id, Unset):
            album_thumbnail_asset_id = str(self.album_thumbnail_asset_id)

        description = self.description

        is_activity_enabled = self.is_activity_enabled

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if album_name is not UNSET:
            field_dict["albumName"] = album_name
        if album_thumbnail_asset_id is not UNSET:
            field_dict["albumThumbnailAssetId"] = album_thumbnail_asset_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_activity_enabled is not UNSET:
            field_dict["isActivityEnabled"] = is_activity_enabled
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_name = d.pop("albumName", UNSET)

        _album_thumbnail_asset_id = d.pop("albumThumbnailAssetId", UNSET)
        album_thumbnail_asset_id: Union[Unset, UUID]
        if isinstance(_album_thumbnail_asset_id, Unset):
            album_thumbnail_asset_id = UNSET
        else:
            album_thumbnail_asset_id = UUID(_album_thumbnail_asset_id)

        description = d.pop("description", UNSET)

        is_activity_enabled = d.pop("isActivityEnabled", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, AssetOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = AssetOrder(_order)

        update_album_dto = cls(
            album_name=album_name,
            album_thumbnail_asset_id=album_thumbnail_asset_id,
            description=description,
            is_activity_enabled=is_activity_enabled,
            order=order,
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
