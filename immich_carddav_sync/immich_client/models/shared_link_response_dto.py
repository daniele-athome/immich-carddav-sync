import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.shared_link_type import SharedLinkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_response_dto import AlbumResponseDto
    from ..models.asset_response_dto import AssetResponseDto


T = TypeVar("T", bound="SharedLinkResponseDto")


@_attrs_define
class SharedLinkResponseDto:
    """
    Attributes:
        allow_download (bool):
        allow_upload (bool):
        assets (List['AssetResponseDto']):
        created_at (datetime.datetime):
        id (str):
        key (str):
        show_metadata (bool):
        type (SharedLinkType):
        user_id (str):
        album (Union[Unset, AlbumResponseDto]):
        description (Optional[str]):
        expires_at (Optional[datetime.datetime]):
        password (Optional[str]):
        token (Union[Unset, None, str]):
    """

    allow_download: bool
    allow_upload: bool
    assets: List["AssetResponseDto"]
    created_at: datetime.datetime
    id: str
    key: str
    show_metadata: bool
    type: SharedLinkType
    user_id: str
    description: Optional[str]
    expires_at: Optional[datetime.datetime]
    password: Optional[str]
    album: Union[Unset, "AlbumResponseDto"] = UNSET
    token: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_download = self.allow_download
        allow_upload = self.allow_upload
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()

            assets.append(assets_item)

        created_at = self.created_at.isoformat()

        id = self.id
        key = self.key
        show_metadata = self.show_metadata
        type = self.type.value

        user_id = self.user_id
        album: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        description = self.description
        expires_at = self.expires_at.isoformat() if self.expires_at else None

        password = self.password
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowDownload": allow_download,
                "allowUpload": allow_upload,
                "assets": assets,
                "createdAt": created_at,
                "id": id,
                "key": key,
                "showMetadata": show_metadata,
                "type": type,
                "userId": user_id,
                "description": description,
                "expiresAt": expires_at,
                "password": password,
            }
        )
        if album is not UNSET:
            field_dict["album"] = album
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.album_response_dto import AlbumResponseDto
        from ..models.asset_response_dto import AssetResponseDto

        d = src_dict.copy()
        allow_download = d.pop("allowDownload")

        allow_upload = d.pop("allowUpload")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetResponseDto.from_dict(assets_item_data)

            assets.append(assets_item)

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        key = d.pop("key")

        show_metadata = d.pop("showMetadata")

        type = SharedLinkType(d.pop("type"))

        user_id = d.pop("userId")

        _album = d.pop("album", UNSET)
        album: Union[Unset, AlbumResponseDto]
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResponseDto.from_dict(_album)

        description = d.pop("description")

        _expires_at = d.pop("expiresAt")
        expires_at: Optional[datetime.datetime]
        if _expires_at is None:
            expires_at = None
        else:
            expires_at = isoparse(_expires_at)

        password = d.pop("password")

        token = d.pop("token", UNSET)

        shared_link_response_dto = cls(
            allow_download=allow_download,
            allow_upload=allow_upload,
            assets=assets,
            created_at=created_at,
            id=id,
            key=key,
            show_metadata=show_metadata,
            type=type,
            user_id=user_id,
            album=album,
            description=description,
            expires_at=expires_at,
            password=password,
            token=token,
        )

        shared_link_response_dto.additional_properties = d
        return shared_link_response_dto

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
