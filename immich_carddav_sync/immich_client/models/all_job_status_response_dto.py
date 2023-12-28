from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_status_dto import JobStatusDto


T = TypeVar("T", bound="AllJobStatusResponseDto")


@_attrs_define
class AllJobStatusResponseDto:
    """
    Attributes:
        background_task (JobStatusDto):
        library (JobStatusDto):
        metadata_extraction (JobStatusDto):
        migration (JobStatusDto):
        object_tagging (JobStatusDto):
        recognize_faces (JobStatusDto):
        search (JobStatusDto):
        sidecar (JobStatusDto):
        smart_search (JobStatusDto):
        storage_template_migration (JobStatusDto):
        thumbnail_generation (JobStatusDto):
        video_conversion (JobStatusDto):
    """

    background_task: "JobStatusDto"
    library: "JobStatusDto"
    metadata_extraction: "JobStatusDto"
    migration: "JobStatusDto"
    object_tagging: "JobStatusDto"
    recognize_faces: "JobStatusDto"
    search: "JobStatusDto"
    sidecar: "JobStatusDto"
    smart_search: "JobStatusDto"
    storage_template_migration: "JobStatusDto"
    thumbnail_generation: "JobStatusDto"
    video_conversion: "JobStatusDto"
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
        from ..models.job_status_dto import JobStatusDto

        d = src_dict.copy()
        background_task = JobStatusDto.from_dict(d.pop("backgroundTask"))

        library = JobStatusDto.from_dict(d.pop("library"))

        metadata_extraction = JobStatusDto.from_dict(d.pop("metadataExtraction"))

        migration = JobStatusDto.from_dict(d.pop("migration"))

        object_tagging = JobStatusDto.from_dict(d.pop("objectTagging"))

        recognize_faces = JobStatusDto.from_dict(d.pop("recognizeFaces"))

        search = JobStatusDto.from_dict(d.pop("search"))

        sidecar = JobStatusDto.from_dict(d.pop("sidecar"))

        smart_search = JobStatusDto.from_dict(d.pop("smartSearch"))

        storage_template_migration = JobStatusDto.from_dict(d.pop("storageTemplateMigration"))

        thumbnail_generation = JobStatusDto.from_dict(d.pop("thumbnailGeneration"))

        video_conversion = JobStatusDto.from_dict(d.pop("videoConversion"))

        all_job_status_response_dto = cls(
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

        all_job_status_response_dto.additional_properties = d
        return all_job_status_response_dto

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
