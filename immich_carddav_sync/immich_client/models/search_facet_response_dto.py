from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_facet_count_response_dto import SearchFacetCountResponseDto


T = TypeVar("T", bound="SearchFacetResponseDto")


@_attrs_define
class SearchFacetResponseDto:
    """
    Attributes:
        counts (List['SearchFacetCountResponseDto']):
        field_name (str):
    """

    counts: List["SearchFacetCountResponseDto"]
    field_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counts = []
        for counts_item_data in self.counts:
            counts_item = counts_item_data.to_dict()

            counts.append(counts_item)

        field_name = self.field_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "counts": counts,
                "fieldName": field_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_facet_count_response_dto import SearchFacetCountResponseDto

        d = src_dict.copy()
        counts = []
        _counts = d.pop("counts")
        for counts_item_data in _counts:
            counts_item = SearchFacetCountResponseDto.from_dict(counts_item_data)

            counts.append(counts_item)

        field_name = d.pop("fieldName")

        search_facet_response_dto = cls(
            counts=counts,
            field_name=field_name,
        )

        search_facet_response_dto.additional_properties = d
        return search_facet_response_dto

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
