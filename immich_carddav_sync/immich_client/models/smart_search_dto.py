import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.asset_type_enum import AssetTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SmartSearchDto")


@_attrs_define
class SmartSearchDto:
    """
    Attributes:
        query (str):
        city (Union[None, Unset, str]):
        country (Union[None, Unset, str]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        device_id (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_encoded (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_motion (Union[Unset, bool]):
        is_not_in_album (Union[Unset, bool]):
        is_offline (Union[Unset, bool]):
        is_visible (Union[Unset, bool]):
        lens_model (Union[None, Unset, str]):
        library_id (Union[None, UUID, Unset]):
        make (Union[Unset, str]):
        model (Union[None, Unset, str]):
        page (Union[Unset, float]):
        person_ids (Union[Unset, List[UUID]]):
        size (Union[Unset, float]):
        state (Union[None, Unset, str]):
        taken_after (Union[Unset, datetime.datetime]):
        taken_before (Union[Unset, datetime.datetime]):
        trashed_after (Union[Unset, datetime.datetime]):
        trashed_before (Union[Unset, datetime.datetime]):
        type (Union[Unset, AssetTypeEnum]):
        updated_after (Union[Unset, datetime.datetime]):
        updated_before (Union[Unset, datetime.datetime]):
        with_archived (Union[Unset, bool]):  Default: False.
        with_deleted (Union[Unset, bool]):
        with_exif (Union[Unset, bool]):
    """

    query: str
    city: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    created_after: Union[Unset, datetime.datetime] = UNSET
    created_before: Union[Unset, datetime.datetime] = UNSET
    device_id: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_encoded: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_motion: Union[Unset, bool] = UNSET
    is_not_in_album: Union[Unset, bool] = UNSET
    is_offline: Union[Unset, bool] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    lens_model: Union[None, Unset, str] = UNSET
    library_id: Union[None, UUID, Unset] = UNSET
    make: Union[Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    page: Union[Unset, float] = UNSET
    person_ids: Union[Unset, List[UUID]] = UNSET
    size: Union[Unset, float] = UNSET
    state: Union[None, Unset, str] = UNSET
    taken_after: Union[Unset, datetime.datetime] = UNSET
    taken_before: Union[Unset, datetime.datetime] = UNSET
    trashed_after: Union[Unset, datetime.datetime] = UNSET
    trashed_before: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, AssetTypeEnum] = UNSET
    updated_after: Union[Unset, datetime.datetime] = UNSET
    updated_before: Union[Unset, datetime.datetime] = UNSET
    with_archived: Union[Unset, bool] = False
    with_deleted: Union[Unset, bool] = UNSET
    with_exif: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

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

        created_after: Union[Unset, str] = UNSET
        if not isinstance(self.created_after, Unset):
            created_after = self.created_after.isoformat()

        created_before: Union[Unset, str] = UNSET
        if not isinstance(self.created_before, Unset):
            created_before = self.created_before.isoformat()

        device_id = self.device_id

        is_archived = self.is_archived

        is_encoded = self.is_encoded

        is_favorite = self.is_favorite

        is_motion = self.is_motion

        is_not_in_album = self.is_not_in_album

        is_offline = self.is_offline

        is_visible = self.is_visible

        lens_model: Union[None, Unset, str]
        if isinstance(self.lens_model, Unset):
            lens_model = UNSET
        else:
            lens_model = self.lens_model

        library_id: Union[None, Unset, str]
        if isinstance(self.library_id, Unset):
            library_id = UNSET
        elif isinstance(self.library_id, UUID):
            library_id = str(self.library_id)
        else:
            library_id = self.library_id

        make = self.make

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        page = self.page

        person_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.person_ids, Unset):
            person_ids = []
            for person_ids_item_data in self.person_ids:
                person_ids_item = str(person_ids_item_data)
                person_ids.append(person_ids_item)

        size = self.size

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        taken_after: Union[Unset, str] = UNSET
        if not isinstance(self.taken_after, Unset):
            taken_after = self.taken_after.isoformat()

        taken_before: Union[Unset, str] = UNSET
        if not isinstance(self.taken_before, Unset):
            taken_before = self.taken_before.isoformat()

        trashed_after: Union[Unset, str] = UNSET
        if not isinstance(self.trashed_after, Unset):
            trashed_after = self.trashed_after.isoformat()

        trashed_before: Union[Unset, str] = UNSET
        if not isinstance(self.trashed_before, Unset):
            trashed_before = self.trashed_before.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        updated_after: Union[Unset, str] = UNSET
        if not isinstance(self.updated_after, Unset):
            updated_after = self.updated_after.isoformat()

        updated_before: Union[Unset, str] = UNSET
        if not isinstance(self.updated_before, Unset):
            updated_before = self.updated_before.isoformat()

        with_archived = self.with_archived

        with_deleted = self.with_deleted

        with_exif = self.with_exif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if created_after is not UNSET:
            field_dict["createdAfter"] = created_after
        if created_before is not UNSET:
            field_dict["createdBefore"] = created_before
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_encoded is not UNSET:
            field_dict["isEncoded"] = is_encoded
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_motion is not UNSET:
            field_dict["isMotion"] = is_motion
        if is_not_in_album is not UNSET:
            field_dict["isNotInAlbum"] = is_not_in_album
        if is_offline is not UNSET:
            field_dict["isOffline"] = is_offline
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if lens_model is not UNSET:
            field_dict["lensModel"] = lens_model
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if page is not UNSET:
            field_dict["page"] = page
        if person_ids is not UNSET:
            field_dict["personIds"] = person_ids
        if size is not UNSET:
            field_dict["size"] = size
        if state is not UNSET:
            field_dict["state"] = state
        if taken_after is not UNSET:
            field_dict["takenAfter"] = taken_after
        if taken_before is not UNSET:
            field_dict["takenBefore"] = taken_before
        if trashed_after is not UNSET:
            field_dict["trashedAfter"] = trashed_after
        if trashed_before is not UNSET:
            field_dict["trashedBefore"] = trashed_before
        if type is not UNSET:
            field_dict["type"] = type
        if updated_after is not UNSET:
            field_dict["updatedAfter"] = updated_after
        if updated_before is not UNSET:
            field_dict["updatedBefore"] = updated_before
        if with_archived is not UNSET:
            field_dict["withArchived"] = with_archived
        if with_deleted is not UNSET:
            field_dict["withDeleted"] = with_deleted
        if with_exif is not UNSET:
            field_dict["withExif"] = with_exif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query")

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

        _created_after = d.pop("createdAfter", UNSET)
        created_after: Union[Unset, datetime.datetime]
        if isinstance(_created_after, Unset):
            created_after = UNSET
        else:
            created_after = isoparse(_created_after)

        _created_before = d.pop("createdBefore", UNSET)
        created_before: Union[Unset, datetime.datetime]
        if isinstance(_created_before, Unset):
            created_before = UNSET
        else:
            created_before = isoparse(_created_before)

        device_id = d.pop("deviceId", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_encoded = d.pop("isEncoded", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        is_motion = d.pop("isMotion", UNSET)

        is_not_in_album = d.pop("isNotInAlbum", UNSET)

        is_offline = d.pop("isOffline", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        def _parse_lens_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lens_model = _parse_lens_model(d.pop("lensModel", UNSET))

        def _parse_library_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                library_id_type_0 = UUID(data)

                return library_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        library_id = _parse_library_id(d.pop("libraryId", UNSET))

        make = d.pop("make", UNSET)

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        page = d.pop("page", UNSET)

        person_ids = []
        _person_ids = d.pop("personIds", UNSET)
        for person_ids_item_data in _person_ids or []:
            person_ids_item = UUID(person_ids_item_data)

            person_ids.append(person_ids_item)

        size = d.pop("size", UNSET)

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        _taken_after = d.pop("takenAfter", UNSET)
        taken_after: Union[Unset, datetime.datetime]
        if isinstance(_taken_after, Unset):
            taken_after = UNSET
        else:
            taken_after = isoparse(_taken_after)

        _taken_before = d.pop("takenBefore", UNSET)
        taken_before: Union[Unset, datetime.datetime]
        if isinstance(_taken_before, Unset):
            taken_before = UNSET
        else:
            taken_before = isoparse(_taken_before)

        _trashed_after = d.pop("trashedAfter", UNSET)
        trashed_after: Union[Unset, datetime.datetime]
        if isinstance(_trashed_after, Unset):
            trashed_after = UNSET
        else:
            trashed_after = isoparse(_trashed_after)

        _trashed_before = d.pop("trashedBefore", UNSET)
        trashed_before: Union[Unset, datetime.datetime]
        if isinstance(_trashed_before, Unset):
            trashed_before = UNSET
        else:
            trashed_before = isoparse(_trashed_before)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AssetTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AssetTypeEnum(_type)

        _updated_after = d.pop("updatedAfter", UNSET)
        updated_after: Union[Unset, datetime.datetime]
        if isinstance(_updated_after, Unset):
            updated_after = UNSET
        else:
            updated_after = isoparse(_updated_after)

        _updated_before = d.pop("updatedBefore", UNSET)
        updated_before: Union[Unset, datetime.datetime]
        if isinstance(_updated_before, Unset):
            updated_before = UNSET
        else:
            updated_before = isoparse(_updated_before)

        with_archived = d.pop("withArchived", UNSET)

        with_deleted = d.pop("withDeleted", UNSET)

        with_exif = d.pop("withExif", UNSET)

        smart_search_dto = cls(
            query=query,
            city=city,
            country=country,
            created_after=created_after,
            created_before=created_before,
            device_id=device_id,
            is_archived=is_archived,
            is_encoded=is_encoded,
            is_favorite=is_favorite,
            is_motion=is_motion,
            is_not_in_album=is_not_in_album,
            is_offline=is_offline,
            is_visible=is_visible,
            lens_model=lens_model,
            library_id=library_id,
            make=make,
            model=model,
            page=page,
            person_ids=person_ids,
            size=size,
            state=state,
            taken_after=taken_after,
            taken_before=taken_before,
            trashed_after=trashed_after,
            trashed_before=trashed_before,
            type=type,
            updated_after=updated_after,
            updated_before=updated_before,
            with_archived=with_archived,
            with_deleted=with_deleted,
            with_exif=with_exif,
        )

        smart_search_dto.additional_properties = d
        return smart_search_dto

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
