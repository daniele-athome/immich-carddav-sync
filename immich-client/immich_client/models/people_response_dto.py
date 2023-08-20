from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.person_response_dto import PersonResponseDto


T = TypeVar("T", bound="PeopleResponseDto")


@_attrs_define
class PeopleResponseDto:
    """
    Attributes:
        people (List['PersonResponseDto']):
        total (int):
        visible (int):
    """

    people: List["PersonResponseDto"]
    total: int
    visible: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()

            people.append(people_item)

        total = self.total
        visible = self.visible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "people": people,
                "total": total,
                "visible": visible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_response_dto import PersonResponseDto

        d = src_dict.copy()
        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = PersonResponseDto.from_dict(people_item_data)

            people.append(people_item)

        total = d.pop("total")

        visible = d.pop("visible")

        people_response_dto = cls(
            people=people,
            total=total,
            visible=visible,
        )

        people_response_dto.additional_properties = d
        return people_response_dto

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
