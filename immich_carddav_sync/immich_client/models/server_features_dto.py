from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerFeaturesDto")


@_attrs_define
class ServerFeaturesDto:
    """
    Attributes:
        clip_encode (bool):
        config_file (bool):
        facial_recognition (bool):
        map_ (bool):
        oauth (bool):
        oauth_auto_launch (bool):
        password_login (bool):
        reverse_geocoding (bool):
        search (bool):
        sidecar (bool):
        tag_image (bool):
        trash (bool):
    """

    clip_encode: bool
    config_file: bool
    facial_recognition: bool
    map_: bool
    oauth: bool
    oauth_auto_launch: bool
    password_login: bool
    reverse_geocoding: bool
    search: bool
    sidecar: bool
    tag_image: bool
    trash: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clip_encode = self.clip_encode
        config_file = self.config_file
        facial_recognition = self.facial_recognition
        map_ = self.map_
        oauth = self.oauth
        oauth_auto_launch = self.oauth_auto_launch
        password_login = self.password_login
        reverse_geocoding = self.reverse_geocoding
        search = self.search
        sidecar = self.sidecar
        tag_image = self.tag_image
        trash = self.trash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clipEncode": clip_encode,
                "configFile": config_file,
                "facialRecognition": facial_recognition,
                "map": map_,
                "oauth": oauth,
                "oauthAutoLaunch": oauth_auto_launch,
                "passwordLogin": password_login,
                "reverseGeocoding": reverse_geocoding,
                "search": search,
                "sidecar": sidecar,
                "tagImage": tag_image,
                "trash": trash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clip_encode = d.pop("clipEncode")

        config_file = d.pop("configFile")

        facial_recognition = d.pop("facialRecognition")

        map_ = d.pop("map")

        oauth = d.pop("oauth")

        oauth_auto_launch = d.pop("oauthAutoLaunch")

        password_login = d.pop("passwordLogin")

        reverse_geocoding = d.pop("reverseGeocoding")

        search = d.pop("search")

        sidecar = d.pop("sidecar")

        tag_image = d.pop("tagImage")

        trash = d.pop("trash")

        server_features_dto = cls(
            clip_encode=clip_encode,
            config_file=config_file,
            facial_recognition=facial_recognition,
            map_=map_,
            oauth=oauth,
            oauth_auto_launch=oauth_auto_launch,
            password_login=password_login,
            reverse_geocoding=reverse_geocoding,
            search=search,
            sidecar=sidecar,
            tag_image=tag_image,
            trash=trash,
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
