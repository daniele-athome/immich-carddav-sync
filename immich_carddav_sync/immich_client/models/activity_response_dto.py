import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_response_dto_type import ActivityResponseDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="ActivityResponseDto")


@_attrs_define
class ActivityResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        type (ActivityResponseDtoType):
        user (UserDto):
        asset_id (Optional[str]):
        comment (Union[Unset, None, str]):
    """

    created_at: datetime.datetime
    id: str
    type: ActivityResponseDtoType
    user: "UserDto"
    asset_id: Optional[str]
    comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id
        type = self.type.value

        user = self.user.to_dict()

        asset_id = self.asset_id
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "type": type,
                "user": user,
                "assetId": asset_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_dto import UserDto

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        type = ActivityResponseDtoType(d.pop("type"))

        user = UserDto.from_dict(d.pop("user"))

        asset_id = d.pop("assetId")

        comment = d.pop("comment", UNSET)

        activity_response_dto = cls(
            created_at=created_at,
            id=id,
            type=type,
            user=user,
            asset_id=asset_id,
            comment=comment,
        )

        activity_response_dto.additional_properties = d
        return activity_response_dto

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
