from enum import Enum


class PathType(str, Enum):
    ENCODED_VIDEO = "encoded_video"
    FACE = "face"
    ORIGINAL = "original"
    PREVIEW = "preview"
    PROFILE = "profile"
    SIDECAR = "sidecar"
    THUMBNAIL = "thumbnail"

    def __str__(self) -> str:
        return str(self.value)
