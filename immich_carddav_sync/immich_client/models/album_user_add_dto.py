from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.album_user_role import AlbumUserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumUserAddDto")


@_attrs_define
class AlbumUserAddDto:
    """
    Attributes:
        user_id (UUID):
        role (Union[Unset, AlbumUserRole]):
    """

    user_id: UUID
    role: Union[Unset, AlbumUserRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = str(self.user_id)

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = UUID(d.pop("userId"))

        _role = d.pop("role", UNSET)
        role: Union[Unset, AlbumUserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = AlbumUserRole(_role)

        album_user_add_dto = cls(
            user_id=user_id,
            role=role,
        )

        album_user_add_dto.additional_properties = d
        return album_user_add_dto

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
