from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmartInfoResponseDto")


@_attrs_define
class SmartInfoResponseDto:
    """
    Attributes:
        objects (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
    """

    objects: Union[Unset, None, List[str]] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.objects, Unset):
            if self.objects is None:
                objects = None
            else:
                objects = self.objects

        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        objects = cast(List[str], d.pop("objects", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

        smart_info_response_dto = cls(
            objects=objects,
            tags=tags,
        )

        smart_info_response_dto.additional_properties = d
        return smart_info_response_dto

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
