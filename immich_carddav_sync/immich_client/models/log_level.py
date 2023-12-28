from enum import Enum


class LogLevel(str, Enum):
    DEBUG = "debug"
    ERROR = "error"
    FATAL = "fatal"
    LOG = "log"
    VERBOSE = "verbose"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
