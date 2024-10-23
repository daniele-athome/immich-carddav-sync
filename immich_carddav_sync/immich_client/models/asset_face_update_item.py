from typing import Any, Dict, List, Type, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetFaceUpdateItem")


@_attrs_define
class AssetFaceUpdateItem:
    """
    Attributes:
        asset_id (UUID):
        person_id (UUID):
    """

    asset_id: UUID
    person_id: UUID
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = str(self.asset_id)

        person_id = str(self.person_id)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "personId": person_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_id = UUID(d.pop("assetId"))

        person_id = UUID(d.pop("personId"))

        asset_face_update_item = cls(
            asset_id=asset_id,
            person_id=person_id,
        )

        asset_face_update_item.additional_properties = d
        return asset_face_update_item

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
