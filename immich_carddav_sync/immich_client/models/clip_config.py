from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clip_mode import CLIPMode
from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CLIPConfig")


@_attrs_define
class CLIPConfig:
    """
    Attributes:
        enabled (bool):
        model_name (str):
        mode (Union[Unset, CLIPMode]):
        model_type (Union[Unset, ModelType]):
    """

    enabled: bool
    model_name: str
    mode: Union[Unset, CLIPMode] = UNSET
    model_type: Union[Unset, ModelType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        model_name = self.model_name
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        model_type: Union[Unset, str] = UNSET
        if not isinstance(self.model_type, Unset):
            model_type = self.model_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "modelName": model_name,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if model_type is not UNSET:
            field_dict["modelType"] = model_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        model_name = d.pop("modelName")

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, CLIPMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CLIPMode(_mode)

        _model_type = d.pop("modelType", UNSET)
        model_type: Union[Unset, ModelType]
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = ModelType(_model_type)

        clip_config = cls(
            enabled=enabled,
            model_name=model_name,
            mode=mode,
            model_type=model_type,
        )

        clip_config.additional_properties = d
        return clip_config

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
