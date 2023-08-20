from enum import Enum


class TranscodeHWAccel(str, Enum):
    DISABLED = "disabled"
    NVENC = "nvenc"
    QSV = "qsv"
    VAAPI = "vaapi"

    def __str__(self) -> str:
        return str(self.value)
