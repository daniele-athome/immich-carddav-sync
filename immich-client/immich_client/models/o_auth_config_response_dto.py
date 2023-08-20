from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthConfigResponseDto")


@_attrs_define
class OAuthConfigResponseDto:
    """
    Attributes:
        enabled (bool):
        password_login_enabled (bool):
        auto_launch (Union[Unset, bool]):
        button_text (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    enabled: bool
    password_login_enabled: bool
    auto_launch: Union[Unset, bool] = UNSET
    button_text: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        password_login_enabled = self.password_login_enabled
        auto_launch = self.auto_launch
        button_text = self.button_text
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "passwordLoginEnabled": password_login_enabled,
            }
        )
        if auto_launch is not UNSET:
            field_dict["autoLaunch"] = auto_launch
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        password_login_enabled = d.pop("passwordLoginEnabled")

        auto_launch = d.pop("autoLaunch", UNSET)

        button_text = d.pop("buttonText", UNSET)

        url = d.pop("url", UNSET)

        o_auth_config_response_dto = cls(
            enabled=enabled,
            password_login_enabled=password_login_enabled,
            auto_launch=auto_launch,
            button_text=button_text,
            url=url,
        )

        o_auth_config_response_dto.additional_properties = d
        return o_auth_config_response_dto

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
