from enum import Enum


class ActivityResponseDtoType(str, Enum):
    COMMENT = "comment"
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
