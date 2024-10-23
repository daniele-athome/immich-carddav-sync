from enum import Enum


class Colorspace(str, Enum):
    P3 = "p3"
    SRGB = "srgb"

    def __str__(self) -> str:
        return str(self.value)
