import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reaction_type import ReactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="ActivityResponseDto")


@_attrs_define
class ActivityResponseDto:
    """
    Attributes:
        asset_id (Union[None, str]):
        created_at (datetime.datetime):
        id (str):
        type (ReactionType):
        user (UserResponseDto):
        comment (Union[None, Unset, str]):
    """

    asset_id: Union[None, str]
    created_at: datetime.datetime
    id: str
    type: ReactionType
    user: "UserResponseDto"
    comment: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id: Union[None, str]
        asset_id = self.asset_id

        created_at = self.created_at.isoformat()

        id = self.id

        type = self.type.value

        user = self.user.to_dict()

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "createdAt": created_at,
                "id": id,
                "type": type,
                "user": user,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_response_dto import UserResponseDto

        d = src_dict.copy()

        def _parse_asset_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        asset_id = _parse_asset_id(d.pop("assetId"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        type = ReactionType(d.pop("type"))

        user = UserResponseDto.from_dict(d.pop("user"))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        activity_response_dto = cls(
            asset_id=asset_id,
            created_at=created_at,
            id=id,
            type=type,
            user=user,
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
