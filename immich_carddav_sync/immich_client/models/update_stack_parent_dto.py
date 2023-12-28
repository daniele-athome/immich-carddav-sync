from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateStackParentDto")


@_attrs_define
class UpdateStackParentDto:
    """
    Attributes:
        new_parent_id (str):
        old_parent_id (str):
    """

    new_parent_id: str
    old_parent_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_parent_id = self.new_parent_id
        old_parent_id = self.old_parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newParentId": new_parent_id,
                "oldParentId": old_parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_parent_id = d.pop("newParentId")

        old_parent_id = d.pop("oldParentId")

        update_stack_parent_dto = cls(
            new_parent_id=new_parent_id,
            old_parent_id=old_parent_id,
        )

        update_stack_parent_dto.additional_properties = d
        return update_stack_parent_dto

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
