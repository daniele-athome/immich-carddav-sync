from enum import Enum


class AssetBulkUploadCheckResultReason(str, Enum):
    DUPLICATE = "duplicate"
    UNSUPPORTED_FORMAT = "unsupported-format"

    def __str__(self) -> str:
        return str(self.value)
