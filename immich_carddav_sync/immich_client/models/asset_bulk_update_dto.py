from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetBulkUpdateDto")


@_attrs_define
class AssetBulkUpdateDto:
    """
    Attributes:
        ids (List[UUID]):
        date_time_original (Union[Unset, str]):
        duplicate_id (Union[None, Unset, str]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        latitude (Union[Unset, float]):
        longitude (Union[Unset, float]):
        rating (Union[Unset, float]):
    """

    ids: List[UUID]
    date_time_original: Union[Unset, str] = UNSET
    duplicate_id: Union[None, Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    rating: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids = []
        for ids_item_data in self.ids:
            ids_item = str(ids_item_data)
            ids.append(ids_item)

        date_time_original = self.date_time_original

        duplicate_id: Union[None, Unset, str]
        if isinstance(self.duplicate_id, Unset):
            duplicate_id = UNSET
        else:
            duplicate_id = self.duplicate_id

        is_archived = self.is_archived

        is_favorite = self.is_favorite

        latitude = self.latitude

        longitude = self.longitude

        rating = self.rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if date_time_original is not UNSET:
            field_dict["dateTimeOriginal"] = date_time_original
        if duplicate_id is not UNSET:
            field_dict["duplicateId"] = duplicate_id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = []
        _ids = d.pop("ids")
        for ids_item_data in _ids:
            ids_item = UUID(ids_item_data)

            ids.append(ids_item)

        date_time_original = d.pop("dateTimeOriginal", UNSET)

        def _parse_duplicate_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        duplicate_id = _parse_duplicate_id(d.pop("duplicateId", UNSET))

        is_archived = d.pop("isArchived", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        rating = d.pop("rating", UNSET)

        asset_bulk_update_dto = cls(
            ids=ids,
            date_time_original=date_time_original,
            duplicate_id=duplicate_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            latitude=latitude,
            longitude=longitude,
            rating=rating,
        )

        asset_bulk_update_dto.additional_properties = d
        return asset_bulk_update_dto

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
