from enum import Enum


class TagTypeEnum(str, Enum):
    CUSTOM = "CUSTOM"
    FACE = "FACE"
    OBJECT = "OBJECT"

    def __str__(self) -> str:
        return str(self.value)
