import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_type_enum import AssetTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto
    from ..models.asset_stack_response_dto import AssetStackResponseDto
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
        is_favorite (bool):
        is_offline (bool):
        is_trashed (bool):
        local_date_time (datetime.datetime):
        original_file_name (str):
        original_path (str):
        owner_id (str):
        thumbhash (Union[None, str]):
        type (AssetTypeEnum):
        updated_at (datetime.datetime):
        duplicate_id (Union[None, Unset, str]):
        exif_info (Union[Unset, ExifResponseDto]):
        library_id (Union[None, Unset, str]): This property was deprecated in v1.106.0
        live_photo_video_id (Union[None, Unset, str]):
        original_mime_type (Union[Unset, str]):
        owner (Union[Unset, UserResponseDto]):
        people (Union[Unset, List['PersonWithFacesResponseDto']]):
        resized (Union[Unset, bool]): This property was deprecated in v1.113.0
        smart_info (Union[Unset, SmartInfoResponseDto]):
        stack (Union['AssetStackResponseDto', None, Unset]):
        tags (Union[Unset, List['TagResponseDto']]):
        unassigned_faces (Union[Unset, List['AssetFaceWithoutPersonResponseDto']]):
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
    is_favorite: bool
    is_offline: bool
    is_trashed: bool
    local_date_time: datetime.datetime
    original_file_name: str
    original_path: str
    owner_id: str
    thumbhash: Union[None, str]
    type: AssetTypeEnum
    updated_at: datetime.datetime
    duplicate_id: Union[None, Unset, str] = UNSET
    exif_info: Union[Unset, "ExifResponseDto"] = UNSET
    library_id: Union[None, Unset, str] = UNSET
    live_photo_video_id: Union[None, Unset, str] = UNSET
    original_mime_type: Union[Unset, str] = UNSET
    owner: Union[Unset, "UserResponseDto"] = UNSET
    people: Union[Unset, List["PersonWithFacesResponseDto"]] = UNSET
    resized: Union[Unset, bool] = UNSET
    smart_info: Union[Unset, "SmartInfoResponseDto"] = UNSET
    stack: Union["AssetStackResponseDto", None, Unset] = UNSET
    tags: Union[Unset, List["TagResponseDto"]] = UNSET
    unassigned_faces: Union[Unset, List["AssetFaceWithoutPersonResponseDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.asset_stack_response_dto import AssetStackResponseDto

        checksum = self.checksum

        device_asset_id = self.device_asset_id

        device_id = self.device_id

        duration = self.duration

        file_created_at = self.file_created_at.isoformat()

        file_modified_at = self.file_modified_at.isoformat()

        has_metadata = self.has_metadata

        id = self.id

        is_archived = self.is_archived

        is_favorite = self.is_favorite

        is_offline = self.is_offline

        is_trashed = self.is_trashed

        local_date_time = self.local_date_time.isoformat()

        original_file_name = self.original_file_name

        original_path = self.original_path

        owner_id = self.owner_id

        thumbhash: Union[None, str]
        thumbhash = self.thumbhash

        type = self.type.value

        updated_at = self.updated_at.isoformat()

        duplicate_id: Union[None, Unset, str]
        if isinstance(self.duplicate_id, Unset):
            duplicate_id = UNSET
        else:
            duplicate_id = self.duplicate_id

        exif_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exif_info, Unset):
            exif_info = self.exif_info.to_dict()

        library_id: Union[None, Unset, str]
        if isinstance(self.library_id, Unset):
            library_id = UNSET
        else:
            library_id = self.library_id

        live_photo_video_id: Union[None, Unset, str]
        if isinstance(self.live_photo_video_id, Unset):
            live_photo_video_id = UNSET
        else:
            live_photo_video_id = self.live_photo_video_id

        original_mime_type = self.original_mime_type

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        people: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.people, Unset):
            people = []
            for people_item_data in self.people:
                people_item = people_item_data.to_dict()
                people.append(people_item)

        resized = self.resized

        smart_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.smart_info, Unset):
            smart_info = self.smart_info.to_dict()

        stack: Union[Dict[str, Any], None, Unset]
        if isinstance(self.stack, Unset):
            stack = UNSET
        elif isinstance(self.stack, AssetStackResponseDto):
            stack = self.stack.to_dict()
        else:
            stack = self.stack

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        unassigned_faces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unassigned_faces, Unset):
            unassigned_faces = []
            for unassigned_faces_item_data in self.unassigned_faces:
                unassigned_faces_item = unassigned_faces_item_data.to_dict()
                unassigned_faces.append(unassigned_faces_item)

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
                "isFavorite": is_favorite,
                "isOffline": is_offline,
                "isTrashed": is_trashed,
                "localDateTime": local_date_time,
                "originalFileName": original_file_name,
                "originalPath": original_path,
                "ownerId": owner_id,
                "thumbhash": thumbhash,
                "type": type,
                "updatedAt": updated_at,
            }
        )
        if duplicate_id is not UNSET:
            field_dict["duplicateId"] = duplicate_id
        if exif_info is not UNSET:
            field_dict["exifInfo"] = exif_info
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if live_photo_video_id is not UNSET:
            field_dict["livePhotoVideoId"] = live_photo_video_id
        if original_mime_type is not UNSET:
            field_dict["originalMimeType"] = original_mime_type
        if owner is not UNSET:
            field_dict["owner"] = owner
        if people is not UNSET:
            field_dict["people"] = people
        if resized is not UNSET:
            field_dict["resized"] = resized
        if smart_info is not UNSET:
            field_dict["smartInfo"] = smart_info
        if stack is not UNSET:
            field_dict["stack"] = stack
        if tags is not UNSET:
            field_dict["tags"] = tags
        if unassigned_faces is not UNSET:
            field_dict["unassignedFaces"] = unassigned_faces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto
        from ..models.asset_stack_response_dto import AssetStackResponseDto
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

        is_favorite = d.pop("isFavorite")

        is_offline = d.pop("isOffline")

        is_trashed = d.pop("isTrashed")

        local_date_time = isoparse(d.pop("localDateTime"))

        original_file_name = d.pop("originalFileName")

        original_path = d.pop("originalPath")

        owner_id = d.pop("ownerId")

        def _parse_thumbhash(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        thumbhash = _parse_thumbhash(d.pop("thumbhash"))

        type = AssetTypeEnum(d.pop("type"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_duplicate_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        duplicate_id = _parse_duplicate_id(d.pop("duplicateId", UNSET))

        _exif_info = d.pop("exifInfo", UNSET)
        exif_info: Union[Unset, ExifResponseDto]
        if isinstance(_exif_info, Unset):
            exif_info = UNSET
        else:
            exif_info = ExifResponseDto.from_dict(_exif_info)

        def _parse_library_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        library_id = _parse_library_id(d.pop("libraryId", UNSET))

        def _parse_live_photo_video_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live_photo_video_id = _parse_live_photo_video_id(d.pop("livePhotoVideoId", UNSET))

        original_mime_type = d.pop("originalMimeType", UNSET)

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

        resized = d.pop("resized", UNSET)

        _smart_info = d.pop("smartInfo", UNSET)
        smart_info: Union[Unset, SmartInfoResponseDto]
        if isinstance(_smart_info, Unset):
            smart_info = UNSET
        else:
            smart_info = SmartInfoResponseDto.from_dict(_smart_info)

        def _parse_stack(data: object) -> Union["AssetStackResponseDto", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stack_type_1 = AssetStackResponseDto.from_dict(data)

                return stack_type_1
            except:  # noqa: E722
                pass
            return cast(Union["AssetStackResponseDto", None, Unset], data)

        stack = _parse_stack(d.pop("stack", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = TagResponseDto.from_dict(tags_item_data)

            tags.append(tags_item)

        unassigned_faces = []
        _unassigned_faces = d.pop("unassignedFaces", UNSET)
        for unassigned_faces_item_data in _unassigned_faces or []:
            unassigned_faces_item = AssetFaceWithoutPersonResponseDto.from_dict(unassigned_faces_item_data)

            unassigned_faces.append(unassigned_faces_item)

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
            is_favorite=is_favorite,
            is_offline=is_offline,
            is_trashed=is_trashed,
            local_date_time=local_date_time,
            original_file_name=original_file_name,
            original_path=original_path,
            owner_id=owner_id,
            thumbhash=thumbhash,
            type=type,
            updated_at=updated_at,
            duplicate_id=duplicate_id,
            exif_info=exif_info,
            library_id=library_id,
            live_photo_video_id=live_photo_video_id,
            original_mime_type=original_mime_type,
            owner=owner,
            people=people,
            resized=resized,
            smart_info=smart_info,
            stack=stack,
            tags=tags,
            unassigned_faces=unassigned_faces,
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
