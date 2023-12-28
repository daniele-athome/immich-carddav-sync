from enum import Enum


class CQMode(str, Enum):
    AUTO = "auto"
    CQP = "cqp"
    ICQ = "icq"

    def __str__(self) -> str:
        return str(self.value)
