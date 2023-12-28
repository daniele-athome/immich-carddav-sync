from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetFaceWithoutPersonResponseDto")


@_attrs_define
class AssetFaceWithoutPersonResponseDto:
    """
    Attributes:
        bounding_box_x1 (int):
        bounding_box_x2 (int):
        bounding_box_y1 (int):
        bounding_box_y2 (int):
        id (str):
        image_height (int):
        image_width (int):
    """

    bounding_box_x1: int
    bounding_box_x2: int
    bounding_box_y1: int
    bounding_box_y2: int
    id: str
    image_height: int
    image_width: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bounding_box_x1 = self.bounding_box_x1
        bounding_box_x2 = self.bounding_box_x2
        bounding_box_y1 = self.bounding_box_y1
        bounding_box_y2 = self.bounding_box_y2
        id = self.id
        image_height = self.image_height
        image_width = self.image_width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boundingBoxX1": bounding_box_x1,
                "boundingBoxX2": bounding_box_x2,
                "boundingBoxY1": bounding_box_y1,
                "boundingBoxY2": bounding_box_y2,
                "id": id,
                "imageHeight": image_height,
                "imageWidth": image_width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bounding_box_x1 = d.pop("boundingBoxX1")

        bounding_box_x2 = d.pop("boundingBoxX2")

        bounding_box_y1 = d.pop("boundingBoxY1")

        bounding_box_y2 = d.pop("boundingBoxY2")

        id = d.pop("id")

        image_height = d.pop("imageHeight")

        image_width = d.pop("imageWidth")

        asset_face_without_person_response_dto = cls(
            bounding_box_x1=bounding_box_x1,
            bounding_box_x2=bounding_box_x2,
            bounding_box_y1=bounding_box_y1,
            bounding_box_y2=bounding_box_y2,
            id=id,
            image_height=image_height,
            image_width=image_width,
        )

        asset_face_without_person_response_dto.additional_properties = d
        return asset_face_without_person_response_dto

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
