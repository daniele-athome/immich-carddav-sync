from enum import Enum


class ThumbnailFormat(str, Enum):
    JPEG = "JPEG"
    WEBP = "WEBP"

    def __str__(self) -> str:
        return str(self.value)
