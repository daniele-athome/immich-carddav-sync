from enum import Enum


class AssetJobName(str, Enum):
    REFRESH_FACES = "refresh-faces"
    REFRESH_METADATA = "refresh-metadata"
    REGENERATE_THUMBNAIL = "regenerate-thumbnail"
    TRANSCODE_VIDEO = "transcode-video"

    def __str__(self) -> str:
        return str(self.value)
