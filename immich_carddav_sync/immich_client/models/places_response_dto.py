from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlacesResponseDto")


@_attrs_define
class PlacesResponseDto:
    """
    Attributes:
        latitude (float):
        longitude (float):
        name (str):
        admin1name (Union[Unset, str]):
        admin2name (Union[Unset, str]):
    """

    latitude: float
    longitude: float
    name: str
    admin1name: Union[Unset, str] = UNSET
    admin2name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        admin1name = self.admin1name

        admin2name = self.admin2name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
            }
        )
        if admin1name is not UNSET:
            field_dict["admin1name"] = admin1name
        if admin2name is not UNSET:
            field_dict["admin2name"] = admin2name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        name = d.pop("name")

        admin1name = d.pop("admin1name", UNSET)

        admin2name = d.pop("admin2name", UNSET)

        places_response_dto = cls(
            latitude=latitude,
            longitude=longitude,
            name=name,
            admin1name=admin1name,
            admin2name=admin2name,
        )

        places_response_dto.additional_properties = d
        return places_response_dto

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
