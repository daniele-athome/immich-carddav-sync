from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.library_type import LibraryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLibraryDto")


@_attrs_define
class CreateLibraryDto:
    """
    Attributes:
        type (LibraryType):
        exclusion_patterns (Union[Unset, List[str]]):
        import_paths (Union[Unset, List[str]]):
        is_visible (Union[Unset, bool]):
        name (Union[Unset, str]):
    """

    type: LibraryType
    exclusion_patterns: Union[Unset, List[str]] = UNSET
    import_paths: Union[Unset, List[str]] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        exclusion_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclusion_patterns, Unset):
            exclusion_patterns = self.exclusion_patterns

        import_paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.import_paths, Unset):
            import_paths = self.import_paths

        is_visible = self.is_visible
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if exclusion_patterns is not UNSET:
            field_dict["exclusionPatterns"] = exclusion_patterns
        if import_paths is not UNSET:
            field_dict["importPaths"] = import_paths
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = LibraryType(d.pop("type"))

        exclusion_patterns = cast(List[str], d.pop("exclusionPatterns", UNSET))

        import_paths = cast(List[str], d.pop("importPaths", UNSET))

        is_visible = d.pop("isVisible", UNSET)

        name = d.pop("name", UNSET)

        create_library_dto = cls(
            type=type,
            exclusion_patterns=exclusion_patterns,
            import_paths=import_paths,
            is_visible=is_visible,
            name=name,
        )

        create_library_dto.additional_properties = d
        return create_library_dto

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
