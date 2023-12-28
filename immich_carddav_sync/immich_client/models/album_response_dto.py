import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_response_dto import AssetResponseDto
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="AlbumResponseDto")


@_attrs_define
class AlbumResponseDto:
    """
    Attributes:
        album_name (str):
        asset_count (int):
        assets (List['AssetResponseDto']):
        created_at (datetime.datetime):
        description (str):
        has_shared_link (bool):
        id (str):
        is_activity_enabled (bool):
        owner (UserResponseDto):
        owner_id (str):
        shared (bool):
        shared_users (List['UserResponseDto']):
        updated_at (datetime.datetime):
        album_thumbnail_asset_id (Optional[str]):
        end_date (Union[Unset, datetime.datetime]):
        last_modified_asset_timestamp (Union[Unset, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
    """

    album_name: str
    asset_count: int
    assets: List["AssetResponseDto"]
    created_at: datetime.datetime
    description: str
    has_shared_link: bool
    id: str
    is_activity_enabled: bool
    owner: "UserResponseDto"
    owner_id: str
    shared: bool
    shared_users: List["UserResponseDto"]
    updated_at: datetime.datetime
    album_thumbnail_asset_id: Optional[str]
    end_date: Union[Unset, datetime.datetime] = UNSET
    last_modified_asset_timestamp: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        album_name = self.album_name
        asset_count = self.asset_count
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()

            assets.append(assets_item)

        created_at = self.created_at.isoformat()

        description = self.description
        has_shared_link = self.has_shared_link
        id = self.id
        is_activity_enabled = self.is_activity_enabled
        owner = self.owner.to_dict()

        owner_id = self.owner_id
        shared = self.shared
        shared_users = []
        for shared_users_item_data in self.shared_users:
            shared_users_item = shared_users_item_data.to_dict()

            shared_users.append(shared_users_item)

        updated_at = self.updated_at.isoformat()

        album_thumbnail_asset_id = self.album_thumbnail_asset_id
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        last_modified_asset_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_asset_timestamp, Unset):
            last_modified_asset_timestamp = self.last_modified_asset_timestamp.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albumName": album_name,
                "assetCount": asset_count,
                "assets": assets,
                "createdAt": created_at,
                "description": description,
                "hasSharedLink": has_shared_link,
                "id": id,
                "isActivityEnabled": is_activity_enabled,
                "owner": owner,
                "ownerId": owner_id,
                "shared": shared,
                "sharedUsers": shared_users,
                "updatedAt": updated_at,
                "albumThumbnailAssetId": album_thumbnail_asset_id,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if last_modified_asset_timestamp is not UNSET:
            field_dict["lastModifiedAssetTimestamp"] = last_modified_asset_timestamp
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_response_dto import AssetResponseDto
        from ..models.user_response_dto import UserResponseDto

        d = src_dict.copy()
        album_name = d.pop("albumName")

        asset_count = d.pop("assetCount")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetResponseDto.from_dict(assets_item_data)

            assets.append(assets_item)

        created_at = isoparse(d.pop("createdAt"))

        description = d.pop("description")

        has_shared_link = d.pop("hasSharedLink")

        id = d.pop("id")

        is_activity_enabled = d.pop("isActivityEnabled")

        owner = UserResponseDto.from_dict(d.pop("owner"))

        owner_id = d.pop("ownerId")

        shared = d.pop("shared")

        shared_users = []
        _shared_users = d.pop("sharedUsers")
        for shared_users_item_data in _shared_users:
            shared_users_item = UserResponseDto.from_dict(shared_users_item_data)

            shared_users.append(shared_users_item)

        updated_at = isoparse(d.pop("updatedAt"))

        album_thumbnail_asset_id = d.pop("albumThumbnailAssetId")

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _last_modified_asset_timestamp = d.pop("lastModifiedAssetTimestamp", UNSET)
        last_modified_asset_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_asset_timestamp, Unset):
            last_modified_asset_timestamp = UNSET
        else:
            last_modified_asset_timestamp = isoparse(_last_modified_asset_timestamp)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        album_response_dto = cls(
            album_name=album_name,
            asset_count=asset_count,
            assets=assets,
            created_at=created_at,
            description=description,
            has_shared_link=has_shared_link,
            id=id,
            is_activity_enabled=is_activity_enabled,
            owner=owner,
            owner_id=owner_id,
            shared=shared,
            shared_users=shared_users,
            updated_at=updated_at,
            album_thumbnail_asset_id=album_thumbnail_asset_id,
            end_date=end_date,
            last_modified_asset_timestamp=last_modified_asset_timestamp,
            start_date=start_date,
        )

        album_response_dto.additional_properties = d
        return album_response_dto

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
