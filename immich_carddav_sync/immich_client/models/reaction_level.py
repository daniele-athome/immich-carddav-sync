from enum import Enum


class ReactionLevel(str, Enum):
    ALBUM = "album"
    ASSET = "asset"

    def __str__(self) -> str:
        return str(self.value)
