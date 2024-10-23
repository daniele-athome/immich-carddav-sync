from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssetDto")


@_attrs_define
class UpdateAssetDto:
    """
    Attributes:
        date_time_original (Union[Unset, str]):
        description (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        latitude (Union[Unset, float]):
        live_photo_video_id (Union[None, UUID, Unset]):
        longitude (Union[Unset, float]):
        rating (Union[Unset, float]):
    """

    date_time_original: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    latitude: Union[Unset, float] = UNSET
    live_photo_video_id: Union[None, UUID, Unset] = UNSET
    longitude: Union[Unset, float] = UNSET
    rating: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_time_original = self.date_time_original

        description = self.description

        is_archived = self.is_archived

        is_favorite = self.is_favorite

        latitude = self.latitude

        live_photo_video_id: Union[None, Unset, str]
        if isinstance(self.live_photo_video_id, Unset):
            live_photo_video_id = UNSET
        elif isinstance(self.live_photo_video_id, UUID):
            live_photo_video_id = str(self.live_photo_video_id)
        else:
            live_photo_video_id = self.live_photo_video_id

        longitude = self.longitude

        rating = self.rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_time_original is not UNSET:
            field_dict["dateTimeOriginal"] = date_time_original
        if description is not UNSET:
            field_dict["description"] = description
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if live_photo_video_id is not UNSET:
            field_dict["livePhotoVideoId"] = live_photo_video_id
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_time_original = d.pop("dateTimeOriginal", UNSET)

        description = d.pop("description", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        latitude = d.pop("latitude", UNSET)

        def _parse_live_photo_video_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                live_photo_video_id_type_0 = UUID(data)

                return live_photo_video_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        live_photo_video_id = _parse_live_photo_video_id(d.pop("livePhotoVideoId", UNSET))

        longitude = d.pop("longitude", UNSET)

        rating = d.pop("rating", UNSET)

        update_asset_dto = cls(
            date_time_original=date_time_original,
            description=description,
            is_archived=is_archived,
            is_favorite=is_favorite,
            latitude=latitude,
            live_photo_video_id=live_photo_video_id,
            longitude=longitude,
            rating=rating,
        )

        update_asset_dto.additional_properties = d
        return update_asset_dto

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
