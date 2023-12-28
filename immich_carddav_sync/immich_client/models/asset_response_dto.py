import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_type_enum import AssetTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exif_response_dto import ExifResponseDto
    from ..models.person_with_faces_response_dto import PersonWithFacesResponseDto
    from ..models.smart_info_response_dto import SmartInfoResponseDto
    from ..models.tag_response_dto import TagResponseDto
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="AssetResponseDto")


@_attrs_define
class AssetResponseDto:
    """
    Attributes:
        checksum (str): base64 encoded sha1 hash
        device_asset_id (str):
        device_id (str):
        duration (str):
        file_created_at (datetime.datetime):
        file_modified_at (datetime.datetime):
        has_metadata (bool):
        id (str):
        is_archived (bool):
        is_external (bool):
        is_favorite (bool):
        is_offline (bool):
        is_read_only (bool):
        is_trashed (bool):
        library_id (str):
        local_date_time (datetime.datetime):
        original_file_name (str):
        original_path (str):
        owner_id (str):
        resized (bool):
        type (AssetTypeEnum):
        updated_at (datetime.datetime):
        exif_info (Union[Unset, ExifResponseDto]):
        live_photo_video_id (Union[Unset, None, str]):
        owner (Union[Unset, UserResponseDto]):
        people (Union[Unset, List['PersonWithFacesResponseDto']]):
        smart_info (Union[Unset, SmartInfoResponseDto]):
        stack (Union[Unset, List['AssetResponseDto']]):
        stack_count (Optional[int]):
        stack_parent_id (Union[Unset, None, str]):
        tags (Union[Unset, List['TagResponseDto']]):
        thumbhash (Optional[str]):
    """

    checksum: str
    device_asset_id: str
    device_id: str
    duration: str
    file_created_at: datetime.datetime
    file_modified_at: datetime.datetime
    has_metadata: bool
    id: str
    is_archived: bool
    is_external: bool
    is_favorite: bool
    is_offline: bool
    is_read_only: bool
    is_trashed: bool
    library_id: str
    local_date_time: datetime.datetime
    original_file_name: str
    original_path: str
    owner_id: str
    resized: bool
    type: AssetTypeEnum
    updated_at: datetime.datetime
    stack_count: Optional[int]
    thumbhash: Optional[str]
    exif_info: Union[Unset, "ExifResponseDto"] = UNSET
    live_photo_video_id: Union[Unset, None, str] = UNSET
    owner: Union[Unset, "UserResponseDto"] = UNSET
    people: Union[Unset, List["PersonWithFacesResponseDto"]] = UNSET
    smart_info: Union[Unset, "SmartInfoResponseDto"] = UNSET
    stack: Union[Unset, List["AssetResponseDto"]] = UNSET
    stack_parent_id: Union[Unset, None, str] = UNSET
    tags: Union[Unset, List["TagResponseDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checksum = self.checksum
        device_asset_id = self.device_asset_id
        device_id = self.device_id
        duration = self.duration
        file_created_at = self.file_created_at.isoformat()

        file_modified_at = self.file_modified_at.isoformat()

        has_metadata = self.has_metadata
        id = self.id
        is_archived = self.is_archived
        is_external = self.is_external
        is_favorite = self.is_favorite
        is_offline = self.is_offline
        is_read_only = self.is_read_only
        is_trashed = self.is_trashed
        library_id = self.library_id
        local_date_time = self.local_date_time.isoformat()

        original_file_name = self.original_file_name
        original_path = self.original_path
        owner_id = self.owner_id
        resized = self.resized
        type = self.type.value

        updated_at = self.updated_at.isoformat()

        exif_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exif_info, Unset):
            exif_info = self.exif_info.to_dict()

        live_photo_video_id = self.live_photo_video_id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        people: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.people, Unset):
            people = []
            for people_item_data in self.people:
                people_item = people_item_data.to_dict()

                people.append(people_item)

        smart_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.smart_info, Unset):
            smart_info = self.smart_info.to_dict()

        stack: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stack, Unset):
            stack = []
            for stack_item_data in self.stack:
                stack_item = stack_item_data.to_dict()

                stack.append(stack_item)

        stack_count = self.stack_count
        stack_parent_id = self.stack_parent_id
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        thumbhash = self.thumbhash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checksum": checksum,
                "deviceAssetId": device_asset_id,
                "deviceId": device_id,
                "duration": duration,
                "fileCreatedAt": file_created_at,
                "fileModifiedAt": file_modified_at,
                "hasMetadata": has_metadata,
                "id": id,
                "isArchived": is_archived,
                "isExternal": is_external,
                "isFavorite": is_favorite,
                "isOffline": is_offline,
                "isReadOnly": is_read_only,
                "isTrashed": is_trashed,
                "libraryId": library_id,
                "localDateTime": local_date_time,
                "originalFileName": original_file_name,
                "originalPath": original_path,
                "ownerId": owner_id,
                "resized": resized,
                "type": type,
                "updatedAt": updated_at,
                "stackCount": stack_count,
                "thumbhash": thumbhash,
            }
        )
        if exif_info is not UNSET:
            field_dict["exifInfo"] = exif_info
        if live_photo_video_id is not UNSET:
            field_dict["livePhotoVideoId"] = live_photo_video_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if people is not UNSET:
            field_dict["people"] = people
        if smart_info is not UNSET:
            field_dict["smartInfo"] = smart_info
        if stack is not UNSET:
            field_dict["stack"] = stack
        if stack_parent_id is not UNSET:
            field_dict["stackParentId"] = stack_parent_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exif_response_dto import ExifResponseDto
        from ..models.person_with_faces_response_dto import PersonWithFacesResponseDto
        from ..models.smart_info_response_dto import SmartInfoResponseDto
        from ..models.tag_response_dto import TagResponseDto
        from ..models.user_response_dto import UserResponseDto

        d = src_dict.copy()
        checksum = d.pop("checksum")

        device_asset_id = d.pop("deviceAssetId")

        device_id = d.pop("deviceId")

        duration = d.pop("duration")

        file_created_at = isoparse(d.pop("fileCreatedAt"))

        file_modified_at = isoparse(d.pop("fileModifiedAt"))

        has_metadata = d.pop("hasMetadata")

        id = d.pop("id")

        is_archived = d.pop("isArchived")

        is_external = d.pop("isExternal")

        is_favorite = d.pop("isFavorite")

        is_offline = d.pop("isOffline")

        is_read_only = d.pop("isReadOnly")

        is_trashed = d.pop("isTrashed")

        library_id = d.pop("libraryId")

        local_date_time = isoparse(d.pop("localDateTime"))

        original_file_name = d.pop("originalFileName")

        original_path = d.pop("originalPath")

        owner_id = d.pop("ownerId")

        resized = d.pop("resized")

        type = AssetTypeEnum(d.pop("type"))

        updated_at = isoparse(d.pop("updatedAt"))

        _exif_info = d.pop("exifInfo", UNSET)
        exif_info: Union[Unset, ExifResponseDto]
        if isinstance(_exif_info, Unset):
            exif_info = UNSET
        else:
            exif_info = ExifResponseDto.from_dict(_exif_info)

        live_photo_video_id = d.pop("livePhotoVideoId", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, UserResponseDto]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserResponseDto.from_dict(_owner)

        people = []
        _people = d.pop("people", UNSET)
        for people_item_data in _people or []:
            people_item = PersonWithFacesResponseDto.from_dict(people_item_data)

            people.append(people_item)

        _smart_info = d.pop("smartInfo", UNSET)
        smart_info: Union[Unset, SmartInfoResponseDto]
        if isinstance(_smart_info, Unset):
            smart_info = UNSET
        else:
            smart_info = SmartInfoResponseDto.from_dict(_smart_info)

        stack = []
        _stack = d.pop("stack", UNSET)
        for stack_item_data in _stack or []:
            stack_item = AssetResponseDto.from_dict(stack_item_data)

            stack.append(stack_item)

        stack_count = d.pop("stackCount")

        stack_parent_id = d.pop("stackParentId", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = TagResponseDto.from_dict(tags_item_data)

            tags.append(tags_item)

        thumbhash = d.pop("thumbhash")

        asset_response_dto = cls(
            checksum=checksum,
            device_asset_id=device_asset_id,
            device_id=device_id,
            duration=duration,
            file_created_at=file_created_at,
            file_modified_at=file_modified_at,
            has_metadata=has_metadata,
            id=id,
            is_archived=is_archived,
            is_external=is_external,
            is_favorite=is_favorite,
            is_offline=is_offline,
            is_read_only=is_read_only,
            is_trashed=is_trashed,
            library_id=library_id,
            local_date_time=local_date_time,
            original_file_name=original_file_name,
            original_path=original_path,
            owner_id=owner_id,
            resized=resized,
            type=type,
            updated_at=updated_at,
            exif_info=exif_info,
            live_photo_video_id=live_photo_video_id,
            owner=owner,
            people=people,
            smart_info=smart_info,
            stack=stack,
            stack_count=stack_count,
            stack_parent_id=stack_parent_id,
            tags=tags,
            thumbhash=thumbhash,
        )

        asset_response_dto.additional_properties = d
        return asset_response_dto

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
