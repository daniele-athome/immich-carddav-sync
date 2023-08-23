from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_album_response_dto import SearchAlbumResponseDto
    from ..models.search_asset_response_dto import SearchAssetResponseDto


T = TypeVar("T", bound="SearchResponseDto")


@_attrs_define
class SearchResponseDto:
    """
    Attributes:
        albums (SearchAlbumResponseDto):
        assets (SearchAssetResponseDto):
    """

    albums: "SearchAlbumResponseDto"
    assets: "SearchAssetResponseDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        albums = self.albums.to_dict()

        assets = self.assets.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albums": albums,
                "assets": assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_album_response_dto import SearchAlbumResponseDto
        from ..models.search_asset_response_dto import SearchAssetResponseDto

        d = src_dict.copy()
        albums = SearchAlbumResponseDto.from_dict(d.pop("albums"))

        assets = SearchAssetResponseDto.from_dict(d.pop("assets"))

        search_response_dto = cls(
            albums=albums,
            assets=assets,
        )

        search_response_dto.additional_properties = d
        return search_response_dto

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
