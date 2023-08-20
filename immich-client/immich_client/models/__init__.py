""" Contains all the data models used in inputs/outputs """

from .add_users_dto import AddUsersDto
from .admin_signup_response_dto import AdminSignupResponseDto
from .album_count_response_dto import AlbumCountResponseDto
from .album_response_dto import AlbumResponseDto
from .all_job_status_response_dto import AllJobStatusResponseDto
from .api_key_create_dto import APIKeyCreateDto
from .api_key_create_response_dto import APIKeyCreateResponseDto
from .api_key_response_dto import APIKeyResponseDto
from .api_key_update_dto import APIKeyUpdateDto
from .asset_bulk_update_dto import AssetBulkUpdateDto
from .asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from .asset_bulk_upload_check_item import AssetBulkUploadCheckItem
from .asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto
from .asset_bulk_upload_check_result import AssetBulkUploadCheckResult
from .asset_bulk_upload_check_result_action import AssetBulkUploadCheckResultAction
from .asset_bulk_upload_check_result_reason import AssetBulkUploadCheckResultReason
from .asset_file_upload_response_dto import AssetFileUploadResponseDto
from .asset_ids_dto import AssetIdsDto
from .asset_ids_response_dto import AssetIdsResponseDto
from .asset_ids_response_dto_error import AssetIdsResponseDtoError
from .asset_job_name import AssetJobName
from .asset_jobs_dto import AssetJobsDto
from .asset_response_dto import AssetResponseDto
from .asset_stats_response_dto import AssetStatsResponseDto
from .asset_type_enum import AssetTypeEnum
from .audio_codec import AudioCodec
from .auth_device_response_dto import AuthDeviceResponseDto
from .bulk_id_response_dto import BulkIdResponseDto
from .bulk_id_response_dto_error import BulkIdResponseDtoError
from .bulk_ids_dto import BulkIdsDto
from .change_password_dto import ChangePasswordDto
from .check_duplicate_asset_dto import CheckDuplicateAssetDto
from .check_duplicate_asset_response_dto import CheckDuplicateAssetResponseDto
from .check_existing_assets_dto import CheckExistingAssetsDto
from .check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from .create_album_dto import CreateAlbumDto
from .create_asset_dto import CreateAssetDto
from .create_profile_image_dto import CreateProfileImageDto
from .create_profile_image_response_dto import CreateProfileImageResponseDto
from .create_tag_dto import CreateTagDto
from .create_user_dto import CreateUserDto
from .curated_locations_response_dto import CuratedLocationsResponseDto
from .curated_objects_response_dto import CuratedObjectsResponseDto
from .delete_asset_dto import DeleteAssetDto
from .delete_asset_response_dto import DeleteAssetResponseDto
from .delete_asset_status import DeleteAssetStatus
from .download_archive_info import DownloadArchiveInfo
from .download_info_dto import DownloadInfoDto
from .download_response_dto import DownloadResponseDto
from .exif_response_dto import ExifResponseDto
from .get_partners_direction import GetPartnersDirection
from .get_profile_image_response_200 import GetProfileImageResponse200
from .import_asset_dto import ImportAssetDto
from .job_command import JobCommand
from .job_command_dto import JobCommandDto
from .job_counts_dto import JobCountsDto
from .job_name import JobName
from .job_settings_dto import JobSettingsDto
from .job_status_dto import JobStatusDto
from .login_credential_dto import LoginCredentialDto
from .login_response_dto import LoginResponseDto
from .logout_response_dto import LogoutResponseDto
from .map_marker_response_dto import MapMarkerResponseDto
from .memory_lane_response_dto import MemoryLaneResponseDto
from .merge_person_dto import MergePersonDto
from .o_auth_callback_dto import OAuthCallbackDto
from .o_auth_config_dto import OAuthConfigDto
from .o_auth_config_response_dto import OAuthConfigResponseDto
from .people_response_dto import PeopleResponseDto
from .people_update_dto import PeopleUpdateDto
from .people_update_item import PeopleUpdateItem
from .person_response_dto import PersonResponseDto
from .person_update_dto import PersonUpdateDto
from .queue_status_dto import QueueStatusDto
from .search_album_response_dto import SearchAlbumResponseDto
from .search_asset_dto import SearchAssetDto
from .search_asset_response_dto import SearchAssetResponseDto
from .search_config_response_dto import SearchConfigResponseDto
from .search_explore_item import SearchExploreItem
from .search_explore_response_dto import SearchExploreResponseDto
from .search_facet_count_response_dto import SearchFacetCountResponseDto
from .search_facet_response_dto import SearchFacetResponseDto
from .search_response_dto import SearchResponseDto
from .search_type import SearchType
from .server_features_dto import ServerFeaturesDto
from .server_info_response_dto import ServerInfoResponseDto
from .server_media_types_response_dto import ServerMediaTypesResponseDto
from .server_ping_response import ServerPingResponse
from .server_stats_response_dto import ServerStatsResponseDto
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
from .system_config_o_auth_dto import SystemConfigOAuthDto
from .system_config_password_login_dto import SystemConfigPasswordLoginDto
from .system_config_storage_template_dto import SystemConfigStorageTemplateDto
from .system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
from .system_config_thumbnail_dto import SystemConfigThumbnailDto
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
from .update_tag_dto import UpdateTagDto
from .update_user_dto import UpdateUserDto
from .usage_by_user_dto import UsageByUserDto
from .user_count_response_dto import UserCountResponseDto
from .user_response_dto import UserResponseDto
from .validate_access_token_response_dto import ValidateAccessTokenResponseDto
from .video_codec import VideoCodec

__all__ = (
    "AddUsersDto",
    "AdminSignupResponseDto",
    "AlbumCountResponseDto",
    "AlbumResponseDto",
    "AllJobStatusResponseDto",
    "APIKeyCreateDto",
    "APIKeyCreateResponseDto",
    "APIKeyResponseDto",
    "APIKeyUpdateDto",
    "AssetBulkUpdateDto",
    "AssetBulkUploadCheckDto",
    "AssetBulkUploadCheckItem",
    "AssetBulkUploadCheckResponseDto",
    "AssetBulkUploadCheckResult",
    "AssetBulkUploadCheckResultAction",
    "AssetBulkUploadCheckResultReason",
    "AssetFileUploadResponseDto",
    "AssetIdsDto",
    "AssetIdsResponseDto",
    "AssetIdsResponseDtoError",
    "AssetJobName",
    "AssetJobsDto",
    "AssetResponseDto",
    "AssetStatsResponseDto",
    "AssetTypeEnum",
    "AudioCodec",
    "AuthDeviceResponseDto",
    "BulkIdResponseDto",
    "BulkIdResponseDtoError",
    "BulkIdsDto",
    "ChangePasswordDto",
    "CheckDuplicateAssetDto",
    "CheckDuplicateAssetResponseDto",
    "CheckExistingAssetsDto",
    "CheckExistingAssetsResponseDto",
    "CreateAlbumDto",
    "CreateAssetDto",
    "CreateProfileImageDto",
    "CreateProfileImageResponseDto",
    "CreateTagDto",
    "CreateUserDto",
    "CuratedLocationsResponseDto",
    "CuratedObjectsResponseDto",
    "DeleteAssetDto",
    "DeleteAssetResponseDto",
    "DeleteAssetStatus",
    "DownloadArchiveInfo",
    "DownloadInfoDto",
    "DownloadResponseDto",
    "ExifResponseDto",
    "GetPartnersDirection",
    "GetProfileImageResponse200",
    "ImportAssetDto",
    "JobCommand",
    "JobCommandDto",
    "JobCountsDto",
    "JobName",
    "JobSettingsDto",
    "JobStatusDto",
    "LoginCredentialDto",
    "LoginResponseDto",
    "LogoutResponseDto",
    "MapMarkerResponseDto",
    "MemoryLaneResponseDto",
    "MergePersonDto",
    "OAuthCallbackDto",
    "OAuthConfigDto",
    "OAuthConfigResponseDto",
    "PeopleResponseDto",
    "PeopleUpdateDto",
    "PeopleUpdateItem",
    "PersonResponseDto",
    "PersonUpdateDto",
    "QueueStatusDto",
    "SearchAlbumResponseDto",
    "SearchAssetDto",
    "SearchAssetResponseDto",
    "SearchConfigResponseDto",
    "SearchExploreItem",
    "SearchExploreResponseDto",
    "SearchFacetCountResponseDto",
    "SearchFacetResponseDto",
    "SearchResponseDto",
    "SearchType",
    "ServerFeaturesDto",
    "ServerInfoResponseDto",
    "ServerMediaTypesResponseDto",
    "ServerPingResponse",
    "ServerStatsResponseDto",
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
    "SystemConfigOAuthDto",
    "SystemConfigPasswordLoginDto",
    "SystemConfigStorageTemplateDto",
    "SystemConfigTemplateStorageOptionDto",
    "SystemConfigThumbnailDto",
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
    "UpdateTagDto",
    "UpdateUserDto",
    "UsageByUserDto",
    "UserCountResponseDto",
    "UserResponseDto",
    "ValidateAccessTokenResponseDto",
    "VideoCodec",
)
