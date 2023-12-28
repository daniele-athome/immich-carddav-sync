from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemConfigMapDto")


@_attrs_define
class SystemConfigMapDto:
    """
    Attributes:
        dark_style (str):
        enabled (bool):
        light_style (str):
    """

    dark_style: str
    enabled: bool
    light_style: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dark_style = self.dark_style
        enabled = self.enabled
        light_style = self.light_style

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "darkStyle": dark_style,
                "enabled": enabled,
                "lightStyle": light_style,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dark_style = d.pop("darkStyle")

        enabled = d.pop("enabled")

        light_style = d.pop("lightStyle")

        system_config_map_dto = cls(
            dark_style=dark_style,
            enabled=enabled,
            light_style=light_style,
        )

        system_config_map_dto.additional_properties = d
        return system_config_map_dto

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
