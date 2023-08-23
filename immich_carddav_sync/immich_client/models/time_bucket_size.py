from enum import Enum


class TimeBucketSize(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"

    def __str__(self) -> str:
        return str(self.value)
