from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.album_response_dto import AlbumResponseDto
    from ..models.search_facet_response_dto import SearchFacetResponseDto


T = TypeVar("T", bound="SearchAlbumResponseDto")


@_attrs_define
class SearchAlbumResponseDto:
    """
    Attributes:
        count (int):
        facets (List['SearchFacetResponseDto']):
        items (List['AlbumResponseDto']):
        total (int):
    """

    count: int
    facets: List["SearchFacetResponseDto"]
    items: List["AlbumResponseDto"]
    total: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        facets = []
        for facets_item_data in self.facets:
            facets_item = facets_item_data.to_dict()
            facets.append(facets_item)

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "facets": facets,
                "items": items,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.album_response_dto import AlbumResponseDto
        from ..models.search_facet_response_dto import SearchFacetResponseDto

        d = src_dict.copy()
        count = d.pop("count")

        facets = []
        _facets = d.pop("facets")
        for facets_item_data in _facets:
            facets_item = SearchFacetResponseDto.from_dict(facets_item_data)

            facets.append(facets_item)

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = AlbumResponseDto.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        search_album_response_dto = cls(
            count=count,
            facets=facets,
            items=items,
            total=total,
        )

        search_album_response_dto.additional_properties = d
        return search_album_response_dto

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
