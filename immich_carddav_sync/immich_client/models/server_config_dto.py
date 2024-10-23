from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerConfigDto")


@_attrs_define
class ServerConfigDto:
    """
    Attributes:
        external_domain (str):
        is_initialized (bool):
        is_onboarded (bool):
        login_page_message (str):
        map_dark_style_url (str):
        map_light_style_url (str):
        oauth_button_text (str):
        trash_days (int):
        user_delete_delay (int):
    """

    external_domain: str
    is_initialized: bool
    is_onboarded: bool
    login_page_message: str
    map_dark_style_url: str
    map_light_style_url: str
    oauth_button_text: str
    trash_days: int
    user_delete_delay: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_domain = self.external_domain

        is_initialized = self.is_initialized

        is_onboarded = self.is_onboarded

        login_page_message = self.login_page_message

        map_dark_style_url = self.map_dark_style_url

        map_light_style_url = self.map_light_style_url

        oauth_button_text = self.oauth_button_text

        trash_days = self.trash_days

        user_delete_delay = self.user_delete_delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalDomain": external_domain,
                "isInitialized": is_initialized,
                "isOnboarded": is_onboarded,
                "loginPageMessage": login_page_message,
                "mapDarkStyleUrl": map_dark_style_url,
                "mapLightStyleUrl": map_light_style_url,
                "oauthButtonText": oauth_button_text,
                "trashDays": trash_days,
                "userDeleteDelay": user_delete_delay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_domain = d.pop("externalDomain")

        is_initialized = d.pop("isInitialized")

        is_onboarded = d.pop("isOnboarded")

        login_page_message = d.pop("loginPageMessage")

        map_dark_style_url = d.pop("mapDarkStyleUrl")

        map_light_style_url = d.pop("mapLightStyleUrl")

        oauth_button_text = d.pop("oauthButtonText")

        trash_days = d.pop("trashDays")

        user_delete_delay = d.pop("userDeleteDelay")

        server_config_dto = cls(
            external_domain=external_domain,
            is_initialized=is_initialized,
            is_onboarded=is_onboarded,
            login_page_message=login_page_message,
            map_dark_style_url=map_dark_style_url,
            map_light_style_url=map_light_style_url,
            oauth_button_text=oauth_button_text,
            trash_days=trash_days,
            user_delete_delay=user_delete_delay,
        )

        server_config_dto.additional_properties = d
        return server_config_dto

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
