from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MapMarkerResponseDto")


@_attrs_define
class MapMarkerResponseDto:
    """
    Attributes:
        id (str):
        lat (float):
        lon (float):
    """

    id: str
    lat: float
    lon: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        lat = self.lat
        lon = self.lon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "lat": lat,
                "lon": lon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        lat = d.pop("lat")

        lon = d.pop("lon")

        map_marker_response_dto = cls(
            id=id,
            lat=lat,
            lon=lon,
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
