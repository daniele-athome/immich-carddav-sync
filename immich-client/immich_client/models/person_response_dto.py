import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PersonResponseDto")


@_attrs_define
class PersonResponseDto:
    """
    Attributes:
        id (str):
        is_hidden (bool):
        name (str):
        thumbnail_path (str):
        birth_date (Optional[datetime.date]):
    """

    id: str
    is_hidden: bool
    name: str
    thumbnail_path: str
    birth_date: Optional[datetime.date]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_hidden = self.is_hidden
        name = self.name
        thumbnail_path = self.thumbnail_path
        birth_date = self.birth_date.isoformat() if self.birth_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isHidden": is_hidden,
                "name": name,
                "thumbnailPath": thumbnail_path,
                "birthDate": birth_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        is_hidden = d.pop("isHidden")

        name = d.pop("name")

        thumbnail_path = d.pop("thumbnailPath")

        _birth_date = d.pop("birthDate")
        birth_date: Optional[datetime.date]
        if _birth_date is None:
            birth_date = None
        else:
            birth_date = isoparse(_birth_date).date()

        person_response_dto = cls(
            id=id,
            is_hidden=is_hidden,
            name=name,
            thumbnail_path=thumbnail_path,
            birth_date=birth_date,
        )

        person_response_dto.additional_properties = d
        return person_response_dto

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
