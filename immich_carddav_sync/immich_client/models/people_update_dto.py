from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.people_update_item import PeopleUpdateItem


T = TypeVar("T", bound="PeopleUpdateDto")


@_attrs_define
class PeopleUpdateDto:
    """
    Attributes:
        people (List['PeopleUpdateItem']):
    """

    people: List["PeopleUpdateItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.people_update_item import PeopleUpdateItem

        d = src_dict.copy()
        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = PeopleUpdateItem.from_dict(people_item_data)

            people.append(people_item)

        people_update_dto = cls(
            people=people,
        )

        people_update_dto.additional_properties = d
        return people_update_dto

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
