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
        library (JobSettingsDto):
        metadata_extraction (JobSettingsDto):
        migration (JobSettingsDto):
        object_tagging (JobSettingsDto):
        recognize_faces (JobSettingsDto):
        search (JobSettingsDto):
        sidecar (JobSettingsDto):
        smart_search (JobSettingsDto):
        storage_template_migration (JobSettingsDto):
        thumbnail_generation (JobSettingsDto):
        video_conversion (JobSettingsDto):
    """

    background_task: "JobSettingsDto"
    library: "JobSettingsDto"
    metadata_extraction: "JobSettingsDto"
    migration: "JobSettingsDto"
    object_tagging: "JobSettingsDto"
    recognize_faces: "JobSettingsDto"
    search: "JobSettingsDto"
    sidecar: "JobSettingsDto"
    smart_search: "JobSettingsDto"
    storage_template_migration: "JobSettingsDto"
    thumbnail_generation: "JobSettingsDto"
    video_conversion: "JobSettingsDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        background_task = self.background_task.to_dict()

        library = self.library.to_dict()

        metadata_extraction = self.metadata_extraction.to_dict()

        migration = self.migration.to_dict()

        object_tagging = self.object_tagging.to_dict()

        recognize_faces = self.recognize_faces.to_dict()

        search = self.search.to_dict()

        sidecar = self.sidecar.to_dict()

        smart_search = self.smart_search.to_dict()

        storage_template_migration = self.storage_template_migration.to_dict()

        thumbnail_generation = self.thumbnail_generation.to_dict()

        video_conversion = self.video_conversion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backgroundTask": background_task,
                "library": library,
                "metadataExtraction": metadata_extraction,
                "migration": migration,
                "objectTagging": object_tagging,
                "recognizeFaces": recognize_faces,
                "search": search,
                "sidecar": sidecar,
                "smartSearch": smart_search,
                "storageTemplateMigration": storage_template_migration,
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

        library = JobSettingsDto.from_dict(d.pop("library"))

        metadata_extraction = JobSettingsDto.from_dict(d.pop("metadataExtraction"))

        migration = JobSettingsDto.from_dict(d.pop("migration"))

        object_tagging = JobSettingsDto.from_dict(d.pop("objectTagging"))

        recognize_faces = JobSettingsDto.from_dict(d.pop("recognizeFaces"))

        search = JobSettingsDto.from_dict(d.pop("search"))

        sidecar = JobSettingsDto.from_dict(d.pop("sidecar"))

        smart_search = JobSettingsDto.from_dict(d.pop("smartSearch"))

        storage_template_migration = JobSettingsDto.from_dict(d.pop("storageTemplateMigration"))

        thumbnail_generation = JobSettingsDto.from_dict(d.pop("thumbnailGeneration"))

        video_conversion = JobSettingsDto.from_dict(d.pop("videoConversion"))

        system_config_job_dto = cls(
            background_task=background_task,
            library=library,
            metadata_extraction=metadata_extraction,
            migration=migration,
            object_tagging=object_tagging,
            recognize_faces=recognize_faces,
            search=search,
            sidecar=sidecar,
            smart_search=smart_search,
            storage_template_migration=storage_template_migration,
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
