from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemConfigLibraryScanDto")


@_attrs_define
class SystemConfigLibraryScanDto:
    """
    Attributes:
        cron_expression (str):
        enabled (bool):
    """

    cron_expression: str
    enabled: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cron_expression = self.cron_expression
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cronExpression": cron_expression,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cron_expression = d.pop("cronExpression")

        enabled = d.pop("enabled")

        system_config_library_scan_dto = cls(
            cron_expression=cron_expression,
            enabled=enabled,
        )

        system_config_library_scan_dto.additional_properties = d
        return system_config_library_scan_dto

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
