from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_explore_item import SearchExploreItem


T = TypeVar("T", bound="SearchExploreResponseDto")


@_attrs_define
class SearchExploreResponseDto:
    """
    Attributes:
        field_name (str):
        items (List['SearchExploreItem']):
    """

    field_name: str
    items: List["SearchExploreItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldName": field_name,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_explore_item import SearchExploreItem

        d = src_dict.copy()
        field_name = d.pop("fieldName")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SearchExploreItem.from_dict(items_item_data)

            items.append(items_item)

        search_explore_response_dto = cls(
            field_name=field_name,
            items=items,
        )

        search_explore_response_dto.additional_properties = d
        return search_explore_response_dto

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
