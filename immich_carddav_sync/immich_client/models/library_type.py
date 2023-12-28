from enum import Enum


class LibraryType(str, Enum):
    EXTERNAL = "EXTERNAL"
    UPLOAD = "UPLOAD"

    def __str__(self) -> str:
        return str(self.value)
