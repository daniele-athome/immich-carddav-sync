from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reaction_type import ReactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCreateDto")


@_attrs_define
class ActivityCreateDto:
    """
    Attributes:
        album_id (UUID):
        type (ReactionType):
        asset_id (Union[Unset, UUID]):
        comment (Union[Unset, str]):
    """

    album_id: UUID
    type: ReactionType
    asset_id: Union[Unset, UUID] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_id = str(self.album_id)

        type = self.type.value

        asset_id: Union[Unset, str] = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumId": album_id,
                "type": type,
            }
        )
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        album_id = UUID(d.pop("albumId"))

        type = ReactionType(d.pop("type"))

        _asset_id = d.pop("assetId", UNSET)
        asset_id: Union[Unset, UUID]
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        comment = d.pop("comment", UNSET)

        activity_create_dto = cls(
            album_id=album_id,
            type=type,
            asset_id=asset_id,
            comment=comment,
        )

        activity_create_dto.additional_properties = d
        return activity_create_dto

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
