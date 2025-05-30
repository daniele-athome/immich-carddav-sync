from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
    from ..models.system_config_image_dto import SystemConfigImageDto
    from ..models.system_config_job_dto import SystemConfigJobDto
    from ..models.system_config_library_dto import SystemConfigLibraryDto
    from ..models.system_config_logging_dto import SystemConfigLoggingDto
    from ..models.system_config_machine_learning_dto import SystemConfigMachineLearningDto
    from ..models.system_config_map_dto import SystemConfigMapDto
    from ..models.system_config_metadata_dto import SystemConfigMetadataDto
    from ..models.system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
    from ..models.system_config_notifications_dto import SystemConfigNotificationsDto
    from ..models.system_config_o_auth_dto import SystemConfigOAuthDto
    from ..models.system_config_password_login_dto import SystemConfigPasswordLoginDto
    from ..models.system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
    from ..models.system_config_server_dto import SystemConfigServerDto
    from ..models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
    from ..models.system_config_theme_dto import SystemConfigThemeDto
    from ..models.system_config_trash_dto import SystemConfigTrashDto
    from ..models.system_config_user_dto import SystemConfigUserDto


T = TypeVar("T", bound="SystemConfigDto")


@_attrs_define
class SystemConfigDto:
    """
    Attributes:
        ffmpeg (SystemConfigFFmpegDto):
        image (SystemConfigImageDto):
        job (SystemConfigJobDto):
        library (SystemConfigLibraryDto):
        logging (SystemConfigLoggingDto):
        machine_learning (SystemConfigMachineLearningDto):
        map_ (SystemConfigMapDto):
        metadata (SystemConfigMetadataDto):
        new_version_check (SystemConfigNewVersionCheckDto):
        notifications (SystemConfigNotificationsDto):
        oauth (SystemConfigOAuthDto):
        password_login (SystemConfigPasswordLoginDto):
        reverse_geocoding (SystemConfigReverseGeocodingDto):
        server (SystemConfigServerDto):
        storage_template (SystemConfigStorageTemplateDto):
        theme (SystemConfigThemeDto):
        trash (SystemConfigTrashDto):
        user (SystemConfigUserDto):
    """

    ffmpeg: "SystemConfigFFmpegDto"
    image: "SystemConfigImageDto"
    job: "SystemConfigJobDto"
    library: "SystemConfigLibraryDto"
    logging: "SystemConfigLoggingDto"
    machine_learning: "SystemConfigMachineLearningDto"
    map_: "SystemConfigMapDto"
    metadata: "SystemConfigMetadataDto"
    new_version_check: "SystemConfigNewVersionCheckDto"
    notifications: "SystemConfigNotificationsDto"
    oauth: "SystemConfigOAuthDto"
    password_login: "SystemConfigPasswordLoginDto"
    reverse_geocoding: "SystemConfigReverseGeocodingDto"
    server: "SystemConfigServerDto"
    storage_template: "SystemConfigStorageTemplateDto"
    theme: "SystemConfigThemeDto"
    trash: "SystemConfigTrashDto"
    user: "SystemConfigUserDto"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ffmpeg = self.ffmpeg.to_dict()

        image = self.image.to_dict()

        job = self.job.to_dict()

        library = self.library.to_dict()

        logging = self.logging.to_dict()

        machine_learning = self.machine_learning.to_dict()

        map_ = self.map_.to_dict()

        metadata = self.metadata.to_dict()

        new_version_check = self.new_version_check.to_dict()

        notifications = self.notifications.to_dict()

        oauth = self.oauth.to_dict()

        password_login = self.password_login.to_dict()

        reverse_geocoding = self.reverse_geocoding.to_dict()

        server = self.server.to_dict()

        storage_template = self.storage_template.to_dict()

        theme = self.theme.to_dict()

        trash = self.trash.to_dict()

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ffmpeg": ffmpeg,
                "image": image,
                "job": job,
                "library": library,
                "logging": logging,
                "machineLearning": machine_learning,
                "map": map_,
                "metadata": metadata,
                "newVersionCheck": new_version_check,
                "notifications": notifications,
                "oauth": oauth,
                "passwordLogin": password_login,
                "reverseGeocoding": reverse_geocoding,
                "server": server,
                "storageTemplate": storage_template,
                "theme": theme,
                "trash": trash,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
        from ..models.system_config_image_dto import SystemConfigImageDto
        from ..models.system_config_job_dto import SystemConfigJobDto
        from ..models.system_config_library_dto import SystemConfigLibraryDto
        from ..models.system_config_logging_dto import SystemConfigLoggingDto
        from ..models.system_config_machine_learning_dto import SystemConfigMachineLearningDto
        from ..models.system_config_map_dto import SystemConfigMapDto
        from ..models.system_config_metadata_dto import SystemConfigMetadataDto
        from ..models.system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
        from ..models.system_config_notifications_dto import SystemConfigNotificationsDto
        from ..models.system_config_o_auth_dto import SystemConfigOAuthDto
        from ..models.system_config_password_login_dto import SystemConfigPasswordLoginDto
        from ..models.system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
        from ..models.system_config_server_dto import SystemConfigServerDto
        from ..models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
        from ..models.system_config_theme_dto import SystemConfigThemeDto
        from ..models.system_config_trash_dto import SystemConfigTrashDto
        from ..models.system_config_user_dto import SystemConfigUserDto

        d = src_dict.copy()
        ffmpeg = SystemConfigFFmpegDto.from_dict(d.pop("ffmpeg"))

        image = SystemConfigImageDto.from_dict(d.pop("image"))

        job = SystemConfigJobDto.from_dict(d.pop("job"))

        library = SystemConfigLibraryDto.from_dict(d.pop("library"))

        logging = SystemConfigLoggingDto.from_dict(d.pop("logging"))

        machine_learning = SystemConfigMachineLearningDto.from_dict(d.pop("machineLearning"))

        map_ = SystemConfigMapDto.from_dict(d.pop("map"))

        metadata = SystemConfigMetadataDto.from_dict(d.pop("metadata"))

        new_version_check = SystemConfigNewVersionCheckDto.from_dict(d.pop("newVersionCheck"))

        notifications = SystemConfigNotificationsDto.from_dict(d.pop("notifications"))

        oauth = SystemConfigOAuthDto.from_dict(d.pop("oauth"))

        password_login = SystemConfigPasswordLoginDto.from_dict(d.pop("passwordLogin"))

        reverse_geocoding = SystemConfigReverseGeocodingDto.from_dict(d.pop("reverseGeocoding"))

        server = SystemConfigServerDto.from_dict(d.pop("server"))

        storage_template = SystemConfigStorageTemplateDto.from_dict(d.pop("storageTemplate"))

        theme = SystemConfigThemeDto.from_dict(d.pop("theme"))

        trash = SystemConfigTrashDto.from_dict(d.pop("trash"))

        user = SystemConfigUserDto.from_dict(d.pop("user"))

        system_config_dto = cls(
            ffmpeg=ffmpeg,
            image=image,
            job=job,
            library=library,
            logging=logging,
            machine_learning=machine_learning,
            map_=map_,
            metadata=metadata,
            new_version_check=new_version_check,
            notifications=notifications,
            oauth=oauth,
            password_login=password_login,
            reverse_geocoding=reverse_geocoding,
            server=server,
            storage_template=storage_template,
            theme=theme,
            trash=trash,
            user=user,
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
