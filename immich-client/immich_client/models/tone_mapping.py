from enum import Enum


class ToneMapping(str, Enum):
    DISABLED = "disabled"
    HABLE = "hable"
    MOBIUS = "mobius"
    REINHARD = "reinhard"

    def __str__(self) -> str:
        return str(self.value)
