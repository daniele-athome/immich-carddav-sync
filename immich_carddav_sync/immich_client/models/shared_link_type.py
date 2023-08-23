from enum import Enum


class SharedLinkType(str, Enum):
    ALBUM = "ALBUM"
    INDIVIDUAL = "INDIVIDUAL"

    def __str__(self) -> str:
        return str(self.value)
