from enum import Enum


class AssetTypeEnum(str, Enum):
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    OTHER = "OTHER"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
