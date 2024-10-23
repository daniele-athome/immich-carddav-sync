from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemConfigSmtpTransportDto")


@_attrs_define
class SystemConfigSmtpTransportDto:
    """
    Attributes:
        host (str):
        ignore_cert (bool):
        password (str):
        port (float):
        username (str):
    """

    host: str
    ignore_cert: bool
    password: str
    port: float
    username: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        ignore_cert = self.ignore_cert

        password = self.password

        port = self.port

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "ignoreCert": ignore_cert,
                "password": password,
                "port": port,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host")

        ignore_cert = d.pop("ignoreCert")

        password = d.pop("password")

        port = d.pop("port")

        username = d.pop("username")

        system_config_smtp_transport_dto = cls(
            host=host,
            ignore_cert=ignore_cert,
            password=password,
            port=port,
            username=username,
        )

        system_config_smtp_transport_dto.additional_properties = d
        return system_config_smtp_transport_dto

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
