from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MapMarkerResponseDto")


@_attrs_define
class MapMarkerResponseDto:
    """
    Attributes:
        city (Union[None, str]):
        country (Union[None, str]):
        id (str):
        lat (float):
        lon (float):
        state (Union[None, str]):
    """

    city: Union[None, str]
    country: Union[None, str]
    id: str
    lat: float
    lon: float
    state: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city: Union[None, str]
        city = self.city

        country: Union[None, str]
        country = self.country

        id = self.id

        lat = self.lat

        lon = self.lon

        state: Union[None, str]
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "country": country,
                "id": id,
                "lat": lat,
                "lon": lon,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_city(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        city = _parse_city(d.pop("city"))

        def _parse_country(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        country = _parse_country(d.pop("country"))

        id = d.pop("id")

        lat = d.pop("lat")

        lon = d.pop("lon")

        def _parse_state(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        state = _parse_state(d.pop("state"))

        map_marker_response_dto = cls(
            city=city,
            country=country,
            id=id,
            lat=lat,
            lon=lon,
            state=state,
        )

        map_marker_response_dto.additional_properties = d
        return map_marker_response_dto

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
