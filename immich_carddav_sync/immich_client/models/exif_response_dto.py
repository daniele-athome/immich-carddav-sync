import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExifResponseDto")


@_attrs_define
class ExifResponseDto:
    """
    Attributes:
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        date_time_original (Union[Unset, None, datetime.datetime]):
        description (Union[Unset, None, str]):
        exif_image_height (Union[Unset, None, float]):
        exif_image_width (Union[Unset, None, float]):
        exposure_time (Union[Unset, None, str]):
        f_number (Union[Unset, None, float]):
        file_size_in_byte (Union[Unset, None, int]):
        focal_length (Union[Unset, None, float]):
        iso (Union[Unset, None, float]):
        latitude (Union[Unset, None, float]):
        lens_model (Union[Unset, None, str]):
        longitude (Union[Unset, None, float]):
        make (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        modify_date (Union[Unset, None, datetime.datetime]):
        orientation (Union[Unset, None, str]):
        projection_type (Union[Unset, None, str]):
        state (Union[Unset, None, str]):
        time_zone (Union[Unset, None, str]):
    """

    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    date_time_original: Union[Unset, None, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    exif_image_height: Union[Unset, None, float] = UNSET
    exif_image_width: Union[Unset, None, float] = UNSET
    exposure_time: Union[Unset, None, str] = UNSET
    f_number: Union[Unset, None, float] = UNSET
    file_size_in_byte: Union[Unset, None, int] = UNSET
    focal_length: Union[Unset, None, float] = UNSET
    iso: Union[Unset, None, float] = UNSET
    latitude: Union[Unset, None, float] = UNSET
    lens_model: Union[Unset, None, str] = UNSET
    longitude: Union[Unset, None, float] = UNSET
    make: Union[Unset, None, str] = UNSET
    model: Union[Unset, None, str] = UNSET
    modify_date: Union[Unset, None, datetime.datetime] = UNSET
    orientation: Union[Unset, None, str] = UNSET
    projection_type: Union[Unset, None, str] = UNSET
    state: Union[Unset, None, str] = UNSET
    time_zone: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city
        country = self.country
        date_time_original: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_time_original, Unset):
            date_time_original = self.date_time_original.isoformat() if self.date_time_original else None

        description = self.description
        exif_image_height = self.exif_image_height
        exif_image_width = self.exif_image_width
        exposure_time = self.exposure_time
        f_number = self.f_number
        file_size_in_byte = self.file_size_in_byte
        focal_length = self.focal_length
        iso = self.iso
        latitude = self.latitude
        lens_model = self.lens_model
        longitude = self.longitude
        make = self.make
        model = self.model
        modify_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modify_date, Unset):
            modify_date = self.modify_date.isoformat() if self.modify_date else None

        orientation = self.orientation
        projection_type = self.projection_type
        state = self.state
        time_zone = self.time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if date_time_original is not UNSET:
            field_dict["dateTimeOriginal"] = date_time_original
        if description is not UNSET:
            field_dict["description"] = description
        if exif_image_height is not UNSET:
            field_dict["exifImageHeight"] = exif_image_height
        if exif_image_width is not UNSET:
            field_dict["exifImageWidth"] = exif_image_width
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if f_number is not UNSET:
            field_dict["fNumber"] = f_number
        if file_size_in_byte is not UNSET:
            field_dict["fileSizeInByte"] = file_size_in_byte
        if focal_length is not UNSET:
            field_dict["focalLength"] = focal_length
        if iso is not UNSET:
            field_dict["iso"] = iso
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if lens_model is not UNSET:
            field_dict["lensModel"] = lens_model
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if modify_date is not UNSET:
            field_dict["modifyDate"] = modify_date
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if projection_type is not UNSET:
            field_dict["projectionType"] = projection_type
        if state is not UNSET:
            field_dict["state"] = state
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        _date_time_original = d.pop("dateTimeOriginal", UNSET)
        date_time_original: Union[Unset, None, datetime.datetime]
        if _date_time_original is None:
            date_time_original = None
        elif isinstance(_date_time_original, Unset):
            date_time_original = UNSET
        else:
            date_time_original = isoparse(_date_time_original)

        description = d.pop("description", UNSET)

        exif_image_height = d.pop("exifImageHeight", UNSET)

        exif_image_width = d.pop("exifImageWidth", UNSET)

        exposure_time = d.pop("exposureTime", UNSET)

        f_number = d.pop("fNumber", UNSET)

        file_size_in_byte = d.pop("fileSizeInByte", UNSET)

        focal_length = d.pop("focalLength", UNSET)

        iso = d.pop("iso", UNSET)

        latitude = d.pop("latitude", UNSET)

        lens_model = d.pop("lensModel", UNSET)

        longitude = d.pop("longitude", UNSET)

        make = d.pop("make", UNSET)

        model = d.pop("model", UNSET)

        _modify_date = d.pop("modifyDate", UNSET)
        modify_date: Union[Unset, None, datetime.datetime]
        if _modify_date is None:
            modify_date = None
        elif isinstance(_modify_date, Unset):
            modify_date = UNSET
        else:
            modify_date = isoparse(_modify_date)

        orientation = d.pop("orientation", UNSET)

        projection_type = d.pop("projectionType", UNSET)

        state = d.pop("state", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        exif_response_dto = cls(
            city=city,
            country=country,
            date_time_original=date_time_original,
            description=description,
            exif_image_height=exif_image_height,
            exif_image_width=exif_image_width,
            exposure_time=exposure_time,
            f_number=f_number,
            file_size_in_byte=file_size_in_byte,
            focal_length=focal_length,
            iso=iso,
            latitude=latitude,
            lens_model=lens_model,
            longitude=longitude,
            make=make,
            model=model,
            modify_date=modify_date,
            orientation=orientation,
            projection_type=projection_type,
            state=state,
            time_zone=time_zone,
        )

        exif_response_dto.additional_properties = d
        return exif_response_dto

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
