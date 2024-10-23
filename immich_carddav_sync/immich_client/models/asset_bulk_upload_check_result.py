from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_bulk_upload_check_result_action import AssetBulkUploadCheckResultAction
from ..models.asset_bulk_upload_check_result_reason import AssetBulkUploadCheckResultReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetBulkUploadCheckResult")


@_attrs_define
class AssetBulkUploadCheckResult:
    """
    Attributes:
        action (AssetBulkUploadCheckResultAction):
        id (str):
        asset_id (Union[Unset, str]):
        is_trashed (Union[Unset, bool]):
        reason (Union[Unset, AssetBulkUploadCheckResultReason]):
    """

    action: AssetBulkUploadCheckResultAction
    id: str
    asset_id: Union[Unset, str] = UNSET
    is_trashed: Union[Unset, bool] = UNSET
    reason: Union[Unset, AssetBulkUploadCheckResultReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        id = self.id

        asset_id = self.asset_id

        is_trashed = self.is_trashed

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "id": id,
            }
        )
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if is_trashed is not UNSET:
            field_dict["isTrashed"] = is_trashed
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = AssetBulkUploadCheckResultAction(d.pop("action"))

        id = d.pop("id")

        asset_id = d.pop("assetId", UNSET)

        is_trashed = d.pop("isTrashed", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, AssetBulkUploadCheckResultReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = AssetBulkUploadCheckResultReason(_reason)

        asset_bulk_upload_check_result = cls(
            action=action,
            id=id,
            asset_id=asset_id,
            is_trashed=is_trashed,
            reason=reason,
        )

        asset_bulk_upload_check_result.additional_properties = d
        return asset_bulk_upload_check_result

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
