from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateLibraryImportPathResponseDto")


@_attrs_define
class ValidateLibraryImportPathResponseDto:
    """
    Attributes:
        import_path (str):
        is_valid (bool):  Default: False.
        message (Union[Unset, str]):
    """

    import_path: str
    is_valid: bool = False
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_path = self.import_path

        is_valid = self.is_valid

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importPath": import_path,
                "isValid": is_valid,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        import_path = d.pop("importPath")

        is_valid = d.pop("isValid")

        message = d.pop("message", UNSET)

        validate_library_import_path_response_dto = cls(
            import_path=import_path,
            is_valid=is_valid,
            message=message,
        )

        validate_library_import_path_response_dto.additional_properties = d
        return validate_library_import_path_response_dto

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
