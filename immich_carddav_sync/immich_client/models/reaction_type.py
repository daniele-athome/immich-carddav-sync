from enum import Enum


class ReactionType(str, Enum):
    COMMENT = "comment"
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
