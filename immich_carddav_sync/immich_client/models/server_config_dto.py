from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerConfigDto")


@_attrs_define
class ServerConfigDto:
    """
    Attributes:
        is_initialized (bool):
        login_page_message (str):
        oauth_button_text (str):
        trash_days (int):
    """

    is_initialized: bool
    login_page_message: str
    oauth_button_text: str
    trash_days: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_initialized = self.is_initialized
        login_page_message = self.login_page_message
        oauth_button_text = self.oauth_button_text
        trash_days = self.trash_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isInitialized": is_initialized,
                "loginPageMessage": login_page_message,
                "oauthButtonText": oauth_button_text,
                "trashDays": trash_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_initialized = d.pop("isInitialized")

        login_page_message = d.pop("loginPageMessage")

        oauth_button_text = d.pop("oauthButtonText")

        trash_days = d.pop("trashDays")

        server_config_dto = cls(
            is_initialized=is_initialized,
            login_page_message=login_page_message,
            oauth_button_text=oauth_button_text,
            trash_days=trash_days,
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
