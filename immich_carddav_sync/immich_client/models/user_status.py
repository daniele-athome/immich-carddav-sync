from enum import Enum


class UserStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    REMOVING = "removing"

    def __str__(self) -> str:
        return str(self.value)
