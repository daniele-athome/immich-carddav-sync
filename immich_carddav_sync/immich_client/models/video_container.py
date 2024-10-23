from enum import Enum


class VideoContainer(str, Enum):
    MOV = "mov"
    MP4 = "mp4"
    OGG = "ogg"
    WEBM = "webm"

    def __str__(self) -> str:
        return str(self.value)
