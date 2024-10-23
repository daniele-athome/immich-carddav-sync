import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExifResponseDto")


@_attrs_define
class ExifResponseDto:
    """
    Attributes:
        city (Union[None, Unset, str]):
        country (Union[None, Unset, str]):
        date_time_original (Union[None, Unset, datetime.datetime]):
        description (Union[None, Unset, str]):
        exif_image_height (Union[None, Unset, float]):
        exif_image_width (Union[None, Unset, float]):
        exposure_time (Union[None, Unset, str]):
        f_number (Union[None, Unset, float]):
        file_size_in_byte (Union[None, Unset, int]):
        focal_length (Union[None, Unset, float]):
        iso (Union[None, Unset, float]):
        latitude (Union[None, Unset, float]):
        lens_model (Union[None, Unset, str]):
        longitude (Union[None, Unset, float]):
        make (Union[None, Unset, str]):
        model (Union[None, Unset, str]):
        modify_date (Union[None, Unset, datetime.datetime]):
        orientation (Union[None, Unset, str]):
        projection_type (Union[None, Unset, str]):
        rating (Union[None, Unset, float]):
        state (Union[None, Unset, str]):
        time_zone (Union[None, Unset, str]):
    """

    city: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    date_time_original: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    exif_image_height: Union[None, Unset, float] = UNSET
    exif_image_width: Union[None, Unset, float] = UNSET
    exposure_time: Union[None, Unset, str] = UNSET
    f_number: Union[None, Unset, float] = UNSET
    file_size_in_byte: Union[None, Unset, int] = UNSET
    focal_length: Union[None, Unset, float] = UNSET
    iso: Union[None, Unset, float] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    lens_model: Union[None, Unset, str] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    make: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    modify_date: Union[None, Unset, datetime.datetime] = UNSET
    orientation: Union[None, Unset, str] = UNSET
    projection_type: Union[None, Unset, str] = UNSET
    rating: Union[None, Unset, float] = UNSET
    state: Union[None, Unset, str] = UNSET
    time_zone: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        date_time_original: Union[None, Unset, str]
        if isinstance(self.date_time_original, Unset):
            date_time_original = UNSET
        elif isinstance(self.date_time_original, datetime.datetime):
            date_time_original = self.date_time_original.isoformat()
        else:
            date_time_original = self.date_time_original

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        exif_image_height: Union[None, Unset, float]
        if isinstance(self.exif_image_height, Unset):
            exif_image_height = UNSET
        else:
            exif_image_height = self.exif_image_height

        exif_image_width: Union[None, Unset, float]
        if isinstance(self.exif_image_width, Unset):
            exif_image_width = UNSET
        else:
            exif_image_width = self.exif_image_width

        exposure_time: Union[None, Unset, str]
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        f_number: Union[None, Unset, float]
        if isinstance(self.f_number, Unset):
            f_number = UNSET
        else:
            f_number = self.f_number

        file_size_in_byte: Union[None, Unset, int]
        if isinstance(self.file_size_in_byte, Unset):
            file_size_in_byte = UNSET
        else:
            file_size_in_byte = self.file_size_in_byte

        focal_length: Union[None, Unset, float]
        if isinstance(self.focal_length, Unset):
            focal_length = UNSET
        else:
            focal_length = self.focal_length

        iso: Union[None, Unset, float]
        if isinstance(self.iso, Unset):
            iso = UNSET
        else:
            iso = self.iso

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        lens_model: Union[None, Unset, str]
        if isinstance(self.lens_model, Unset):
            lens_model = UNSET
        else:
            lens_model = self.lens_model

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        make: Union[None, Unset, str]
        if isinstance(self.make, Unset):
            make = UNSET
        else:
            make = self.make

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        modify_date: Union[None, Unset, str]
        if isinstance(self.modify_date, Unset):
            modify_date = UNSET
        elif isinstance(self.modify_date, datetime.datetime):
            modify_date = self.modify_date.isoformat()
        else:
            modify_date = self.modify_date

        orientation: Union[None, Unset, str]
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        projection_type: Union[None, Unset, str]
        if isinstance(self.projection_type, Unset):
            projection_type = UNSET
        else:
            projection_type = self.projection_type

        rating: Union[None, Unset, float]
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        time_zone: Union[None, Unset, str]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
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
        if rating is not UNSET:
            field_dict["rating"] = rating
        if state is not UNSET:
            field_dict["state"] = state
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_date_time_original(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_time_original_type_0 = isoparse(data)

                return date_time_original_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_time_original = _parse_date_time_original(d.pop("dateTimeOriginal", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_exif_image_height(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        exif_image_height = _parse_exif_image_height(d.pop("exifImageHeight", UNSET))

        def _parse_exif_image_width(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        exif_image_width = _parse_exif_image_width(d.pop("exifImageWidth", UNSET))

        def _parse_exposure_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime", UNSET))

        def _parse_f_number(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        f_number = _parse_f_number(d.pop("fNumber", UNSET))

        def _parse_file_size_in_byte(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        file_size_in_byte = _parse_file_size_in_byte(d.pop("fileSizeInByte", UNSET))

        def _parse_focal_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        focal_length = _parse_focal_length(d.pop("focalLength", UNSET))

        def _parse_iso(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        iso = _parse_iso(d.pop("iso", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_lens_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lens_model = _parse_lens_model(d.pop("lensModel", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_make(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        make = _parse_make(d.pop("make", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_modify_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modify_date_type_0 = isoparse(data)

                return modify_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        modify_date = _parse_modify_date(d.pop("modifyDate", UNSET))

        def _parse_orientation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_projection_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        projection_type = _parse_projection_type(d.pop("projectionType", UNSET))

        def _parse_rating(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_time_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

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
            rating=rating,
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
