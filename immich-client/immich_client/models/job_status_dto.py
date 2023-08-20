from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_counts_dto import JobCountsDto
    from ..models.queue_status_dto import QueueStatusDto


T = TypeVar("T", bound="JobStatusDto")


@_attrs_define
class JobStatusDto:
    """
    Attributes:
        job_counts (JobCountsDto):
        queue_status (QueueStatusDto):
    """

    job_counts: "JobCountsDto"
    queue_status: "QueueStatusDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_counts = self.job_counts.to_dict()

        queue_status = self.queue_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobCounts": job_counts,
                "queueStatus": queue_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_counts_dto import JobCountsDto
        from ..models.queue_status_dto import QueueStatusDto

        d = src_dict.copy()
        job_counts = JobCountsDto.from_dict(d.pop("jobCounts"))

        queue_status = QueueStatusDto.from_dict(d.pop("queueStatus"))

        job_status_dto = cls(
            job_counts=job_counts,
            queue_status=queue_status,
        )

        job_status_dto.additional_properties = d
        return job_status_dto

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
