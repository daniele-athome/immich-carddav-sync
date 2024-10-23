import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LibraryResponseDto")


@_attrs_define
class LibraryResponseDto:
    """
    Attributes:
        asset_count (int):
        created_at (datetime.datetime):
        exclusion_patterns (List[str]):
        id (str):
        import_paths (List[str]):
        name (str):
        owner_id (str):
        refreshed_at (Union[None, datetime.datetime]):
        updated_at (datetime.datetime):
    """

    asset_count: int
    created_at: datetime.datetime
    exclusion_patterns: List[str]
    id: str
    import_paths: List[str]
    name: str
    owner_id: str
    refreshed_at: Union[None, datetime.datetime]
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_count = self.asset_count

        created_at = self.created_at.isoformat()

        exclusion_patterns = self.exclusion_patterns

        id = self.id

        import_paths = self.import_paths

        name = self.name

        owner_id = self.owner_id

        refreshed_at: Union[None, str]
        if isinstance(self.refreshed_at, datetime.datetime):
            refreshed_at = self.refreshed_at.isoformat()
        else:
            refreshed_at = self.refreshed_at

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetCount": asset_count,
                "createdAt": created_at,
                "exclusionPatterns": exclusion_patterns,
                "id": id,
                "importPaths": import_paths,
                "name": name,
                "ownerId": owner_id,
                "refreshedAt": refreshed_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_count = d.pop("assetCount")

        created_at = isoparse(d.pop("createdAt"))

        exclusion_patterns = cast(List[str], d.pop("exclusionPatterns"))

        id = d.pop("id")

        import_paths = cast(List[str], d.pop("importPaths"))

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        def _parse_refreshed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refreshed_at_type_0 = isoparse(data)

                return refreshed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        refreshed_at = _parse_refreshed_at(d.pop("refreshedAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        library_response_dto = cls(
            asset_count=asset_count,
            created_at=created_at,
            exclusion_patterns=exclusion_patterns,
            id=id,
            import_paths=import_paths,
            name=name,
            owner_id=owner_id,
            refreshed_at=refreshed_at,
            updated_at=updated_at,
        )

        library_response_dto.additional_properties = d
        return library_response_dto

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
