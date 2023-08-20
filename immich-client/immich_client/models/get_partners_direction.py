from enum import Enum


class GetPartnersDirection(str, Enum):
    SHARED_BY = "shared-by"
    SHARED_WITH = "shared-with"

    def __str__(self) -> str:
        return str(self.value)
