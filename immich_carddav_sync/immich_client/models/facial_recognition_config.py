from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FacialRecognitionConfig")


@_attrs_define
class FacialRecognitionConfig:
    """
    Attributes:
        enabled (bool):
        max_distance (float):
        min_faces (int):
        min_score (float):
        model_name (str):
    """

    enabled: bool
    max_distance: float
    min_faces: int
    min_score: float
    model_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        max_distance = self.max_distance

        min_faces = self.min_faces

        min_score = self.min_score

        model_name = self.model_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "maxDistance": max_distance,
                "minFaces": min_faces,
                "minScore": min_score,
                "modelName": model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        max_distance = d.pop("maxDistance")

        min_faces = d.pop("minFaces")

        min_score = d.pop("minScore")

        model_name = d.pop("modelName")

        facial_recognition_config = cls(
            enabled=enabled,
            max_distance=max_distance,
            min_faces=min_faces,
            min_score=min_score,
            model_name=model_name,
        )

        facial_recognition_config.additional_properties = d
        return facial_recognition_config

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
