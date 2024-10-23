"""Contains all the data models used in inputs/outputs"""

from .activity_create_dto import ActivityCreateDto
from .activity_response_dto import ActivityResponseDto
from .activity_statistics_response_dto import ActivityStatisticsResponseDto
from .add_users_dto import AddUsersDto
from .admin_onboarding_update_dto import AdminOnboardingUpdateDto
from .album_response_dto import AlbumResponseDto
from .album_statistics_response_dto import AlbumStatisticsResponseDto
from .album_user_add_dto import AlbumUserAddDto
from .album_user_create_dto import AlbumUserCreateDto
from .album_user_response_dto import AlbumUserResponseDto
from .album_user_role import AlbumUserRole
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
from .asset_delta_sync_dto import AssetDeltaSyncDto
from .asset_delta_sync_response_dto import AssetDeltaSyncResponseDto
from .asset_face_response_dto import AssetFaceResponseDto
from .asset_face_update_dto import AssetFaceUpdateDto
from .asset_face_update_item import AssetFaceUpdateItem
from .asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto
from .asset_full_sync_dto import AssetFullSyncDto
from .asset_ids_dto import AssetIdsDto
from .asset_ids_response_dto import AssetIdsResponseDto
from .asset_ids_response_dto_error import AssetIdsResponseDtoError
from .asset_job_name import AssetJobName
from .asset_jobs_dto import AssetJobsDto
from .asset_media_create_dto import AssetMediaCreateDto
from .asset_media_replace_dto import AssetMediaReplaceDto
from .asset_media_response_dto import AssetMediaResponseDto
from .asset_media_size import AssetMediaSize
from .asset_media_status import AssetMediaStatus
from .asset_order import AssetOrder
from .asset_response_dto import AssetResponseDto
from .asset_stack_response_dto import AssetStackResponseDto
from .asset_stats_response_dto import AssetStatsResponseDto
from .asset_type_enum import AssetTypeEnum
from .audio_codec import AudioCodec
from .audit_deletes_response_dto import AuditDeletesResponseDto
from .avatar_response import AvatarResponse
from .avatar_update import AvatarUpdate
from .bulk_id_response_dto import BulkIdResponseDto
from .bulk_id_response_dto_error import BulkIdResponseDtoError
from .bulk_ids_dto import BulkIdsDto
from .change_password_dto import ChangePasswordDto
from .check_existing_assets_dto import CheckExistingAssetsDto
from .check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from .clip_config import CLIPConfig
from .colorspace import Colorspace
from .cq_mode import CQMode
from .create_album_dto import CreateAlbumDto
from .create_library_dto import CreateLibraryDto
from .create_profile_image_dto import CreateProfileImageDto
from .create_profile_image_response_dto import CreateProfileImageResponseDto
from .download_archive_info import DownloadArchiveInfo
from .download_info_dto import DownloadInfoDto
from .download_response import DownloadResponse
from .download_response_dto import DownloadResponseDto
from .download_update import DownloadUpdate
from .duplicate_detection_config import DuplicateDetectionConfig
from .duplicate_response_dto import DuplicateResponseDto
from .email_notifications_response import EmailNotificationsResponse
from .email_notifications_update import EmailNotificationsUpdate
from .entity_type import EntityType
from .exif_response_dto import ExifResponseDto
from .face_dto import FaceDto
from .facial_recognition_config import FacialRecognitionConfig
from .file_checksum_dto import FileChecksumDto
from .file_checksum_response_dto import FileChecksumResponseDto
from .file_report_dto import FileReportDto
from .file_report_fix_dto import FileReportFixDto
from .file_report_item_dto import FileReportItemDto
from .folders_response import FoldersResponse
from .folders_update import FoldersUpdate
from .image_format import ImageFormat
from .job_command import JobCommand
from .job_command_dto import JobCommandDto
from .job_counts_dto import JobCountsDto
from .job_create_dto import JobCreateDto
from .job_name import JobName
from .job_settings_dto import JobSettingsDto
from .job_status_dto import JobStatusDto
from .library_response_dto import LibraryResponseDto
from .library_stats_response_dto import LibraryStatsResponseDto
from .license_key_dto import LicenseKeyDto
from .license_response_dto import LicenseResponseDto
from .log_level import LogLevel
from .login_credential_dto import LoginCredentialDto
from .login_response_dto import LoginResponseDto
from .logout_response_dto import LogoutResponseDto
from .manual_job_name import ManualJobName
from .map_marker_response_dto import MapMarkerResponseDto
from .map_reverse_geocode_response_dto import MapReverseGeocodeResponseDto
from .memories_response import MemoriesResponse
from .memories_update import MemoriesUpdate
from .memory_create_dto import MemoryCreateDto
from .memory_lane_response_dto import MemoryLaneResponseDto
from .memory_response_dto import MemoryResponseDto
from .memory_type import MemoryType
from .memory_update_dto import MemoryUpdateDto
from .merge_person_dto import MergePersonDto
from .metadata_search_dto import MetadataSearchDto
from .o_auth_authorize_response_dto import OAuthAuthorizeResponseDto
from .o_auth_callback_dto import OAuthCallbackDto
from .o_auth_config_dto import OAuthConfigDto
from .on_this_day_dto import OnThisDayDto
from .partner_direction import PartnerDirection
from .partner_response_dto import PartnerResponseDto
from .path_entity_type import PathEntityType
from .path_type import PathType
from .people_response import PeopleResponse
from .people_response_dto import PeopleResponseDto
from .people_update import PeopleUpdate
from .people_update_dto import PeopleUpdateDto
from .people_update_item import PeopleUpdateItem
from .permission import Permission
from .person_create_dto import PersonCreateDto
from .person_response_dto import PersonResponseDto
from .person_statistics_response_dto import PersonStatisticsResponseDto
from .person_update_dto import PersonUpdateDto
from .person_with_faces_response_dto import PersonWithFacesResponseDto
from .places_response_dto import PlacesResponseDto
from .purchase_response import PurchaseResponse
from .purchase_update import PurchaseUpdate
from .queue_status_dto import QueueStatusDto
from .random_search_dto import RandomSearchDto
from .ratings_response import RatingsResponse
from .ratings_update import RatingsUpdate
from .reaction_level import ReactionLevel
from .reaction_type import ReactionType
from .reverse_geocoding_state_response_dto import ReverseGeocodingStateResponseDto
from .search_album_response_dto import SearchAlbumResponseDto
from .search_asset_response_dto import SearchAssetResponseDto
from .search_explore_item import SearchExploreItem
from .search_explore_response_dto import SearchExploreResponseDto
from .search_facet_count_response_dto import SearchFacetCountResponseDto
from .search_facet_response_dto import SearchFacetResponseDto
from .search_response_dto import SearchResponseDto
from .search_suggestion_type import SearchSuggestionType
from .server_about_response_dto import ServerAboutResponseDto
from .server_config_dto import ServerConfigDto
from .server_features_dto import ServerFeaturesDto
from .server_media_types_response_dto import ServerMediaTypesResponseDto
from .server_ping_response import ServerPingResponse
from .server_stats_response_dto import ServerStatsResponseDto
from .server_storage_response_dto import ServerStorageResponseDto
from .server_theme_dto import ServerThemeDto
from .server_version_history_response_dto import ServerVersionHistoryResponseDto
from .server_version_response_dto import ServerVersionResponseDto
from .session_response_dto import SessionResponseDto
from .shared_link_create_dto import SharedLinkCreateDto
from .shared_link_edit_dto import SharedLinkEditDto
from .shared_link_response_dto import SharedLinkResponseDto
from .shared_link_type import SharedLinkType
from .sign_up_dto import SignUpDto
from .smart_info_response_dto import SmartInfoResponseDto
from .smart_search_dto import SmartSearchDto
from .source_type import SourceType
from .stack_create_dto import StackCreateDto
from .stack_response_dto import StackResponseDto
from .stack_update_dto import StackUpdateDto
from .system_config_dto import SystemConfigDto
from .system_config_f_fmpeg_dto import SystemConfigFFmpegDto
from .system_config_faces_dto import SystemConfigFacesDto
from .system_config_generated_image_dto import SystemConfigGeneratedImageDto
from .system_config_image_dto import SystemConfigImageDto
from .system_config_job_dto import SystemConfigJobDto
from .system_config_library_dto import SystemConfigLibraryDto
from .system_config_library_scan_dto import SystemConfigLibraryScanDto
from .system_config_library_watch_dto import SystemConfigLibraryWatchDto
from .system_config_logging_dto import SystemConfigLoggingDto
from .system_config_machine_learning_dto import SystemConfigMachineLearningDto
from .system_config_map_dto import SystemConfigMapDto
from .system_config_metadata_dto import SystemConfigMetadataDto
from .system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
from .system_config_notifications_dto import SystemConfigNotificationsDto
from .system_config_o_auth_dto import SystemConfigOAuthDto
from .system_config_password_login_dto import SystemConfigPasswordLoginDto
from .system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
from .system_config_server_dto import SystemConfigServerDto
from .system_config_smtp_dto import SystemConfigSmtpDto
from .system_config_smtp_transport_dto import SystemConfigSmtpTransportDto
from .system_config_storage_template_dto import SystemConfigStorageTemplateDto
from .system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
from .system_config_theme_dto import SystemConfigThemeDto
from .system_config_trash_dto import SystemConfigTrashDto
from .system_config_user_dto import SystemConfigUserDto
from .tag_bulk_assets_dto import TagBulkAssetsDto
from .tag_bulk_assets_response_dto import TagBulkAssetsResponseDto
from .tag_create_dto import TagCreateDto
from .tag_response_dto import TagResponseDto
from .tag_update_dto import TagUpdateDto
from .tag_upsert_dto import TagUpsertDto
from .tags_response import TagsResponse
from .tags_update import TagsUpdate
from .test_email_response_dto import TestEmailResponseDto
from .time_bucket_response_dto import TimeBucketResponseDto
from .time_bucket_size import TimeBucketSize
from .tone_mapping import ToneMapping
from .transcode_hw_accel import TranscodeHWAccel
from .transcode_policy import TranscodePolicy
from .trash_response_dto import TrashResponseDto
from .update_album_dto import UpdateAlbumDto
from .update_album_user_dto import UpdateAlbumUserDto
from .update_asset_dto import UpdateAssetDto
from .update_library_dto import UpdateLibraryDto
from .update_partner_dto import UpdatePartnerDto
from .usage_by_user_dto import UsageByUserDto
from .user_admin_create_dto import UserAdminCreateDto
from .user_admin_delete_dto import UserAdminDeleteDto
from .user_admin_response_dto import UserAdminResponseDto
from .user_admin_update_dto import UserAdminUpdateDto
from .user_avatar_color import UserAvatarColor
from .user_license import UserLicense
from .user_preferences_response_dto import UserPreferencesResponseDto
from .user_preferences_update_dto import UserPreferencesUpdateDto
from .user_response_dto import UserResponseDto
from .user_status import UserStatus
from .user_update_me_dto import UserUpdateMeDto
from .validate_access_token_response_dto import ValidateAccessTokenResponseDto
from .validate_library_dto import ValidateLibraryDto
from .validate_library_import_path_response_dto import ValidateLibraryImportPathResponseDto
from .validate_library_response_dto import ValidateLibraryResponseDto
from .video_codec import VideoCodec
from .video_container import VideoContainer

__all__ = (
    "ActivityCreateDto",
    "ActivityResponseDto",
    "ActivityStatisticsResponseDto",
    "AddUsersDto",
    "AdminOnboardingUpdateDto",
    "AlbumResponseDto",
    "AlbumStatisticsResponseDto",
    "AlbumUserAddDto",
    "AlbumUserCreateDto",
    "AlbumUserResponseDto",
    "AlbumUserRole",
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
    "AssetDeltaSyncDto",
    "AssetDeltaSyncResponseDto",
    "AssetFaceResponseDto",
    "AssetFaceUpdateDto",
    "AssetFaceUpdateItem",
    "AssetFaceWithoutPersonResponseDto",
    "AssetFullSyncDto",
    "AssetIdsDto",
    "AssetIdsResponseDto",
    "AssetIdsResponseDtoError",
    "AssetJobName",
    "AssetJobsDto",
    "AssetMediaCreateDto",
    "AssetMediaReplaceDto",
    "AssetMediaResponseDto",
    "AssetMediaSize",
    "AssetMediaStatus",
    "AssetOrder",
    "AssetResponseDto",
    "AssetStackResponseDto",
    "AssetStatsResponseDto",
    "AssetTypeEnum",
    "AudioCodec",
    "AuditDeletesResponseDto",
    "AvatarResponse",
    "AvatarUpdate",
    "BulkIdResponseDto",
    "BulkIdResponseDtoError",
    "BulkIdsDto",
    "ChangePasswordDto",
    "CheckExistingAssetsDto",
    "CheckExistingAssetsResponseDto",
    "CLIPConfig",
    "Colorspace",
    "CQMode",
    "CreateAlbumDto",
    "CreateLibraryDto",
    "CreateProfileImageDto",
    "CreateProfileImageResponseDto",
    "DownloadArchiveInfo",
    "DownloadInfoDto",
    "DownloadResponse",
    "DownloadResponseDto",
    "DownloadUpdate",
    "DuplicateDetectionConfig",
    "DuplicateResponseDto",
    "EmailNotificationsResponse",
    "EmailNotificationsUpdate",
    "EntityType",
    "ExifResponseDto",
    "FaceDto",
    "FacialRecognitionConfig",
    "FileChecksumDto",
    "FileChecksumResponseDto",
    "FileReportDto",
    "FileReportFixDto",
    "FileReportItemDto",
    "FoldersResponse",
    "FoldersUpdate",
    "ImageFormat",
    "JobCommand",
    "JobCommandDto",
    "JobCountsDto",
    "JobCreateDto",
    "JobName",
    "JobSettingsDto",
    "JobStatusDto",
    "LibraryResponseDto",
    "LibraryStatsResponseDto",
    "LicenseKeyDto",
    "LicenseResponseDto",
    "LoginCredentialDto",
    "LoginResponseDto",
    "LogLevel",
    "LogoutResponseDto",
    "ManualJobName",
    "MapMarkerResponseDto",
    "MapReverseGeocodeResponseDto",
    "MemoriesResponse",
    "MemoriesUpdate",
    "MemoryCreateDto",
    "MemoryLaneResponseDto",
    "MemoryResponseDto",
    "MemoryType",
    "MemoryUpdateDto",
    "MergePersonDto",
    "MetadataSearchDto",
    "OAuthAuthorizeResponseDto",
    "OAuthCallbackDto",
    "OAuthConfigDto",
    "OnThisDayDto",
    "PartnerDirection",
    "PartnerResponseDto",
    "PathEntityType",
    "PathType",
    "PeopleResponse",
    "PeopleResponseDto",
    "PeopleUpdate",
    "PeopleUpdateDto",
    "PeopleUpdateItem",
    "Permission",
    "PersonCreateDto",
    "PersonResponseDto",
    "PersonStatisticsResponseDto",
    "PersonUpdateDto",
    "PersonWithFacesResponseDto",
    "PlacesResponseDto",
    "PurchaseResponse",
    "PurchaseUpdate",
    "QueueStatusDto",
    "RandomSearchDto",
    "RatingsResponse",
    "RatingsUpdate",
    "ReactionLevel",
    "ReactionType",
    "ReverseGeocodingStateResponseDto",
    "SearchAlbumResponseDto",
    "SearchAssetResponseDto",
    "SearchExploreItem",
    "SearchExploreResponseDto",
    "SearchFacetCountResponseDto",
    "SearchFacetResponseDto",
    "SearchResponseDto",
    "SearchSuggestionType",
    "ServerAboutResponseDto",
    "ServerConfigDto",
    "ServerFeaturesDto",
    "ServerMediaTypesResponseDto",
    "ServerPingResponse",
    "ServerStatsResponseDto",
    "ServerStorageResponseDto",
    "ServerThemeDto",
    "ServerVersionHistoryResponseDto",
    "ServerVersionResponseDto",
    "SessionResponseDto",
    "SharedLinkCreateDto",
    "SharedLinkEditDto",
    "SharedLinkResponseDto",
    "SharedLinkType",
    "SignUpDto",
    "SmartInfoResponseDto",
    "SmartSearchDto",
    "SourceType",
    "StackCreateDto",
    "StackResponseDto",
    "StackUpdateDto",
    "SystemConfigDto",
    "SystemConfigFacesDto",
    "SystemConfigFFmpegDto",
    "SystemConfigGeneratedImageDto",
    "SystemConfigImageDto",
    "SystemConfigJobDto",
    "SystemConfigLibraryDto",
    "SystemConfigLibraryScanDto",
    "SystemConfigLibraryWatchDto",
    "SystemConfigLoggingDto",
    "SystemConfigMachineLearningDto",
    "SystemConfigMapDto",
    "SystemConfigMetadataDto",
    "SystemConfigNewVersionCheckDto",
    "SystemConfigNotificationsDto",
    "SystemConfigOAuthDto",
    "SystemConfigPasswordLoginDto",
    "SystemConfigReverseGeocodingDto",
    "SystemConfigServerDto",
    "SystemConfigSmtpDto",
    "SystemConfigSmtpTransportDto",
    "SystemConfigStorageTemplateDto",
    "SystemConfigTemplateStorageOptionDto",
    "SystemConfigThemeDto",
    "SystemConfigTrashDto",
    "SystemConfigUserDto",
    "TagBulkAssetsDto",
    "TagBulkAssetsResponseDto",
    "TagCreateDto",
    "TagResponseDto",
    "TagsResponse",
    "TagsUpdate",
    "TagUpdateDto",
    "TagUpsertDto",
    "TestEmailResponseDto",
    "TimeBucketResponseDto",
    "TimeBucketSize",
    "ToneMapping",
    "TranscodeHWAccel",
    "TranscodePolicy",
    "TrashResponseDto",
    "UpdateAlbumDto",
    "UpdateAlbumUserDto",
    "UpdateAssetDto",
    "UpdateLibraryDto",
    "UpdatePartnerDto",
    "UsageByUserDto",
    "UserAdminCreateDto",
    "UserAdminDeleteDto",
    "UserAdminResponseDto",
    "UserAdminUpdateDto",
    "UserAvatarColor",
    "UserLicense",
    "UserPreferencesResponseDto",
    "UserPreferencesUpdateDto",
    "UserResponseDto",
    "UserStatus",
    "UserUpdateMeDto",
    "ValidateAccessTokenResponseDto",
    "ValidateLibraryDto",
    "ValidateLibraryImportPathResponseDto",
    "ValidateLibraryResponseDto",
    "VideoCodec",
    "VideoContainer",
)
