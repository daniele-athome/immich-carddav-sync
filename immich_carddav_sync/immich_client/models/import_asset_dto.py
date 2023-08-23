import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportAssetDto")


@_attrs_define
class ImportAssetDto:
    """
    Attributes:
        asset_path (str):
        device_asset_id (str):
        device_id (str):
        file_created_at (datetime.datetime):
        file_modified_at (datetime.datetime):
        is_favorite (bool):
        duration (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_read_only (Union[Unset, bool]):  Default: True.
        is_visible (Union[Unset, bool]):
        sidecar_path (Union[Unset, str]):
    """

    asset_path: str
    device_asset_id: str
    device_id: str
    file_created_at: datetime.datetime
    file_modified_at: datetime.datetime
    is_favorite: bool
    duration: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_read_only: Union[Unset, bool] = True
    is_visible: Union[Unset, bool] = UNSET
    sidecar_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_path = self.asset_path
        device_asset_id = self.device_asset_id
        device_id = self.device_id
        file_created_at = self.file_created_at.isoformat()

        file_modified_at = self.file_modified_at.isoformat()

        is_favorite = self.is_favorite
        duration = self.duration
        is_archived = self.is_archived
        is_read_only = self.is_read_only
        is_visible = self.is_visible
        sidecar_path = self.sidecar_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetPath": asset_path,
                "deviceAssetId": device_asset_id,
                "deviceId": device_id,
                "fileCreatedAt": file_created_at,
                "fileModifiedAt": file_modified_at,
                "isFavorite": is_favorite,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if sidecar_path is not UNSET:
            field_dict["sidecarPath"] = sidecar_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_path = d.pop("assetPath")

        device_asset_id = d.pop("deviceAssetId")

        device_id = d.pop("deviceId")

        file_created_at = isoparse(d.pop("fileCreatedAt"))

        file_modified_at = isoparse(d.pop("fileModifiedAt"))

        is_favorite = d.pop("isFavorite")

        duration = d.pop("duration", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        sidecar_path = d.pop("sidecarPath", UNSET)

        import_asset_dto = cls(
            asset_path=asset_path,
            device_asset_id=device_asset_id,
            device_id=device_id,
            file_created_at=file_created_at,
            file_modified_at=file_modified_at,
            is_favorite=is_favorite,
            duration=duration,
            is_archived=is_archived,
            is_read_only=is_read_only,
            is_visible=is_visible,
            sidecar_path=sidecar_path,
        )

        import_asset_dto.additional_properties = d
        return import_asset_dto

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
