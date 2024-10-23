from enum import Enum


class SearchSuggestionType(str, Enum):
    CAMERA_MAKE = "camera-make"
    CAMERA_MODEL = "camera-model"
    CITY = "city"
    COUNTRY = "country"
    STATE = "state"

    def __str__(self) -> str:
        return str(self.value)
