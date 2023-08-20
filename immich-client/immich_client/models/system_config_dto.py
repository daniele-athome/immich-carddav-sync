from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
    from ..models.system_config_job_dto import SystemConfigJobDto
    from ..models.system_config_o_auth_dto import SystemConfigOAuthDto
    from ..models.system_config_password_login_dto import SystemConfigPasswordLoginDto
    from ..models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
    from ..models.system_config_thumbnail_dto import SystemConfigThumbnailDto


T = TypeVar("T", bound="SystemConfigDto")


@_attrs_define
class SystemConfigDto:
    """
    Attributes:
        ffmpeg (SystemConfigFFmpegDto):
        job (SystemConfigJobDto):
        oauth (SystemConfigOAuthDto):
        password_login (SystemConfigPasswordLoginDto):
        storage_template (SystemConfigStorageTemplateDto):
        thumbnail (SystemConfigThumbnailDto):
    """

    ffmpeg: "SystemConfigFFmpegDto"
    job: "SystemConfigJobDto"
    oauth: "SystemConfigOAuthDto"
    password_login: "SystemConfigPasswordLoginDto"
    storage_template: "SystemConfigStorageTemplateDto"
    thumbnail: "SystemConfigThumbnailDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ffmpeg = self.ffmpeg.to_dict()

        job = self.job.to_dict()

        oauth = self.oauth.to_dict()

        password_login = self.password_login.to_dict()

        storage_template = self.storage_template.to_dict()

        thumbnail = self.thumbnail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ffmpeg": ffmpeg,
                "job": job,
                "oauth": oauth,
                "passwordLogin": password_login,
                "storageTemplate": storage_template,
                "thumbnail": thumbnail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
        from ..models.system_config_job_dto import SystemConfigJobDto
        from ..models.system_config_o_auth_dto import SystemConfigOAuthDto
        from ..models.system_config_password_login_dto import SystemConfigPasswordLoginDto
        from ..models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
        from ..models.system_config_thumbnail_dto import SystemConfigThumbnailDto

        d = src_dict.copy()
        ffmpeg = SystemConfigFFmpegDto.from_dict(d.pop("ffmpeg"))

        job = SystemConfigJobDto.from_dict(d.pop("job"))

        oauth = SystemConfigOAuthDto.from_dict(d.pop("oauth"))

        password_login = SystemConfigPasswordLoginDto.from_dict(d.pop("passwordLogin"))

        storage_template = SystemConfigStorageTemplateDto.from_dict(d.pop("storageTemplate"))

        thumbnail = SystemConfigThumbnailDto.from_dict(d.pop("thumbnail"))

        system_config_dto = cls(
            ffmpeg=ffmpeg,
            job=job,
            oauth=oauth,
            password_login=password_login,
            storage_template=storage_template,
            thumbnail=thumbnail,
        )

        system_config_dto.additional_properties = d
        return system_config_dto

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
