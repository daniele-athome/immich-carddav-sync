from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_report_item_dto import FileReportItemDto


T = TypeVar("T", bound="FileReportDto")


@_attrs_define
class FileReportDto:
    """
    Attributes:
        extras (List[str]):
        orphans (List['FileReportItemDto']):
    """

    extras: List[str]
    orphans: List["FileReportItemDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extras = self.extras

        orphans = []
        for orphans_item_data in self.orphans:
            orphans_item = orphans_item_data.to_dict()

            orphans.append(orphans_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extras": extras,
                "orphans": orphans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_report_item_dto import FileReportItemDto

        d = src_dict.copy()
        extras = cast(List[str], d.pop("extras"))

        orphans = []
        _orphans = d.pop("orphans")
        for orphans_item_data in _orphans:
            orphans_item = FileReportItemDto.from_dict(orphans_item_data)

            orphans.append(orphans_item)

        file_report_dto = cls(
            extras=extras,
            orphans=orphans,
        )

        file_report_dto.additional_properties = d
        return file_report_dto

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
