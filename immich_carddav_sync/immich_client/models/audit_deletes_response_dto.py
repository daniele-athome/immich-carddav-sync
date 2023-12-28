from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditDeletesResponseDto")


@_attrs_define
class AuditDeletesResponseDto:
    """
    Attributes:
        ids (List[str]):
        needs_full_sync (bool):
    """

    ids: List[str]
    needs_full_sync: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids = self.ids

        needs_full_sync = self.needs_full_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "needsFullSync": needs_full_sync,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(List[str], d.pop("ids"))

        needs_full_sync = d.pop("needsFullSync")

        audit_deletes_response_dto = cls(
            ids=ids,
            needs_full_sync=needs_full_sync,
        )

        audit_deletes_response_dto.additional_properties = d
        return audit_deletes_response_dto

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
