from enum import Enum


class DeleteAssetStatus(str, Enum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
