from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_ids_response_dto_error import AssetIdsResponseDtoError
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetIdsResponseDto")


@_attrs_define
class AssetIdsResponseDto:
    """
    Attributes:
        asset_id (str):
        success (bool):
        error (Union[Unset, AssetIdsResponseDtoError]):
    """

    asset_id: str
    success: bool
    error: Union[Unset, AssetIdsResponseDtoError] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id

        success = self.success

        error: Union[Unset, str] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "success": success,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_id = d.pop("assetId")

        success = d.pop("success")

        _error = d.pop("error", UNSET)
        error: Union[Unset, AssetIdsResponseDtoError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AssetIdsResponseDtoError(_error)

        asset_ids_response_dto = cls(
            asset_id=asset_id,
            success=success,
            error=error,
        )

        asset_ids_response_dto.additional_properties = d
        return asset_ids_response_dto

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
