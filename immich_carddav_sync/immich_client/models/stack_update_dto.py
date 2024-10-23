from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StackUpdateDto")


@_attrs_define
class StackUpdateDto:
    """
    Attributes:
        primary_asset_id (Union[Unset, UUID]):
    """

    primary_asset_id: Union[Unset, UUID] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary_asset_id: Union[Unset, str] = UNSET
        if not isinstance(self.primary_asset_id, Unset):
            primary_asset_id = str(self.primary_asset_id)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_asset_id is not UNSET:
            field_dict["primaryAssetId"] = primary_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _primary_asset_id = d.pop("primaryAssetId", UNSET)
        primary_asset_id: Union[Unset, UUID]
        if isinstance(_primary_asset_id, Unset):
            primary_asset_id = UNSET
        else:
            primary_asset_id = UUID(_primary_asset_id)

        stack_update_dto = cls(
            primary_asset_id=primary_asset_id,
        )

        stack_update_dto.additional_properties = d
        return stack_update_dto

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
