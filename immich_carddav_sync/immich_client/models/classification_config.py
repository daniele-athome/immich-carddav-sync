from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassificationConfig")


@_attrs_define
class ClassificationConfig:
    """
    Attributes:
        enabled (bool):
        min_score (int):
        model_name (str):
        model_type (Union[Unset, ModelType]):
    """

    enabled: bool
    min_score: int
    model_name: str
    model_type: Union[Unset, ModelType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
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

        min_score = d.pop("minScore")

        model_name = d.pop("modelName")

        _model_type = d.pop("modelType", UNSET)
        model_type: Union[Unset, ModelType]
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = ModelType(_model_type)

        classification_config = cls(
            enabled=enabled,
            min_score=min_score,
            model_name=model_name,
            model_type=model_type,
        )

        classification_config.additional_properties = d
        return classification_config

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
