from enum import Enum


class VideoCodec(str, Enum):
    H264 = "h264"
    HEVC = "hevc"
    VP9 = "vp9"

    def __str__(self) -> str:
        return str(self.value)
