from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_config_library_scan_dto import SystemConfigLibraryScanDto
    from ..models.system_config_library_watch_dto import SystemConfigLibraryWatchDto


T = TypeVar("T", bound="SystemConfigLibraryDto")


@_attrs_define
class SystemConfigLibraryDto:
    """
    Attributes:
        scan (SystemConfigLibraryScanDto):
        watch (SystemConfigLibraryWatchDto):
    """

    scan: "SystemConfigLibraryScanDto"
    watch: "SystemConfigLibraryWatchDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan = self.scan.to_dict()

        watch = self.watch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan": scan,
                "watch": watch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_config_library_scan_dto import SystemConfigLibraryScanDto
        from ..models.system_config_library_watch_dto import SystemConfigLibraryWatchDto

        d = src_dict.copy()
        scan = SystemConfigLibraryScanDto.from_dict(d.pop("scan"))

        watch = SystemConfigLibraryWatchDto.from_dict(d.pop("watch"))

        system_config_library_dto = cls(
            scan=scan,
            watch=watch,
        )

        system_config_library_dto.additional_properties = d
        return system_config_library_dto

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
