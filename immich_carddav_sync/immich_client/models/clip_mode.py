from enum import Enum


class CLIPMode(str, Enum):
    TEXT = "text"
    VISION = "vision"

    def __str__(self) -> str:
        return str(self.value)
