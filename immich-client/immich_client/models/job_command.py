from enum import Enum


class JobCommand(str, Enum):
    EMPTY = "empty"
    PAUSE = "pause"
    RESUME = "resume"
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
