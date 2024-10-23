from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_response_dto import AssetResponseDto


T = TypeVar("T", bound="AssetDeltaSyncResponseDto")


@_attrs_define
class AssetDeltaSyncResponseDto:
    """
    Attributes:
        deleted (List[str]):
        needs_full_sync (bool):
        upserted (List['AssetResponseDto']):
    """

    deleted: List[str]
    needs_full_sync: bool
    upserted: List["AssetResponseDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deleted = self.deleted

        needs_full_sync = self.needs_full_sync

        upserted = []
        for upserted_item_data in self.upserted:
            upserted_item = upserted_item_data.to_dict()
            upserted.append(upserted_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "needsFullSync": needs_full_sync,
                "upserted": upserted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_response_dto import AssetResponseDto

        d = src_dict.copy()
        deleted = cast(List[str], d.pop("deleted"))

        needs_full_sync = d.pop("needsFullSync")

        upserted = []
        _upserted = d.pop("upserted")
        for upserted_item_data in _upserted:
            upserted_item = AssetResponseDto.from_dict(upserted_item_data)

            upserted.append(upserted_item)

        asset_delta_sync_response_dto = cls(
            deleted=deleted,
            needs_full_sync=needs_full_sync,
            upserted=upserted,
        )

        asset_delta_sync_response_dto.additional_properties = d
        return asset_delta_sync_response_dto

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
