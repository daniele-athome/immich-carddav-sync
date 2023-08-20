from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerFeaturesDto")


@_attrs_define
class ServerFeaturesDto:
    """
    Attributes:
        machine_learning (bool):
        oauth (bool):
        oauth_auto_launch (bool):
        password_login (bool):
        search (bool):
    """

    machine_learning: bool
    oauth: bool
    oauth_auto_launch: bool
    password_login: bool
    search: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_learning = self.machine_learning
        oauth = self.oauth
        oauth_auto_launch = self.oauth_auto_launch
        password_login = self.password_login
        search = self.search

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machineLearning": machine_learning,
                "oauth": oauth,
                "oauthAutoLaunch": oauth_auto_launch,
                "passwordLogin": password_login,
                "search": search,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        machine_learning = d.pop("machineLearning")

        oauth = d.pop("oauth")

        oauth_auto_launch = d.pop("oauthAutoLaunch")

        password_login = d.pop("passwordLogin")

        search = d.pop("search")

        server_features_dto = cls(
            machine_learning=machine_learning,
            oauth=oauth,
            oauth_auto_launch=oauth_auto_launch,
            password_login=password_login,
            search=search,
        )

        server_features_dto.additional_properties = d
        return server_features_dto

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
