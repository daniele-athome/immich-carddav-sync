import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto


T = TypeVar("T", bound="PersonWithFacesResponseDto")


@_attrs_define
class PersonWithFacesResponseDto:
    """
    Attributes:
        faces (List['AssetFaceWithoutPersonResponseDto']):
        id (str):
        is_hidden (bool):
        name (str):
        thumbnail_path (str):
        birth_date (Optional[datetime.date]):
    """

    faces: List["AssetFaceWithoutPersonResponseDto"]
    id: str
    is_hidden: bool
    name: str
    thumbnail_path: str
    birth_date: Optional[datetime.date]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        faces = []
        for faces_item_data in self.faces:
            faces_item = faces_item_data.to_dict()

            faces.append(faces_item)

        id = self.id
        is_hidden = self.is_hidden
        name = self.name
        thumbnail_path = self.thumbnail_path
        birth_date = self.birth_date.isoformat() if self.birth_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "faces": faces,
                "id": id,
                "isHidden": is_hidden,
                "name": name,
                "thumbnailPath": thumbnail_path,
                "birthDate": birth_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto

        d = src_dict.copy()
        faces = []
        _faces = d.pop("faces")
        for faces_item_data in _faces:
            faces_item = AssetFaceWithoutPersonResponseDto.from_dict(faces_item_data)

            faces.append(faces_item)

        id = d.pop("id")

        is_hidden = d.pop("isHidden")

        name = d.pop("name")

        thumbnail_path = d.pop("thumbnailPath")

        _birth_date = d.pop("birthDate")
        birth_date: Optional[datetime.date]
        if _birth_date is None:
            birth_date = None
        else:
            birth_date = isoparse(_birth_date).date()

        person_with_faces_response_dto = cls(
            faces=faces,
            id=id,
            is_hidden=is_hidden,
            name=name,
            thumbnail_path=thumbnail_path,
            birth_date=birth_date,
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
