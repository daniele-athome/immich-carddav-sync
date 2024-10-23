import datetime
from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetFullSyncDto")


@_attrs_define
class AssetFullSyncDto:
    """
    Attributes:
        limit (int):
        updated_until (datetime.datetime):
        last_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
    """

    limit: int
    updated_until: datetime.datetime
    last_id: Union[Unset, UUID] = UNSET
    user_id: Union[Unset, UUID] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        updated_until = self.updated_until.isoformat()

        last_id: Union[Unset, str] = UNSET
        if not isinstance(self.last_id, Unset):
            last_id = str(self.last_id)

        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "updatedUntil": updated_until,
            }
        )
        if last_id is not UNSET:
            field_dict["lastId"] = last_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit")

        updated_until = isoparse(d.pop("updatedUntil"))

        _last_id = d.pop("lastId", UNSET)
        last_id: Union[Unset, UUID]
        if isinstance(_last_id, Unset):
            last_id = UNSET
        else:
            last_id = UUID(_last_id)

        _user_id = d.pop("userId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        asset_full_sync_dto = cls(
            limit=limit,
            updated_until=updated_until,
            last_id=last_id,
            user_id=user_id,
        )

        asset_full_sync_dto.additional_properties = d
        return asset_full_sync_dto

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
