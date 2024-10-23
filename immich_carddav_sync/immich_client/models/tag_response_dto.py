import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagResponseDto")


@_attrs_define
class TagResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        updated_at (datetime.datetime):
        value (str):
        color (Union[Unset, str]):
        parent_id (Union[Unset, str]):
    """

    created_at: datetime.datetime
    id: str
    name: str
    updated_at: datetime.datetime
    value: str
    color: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        updated_at = self.updated_at.isoformat()

        value = self.value

        color = self.color

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "updatedAt": updated_at,
                "value": value,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updatedAt"))

        value = d.pop("value")

        color = d.pop("color", UNSET)

        parent_id = d.pop("parentId", UNSET)

        tag_response_dto = cls(
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            value=value,
            color=color,
            parent_id=parent_id,
        )

        tag_response_dto.additional_properties = d
        return tag_response_dto

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
