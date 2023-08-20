from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_response_dto import AssetResponseDto


T = TypeVar("T", bound="MemoryLaneResponseDto")


@_attrs_define
class MemoryLaneResponseDto:
    """
    Attributes:
        assets (List['AssetResponseDto']):
        title (str):
    """

    assets: List["AssetResponseDto"]
    title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()

            assets.append(assets_item)

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_response_dto import AssetResponseDto

        d = src_dict.copy()
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetResponseDto.from_dict(assets_item_data)

            assets.append(assets_item)

        title = d.pop("title")

        memory_lane_response_dto = cls(
            assets=assets,
            title=title,
        )

        memory_lane_response_dto.additional_properties = d
        return memory_lane_response_dto

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
