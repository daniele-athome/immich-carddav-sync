from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmartInfoResponseDto")


@_attrs_define
class SmartInfoResponseDto:
    """
    Attributes:
        objects (Union[List[str], None, Unset]):
        tags (Union[List[str], None, Unset]):
    """

    objects: Union[List[str], None, Unset] = UNSET
    tags: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[List[str], None, Unset]
        if isinstance(self.objects, Unset):
            objects = UNSET
        elif isinstance(self.objects, list):
            objects = self.objects

        else:
            objects = self.objects

        tags: Union[List[str], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

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

        def _parse_objects(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objects_type_0 = cast(List[str], data)

                return objects_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        objects = _parse_objects(d.pop("objects", UNSET))

        def _parse_tags(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(List[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))

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
