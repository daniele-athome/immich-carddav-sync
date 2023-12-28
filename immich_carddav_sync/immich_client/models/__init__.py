""" Contains all the data models used in inputs/outputs """

from .activity_create_dto import ActivityCreateDto
from .activity_response_dto import ActivityResponseDto
from .activity_response_dto_type import ActivityResponseDtoType
from .activity_statistics_response_dto import ActivityStatisticsResponseDto
from .add_users_dto import AddUsersDto
from .album_count_response_dto import AlbumCountResponseDto
from .album_response_dto import AlbumResponseDto
from .all_job_status_response_dto import AllJobStatusResponseDto
from .api_key_create_dto import APIKeyCreateDto
from .api_key_create_response_dto import APIKeyCreateResponseDto
from .api_key_response_dto import APIKeyResponseDto
from .api_key_update_dto import APIKeyUpdateDto
from .asset_bulk_delete_dto import AssetBulkDeleteDto
from .asset_bulk_update_dto import AssetBulkUpdateDto
from .asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from .asset_bulk_upload_check_item import AssetBulkUploadCheckItem
from .asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto
from .asset_bulk_upload_check_result import AssetBulkUploadCheckResult
from .asset_bulk_upload_check_result_action import AssetBulkUploadCheckResultAction
from .asset_bulk_upload_check_result_reason import AssetBulkUploadCheckResultReason
from .asset_face_response_dto import AssetFaceResponseDto
from .asset_face_update_dto import AssetFaceUpdateDto
from .asset_face_update_item import AssetFaceUpdateItem
from .asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto
from .asset_file_upload_response_dto import AssetFileUploadResponseDto
from .asset_ids_dto import AssetIdsDto
from .asset_ids_response_dto import AssetIdsResponseDto
from .asset_ids_response_dto_error import AssetIdsResponseDtoError
from .asset_job_name import AssetJobName
from .asset_jobs_dto import AssetJobsDto
from .asset_order import AssetOrder
from .asset_response_dto import AssetResponseDto
from .asset_stats_response_dto import AssetStatsResponseDto
from .asset_type_enum import AssetTypeEnum
from .audio_codec import AudioCodec
from .audit_deletes_response_dto import AuditDeletesResponseDto
from .auth_device_response_dto import AuthDeviceResponseDto
from .bulk_id_response_dto import BulkIdResponseDto
from .bulk_id_response_dto_error import BulkIdResponseDtoError
from .bulk_ids_dto import BulkIdsDto
from .change_password_dto import ChangePasswordDto
from .check_existing_assets_dto import CheckExistingAssetsDto
from .check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from .classification_config import ClassificationConfig
from .clip_config import CLIPConfig
from .clip_mode import CLIPMode
from .colorspace import Colorspace
from .cq_mode import CQMode
from .create_album_dto import CreateAlbumDto
from .create_asset_dto import CreateAssetDto
from .create_library_dto import CreateLibraryDto
from .create_profile_image_dto import CreateProfileImageDto
from .create_profile_image_response_dto import CreateProfileImageResponseDto
from .create_tag_dto import CreateTagDto
from .create_user_dto import CreateUserDto
from .curated_locations_response_dto import CuratedLocationsResponseDto
from .curated_objects_response_dto import CuratedObjectsResponseDto
from .download_archive_info import DownloadArchiveInfo
from .download_info_dto import DownloadInfoDto
from .download_response_dto import DownloadResponseDto
from .entity_type import EntityType
from .exif_response_dto import ExifResponseDto
from .face_dto import FaceDto
from .file_checksum_dto import FileChecksumDto
from .file_checksum_response_dto import FileChecksumResponseDto
from .file_report_dto import FileReportDto
from .file_report_fix_dto import FileReportFixDto
from .file_report_item_dto import FileReportItemDto
from .get_map_style_response_200 import GetMapStyleResponse200
from .get_partners_direction import GetPartnersDirection
from .job_command import JobCommand
from .job_command_dto import JobCommandDto
from .job_counts_dto import JobCountsDto
from .job_name import JobName
from .job_settings_dto import JobSettingsDto
from .job_status_dto import JobStatusDto
from .library_response_dto import LibraryResponseDto
from .library_stats_response_dto import LibraryStatsResponseDto
from .library_type import LibraryType
from .log_level import LogLevel
from .login_credential_dto import LoginCredentialDto
from .login_response_dto import LoginResponseDto
from .logout_response_dto import LogoutResponseDto
from .map_marker_response_dto import MapMarkerResponseDto
from .map_theme import MapTheme
from .memory_lane_response_dto import MemoryLaneResponseDto
from .merge_person_dto import MergePersonDto
from .model_type import ModelType
from .o_auth_authorize_response_dto import OAuthAuthorizeResponseDto
from .o_auth_callback_dto import OAuthCallbackDto
from .o_auth_config_dto import OAuthConfigDto
from .o_auth_config_response_dto import OAuthConfigResponseDto
from .partner_response_dto import PartnerResponseDto
from .path_entity_type import PathEntityType
from .path_type import PathType
from .people_response_dto import PeopleResponseDto
from .people_update_dto import PeopleUpdateDto
from .people_update_item import PeopleUpdateItem
from .person_response_dto import PersonResponseDto
from .person_statistics_response_dto import PersonStatisticsResponseDto
from .person_update_dto import PersonUpdateDto
from .person_with_faces_response_dto import PersonWithFacesResponseDto
from .queue_status_dto import QueueStatusDto
from .reaction_level import ReactionLevel
from .reaction_type import ReactionType
from .recognition_config import RecognitionConfig
from .scan_library_dto import ScanLibraryDto
from .search_album_response_dto import SearchAlbumResponseDto
from .search_asset_response_dto import SearchAssetResponseDto
from .search_explore_item import SearchExploreItem
from .search_explore_response_dto import SearchExploreResponseDto
from .search_facet_count_response_dto import SearchFacetCountResponseDto
from .search_facet_response_dto import SearchFacetResponseDto
from .search_response_dto import SearchResponseDto
from .search_type import SearchType
from .server_config_dto import ServerConfigDto
from .server_features_dto import ServerFeaturesDto
from .server_info_response_dto import ServerInfoResponseDto
from .server_media_types_response_dto import ServerMediaTypesResponseDto
from .server_ping_response import ServerPingResponse
from .server_stats_response_dto import ServerStatsResponseDto
from .server_theme_dto import ServerThemeDto
from .server_version_response_dto import ServerVersionResponseDto
from .shared_link_create_dto import SharedLinkCreateDto
from .shared_link_edit_dto import SharedLinkEditDto
from .shared_link_response_dto import SharedLinkResponseDto
from .shared_link_type import SharedLinkType
from .sign_up_dto import SignUpDto
from .smart_info_response_dto import SmartInfoResponseDto
from .system_config_dto import SystemConfigDto
from .system_config_f_fmpeg_dto import SystemConfigFFmpegDto
from .system_config_job_dto import SystemConfigJobDto
from .system_config_library_dto import SystemConfigLibraryDto
from .system_config_library_scan_dto import SystemConfigLibraryScanDto
from .system_config_logging_dto import SystemConfigLoggingDto
from .system_config_machine_learning_dto import SystemConfigMachineLearningDto
from .system_config_map_dto import SystemConfigMapDto
from .system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
from .system_config_o_auth_dto import SystemConfigOAuthDto
from .system_config_password_login_dto import SystemConfigPasswordLoginDto
from .system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
from .system_config_storage_template_dto import SystemConfigStorageTemplateDto
from .system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
from .system_config_theme_dto import SystemConfigThemeDto
from .system_config_thumbnail_dto import SystemConfigThumbnailDto
from .system_config_trash_dto import SystemConfigTrashDto
from .tag_response_dto import TagResponseDto
from .tag_type_enum import TagTypeEnum
from .thumbnail_format import ThumbnailFormat
from .time_bucket_response_dto import TimeBucketResponseDto
from .time_bucket_size import TimeBucketSize
from .tone_mapping import ToneMapping
from .transcode_hw_accel import TranscodeHWAccel
from .transcode_policy import TranscodePolicy
from .update_album_dto import UpdateAlbumDto
from .update_asset_dto import UpdateAssetDto
from .update_library_dto import UpdateLibraryDto
from .update_partner_dto import UpdatePartnerDto
from .update_stack_parent_dto import UpdateStackParentDto
from .update_tag_dto import UpdateTagDto
from .update_user_dto import UpdateUserDto
from .usage_by_user_dto import UsageByUserDto
from .user_avatar_color import UserAvatarColor
from .user_dto import UserDto
from .user_response_dto import UserResponseDto
from .validate_access_token_response_dto import ValidateAccessTokenResponseDto
from .video_codec import VideoCodec

__all__ = (
    "ActivityCreateDto",
    "ActivityResponseDto",
    "ActivityResponseDtoType",
    "ActivityStatisticsResponseDto",
    "AddUsersDto",
    "AlbumCountResponseDto",
    "AlbumResponseDto",
    "AllJobStatusResponseDto",
    "APIKeyCreateDto",
    "APIKeyCreateResponseDto",
    "APIKeyResponseDto",
    "APIKeyUpdateDto",
    "AssetBulkDeleteDto",
    "AssetBulkUpdateDto",
    "AssetBulkUploadCheckDto",
    "AssetBulkUploadCheckItem",
    "AssetBulkUploadCheckResponseDto",
    "AssetBulkUploadCheckResult",
    "AssetBulkUploadCheckResultAction",
    "AssetBulkUploadCheckResultReason",
    "AssetFaceResponseDto",
    "AssetFaceUpdateDto",
    "AssetFaceUpdateItem",
    "AssetFaceWithoutPersonResponseDto",
    "AssetFileUploadResponseDto",
    "AssetIdsDto",
    "AssetIdsResponseDto",
    "AssetIdsResponseDtoError",
    "AssetJobName",
    "AssetJobsDto",
    "AssetOrder",
    "AssetResponseDto",
    "AssetStatsResponseDto",
    "AssetTypeEnum",
    "AudioCodec",
    "AuditDeletesResponseDto",
    "AuthDeviceResponseDto",
    "BulkIdResponseDto",
    "BulkIdResponseDtoError",
    "BulkIdsDto",
    "ChangePasswordDto",
    "CheckExistingAssetsDto",
    "CheckExistingAssetsResponseDto",
    "ClassificationConfig",
    "CLIPConfig",
    "CLIPMode",
    "Colorspace",
    "CQMode",
    "CreateAlbumDto",
    "CreateAssetDto",
    "CreateLibraryDto",
    "CreateProfileImageDto",
    "CreateProfileImageResponseDto",
    "CreateTagDto",
    "CreateUserDto",
    "CuratedLocationsResponseDto",
    "CuratedObjectsResponseDto",
    "DownloadArchiveInfo",
    "DownloadInfoDto",
    "DownloadResponseDto",
    "EntityType",
    "ExifResponseDto",
    "FaceDto",
    "FileChecksumDto",
    "FileChecksumResponseDto",
    "FileReportDto",
    "FileReportFixDto",
    "FileReportItemDto",
    "GetMapStyleResponse200",
    "GetPartnersDirection",
    "JobCommand",
    "JobCommandDto",
    "JobCountsDto",
    "JobName",
    "JobSettingsDto",
    "JobStatusDto",
    "LibraryResponseDto",
    "LibraryStatsResponseDto",
    "LibraryType",
    "LoginCredentialDto",
    "LoginResponseDto",
    "LogLevel",
    "LogoutResponseDto",
    "MapMarkerResponseDto",
    "MapTheme",
    "MemoryLaneResponseDto",
    "MergePersonDto",
    "ModelType",
    "OAuthAuthorizeResponseDto",
    "OAuthCallbackDto",
    "OAuthConfigDto",
    "OAuthConfigResponseDto",
    "PartnerResponseDto",
    "PathEntityType",
    "PathType",
    "PeopleResponseDto",
    "PeopleUpdateDto",
    "PeopleUpdateItem",
    "PersonResponseDto",
    "PersonStatisticsResponseDto",
    "PersonUpdateDto",
    "PersonWithFacesResponseDto",
    "QueueStatusDto",
    "ReactionLevel",
    "ReactionType",
    "RecognitionConfig",
    "ScanLibraryDto",
    "SearchAlbumResponseDto",
    "SearchAssetResponseDto",
    "SearchExploreItem",
    "SearchExploreResponseDto",
    "SearchFacetCountResponseDto",
    "SearchFacetResponseDto",
    "SearchResponseDto",
    "SearchType",
    "ServerConfigDto",
    "ServerFeaturesDto",
    "ServerInfoResponseDto",
    "ServerMediaTypesResponseDto",
    "ServerPingResponse",
    "ServerStatsResponseDto",
    "ServerThemeDto",
    "ServerVersionResponseDto",
    "SharedLinkCreateDto",
    "SharedLinkEditDto",
    "SharedLinkResponseDto",
    "SharedLinkType",
    "SignUpDto",
    "SmartInfoResponseDto",
    "SystemConfigDto",
    "SystemConfigFFmpegDto",
    "SystemConfigJobDto",
    "SystemConfigLibraryDto",
    "SystemConfigLibraryScanDto",
    "SystemConfigLoggingDto",
    "SystemConfigMachineLearningDto",
    "SystemConfigMapDto",
    "SystemConfigNewVersionCheckDto",
    "SystemConfigOAuthDto",
    "SystemConfigPasswordLoginDto",
    "SystemConfigReverseGeocodingDto",
    "SystemConfigStorageTemplateDto",
    "SystemConfigTemplateStorageOptionDto",
    "SystemConfigThemeDto",
    "SystemConfigThumbnailDto",
    "SystemConfigTrashDto",
    "TagResponseDto",
    "TagTypeEnum",
    "ThumbnailFormat",
    "TimeBucketResponseDto",
    "TimeBucketSize",
    "ToneMapping",
    "TranscodeHWAccel",
    "TranscodePolicy",
    "UpdateAlbumDto",
    "UpdateAssetDto",
    "UpdateLibraryDto",
    "UpdatePartnerDto",
    "UpdateStackParentDto",
    "UpdateTagDto",
    "UpdateUserDto",
    "UsageByUserDto",
    "UserAvatarColor",
    "UserDto",
    "UserResponseDto",
    "ValidateAccessTokenResponseDto",
    "VideoCodec",
)
