from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_asset_status import DeleteAssetStatus

T = TypeVar("T", bound="DeleteAssetResponseDto")


@_attrs_define
class DeleteAssetResponseDto:
    """
    Attributes:
        id (str):
        status (DeleteAssetStatus):
    """

    id: str
    status: DeleteAssetStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = DeleteAssetStatus(d.pop("status"))

        delete_asset_response_dto = cls(
            id=id,
            status=status,
        )

        delete_asset_response_dto.additional_properties = d
        return delete_asset_response_dto

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
