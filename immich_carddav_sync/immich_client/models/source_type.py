from enum import Enum


class SourceType(str, Enum):
    EXIF = "exif"
    MACHINE_LEARNING = "machine-learning"

    def __str__(self) -> str:
        return str(self.value)
