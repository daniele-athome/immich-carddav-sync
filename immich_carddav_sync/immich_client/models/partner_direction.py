from enum import Enum


class PartnerDirection(str, Enum):
    SHARED_BY = "shared-by"
    SHARED_WITH = "shared-with"

    def __str__(self) -> str:
        return str(self.value)
