from enum import Enum


class AudioCodec(str, Enum):
    AAC = "aac"
    MP3 = "mp3"
    OPUS = "opus"

    def __str__(self) -> str:
        return str(self.value)
