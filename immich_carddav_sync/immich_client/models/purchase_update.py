from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseUpdate")


@_attrs_define
class PurchaseUpdate:
    """
    Attributes:
        hide_buy_button_until (Union[Unset, str]):
        show_support_badge (Union[Unset, bool]):
    """

    hide_buy_button_until: Union[Unset, str] = UNSET
    show_support_badge: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hide_buy_button_until = self.hide_buy_button_until

        show_support_badge = self.show_support_badge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hide_buy_button_until is not UNSET:
            field_dict["hideBuyButtonUntil"] = hide_buy_button_until
        if show_support_badge is not UNSET:
            field_dict["showSupportBadge"] = show_support_badge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hide_buy_button_until = d.pop("hideBuyButtonUntil", UNSET)

        show_support_badge = d.pop("showSupportBadge", UNSET)

        purchase_update = cls(
            hide_buy_button_until=hide_buy_button_until,
            show_support_badge=show_support_badge,
        )

        purchase_update.additional_properties = d
        return purchase_update

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
