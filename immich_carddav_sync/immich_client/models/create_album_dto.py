from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_user_create_dto import AlbumUserCreateDto


T = TypeVar("T", bound="CreateAlbumDto")


@_attrs_define
class CreateAlbumDto:
    """
    Attributes:
        album_name (str):
        album_users (Union[Unset, List['AlbumUserCreateDto']]):
        asset_ids (Union[Unset, List[UUID]]):
        description (Union[Unset, str]):
    """

    album_name: str
    album_users: Union[Unset, List["AlbumUserCreateDto"]] = UNSET
    asset_ids: Union[Unset, List[UUID]] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_name = self.album_name

        album_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.album_users, Unset):
            album_users = []
            for album_users_item_data in self.album_users:
                album_users_item = album_users_item_data.to_dict()
                album_users.append(album_users_item)

        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = []
            for asset_ids_item_data in self.asset_ids:
                asset_ids_item = str(asset_ids_item_data)
                asset_ids.append(asset_ids_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumName": album_name,
            }
        )
        if album_users is not UNSET:
            field_dict["albumUsers"] = album_users
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.album_user_create_dto import AlbumUserCreateDto

        d = src_dict.copy()
        album_name = d.pop("albumName")

        album_users = []
        _album_users = d.pop("albumUsers", UNSET)
        for album_users_item_data in _album_users or []:
            album_users_item = AlbumUserCreateDto.from_dict(album_users_item_data)

            album_users.append(album_users_item)

        asset_ids = []
        _asset_ids = d.pop("assetIds", UNSET)
        for asset_ids_item_data in _asset_ids or []:
            asset_ids_item = UUID(asset_ids_item_data)

            asset_ids.append(asset_ids_item)

        description = d.pop("description", UNSET)

        create_album_dto = cls(
            album_name=album_name,
            album_users=album_users,
            asset_ids=asset_ids,
            description=description,
        )

        create_album_dto.additional_properties = d
        return create_album_dto

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
