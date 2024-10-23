from enum import Enum


class TranscodePolicy(str, Enum):
    ALL = "all"
    BITRATE = "bitrate"
    DISABLED = "disabled"
    OPTIMAL = "optimal"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
