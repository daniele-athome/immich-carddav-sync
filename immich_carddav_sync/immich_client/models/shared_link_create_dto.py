import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

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
        album_id (Union[Unset, UUID]):
        allow_download (Union[Unset, bool]):  Default: True.
        allow_upload (Union[Unset, bool]):
        asset_ids (Union[Unset, List[UUID]]):
        description (Union[Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
        password (Union[Unset, str]):
        show_metadata (Union[Unset, bool]):  Default: True.
    """

    type: SharedLinkType
    album_id: Union[Unset, UUID] = UNSET
    allow_download: Union[Unset, bool] = True
    allow_upload: Union[Unset, bool] = UNSET
    asset_ids: Union[Unset, List[UUID]] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    password: Union[Unset, str] = UNSET
    show_metadata: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        album_id: Union[Unset, str] = UNSET
        if not isinstance(self.album_id, Unset):
            album_id = str(self.album_id)

        allow_download = self.allow_download

        allow_upload = self.allow_upload

        asset_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = []
            for asset_ids_item_data in self.asset_ids:
                asset_ids_item = str(asset_ids_item_data)
                asset_ids.append(asset_ids_item)

        description = self.description

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        password = self.password

        show_metadata = self.show_metadata

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
        if password is not UNSET:
            field_dict["password"] = password
        if show_metadata is not UNSET:
            field_dict["showMetadata"] = show_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SharedLinkType(d.pop("type"))

        _album_id = d.pop("albumId", UNSET)
        album_id: Union[Unset, UUID]
        if isinstance(_album_id, Unset):
            album_id = UNSET
        else:
            album_id = UUID(_album_id)

        allow_download = d.pop("allowDownload", UNSET)

        allow_upload = d.pop("allowUpload", UNSET)

        asset_ids = []
        _asset_ids = d.pop("assetIds", UNSET)
        for asset_ids_item_data in _asset_ids or []:
            asset_ids_item = UUID(asset_ids_item_data)

            asset_ids.append(asset_ids_item)

        description = d.pop("description", UNSET)

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        password = d.pop("password", UNSET)

        show_metadata = d.pop("showMetadata", UNSET)

        shared_link_create_dto = cls(
            type=type,
            album_id=album_id,
            allow_download=allow_download,
            allow_upload=allow_upload,
            asset_ids=asset_ids,
            description=description,
            expires_at=expires_at,
            password=password,
            show_metadata=show_metadata,
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
