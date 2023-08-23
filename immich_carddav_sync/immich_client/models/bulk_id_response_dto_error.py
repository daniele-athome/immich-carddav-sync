from enum import Enum


class BulkIdResponseDtoError(str, Enum):
    DUPLICATE = "duplicate"
    NOT_FOUND = "not_found"
    NO_PERMISSION = "no_permission"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
