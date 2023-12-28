from enum import Enum


class UserAvatarColor(str, Enum):
    AMBER = "amber"
    BLUE = "blue"
    GRAY = "gray"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    PRIMARY = "primary"
    PURPLE = "purple"
    RED = "red"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
