from enum import Enum


class EntityType(str, Enum):
    ALBUM = "ALBUM"
    ASSET = "ASSET"

    def __str__(self) -> str:
        return str(self.value)
