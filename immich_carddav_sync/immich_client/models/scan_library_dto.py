from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScanLibraryDto")


@_attrs_define
class ScanLibraryDto:
    """
    Attributes:
        refresh_all_files (Union[Unset, bool]):
        refresh_modified_files (Union[Unset, bool]):
    """

    refresh_all_files: Union[Unset, bool] = False
    refresh_modified_files: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh_all_files = self.refresh_all_files
        refresh_modified_files = self.refresh_modified_files

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refresh_all_files is not UNSET:
            field_dict["refreshAllFiles"] = refresh_all_files
        if refresh_modified_files is not UNSET:
            field_dict["refreshModifiedFiles"] = refresh_modified_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh_all_files = d.pop("refreshAllFiles", UNSET)

        refresh_modified_files = d.pop("refreshModifiedFiles", UNSET)

        scan_library_dto = cls(
            refresh_all_files=refresh_all_files,
            refresh_modified_files=refresh_modified_files,
        )

        scan_library_dto.additional_properties = d
        return scan_library_dto

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
