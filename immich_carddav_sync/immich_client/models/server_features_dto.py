from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerFeaturesDto")


@_attrs_define
class ServerFeaturesDto:
    """
    Attributes:
        config_file (bool):
        duplicate_detection (bool):
        email (bool):
        facial_recognition (bool):
        import_faces (bool):
        map_ (bool):
        oauth (bool):
        oauth_auto_launch (bool):
        password_login (bool):
        reverse_geocoding (bool):
        search (bool):
        sidecar (bool):
        smart_search (bool):
        trash (bool):
    """

    config_file: bool
    duplicate_detection: bool
    email: bool
    facial_recognition: bool
    import_faces: bool
    map_: bool
    oauth: bool
    oauth_auto_launch: bool
    password_login: bool
    reverse_geocoding: bool
    search: bool
    sidecar: bool
    smart_search: bool
    trash: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_file = self.config_file

        duplicate_detection = self.duplicate_detection

        email = self.email

        facial_recognition = self.facial_recognition

        import_faces = self.import_faces

        map_ = self.map_

        oauth = self.oauth

        oauth_auto_launch = self.oauth_auto_launch

        password_login = self.password_login

        reverse_geocoding = self.reverse_geocoding

        search = self.search

        sidecar = self.sidecar

        smart_search = self.smart_search

        trash = self.trash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configFile": config_file,
                "duplicateDetection": duplicate_detection,
                "email": email,
                "facialRecognition": facial_recognition,
                "importFaces": import_faces,
                "map": map_,
                "oauth": oauth,
                "oauthAutoLaunch": oauth_auto_launch,
                "passwordLogin": password_login,
                "reverseGeocoding": reverse_geocoding,
                "search": search,
                "sidecar": sidecar,
                "smartSearch": smart_search,
                "trash": trash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_file = d.pop("configFile")

        duplicate_detection = d.pop("duplicateDetection")

        email = d.pop("email")

        facial_recognition = d.pop("facialRecognition")

        import_faces = d.pop("importFaces")

        map_ = d.pop("map")

        oauth = d.pop("oauth")

        oauth_auto_launch = d.pop("oauthAutoLaunch")

        password_login = d.pop("passwordLogin")

        reverse_geocoding = d.pop("reverseGeocoding")

        search = d.pop("search")

        sidecar = d.pop("sidecar")

        smart_search = d.pop("smartSearch")

        trash = d.pop("trash")

        server_features_dto = cls(
            config_file=config_file,
            duplicate_detection=duplicate_detection,
            email=email,
            facial_recognition=facial_recognition,
            import_faces=import_faces,
            map_=map_,
            oauth=oauth,
            oauth_auto_launch=oauth_auto_launch,
            password_login=password_login,
            reverse_geocoding=reverse_geocoding,
            search=search,
            sidecar=sidecar,
            smart_search=smart_search,
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
