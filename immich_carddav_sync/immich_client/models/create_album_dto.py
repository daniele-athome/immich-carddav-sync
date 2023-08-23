from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAlbumDto")


@_attrs_define
class CreateAlbumDto:
    """
    Attributes:
        album_name (str):
        asset_ids (Union[Unset, List[str]]):
        description (Union[Unset, str]):
        shared_with_user_ids (Union[Unset, List[str]]):
    """

    album_name: str
    asset_ids: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    shared_with_user_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_name = self.album_name
        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        description = self.description
        shared_with_user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.shared_with_user_ids, Unset):
            shared_with_user_ids = self.shared_with_user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumName": album_name,
            }
        )
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if description is not UNSET:
            field_dict["description"] = description
        if shared_with_user_ids is not UNSET:
            field_dict["sharedWithUserIds"] = shared_with_user_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_name = d.pop("albumName")

        asset_ids = cast(List[str], d.pop("assetIds", UNSET))

        description = d.pop("description", UNSET)

        shared_with_user_ids = cast(List[str], d.pop("sharedWithUserIds", UNSET))

        create_album_dto = cls(
            album_name=album_name,
            asset_ids=asset_ids,
            description=description,
            shared_with_user_ids=shared_with_user_ids,
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
