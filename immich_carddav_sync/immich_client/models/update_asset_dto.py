from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssetDto")


@_attrs_define
class UpdateAssetDto:
    """
    Attributes:
        description (Union[Unset, str]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        tag_ids (Union[Unset, List[str]]):  Example: ['bf973405-3f2a-48d2-a687-2ed4167164be',
            'dd41870b-5d00-46d2-924e-1d8489a0aa0f', 'fad77c3f-deef-4e7e-9608-14c1aa4e559a'].
    """

    description: Union[Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    tag_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        is_archived = self.is_archived
        is_favorite = self.is_favorite
        tag_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        tag_ids = cast(List[str], d.pop("tagIds", UNSET))

        update_asset_dto = cls(
            description=description,
            is_archived=is_archived,
            is_favorite=is_favorite,
            tag_ids=tag_ids,
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
