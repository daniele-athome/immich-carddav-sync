from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_bulk_upload_check_result import AssetBulkUploadCheckResult


T = TypeVar("T", bound="AssetBulkUploadCheckResponseDto")


@_attrs_define
class AssetBulkUploadCheckResponseDto:
    """
    Attributes:
        results (List['AssetBulkUploadCheckResult']):
    """

    results: List["AssetBulkUploadCheckResult"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_bulk_upload_check_result import AssetBulkUploadCheckResult

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AssetBulkUploadCheckResult.from_dict(results_item_data)

            results.append(results_item)

        asset_bulk_upload_check_response_dto = cls(
            results=results,
        )

        asset_bulk_upload_check_response_dto.additional_properties = d
        return asset_bulk_upload_check_response_dto

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
