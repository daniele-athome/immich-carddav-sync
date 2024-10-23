import datetime
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="AssetMediaCreateDto")


@_attrs_define
class AssetMediaCreateDto:
    """
    Attributes:
        asset_data (File):
        device_asset_id (str):
        device_id (str):
        file_created_at (datetime.datetime):
        file_modified_at (datetime.datetime):
        duration (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_visible (Union[Unset, bool]):
        live_photo_video_id (Union[Unset, UUID]):
        sidecar_data (Union[Unset, File]):
    """

    asset_data: File
    device_asset_id: str
    device_id: str
    file_created_at: datetime.datetime
    file_modified_at: datetime.datetime
    duration: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    live_photo_video_id: Union[Unset, UUID] = UNSET
    sidecar_data: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_data = self.asset_data.to_tuple()

        device_asset_id = self.device_asset_id

        device_id = self.device_id

        file_created_at = self.file_created_at.isoformat()

        file_modified_at = self.file_modified_at.isoformat()

        duration = self.duration

        is_archived = self.is_archived

        is_favorite = self.is_favorite

        is_visible = self.is_visible

        live_photo_video_id: Union[Unset, str] = UNSET
        if not isinstance(self.live_photo_video_id, Unset):
            live_photo_video_id = str(self.live_photo_video_id)

        sidecar_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.sidecar_data, Unset):
            sidecar_data = self.sidecar_data.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetData": asset_data,
                "deviceAssetId": device_asset_id,
                "deviceId": device_id,
                "fileCreatedAt": file_created_at,
                "fileModifiedAt": file_modified_at,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if live_photo_video_id is not UNSET:
            field_dict["livePhotoVideoId"] = live_photo_video_id
        if sidecar_data is not UNSET:
            field_dict["sidecarData"] = sidecar_data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        asset_data = self.asset_data.to_tuple()

        device_asset_id = (None, str(self.device_asset_id).encode(), "text/plain")

        device_id = (None, str(self.device_id).encode(), "text/plain")

        file_created_at = self.file_created_at.isoformat().encode()

        file_modified_at = self.file_modified_at.isoformat().encode()

        duration = (
            self.duration if isinstance(self.duration, Unset) else (None, str(self.duration).encode(), "text/plain")
        )

        is_archived = (
            self.is_archived
            if isinstance(self.is_archived, Unset)
            else (None, str(self.is_archived).encode(), "text/plain")
        )

        is_favorite = (
            self.is_favorite
            if isinstance(self.is_favorite, Unset)
            else (None, str(self.is_favorite).encode(), "text/plain")
        )

        is_visible = (
            self.is_visible
            if isinstance(self.is_visible, Unset)
            else (None, str(self.is_visible).encode(), "text/plain")
        )

        live_photo_video_id: Union[Unset, bytes] = UNSET
        if not isinstance(self.live_photo_video_id, Unset):
            live_photo_video_id = str(self.live_photo_video_id)

        sidecar_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.sidecar_data, Unset):
            sidecar_data = self.sidecar_data.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "assetData": asset_data,
                "deviceAssetId": device_asset_id,
                "deviceId": device_id,
                "fileCreatedAt": file_created_at,
                "fileModifiedAt": file_modified_at,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if live_photo_video_id is not UNSET:
            field_dict["livePhotoVideoId"] = live_photo_video_id
        if sidecar_data is not UNSET:
            field_dict["sidecarData"] = sidecar_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_data = File(payload=BytesIO(d.pop("assetData")))

        device_asset_id = d.pop("deviceAssetId")

        device_id = d.pop("deviceId")

        file_created_at = isoparse(d.pop("fileCreatedAt"))

        file_modified_at = isoparse(d.pop("fileModifiedAt"))

        duration = d.pop("duration", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        _live_photo_video_id = d.pop("livePhotoVideoId", UNSET)
        live_photo_video_id: Union[Unset, UUID]
        if isinstance(_live_photo_video_id, Unset):
            live_photo_video_id = UNSET
        else:
            live_photo_video_id = UUID(_live_photo_video_id)

        _sidecar_data = d.pop("sidecarData", UNSET)
        sidecar_data: Union[Unset, File]
        if isinstance(_sidecar_data, Unset):
            sidecar_data = UNSET
        else:
            sidecar_data = File(payload=BytesIO(_sidecar_data))

        asset_media_create_dto = cls(
            asset_data=asset_data,
            device_asset_id=device_asset_id,
            device_id=device_id,
            file_created_at=file_created_at,
            file_modified_at=file_modified_at,
            duration=duration,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_visible=is_visible,
            live_photo_video_id=live_photo_video_id,
            sidecar_data=sidecar_data,
        )

        asset_media_create_dto.additional_properties = d
        return asset_media_create_dto

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
