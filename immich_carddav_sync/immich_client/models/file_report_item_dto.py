from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.path_entity_type import PathEntityType
from ..models.path_type import PathType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileReportItemDto")


@_attrs_define
class FileReportItemDto:
    """
    Attributes:
        entity_id (UUID):
        entity_type (PathEntityType):
        path_type (PathType):
        path_value (str):
        checksum (Union[Unset, str]):
    """

    entity_id: UUID
    entity_type: PathEntityType
    path_type: PathType
    path_value: str
    checksum: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = str(self.entity_id)

        entity_type = self.entity_type.value

        path_type = self.path_type.value

        path_value = self.path_value

        checksum = self.checksum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityId": entity_id,
                "entityType": entity_type,
                "pathType": path_type,
                "pathValue": path_value,
            }
        )
        if checksum is not UNSET:
            field_dict["checksum"] = checksum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity_id = UUID(d.pop("entityId"))

        entity_type = PathEntityType(d.pop("entityType"))

        path_type = PathType(d.pop("pathType"))

        path_value = d.pop("pathValue")

        checksum = d.pop("checksum", UNSET)

        file_report_item_dto = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            path_type=path_type,
            path_value=path_value,
            checksum=checksum,
        )

        file_report_item_dto.additional_properties = d
        return file_report_item_dto

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
