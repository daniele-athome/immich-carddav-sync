from enum import Enum


class ManualJobName(str, Enum):
    PERSON_CLEANUP = "person-cleanup"
    TAG_CLEANUP = "tag-cleanup"
    USER_CLEANUP = "user-cleanup"

    def __str__(self) -> str:
        return str(self.value)
