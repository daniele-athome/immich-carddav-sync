from enum import Enum


class AssetIdsResponseDtoError(str, Enum):
    DUPLICATE = "duplicate"
    NOT_FOUND = "not_found"
    NO_PERMISSION = "no_permission"

    def __str__(self) -> str:
        return str(self.value)
