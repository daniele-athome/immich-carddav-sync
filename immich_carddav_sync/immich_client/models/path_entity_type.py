from enum import Enum


class PathEntityType(str, Enum):
    ASSET = "asset"
    PERSON = "person"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
