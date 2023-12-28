from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecognitionConfig")


@_attrs_define
class RecognitionConfig:
    """
    Attributes:
        enabled (bool):
        max_distance (int):
        min_faces (int):
        min_score (int):
        model_name (str):
        model_type (Union[Unset, ModelType]):
    """

    enabled: bool
    max_distance: int
    min_faces: int
    min_score: int
    model_name: str
    model_type: Union[Unset, ModelType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        max_distance = self.max_distance
        min_faces = self.min_faces
        min_score = self.min_score
        model_name = self.model_name
        model_type: Union[Unset, str] = UNSET
        if not isinstance(self.model_type, Unset):
            model_type = self.model_type.value

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
        if model_type is not UNSET:
            field_dict["modelType"] = model_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        max_distance = d.pop("maxDistance")

        min_faces = d.pop("minFaces")

        min_score = d.pop("minScore")

        model_name = d.pop("modelName")

        _model_type = d.pop("modelType", UNSET)
        model_type: Union[Unset, ModelType]
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = ModelType(_model_type)

        recognition_config = cls(
            enabled=enabled,
            max_distance=max_distance,
            min_faces=min_faces,
            min_score=min_score,
            model_name=model_name,
            model_type=model_type,
        )

        recognition_config.additional_properties = d
        return recognition_config

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
