from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteAssetDto")


@_attrs_define
class DeleteAssetDto:
    """
    Attributes:
        ids (List[str]):  Example: ['bf973405-3f2a-48d2-a687-2ed4167164be', 'dd41870b-5d00-46d2-924e-1d8489a0aa0f',
            'fad77c3f-deef-4e7e-9608-14c1aa4e559a'].
    """

    ids: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[str], d.pop("ids"))

        delete_asset_dto = cls(
            ids=ids,
        )

        delete_asset_dto.additional_properties = d
        return delete_asset_dto

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
