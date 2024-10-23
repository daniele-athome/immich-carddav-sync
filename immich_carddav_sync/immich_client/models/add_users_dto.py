from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.album_user_add_dto import AlbumUserAddDto


T = TypeVar("T", bound="AddUsersDto")


@_attrs_define
class AddUsersDto:
    """
    Attributes:
        album_users (List['AlbumUserAddDto']):
    """

    album_users: List["AlbumUserAddDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_users = []
        for album_users_item_data in self.album_users:
            album_users_item = album_users_item_data.to_dict()
            album_users.append(album_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumUsers": album_users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.album_user_add_dto import AlbumUserAddDto

        d = src_dict.copy()
        album_users = []
        _album_users = d.pop("albumUsers")
        for album_users_item_data in _album_users:
            album_users_item = AlbumUserAddDto.from_dict(album_users_item_data)

            album_users.append(album_users_item)

        add_users_dto = cls(
            album_users=album_users,
        )

        add_users_dto.additional_properties = d
        return add_users_dto

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
