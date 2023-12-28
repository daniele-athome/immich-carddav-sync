import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonUpdateDto")


@_attrs_define
class PersonUpdateDto:
    """
    Attributes:
        birth_date (Union[Unset, None, datetime.date]): Person date of birth.
            Note: the mobile app cannot currently set the birth date to null.
        feature_face_asset_id (Union[Unset, str]): Asset is used to get the feature face thumbnail.
        is_hidden (Union[Unset, bool]): Person visibility
        name (Union[Unset, str]): Person name.
    """

    birth_date: Union[Unset, None, datetime.date] = UNSET
    feature_face_asset_id: Union[Unset, str] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        birth_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat() if self.birth_date else None

        feature_face_asset_id = self.feature_face_asset_id
        is_hidden = self.is_hidden
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        _birth_date = d.pop("birthDate", UNSET)
        birth_date: Union[Unset, None, datetime.date]
        if _birth_date is None:
            birth_date = None
        elif isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date).date()

        feature_face_asset_id = d.pop("featureFaceAssetId", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        name = d.pop("name", UNSET)

        person_update_dto = cls(
            birth_date=birth_date,
            feature_face_asset_id=feature_face_asset_id,
            is_hidden=is_hidden,
            name=name,
        )

        person_update_dto.additional_properties = d
        return person_update_dto

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
