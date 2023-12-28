from enum import Enum


class AudioCodec(str, Enum):
    AAC = "aac"
    LIBOPUS = "libopus"
    MP3 = "mp3"

    def __str__(self) -> str:
        return str(self.value)
