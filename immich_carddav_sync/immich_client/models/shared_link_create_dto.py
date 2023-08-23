import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.shared_link_type import SharedLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedLinkCreateDto")


@_attrs_define
class SharedLinkCreateDto:
    """
    Attributes:
        type (SharedLinkType):
        album_id (Union[Unset, str]):
        allow_download (Union[Unset, bool]):  Default: True.
        allow_upload (Union[Unset, bool]):
        asset_ids (Union[Unset, List[str]]):
        description (Union[Unset, str]):
        expires_at (Union[Unset, None, datetime.datetime]):
        show_exif (Union[Unset, bool]):  Default: True.
    """

    type: SharedLinkType
    album_id: Union[Unset, str] = UNSET
    allow_download: Union[Unset, bool] = True
    allow_upload: Union[Unset, bool] = False
    asset_ids: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[Unset, None, datetime.datetime] = UNSET
    show_exif: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        album_id = self.album_id
        allow_download = self.allow_download
        allow_upload = self.allow_upload
        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        description = self.description
        expires_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat() if self.expires_at else None

        show_exif = self.show_exif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if allow_upload is not UNSET:
            field_dict["allowUpload"] = allow_upload
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if show_exif is not UNSET:
            field_dict["showExif"] = show_exif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SharedLinkType(d.pop("type"))

        album_id = d.pop("albumId", UNSET)

        allow_download = d.pop("allowDownload", UNSET)

        allow_upload = d.pop("allowUpload", UNSET)

        asset_ids = cast(List[str], d.pop("assetIds", UNSET))

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, None, datetime.datetime]
        if _expires_at is None:
            expires_at = None
        elif isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        show_exif = d.pop("showExif", UNSET)

        shared_link_create_dto = cls(
            type=type,
            album_id=album_id,
            allow_download=allow_download,
            allow_upload=allow_upload,
            asset_ids=asset_ids,
            description=description,
            expires_at=expires_at,
            show_exif=show_exif,
        )

        shared_link_create_dto.additional_properties = d
        return shared_link_create_dto

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
