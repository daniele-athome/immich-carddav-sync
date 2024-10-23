from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.clip_config import CLIPConfig
    from ..models.duplicate_detection_config import DuplicateDetectionConfig
    from ..models.facial_recognition_config import FacialRecognitionConfig


T = TypeVar("T", bound="SystemConfigMachineLearningDto")


@_attrs_define
class SystemConfigMachineLearningDto:
    """
    Attributes:
        clip (CLIPConfig):
        duplicate_detection (DuplicateDetectionConfig):
        enabled (bool):
        facial_recognition (FacialRecognitionConfig):
        url (str):
    """

    clip: "CLIPConfig"
    duplicate_detection: "DuplicateDetectionConfig"
    enabled: bool
    facial_recognition: "FacialRecognitionConfig"
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clip = self.clip.to_dict()

        duplicate_detection = self.duplicate_detection.to_dict()

        enabled = self.enabled

        facial_recognition = self.facial_recognition.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clip": clip,
                "duplicateDetection": duplicate_detection,
                "enabled": enabled,
                "facialRecognition": facial_recognition,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.clip_config import CLIPConfig
        from ..models.duplicate_detection_config import DuplicateDetectionConfig
        from ..models.facial_recognition_config import FacialRecognitionConfig

        d = src_dict.copy()
        clip = CLIPConfig.from_dict(d.pop("clip"))

        duplicate_detection = DuplicateDetectionConfig.from_dict(d.pop("duplicateDetection"))

        enabled = d.pop("enabled")

        facial_recognition = FacialRecognitionConfig.from_dict(d.pop("facialRecognition"))

        url = d.pop("url")

        system_config_machine_learning_dto = cls(
            clip=clip,
            duplicate_detection=duplicate_detection,
            enabled=enabled,
            facial_recognition=facial_recognition,
            url=url,
        )

        system_config_machine_learning_dto.additional_properties = d
        return system_config_machine_learning_dto

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
