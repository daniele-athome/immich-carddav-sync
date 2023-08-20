from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckDuplicateAssetResponseDto")


@_attrs_define
class CheckDuplicateAssetResponseDto:
    """
    Attributes:
        is_exist (bool):
        id (Union[Unset, str]):
    """

    is_exist: bool
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_exist = self.is_exist
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isExist": is_exist,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_exist = d.pop("isExist")

        id = d.pop("id", UNSET)

        check_duplicate_asset_response_dto = cls(
            is_exist=is_exist,
            id=id,
        )

        check_duplicate_asset_response_dto.additional_properties = d
        return check_duplicate_asset_response_dto

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
