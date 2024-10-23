import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryUpdateDto")


@_attrs_define
class MemoryUpdateDto:
    """
    Attributes:
        is_saved (Union[Unset, bool]):
        memory_at (Union[Unset, datetime.datetime]):
        seen_at (Union[Unset, datetime.datetime]):
    """

    is_saved: Union[Unset, bool] = UNSET
    memory_at: Union[Unset, datetime.datetime] = UNSET
    seen_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_saved = self.is_saved

        memory_at: Union[Unset, str] = UNSET
        if not isinstance(self.memory_at, Unset):
            memory_at = self.memory_at.isoformat()

        seen_at: Union[Unset, str] = UNSET
        if not isinstance(self.seen_at, Unset):
            seen_at = self.seen_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_saved is not UNSET:
            field_dict["isSaved"] = is_saved
        if memory_at is not UNSET:
            field_dict["memoryAt"] = memory_at
        if seen_at is not UNSET:
            field_dict["seenAt"] = seen_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_saved = d.pop("isSaved", UNSET)

        _memory_at = d.pop("memoryAt", UNSET)
        memory_at: Union[Unset, datetime.datetime]
        if isinstance(_memory_at, Unset):
            memory_at = UNSET
        else:
            memory_at = isoparse(_memory_at)

        _seen_at = d.pop("seenAt", UNSET)
        seen_at: Union[Unset, datetime.datetime]
        if isinstance(_seen_at, Unset):
            seen_at = UNSET
        else:
            seen_at = isoparse(_seen_at)

        memory_update_dto = cls(
            is_saved=is_saved,
            memory_at=memory_at,
            seen_at=seen_at,
        )

        memory_update_dto.additional_properties = d
        return memory_update_dto

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
