import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        description (Union[None, str]):
        expires_at (Union[None, datetime.datetime]):
        id (str):
        key (str):
        password (Union[None, str]):
        show_metadata (bool):
        type (SharedLinkType):
        user_id (str):
        album (Union[Unset, AlbumResponseDto]):
        token (Union[None, Unset, str]):
    """

    allow_download: bool
    allow_upload: bool
    assets: List["AssetResponseDto"]
    created_at: datetime.datetime
    description: Union[None, str]
    expires_at: Union[None, datetime.datetime]
    id: str
    key: str
    password: Union[None, str]
    show_metadata: bool
    type: SharedLinkType
    user_id: str
    album: Union[Unset, "AlbumResponseDto"] = UNSET
    token: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_download = self.allow_download

        allow_upload = self.allow_upload

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        created_at = self.created_at.isoformat()

        description: Union[None, str]
        description = self.description

        expires_at: Union[None, str]
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        id = self.id

        key = self.key

        password: Union[None, str]
        password = self.password

        show_metadata = self.show_metadata

        type = self.type.value

        user_id = self.user_id

        album: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        token: Union[None, Unset, str]
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowDownload": allow_download,
                "allowUpload": allow_upload,
                "assets": assets,
                "createdAt": created_at,
                "description": description,
                "expiresAt": expires_at,
                "id": id,
                "key": key,
                "password": password,
                "showMetadata": show_metadata,
                "type": type,
                "userId": user_id,
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

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        def _parse_expires_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        id = d.pop("id")

        key = d.pop("key")

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop("password"))

        show_metadata = d.pop("showMetadata")

        type = SharedLinkType(d.pop("type"))

        user_id = d.pop("userId")

        _album = d.pop("album", UNSET)
        album: Union[Unset, AlbumResponseDto]
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResponseDto.from_dict(_album)

        def _parse_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token = _parse_token(d.pop("token", UNSET))

        shared_link_response_dto = cls(
            allow_download=allow_download,
            allow_upload=allow_upload,
            assets=assets,
            created_at=created_at,
            description=description,
            expires_at=expires_at,
            id=id,
            key=key,
            password=password,
            show_metadata=show_metadata,
            type=type,
            user_id=user_id,
            album=album,
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
