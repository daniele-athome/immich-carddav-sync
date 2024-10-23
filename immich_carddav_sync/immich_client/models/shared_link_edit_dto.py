import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedLinkEditDto")


@_attrs_define
class SharedLinkEditDto:
    """
    Attributes:
        allow_download (Union[Unset, bool]):
        allow_upload (Union[Unset, bool]):
        change_expiry_time (Union[Unset, bool]): Few clients cannot send null to set the expiryTime to never.
            Setting this flag and not sending expiryAt is considered as null instead.
            Clients that can send null values can ignore this.
        description (Union[Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
        password (Union[Unset, str]):
        show_metadata (Union[Unset, bool]):
    """

    allow_download: Union[Unset, bool] = UNSET
    allow_upload: Union[Unset, bool] = UNSET
    change_expiry_time: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    password: Union[Unset, str] = UNSET
    show_metadata: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_download = self.allow_download

        allow_upload = self.allow_upload

        change_expiry_time = self.change_expiry_time

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
        field_dict.update({})
        if allow_download is not UNSET:
            field_dict["allowDownload"] = allow_download
        if allow_upload is not UNSET:
            field_dict["allowUpload"] = allow_upload
        if change_expiry_time is not UNSET:
            field_dict["changeExpiryTime"] = change_expiry_time
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
        allow_download = d.pop("allowDownload", UNSET)

        allow_upload = d.pop("allowUpload", UNSET)

        change_expiry_time = d.pop("changeExpiryTime", UNSET)

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

        shared_link_edit_dto = cls(
            allow_download=allow_download,
            allow_upload=allow_upload,
            change_expiry_time=change_expiry_time,
            description=description,
            expires_at=expires_at,
            password=password,
            show_metadata=show_metadata,
        )

        shared_link_edit_dto.additional_properties = d
        return shared_link_edit_dto

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
