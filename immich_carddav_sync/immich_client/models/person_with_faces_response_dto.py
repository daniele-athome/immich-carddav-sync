import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto


T = TypeVar("T", bound="PersonWithFacesResponseDto")


@_attrs_define
class PersonWithFacesResponseDto:
    """
    Attributes:
        birth_date (Union[None, datetime.date]):
        faces (List['AssetFaceWithoutPersonResponseDto']):
        id (str):
        is_hidden (bool):
        name (str):
        thumbnail_path (str):
        updated_at (Union[Unset, datetime.datetime]): This property was added in v1.107.0
    """

    birth_date: Union[None, datetime.date]
    faces: List["AssetFaceWithoutPersonResponseDto"]
    id: str
    is_hidden: bool
    name: str
    thumbnail_path: str
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        birth_date: Union[None, str]
        if isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        faces = []
        for faces_item_data in self.faces:
            faces_item = faces_item_data.to_dict()
            faces.append(faces_item)

        id = self.id

        is_hidden = self.is_hidden

        name = self.name

        thumbnail_path = self.thumbnail_path

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "birthDate": birth_date,
                "faces": faces,
                "id": id,
                "isHidden": is_hidden,
                "name": name,
                "thumbnailPath": thumbnail_path,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto

        d = src_dict.copy()

        def _parse_birth_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data).date()

                return birth_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        birth_date = _parse_birth_date(d.pop("birthDate"))

        faces = []
        _faces = d.pop("faces")
        for faces_item_data in _faces:
            faces_item = AssetFaceWithoutPersonResponseDto.from_dict(faces_item_data)

            faces.append(faces_item)

        id = d.pop("id")

        is_hidden = d.pop("isHidden")

        name = d.pop("name")

        thumbnail_path = d.pop("thumbnailPath")

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        person_with_faces_response_dto = cls(
            birth_date=birth_date,
            faces=faces,
            id=id,
            is_hidden=is_hidden,
            name=name,
            thumbnail_path=thumbnail_path,
            updated_at=updated_at,
        )

        person_with_faces_response_dto.additional_properties = d
        return person_with_faces_response_dto

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
