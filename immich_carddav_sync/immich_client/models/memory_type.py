from enum import Enum


class MemoryType(str, Enum):
    ON_THIS_DAY = "on_this_day"

    def __str__(self) -> str:
        return str(self.value)
