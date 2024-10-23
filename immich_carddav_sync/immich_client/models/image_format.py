from enum import Enum


class ImageFormat(str, Enum):
    JPEG = "jpeg"
    WEBP = "webp"

    def __str__(self) -> str:
        return str(self.value)
