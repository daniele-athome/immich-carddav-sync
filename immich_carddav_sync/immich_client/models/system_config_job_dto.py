from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_settings_dto import JobSettingsDto


T = TypeVar("T", bound="SystemConfigJobDto")


@_attrs_define
class SystemConfigJobDto:
    """
    Attributes:
        background_task (JobSettingsDto):
        face_detection (JobSettingsDto):
        library (JobSettingsDto):
        metadata_extraction (JobSettingsDto):
        migration (JobSettingsDto):
        notifications (JobSettingsDto):
        search (JobSettingsDto):
        sidecar (JobSettingsDto):
        smart_search (JobSettingsDto):
        thumbnail_generation (JobSettingsDto):
        video_conversion (JobSettingsDto):
    """

    background_task: "JobSettingsDto"
    face_detection: "JobSettingsDto"
    library: "JobSettingsDto"
    metadata_extraction: "JobSettingsDto"
    migration: "JobSettingsDto"
    notifications: "JobSettingsDto"
    search: "JobSettingsDto"
    sidecar: "JobSettingsDto"
    smart_search: "JobSettingsDto"
    thumbnail_generation: "JobSettingsDto"
    video_conversion: "JobSettingsDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        background_task = self.background_task.to_dict()

        face_detection = self.face_detection.to_dict()

        library = self.library.to_dict()

        metadata_extraction = self.metadata_extraction.to_dict()

        migration = self.migration.to_dict()

        notifications = self.notifications.to_dict()

        search = self.search.to_dict()

        sidecar = self.sidecar.to_dict()

        smart_search = self.smart_search.to_dict()

        thumbnail_generation = self.thumbnail_generation.to_dict()

        video_conversion = self.video_conversion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backgroundTask": background_task,
                "faceDetection": face_detection,
                "library": library,
                "metadataExtraction": metadata_extraction,
                "migration": migration,
                "notifications": notifications,
                "search": search,
                "sidecar": sidecar,
                "smartSearch": smart_search,
                "thumbnailGeneration": thumbnail_generation,
                "videoConversion": video_conversion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_settings_dto import JobSettingsDto

        d = src_dict.copy()
        background_task = JobSettingsDto.from_dict(d.pop("backgroundTask"))

        face_detection = JobSettingsDto.from_dict(d.pop("faceDetection"))

        library = JobSettingsDto.from_dict(d.pop("library"))

        metadata_extraction = JobSettingsDto.from_dict(d.pop("metadataExtraction"))

        migration = JobSettingsDto.from_dict(d.pop("migration"))

        notifications = JobSettingsDto.from_dict(d.pop("notifications"))

        search = JobSettingsDto.from_dict(d.pop("search"))

        sidecar = JobSettingsDto.from_dict(d.pop("sidecar"))

        smart_search = JobSettingsDto.from_dict(d.pop("smartSearch"))

        thumbnail_generation = JobSettingsDto.from_dict(d.pop("thumbnailGeneration"))

        video_conversion = JobSettingsDto.from_dict(d.pop("videoConversion"))

        system_config_job_dto = cls(
            background_task=background_task,
            face_detection=face_detection,
            library=library,
            metadata_extraction=metadata_extraction,
            migration=migration,
            notifications=notifications,
            search=search,
            sidecar=sidecar,
            smart_search=smart_search,
            thumbnail_generation=thumbnail_generation,
            video_conversion=video_conversion,
        )

        system_config_job_dto.additional_properties = d
        return system_config_job_dto

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
