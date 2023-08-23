from enum import Enum


class AssetBulkUploadCheckResultAction(str, Enum):
    ACCEPT = "accept"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
