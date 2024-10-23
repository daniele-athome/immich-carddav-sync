from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_config_smtp_transport_dto import SystemConfigSmtpTransportDto


T = TypeVar("T", bound="SystemConfigSmtpDto")


@_attrs_define
class SystemConfigSmtpDto:
    """
    Attributes:
        enabled (bool):
        from_ (str):
        reply_to (str):
        transport (SystemConfigSmtpTransportDto):
    """

    enabled: bool
    from_: str
    reply_to: str
    transport: "SystemConfigSmtpTransportDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        from_ = self.from_

        reply_to = self.reply_to

        transport = self.transport.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "from": from_,
                "replyTo": reply_to,
                "transport": transport,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_config_smtp_transport_dto import SystemConfigSmtpTransportDto

        d = src_dict.copy()
        enabled = d.pop("enabled")

        from_ = d.pop("from")

        reply_to = d.pop("replyTo")

        transport = SystemConfigSmtpTransportDto.from_dict(d.pop("transport"))

        system_config_smtp_dto = cls(
            enabled=enabled,
            from_=from_,
            reply_to=reply_to,
            transport=transport,
        )

        system_config_smtp_dto.additional_properties = d
        return system_config_smtp_dto

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
