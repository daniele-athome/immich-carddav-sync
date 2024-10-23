from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.album_user_role import AlbumUserRole

if TYPE_CHECKING:
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="AlbumUserResponseDto")


@_attrs_define
class AlbumUserResponseDto:
    """
    Attributes:
        role (AlbumUserRole):
        user (UserResponseDto):
    """

    role: AlbumUserRole
    user: "UserResponseDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_response_dto import UserResponseDto

        d = src_dict.copy()
        role = AlbumUserRole(d.pop("role"))

        user = UserResponseDto.from_dict(d.pop("user"))

        album_user_response_dto = cls(
            role=role,
            user=user,
        )

        album_user_response_dto.additional_properties = d
        return album_user_response_dto

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
