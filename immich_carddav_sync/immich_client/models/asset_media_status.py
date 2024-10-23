from enum import Enum


class AssetMediaStatus(str, Enum):
    CREATED = "created"
    DUPLICATE = "duplicate"
    REPLACED = "replaced"

    def __str__(self) -> str:
        return str(self.value)
