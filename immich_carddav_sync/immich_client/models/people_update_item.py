import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeopleUpdateItem")


@_attrs_define
class PeopleUpdateItem:
    """
    Attributes:
        id (str): Person id.
        birth_date (Union[None, Unset, datetime.date]): Person date of birth.
            Note: the mobile app cannot currently set the birth date to null.
        feature_face_asset_id (Union[Unset, str]): Asset is used to get the feature face thumbnail.
        is_hidden (Union[Unset, bool]): Person visibility
        name (Union[Unset, str]): Person name.
    """

    id: str
    birth_date: Union[None, Unset, datetime.date] = UNSET
    feature_face_asset_id: Union[Unset, str] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        birth_date: Union[None, Unset, str]
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        feature_face_asset_id = self.feature_face_asset_id

        is_hidden = self.is_hidden

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if feature_face_asset_id is not UNSET:
            field_dict["featureFaceAssetId"] = feature_face_asset_id
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_birth_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data).date()

                return birth_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        birth_date = _parse_birth_date(d.pop("birthDate", UNSET))

        feature_face_asset_id = d.pop("featureFaceAssetId", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        name = d.pop("name", UNSET)

        people_update_item = cls(
            id=id,
            birth_date=birth_date,
            feature_face_asset_id=feature_face_asset_id,
            is_hidden=is_hidden,
            name=name,
        )

        people_update_item.additional_properties = d
        return people_update_item

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
