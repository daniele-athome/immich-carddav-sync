import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_avatar_color import UserAvatarColor
from ..models.user_status import UserStatus

if TYPE_CHECKING:
    from ..models.user_license import UserLicense


T = TypeVar("T", bound="UserAdminResponseDto")


@_attrs_define
class UserAdminResponseDto:
    """
    Attributes:
        avatar_color (UserAvatarColor):
        created_at (datetime.datetime):
        deleted_at (Union[None, datetime.datetime]):
        email (str):
        id (str):
        is_admin (bool):
        license_ (Union['UserLicense', None]):
        name (str):
        oauth_id (str):
        profile_changed_at (datetime.datetime):
        profile_image_path (str):
        quota_size_in_bytes (Union[None, int]):
        quota_usage_in_bytes (Union[None, int]):
        should_change_password (bool):
        status (UserStatus):
        storage_label (Union[None, str]):
        updated_at (datetime.datetime):
    """

    avatar_color: UserAvatarColor
    created_at: datetime.datetime
    deleted_at: Union[None, datetime.datetime]
    email: str
    id: str
    is_admin: bool
    license_: Union["UserLicense", None]
    name: str
    oauth_id: str
    profile_changed_at: datetime.datetime
    profile_image_path: str
    quota_size_in_bytes: Union[None, int]
    quota_usage_in_bytes: Union[None, int]
    should_change_password: bool
    status: UserStatus
    storage_label: Union[None, str]
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_license import UserLicense

        avatar_color = self.avatar_color.value

        created_at = self.created_at.isoformat()

        deleted_at: Union[None, str]
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        email = self.email

        id = self.id

        is_admin = self.is_admin

        license_: Union[Dict[str, Any], None]
        if isinstance(self.license_, UserLicense):
            license_ = self.license_.to_dict()
        else:
            license_ = self.license_

        name = self.name

        oauth_id = self.oauth_id

        profile_changed_at = self.profile_changed_at.isoformat()

        profile_image_path = self.profile_image_path

        quota_size_in_bytes: Union[None, int]
        quota_size_in_bytes = self.quota_size_in_bytes

        quota_usage_in_bytes: Union[None, int]
        quota_usage_in_bytes = self.quota_usage_in_bytes

        should_change_password = self.should_change_password

        status = self.status.value

        storage_label: Union[None, str]
        storage_label = self.storage_label

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatarColor": avatar_color,
                "createdAt": created_at,
                "deletedAt": deleted_at,
                "email": email,
                "id": id,
                "isAdmin": is_admin,
                "license": license_,
                "name": name,
                "oauthId": oauth_id,
                "profileChangedAt": profile_changed_at,
                "profileImagePath": profile_image_path,
                "quotaSizeInBytes": quota_size_in_bytes,
                "quotaUsageInBytes": quota_usage_in_bytes,
                "shouldChangePassword": should_change_password,
                "status": status,
                "storageLabel": storage_label,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_license import UserLicense

        d = src_dict.copy()
        avatar_color = UserAvatarColor(d.pop("avatarColor"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_deleted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))

        email = d.pop("email")

        id = d.pop("id")

        is_admin = d.pop("isAdmin")

        def _parse_license_(data: object) -> Union["UserLicense", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                license_type_1 = UserLicense.from_dict(data)

                return license_type_1
            except:  # noqa: E722
                pass
            return cast(Union["UserLicense", None], data)

        license_ = _parse_license_(d.pop("license"))

        name = d.pop("name")

        oauth_id = d.pop("oauthId")

        profile_changed_at = isoparse(d.pop("profileChangedAt"))

        profile_image_path = d.pop("profileImagePath")

        def _parse_quota_size_in_bytes(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        quota_size_in_bytes = _parse_quota_size_in_bytes(d.pop("quotaSizeInBytes"))

        def _parse_quota_usage_in_bytes(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        quota_usage_in_bytes = _parse_quota_usage_in_bytes(d.pop("quotaUsageInBytes"))

        should_change_password = d.pop("shouldChangePassword")

        status = UserStatus(d.pop("status"))

        def _parse_storage_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        storage_label = _parse_storage_label(d.pop("storageLabel"))

        updated_at = isoparse(d.pop("updatedAt"))

        user_admin_response_dto = cls(
            avatar_color=avatar_color,
            created_at=created_at,
            deleted_at=deleted_at,
            email=email,
            id=id,
            is_admin=is_admin,
            license_=license_,
            name=name,
            oauth_id=oauth_id,
            profile_changed_at=profile_changed_at,
            profile_image_path=profile_image_path,
            quota_size_in_bytes=quota_size_in_bytes,
            quota_usage_in_bytes=quota_usage_in_bytes,
            should_change_password=should_change_password,
            status=status,
            storage_label=storage_label,
            updated_at=updated_at,
        )

        user_admin_response_dto.additional_properties = d
        return user_admin_response_dto

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
