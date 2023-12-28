import datetime
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateAssetDto")


@_attrs_define
class CreateAssetDto:
    """
    Attributes:
        asset_data (File):
        device_asset_id (str):
        device_id (str):
        file_created_at (datetime.datetime):
        file_modified_at (datetime.datetime):
        duration (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_external (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_offline (Union[Unset, bool]):
        is_read_only (Union[Unset, bool]):
        is_visible (Union[Unset, bool]):
        library_id (Union[Unset, str]):
        live_photo_data (Union[Unset, File]):
        sidecar_data (Union[Unset, File]):
    """

    asset_data: File
    device_asset_id: str
    device_id: str
    file_created_at: datetime.datetime
    file_modified_at: datetime.datetime
    duration: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_external: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_offline: Union[Unset, bool] = UNSET
    is_read_only: Union[Unset, bool] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    library_id: Union[Unset, str] = UNSET
    live_photo_data: Union[Unset, File] = UNSET
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
        is_external = self.is_external
        is_favorite = self.is_favorite
        is_offline = self.is_offline
        is_read_only = self.is_read_only
        is_visible = self.is_visible
        library_id = self.library_id
        live_photo_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.live_photo_data, Unset):
            live_photo_data = self.live_photo_data.to_tuple()

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
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_offline is not UNSET:
            field_dict["isOffline"] = is_offline
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if live_photo_data is not UNSET:
            field_dict["livePhotoData"] = live_photo_data
        if sidecar_data is not UNSET:
            field_dict["sidecarData"] = sidecar_data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        asset_data = self.asset_data.to_tuple()

        device_asset_id = (
            self.device_asset_id
            if isinstance(self.device_asset_id, Unset)
            else (None, str(self.device_asset_id).encode(), "text/plain")
        )
        device_id = (
            self.device_id if isinstance(self.device_id, Unset) else (None, str(self.device_id).encode(), "text/plain")
        )
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
        is_external = (
            self.is_external
            if isinstance(self.is_external, Unset)
            else (None, str(self.is_external).encode(), "text/plain")
        )
        is_favorite = (
            self.is_favorite
            if isinstance(self.is_favorite, Unset)
            else (None, str(self.is_favorite).encode(), "text/plain")
        )
        is_offline = (
            self.is_offline
            if isinstance(self.is_offline, Unset)
            else (None, str(self.is_offline).encode(), "text/plain")
        )
        is_read_only = (
            self.is_read_only
            if isinstance(self.is_read_only, Unset)
            else (None, str(self.is_read_only).encode(), "text/plain")
        )
        is_visible = (
            self.is_visible
            if isinstance(self.is_visible, Unset)
            else (None, str(self.is_visible).encode(), "text/plain")
        )
        library_id = (
            self.library_id
            if isinstance(self.library_id, Unset)
            else (None, str(self.library_id).encode(), "text/plain")
        )
        live_photo_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.live_photo_data, Unset):
            live_photo_data = self.live_photo_data.to_tuple()

        sidecar_data: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.sidecar_data, Unset):
            sidecar_data = self.sidecar_data.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
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
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_offline is not UNSET:
            field_dict["isOffline"] = is_offline
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if live_photo_data is not UNSET:
            field_dict["livePhotoData"] = live_photo_data
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

        is_external = d.pop("isExternal", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        is_offline = d.pop("isOffline", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        library_id = d.pop("libraryId", UNSET)

        _live_photo_data = d.pop("livePhotoData", UNSET)
        live_photo_data: Union[Unset, File]
        if isinstance(_live_photo_data, Unset):
            live_photo_data = UNSET
        else:
            live_photo_data = File(payload=BytesIO(_live_photo_data))

        _sidecar_data = d.pop("sidecarData", UNSET)
        sidecar_data: Union[Unset, File]
        if isinstance(_sidecar_data, Unset):
            sidecar_data = UNSET
        else:
            sidecar_data = File(payload=BytesIO(_sidecar_data))

        create_asset_dto = cls(
            asset_data=asset_data,
            device_asset_id=device_asset_id,
            device_id=device_id,
            file_created_at=file_created_at,
            file_modified_at=file_modified_at,
            duration=duration,
            is_archived=is_archived,
            is_external=is_external,
            is_favorite=is_favorite,
            is_offline=is_offline,
            is_read_only=is_read_only,
            is_visible=is_visible,
            library_id=library_id,
            live_photo_data=live_photo_data,
            sidecar_data=sidecar_data,
        )

        create_asset_dto.additional_properties = d
        return create_asset_dto

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
