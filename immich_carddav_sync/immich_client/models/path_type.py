from enum import Enum


class PathType(str, Enum):
    ENCODED_VIDEO = "encoded_video"
    FACE = "face"
    JPEG_THUMBNAIL = "jpeg_thumbnail"
    ORIGINAL = "original"
    PROFILE = "profile"
    SIDECAR = "sidecar"
    WEBP_THUMBNAIL = "webp_thumbnail"

    def __str__(self) -> str:
        return str(self.value)
