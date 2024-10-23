from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_response_dto import PersonResponseDto


T = TypeVar("T", bound="PeopleResponseDto")


@_attrs_define
class PeopleResponseDto:
    """
    Attributes:
        hidden (int):
        people (List['PersonResponseDto']):
        total (int):
        has_next_page (Union[Unset, bool]): This property was added in v1.110.0
    """

    hidden: int
    people: List["PersonResponseDto"]
    total: int
    has_next_page: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hidden = self.hidden

        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        total = self.total

        has_next_page = self.has_next_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hidden": hidden,
                "people": people,
                "total": total,
            }
        )
        if has_next_page is not UNSET:
            field_dict["hasNextPage"] = has_next_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_response_dto import PersonResponseDto

        d = src_dict.copy()
        hidden = d.pop("hidden")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = PersonResponseDto.from_dict(people_item_data)

            people.append(people_item)

        total = d.pop("total")

        has_next_page = d.pop("hasNextPage", UNSET)

        people_response_dto = cls(
            hidden=hidden,
            people=people,
            total=total,
            has_next_page=has_next_page,
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
